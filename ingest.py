import os
from db import get_connection
from pypdf import PdfReader

DOCS_PATH = "data/documents"

def read_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def ingest_documents():
    conn = get_connection()
    cur = conn.cursor()

    found_any = False

    for root, _, files in os.walk(DOCS_PATH):
        print("Scanning:", root)

        for file in files:
            print("Found file:", file)

            if file.endswith(".pdf"):
                found_any = True
                path = os.path.join(root, file)
                print("Ingesting:", path)

                content = read_pdf(path)
                module = os.path.basename(root)

                cur.execute("""
                INSERT INTO documents
                (filename, module, submodule, status, version, effective_date, content)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    file,
                    module,
                    None,
                    "Approved",
                    1,
                    "2025-01-01",
                    content
                ))

    conn.commit()
    conn.close()

    if not found_any:
        print("❌ No PDF files found. Check folder structure.")
    else:
        print("✅ Documents ingested successfully")

if __name__ == "__main__":
    ingest_documents()
