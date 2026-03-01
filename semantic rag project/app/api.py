from fastapi import FastAPI
from app.search import semantic_search
from app.rag import generate_answer

app = FastAPI()

@app.post("/ask")
def ask(query: str):
    docs = semantic_search(query)
    return {"answer": generate_answer(query, docs)}
