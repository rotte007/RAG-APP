import streamlit as st
import requests

st.title("RAG App: MongoDB + Ollama")

question = st.text_input("Ask a question:")
if question:
    resp = requests.post("http://localhost:8000/rag", json={"question": question})
    data = resp.json()
    st.subheader("Answer")
    st.write(data['answer'])
    st.subheader("Context Chunks")
    for text, score in data['context']:
        st.write(f"- {text} (score={score:.3f})")