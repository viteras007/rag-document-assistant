from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
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
    llm = OllamaLLM(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
