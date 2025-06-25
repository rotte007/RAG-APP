# from pymongo import MongoClient, ServerApi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sentence_transformers import SentenceTransformer
from data_loader import load_docs
from chunker import chunk_text

# Initialize
uri = "your mongo uri"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['rag']
coll = db['docs']
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def index_documents(json_path: str):
    print(f"Indexing documents from {json_path}...")
    docs = load_docs(json_path)
    for doc in docs:
        print(f"Indexing document {doc['text']}")
        # chunks = chunk_text(doc['text'])
        # print(f"Document {doc['text']} split into {len(chunks)} chunks")
        # for i, chunk in enumerate(chunks):
        #     emb = embedder.encode(chunk).tolist()
        #     record = {
        #         '_id': f"{doc['id']}_{i}",
        #         'doc_id': doc['id'],
        #         'text': chunk,
        #         'embedding': emb
        #     }
        #     coll.replace_one({'_id': record['_id']}, record, upsert=True)

index_documents("data/faqs.json")
