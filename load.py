from langchain_community.document_loaders import PyPDFLoader

file_path = r"C:\Users\muhammad waseem\OneDrive\Desktop\labor_law\law_labor.pdf"
# loader = PyPDFLoader(file_path)
# docs = loader.load()
# docs[0]
# print(len(docs))

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs