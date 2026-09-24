#!/usr/bin/env python3
"""Capture a public Gemini share page as verbatim Markdown.

Gemini share pages render in the browser, so a plain fetch returns only the
sign-in shell. This script dumps the rendered DOM with headless Chrome, keeps
only the conversation (each prompt's ``user-query-content`` and each reply's
``message-content``), restores math from the ``data-math`` attributes, and
converts the result to GitHub Markdown with pandoc.

The raw DOM never enters the repo; its sha256 goes in the file header and in
MANIFEST.md so a later capture can be compared against it.

Usage (system python3, which has bs4 + lxml; pandoc on PATH):

    /usr/bin/python3 capture_gemini_share.py SHORT_ID OUT.md --raw-dir DIR
    /usr/bin/python3 capture_gemini_share.py SHORT_ID OUT.md --from-raw FILE.html

``--from-raw`` re-extracts from a saved dump, which is how the idempotence
check runs without touching the network.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote

from bs4 import BeautifulSoup, Comment, NavigableString

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SHARE = "https://share.gemini.google/{}"

# Interface elements that sit inside a reply but are not part of what the
# model wrote. Each is counted before removal so nothing disappears silently.
CHROME_SELECTORS = [
    "button",
    "mat-icon",
    "gem-icon",
    "gem-button",
    "gem-icon-button",
    "gem-popover",
    "sources-carousel",
    "sources-carousel-inline",
    "source-inline-chip",
    "retry-without-tool-button",
    "immersive-entry-chip",
    "model-thoughts",
    ".cdk-visually-hidden",
    ".code-block-decoration",
    ".table-footer",
    ".export-sheets-button-container",
    "processing-state",
]


def chrome_version() -> str:
    out = subprocess.run([CHROME, "--version"], capture_output=True, text=True)
    return out.stdout.strip()


def pandoc_version() -> str:
    out = subprocess.run(["pandoc", "--version"], capture_output=True, text=True)
    return out.stdout.splitlines()[0].strip()


def dump_dom(url: str, budget_ms: int) -> str:
    """Render ``url`` in headless Chrome and return the serialized DOM.

    Chrome's --dump-dom writes the DOM once the virtual-time budget runs out
    but the process does not always exit, so the whole process group is
    killed after a wall-clock limit. The DOM goes to a file rather than a
    pipe: a Chrome helper can outlive the kill and hold a pipe open forever.
    """
    with tempfile.TemporaryDirectory(prefix="gemcap-") as profile:
        dom_path = os.path.join(profile, "dom.html")
        with open(dom_path, "wb") as dom:
            proc = subprocess.Popen(
                [CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
                 "--no-default-browser-check", f"--user-data-dir={profile}",
                 "--window-size=1400,4000", f"--virtual-time-budget={budget_ms}",
                 "--dump-dom", url],
                stdout=dom, stderr=subprocess.DEVNULL, start_new_session=True)
            try:
                proc.wait(timeout=30 + budget_ms // 1000)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                subprocess.run(["pkill", "-9", "-f", profile])
                proc.wait(timeout=10)
        with open(dom_path, "rb") as dom:
            out = dom.read()
    html = out.decode("utf-8", "replace")
    if "</html>" not in html or "share-turn-viewer" not in html:
        raise SystemExit(f"incomplete DOM for {url} ({len(html)} bytes)")
    return html


def _math_node(soup, tex: str, display: bool, store: list):
    """Swap a math node for a plain-text token; the TeX goes back in after pandoc.

    pandoc's HTML reader does not reliably parse math spans, so each formula is
    parked as a token that survives conversion untouched and is restored as
    ``$tex$`` or ``$$tex$$`` in the Markdown. Source markers use the same
    store with ``display=None``.
    """
    store.append((tex.strip(), display))
    return NavigableString(f"GEMKEEPTOKEN{len(store) - 1:04d}X")


def _clean(node, soup, counts: dict, store: list) -> None:
    """Strip interface chrome, restore math and keep source names in one node."""
    for c in node.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    # Math first: the KaTeX render duplicates every glyph (visual + MathML),
    # so replace each rendered node with its TeX source before anything else.
    for el in node.select("[data-math]"):
        display = "math-block" in el.get("class", []) or el.name == "div"
        el.replace_with(_math_node(soup, el["data-math"], display, store))
        counts["math_display" if display else "math_inline"] = (
            counts.get("math_display" if display else "math_inline", 0) + 1)
    for el in node.select(".katex-display, .katex"):
        ann = el.select_one('annotation[encoding="application/x-tex"]')
        if ann is None:
            continue
        display = "katex-display" in el.get("class", [])
        el.replace_with(_math_node(soup, ann.get_text(), display, store))
        counts["math_katex_fallback"] = counts.get("math_katex_fallback", 0) + 1
    # Footnote markers: keep the source index so a later export can be keyed.
    for sup in node.select("sup[data-turn-source-index]"):
        idx = sup["data-turn-source-index"]
        sup.replace_with(NavigableString(f"[{idx}]"))
        counts["source_markers"] = counts.get("source_markers", 0) + 1
    # Code blocks: keep the code and the visible language label, not the
    # Angular class names pandoc would otherwise turn into the fence label.
    for cb in node.select("code-block"):
        code = cb.select_one("pre code") or cb.select_one("pre")
        if code is None:
            continue
        label_el = cb.select_one(".code-block-decoration span")
        label = label_el.get_text(strip=True).lower() if label_el else ""
        pre = soup.new_tag("pre")
        new_code = soup.new_tag("code")
        if label:
            new_code["class"] = [f"language-{label}"]
        new_code.string = code.get_text()
        pre.append(new_code)
        cb.replace_with(pre)
        counts["code_blocks"] = counts.get("code_blocks", 0) + 1
    # Deep Research plans are one text node shown with white-space: pre-line;
    # turn its newlines into explicit breaks so the plan keeps its lines.
    for step in node.select(".research-step-description"):
        for text in list(step.find_all(string=True)):
            if "\n" not in text:
                continue
            pieces = text.split("\n")
            anchor = text
            for k, piece in enumerate(pieces):
                if k:
                    br = soup.new_tag("br")
                    anchor.insert_after(br)
                    anchor = br
                ns = NavigableString(piece)
                anchor.insert_after(ns)
                anchor = ns
            text.extract()
    # Source chips name the Project documents a passage drew on ("citation
    # from Google Docs: <title>"). Keep that name as text; drop the widget.
    for chip in node.select("sources-carousel-inline, source-inline-chip"):
        if chip.find_parent(["sources-carousel-inline", "source-inline-chip"]):
            continue
        label = next((el["aria-label"] for el in chip.select("[aria-label]")
                      if "citation" in el["aria-label"]), "")
        m = re.search(r"citations? from (.*?)\. Press Enter", label)
        if m:
            store.append((f"[source: {m.group(1)}]", None))
            chip.replace_with(NavigableString(f" GEMKEEPTOKEN{len(store) - 1:04d}X"))
            counts["source_chips_kept"] = counts.get("source_chips_kept", 0) + 1
    for sel in CHROME_SELECTORS:
        found = node.select(sel)
        if found:
            counts[f"dropped:{sel}"] = counts.get(f"dropped:{sel}", 0) + len(found)
        for el in found:
            el.decompose()
    for a in node.select("a[href]"):
        href = a["href"]
        m = re.match(r"https?://www\.google\.com/url\?.*?[?&]q=([^&]+)", href)
        if m:
            a["href"] = unquote(m.group(1))


def to_markdown(fragment_html: str, store: list) -> str:
    out = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none",
         "--shift-heading-level-by=2"],
        input=fragment_html, capture_output=True, text=True, check=True)
    md = out.stdout
    # pandoc escapes the brackets of the footnote markers; restore them.
    md = re.sub(r"\\\[(\d+)\\\]", r"[\1]", md)

    def put_back(m):
        tex, display = store[int(m.group(1))]
        if display is None:          # a source marker, restored as plain text
            return tex
        return f"$${tex}$$" if display else f"${tex}$"
    md = re.sub(r"GEMKEEPTOKEN(\d{4})X", put_back, md)
    return md.strip() + "\n"


def _unpad(line: str) -> str:
    """Remove the single space Gemini's template puts at each end of a line."""
    if line.startswith(" "):
        line = line[1:]
    if line.endswith(" "):
        line = line[:-1]
    return line


