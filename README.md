# RAG Document Assistant

Um assistente de documentos baseado em RAG (Retrieval-Augmented Generation) construído com Streamlit, LangChain, HuggingFace e Ollama.

## 🚀 Funcionalidades

- **Interface Web**: Interface amigável construída com Streamlit
- **RAG Pipeline**: Sistema de recuperação e geração de respostas
- **Modelos Locais**: Usa Ollama para rodar modelos LLM localmente
- **Embeddings**: Utiliza HuggingFace para embeddings de alta qualidade
- **Base Vetorial**: ChromaDB para armazenamento e busca de documentos

## 📋 Pré-requisitos

- Python 3.8+
- Ollama instalado e rodando
- Modelo Mistral baixado no Ollama

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone <seu-repositorio>
cd rag-document-assistant
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure o Ollama:**
```bash
# Instale o Ollama (se ainda não tiver)
# https://ollama.ai/

# Baixe o modelo Mistral
ollama pull mistral
```

## 📚 Como usar

1. **Prepare seus documentos:**
   - Coloque seus PDFs na pasta `docs/`

2. **Execute a ingestão:**
```bash
python ingest.py
```

3. **Inicie a aplicação:**
```bash
streamlit run app.py
```

4. **Acesse a interface:**
   - Abra http://localhost:8501 no seu navegador

## 🏗️ Arquitetura

- **`app.py`**: Interface Streamlit principal
- **`rag_chain.py`**: Configuração da cadeia RAG
- **`ingest.py`**: Script para processar documentos
- **`requirements.txt`**: Dependências do projeto

## 📁 Estrutura do Projeto

```
rag-document-assistant/
├── app.py              # Interface Streamlit
├── rag_chain.py        # Configuração RAG
├── ingest.py           # Processamento de documentos
├── requirements.txt    # Dependências
├── .gitignore         # Arquivos ignorados pelo Git
├── README.md          # Documentação
├── docs/              # Documentos PDF (não versionado)
├── db/                # Base vetorial (não versionado)
└── venv/              # Ambiente virtual (não versionado)
```

## 🔧 Tecnologias Utilizadas

- **Streamlit**: Interface web
- **LangChain**: Framework para LLMs
- **HuggingFace**: Embeddings e modelos
- **Ollama**: LLM local
- **ChromaDB**: Base vetorial
- **PyPDF**: Leitura de PDFs

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
