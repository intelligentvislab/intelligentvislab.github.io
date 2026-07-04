"""Draft news entries for publications newly added to _data/research-output.yml.

Usage: news_from_publications.py <base-git-sha>
Compares the publications list at <base-git-sha> with the working tree and
appends one news entry per new publication to _data/news.yml. Writes
`count=<n>` to $GITHUB_OUTPUT so the workflow knows whether to open a PR.
"""
import datetime
import os
import re
import subprocess
import sys

import yaml

PUBS = "_data/research-output.yml"
NEWS = "_data/news.yml"


def entry_key(e):
    return e.get("id") or e.get("title")


def write_output(count):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"count={count}\n")


def main():
    base = sys.argv[1]
    shown = subprocess.run(
        ["git", "show", f"{base}:{PUBS}"], capture_output=True, text=True
    )
    old = yaml.safe_load(shown.stdout) or [] if shown.returncode == 0 else []
    with open(PUBS, encoding="utf-8") as f:
        new = yaml.safe_load(f) or []

    old_keys = {entry_key(e) for e in old}
    added = [e for e in new if entry_key(e) not in old_keys]

    with open(NEWS, encoding="utf-8") as f:
        news_txt = f.read()

    today = datetime.date.today().isoformat()
    entries = []
    for e in added:
        title = str(e.get("title") or "").strip()
        if not title or title in news_txt:
            continue  # already announced (or nothing to announce)
        venue = ""
        m = re.search(r"\(([^()]+)\)\s*$", str(e.get("publisher") or "").strip())
        if m:
            venue = m.group(1).strip()
        year = str(e.get("date") or "")[:4]
        label = " ".join(x for x in (venue, year) if x)
        text = f"New paper: {title}" + (f" ({label})" if label else "")
        quoted = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
        lines = [f"- date: {today}", f"  text: {quoted}"]
        link = str(e.get("link") or "").strip()
        if link:
            lines.append(f"  link: {link}")
        entries.append("\n".join(lines))

    if not entries:
        print("No new publications to announce.")
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
