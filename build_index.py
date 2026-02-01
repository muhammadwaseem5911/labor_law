from load import load_pdf
from text_spt import split_documents
from embedding import create_vector_store

PDF_PATH = "law_labor.pdf"

docs = load_pdf(PDF_PATH)
chunks = split_documents(docs)

vectorstore = create_vector_store(chunks)
vectorstore.save_local("faiss_index")

print("FAISS index created successfully")