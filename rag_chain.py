from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

DB_PATH = "db/"

def get_rag_chain():
    print("🔄 Loading vector database...")
    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    print("🤖 Loading local LLM model via Ollama...")
    llm = Ollama(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
