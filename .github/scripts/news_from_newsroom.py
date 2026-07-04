"""Draft news entries from York LA&PS newsroom articles mentioning Prof. Hoque.

Fetches the newsroom RSS feed, keeps items whose title/summary/body mention
"Hoque", skips items whose URL already appears in _data/news.yml, and appends
the rest as news entries. Writes `count=<n>` to $GITHUB_OUTPUT.
"""
import datetime
import html
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED = "https://www.yorku.ca/laps/newsroom/feed/"
NEWS = "_data/news.yml"
MENTION = re.compile(r"hoque", re.I)
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}


def write_output(count):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"count={count}\n")


def main():
    req = urllib.request.Request(
        FEED, headers={"User-Agent": "Mozilla/5.0 (IVL lab website news bot)"}
    )
    data = urllib.request.urlopen(req, timeout=30).read()
    root = ET.fromstring(data)

    with open(NEWS, encoding="utf-8") as f:
        news_txt = f.read()

    entries = []
    for item in root.iter("item"):
        title = html.unescape((item.findtext("title") or "").strip())
        link = (item.findtext("link") or "").strip()
        summary = item.findtext("description") or ""
        body = item.findtext("content:encoded", default="", namespaces=NS) or ""
        if not title or not link:
            continue
        if not MENTION.search(" ".join((title, summary, body))):
            continue
        # dedupe by URL path so fragment/query differences don't matter
        path = re.sub(r"^https?://[^/]+", "", link).split("#")[0].rstrip("/")
        if path and path in news_txt:
            continue
        try:
            date = parsedate_to_datetime(item.findtext("pubDate")).date().isoformat()
        except Exception:
            date = datetime.date.today().isoformat()
        text = f"In the news: {title}"
        quoted = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
        entries.append(f"- date: {date}\n  text: {quoted}\n  link: {link}")

    if not entries:
        print("No new newsroom mentions.")
        write_output(0)
        return

    with open(NEWS, "a", encoding="utf-8") as f:
        f.write("\n".join(entries) + "\n")
    print(f"Drafted {len(entries)} news entr{'y' if len(entries) == 1 else 'ies'}:")
    for e in entries:
        print(e)
    write_output(len(entries))


if __name__ == "__main__":
    main()
