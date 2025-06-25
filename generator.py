import requests
from typing import List, Tuple

LLM_URL = 'http://localhost:11434/api/generate'
MODEL = 'gemma3:1b'

def build_prompt(query: str, context: List[Tuple[str, float]]) -> str:
    docs = "\n---\n".join([text for text, _ in context])
    return (
        "You are an expert assistant. Use the context below to answer.\n"
        f"Context:\n{docs}\n"
        f"Question: {query}\nAnswer:"
    )

def generate_answer(query: str, context: List[Tuple[str, float]]) -> str:
    prompt = build_prompt(query, context)
    resp = requests.post(LLM_URL, json={"model": MODEL, "prompt": prompt, "stream": False})
    resp.raise_for_status()
    return resp.json().get('response', '').strip()
