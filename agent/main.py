from agent.indexer.file_loader import ingest_codebase
from agent.indexer.chunker import chunk_code
from agent.memory.embeddings import embed_texts
from agent.memory.vector_store import VectorStore
from agent.memory.metadata import init_db, insert_chunks
from agent.config import VECTOR_STORE_DIR
from agent.memory.metadata import get_chunks_by_ids
import numpy as np
from pathlib import Path
from agent.utils.git_utils import is_github_url, clone_repo



def build_context(chunks):
    context = ""
    for c in chunks:
        file_path, symbol, start, end, code = c
        context += f"\nFILE: {file_path}\n"
        context += f"SYMBOL: {symbol} (lines {start}-{end})\n"
        context += f"{code}\n"
        context += "-" * 40 + "\n"
    return context


def index_codebase(path: str):
    if is_github_url(path):
        repos_dir = Path("data/repos")
        path = clone_repo(path, repos_dir)

    print(f"[INFO] Indexing codebase at: {path}")

    # IMPORTANT: convert Path → str for rest of pipeline
    path = str(path)

    files = ingest_codebase(path)
    all_chunks = []

    for file_obj in files:
        all_chunks.extend(chunk_code(file_obj))

    print(f"[INFO] Created {len(all_chunks)} chunks")

    # init DB
    init_db()

    # embed
    texts = [c["code"] for c in all_chunks]
    embeddings = embed_texts(texts)
    embeddings = np.array(embeddings).astype("float32")

    # FAISS
    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
    index_path = VECTOR_STORE_DIR / "index.faiss"

    store = VectorStore(dim=embeddings.shape[1], store_path=index_path)
    store.add(embeddings)
    store.save()

    # metadata
    insert_chunks(all_chunks)

    print("[INFO] Embeddings stored in FAISS")



from agent.agents.llm import ask_llm
from agent.memory.metadata import get_chunks_by_ids
from agent.memory.embeddings import embed_texts
from agent.memory.vector_store import VectorStore
from agent.config import VECTOR_STORE_DIR
import numpy as np


def query_codebase(question: str):
    print(f"[INFO] Query: {question}")

    # Embed question
    query_embedding = embed_texts([question])
    query_embedding = np.array(query_embedding).astype("float32")

    # Load FAISS
    index_path = VECTOR_STORE_DIR / "index.faiss"
    store = VectorStore(dim=query_embedding.shape[1], store_path=index_path)
    store.load()

    # Search
    distances, indices = store.search(query_embedding, top_k=5)
    chunk_ids = [int(i + 1) for i in indices if i >= 0]

    chunks = get_chunks_by_ids(chunk_ids)

    if not chunks:
        print("No relevant code found.")
        return

    # Build context
    context = build_context(chunks)

    # Ask LLM
    answer = ask_llm(question, context)

    print("\n🧠 ANSWER:\n")
    print(answer)
