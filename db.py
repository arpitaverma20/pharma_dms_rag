import sqlite3

DB_NAME = "pharma_dms.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        module TEXT,
        submodule TEXT,
        content TEXT,
        status TEXT,              -- Approved / Draft
        version INTEGER,           -- 1, 2, 3
        effective_date TEXT        -- YYYY-MM-DD
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS query_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        retrieved_docs TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
    print("Database & tables created")

if __name__ == "__main__":
    create_tables()
