import numpy as np
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

client = MongoClient("mongodb://localhost:27017")
db = client['rag']
coll = db['docs']
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def retrieve(query: str, k: int = 5):
    q_emb = embedder.encode(query).tolist()
    # naive scan; for production use MongoDB vector search or indexing
    docs = list(coll.find({}))
    scored = [(d['text'], cosine_sim(q_emb, d['embedding'])) for d in docs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
