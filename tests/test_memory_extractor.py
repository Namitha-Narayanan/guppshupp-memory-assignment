from MemoryExtractor import extract_memories

def test_memory_extractor_structure():
    messages = [{"role": "user", "content": "Hello"}]
    result = extract_memories(messages)

    assert "preferences" in result
    assert "emotional_patterns" in result
    assert "long_term_facts" in result

    assert isinstance(result["preferences"], list)
