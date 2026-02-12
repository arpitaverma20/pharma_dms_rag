from db import get_connection

def get_approved_latest(module=None):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT id, filename, module, version, effective_date, content
    FROM documents
    WHERE status = 'Approved'
    """
    params = []

    if module:
        query += " AND module = ?"
        params.append(module)

    query += " ORDER BY version DESC"

    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()

    return rows
