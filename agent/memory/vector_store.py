import faiss


class VectorStore:
    def __init__(self, dim: int, store_path):
        self.dim = dim
        self.store_path = store_path
        self.index = faiss.IndexFlatL2(dim)

    def add(self, vectors):
        self.index.add(vectors)

    def search(self, query_vector, top_k=5):
        distances, indices = self.index.search(query_vector, top_k)
        return distances[0], indices[0]

    def save(self):
        faiss.write_index(self.index, str(self.store_path))

    def load(self):
        if self.store_path.exists():
            self.index = faiss.read_index(str(self.store_path))
