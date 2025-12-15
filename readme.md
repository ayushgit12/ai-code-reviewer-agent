# 🧠 Autonomous Codebase Intelligence Agent

An **offline, agentic AI system** that understands codebases, answers architecture and logic questions, and stays up-to-date automatically using **local LLMs and vector memory** — without third-party APIs.

---

## 🚀 Overview

Large codebases are hard to understand, navigate, and maintain.  
This project builds an **autonomous code intelligence agent** that:

- Ingests local or GitHub-hosted codebases
- Chunks code into semantic units (functions/classes)
- Stores embeddings in FAISS for meaning-based retrieval
- Uses an LLM to reason **only over retrieved code**
- Automatically re-indexes when files change

Everything runs **fully offline**.

---

## ✨ Key Features

- **Semantic Code Understanding**  
  Function- and class-level chunking with FAISS-based retrieval.

- **Grounded AI Reasoning**  
  Retrieval-augmented generation (RAG) to avoid hallucinations.

- **Autonomous Updates**  
  File watcher detects changes and refreshes embeddings automatically.

- **Offline & Self-Hosted**  
  Local LLMs (Ollama + LLaMA 3), no APIs or tokens required.

- **GitHub Support**  
  Accepts GitHub URLs via `git clone` (no GitHub API).

---

## 🏗️ Architecture

```text
Codebase → Ingestion → Chunking → Embeddings
        → FAISS + Metadata → Retrieval → LLM Reasoning
```

Autonomous mode adds:
```text
File Watcher → Re-Indexing
```

Tech Stack :
- Python 3.10+
- LLM: LLaMA 3 (Ollama, quantized)
- Embeddings: Sentence Transformers (MiniLM)
- Vector DB: FAISS 
- Metadata: SQLite
- Agent Runtime: watchdog

## How to run this :

Clone the repository:
```bash
git clone <your-repo-url>
cd <ai-code-reviewer-agent>
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```


Install dependencies:
```bash
pip install -r requirements.txt
```

This installs FAISS, sentence-transformers, watchdog, the Ollama Python client, and other required libraries.

Pull the LLM model (one-time setup):
```bash
ollama pull llama3:8b-instruct-q4_K_M
```


## How to run Different methods:

**Index a local project**
```bash
python -m agent.cli index <path-to-your-project>
```

**Index a GitHub repository**
```bash
python -m agent.cli index <repo-url>
```

**Query the codebase**
```bash
python -m agent.cli query "How does authentication work?"
```

**Run in autonomous mode**
```bash
python -m agent.cli watch ./my_project
```

