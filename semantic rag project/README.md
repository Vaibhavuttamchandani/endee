# Endee Semantic Search & RAG System

## Project Overview
Organizations store large amounts of information in documents such as PDFs, manuals, and reports. Traditional keyword-based search systems fail to understand the semantic meaning of user queries, often returning irrelevant or incomplete results.

This project demonstrates an AI-powered Semantic Search and Retrieval Augmented Generation (RAG) system built using Endee as the vector database. The system allows users to ask natural language questions and retrieves the most relevant document content using vector similarity search before generating an answer.

## Problem Statement
Keyword-based document search lacks contextual understanding and semantic relevance. The goal of this project is to build a document-aware AI system that:
- Understands semantic meaning instead of keywords
- Retrieves relevant document context using vector search
- Generates accurate, context-grounded answers

## System Design & Technical Approach

PDF Documents
→ Text Extraction & Chunking
→ Embedding Generation
→ Endee Vector Database
→ Semantic Similarity Search
→ Retrieval Augmented Generation (Answer)

## Use of Endee
Endee is used as the core vector database in this project.

- Document chunks are converted into vector embeddings
- Embeddings are stored in an Endee collection
- User queries are embedded and searched using vector similarity
- Retrieved chunks are used as context for answer generation

This enables semantic search rather than traditional keyword-based retrieval.

## Setup & Execution Instructions

### Prerequisites
- Python 3.9+
- Git
- Optional: Docker

### Local Setup
pip install -r requirements.txt
python app/ingest_pdf.py
uvicorn app.api:app --reload

### Docker Setup
docker-compose up --build

## API Usage
POST /ask

Example request:
{
  "query": "What is retrieval augmented generation?"
}

## Practical Use Case
- Internal knowledge base assistant
- Document search and Q&A system
- Policy or compliance document analysis
- Research document understanding

## Future Enhancements
- Streamlit UI
- Agentic workflow (search → verify → answer)
- Multiple Endee collections
- Cloud deployment

## Conclusion
This project demonstrates how Endee can be effectively used as a vector database to power semantic search and RAG-based AI applications.
