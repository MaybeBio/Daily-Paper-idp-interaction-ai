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
    body = monitor.build_issue(rows_by_platform, "2026-01-01", "2026-01-07", analyses)
    assert "| 标题 | 作者 | 日期 | 评分 | 一句话 | 链接 |" in body
    assert "[A\\|B](http://orig)" in body
    assert "| 7 | 一句话 | [解析](papers/pubmed/1/index.html) |" in body


def test_analysis_for_missing_returns_default():
    assert monitor._analysis_for({"source": "pubmed", "id": "9"}, {})["score"] is None
