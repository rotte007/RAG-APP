## Simple RAG pipeline in Python using:

- Sentence‑Transformers for embeddings
- MongoDB for document storage
- FAISS for vector search
- Ollama as the local LLM backend
- FAST API for the backend API
- Streamlit for the frontend UI

## Features

- Index documents and store embeddings in MongoDB
- Retrieve relevant context chunks for a query using semantic search
- Generate answers using a local LLM (Ollama)
- Simple web UI for asking questions

## Setup

1. **Install dependencies**

   ```sh
   pip install -r requirements.txt

2. Set up MongoDB

  - Start a local MongoDB instance or use a cloud MongoDB.
  - Add your MongoDB URI to .env or directly in indexer.py and retriever.py. 

3. Prepare your data. Place your documents in a JSON file (e.g., data/faqs.json) with format
    ```
    [
      {"id": "doc1", "text": "Document text 1"},
      {"id": "doc2", "text": "Document text 2"}
    ]
    ```
4. Index documents
    ```sh
    python indexer.py

5. Start the backend API
    ```sh
    uvicorn app:app --reload

6. Start the frontend
     ```sh
    streamlit run front/app.py

7. Start Ollama

 - Install and run Ollama with your desired model (e.g., gemma3:1b).

Usage

- Open the Streamlit UI in your browser.
- Ask a question; the app will retrieve relevant context and generate an answer using the LLM.

Notes

- For production, consider using MongoDB's vector search or FAISS for efficient retrieval.
- Update the model and endpoints in generator.py as needed.
    










