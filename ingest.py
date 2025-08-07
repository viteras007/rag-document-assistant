from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

# Caminho dos PDFs
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
    print("📄 Carregando documentos...")
    docs = load_documents()

    print("✂️ Dividindo textos...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    print("🧠 Criando embeddings com HuggingFace...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("📦 Salvando base vetorial com Chroma...")
    Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=DB_PATH)

    print("✅ Ingestão concluída!")

if __name__ == "__main__":
    ingest()
