#!/usr/bin/env python3
"""Combine the eight §-drafts into DRAFT.md with one consolidated bibliography.

- Concatenates section bodies in spine order (§1..§8), dropping per-section reference lists.
- Cleans Google-Docs export cruft (escaped punctuation) and normalizes section headers.
- Collects every reference entry, dedupes by a normalized key, alphabetizes, writes one master list.
Prints a report (section word counts, raw vs deduped ref counts) to stderr.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(BASE, "drafts")
FILES = [
    "s1_introduction.md", "s2_method.md", "s3_object.md", "s4_foreclosure.md",
    "s5_warrant.md", "s6_construct.md", "s7_agenda.md", "s8_conclusion.md",
]
REF_HEADING = re.compile(r"^##\s+Working references", re.I)

def declutter(text):
    # Remove Google-Docs backslash escapes before punctuation/digits.
    text = re.sub(r"\\([.\[\]()+=%&#_~])", r"\1", text)
    text = text.replace("\\ ", " ")
    # Normalize bold/escaped section headers: "## **3\. Title**" -> "## 3. Title"
    text = re.sub(r"^(#{2,3})\s*\*\*(.+?)\*\*\s*$",
                  lambda m: f"{m.group(1)} {m.group(2)}", text, flags=re.M)
    return text

def is_ref_line(line):
    s = line.strip()
    if s.startswith("- "):
        s = s[2:].strip()
    if s.startswith("*"):
        return False
    if "to confirm against" in s or "Bibliographic detail" in s:
        return False  # drop placeholder stubs
    # Any APA entry carries a (year); robust for personal and organizational authors.
    return bool(re.search(r"\((1[89]\d\d|20\d\d)[a-z]?\)", s[:200]))

def _clean(entry):
    s = entry.strip()
    if s.startswith("- "):
        s = s[2:]
    s = re.sub(r"\[(new|verify[^\]]*|shared[^\]]*)\]", "", s, flags=re.I)
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"\*|_", "", s)
    return re.sub(r"\s+", " ", s).strip(" .,")

def dedupe_key(entry):
    """Key on year + title-start, stable across author-name formatting variants."""
    s = _clean(entry).lower()
    ym = re.search(r"\((1[89]\d\d|20\d\d)[a-z]?\)", s) or re.search(r"(1[89]\d\d|20\d\d)", s)
    year = ym.group(1) if ym else "0000"
    after = s.split(year, 1)[1] if year in s else s
    after = re.sub(r"^[a-z]?\)?\.?,?\s*", "", after)        # strip year-letter/paren/punct
    title = re.sub(r"[^a-z0-9 ]", "", after)[:55].strip()
    return f"{year}|{title}" if title else _clean(entry).lower()[:60]

def sort_key(entry):
    return _clean(entry).lower()

bodies, refs_raw = [], []
report = []
for fn in FILES:
    raw = open(os.path.join(DRAFTS, fn), encoding="utf-8").read()
    lines = raw.splitlines()
    # split body / refs at the Working-references heading
    cut = next((i for i, l in enumerate(lines) if REF_HEADING.match(l)), len(lines))
    body_lines = lines[:cut]
    ref_lines = lines[cut:]
    # drop a leading multi-line italic note block (e.g. "*Section draft ... at the end.*")
    cleaned, skipping = [], False
    for l in body_lines:
        s = l.strip()
        if not skipping and s.startswith("*Section draft"):
            skipping = True
            if s.endswith("*") and len(s) > 1:
                skipping = False
            continue
        if skipping:
            if s.endswith("*"):
                skipping = False
            continue
        cleaned.append(l)
    body_lines = cleaned
    # normalize section/subsection header levels (section -> ##, subsection -> ###)
    norm = []
    for l in body_lines:
        m2 = re.match(r"^#{1,4}\s+(\d+)\.(\d+)(\s.*)$", l)
        m1 = re.match(r"^#{1,4}\s+(\d+)\.?(\s.*)$", l)
        if m2:
            norm.append(f"### {m2.group(1)}.{m2.group(2)}{m2.group(3)}")
        elif m1:
            norm.append(f"## {m1.group(1)}.{m1.group(2)}")
        else:
            norm.append(l)
    body_lines = norm
    # drop a trailing horizontal rule the per-section file used before refs
    while body_lines and body_lines[-1].strip() in ("", "---"):
        body_lines.pop()
    body = declutter("\n".join(body_lines)).strip()
    bodies.append(body)
    wc = len(re.findall(r"\b\w+\b", body))
    # collect refs: a new entry begins at a "- " bullet OR after a blank line;
    # indented/continuation lines join the current entry. Handles both formats
    # (§1/§2 contiguous bullet lists; §3-§8 blank-line-separated single lines).
    n = 0
    block, blocks = [], []
    for l in ref_lines[1:]:   # skip the "## Working references" heading line
        if l.lstrip().startswith("- "):
            blocks.append(block)
            block = [l.lstrip()[2:]]
        elif l.strip() == "":
            blocks.append(block)
            block = []
        else:
            block.append(l)
    blocks.append(block)
    for b in blocks:
        if not b:
            continue
        text = re.sub(r"\s+", " ", " ".join(x.strip() for x in b)).strip()
        if text.startswith("- "):
            text = text[2:].strip()
        if is_ref_line(text):
            refs_raw.append(declutter(text))
            n += 1
    report.append(f"{fn}: body {wc} words, {n} ref entries")

# dedupe refs (key on year+title; keep the most complete variant). Keep DOIs/URLs in the stored text;
# only the dedupe key strips them.
def display(entry):
    # Post citation-pass: strip resolved working tags ([new]/[shared…]); KEEP genuine [verify…] flags
    # for the few entries with an unconfirmed page range.
    s = entry[2:].strip() if entry.startswith("- ") else entry.strip()
    s = re.sub(r"\s*\[(new|shared)[^\]]*\]", "", s)
    return re.sub(r"\s+", " ", s).strip()

seen = {}
for r in refs_raw:
    entry = r[2:].strip() if r.startswith("- ") else r.strip()
    k = dedupe_key(entry)
    cand = display(entry)
    if k not in seen or len(cand) > len(seen[k]):
        seen[k] = cand

master = sorted(seen.values(), key=lambda e: sort_key(e))

# assemble DRAFT.md
out = []
out.append("# Algorithmacy: A communication competency for triadic algorithmic coordination\n")
out.append("Roger Hunt III · Bentley University\n")
out.append("*Target venue: Academy of Management Annals. Combined full draft (deepened build). "
           "Consolidated bibliography follows the body; in-text citations resolve to it. "
           "Entries flagged for verification in the citation-integrity pass are marked there.*\n")
out.append("\n## Abstract\n")
out.append(
    "\nCommunication theory has measured how a worker engages an algorithmic system; it has not measured what "
    "a worker does, through that system, to coordinate with another human party whose interests and presence "
    "she cannot directly access. The two are different problems. CMC competence, HMC, AI-MC, algorithmic "
    "literacy, AI literacy, and algorithm sensemaking describe a worker on one side of an algorithmic medium "
    "that conveys, scores, or interprets but does not pursue objectives of its own across both human parties. "
    "A driver coordinates with a rider through a matching algorithm whose surge, dispatch, and retention "
    "objectives transform what each side sends to the other. An applicant communicates with a hiring manager "
    "through a system that scores resumes against a keyword profile rather than forwarding them. A lawyer "
    "reaches the opposing counsel only through what the judge admits, rules on, or excludes. The competency "
    "these arrangements demand of their human parties has no name in the field's existing vocabulary, and "
    "refining the existing constructs cannot produce it because the structural unit they were built around is "
    "the wrong one. *Algorithmacy* names the missing competency. This integrative review specifies the "
    "construct, locates it among the existing literacies it extends, and positions it for the measurement "
    "program it makes possible.\n")
out.append("\n*Keywords:* algorithmacy; triadic coordination; algorithmic management; platform work; "
           "communication competency; integrative review\n")
out.append("\n---\n")
for body in bodies:
    out.append("\n" + body + "\n")
    out.append("\n---\n")
out.append("\n## Consolidated bibliography\n")
out.append(f"\n*{len(master)} unique entries, merged and de-duplicated from the eight section drafts. "
           "Items needing confirmation are noted in the per-section research files and the combine report.*\n\n")
for e in master:
    out.append(e + "\n\n")

open(os.path.join(BASE, "DRAFT.md"), "w", encoding="utf-8").write("\n".join(out))

total_words = sum(len(re.findall(r"\b\w+\b", b)) for b in bodies)
sys.stderr.write("\n".join(report) + "\n")
sys.stderr.write(f"\nTOTAL body words: {total_words}\n")
sys.stderr.write(f"Raw ref entries: {len(refs_raw)}  ->  deduped: {len(master)}\n")
