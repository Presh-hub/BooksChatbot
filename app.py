import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Books ChatBot", page_icon="📚")

st.title("📚 Books ChatBot")
st.markdown(
    """
    <style>
    .stChatMessage {
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.write("Discover books, search, and get summaries!")

# SESSION MEMORY (keeps chat history)
if "messages" not in st.session_state:
    st.session_state.messages = []

# DISPLAY CHAT HISTORY
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# USER INPUT
st.write("### ⚡️ Quick Actions")
user_input = None

col1, col2, col3 = st.columns(3)

if col1.button("📚 All Books"):
    user_input = "1"

elif col2.button("🟢 Beginner"):
    user_input = "2"

elif col3.button("🔵 Intermediate"):
    user_input = "3"

col4, col5 = st.columns(2)

if col4.button("🔴 Advanced"):
    user_input = "4"

elif col5.button("🔍 Search Python"):
    user_input = "5 python"
chat_input = st.chat_input("Type your message here...")
if chat_input:
    user_input = chat_input

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    bot_response = chatbot_response(user_input)

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)