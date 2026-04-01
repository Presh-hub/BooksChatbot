import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Books Chatbot", page_icon="📚")

st.title("📚 Books ChatBot")
st.write("Discover books, search, and get summaries!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.write(msg)

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)

        st.session_state.messages.append(f"🧑 You: {user_input}")
        st.session_state.messages.append(f"🤖 Bot: {response}")

        st.rerun()