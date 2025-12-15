from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"
DB_PATH = DATA_DIR / "metadata.db"

SUPPORTED_EXTENSIONS = [
    ".py", ".js", ".ts", ".java", ".cpp", ".c", ".h"
]

EXCLUDED_DIRS = {
    ".git", "node_modules", "__pycache__", "build", "dist", ".venv"
}
