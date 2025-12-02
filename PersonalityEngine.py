# PersonalityEngine.py
import os
from dataclasses import dataclass
from typing import Dict, List

from openai import OpenAI

# Global OpenAI client (uses your OPENAI_API_KEY from .env)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dataclass
class PersonalityStyle:
    """Simple container to describe a personality style."""
    key: str
    label: str
    description: str
    opener: str
    emoji: str


class PersonalityEngine:
    """
    Personality engine that rewrites a neutral assistant reply
    into different tones (mentor, witty friend, therapist, etc.).

    It uses small, focused prompts so it’s easy to reason about
    in a code review.
    """

    def __init__(self) -> None:
        self.styles: Dict[str, PersonalityStyle] = {
            "mentor": PersonalityStyle(
                key="Mentor",
                label="Supportive Mentor",
                description="Encouraging, structured, gives clear next steps and gentle accountability.",
                opener="Here's how I’d approach this with you as a mentor:",
                emoji="🧭",
            ),
            "witty_friend": PersonalityStyle(
                key="Witty_Friend",
                label="Witty Friend",
                description="Casual, playful, relatable, but still practically helpful.",
                opener="Okay, real talk, friend:",
                emoji="😄",
            ),
            "therapist": PersonalityStyle(
                key="Therapist",
                label="Calm Therapist",
                description="Empathetic, validating, reflective, focuses on emotions and safety.",
                opener="Let’s slow this down for a moment:",
                emoji="🪷",
            ),
            "cheerleader": PersonalityStyle(
                key="Cheerleader",
                label="Cheerleader",
                description="High energy, motivating, lots of positive reinforcement and small wins.",
                opener="You’ve got this, seriously:",
                emoji="📣",
            ),
        }

    def list_styles(self) -> List[PersonalityStyle]:
        """Return all supported styles (for the UI to show)."""
        return list(self.styles.values())

    def rewrite(self, base_reply: str, style_key: str) -> str:
        """
        Transform a neutral reply into a styled one.

        - Uses OpenAI to fully rewrite the reply in the chosen tone.
        - Falls back to the original text if anything goes wrong.
        """
        style = self.styles.get(style_key)
        if style is None:
            return base_reply

        # If the base reply is empty or too short, don’t over-process it.
        stripped = (base_reply or "").strip()
        if not stripped:
            return ""

        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"""
You rewrite assistant replies into different tones.

BASE REPLY:
\"\"\"{stripped}\"\"\"

TARGET STYLE:
- Name: {style.label}
- Description: {style.description}

REWRITE RULES:
- Keep the meaning and key information the same.
- Change phrasing, tone, and rhythm to match the style.
- Use clear, natural, human-like language.
- 2–4 short paragraphs max.
- No explanations, no meta comments, just the rewritten reply text.
"""
            )

            rewritten = response.output[0].content[0].text.strip()
        except Exception:
            # If the API fails for any reason, just return the original reply
            rewritten = stripped

        # Add personality opener + emoji so before/after is obvious in the UI
        return f"{style.emoji} {style.opener}\n\n{rewritten}"

