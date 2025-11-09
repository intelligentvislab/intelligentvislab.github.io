---
title: Home
---

<!-- Local page styles (kept inline so you don't have to hunt for files) -->
<style>
  /* ===== Theme: Blue + Near-Black ===== */
  :root{
    --ink:#1c1f23;           /* near-black text */
    --muted:#5f6b76;         /* secondary text */
    --brand:#2b6cb0;         /* primary blue */
    --brand-ink:#1f4e84;     /* darker blue for hover */
    --bg:#f7f9fc;            /* page section background */
    --card:#ffffff;          /* cards */
    --line:#e6e8eb;          /* borders/separators */
    --tint:#edf2fa;          /* pale blue for news cards */
    --nav-h:78px;            /* header height */
  }

  body main { padding-top: 0 !important; }

  .wrap{max-width:1100px;margin:0 auto;padding:0 16px}

  /* ===== Hero ===== */
  .hero{
    background:var(--bg);
    margin-top:var(--nav-h);
    padding:40px 0 28px;
    border-radius:12px;
  }
  .hero h1{
    font:600 1.9rem/1.25 Poppins,system-ui,sans-serif;
    color:var(--ink); text-align:center; margin:0 0 10px;
    letter-spacing:.02em;
  }
  .hero p{
    font:400 1.05rem/1.6 Lora,Georgia,serif;
    color:var(--muted); max-width:840px; margin:0 auto; text-align:center;
  }

  /* ===== Two-column layout aligned at the top ===== */
  .grid{
    display:grid;
    grid-template-columns:1fr 300px;
    gap:24px;
    margin:20px 0 28px;
    align-items:start;
  }
  @media (max-width:980px){ .grid{grid-template-columns:1fr} }

  .section-title{
    font:700 1.35rem/1.25 Poppins,system-ui,sans-serif;
    color:var(--ink);
    margin:10px 0 16px;
    border-left:4px solid var(--brand);
    padding-left:10px;
  }

  /* ===== Theme cards ===== */
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
    margin:0 0 6px;
  }
  .theme p{margin:0 0 10px;color:var(--ink)}
  .theme img{width:100%;border-radius:10px;display:block;margin:8px 0 10px}
  .theme a{color:var(--brand)} .theme a:hover{color:var(--brand-ink)}

  /* ===== Sidebar ===== */
  .card{
    background:var(--card);
    border:1px solid var(--line);
    border-radius:12px;
    padding:12px;
    box-shadow:0 1px 0 rgba(0,0,0,.03);
  }
  .sidebar h3{
    font:800 1rem/1.2 Poppins,system-ui,sans-serif;
    margin:2px 0 10px;
    color:var(--brand);
    letter-spacing:.02em;
  }

  /* --- NEWS cards: soft blue, linked text, date footer --- */
  .news-list{ list-style:none; margin:0; padding:0; }

  .news-list li{
    background: var(--tint);
    border: 1px solid #dfe7f7;
    padding: 12px 14px 10px;
    border-radius: 10px;
    margin: 0 0 10px;
    display: flex;
    flex-direction: column;
    min-height: 72px;
  }

  .news-link{
    display:block;
    text-decoration:none;
    color:var(--ink);
  }
  .news-link:hover .news-text{
    color:var(--brand-ink);
    text-decoration:underline;
  }

  .news-text{
    font-size:.95rem;
    line-height:1.45;
    color:var(--ink);
  }

  .news-date{
    margin-top:auto;
    font-size:.85rem;
    color:#9aa3ad;
    letter-spacing:.01em;
  }

  /* ===== PEOPLE grid ===== */
  .person-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:8px;
  }
  .person-grid img{
    width:100%;
    border-radius:10px;
    display:block;
  }
</style>


<!-- HERO -->
<section class="hero">
  <div class="wrap">
    <h1>Connecting language, visualization, and intelligence to help humans see and think with data.</h1>
    <p>Our lab bridges <b>Natural Language Processing (NLP)</b> and <b>Information Visualization (Vis)</b>—two domains that have historically evolved separately—to advance language-based data interaction and reasoning that is more accessible, inclusive, and intelligent.</p>
  </div>
