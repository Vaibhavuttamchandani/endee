from sentence_transformers import SentenceTransformer
from endee import Client
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Client(host=os.getenv("ENDEE_HOST", "localhost"), port=int(os.getenv("ENDEE_PORT", 7000)))

def semantic_search(query, top_k=3):
    vec = model.encode(query).tolist()
    return client.search(collection="documents", vector=vec, top_k=top_k)
