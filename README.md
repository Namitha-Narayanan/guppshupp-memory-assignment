# GuppShupp – Memory & Personality Engine Assignment

This repository contains my implementation of the **Founding AI Engineer** assessment for **GuppShupp**.  
The assignment explores how a companion AI can understand a user over time and adapt its tone using memory-driven personalisation.

---

## 🌱 Overview

The project focuses on two tightly connected capabilities:

### 1. **Memory Extraction Module**
Given ~30 user messages, the module extracts structured long-term memories:
- **Preferences** (likes/dislikes, habits, routines)
- **Emotional patterns** (recurring feelings and triggers)
- **Facts worth remembering** (biographical or stable information)

The extracted memories are returned as a clean JSON object so they can be reused by other components.

### 2. **Personality Engine**
The same user message is answered in two ways:
- **Before:** a plain, neutral LLM response  
- **After:** a personalised response that uses:
  - extracted memories  
  - a selected personality style (mentor, witty friend, therapist, etc.)  
  - tone-modifying rules  

This makes the personality shift and memory use immediately visible.

---

## 🧠 System Design

The app is built as a small pipeline:

1. **Raw conversation → Memory Extraction**  
   A prompt instructs the LLM to identify stable patterns and generate structured memories.

2. **Memories → Persona Profile**  
   Based on extracted memories, a short persona ruleset is created for the assistant.

3. **User message → Two Responses**
   - **Baseline** (no memory, no personality)
   - **Personalised** (memory-informed + persona-driven)

This highlights how the assistant’s tone and specificity evolve when memory is involved.

---

## 🛠 Tech Stack

- **Python 3**
- **Streamlit** – for a simple, interactive UI
- **OpenAI API** – for memory extraction & personality transformation
- **Modular Python files** – for clarity and extendability  
- **Virtual environment (`.venv`)** – isolates dependencies

---

## 🚀 How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
# GuppShupp – Memory & Personality Engine Assignment

This project is my implementation of the GuppShupp Founding AI Engineer assessment.  
It focuses on two core areas of companion AI:

1. **Memory Extraction**
   - Identifying user preferences  
   - Recognising emotional patterns  
   - Extracting long-term facts worth remembering  

2. **Personality Engine**
   - Transforming a neutral assistant reply into different tones  
     (mentor, witty friend, therapist, etc.)
   - Showing before/after response differences

## Tech Stack

- Python  
- Streamlit (simple UI layer)  
- OpenAI API  
- Virtual environment (`.venv`)  
- Modular Python files for clarity

## How to Run

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py


## Notes

This project was built for the GuppShupp technical assignment.  
It is intentionally simple, modular, and easy to extend.
	
