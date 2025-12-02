from PersonalityEngine import PersonalityEngine

def test_unknown_style_returns_base_reply():
    engine = PersonalityEngine()
    out = engine.rewrite("Hello world", "not_a_style")
    assert "Hello world" in out

def test_mentor_style_adds_opener_and_emoji():
    engine = PersonalityEngine()
    out = engine.rewrite("This is a test reply.", "mentor")
    assert "🧭" in out
    assert "mentor" in out.lower()
