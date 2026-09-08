"""LLM agent layer: OpenAI-compatible client + three prompt builders."""
from __future__ import annotations

import json
import os
import random
import time

from openai import OpenAI

DEFAULT_MODEL = "deepseek-chat"
MAX_INPUT_CHARS = 180_000  # keep comfortably inside a 256k-token context

SCORE_SYSTEM = """你是「无序蛋白/相分离 × 蛋白互作 × AI 方法」领域的文献筛选助手。
根据论文标题与摘要，评估它与该课题的相关性，输出一个 JSON 对象：
{"score": 0, "one_liner_zh": "..."}

score 为 0-10 的整数，衡量相关性：
- 8-10：核心命中（无序蛋白/相分离 + 蛋白互作 + AI/计算方法三者齐全，且有实质贡献）
- 5-7：部分命中（三者缺一，或仅为应用/综述）
- 0-4：边缘或无关
one_liner_zh 用一句话中文概括该文做什么、与课题的关系。只输出 JSON，不要其他文字。"""


def make_client() -> OpenAI:
    base_url = os.environ.get("LLM_BASE_URL", "").strip()
    api_key = os.environ.get("LLM_API_KEY", "").strip()
    kwargs = {"api_key": api_key, "timeout": 180.0}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def model_name() -> str:
    return os.environ.get("LLM_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL


def _truncate(text: str, limit: int = MAX_INPUT_CHARS) -> str:
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    head = text[: limit // 2]
    tail = text[-(limit // 2) :]
    return head + "\n\n[内容过长，中间已省略]\n\n" + tail


def _chat(client, model, messages, temperature=0.0, max_tokens=8000, json_mode=False, max_attempts=4):
    last: Exception | None = None
    for attempt in range(max_attempts):
        try:
            kwargs = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}
            resp = client.chat.completions.create(**kwargs)
            return (resp.choices[0].message.content or "").strip()
        except Exception as exc:  # noqa: BLE001 — retry any transport/parse failure
            last = exc
            if attempt + 1 < max_attempts:
                time.sleep(min(30.0, 2 ** attempt + random.random()))
    raise RuntimeError(f"LLM call failed after {max_attempts} attempts: {last}")


def _validate_score(obj: dict) -> dict:
    raw_score = obj.get("score", 0)
    try:
        score = int(raw_score)
    except (TypeError, ValueError):
        score = 0
    score = max(0, min(10, score))
    one_liner = str(obj.get("one_liner_zh", "") or "").strip()
    return {"score": score, "one_liner_zh": one_liner}


def score_paper(client, model, title: str, abstract: str) -> dict:
    user = f"标题：{title}\n\n摘要：{abstract or '（无摘要）'}"
    raw = _chat(
        client,
        model,
        [
            {"role": "system", "content": SCORE_SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.0,
        max_tokens=500,
        json_mode=True,
    )
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        obj = {}
    return _validate_score(obj)
