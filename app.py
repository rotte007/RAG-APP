from fastapi import FastAPI
from pydantic import BaseModel
from retriever import retrieve
from generator import generate_answer

class Query(BaseModel):
    question: str

app = FastAPI()

@app.post("/rag")
async def rag(query: Query):
    context = retrieve(query.question, k=5)
    answer = generate_answer(query.question, context)
    return {"answer": answer, "context": context}
