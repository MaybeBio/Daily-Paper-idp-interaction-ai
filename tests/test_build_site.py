import json
import os

import build_site


def make_archive(root):
    d = os.path.join(root, "Archive", "pubmed", "2026", "09", "42437078")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "42437078.json"), "w", encoding="utf-8") as f:
        json.dump({"identity": {"title": "Paper Title", "pmid": "42437078"}, "metadata": {"entrez_date": "2026/09/01 00:00"}}, f, ensure_ascii=False)
    with open(os.path.join(d, "analysis.json"), "w", encoding="utf-8") as f:
        json.dump({
            "title": "Paper Title",
            "authors": "Alice; Bob",
            "published_date": "2026-09-01",
            "score": 8, "one_liner_zh": "一句话", "url": "http://u",
            "paper_page_path": "papers/pubmed/42437078/index.html",
            "has_fulltext": True, "fulltext_source": "pmc",
        }, f, ensure_ascii=False)
    with open(os.path.join(d, "paper-card.md"), "w", encoding="utf-8") as f:
        f.write("## 01 基本信息\n...")
    with open(os.path.join(d, "review.md"), "w", encoding="utf-8") as f:
        f.write("## Review setup\n...")


def test_load_archive_merges(tmp_path):
    make_archive(str(tmp_path))
    papers = build_site.load_archive(str(tmp_path))
    assert len(papers) == 1
    p = papers[0]
    assert p["title"] == "Paper Title"
    assert p["score"] == 8
    assert p["paper_page_path"] == "papers/pubmed/42437078/index.html"


def test_build_site_writes_outputs(tmp_path):
    make_archive(str(tmp_path))
    out = str(tmp_path)
    build_site.build_site(out)
    assert os.path.exists(os.path.join(out, "site", "index.html"))
    assert os.path.exists(os.path.join(out, "site", "archive.html"))
    assert os.path.exists(os.path.join(out, "site", "papers", "pubmed", "42437078", "index.html"))
    assert os.path.exists(os.path.join(out, "site", "data", "index.json"))
    with open(os.path.join(out, "site", "data", "index.json"), encoding="utf-8") as f:
        data = json.load(f)
    assert data["papers"][0]["title"] == "Paper Title"
