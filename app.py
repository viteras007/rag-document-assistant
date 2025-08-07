import streamlit as st
from rag_chain import get_rag_chain
import time

st.set_page_config(page_title="RAG Doc Assistant", layout="wide")

# Initialize session state to control if the model is loaded
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
if 'chain' not in st.session_state:
    st.session_state.chain = None

# Show initial loading if the model hasn't been loaded yet
if not st.session_state.model_loaded:
    # Centered layout for loading
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
        <div style="text-align: center; padding: 40px; border-radius: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
            <h1 style="margin-bottom: 20px;">🤖 RAG Document Assistant</h1>
            <div style="font-size: 48px; margin: 20px 0;">🔄</div>
            <h2 style="margin-bottom: 15px;">Loading AI Model...</h2>
            <p style="font-size: 16px; opacity: 0.9;">Initializing document processing system</p>
            <div style="margin-top: 30px;">
                <div style="width: 200px; height: 4px; background: rgba(255,255,255,0.3); border-radius: 2px; margin: 0 auto;">
                    <div style="width: 0%; height: 100%; background: white; border-radius: 2px; animation: loading 2s infinite;"></div>
                </div>
            </div>
        </div>
    </div>
    <style>
    @keyframes loading {
        0% { width: 0%; }
        50% { width: 70%; }
        100% { width: 100%; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Progress spinner
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Simulate loading progress
    for i in range(101):
        time.sleep(0.05)  # Adjust as needed
        progress_bar.progress(i)
        if i < 30:
            status_text.text("🔄 Connecting to vector database...")
        elif i < 60:
            status_text.text("🤖 Loading language model...")
        elif i < 90:
            status_text.text("📚 Preparing query system...")
        else:
            status_text.text("✅ Finalizing initialization...")
    
    # Load the real model
    with st.spinner("Initializing AI model..."):
        st.session_state.chain = get_rag_chain()
        st.session_state.model_loaded = True
    
    # Reload the page to show the main interface
    st.rerun()

# Main interface when the model is loaded
st.title("💬 Document RAG Assistant")
st.success("✅ Model loaded and ready to use!")

# Input field for questions
query = st.text_input("Enter your question based on the documents:")

if query:
    with st.spinner("Consulting documents..."):
        result = st.session_state.chain.invoke(query)

    st.subheader("📚 Answer:")
    st.write(result["result"])

    st.subheader("🔗 Sources:")
    for doc in result["source_documents"]:
        st.markdown(f"- `{doc.metadata['source']}`")
