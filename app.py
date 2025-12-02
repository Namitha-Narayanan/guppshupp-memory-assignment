import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="GuppShupp Memory Prototype", page_icon="💭")

st.title("GuppShupp – Memory & Personality Prototype")

user_message = st.text_input("Hi There, How can I help you?")
if st.button("Send") and user_message:
    with st.spinner("Thinking..."):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"You are a friendly assistant. Reply to the user: {user_message}",
        )
        reply_text = response.output[0].content[0].text.value

    st.markdown("**Reply:**")
    st.write(reply_text)
