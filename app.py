import streamlit as st
from rag_chain import get_rag_chain

st.set_page_config(page_title="RAG with HuggingFace + Ollama", layout="wide")
st.title("💬 RAG with Hugging Face, LangChain, Ollama and Streamlit")

query = st.text_input("Enter your question based on the documents:")

if query:
    chain = get_rag_chain()
    with st.spinner("Consulting..."):
        result = chain(query)

    st.subheader("📚 Answer:")
    st.write(result["result"])

    st.subheader("🔗 Sources:")
    for doc in result["source_documents"]:
        st.markdown(f"- `{doc.metadata['source']}`")
