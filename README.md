# idp-interaction-ai — 无序蛋白互作（AI×模拟）（Intrinsically Disordered Protein Interactions）

无序蛋白/无序区（IDP/IDR）介导的蛋白质互作，含相分离/凝聚体；方法限定为深度学习、分子动力学、对接。

每周自动从 PubMed / arXiv / bioRxiv / medRxiv / chemRxiv 抓取本课题最新文献**元数据**，commit+push 回本仓库，并开一条 Issue 表格提醒。你在本地用 Zotero 按 `_ids.txt` 批量导入阅读筛选。

## 本仓库结构

- `monitor.py` — 独立脚本：读 `config.yaml`，对每个平台跑检索，规范化后落盘 CSV + `_ids.txt`，并生成 Issue 正文。
- `config.yaml` — 本课题检索配置（课题短名 / 时间窗口 / 每平台一条布尔检索式；PubMed 邮箱和 API key 走环境变量，不写进文件）。
- `.github/workflows/monitor.yml` — 每周一 09:23 UTC 自动运行 + `workflow_dispatch` 手动触发；`pip install pyPaperFlow` 后跑脚本 → commit+push → 有结果时开 Issue。

> 平台 query 语法与调优历史见母仓 `docs/topics-catalog.md` 与该课题 `topics/idp-interaction-ai/test-notes.md`。

## 产出

```
pubmed/{year}/{month}/idp-interaction-ai_{date}.csv      # 固定 10 列元数据
pubmed/{year}/{month}/idp-interaction-ai_{date}_ids.txt  # 每行一个标识符，供 Zotero「按标识符添加」
arxiv/  biorxiv/  medrxiv/  chemrxiv/ ...   # 各平台同构
```

- 每平台独立、原样落盘：**不做跨平台去重、不判新增**——重复与否留给 Zotero 处理。
- 某平台当周无命中 → 仍写仅表头 CSV（快照存在）；arXiv 0 命中由 pre-flight 守卫写空 CSV。

## 配置密钥（PubMed）

PubMed 需要邮箱和可选的 NCBI API key，**不能写进 git**，改用环境变量注入：

- 本地：`export ENTREZ_EMAIL=you@example.com`（可选 `export NCBI_API_KEY=...`）
- GitHub Actions：仓库 **Settings → Secrets and variables → Actions → New repository secret**，添加 `ENTREZ_EMAIL`（必填）与 `NCBI_API_KEY`（可选）两个 secret。

## 本地运行

```bash
pip install pyPaperFlow
export ENTREZ_EMAIL=you@example.com
python monitor.py --config config.yaml --out-dir . --issue-body /tmp/issue.md
```

改时间窗口：`--window-days 1`（或改 `config.yaml` 的 `window_days`）。
