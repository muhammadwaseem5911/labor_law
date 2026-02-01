A **Retrieval-Augmented Generation (RAG)** application designed to answer questions related to the **UAE Labor Law using official legal** documents, with strict context grounding to prevent hallucinations.

This project demonstrates how **GenAI** can be applied responsibly in legal and compliance domains.

**Features**

Document-based question answering\
Vector-based semantic search\
Strict context grounding (no hallucinations)\
LLM-powered legal Q&A\
Low-latency inference using Groq (LLaMA 3.1)\
Interactive Streamlit UI\
Production-style error handling & caching

**How It Works**

UAE Labor Law documents are loaded and split into chunks\
Chunks are embedded and stored in a vector database\
User questions trigger semantic retrieval\
Retrieved context is injected into the prompt\
The LLM generates answers strictly from the retrieved documents\
If information is not present, the assistant clearly states **sorry**

**Use Cases**

UAE Labor Law Q&A\
HR compliance assistance\
Legal research support\
Policy interpretation tools\
Educational legal assistants

**Support**

If you find this project useful, feel free to ⭐ star the repository or suggest improvements.
