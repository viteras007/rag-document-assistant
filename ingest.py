from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

# PDF files path
DOCS_PATH = "docs/"
DB_PATH = "db/"

def load_documents():
    docs = []
    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DOCS_PATH, filename))
            docs.extend(loader.load())
    return docs

def ingest():
    print("📄 Loading documents...")
    docs = load_documents()

    print("✂️ Splitting texts...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    print("🧠 Creating embeddings with HuggingFace...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("📦 Saving vector database with Chroma...")
    Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=DB_PATH)

    print("✅ Ingestion completed!")

if __name__ == "__main__":
    ingest()
