import streamlit as st
from gtts import gTTS
from chatbot import chatbot_response
from PIL import Image
import pytesseract
import time

# CLEAN TEXT FOR AUDIO
def clean_text_for_voice(text):
    if not text:
        return ""

    text = text.split("💡")[0]

    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        if line.strip().startswith(("•", "-", "1", "2", "3", "4", "5", "6")):
            continue
        clean_lines.append(line)

    return "\n".join(clean_lines).strip()

# TEXT TO SPEECH
def speak_text(text):
    if not text:
        return None
    
    try:
        tts = gTTS(text, lang='en')
        file_path = f"voice_{int(time.time())}.mp3"
        tts.save(file_path)
        return file_path
    except Exception as e:
        print("Error:", e)
        return None


# PAGE SETUP
col1, col2 = st.columns([4,1])

with col1:
    st.title("📚 Books ChatBot")
    st.write("Book Sequencing Chatbot")

with col2:
    st.image("chatbot.png", width=100)


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
    user_input = "1 all books"

elif col2.button("🟢 Beginner"):
    user_input = "2 beginner books"

elif col3.button("🔵 Intermediate"):
    user_input = "3 intermediate books"

col4, col5 = st.columns(2)

if col4.button("🔴 Advanced"):
    user_input = "4 advanced books"

elif col5.button("🔍 Search Python"):
    user_input = "5 python"


# OCR UPLOAD
uploaded_files = st.file_uploader(
    "📸 Upload book images", 
    type=["jpg", "png"], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=120)

        text = pytesseract.image_to_string(image)
        st.write("🔍 Detected Text:", text)

        # 🔥 FIX: always treat OCR as SEARCH
        user_input = f"5 {text}"


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
    bot_reply = chatbot_response(user_input)
    st.session_state.bot_response = bot_reply

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)


# 🔊 AUDIO BUTTON (FIXED PROPERLY)
if st.session_state.bot_response:
    if st.button("🔊 Read aloud"):
        clean_text = clean_text_for_voice(st.session_state.bot_response)
        audio_file = speak_text(clean_text)

        if audio_file:
            st.session_state.play_audio = audio_file  # ✅ SAVE STATE


# 🔊 PLAY AFTER RERUN (IMPORTANT)
if st.session_state.play_audio:
    st.audio(st.session_state.play_audio)