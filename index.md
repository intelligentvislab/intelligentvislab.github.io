---
title: Home
---

<style>
  /* ===== Theme: Blue + Near-Black ===== */
  :root{
    --ink:#1c1f23;
    --muted:#5f6b76;
    --brand:#2b6cb0;
    --brand-ink:#1f4e84;
    --bg:#f7f9fc;
    --card:#ffffff;
    --line:#e6e8eb;
    --tint:#f1f6ff;  /* very soft blue tint for news items */
    --nav-h:78px;
  }
  @media (max-width:980px){ :root{ --nav-h:64px; } }

  /* Containers */
  .wrap{ max-width:1400px; margin:0 auto;  }

  /* HERO */
  .hero{
    background:var(--bg);
    margin-top:var(--nav-h);
    padding:5px 0 10px;
    border-radius:12px;
  }
  .hero h1{
    font:600 1.9rem/1.25 Poppins,system-ui,sans-serif;
    color:var(--ink);
    text-align:center;
    margin:0 0 10px;
    letter-spacing:.02em;
    text-transform:none;
  }
  .hero p{
    font:400 1.05rem/1.6 Lora,Georgia,serif;
    color:var(--muted);
    max-width:840px;
    margin:0 auto;
    text-align:center;
  }

  /* Two-column layout */
  .grid{
    display:grid;
  grid-template-columns: minmax(0, 1.25fr) 300px; /* main gets more space */
    gap:24px;
    margin:20px 0 28px;
    align-items:start;
  }
  @media (max-width:980px){
    .grid{ grid-template-columns:1fr; }
  }

  /* Section titles (left aligned accent) */
  .section-title,
  .side-title{
    font:700 1.35rem/1.25 Poppins,system-ui,sans-serif;
    color:var(--ink);
    margin:1px 0 16px;
    text-align:left;
    border-left:4px solid var(--brand);
    padding-left:1px;
  }

  /* Themes (left column cards) */
  .theme{
    background:var(--card);
    border:1px solid var(--line);
    border-radius:12px;
    padding:16px;
    margin:0 0 16px;
    box-shadow:0 1px 0 rgba(0,0,0,.03);
  }
  .theme h3{
    font:700 1.1rem/1.3 Poppins,system-ui,sans-serif;
    color:var(--brand);
    margin:0 0 4px;
  }
  .theme-subtitle{
    margin:0 0 1px;
    color:var(--ink);
    font-size:.96rem;
  }

  /* Side-by-side layout inside each theme */
  .theme-layout{
    display:grid;
    grid-template-columns:minmax(0, 1.1fr) minmax(0, 1.4fr);
    gap:16px;
    align-items:start;
  }
  @media (max-width:780px){
    .theme-layout{
      grid-template-columns:1fr;
    }
  }

  .theme-media img{
    width:100%;
    border-radius:10px;
    display:block;
  }

  .theme-papers-header{
    font:600 .95rem/1.4 Poppins,system-ui,sans-serif;
    color:var(--ink);
    margin:0 0 6px;
  }

  .theme-papers-list{
    max-height:220px;          /* scrollable area */
    overflow-y:auto;
    padding-right:4px;
  }
  

  .theme-papers-list ul{
    list-style:none;
    margin:0;
    padding:0;
  }
.theme-papers-list li{
  margin: 0 0 6px;
  padding: 3px 4px;
  background: #f9fbff;              /* subtle light-blue tint */
  border: 1px solid #e3e8f0;         /* very light border */
  border-radius: 6px;
  font-size: .82rem;
  line-height: 1.35;
  transition: background .18s ease, border-color .18s ease;
}
.theme-papers-list li:hover{
  background: #f1f6ff;              /* slightly more visible tint */
  border-color: #c9d6ee;
}
.theme-papers-list a{
  color: var(--brand);
  text-decoration: none;
}
.theme-papers-list a:hover{
  color: var(--brand-ink);
  text-decoration: underline;
}
  .theme a{
    color:var(--brand);
    text-decoration:none;
  }
  .theme a:hover{
    color:var(--brand-ink);
    text-decoration:underline;
  }

  /* ===== NEWS ===== */
  .news-wrap{ padding:0; background:transparent; border:none; box-shadow:none; }
  .news-list{ list-style:none; margin:0; padding:0; }
  .news-list li{
    background:var(--tint);
    border:1px solid #e7eefc;
    padding:12px 12px 10px;
    border-radius:10px;
    margin:0 0 10px;
  }
  .news-link{
    display:inline-block;
    font-size:.95rem;
    line-height:1.45;
    color:var(--ink);
    text-decoration:none;
  }
  .news-link:hover{ color:var(--brand-ink); text-decoration:underline; }
  .news-date{
    display:block;
    margin-top:8px;
    font-size:.9rem;
    color:#9aa3ad;
    letter-spacing:.01em;
  }

  /* ===== PEOPLE ===== */
  .people-wrap{ padding:0; background:transparent; border:none; box-shadow:none; }
  .person-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:8px;
    margin-bottom:8px;
  }
  .person-grid img{
    width:100%;
    border-radius:10px;
    display:block;
  }
  .people-footer{
    text-align:right;
    font-size:.9rem;
    margin-top:4px;
  }
  .people-footer a{
    color:var(--brand);
    text-decoration:none;
  }
  .people-footer a:hover{
    color:var(--brand-ink);
    text-decoration:underline;
  }

  body main{ padding-top:0 !important; }
