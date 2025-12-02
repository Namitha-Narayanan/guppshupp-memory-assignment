import json
import os
from openai import OpenAI

"""
Memory Extraction Module

This module takes a sequence of chat messages and asks the LLM to extract
useful long-term memories:
- preferences
- emotional patterns
- stable facts

The output is a structured JSON object that the personality engine can reuse.
"""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for memory extraction
MEMORY_SYSTEM_PROMPT = """
You are a memory extraction module inside a companion AI system.

Read the user's past messages and extract ONLY long-term, meaningful information.

Focus on three categories:
1. preferences (likes, dislikes, habits, routines)
2. emotional_patterns (repeated feelings, triggers, anxieties, coping patterns)
3. facts (biographical or stable information)

RULES:
- Only extract info from USER messages, not assistant messages.
- Do not invent anything that is not strongly implied.
- Group similar items together.
- Output STRICT JSON with three keys:
  "preferences": [],
  "emotional_patterns": [],
  "facts": []
Each list should contain simple strings (not nested objects).

If there is nothing for a category, return an empty list.
"""


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_SYSTEM_PROMPT = """
You are a memory extraction engine for a personal AI companion.
Given a chat history, pull out only information that is useful
to remember long term.

Return STRICT JSON with these keys:
- preferences: list of short strings
- emotional_patterns: list of short strings
- long_term_facts: list of short strings
"""

def extract_memories(messages):
    """
    Extract long-term memories from a list of chat messages.

    messages: list[dict] with {"role": "...", "content": "..."}
    returns: dict with keys: preferences, emotional_patterns, long_term_facts
    """

    # If there's no API key (e.g. in tests), just return an empty but valid structure.
    if not os.getenv("OPENAI_API_KEY"):
        return {
            "preferences": [],
            "emotional_patterns": [],
            "long_term_facts": [],
        }

    # Keep only user messages to avoid system/tool noise
    user_lines = [m["content"] for m in messages if m.get("role") == "user"]
    joined = "\n".join(f"- {line}" for line in user_lines)

    user_prompt = (
        "Here is a chat history from one user.\n\n"
        f"{joined}\n\n"
        "Extract stable preferences, recurring emotional themes, "
        "and long-term factual details. Follow the JSON format exactly."
    )

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": MEMORY_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )

    raw = resp.choices[0].message.content

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        # Fallback: never crash the app if the LLM returns something slightly off
        parsed = {}

    return {
        "preferences": parsed.get("preferences", []),
        "emotional_patterns": parsed.get("emotional_patterns", []),
        "long_term_facts": parsed.get("long_term_facts", []),
    }

