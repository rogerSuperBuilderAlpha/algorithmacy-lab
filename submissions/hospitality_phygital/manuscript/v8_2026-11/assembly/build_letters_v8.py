#!/usr/bin/env python3
"""Fill the two v8 letter templates and check every quotation in them. Copies only; writes no prose.

Placeholders in letter_reviewers_v8.md and letter_editor_v8.md:
  {{O-nnn}}    the sentence with ledger id O-nnn, copied from v8_2026-11/LEDGER.md (for the list
               O-237, its lead-in only)
  {{L:O-nnn}}  where that sentence sits in DRAFT_v8.md, in words: 'Theoretical context',
               subsection 'The host', third paragraph
  {{l:O-nnn}}  the same, short, for the traceability matrix: Host ¶3
  {{WORDS}}    the body count from wordcount.py
  {{NREFS}} {{NCASES}} {{NLEG}}  entries in the reference list, the cases and the legislation
Checks, all fatal:
  every quoted sentence appears string for string in DRAFT_v8.md;
  every reviewer quotation (an italic double-quoted run after a comment id) appears, piece by
  piece between ellipses, in reviews/journal_2026-11/REVIEWS_FULL.md, quote marks normalized;
  no placeholder is left unfilled.
Writes submission/RESPONSE_TO_REVIEWERS_v8.md and submission/RESPONSE_TO_EDITOR_v8.md.
Usage: python3 build_letters_v8.py
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V8 = HERE.parent
MS = V8.parent

ledger = (V8 / "LEDGER.md").read_text(encoding="utf-8").splitlines()
draft = (MS / "DRAFT_v8.md").read_text(encoding="utf-8")
reviews = (MS / "reviews/journal_2026-11/REVIEWS_FULL.md").read_text(encoding="utf-8")

# --- sentences by ledger id, read as assemble_v8.py reads them ---------------------------------
text = {}
i = 0
while i < len(ledger):
    m = re.match(r"^#### (O-[\w.]+) · (.*)$", ledger[i])
    if m:
        j = i + 1
        if j < len(ledger) and ledger[j].startswith("**CUT AT LEDGER"):
            i = j + 1
            continue
        while j < len(ledger) and not ledger[j].startswith("> "):
            j += 1
        text[m.group(1)] = ledger[j][2:]          # first quoted line: the sentence, or a list's lead-in
        while j < len(ledger) and ledger[j].startswith("> "):
            j += 1
        i = j
        continue
    i += 1

# --- paragraphs of the body, with section, subsection and ordinal ------------------------------
body = draft[draft.index("## INTRODUCTION"):draft.index("## Acknowledgment")]
SKIP = ("#", "|", "!", "**Table", "**Figure", "<!--")
paras = []                                        # (section, subsection, ordinal, text)
sec = sub = None
n = 0
for ln in body.splitlines():
    if ln.startswith("## "):
        sec, sub, n = ln[3:].strip(), None, 0
        continue
    if ln.startswith("### "):
        sub, n = ln[4:].strip().strip("*"), 0
        continue
    if not ln.strip() or ln.startswith(SKIP) or re.match(r"^\d+\. ", ln):
        continue
    n += 1
    paras.append((sec, sub, n, ln))

ORD = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
SHORT_SEC = {"INTRODUCTION": "Intro", "APPROACH": "Approach", "THE PARTIES TO A PHYGITAL ARRANGEMENT": "Parties",
             "DURING THE STAY": "Stay", "AT THE TOUCHPOINT": "Touchpoint", "CONCLUSION": "Conclusion"}
SHORT_SUB = {"Phygital hospitality": "Phygital", "The host": "Host", "The host's duty in law": "Law",
             "The property": "Property", "The brand": "Brand", "The platform": "Platform",
             "The vendor": "Vendor", "The state": "State"}

def where(k):
    s = text[k]
    hits = [p for p in paras if s in p[3]]
    if len(hits) != 1:
        sys.exit(f"{k}: found in {len(hits)} paragraphs of DRAFT_v8.md")
    return hits[0]

def loc_long(k):
    sec, sub, n, _ = where(k)
    name = sec.capitalize()
    if sub:
        return f"'{name}', subsection '{sub}', {ORD[n-1]} paragraph"
    return f"'{name}', {ORD[n-1]} paragraph"

def loc_short(k):
    sec, sub, n, _ = where(k)
    return f"{SHORT_SUB[sub] if sub else SHORT_SEC[sec]} ¶{n}"

# --- counts ----------------------------------------------------------------------------------
wc = subprocess.run([sys.executable, str(MS / "wordcount.py"), str(MS / "DRAFT_v8.md")],
                    capture_output=True, text=True).stdout
words = re.search(r"BODY\s+([\d,]+)", wc).group(1)
refs = draft[draft.index("## References"):]
part = lambda a, b: [l for l in refs[refs.index(a):refs.index(b) if b else None].splitlines()[1:]
                     if l.strip() and not l.startswith(("#", "<!--"))]
nrefs = len(part("## References", "### Cases"))
ncases = len(part("### Cases", "### Legislation"))
nleg = len(part("### Legislation", None))
# sentence lengths in the body's prose paragraphs (list items and tables excluded)
sents = [s for p in paras for s in re.split(r"(?<=[.?!])\s+(?=[A-Z'‘(])", p[3])]
lens = sorted((len(s.split()) for s in sents), reverse=True)
longest, over50 = lens[0], sum(1 for n in lens if n > 50)
# provenance tags in the marked copy: one per placed ledger entry
marked = (MS / "DRAFT_v8_marked.md").read_text(encoding="utf-8")
tags = {t: len(re.findall(re.escape(f"[{t}] "), marked)) for t in ("PB", "PB-a", "C")}

# --- reviewer quotations ---------------------------------------------------------------------
def norm(s):
    s = re.sub(r"[“”\"‘’']", "'", s)
    return re.sub(r"\s+", " ", s)

REV = norm(reviews)

def check_reviewer_quotes(t, name):
    bad = []
    for q in re.findall(r"\*\"(.+?)\"\*", t):
        for piece in re.split(r"\s*…\s*", q):
            for frag in re.split(r'"\s+and\s+"', piece):   # two comments quoted in one line
                frag = frag.strip(" .")
                if frag and norm(frag) not in REV:
                    bad.append(frag[:80])
    return bad

# --- fill ------------------------------------------------------------------------------------
missing, revbad = [], []
for src, dst in [("letter_reviewers_v8.md", "submission/RESPONSE_TO_REVIEWERS_v8.md"),
                 ("letter_editor_v8.md", "submission/RESPONSE_TO_EDITOR_v8.md")]:
    t = (HERE / src).read_text(encoding="utf-8")
    revbad += [(src, b) for b in check_reviewer_quotes(t, src)]
    t = (t.replace("{{WORDS}}", words).replace("{{NREFS}}", str(nrefs))
          .replace("{{NCASES}}", str(ncases)).replace("{{NLEG}}", str(nleg))
          .replace("{{LONGEST}}", str(longest)).replace("{{OVER50}}", str(over50))
          .replace("{{NPB}}", str(tags["PB"])).replace("{{NPBA}}", str(tags["PB-a"]))
          .replace("{{NC}}", str(tags["C"])))
    t = re.sub(r"\{\{L:(O-[\w.]+)\}\}", lambda m: loc_long(m.group(1)), t)
    t = re.sub(r"\{\{l:(O-[\w.]+)\}\}", lambda m: loc_short(m.group(1)), t)

    def q(m):
        k = m.group(1)
        if k not in text:
            sys.exit(f"{src}: no ledger sentence {k}")
        s = text[k]
        if s not in draft:
            missing.append((src, k))
        return s
    t = re.sub(r"\{\{(O-[\w.]+)\}\}", q, t)
    left = re.findall(r"\{\{[^}]*\}\}", t)
    if left:
        sys.exit(f"{src}: unfilled {left}")
    (MS / dst).write_text(t, encoding="utf-8")

print(f"body {words} | refs {nrefs}, cases {ncases}, legislation {nleg}")
print("ledger quotes not found in DRAFT_v8.md:", missing or "none")
print("reviewer quotes not found in REVIEWS_FULL.md:", revbad or "none")
if missing or revbad:
    sys.exit(1)
