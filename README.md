# RAG Document Assistant

A document assistant based on RAG (Retrieval-Augmented Generation) built with Streamlit, LangChain, HuggingFace and Ollama.

## 🚀 Features

- **Web Interface**: User-friendly interface built with Streamlit
- **RAG Pipeline**: Retrieval and response generation system
- **Local Models**: Uses Ollama to run LLM models locally
- **Embeddings**: Uses HuggingFace for high-quality embeddings
- **Vector Database**: ChromaDB for document storage and search

## 📋 Prerequisites

- Python 3.8+
- Ollama installed and running
- Mistral model downloaded in Ollama

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone <your-repository>
cd rag-document-assistant
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure Ollama:**
```bash
# Install Ollama (if you don't have it yet)
# https://ollama.ai/

# Download the Mistral model
ollama pull mistral
```

## 📚 How to use

1. **Prepare your documents:**
   - Place your PDFs in the `docs/` folder

2. **Run the ingestion:**
```bash
python ingest.py
```

3. **Start the application:**
```bash
streamlit run app.py
```

4. **Access the interface:**
   - Open http://localhost:8501 in your browser

## 🏗️ Architecture

- **`app.py`**: Main Streamlit interface
- **`rag_chain.py`**: RAG chain configuration
- **`ingest.py`**: Document processing script
- **`requirements.txt`**: Project dependencies

## 📁 Project Structure

```
rag-document-assistant/
├── app.py              # Streamlit interface
├── rag_chain.py        # RAG configuration
├── ingest.py           # Document processing
├── requirements.txt    # Dependencies
├── .gitignore         # Git ignored files
├── README.md          # Documentation
├── docs/              # PDF documents (not versioned)
├── db/                # Vector database (not versioned)
└── venv/              # Virtual environment (not versioned)
```

## 🔧 Technologies Used

- **Streamlit**: Web interface
- **LangChain**: LLM framework
- **HuggingFace**: Embeddings and models
- **Ollama**: Local LLM
- **ChromaDB**: Vector database
- **PyPDF**: PDF reading

## 📄 License

This project is under the MIT license. See the `LICENSE` file for more details.
