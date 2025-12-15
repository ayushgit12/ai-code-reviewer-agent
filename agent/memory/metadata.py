import sqlite3
from agent.config import DB_PATH


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT,
        symbol TEXT,
        start_line INTEGER,
        end_line INTEGER,
        code TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_chunks(chunks):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for c in chunks:
        cur.execute("""
        INSERT INTO chunks (file_path, symbol, start_line, end_line, code)
        VALUES (?, ?, ?, ?, ?)
        """, (
            c["file_path"],
            c["symbol"],
            c["start_line"],
            c["end_line"],
            c["code"]
        ))

    conn.commit()
    conn.close()


def get_chunks_by_ids(ids):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    placeholders = ",".join("?" for _ in ids)
    query = f"""
    SELECT file_path, symbol, start_line, end_line, code
    FROM chunks
    WHERE id IN ({placeholders})
    """

    cur.execute(query, ids)
    rows = cur.fetchall()

    conn.close()

    return rows

