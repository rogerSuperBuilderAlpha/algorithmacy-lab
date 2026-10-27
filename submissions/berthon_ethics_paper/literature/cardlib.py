"""Shared helpers for this arm's literature scripts: parse the two card formats into one record.

Format Y (berthon_ethics_course): YAML-style frontmatter between --- lines (citekey, title, authors,
year, doi, source_basis, verified, ...).
Format H (algorithmacy_design_ethics, dxd_foundation, algorithmacy_scaffolding): an H1 citation line,
then a bold "**Identifier:** ... · **Read depth:** ..." line, and in many cards an S2 "**Verdict:**".

Nothing here rewrites a card. Stdlib only; run the scripts with python3 -I.
"""
import glob
import hashlib
import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ARM = os.path.dirname(HERE)
SUBMISSIONS = os.path.dirname(ARM)
CARDS = os.path.join(HERE, "cards")

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s)\]>,;·*\"']+", re.I)

# Files in a card directory that are notes or indexes, not reference cards.
NONCARDS = {
    "INDEX.md", "README.md", "REFERENCES.md",
    "counter_agent_search_notes.md", "fairness_matrix_2026-09-19.md",
    "gemini_report_citation_audit.md", "journal_scan_memo.md", "triadic_hf_search_notes.md",
}

BASIS_MAP = {
    "full-text": "full", "full_text": "full", "partial_full_text": "partial", "read": "full",
    "partial-text": "partial", "partial": "partial",
    "abstract": "abstract", "abstract_only": "abstract", "abstract-only": "abstract",
    "secondary": "secondary", "secondary_summary": "secondary",
    "adapted_from_verified_card": "adapted",
}


def sources():
    with open(os.path.join(HERE, "card_sources.json"), encoding="utf-8") as f:
        return json.load(f)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def norm_doi(s):
    if not s:
        return ""
    m = DOI_RE.search(s)
    return m.group(0).rstrip(".").lower() if m else ""


def norm_title(title, year):
    t = unicodedata.normalize("NFKD", title or "").encode("ascii", "ignore").decode().lower()
    words = re.findall(r"[a-z0-9]+", t)
    return (" ".join(words[:6]) + f" {year}") if words else ""


def _frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"([A-Za-z_]+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm


def parse_card(path, subfolder):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    key = os.path.basename(path)[:-3]
    rec = {"subfolder": subfolder, "file": os.path.basename(path), "key": key,
           "authors": "", "year": "", "title": "", "doi": "", "basis": "", "verified": "", "format": ""}
    fm = _frontmatter(text)
    if fm is not None:
        rec.update(format="Y", authors=fm.get("authors", ""), year=fm.get("year", ""),
                   title=fm.get("title", ""), doi=norm_doi(fm.get("doi", "")),
                   basis=BASIS_MAP.get(fm.get("source_basis", ""), fm.get("source_basis", "")),
                   verified=fm.get("verified", ""))
        rec["key"] = fm.get("citekey", key) or key
        return rec
    rec["format"] = "H"
    first = text.splitlines()[0] if text else ""
    m = re.match(r"#\s*(.*?)\s*\((\d{4})[a-z]?[^)]*\)\.?\s*(.*)", first)
    if m:
        rec["authors"], rec["year"] = m.group(1), m.group(2)
        rec["title"] = re.sub(r"[*_]", "", m.group(3)).split(". ")[0].strip()
    else:
        rec["title"] = first.lstrip("# ").strip()
    ident = re.search(r"\*\*Identifier:\*\*(.*?)(?:·|\n)", text)
    rec["doi"] = norm_doi(ident.group(1)) if ident else ""
    if not rec["doi"]:
        rec["doi"] = norm_doi(text[:1500])
    depth = re.search(r"\*\*Read depth:\*\*\s*([^·\n]{0,60})", text)
    if depth:
        d = depth.group(1).lower()
        word = re.match(r"[a-z_\-]+", d)
        if d.startswith("not read"):
            rec["basis"] = "record"
        elif word and word.group(0) in BASIS_MAP:
            rec["basis"] = BASIS_MAP[word.group(0)]
        else:
            hit = next((v for k, v in BASIS_MAP.items() if k in d), "")
            rec["basis"] = hit or "see card"
    verdict = re.search(r"\*\*Verdict:\*\*\s*([^.\n—;(]+)", text)
    if verdict:
        rec["verified"] = "S2 " + verdict.group(1).strip()
    return rec


def all_cards():
    """Every reference card in literature/cards/<subfolder>/, sorted, as parsed records."""
    out = []
    for sub in sorted(os.listdir(CARDS)):
        d = os.path.join(CARDS, sub)
        if not os.path.isdir(d):
            continue
        for p in sorted(glob.glob(os.path.join(d, "*.md"))):
            if os.path.basename(p) in NONCARDS:
                continue
            out.append(parse_card(p, sub))
    return out


def parse_bib(path):
    """Return {key: {field: value}} for a .bib file (flat fields only)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    entries = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, re.S):
        fields = {"_type": m.group(1).lower(), "_raw": m.group(0)}
        for fm in re.finditer(r"(\w+)\s*=\s*[{\"](.*?)[}\"]\s*,?\s*$", m.group(3), re.M):
            fields[fm.group(1).lower()] = fm.group(2)
        entries[m.group(2)] = fields
    return entries


def write_or_check(path, content, check):
    """Write content to path; with check, return False (and write nothing) if the file differs."""
    if check:
        try:
            with open(path, encoding="utf-8") as f:
                return f.read() == content
        except FileNotFoundError:
            return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def md_cell(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()
