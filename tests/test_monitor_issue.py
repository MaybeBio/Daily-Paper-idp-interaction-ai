import monitor


def test_build_issue_six_columns():
    rows_by_platform = {
        "pubmed": [
            {
                "source": "pubmed", "id": "1", "title": "A|B", "authors": "X; Y; Z; W",
                "published_date": "2026-01-01", "url": "http://orig",
            }
        ],
        "arxiv": [], "biorxiv": [], "chemrxiv": [], "medrxiv": [],
    }
    analyses = {
        ("pubmed", "1"): {
            "score": 7, "one_liner_zh": "一句话", "paper_page_path": "papers/pubmed/1/index.html"
        }
    }
    body = monitor.build_issue(rows_by_platform, "2026-01-01", "2026-01-07", analyses,
                               site_base_url="https://MaybeBio.github.io/Daily-Paper-idp-interaction-ai")
    assert "| 标题 | 作者 | 日期 | 评分 | 一句话 | 链接 |" in body
    assert "[A\\|B](http://orig)" in body
    assert "| 7 | 一句话 | [解析](https://MaybeBio.github.io/Daily-Paper-idp-interaction-ai/papers/pubmed/1/index.html) |" in body


def test_build_issue_link_falls_back_to_relative():
    rows_by_platform = {
        "pubmed": [
            {
                "source": "pubmed", "id": "1", "title": "T", "authors": "A",
                "published_date": "2026-01-01", "url": "http://orig",
            }
        ],
        "arxiv": [], "biorxiv": [], "chemrxiv": [], "medrxiv": [],
    }
    analyses = {("pubmed", "1"): {"score": 7, "one_liner_zh": "", "paper_page_path": "papers/pubmed/1/index.html"}}
    body = monitor.build_issue(rows_by_platform, "2026-01-01", "2026-01-07", analyses)
    assert "[解析](papers/pubmed/1/index.html)" in body


def test_analysis_for_missing_returns_default():
    assert monitor._analysis_for({"source": "pubmed", "id": "9"}, {})["score"] is None


def test_run_agent_pipeline_all_collects_results(monkeypatch):
    import threading
    import time

    rows = [{"source": "pubmed", "id": str(i)} for i in range(12)]
    cfg = {"llm": {"concurrency": 4}}
    active = {"n": 0, "max": 0}
    lock = threading.Lock()

    def fake_pipeline(row, cfg, out_dir):
        with lock:
            active["n"] += 1
            active["max"] = max(active["max"], active["n"])
        time.sleep(0.02)
        with lock:
            active["n"] -= 1
        i = int(row["id"])
        return {"score": i, "id": row["id"]} if i % 2 == 0 else None

    monkeypatch.setattr(monitor, "run_agent_pipeline", fake_pipeline)
    analyses = monitor.run_agent_pipeline_all(rows, cfg, "/tmp")

    assert set(analyses) == {("pubmed", str(i)) for i in range(0, 12, 2)}
    assert active["max"] > 1


def test_run_agent_pipeline_all_skips_when_llm_disabled(monkeypatch):
    calls = []

    def fake_pipeline(row, cfg, out_dir):
        calls.append(row["id"])
        return {"score": 1}

    monkeypatch.setattr(monitor, "run_agent_pipeline", fake_pipeline)
    analyses = monitor.run_agent_pipeline_all([{"source": "pubmed", "id": "1"}], {}, "/tmp")
    assert analyses == {}
    assert calls == []
