from flask import Flask, request, jsonify, render_template
from retrieval import search_documents
from db import get_connection
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    user_query = data.get("query")
    module = data.get("module")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    results = search_documents(user_query, module)

    if not results:
        return jsonify({
            "answer": "Insufficient evidence in approved documents.",
            "citations": []
        })

    answer = "Based on approved documents:\n"
    citations = []

    for r in results:
        answer += f"- {r['snippet']}\n"
        citations.append({
            "doc_id": r["doc_id"],
            "filename": r["filename"]
        })

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO query_logs (query, retrieved_docs) VALUES (?, ?)",
            (user_query, json.dumps(citations))
        )
        conn.commit()
    except Exception as e:
        print("DB Error:", e)
    finally:
        conn.close()

    return jsonify({
        "answer": answer,
        "citations": citations
    })

if __name__ == "__main__":
    app.run(debug=True)
