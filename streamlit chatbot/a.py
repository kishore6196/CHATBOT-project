import streamlit as st
from streamlit_chat import message as st_message





if "history" not in st.session_state:
    st.session_state.history = []

st.title("Hello Chatbot")


def generate_answer():
    # .replace("<s>", "").replace("</s>", "")

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})


st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)  # unpacking