def prompt_text(q) -> str:
    """A prompt is plain text the user typed: keep its lines and indentation."""
    lines = q.select(".query-text-line")
    if lines:
        return "\n".join(_unpad(ln.get_text()) for ln in lines).strip("\n") + "\n"
    return q.get_text("\n", strip=True) + "\n"


def extract(html: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    title_el = soup.select_one("share-viewer h1") or soup.select_one("h1")
    title = title_el.get_text(" ", strip=True) if title_el else ""
    banner = ""
    viewer = soup.select_one("share-viewer")
    if viewer is not None:
        text = viewer.get_text(" ", strip=True)
        m = re.search(r"(Responses below were generated with a creator's Project"
                      r"[^.]*\.|Created with Gemini[^\n]*?(?= [A-Z][a-z]+ \d))", text)
        banner = m.group(1).strip() if m else ""
        d = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4} at \d{1,2}:\d{2} [AP]M) "
                      r"Published ([A-Z][a-z]+ \d{1,2}, \d{4} at \d{1,2}:\d{2} [AP]M)", text)
        created, published = (d.group(1), d.group(2)) if d else ("", "")
    else:
        created = published = ""
    turns = soup.select("share-turn-viewer")
    if not turns:
        raise SystemExit("selector drift: no share-turn-viewer in DOM")
    counts: dict = {}
    out_turns = []
    visible: list = []      # text as shown on the page, for word counts
    for t in turns:
        q = t.select_one("user-query-content")
        replies = t.select("message-content")
        parts = []
        for r in replies:
            r = copy.copy(r)
            store: list = []
            _clean(r, soup, counts, store)
            visible.append(r.get_text(" "))
            parts.append(to_markdown(str(r), store))
        prompt = prompt_text(q) if q is not None else ""
        visible.append(prompt)
        out_turns.append({"prompt": prompt, "responses": parts})
    # A formula or a [source: …] marker counts as one word.
    n_words = sum(len(v.split()) for v in visible)
    return {"title": title, "banner": banner, "created": created,
            "published": published, "turns": out_turns, "counts": counts,
            "words": n_words}


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def render(short_id: str, data: dict, raw_sha: str, captured: str,
           chrome: str, pandoc: str) -> str:
    n = len(data["turns"])
    total = data["words"]
    lines = [
        f"# {data['title']}",
        "",
        f"Ingested verbatim from a public Gemini share link "
        f"(<{SHARE.format(short_id)}>), captured {captured} with {chrome} "
        f"(headless) via [`capture_gemini_share.py`](capture_gemini_share.py) "
        f"and {pandoc}. {n} turn{'s' if n != 1 else ''}, {total:,} words. "
        f"Gemini dates: created {data['created'] or 'n/a'}, published "
        f"{data['published'] or 'n/a'}. Raw DOM sha256 `{raw_sha}` (kept "
        f"local, not committed).",
    ]
    if data["banner"]:
        lines += ["", f"Share-page banner: \"{data['banner']}\""]
    lines += [
        "",
        "**Status: PRELIMINARY.** This is process, not a citable source. "
        "Nothing here enters the talk except through `../claims/REGISTER.md` "
        "and a verified card in `../library/cards/`. Bracketed numbers such as "
        "[12] are Gemini's web-source markers; the share page does not carry "
        "the source list they point to. A `[source: …]` marker names the "
        "Project document or uploaded file Gemini cited at that point.",
        "",
        "**Overlap note.** _To be written in Phase 2._",
        "",
        "---",
        "",
    ]
    for k, t in enumerate(data["turns"], 1):
        # Prompts are plain text; a fence keeps their lines and indentation.
        lines += [f"## Turn {k} — prompt", "", "~~~~text",
                  t["prompt"].rstrip("\n"), "~~~~", ""]
        for j, r in enumerate(t["responses"], 1):
            label = "response" if len(t["responses"]) == 1 else f"response, part {j}"
            lines += [f"## Turn {k} — {label}", "", r.strip(), ""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("short_id")
    ap.add_argument("out")
    ap.add_argument("--raw-dir")
    ap.add_argument("--from-raw")
    ap.add_argument("--budget-ms", type=int, default=20000)
    ap.add_argument("--captured", default=dt.date.today().isoformat())
    ap.add_argument("--stats", help="write capture statistics JSON here")
    a = ap.parse_args()

    if a.from_raw:
        html = open(a.from_raw, encoding="utf-8").read()
    else:
        html = dump_dom(SHARE.format(a.short_id), a.budget_ms)
        if a.raw_dir:
            os.makedirs(a.raw_dir, exist_ok=True)
            path = os.path.join(a.raw_dir, f"{a.short_id}.b{a.budget_ms}.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
    raw_sha = hashlib.sha256(html.encode("utf-8")).hexdigest()
    data = extract(html)
    md = render(a.short_id, data, raw_sha, a.captured, chrome_version(),
                pandoc_version())
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(md)
    body = "\n".join(t["prompt"] + "".join(t["responses"]) for t in data["turns"])
    stats = {
        "short_id": a.short_id,
        "title": data["title"],
        "turns": len(data["turns"]),
        "responses_per_turn": [len(t["responses"]) for t in data["turns"]],
        "empty_responses": sum(1 for t in data["turns"] for r in t["responses"]
                               if not r.strip()),
        "words": data["words"],
        "raw_sha256": raw_sha,
        "body_sha256": hashlib.sha256(normalize(body).encode()).hexdigest(),
        "md_sha256": hashlib.sha256(md.encode()).hexdigest(),
        "counts": data["counts"],
    }
    if a.stats:
        with open(a.stats, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=1, ensure_ascii=False)
    print(json.dumps({k: stats[k] for k in ("short_id", "title", "turns",
                                            "words", "empty_responses")},
                     ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
