import streamlit as st
from gtts import gTTS
from chatbot import chatbot_response
from PIL import Image
import pytesseract

def clean_text_for_voice(text):
    if not text:
        return ""

    text = text.split("💡")[0]
    text = text.split("You can try")[0]

    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        if line.strip().startswith(("•", "-", "1", "2", "3", "4", "5", "6")):
            continue
        clean_lines.append(line)

    return "\n".join(clean_lines).strip()

def speak_text(text):
    if not text:
        return None
    
    tts = gTTS(text, lang='en')
    file_path = "voice.mp3"
    tts.save(file_path)
    return file_path

# PAGE SETUP
st.set_page_config(page_title="Books ChatBot", page_icon="📚")

st.title("📚 Books ChatBot")
st.write("Book Sequencing Chatbot")

# SESSION MEMORY
if "messages" not in st.session_state:
    st.session_state.messages = []

if "bot_response" not in st.session_state:
    st.session_state.bot_response = ""

if "play_audio" not in st.session_state:
    st.session_state.play_audio = None

# DISPLAY CHAT HISTORY
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# QUICK BUTTONS
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

uploaded_files = st.file_uploader(
    "📸 Upload book images", 
    type=["jpg", "png"], 
    accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=120)

        # OCR
        text = pytesseract.image_to_string(image)
        st.write("🔍 Detected Text:", text)

        # Send to chatbot
        user_input = text

        if user_input:
            bot_reply = chatbot_response(user_input)

            with st.chat_message("assistant"):
                st.markdown(bot_reply)

# CHAT INPUT
chat_input = st.chat_input("Type your message here...")
if chat_input:
    user_input = chat_input

# HANDLE INPUT
if user_input:
    # USER MESSAGE
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # BOT RESPONSE
    st.session_state.last_input = user_input
    bot_reply = chatbot_response(user_input)
    st.session_state.bot_response = bot_reply

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# 🔊 READ ALOUD BUTTON ONLY FOR OPTION 6
if "last_input" in st.session_state and str(st.session_state.last_input).startswith("6"):

    if st.button("🔊 Read aloud"):
        clean_text = clean_text_for_voice(st.session_state.bot_response)
        st.session_state.play_audio = speak_text(clean_text)

# 🔊 PLAY AUDIO
if st.session_state.play_audio:
    st.audio(st.session_state.play_audio)