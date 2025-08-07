import streamlit as st
from rag_chain import get_rag_chain

st.set_page_config(page_title="RAG com HuggingFace + Ollama", layout="wide")
st.title("💬 RAG com Hugging Face, LangChain, Ollama e Streamlit")

query = st.text_input("Digite sua pergunta baseada nos documentos:")

if query:
    chain = get_rag_chain()
    with st.spinner("Consultando..."):
        result = chain(query)

    st.subheader("📚 Resposta:")
    st.write(result["result"])

    st.subheader("🔗 Fontes:")
    for doc in result["source_documents"]:
        st.markdown(f"- `{doc.metadata['source']}`")
