from db import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id TEXT UNIQUE,
        title TEXT,
        module TEXT,
        submodule TEXT,
        version TEXT,
        status TEXT,
        effective_date TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER,
        chunk_index INTEGER,
        chunk_text TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS query_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        retrieved_docs TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
