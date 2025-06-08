import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="RAG QnA & Summarization Chatbot", layout="wide")

st.title("Welcome to the Gemini RAG Chatbot!")
st.markdown("Select a page from the sidebar to get started.")

# Streamlit will automatically detect and display pages in the 'pages' directory.
