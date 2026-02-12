# DMS – Document-Based Query & Retrieval System

DMS (Document Management System) is a Flask-based backend application that allows users to query approved documents and receive answers strictly grounded in retrieved document content.

The system ensures controlled responses, citation tracking, and query logging, making it suitable for enterprise knowledge systems and GenAI-based RAG architectures.

**Features**

**Document Retrieval:**
Uses search_documents() function
Retrieves relevant snippets based on user query
Supports optional module-based filtering

**Grounded Responses:**

Generates answers only from retrieved snippets
If no relevant data → returns
“Insufficient evidence in approved documents.”
 Citation Tracking
 
**Returns:**
Document ID
Filename
Ensures traceability and audit compliance

**Query Logging**
 **Stores:**
User query
Retrieved document citations
Logged in SQLite database (query_logs table)


| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| Python                 | Core language             |
| Flask                  | REST API framework        |
| SQLite                 | Database for query logs   |
| JSON                   | Data exchange format      |
| Custom Retrieval Logic | Document search mechanism |

**System Architecture**

User Request
     ↓
Flask API (/query)
     ↓
search_documents()
     ↓
Retrieve relevant snippets
     ↓
Generate grounded answer
     ↓
Store query + citations in DB
     ↓
Return JSON response

Retrieved document citations

Logged in SQLite database (query_logs table)
