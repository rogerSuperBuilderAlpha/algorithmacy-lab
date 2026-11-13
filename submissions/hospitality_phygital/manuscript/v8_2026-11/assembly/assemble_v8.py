#!/usr/bin/env python3
"""Assemble DRAFT_v8.md from v8_2026-11/LEDGER.md. Copies only; writes no prose.

Reads the ledger's sentences in order, skips entries marked CUT AT LEDGER, joins each
paragraph's sentences, and adds the headings, Figure 1 and Tables 1 and 2 at fixed points.
Writes two files beside DRAFT_v7.md:
  DRAFT_v8.md          the manuscript
  DRAFT_v8_marked.md   the same text with each sentence's provenance in brackets:
                       [PB] Pierre's sentence verbatim; [PB-a] Pierre's, adapted (reason in
                       the ledger); [C] Claude's.
Front and back matter come from assembly/head_v8.md and assembly/tail_v8.md, written by hand.
Usage: python3 assemble_v8.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
V8 = HERE.parent
MS = V8.parent

ledger = (V8 / "LEDGER.md").read_text(encoding="utf-8")
head = (HERE / "head_v8.md").read_text(encoding="utf-8")
tail = (HERE / "tail_v8.md").read_text(encoding="utf-8")
inserts = {k: (HERE / f"{k}.md").read_text(encoding="utf-8").strip("\n")
           for k in ("figure1", "table1", "table2")}

SECTIONS = {
    "INTRODUCTION": "INTRODUCTION",
    "THEORETICAL CONTEXT": "THEORETICAL CONTEXT",
    "APPROACH": "APPROACH",
    "THE PARTIES TO A PHYGITAL ARRANGEMENT": "THE PARTIES TO A PHYGITAL ARRANGEMENT",
    "DURING THE STAY": "DURING THE STAY",
    "AT THE TOUCHPOINT": "AT THE TOUCHPOINT",
    "CONCLUSION": "CONCLUSION",
}
SUBSECTIONS = ["Phygital hospitality", "The host", "The host's duty in law", "The property",
               "The brand", "The platform", "The vendor", "The state"]
# Inserted after the paragraph whose ledger header carries this key.
AFTER = {"AT ¶1": "figure1", "DS ¶5": "table1", "AT ¶7": "table2"}

def tag_of(header):
    m = re.search(r"\[(PB-a|PB|C)\]", header)
    if m:
        return m.group(1)
    raise SystemExit(f"no provenance tag in: {header}")

out, marked = [], []
section = None
para, para_m = [], []
para_key = None

def flush():
    global para, para_m
    if para:
        out.append(" ".join(para)); out.append("")
        marked.append(" ".join(para_m)); marked.append("")
        if para_key and para_key in AFTER:
            ins = inserts[AFTER[para_key]]
            out.append(ins); out.append("")
            marked.append(ins); marked.append("")
    para, para_m = [], []

lines = ledger.splitlines()
i = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r"^## (.+)$", ln)
    if m and m.group(1).strip() in SECTIONS:
        flush()
        section = m.group(1).strip()
        h = f"## {SECTIONS[section]}"
        out += [h, ""]; marked += [h, ""]
        i += 1; continue
    m = re.match(r"^### (.+)$", ln)
    if m and section:
        flush()
        text = m.group(1)
        sub = re.match(r"^\*(.+?)\*", text)
        if sub and sub.group(1) in SUBSECTIONS:
            h = f"### *{sub.group(1)}*"
            out += [h, ""]; marked += [h, ""]
        k = re.search(r"\b([A-Z]{2}) ¶(\d+a?)", text)
        para_key = f"{k.group(1)} ¶{k.group(2)}" if k else None
        i += 1; continue
    m = re.match(r"^#### (O-[\w.]+) · (.*)$", ln)
    if m and section:
        oid, hdr = m.group(1), m.group(2)
        j = i + 1
        cut = j < len(lines) and lines[j].startswith("**CUT AT LEDGER")
        if cut:
            i = j + 1; continue
        while j < len(lines) and not lines[j].startswith("> "):
            j += 1
        quote = []
        while j < len(lines) and lines[j].startswith("> "):
            quote.append(lines[j][2:]); j += 1
        tag = tag_of(hdr)
        if len(quote) > 1:                      # a list (O-237): lead-in, then items
            flush_para = " ".join(para + [quote[0]])
            out.append(flush_para); out.append("")
            marked.append(" ".join(para_m + [f"[{tag}] {quote[0]}"])); marked.append("")
            para, para_m = [], []
            for q in quote[1:]:
                out.append(q); marked.append(q)
            out.append(""); marked.append("")
        else:
            para.append(quote[0]); para_m.append(f"[{tag}] {quote[0]}")
        i = j; continue
    i += 1
flush()

body = "\n".join(out).strip("\n")
body_m = "\n".join(marked).strip("\n")
banner = ("<!--\nASSEMBLED BY assemble_v8.py from v8_2026-11/LEDGER.md. DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026, "
          "except Pierre's sentences, which DRAFT_v8_marked.md tags [PB] (verbatim) and [PB-a] (adapted). "
          "Delete this comment before submission.\n-->\n\n")
(MS / "DRAFT_v8.md").write_text(banner + head.strip("\n") + "\n\n" + body + "\n\n" + tail.strip("\n") + "\n", encoding="utf-8")
(MS / "DRAFT_v8_marked.md").write_text(banner + head.strip("\n") + "\n\n" + body_m + "\n\n" + tail.strip("\n") + "\n", encoding="utf-8")
print("wrote DRAFT_v8.md and DRAFT_v8_marked.md")
