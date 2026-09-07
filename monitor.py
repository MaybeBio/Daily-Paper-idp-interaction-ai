#!/usr/bin/env python3
"""Standalone literature monitor.

Fetches metadata only (no PDF / full text) for the configured topic from
multiple platforms via the published `pyPaperFlow` package, writes one CSV and
one `_ids.txt` per platform under `<source>/YYYY/MM/`, and emits a markdown
issue body.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET

import httpx
import pandas as pd
import yaml

from pyPaperFlow.preprint.arxiv_fetcher import ArxivFetcher
from pyPaperFlow.preprint.biorxiv_fetcher import BioRxivFetcher
from pyPaperFlow.preprint.chemrxiv_fetcher import ChemRxivFetcher
from pyPaperFlow.pubmed.pubmed_fetcher import PubmedFetcher

COLUMNS = [
    "source", "id", "doi", "title", "authors", "abstract",
    "published_date", "journal", "url", "fetched_date",
]
PLATFORMS = ["pubmed", "arxiv", "biorxiv", "medrxiv", "chemrxiv"]

# arXiv's native backend sorts newest-first but pages the ENTIRE week's matches when
# max_results is unset — a rich OR-query hangs. Cap keeps only the freshest records.
ARXIV_MAX_RESULTS = 150


def parse_args():
    p = argparse.ArgumentParser(description="Fetch topic literature metadata and write CSV/ids/issue.")
    p.add_argument("--config", required=True, help="Path to config.yaml")
    p.add_argument("--out-dir", default=".", help="Root dir for CSV output (default: cwd)")
    p.add_argument("--window-days", type=int, default=None, help="Override config window_days")
    p.add_argument("--run-date", default=None, help="Run date YYYY-MM-DD (default: today)")
    p.add_argument("--issue-body", default=None, help="Write issue markdown to this path")
    return p.parse_args()


def load_config(path):
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if not isinstance(cfg, dict):
        raise ValueError("config must be a YAML mapping")
    return cfg


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return list(value)


def _strip_version(arxiv_id):
    return re.sub(r"v\d+$", "", (arxiv_id or "").strip())


def normalize_source_paper(rec, source, fetched_date):
    return {
        "source": source,
        "id": rec.source_id or "",
        "doi": rec.doi or "",
        "title": rec.title or "",
        "authors": "; ".join(_as_list(getattr(rec, "authors", None))),
        "abstract": rec.abstract or "",
        "published_date": rec.published_date or "",
        "journal": rec.journal or "",
        "url": rec.landing_url or "",
        "fetched_date": fetched_date,
    }


def normalize_pubmed(paper, fetched_date):
    pmid = paper.identity.pmid or ""
    journal = paper.source.journal_title
    if isinstance(journal, (tuple, list)):
        journal = journal[0] if journal else ""
    return {
        "source": "pubmed",
        "id": pmid,
        "doi": paper.identity.doi or "",
        "title": paper.identity.title or "",
        "authors": "; ".join(_as_list(paper.contributors.medline.get("full_names"))),
        "abstract": paper.content.abstract or "",
        "published_date": paper.source.pub_date or "",
        "journal": journal or "",
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
        "fetched_date": fetched_date,
    }


ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_NS = {"o": "http://a9.com/-/spec/opensearch/1.1/"}


def _arxiv_total_results(search_query):
    """Return arXiv's totalResults for a built search_query (0 on error/empty)."""
    try:
        resp = httpx.get(
            ARXIV_API,
            params={"search_query": search_query, "start": 0, "max_results": 1},
            timeout=30,
        )
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        el = root.find("o:totalResults", ARXIV_NS)
        return int(el.text) if el is not None and el.text else 0
    except Exception:
        return 0


