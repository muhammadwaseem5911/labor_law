from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def create_rag_chain(vectorstore):

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.01,
        max_tokens=512
    )

    system_prompt = (
        "You are a legal assistant specialized in UAE Labor Law. "
        "Answer the user's question strictly using the provided context from UAE labor law documents. "
        "If the answer is not explicitly stated in the context, say: "
        "'The provided documents do not contain this information.' "
        "Do not provide legal advice or assumptions.\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    document_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    rag_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return rag_chain