</style>

<!-- HERO -->
<section class="hero">
  <div class="wrap">
    <h1>Building multimodal AI that sees, reasons, and communicates with data</h1>
    <p>
      Established in <b>2019</b> at <a href="https://www.yorku.ca/" target="_blank" rel="noopener noreferrer"><b>York University</b></a>, our lab bridges <b>Natural Language Processing (NLP)</b> and <b>Information Visualization (Vis)</b>—two domains that have historically evolved separately—to advance language-based data interaction and reasoning that is more accessible, inclusive, and intelligent.
    </p>  
    <!-- <h1>Connecting language, visualization, and intelligence to help humans see and think with data.</h1>
    <p>
      Established in <b>2019</b> at <a href="https://www.yorku.ca/" target="_blank" rel="noopener noreferrer"><b>York University</b></a>, our lab bridges <b>Natural Language Processing (NLP)</b> and <b>Information Visualization (Vis)</b>—two domains that have historically evolved separately—to advance language-based data interaction and reasoning that is more accessible, inclusive, and intelligent.
    </p> -->
  </div>
</section>

<div class="wrap">
  <div class="grid">
    <!-- LEFT COLUMN -->
    <main>
      <h2 class="section-title">RESEARCH THEMES</h2>

      <!-- THEME 1 -->
      <article class="theme">
        <h3>Multimodal LLMs for Visualization Understanding and Generation</h3>
        <p class="theme-subtitle">
          Benchmarks and models for chart comprehension, narrative generation, and visual data communication—shaping how multimodal LLMs interpret, explain, and generate visualizations from and for real analytic workflows.
        </p>
        <div class="theme-layout">
          <div class="theme-media">
            <img src="/images/chart-tasks.png" alt="Multimodal LLMs for chart and visualization reasoning">
          </div>
          <div class="theme-papers">
            <p class="theme-papers-header">Representative papers</p>
            <div class="theme-papers-list">
              <ul>
                <li><a href="/research/?search=Text2Vis">Text2Vis: Generating Multimodal Visualizations from Natural Language (EMNLP 2025)</a></li>
                <li><a href="/research/?search=DataNarrative">DataNarrative: Automated data-driven storytelling with visualizations and texts (EMNLP 2024)</a></li>
                <li><a href="/research/?search=ChartGemma">ChartGemma: Visual instruction-tuning for chart reasoning in the wild (COLING 2025)</a></li>
                <li><a href="/research/?search=ChartQA">ChartQA: A benchmark for question answering about charts with visual and logical reasoning (ACL 2022)</a></li>
                <li><a href="/research/?search=Chart-to-Text">Chart-to-Text: A Large-Scale Benchmark for Chart Summarization (ACL 2022)</a></li>
                <li><a href="/research/?search=BigCharts-R1">BigCharts-R1: Visual Reinforcement Learning for Chart Reasoning (COLM 2025)</a></li>
              </ul>
            </div>
          </div>
        </div>
      </article>

      <!-- THEME 2 -->
      <article class="theme">
        <h3>Agentic AI for Analytic Workflows</h3>
        <p class="theme-subtitle">
          Building multimodal agents that plan actions, interact with analytic tools, refine outputs, and collaborate with humans across realistic, end-to-end data workflows.
        </p>
        <div class="theme-layout">
          <div class="theme-media">
            <img src="/images/GUIAgent.gif" alt="Agentic AI operating on analytic dashboards and tools">
          </div>
          <div class="theme-papers">
            <p class="theme-papers-header">Representative papers</p>
            <div class="theme-papers-list">
              <ul>
                <li><a href="/research/?search=DashboardQA">DashboardQA: Benchmarking Multimodal Agents for Interactive Dashboards (2025)</a></li>
                <li><a href="/research/?search=Text2Vis">Text2Vis: Agentic Refinement for Visualization Generation via an Actor–Critic Framework (EMNLP 2025)</a></li>
                <li><a href="/research/?search=DataNarrative">DataNarrative: Narrative Construction via Multi-Agent Planner–Evaluator Systems (EMNLP 2024)</a></li>
              </ul>
            </div>
          </div>
        </div>
      </article>

      <!-- THEME 3 -->
      <article class="theme">
        <h3>Accessible, Inclusive &amp; Responsible VLMs for Visualization</h3>
        <p class="theme-subtitle">
          Ensuring analytic AI systems are fair, transparent, robust to deceptive designs, and supportive of users with diverse abilities, literacy levels, and cultural backgrounds.
        </p>
        <div class="theme-layout">
          <div class="theme-media">
            <img src="/images/teaser1.png" alt="Accessible, inclusive, and responsible visualization with VLMs">
          </div>
          <div class="theme-papers">
            <p class="theme-papers-header">Representative papers</p>
            <div class="theme-papers-list">
              <ul>
                <li><a href="/research/?search=SeeChart">SeeChart: Accessible Visualizations for Blind and Low-Vision Users (IUI 2023)</a></li>
                <li><a href="/research/?search=DeceptionVis">DeceptionVis: The Perils of Chart Deception for Vision-Language Models (IEEE VIS 2025 — Best Paper)</a></li>
                <li><a href="/research/?search=Fair%20Narratives">From Charts to Fair Narratives: Uncovering Geo-Economic Bias in Chart-to-Text (EMNLP 2025)</a></li>
                <li><a href="/research/?search=Judging%20the%20Judges">Judging the Judges: Reliability of VLMs as Chart Reasoning Evaluators (ACL 2025, Industry Track)</a></li>
              </ul>
            </div>
          </div>
        </div>
      </article>

      <!-- THEME 4 -->
      <article class="theme">
        <h3>Human-AI Alignment for Co-Creative Data Intelligence</h3>
        <p class="theme-subtitle">
          Designing generative analytic interfaces and collaboration modes that align AI reasoning with human goals, critique, and creativity in real data analysis settings.
        </p>
        <div class="theme-layout">
          <div class="theme-media">
            <img src="/images/intervention2.png" alt="Human–AI collaboration and co-creative analytic interfaces">
          </div>
          <div class="theme-papers">
            <p class="theme-papers-header">Representative papers</p>
            <div class="theme-papers-list">
              <ul>
                <li><a href="/research/?search=Sneak%20Pique">Sneak Pique: Autocompletion as a Data Discovery Scaffold (UIST 2020)</a></li>
                <li><a href="/research/?search=evizeon">evizeon: Applying Pragmatics Principles for Visual Analytics Interaction (TVCG 2017)</a></li>
              </ul>
            </div>
          </div>
        </div>
      </article>

      <!-- THEME 5 -->
      <article class="theme">
        <h3>Language Understanding, Summarization, and Evaluation</h3>
        <p class="theme-subtitle">
          Advancing question answering, summarization, domain adaptation, and trustworthy evaluation methods that strengthen the foundations of language-driven analytics.
        </p>
        <div class="theme-layout">
          <div class="theme-media">
            <img src="/images/teaser3.png" alt="Language understanding, summarization, and evaluation for analytics">
          </div>
          <div class="theme-papers">
            <p class="theme-papers-header">Representative papers</p>
            <div class="theme-papers-list">
              <ul>
                <li><a href="/research/?search=LLM%20Evaluation%20Survey">A Systematic Survey and Critical Review on Evaluating Large Language Models (EMNLP 2024)</a></li>
                <li><a href="/research/?search=Biomedical%20LLM-as-the-Judge">Improving Automatic Evaluation of LLMs in Biomedical Relation Extraction via LLMs-as-the-Judge (ACL 2025)</a></li>
                <li><a href="/research/?search=Open-RAG">Open-RAG: Enhanced Retrieval-Augmented Reasoning with Open-Source LLMs (EMNLP 2024)</a></li>
                <li><a href="/research/?search=Domain%20Adaptation%20Query-Focused%20Abstractive%20Summarization">Domain Adaptation with Pre-Trained Transformers for Query-Focused Abstractive Text Summarization (Computational Linguistics 2022)</a></li>
              </ul>
            </div>
          </div>
        </div>
      </article>
    </main>

    <!-- RIGHT COLUMN -->
    <aside class="sidebar">
      <section class="news-wrap">
        <h3 class="side-title">NEWS</h3>
        <ul class="news-list">
          {% assign items = site.data.news | default: empty %}
          {% if items and items.size > 0 %}
            {% for n in items limit:6 %}
              <li>
                {% if n.link %}
                  <a class="news-link" href="{{ n.link }}">{{ n.text }}</a>
                {% else %}
                  <span class="news-link">{{ n.text }}</span>
                {% endif %}
                {% if n.date %}<span class="news-date">{{ n.date | date: "%b %Y" }}</span>{% endif %}
              </li>
            {% endfor %}
          {% else %}
            <li>
              <span class="news-link">New site launched — more updates soon.</span>
              <span class="news-date">{{ "now" | date: "%b %Y" }}</span>
            </li>
          {% endif %}
        </ul>
      </section>

      <!--
      <section class="people-wrap" style="margin-top:12px">
        <h3 class="side-title" style="border-left-color:#0b7a75;">PEOPLE</h3>
        <div class="person-grid">
          <a href="/team"><img src="/images/people/sample1.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample2.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample3.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample4.jpg" alt="Team member"></a>
        </div>
        <div class="people-footer"><a href="/team">See all →</a></div>
      </section>
      -->
    </aside>
  </div>
</div>