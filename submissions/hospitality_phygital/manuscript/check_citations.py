#!/usr/bin/env python3
"""Every surname+year in the body must match a year in the reference list.

Added 8 August 2026, after four references turned out to pair an online-first year
with a version-of-record issue: the bibliography said Nguyen et al. (2024) beside
*Tourism Review* 80:7, and volume 80 is 2025. Correcting the reference list without
correcting the body would have left the two disagreeing, which is the failure this
gate exists to make impossible.

Usage: python3 check_citations.py        (prints 'citations OK' and exits 0)
"""
import re
import subprocess
import sys
from pathlib import Path

ARM = Path(__file__).resolve().parent.parent

# DRAFT.md is the paper. It was once hardcoded to a second draft and silently ignored its
# argument, so a whole session's worth of "citations OK" was reported about the wrong file.
# That second draft was deleted on 17 August; there is one paper in this arm now.
_paper = Path(sys.argv[1]) if len(sys.argv) > 1 else ARM / "manuscript" / "DRAFT.md"
if not _paper.is_absolute():
    _paper = Path.cwd() / _paper
print(f"checking {_paper.name}")
text = _paper.read_text(encoding="utf-8")
body = text.split("## References")[0]
body = re.sub(r"\s+", " ", body)

# The key list must match the paper. Rendering the wrong one made every entry unique to
# the other draft look like a year disagreement.
_keys = ARM / "manuscript" / "cited_keys_draft.txt"
refs = subprocess.run(
    ["python3", str(ARM / "manuscript" / "render_refs.py"), "--cited", str(_keys)],
    capture_output=True, text=True).stdout

# surname -> set of years present in the reference list
listed = {}
for line in refs.splitlines():
    # A reference may open with a lowercase nobiliary particle -- "van Doorn, Jenny",
    # "de Certeau, Michel". Requiring ^[A-Z] skipped those lines entirely, so the
    # checker never saw van Doorn 2017 and matched the in-text citation against a
    # co-author's surname in a different entry (Doorn, Neelke, in Alfrink et al. 2023),
    # reporting a disagreement that did not exist.
    m = re.match(r"^((?:van|von|de|del|della|du|da|dos|le|la|ter|ten|af|zu)\s+)?"
                 r"([A-Z][^(]*?)\s*\((\d{4}[a-z]?|n\.d\.)\)", line.strip())
    if not m:
        continue
    year = m.group(3)
    names = m.group(2)
    for sur in re.findall(r"([A-Z][A-Za-z'\-]+),", names):
        listed.setdefault(sur, set()).add(year)
    for sur in re.findall(r"\b([A-Z][A-Za-z'\-]+)\b", names):
        listed.setdefault(sur, set()).add(year)

# narrative: "Surname (2020)" / "Surname et al. (2020)" / "Surname and Other (2020)"
pat = re.compile(r"\b([A-Z][A-Za-z'\-]+)"
                 r"(?:\s+et\s+al\.|\s+and\s+[A-Z][A-Za-z'\-]+)?"
                 r"(?:'s)?\s*\((\d{4}[a-z]?)\)")
# parenthetical: "(Surname 2020; Other 2019)"
pat2 = re.compile(r"\(([^()]*?\b\d{4}[a-z]?[^()]*?)\)")

problems, checked = [], 0
for m in pat.finditer(body):
    sur, yr = m.group(1), m.group(2)
    if sur not in listed:
        continue
    checked += 1
    if yr not in listed[sur]:
        problems.append((sur, yr, sorted(listed[sur]),
                         body[max(0, m.start() - 70):m.end() + 25]))

for m in pat2.finditer(body):
    for sur, yr in re.findall(r"([A-Z][A-Za-z'\-]+)(?:\s+et\s+al\.)?"
                              r"(?:\s+and\s+[A-Z][A-Za-z'\-]+)?\s+(\d{4}[a-z]?)", m.group(1)):
        if sur not in listed:
            continue
        checked += 1
        if yr not in listed[sur]:
            problems.append((sur, yr, sorted(listed[sur]),
                             body[max(0, m.start() - 60):m.end() + 15]))

seen, uniq = set(), []
for p in problems:
    k = (p[0], p[1])
    if k not in seen:
        seen.add(k); uniq.append(p)

print(f"{checked} in-text citations checked against {len(listed)} surnames in the reference list")
if uniq:
    print(f"\n{len(uniq)} disagree with the reference list:\n")
    for sur, yr, have, ctx in uniq:
        print(f"  {sur} ({yr})  — reference list has {have}")
        print(f"      …{ctx.strip()}…\n")
else:
    print("citations OK")
sys.exit(1 if uniq else 0)
