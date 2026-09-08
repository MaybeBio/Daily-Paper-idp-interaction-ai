import json
from types import SimpleNamespace

import agent

def fake_client(responses):
    calls = []
    class Completions:
        def create(self, **kwargs):
            calls.append(kwargs)
            r = responses.pop(0)
            if isinstance(r, Exception):
                raise r
            return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=r))])
    return SimpleNamespace(chat=SimpleNamespace(completions=Completions())), calls


def test_validate_score_good():
    assert agent._validate_score({"score": 7, "one_liner_zh": "x"}) == {"score": 7, "one_liner_zh": "x"}


def test_validate_score_clamps_and_coerces():
    assert agent._validate_score({"score": "9", "one_liner_zh": 3}) == {"score": 9, "one_liner_zh": "3"}


def test_score_paper_parses_json():
    client, calls = fake_client([json.dumps({"score": 5, "one_liner_zh": "一句话"})])
    res = agent.score_paper(client, "m", "title", "abstract")
    assert res == {"score": 5, "one_liner_zh": "一句话"}
    assert calls[0]["response_format"] == {"type": "json_object"}


def test_chat_retries_then_raises():
    client, calls = fake_client([RuntimeError("boom"), RuntimeError("boom"), RuntimeError("boom"), RuntimeError("boom")])
    import pytest
    with pytest.raises(RuntimeError):
        agent._chat(client, "m", [{"role": "user", "content": "hi"}], max_attempts=2)
    assert len(calls) == 2
