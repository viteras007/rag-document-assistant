import streamlit as st
from rag_chain import get_rag_chain

st.set_page_config(page_title="RAG Doc Assistant", layout="wide")
st.title("💬 Document RAG Assistant")

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
