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


PAPER_CARD_SYSTEM = """你是资深科研人员，为一篇论文生成「深度阅读 Paper Card」，中文为主，技术术语保留英文。你只能基于提供的全文（或摘要），绝不编造。

严格输出以下 16 节，固定顺序，用 ## 二级标题，不得增删节，不得加第 17/18 节：

## 01 基本信息
标题、作者与单位、期刊/预印本平台、年份、论文类型、领域、关键词、DOI/arXiv 号、代码、数据、阅读日期，及该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置。缺失字段写「未提供」。

## 02 一句话总结
一句话：解决什么问题、用什么方法、通过什么机制、得到什么有边界的结论。避免推广性形容词。

## 03 研究问题
具体问题；为什么重要；现有方法为何不足；如适用给一个精确的「Can ... ?」研究问题。

## 04 背景与发展脉络
分阶段、代表性方法、优点、局限、本文主张的位置。注明这条脉络是「仅本文框架」还是「经外部核验」。

## 05 核心痛点
表格：| 痛点 | 表现 | 成因或作者解释 | 文中证据 |。不得把作者解释当既成根因而无证据。

## 06 核心思想
分三部分：1) 表面方法；2) 核心洞察；3) 可能的普适教训（标注 [Analysis]）。

## 07 方法总览
输入、输出、模块、训练、工具、反馈回路、假设；给出从输入到输出的文字流程。

## 08 核心模块拆解
表格：| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |。区分「实测消融效应」与「预期效应」。

## 09 关键公式符号
仅列理解必需的公式；每个给公式、符号含义、用途、直觉、来源指针。无则写「不适用」。

## 10 实验设计与证据链
先记录数据集/群体、规模、指标、基线、预算、骨干/仪器、oracle 输入、评测协议。
再列表格：| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |。

## 11 结论正确解读
审计任务范围、oracle/真值输入、端到端状态、算力成本、历史数据依赖、模型依赖、最难情形、群体/领域边界、不确定性。以有边界的复述收尾。

## 12 作者自认局限
只列作者明确承认的局限，表格：| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |。
若无则写「在提供的材料中未发现作者明确承认的局限」，不填表。可另加「作者提及的相关约束」小节并注明非正式局限。

## 13 批判性分析
表格：| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |。只列具体、可证伪的关切，不模仿正式审稿报告。

## 14 学到什么
可迁移的概念、方法、公式、实验设计。标题写「Agent 提炼的知识候选」。

## 15 与已有知识连接
连接到可核验的外部文献、用户已有知识，或明确标注的候选方向；覆盖相似、组合、冲突、可迁移领域（仅在可支撑时）。

## 16 研究想法
每个候选给：名称、来源局限/观察、核心假设、相对本文的增量、初步方法、验证方式、可能的失败模式、创新状态（unverified / partially checked / prior-art checked）。标题写「Agent 生成的研究候选」。

证据与来源规则：
- 区分「作者主张」与你自己的分析（标 [Analysis]）。
- 证据指针指向原文 section/图/表（如「Results 图 2」「Methods 节」）；没有就写「未提供」，绝不编造行号或图表。
- 拿不到的信息写「Not assessable / Not applicable」，不臆造。
- 数值必须与原文一致。"""


def _meta_block(meta: dict) -> str:
    return "\n".join(
        [
            f"标题：{meta.get('title', '')}",
            f"作者：{meta.get('authors', '')}",
            f"期刊/平台：{meta.get('journal', '')}",
            f"日期：{meta.get('published_date', '')}",
            f"DOI/ID：{meta.get('doi', '') or meta.get('id', '')}",
            f"URL：{meta.get('url', '')}",
        ]
    )


def build_paper_card(client, model, fulltext: str, meta: dict) -> str:
    user = f"{_meta_block(meta)}\n\n--- 正文（全文或摘要）---\n\n{_truncate(fulltext)}"
    return _chat(
        client,
        model,
        [
            {"role": "system", "content": PAPER_CARD_SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.0,
        max_tokens=16000,
    )


REVIEWER_SYSTEM = """你是审稿人，为一份手稿（论文全文或摘要）生成 Nature 风格的单审稿人评审。中文为主，技术术语保留英文。只基于提供的材料，绝不编造。

按以下结构输出（固定顺序）：

## Review setup
- **Input scope** [值]
- **Assessment boundary** [值]
- **Shared manuscript claim summary** [值]
- **Visible evidence base** [值]
- **Missing materials affecting confidence** [值]

## Reviewer 1
- **Overall assessment** [text]
- **Who would be interested in the results, and why** [text]
- **Major strengths** [text]
- **Major Concerns** [items]
- **Minor Comments** [items]
- **Technical failings that need to be addressed before the case is established** [IDs or summary]
- **Assessment against Nature-style criteria** [text，须显式覆盖 originality / scientific importance / interdisciplinary readership / technical soundness / readability for nonspecialists]
- **Recommendation posture** [text，如「supportive if technical concerns are resolved」「currently not established from the provided evidence」]

每个 Major Concern：
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes / No
- **Axis** [value]
- **Claim pointer** [忠实改写被质疑的claim或报告要素]
- **Evidence pointer** [section / figure / table，或 "location not provided"]
- **Concern** [text]
- **Why it matters** [text]
- **Resolution test** [text]

每个 Minor Comment：
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** [value]
- **Affected element** [value]
- **Evidence pointer** [value]
- **Issue** [text]
- **Required correction** [text]

## Risk / unsupported claims
- [列出不受支持或不可评估的声明]

规则：
- 证据指针只用 section/图/表名，材料未提供行号时写 "location not provided"，不编造行号。
- 区分「有支撑」「薄弱」「不可评估」。
- 不设 concern 数量下限；没有就写「None identified from the supplied material」。
- Blocking Yes 仅在当前材料无法支撑核心结论时标。
- 语气正式、直接、基于证据；不用讥讽或夸张。
- 不要写作者立场、rebuttal、编辑决定信；不要声称「该文属于 Nature」这一既定事实。
- 不用 em dash / en dash / 冒号作常规标点；保留 ID 与公式/引文中的标点。"""


def build_review(client, model, fulltext: str, meta: dict) -> str:
    user = f"{_meta_block(meta)}\n\n--- 正文（全文或摘要）---\n\n{_truncate(fulltext)}"
    return _chat(
        client,
        model,
        [
            {"role": "system", "content": REVIEWER_SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.0,
        max_tokens=12000,
    )