</section>

<div class="wrap">
  <div class="grid">
    <!-- LEFT COLUMN -->
    <main>
      <h2 class="section-title">Research Themes</h2>

      <!-- THEME 1 -->
      <article class="theme">
        <h3>LLMs for Visualization Understanding</h3>
        <p>Benchmarks and models for chart comprehension and visual data communication—e.g., ChartQA, Chart-to-Text, and ChartGemma—shaping how multimodal LLMs interpret and explain charts.</p>
        <img src="/images/teaser3.png" alt="Chart reasoning with multimodal LLMs">
        <p><b>Representative papers:</b></p>
        <ul>
          <li><a href="/research/?search=ChartQA">ChartQA: A Benchmark for Question Answering on Charts</a></li>
          <li><a href="/research/?search=Chart-to-Text">Chart-to-Text: From Charts to Natural Language</a></li>
          <li><a href="/research/?search=ChartGemma">ChartGemma: Efficient Multimodal LLMs for Chart Reasoning</a></li>
        </ul>
      </article>

      <!-- THEME 2 -->
      <article class="theme">
        <h3>Accessible & Inclusive Data Interaction</h3>
        <p>Human-centered, responsible visualization—bias/fairness, deception, and accessibility—to ensure diverse users can explore and communicate data effectively.</p>
        <img src="/images/teaser1.png" alt="Accessible and responsible visualization">
        <ul>
          <li><a href="/research/?search=Fairness">Mitigating Bias &amp; Deception in Visualization</a></li>
          <li><a href="/research/?search=Accessibility">Accessible Charts &amp; Data Narratives</a></li>
        </ul>
      </article>

      <!-- THEME 3 -->
      <article class="theme">
        <h3>Human–AI Interaction for Data Analysis</h3>
        <p>Agentic and interactive AI systems that collaborate with analysts: natural-language interfaces, dashboard QA, and user-adaptive visualizations for real analytical workflows.</p>
        <img src="/images/intervention2.png" alt="Agentic AI and dashboard question answering">
        <ul>
          <li><a href="/research/?search=DashboardQA">DashboardQA: Interactive Question Answering on Dashboards</a></li>
          <li><a href="/research/?search=NL%20Interaction">Natural-Language Interaction with Data &amp; Visualizations</a></li>
        </ul>
      </article>

      <!-- ABOUT -->
      <section class="card">
        The Intelligent Visualization Lab was created in 2019 when
        <a href="https://www.yorku.ca/enamulh/">Dr. Enamul Hoque Prince</a> joined York University.
        Our work sits at the intersection of NLP, visualization, and HCI; we design intelligent tools that make data analysis more natural, accessible, and responsible.
      </section>
    </main>

    <!-- RIGHT COLUMN -->
    <aside class="sidebar">
      <!-- NEWS -->
      <section class="card">
        <h3>NEWS</h3>
        <ul class="news-list">
          {% assign items = site.data.news | default: empty %}
          {% if items and items.size > 0 %}
            {% for n in items limit:6 %}
              <li>
                {% if n.link %}
                  <a class="news-link" href="{{ n.link }}">
                    <div class="news-text">{{ n.text }}</div>
                  </a>
                {% else %}
                  <div class="news-text">{{ n.text }}</div>
                {% endif %}
                {% if n.date %}
                  <div class="news-date">{{ n.date | date: "%b %Y" }}</div>
                {% endif %}
              </li>
            {% endfor %}
          {% else %}
            <li>
              <div class="news-text">New site launched — more updates soon.</div>
              <div class="news-date">{{ "now" | date: "%b %Y" }}</div>
            </li>
          {% endif %}
        </ul>
      </section>

      <!-- PEOPLE -->
      <section class="card" style="margin-top:12px">
        <h3>PEOPLE</h3>
        <div class="person-grid">
          <a href="/team"><img src="/images/people/sample1.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample2.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample3.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample4.jpg" alt="Team member"></a>
        </div>
        <div style="text-align:right;margin-top:8px"><a href="/team">See all →</a></div>
      </section>
    </aside>
  </div>
</div>
