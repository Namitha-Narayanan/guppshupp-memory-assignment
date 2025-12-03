# GuppShupp – Founding AI Engineer Assignment

This repository contains my implementation of the GuppShupp AI Companion assignment.  
The project includes:

- A **Memory Extraction Module**
- A **Personality Engine**
- A **Streamlit interface** to demonstrate the full flow
- **Unit tests** for core components

The solution is modular, easy to run, and follows the assignment requirements.

---

## 1. Project Overview

### Memory Extraction Module
Extracts the following from up to 30 user chat messages:
- User preferences  
- Emotional patterns  
- Long-term factual memories  

If an `OPENAI_API_KEY` is available, this module uses an LLM to perform the extraction.  
If no key is available, it returns a consistent empty structure for testing.

### Personality Engine
Rewrites a **neutral response** into a selected tone:
- Mentor  
- Witty Friend  
- Therapist  
- Cheerleader  

This is done using an LLM prompt that rewrites the full message in the chosen style.

### Streamlit App
A simple UI that shows:
1. User input  
2. Neutral response  
3. Styled response  
4. Personality switcher  

---

## 2. Repository Structure

```
├── app.py                     # Streamlit UI
├── MemoryExtractor.py         # Memory extraction logic (LLM-based)
├── PersonalityEngine.py       # Personality rewriting (LLM-based)
├── sample_data/               # Example chat logs
├── screenshots/               # Output screenshots
├── tests/
│   ├── test_memory_extractor.py
│   ├── test_personality_engine.py
│   └── test_validation.py
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

##  3. Requirements
Python Version

Python 3.10+

Install Dependencies
```bash
pip install -r requirements.txt
```
Environment Variable
```graphql
Set your OpenAI key (optional but recommended):
```
macOS/Linux
```bash
export OPENAI_API_KEY=your_key_here
```

Windows (PowerShell)
```bash
setx OPENAI_API_KEY "your_key_here"
```

If no key is set:

- Memory extraction returns empty structured output

- Personality engine will still run with fallback prompts

- Tests will still pass

## 4. Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

## 5. Running Tests

Tests are written using pytest.

Run all tests:

```bash
pytest
```


## 7. System Architecture
Overview Diagram (Text Version)
```
┌──────────────────────────────┐
│         User Input            │
│  (chat messages from user)    │
└───────────────┬──────────────┘
                │
                ▼
      ┌────────────────────┐
      │  Validation Layer  │
      │ - Max 30 messages  │
      │ - Structure check  │
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │  MemoryExtractor   │
      │  (LLM-based)       │
      │ - Preferences      │
      │ - Emotional cues   │
      │ - Long-term facts  │
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │  Neutral Response  │
      │   (LLM-based)      │
      └─────────┬──────────┘
                │
                ▼
  ┌──────────────────────────────┐
  │      PersonalityEngine       │
  │   (LLM tone transformation)  │
  │  - Mentor                    │
  │  - Witty friend              │
  │  - Therapist                 │
  │  - Cheerleader               │
  └───────────────┬──────────────┘
                  │
                  ▼
       ┌────────────────────┐
       │   Styled Reply     │
       │  (persona output)  │
       └────────────────────┘

```
## 8. Notes

- The solution is modular: Memory extraction and personality rewriting are independent components.

- The codebase is small, simple, and easy to extend.

- Test cases are deterministic and do not require network access.

- Designed to match the assignment requirement: modularity, structured output, and clean reasoning.

