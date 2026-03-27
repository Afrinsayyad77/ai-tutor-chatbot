# AI Tutor Chatbot (RAG + Ollama)

# Overview
This project is an AI chatbot that answers questions strictly from a provided document.

If the question is outside the document, it responds:
"This question is outside the provided material."

# Features
- RAG-based architecture
- Context-aware responses
- Hallucination control
- Local LLM using Ollama

# Tech Stack
- Python
- LangChain
- FAISS
- Ollama

# How to Run

pip install -r requirements.txt  
ollama pull phi  
python app.py  

# Example

Q: What is machine learning?  
A: Answer from document  

Q: What is RAG  
A: This question is outside the provided material.
