<p align="center">
  <img src="assets/banner.svg" width="100%" alt="BioLit Monitor —— 生物医学 × 计算 文献自动推送模板">
</p>

<h1 align="center">idp-interaction-ai — 无序蛋白互作 × AI</h1>

<p align="center">
  <strong>生物医学 × 计算交叉领域的文献自动推送模板</strong><br/>
  用 GitHub Actions 按周期自动追踪 <b>PubMed · arXiv · bioRxiv · medRxiv · chemRxiv</b> 上的最新文献，双份落盘并生成 Issue 周报，配合 Zotero 与 AI 工具完成筛选与精读。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/pyPaperFlow-powered-7C3AED?style=for-the-badge" alt="pyPaperFlow powered">
  <img src="https://img.shields.io/badge/platforms-PubMed%C2%B7arXiv%C2%B7bioRxiv%C2%B7medRxiv%C2%B7chemRxiv-0EA5E9?style=for-the-badge" alt="Supported platforms">
  <img src="https://img.shields.io/badge/schedule-weekly%C2%B7GitHub%20Actions-0D9488?style=for-the-badge" alt="Weekly via GitHub Actions">
  <img src="https://img.shields.io/badge/output-Archive%20JSON%20%2B%20Discovery%20CSV-4F46E5?style=for-the-badge" alt="Outputs">
  <img src="https://img.shields.io/badge/reading-Zotero%20ready-0D9488?style=for-the-badge" alt="Zotero reading">
</p>


> **模板即实例。** 仓库内的 `config.yaml` 已内置一套完整可跑的示例检索式 —— 拿到后你只需改**两处**：`config.yaml`（换成你的研究领域）与 `.github/workflows/monitor.yml`（推送周期）。工具与平台默认面向 **生物医学 × 计算**交叉课题。核心驱动为我们自研的文献检索获取工具 [pyPaperFlow](https://github.com/MaybeBio/pyPaperFlow)。

---

> 由自研文献推送模板[Daily-Paper-noAgent-Template](https://github.com/MaybeBio/Daily-Paper-noAgent-Template) 生成

无序蛋白/无序区（IDP/IDR）介导的蛋白质互作，含相分离与凝聚体；方法限定为深度学习、分子动力学与对接。