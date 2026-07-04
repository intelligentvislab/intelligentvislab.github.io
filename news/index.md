---
title: News
description: News and announcements from the Intelligent Visualization Lab at York University.
---

<style>
  .news-archive{ list-style:none; margin:0 0 28px; padding:0; }
  .news-archive li{
    background:#f1f6ff;
    border:1px solid #e7eefc;
    padding:12px 14px 10px;
    border-radius:10px;
    margin:0 0 10px;
    text-align:left;
  }
  .news-archive .news-text{
    font-size:.98rem;
    line-height:1.5;
    color:#1c1f23;
    text-decoration:none;
  }
  .news-archive a.news-text:hover{ color:#1f4e84; text-decoration:underline; }
  .news-archive .news-date{
    display:block;
    margin-top:6px;
    font-size:.88rem;
    color:#9aa3ad;
  }
  .news-year{
    font:700 1.25rem/1.3 Poppins,system-ui,sans-serif;
    color:#1c1f23;
    text-align:left;
    border-left:4px solid #2b6cb0;
    padding-left:8px;
    margin:28px 0 14px;
  }
</style>

# <i class="fas fa-newspaper"></i>News

All news and announcements from the lab, newest first.
{:.center}

{% assign items = site.data.news | sort: "date" | reverse %}
{% assign by_year = items | group_by_exp: "item", "item.date | date: '%Y'" %}
{% for year in by_year %}
<h2 class="news-year">{{ year.name }}</h2>
<ul class="news-archive">
  {% for n in year.items %}
  <li>
    {% if n.link %}
      <a class="news-text" href="{{ n.link }}">{{ n.text }}</a>
    {% else %}
      <span class="news-text">{{ n.text }}</span>
    {% endif %}
    <span class="news-date">{{ n.date | date: "%B %-d, %Y" }}</span>
  </li>
  {% endfor %}
</ul>
{% endfor %}
