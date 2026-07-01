---
title: 'DashboardQA: Benchmarking Multimodal Agents for Question Answering on Interactive Dashboards'
authors:
  - Aaryaman Kartha
  - Ahmed Masry
  - Mohammed Saidul Islam
  - Thinh Lang
  - Shadikur Rahman
  - Ridwan Mahbub
  - Mizanur Rahman
  - Mahir Ahmed
  - Md Rizwan Parvez
  - Enamul Hoque
  - Shafiq Joty
publisher: In Proceedings of the Conference on European Chapter of the ACL (EACL)
date: '2026-01-01'
link: https://arxiv.org/abs/2508.17398
image: images/publications/dashboardqa.png
extra-links:
  - type: PDF
    link: https://arxiv.org/pdf/2508.17398
  - type: Source
    link: https://github.com/vis-nlp/DashboardQA
---

Dashboards are powerful visualization tools for data-driven decision-making,
integrating multiple interactive views that allow users to explore, filter, and
navigate data. Unlike static charts, dashboards support rich interactivity, which
is essential for uncovering insights in real-world analytical workflows. However,
existing question-answering benchmarks for data visualizations largely overlook
this interactivity, focusing instead on static charts. This limitation severely
constrains their ability to evaluate the capabilities of modern multimodal agents
designed for GUI-based reasoning. To address this gap, we introduce DashboardQA,
the first benchmark explicitly designed to assess how vision-language GUI agents
comprehend and interact with real-world dashboards. The benchmark includes 405
question-answer pairs with interactive dashboards spanning five categories:
multiple-choice, factoid, hypothetical, multi-dashboard, and conversational. By
assessing a variety of leading closed- and open-source GUI agents, our analysis
reveals their key limitations, particularly in grounding dashboard elements,
planning interaction trajectories, and performing reasoning. Our findings indicate
that interactive dashboard reasoning is a challenging task overall for all the VLMs
evaluated. Even the top-performing agents struggle; for instance, the best agent
based on Gemini-Pro-2.5 achieves only 38.69% accuracy, while the OpenAI CUA agent
reaches just 22.69%, demonstrating the benchmark's significant difficulty. We
release DashboardQA at
[https://github.com/vis-nlp/DashboardQA](https://github.com/vis-nlp/DashboardQA).
