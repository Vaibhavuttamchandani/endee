"""Ingest PDF documents and store embeddings in Endee."""
import os
from sentence_transformers import SentenceTransformer
from endee import Client
import PyPDF2

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Client(host=os.getenv("ENDEE_HOST", "localhost"), port=int(os.getenv("ENDEE_PORT", 7000)))
COLLECTION_NAME = "documents"

def ingest_pdf(pdf_path):
    reader = PyPDF2.PdfReader(open(pdf_path, "rb"))
    for page in reader.pages:
        text = page.extract_text()
        if text:
            emb = model.encode(text).tolist()
            client.insert(collection=COLLECTION_NAME, vector=emb, metadata={"text": text})

if __name__ == "__main__":
    ingest_pdf("data/sample.pdf")
