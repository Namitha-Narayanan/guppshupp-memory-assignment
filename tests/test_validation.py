# tests/test_validation.py

from app import validate_conversation_length

def test_allows_up_to_30_messages():
    messages = [{"role": "user", "content": "msg"}] * 30
    assert validate_conversation_length(messages) is True

def test_rejects_more_than_30_messages():
    messages = [{"role": "user", "content": "msg"}] * 31
    assert validate_conversation_length(messages) is False

def test_invalid_structure_rejected():
    assert validate_conversation_length({"role": "user"}) is False
