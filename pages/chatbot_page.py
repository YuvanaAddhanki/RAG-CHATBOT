import streamlit as st
from genai_services import answer_with_context
from dotenv import load_dotenv
load_dotenv()
st.title("Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Gemini is thinking..."):
        response = answer_with_context(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