def fetch_platform(platform, cfg, start, end, root_dir, fetched_date):
    query = cfg["platforms"][platform]["query"]
      
    if platform == "pubmed":
        email = (os.environ.get("ENTREZ_EMAIL") or "").strip()
        if not email:
            raise ValueError("ENTREZ_EMAIL env var is required for the pubmed platform")
        api_key = os.environ.get("NCBI_API_KEY") or ""
        dated = f'({query}) AND ("{start.replace("-", "/")}"[dp] : "{end.replace("-", "/")}"[dp])'
        fetcher = PubmedFetcher(root_dir=root_dir, entrez_email=email, api_key=api_key)
        meta = fetcher.query_search(dated)
        if meta.get("count", 0) == 0 or "webenv" not in meta:
            return []
        pmids = fetcher.get_pubmedIDs_from_query(meta, retmax=500)
        if not pmids:
            return []
        papers = fetcher.fetch_from_pmid_list(pmids, output_dir=root_dir)
        return [normalize_pubmed(p, fetched_date) for p in papers]

    if platform == "arxiv":
        max_results = cfg["platforms"][platform].get("max_results", ARXIV_MAX_RESULTS)
        # pyPaperFlow falls back to a looser query when the first page is empty; on a
        # genuinely empty week that fallback silently returns unrelated newest preprints.
        # Pre-flight the built query so a 0-hit week writes an empty CSV instead of noise.
        fetcher = ArxivFetcher(root_dir=root_dir)
        search_query = fetcher.build_query(query, start_date=start, end_date=end)
        if _arxiv_total_results(search_query) <= 0:
            records = []
        else:
            records = fetcher.search(query=query, max_results=max_results, start_date=start, end_date=end)
    elif platform in ("biorxiv", "medrxiv"):
        records = BioRxivFetcher(root_dir=root_dir, platform=platform).search(query=query, start_date=start, end_date=end)
    elif platform == "chemrxiv":
        records = ChemRxivFetcher(root_dir=root_dir).search(query=query, start_date=start, end_date=end)
    else:
        raise ValueError(f"unknown platform: {platform}")

    return [normalize_source_paper(r, platform, fetched_date) for r in records]


def _zotero_id(platform, row):
    if platform == "arxiv":
        return f"arXiv:{_strip_version(row['id'])}"
    return row["id"]


def write_platform(out_dir, platform, topic, date_str, rows):
    year, month, _ = date_str.split("-")
    d = os.path.join(out_dir, platform, year, month)
    os.makedirs(d, exist_ok=True)
    stem = f"{topic}_{date_str}"
    csv_path = os.path.join(d, stem + ".csv")
    ids_path = os.path.join(d, stem + "_ids.txt")

    df = pd.DataFrame(rows, columns=COLUMNS)
    df.to_csv(csv_path, index=False, quoting=csv.QUOTE_ALL, encoding="utf-8-sig")

    ids = [_zotero_id(platform, r) for r in rows]
    with open(ids_path, "w", encoding="utf-8") as f:
        f.write("\n".join(ids) + ("\n" if ids else ""))

    return csv_path, ids_path, len(rows)


def _short_authors(authors_str, limit=3):
    parts = [a.strip() for a in (authors_str or "").split(";") if a.strip()]
    if not parts:
        return ""
    if len(parts) <= limit:
        return "; ".join(parts)
    return "; ".join(parts[:limit]) + "; et al."


def build_issue(rows_by_platform):
    total = sum(len(v) for v in rows_by_platform.values())
    if total == 0:
        return ""
    lines = [f"本次抓取 {total} 篇", ""]
    for platform in PLATFORMS:
        rows = rows_by_platform.get(platform)
        if not rows:
            continue
        lines.append(f"## {platform}（{len(rows)}）")
        lines.append("")
        lines.append("| 标题 | 作者 | 日期 |")
        lines.append("|---|---|---|")
        for r in rows:
            title = (r["title"] or "untitled").replace("|", "\\|").replace("\n", " ")
            url = r["url"] or ""
            cell = f"[{title}]({url})" if url else title
            lines.append(f"| {cell} | {_short_authors(r['authors'])} | {(r['published_date'] or '')[:10]} |")
        lines.append("")
    return "\n".join(lines)


def main():
    args = parse_args()
    cfg = load_config(args.config)
    topic = (cfg.get("topic") or "topic").strip()
    window_days = args.window_days if args.window_days is not None else int(cfg.get("window_days", 7))
    run_date = args.run_date or dt.date.today().isoformat()
    start = (dt.date.fromisoformat(run_date) - dt.timedelta(days=window_days)).isoformat()

    platforms = [p for p in PLATFORMS if p in cfg.get("platforms", {})]
    if not platforms:
        print("No platforms configured.", file=sys.stderr)
        sys.exit(1)

    tmp = tempfile.mkdtemp(prefix="monitor_")
    rows_by_platform = {}
    failures = []
    try:
        for platform in platforms:
            try:
                rows = fetch_platform(platform, cfg, start, run_date, tmp, run_date)
                rows_by_platform[platform] = rows
                csv_path, _ids_path, n = write_platform(args.out_dir, platform, topic, run_date, rows)
                print(f"[{platform}] {n} records -> {csv_path}")
            except Exception as e:
                print(f"[{platform}] FAILED: {e}", file=sys.stderr)
                failures.append(platform)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if args.issue_body:
        with open(args.issue_body, "w", encoding="utf-8") as f:
            f.write(build_issue(rows_by_platform))

    if failures:
        print(f"Warning: {len(failures)} platform(s) failed: {failures}", file=sys.stderr)
        if len(failures) == len(platforms):
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
