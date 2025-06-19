import streamlit as st
from dotenv import load_dotenv
import os
from api_calls import get_response

load_dotenv()
api_key = os.getenv('API_KEY')
st.markdown(api_key)


st.set_page_config(page_title="DigiBuddy Chatbot", page_icon="💬", layout="centered")
st.title("DigiBuddy 🤖 - Your Friendly Tech Buddy")
st.caption("Helping parents and seniors master the digital world 🌐")

# Accessibility: bigger text
st.markdown("""
    <style>
        .stChatMessage { font-size: 1.2em; }
        .stTextInput > div > div > input { font-size: 1.2em; }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar quick actions
with st.sidebar:
    st.header("🔍 Quick Options")
    if st.button("🎓 Learn Basics"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Let’s start with basics! You can ask things like 'What is a browser?' or 'How to set up an email?'"
        })
    if st.button("❓ Ask a Question"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Sure! Type your tech question below and I’ll guide you step by step."
        })
    if st.button("🚨 Get Help"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Having trouble? Try asking 'Why isn’t my phone connecting to Wi-Fi?' or 'How to pay electricity bill online?'"
        })
    st.markdown("---")
    st.markdown("**🌟 Tip:** Click a button to get started if you're not sure what to ask!")

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Ask me anything about using digital tools..."):
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Generating Output..."):
            response = get_response(user_input, api_key)
            if 'error' in response:
                message = response['error'].get('message', 'Oops, something went wrong.')
                st.error(message)
                st.session_state.messages.append({"role": "assistant", "content": message})
            else:
                reply = response['choices'][0]['message']['content']
                # Add warmth and motivation
                if any(word in user_input.lower() for word in ["can't", "difficult", "trouble"]):
                    reply += "\n\n💖 Remember: You're doing great! Learning tech takes time and you're on the right track."
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
