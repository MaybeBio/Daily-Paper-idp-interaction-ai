"""Static site generator: walk Archive/, render Jinja2 templates into site/."""
from __future__ import annotations

import datetime as dt
import json
import os
import shutil

import markdown as md
from jinja2 import Environment, FileSystemLoader, select_autoescape

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(HERE, "templates")


def _week_of(iso: str) -> str:
    try:
        d = dt.date.fromisoformat((iso or "")[:10])
    except ValueError:
        return "unknown"
    return f"{d.isocalendar()[0]}-W{d.isocalendar()[1]:02d}"


def load_archive(out_dir: str) -> list[dict]:
    papers = []
    archive_root = os.path.join(out_dir, "Archive")
    if not os.path.isdir(archive_root):
        return papers
    for source in sorted(os.listdir(archive_root)):
        src_dir = os.path.join(archive_root, source)
        if not os.path.isdir(src_dir):
            continue
        for year in sorted(os.listdir(src_dir)):
            for month in sorted(os.listdir(os.path.join(src_dir, year))):
                for sid in sorted(os.listdir(os.path.join(src_dir, year, month))):
                    paper_dir = os.path.join(src_dir, year, month, sid)
                    analysis_path = os.path.join(paper_dir, "analysis.json")
                    if not os.path.isfile(analysis_path):
                        continue
                    with open(analysis_path, encoding="utf-8") as f:
                        a = json.load(f)
                    papers.append({
                        "source": source,
                        "id": a.get("id", sid),
                        "title": a.get("title", ""),
                        "authors": a.get("authors", ""),
                        "published_date": a.get("published_date", ""),
                        "score": a.get("score"),
                        "one_liner_zh": a.get("one_liner_zh", ""),
                        "url": a.get("url", ""),
                        "has_fulltext": a.get("has_fulltext", False),
                        "fulltext_source": a.get("fulltext_source", ""),
                        "paper_page_path": a.get("paper_page_path", ""),
                        "paper_dir": paper_dir,
                        "week": _week_of(a.get("published_date", "")),
                    })
    papers.sort(key=lambda p: p.get("published_date") or "", reverse=True)
    return papers


def _md_to_html(text: str) -> str:
    return md.markdown(text or "", extensions=["tables", "fenced_code", "sane_lists"])


def _load_paper_files(paper_dir: str) -> tuple[str, str]:
    card = review = ""
    card_path = os.path.join(paper_dir, "paper-card.md")
    review_path = os.path.join(paper_dir, "review.md")
    if os.path.isfile(card_path):
        with open(card_path, encoding="utf-8") as f:
            card = _md_to_html(f.read())
    if os.path.isfile(review_path):
        with open(review_path, encoding="utf-8") as f:
            review = _md_to_html(f.read())
    return card, review


def build_site(out_dir: str) -> None:
    papers = load_archive(out_dir)
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
    )

    site_dir = os.path.join(out_dir, "site")
    data_dir = os.path.join(site_dir, "data")
    assets_dir = os.path.join(site_dir, "assets")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)

    # Weekly grouping for the archive page.
    weeks: dict[str, list[dict]] = {}
    for p in papers:
        weeks.setdefault(p["week"], []).append(p)
    for wk in weeks.values():
        wk.sort(key=lambda x: x.get("score") if x.get("score") is not None else -1, reverse=True)

    # This week = the latest week that has papers.
    latest_week = papers[0]["week"] if papers else "unknown"
    this_week = [p for p in papers if p["week"] == latest_week]
    this_week.sort(key=lambda x: x.get("score") if x.get("score") is not None else -1, reverse=True)

    # Per-paper pages.
    for p in papers:
        card_html, review_html = _load_paper_files(p["paper_dir"])
        page = env.get_template("paper.html").render(paper=p, card_html=card_html, review_html=review_html)
        page_path = os.path.join(site_dir, p["paper_page_path"])
        os.makedirs(os.path.dirname(page_path), exist_ok=True)
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(page)

    # Index + archive + data.
    with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(env.get_template("index.html").render(week=latest_week, papers=this_week, total=len(papers)))
    with open(os.path.join(site_dir, "archive.html"), "w", encoding="utf-8") as f:
        f.write(env.get_template("archive.html").render(weeks=weeks, total=len(papers)))
    with open(os.path.join(data_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"latest_week": latest_week, "papers": papers}, f, ensure_ascii=False, indent=2)
    _write_style(assets_dir)


def _write_style(assets_dir: str) -> None:
    css = os.path.join(TEMPLATES, "assets", "style.css")
    if os.path.isfile(css):
        shutil.copy(css, os.path.join(assets_dir, "style.css"))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build the static site from Archive/.")
    parser.add_argument("--out-dir", default=".", help="Repo root")
    args = parser.parse_args()
    build_site(args.out_dir)
