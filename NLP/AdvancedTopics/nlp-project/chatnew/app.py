import streamlit as st
from openai import OpenAI

# 🔌 Connect to LM Studio
client = OpenAI(
    base_url="http://192.168.29.105:1234/v1",
    api_key="lm-studio"
)

st.set_page_config(page_title="Local Qwen Chat", page_icon="🤖")
st.title("🤖 Local Qwen Chat (LM Studio)")

# 🧠 Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔁 Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 💬 User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # 🔥 Send to LM Studio
    response = client.chat.completions.create(
        model="qwen3-vl-4b",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Add assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)