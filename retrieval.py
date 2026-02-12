# retrieval.py
from governance import get_approved_latest

def search_documents(query, module=None, top_k=3):
    """
    Keyword-based document retrieval for Pharma DMS RAG system.

    Parameters:
        query (str): User's search query
        module (str): Optional module filter ('production', 'quality', 'inventory')
        top_k (int): Maximum number of results to return

    Returns:
        List of dicts: Each dict contains doc_id, filename, module, version, snippet
    """
    docs = get_approved_latest(module)  # Fetch approved docs for the module
    results = []

    if not query.strip():
        return results  # Empty query, return no results

    query_words = query.lower().split()

    for doc in docs:
        doc_id, filename, doc_module, version, eff_date, content = doc
        content_lower = content.lower()

        # Check if any word in query is in document content
        matched_words = [word for word in query_words if word in content_lower]
        if matched_words:
            # Get snippet around first match
            first_match_pos = min([content_lower.find(word) for word in matched_words])
            snippet_start = max(first_match_pos - 50, 0)  # 50 chars before match
            snippet_end = snippet_start + 200  # total snippet length
            snippet = content[snippet_start:snippet_end]

            # Optional: highlight matched words
            for word in matched_words:
                snippet = snippet.replace(word, f"**{word}**")
                snippet = snippet.replace(word.capitalize(), f"**{word.capitalize()}**")

            results.append({
                "doc_id": doc_id,
                "filename": filename,
                "module": doc_module,
                "version": version,
                "snippet": snippet
            })

        if len(results) >= top_k:
            break  # Limit to top_k results

    return results
