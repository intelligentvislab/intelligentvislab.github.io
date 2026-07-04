"""Draft news entries from the Announcements section of Prof. Hoque's homepage.

Parses https://www.yorku.ca/enamulh/ for <div class="news"> blocks (skipping
ones inside HTML comments), converts each into a news entry, and appends the
ones not seen before to _data/news.yml. Seen items are remembered by hash in
.github/data/announcements-seen.txt so a rejected (closed) PR is never
re-proposed. Writes `count=<n>` to $GITHUB_OUTPUT.

Usage: news_from_announcements.py [local-html-file]   (file arg is for testing)
"""
import datetime
import hashlib
import html
import os
import re
import sys
import urllib.request

PAGE = "https://www.yorku.ca/enamulh/"
NEWS = "_data/news.yml"
SEEN = ".github/data/announcements-seen.txt"


def write_output(count):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"count={count}\n")


def parse_month_year(raw):
    raw = " ".join(raw.split())
    for fmt in ("%b %Y", "%B %Y"):
        try:
            return datetime.datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def normalize(text):
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", text.lower()).split())


def main():
    if len(sys.argv) > 1:
        page = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    else:
        req = urllib.request.Request(
            PAGE, headers={"User-Agent": "Mozilla/5.0 (IVL lab website news bot)"}
        )
        page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

    page = re.sub(r"<!--.*?-->", "", page, flags=re.S)  # drop commented-out items
    blocks = re.findall(r'<div class="news">(.*?)</div>', page, flags=re.S)

    with open(NEWS, encoding="utf-8") as f:
        news_txt = f.read()
    news_norm = normalize(news_txt)
    seen = set()
    if os.path.exists(SEEN):
        with open(SEEN, encoding="utf-8") as f:
            seen = {line.strip() for line in f if line.strip()}

    entries, new_hashes = [], []
    for block in blocks:
        m = re.search(r'<span class="date">(.*?)</span>', block, flags=re.S)
        date = parse_month_year(m.group(1)) if m else None
        if m:
            block = block.replace(m.group(0), "")
        link_m = re.search(r'<a\s[^>]*href="([^"]+)"', block)
        link = link_m.group(1).strip() if link_m else ""
        text = html.unescape(re.sub(r"<[^>]+>", " ", block))
        text = " ".join(text.split()).strip()
        if not text:
            continue
        digest = hashlib.sha1(f"{normalize(text)}|{date}".encode()).hexdigest()[:16]
        if digest in seen:
            continue
        if normalize(text) and normalize(text) in news_norm:
            new_hashes.append(digest)  # already posted manually; just remember it
            continue
        quoted = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
        lines = [f"- date: {date or datetime.date.today().isoformat()}", f"  text: {quoted}"]
        if link:
            lines.append(f"  link: {link}")
        entries.append("\n".join(lines))
        new_hashes.append(digest)

    if new_hashes:
        os.makedirs(os.path.dirname(SEEN), exist_ok=True)
        with open(SEEN, "a", encoding="utf-8") as f:
            f.write("".join(h + "\n" for h in new_hashes))

    if not entries:
        print("No new announcements.")
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
