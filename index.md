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
  .wrap{ max-width:1100px; margin:0 auto; padding:0 16px; }

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
    text-transform:none;          /* disables all-caps to soften tone */
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
    grid-template-columns:1fr 300px;
    gap:24px;
    margin:20px 0 28px;
    align-items:start;
  }
  @media (max-width:980px){ .grid{ grid-template-columns:1fr; } }

  /* Section titles (left aligned accent) */
  .section-title,
  .side-title{
    font:700 1.35rem/1.25 Poppins,system-ui,sans-serif;
    color:var(--ink);
    margin:10px 0 16px;
    text-align:left;
    border-left:4px solid var(--brand);
    padding-left:10px;
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
    margin:0 0 6px;
  }
  .theme p{ margin:0 0 10px; color:var(--ink); }
  .theme img{ width:100%; border-radius:10px; display:block; margin:8px 0 10px; }
  .theme a{ color:var(--brand); }
  .theme a:hover{ color:var(--brand-ink); }

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
    <h1>Connecting language, visualization, and intelligence to help humans see and think with data.</h1>
<p>
             Established in <b>2019</b> at <a href="https://www.yorku.ca/" target="_blank" rel="noopener noreferrer"><b>York University</b></a>, our lab bridges <b>Natural Language Processing (NLP)</b> and <b>Information Visualization (Vis)</b>—two domains that have historically evolved separately—to advance language-based data interaction and reasoning that is more accessible, inclusive, and intelligent.

</p>
  </div>
</section>

<div class="wrap">
  <div class="grid">
    <!-- LEFT COLUMN -->
    <main>
      <h2 class="section-title">RESEARCH THEMES</h2>

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

      <article class="theme">
        <h3>Accessible & Inclusive Data Interaction</h3>
        <p>Human-centered, responsible visualization—bias/fairness, deception, and accessibility—to ensure diverse users can explore and communicate data effectively.</p>
        <img src="/images/teaser1.png" alt="Accessible and responsible visualization">
        <ul>
          <li><a href="/research/?search=Fairness">Mitigating Bias &amp; Deception in Visualization</a></li>
          <li><a href="/research/?search=Accessibility">Accessible Charts &amp; Data Narratives</a></li>
        </ul>
      </article>

      <article class="theme">
        <h3>Human–AI Interaction for Data Analysis</h3>
        <p>Agentic and interactive AI systems that collaborate with analysts: natural-language interfaces, dashboard QA, and user-adaptive visualizations for real analytical workflows.</p>
        <img src="/images/intervention2.png" alt="Agentic AI and dashboard question answering">
        <ul>
          <li><a href="/research/?search=DashboardQA">DashboardQA: Interactive Question Answering on Dashboards</a></li>
          <li><a href="/research/?search=NL%20Interaction">Natural-Language Interaction with Data &amp; Visualizations</a></li>
        </ul>
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

<!--       <section class="people-wrap" style="margin-top:12px">
        <h3 class="side-title" style="border-left-color:#0b7a75;">PEOPLE</h3>
        <div class="person-grid">
          <a href="/team"><img src="/images/people/sample1.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample2.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample3.jpg" alt="Team member"></a>
          <a href="/team"><img src="/images/people/sample4.jpg" alt="Team member"></a>
        </div>
        <div class="people-footer"><a href="/team">See all →</a></div>
      </section> -->
    </aside>
  </div>
</div>
