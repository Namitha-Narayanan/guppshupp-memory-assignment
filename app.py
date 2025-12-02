import os
import json
import streamlit as st
from openai import OpenAI

from MemoryExtractor import extract_memories
from PersonalityEngine import PersonalityEngine

# Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI settings
st.markdown("# 💬 GuppShupp – Memory & Personality Engine Demo")
st.markdown("A simple prototype that extracts long-term memories, generates neutral replies, and rewrites them in different personality styles.")

st.markdown("---")

st.markdown("### 👋 Welcome! Please enter your conversation below to get started.")
st.caption("Supports up to **30 messages** in JSON format.")
st.caption("Format: [{ role: 'user'/'assistant', content: '...' }, ...]")

def validate_conversation_length(messages):
    """
    Simple guardrail:
    - messages must be a list
    - each item must be a dict with 'role' and 'content'
    - max 30 messages (assignment requirement)
    """
    if not isinstance(messages, list):
        return False

    if len(messages) > 30:
        return False

    for m in messages:
        if not isinstance(m, dict):
            return False
        if "role" not in m or "content" not in m:
            return False

    return True

# -------------------------------------------------------
# SECTION 1 — Input: conversation JSON
# -------------------------------------------------------
st.subheader("1. Paste Conversation Messages (JSON Format)")

default_messages = [
    {"role": "user", "content": "Hey, I'm Namitha. I just moved to Bangalore."},
    {"role": "assistant", "content": "That's exciting! How is it so far?"},
    {"role": "user", "content": "I love late-night coding and chai."},
    {"role": "user", "content": "I get excited about AI and machine learning."},
]

conversation_text = st.text_area(
    "Enter chat history as a list of message objects:",
    json.dumps(default_messages, indent=2),
    height=220
)

conversation = None
try:
    conversation = json.loads(conversation_text)
except Exception:
    st.error("Invalid JSON. Please check the format.")


# -------------------------------------------------------
# SECTION 2 — Memory Extraction
# -------------------------------------------------------
st.subheader("2. Extract Long-Term User Memories")

if conversation and st.button("Extract Memories"):

    # Validate conversation length (assignment requirement)
    if not validate_conversation_length(conversation):
        st.error("Conversation too long. Maximum allowed is 30 messages.")
        st.stop()

    with st.spinner("Processing..."):
        memories = extract_memories(conversation)

    st.success("Memories extracted!")
    st.json(memories)

else:
    memories = None



# -------------------------------------------------------
# SECTION 3 — Generate Responses with Personality
# -------------------------------------------------------
st.subheader("3. Generate Before/After Responses")

user_message = st.text_input("Type a new user message:")

engine = PersonalityEngine()
style_keys = [s.key for s in engine.list_styles()]

chosen_style = st.selectbox("Choose a Personality Style:", style_keys)

if st.button("Generate Response"):
    if not user_message:
        st.error("Please enter a message first.")
    else:
        # Neutral baseline response
        with st.spinner("Generating neutral response..."):
            resp = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a neutral assistant."},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.4,
            )
            base_reply = resp.choices[0].message.content

        # Styled reply
        styled_reply = engine.rewrite(base_reply, chosen_style)

        # Display output
        st.write("### Neutral Response")
        st.info(base_reply)

        st.write(f"### Styled Response ({chosen_style})")
        st.success(styled_reply)
