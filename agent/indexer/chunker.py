import ast
from typing import List, Dict


def chunk_python_code(code: str, file_path: str) -> List[Dict]:
    """
    Chunk Python code into functions and classes using AST.
    """
    chunks = []

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return chunks

    lines = code.splitlines()

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            start_line = node.lineno - 1
            end_line = getattr(node, "end_lineno", None)

            if end_line is None:
                continue

            chunk_code = "\n".join(lines[start_line:end_line])

            chunks.append({
                "file_path": file_path,
                "symbol": node.name,
                "type": node.__class__.__name__,
                "start_line": start_line + 1,
                "end_line": end_line,
                "code": chunk_code
            })

    return chunks


def chunk_fallback(code: str, file_path: str, max_lines: int = 50):
    """
    Chunk code into fixed-size blocks (fallback).
    """
    lines = code.splitlines()
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk = "\n".join(lines[i:i + max_lines])

        chunks.append({
            "file_path": file_path,
            "symbol": f"block_{i // max_lines}",
            "type": "block",
            "start_line": i + 1,
            "end_line": min(i + max_lines, len(lines)),
            "code": chunk
        })

    return chunks


def chunk_code(file_obj):
    code = file_obj["content"]
    path = file_obj["file_path"]

    if path.endswith(".py"):
        chunks = chunk_python_code(code, path)
        if chunks:
            return chunks

    # fallback
    return chunk_fallback(code, path)
