from pathlib import Path
from agent.config import SUPPORTED_EXTENSIONS, EXCLUDED_DIRS


def discover_code_files(root_path: str):
    """
    Recursively discover supported code files,
    excluding unwanted directories.
    """
    root = Path(root_path).resolve()
    code_files = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        # Skip excluded directories
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue

        # Check extension
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            code_files.append(path)

    return code_files


def read_code_file(file_path: Path):
    """
    Safely read a code file.
    """
    try:
        return file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"[WARN] Could not read {file_path}: {e}")
        return None


def ingest_codebase(root_path: str):
    """
    Ingest a codebase and return structured file objects.
    """
    files = discover_code_files(root_path)
    ingested = []

    for file_path in files:
        content = read_code_file(file_path)
        if not content:
            continue

        ingested.append({
            "file_path": str(file_path),
            "extension": file_path.suffix,
            "content": content
        })

    return ingested
