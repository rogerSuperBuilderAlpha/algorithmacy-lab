#!/usr/bin/env python3
"""Compile every open question in records/*.md into QUESTIONS.tsv and QUESTIONS.md.

Measurement only: it copies fields the records already hold and writes no prose of its own.

    python3 -I tools/compile_questions.py

QUESTIONS.tsv has one row per OQ: oq_id, key, apa_short, volume, issue, published_online, band,
article_type_norm, exchange_id, form, level, addressee, scope, quote, locator, paraphrase, verified,
hand_check, fit_A, fit_B (the fit columns stay blank until S6). QUESTIONS.md groups the same rows by
article, in volume/issue order, for reading.
"""
import csv
import glob
import os
import re

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REC = os.path.join(RUN, "records")
COLS = ["oq_id", "key", "apa_short", "volume", "issue", "published_online", "band", "article_type_norm",
        "exchange_id", "form", "level", "addressee", "scope", "quote", "locator", "paraphrase",
        "verified", "hand_check", "fit_A", "fit_B"]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                out[k.strip()] = v.split("#")[0].strip().strip('"')
    return out


def field(block, name):
    m = re.search(rf"^- {name}:\s*(.*)$", block, re.M)
    return m.group(1).strip() if m else ""


def main():
    rows, removed = [], []
    for path in sorted(glob.glob(os.path.join(REC, "*.md"))):
        text = open(path, encoding="utf-8").read()
        fm = frontmatter(text)
        key = fm.get("key") or os.path.basename(path)[:-3]
        title = re.search(r"^# (.+)$", text, re.M)
        sec = re.search(r"^## Open questions\s*\n(.*?)(?=^## )", text, re.S | re.M)
        body = sec.group(1) if sec else ""
        for m in re.finditer(r"^### (OQ-[\w-]+)\s*\n(.*?)(?=^### |\Z)", body, re.S | re.M):
            oq, block = m.group(1), m.group(2)
            if re.search(r"^- Removed by", block, re.M):
                removed.append(oq)
                continue
            q = field(block, "Quote")
            qm = re.match(r'["“](.+?)["”]\s*(\(.*\))?\s*$', q)
            rows.append({
                "oq_id": oq, "key": key, "apa_short": title.group(1)[:90] if title else "",
                "volume": fm.get("volume", ""), "issue": fm.get("issue", ""),
                "published_online": fm.get("published_online", ""), "band": fm.get("band", ""),
                "article_type_norm": fm.get("article_type_norm", ""), "exchange_id": fm.get("exchange_id", ""),
                "form": field(block, "Form"), "level": field(block, "Level of analysis"),
                "addressee": field(block, "Addressee"), "scope": field(block, "Scope"),
                "quote": qm.group(1) if qm else q, "locator": (qm.group(2) or "") if qm else "",
                "paraphrase": field(block, "Paraphrase"), "verified": fm.get("verified", ""),
                "hand_check": fm.get("hand_check", ""), "fit_A": "", "fit_B": ""})
    rows.sort(key=lambda r: (int(r["volume"] or 0), int(r["issue"] or 0), r["key"], r["oq_id"]))
    with open(os.path.join(RUN, "QUESTIONS.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    lines = ["# Open questions in *Organization Theory*, vol. 4(1) 2023 – 7(3) 2026", "",
             "> Compiled by `tools/compile_questions.py` from the records; every quotation is the "
             "article's own words, located, and verified at S5. Form `own_research_question` marks a "
             "question the paper answers itself.", ""]
    keys = []
    for r in rows:
        if r["key"] not in keys:
            keys.append(r["key"])
    n_open = sum(1 for r in rows if "own_research_question" not in r["form"])
    lines += [f"{len(rows)} entries from {len(keys)} articles; {n_open} excluding the papers' own research questions.", ""]
    for k in keys:
        rs = [r for r in rows if r["key"] == k]
        lines += [f"## {rs[0]['apa_short']}", f"`{k}` · {rs[0]['volume']}({rs[0]['issue']}) · "
                  f"{rs[0]['article_type_norm']}" + (f" · exchange `{rs[0]['exchange_id']}`"
                  if rs[0]["exchange_id"] not in ("", "none") else ""), ""]
        for r in rs:
            lines.append(f"- **{r['oq_id']}** ({r['form']}; {r['level']}): “{r['quote']}” {r['locator']}")
        lines.append("")
    open(os.path.join(RUN, "QUESTIONS.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"{len(rows)} OQs from {len(keys)} records; {len(removed)} removed entries skipped")


if __name__ == "__main__":
    main()
