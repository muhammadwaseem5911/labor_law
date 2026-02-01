import streamlit as st
from dotenv import load_dotenv

from embedding import load_vector_store
from rag import create_rag_chain

load_dotenv()

st.set_page_config(
    page_title="UAE Labor Law Assistant",
    page_icon="⚖️"
)

st.title("⚖️ UAE Labor Law Assistant")

# ✅ Cache RAG chain
@st.cache_resource
def load_rag_chain():
    vectorstore = load_vector_store()
    return create_rag_chain(vectorstore)

rag = load_rag_chain()

question = st.text_input(
    "Ask a question related to UAE Labor Law"
)

if question:
    result = rag.invoke({"input": question})

    st.subheader("Answer")
    st.write(result["answer"])