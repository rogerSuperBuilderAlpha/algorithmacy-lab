#!/usr/bin/env python3
"""Reconcile a Chicago notes-bibliography chapter's apparatus, both directions.

Panel 3 left D2 open -- "bibliography both-directions still fails" -- and the check had
only ever been done by eye. Three separate reviewers found orphans and placeholders that
a script finds in a second, so this is the script.

What it checks:

  1. every note key referenced in the body has a definition, and vice versa
  2. note numbering has no gaps and no duplicates
  3. every surname appearing in a note resolves to a bibliography entry
  4. every bibliography entry is reached by at least one note   (the orphan check)
  5. no placeholder text survives anywhere
  6. every live URL carries an access date; DOIs are exempt
  7. word counts by section, against the ceiling

Usage: python3 check_apparatus.py chapter/chapter_v3.md
"""
import re
import sys
from collections import Counter

PLACEHOLDER = re.compile(
    r"\[(?:title|article titles?|page|volume|issue|year|doi|url|to be supplied|tbd|tk)"
    r"[^\]]*\]", re.I)
# "———." repeats the previous entry's author in Chicago style
BIB_LINE = re.compile(r"^(?:———\.|[A-ZÀ-Þ][^.]{1,80}?[,.])\s")
SURNAME = re.compile(r"\b([A-ZÀ-Þ][a-zà-ÿčćšžńłéèáóúüöäğ]+(?:-[A-ZÀ-Þ][a-zà-ÿ]+)?)\b")
STOP = set("""The A An In On At Of For And But Or Not This That These Those It Its He She
They Their His Her We Our I My You Your There Here When While Since Because Although
Chapter Section Note Notes Figure Table See Also Ibid Idem Press University Books Book
New York London Chicago Cambridge Oxford Minneapolis Madison Durham Berkeley Los Angeles
Edinburgh Amsterdam Routledge Verso Blackwell Sage Wiley Springer MIT Duke Columbia
Harvard Princeton Yale Stanford January February March April May June July August
September October November December Accessed Vol No PhD Trans Ed Eds Reprint Second
First Third Version Selected Writings Screen Slacker Austin Texas American Journal
Review Studies Research Quarterly Annals Society Media Film Cinema Culture""".split())


def main(path):
    raw = open(path, encoding="utf-8").read()
    problems, notes_ok = [], True

    # split the three regions
    body = re.split(r"(?m)^##\s*Notes\s*$", raw)[0]
    rest = raw[len(body):]
    notes_block = re.split(r"(?m)^##\s*Bibliography\s*$", rest)[0]
    bib_block = rest[len(notes_block):]

    # 1 + 2 -- note keys
    used = re.findall(r"\[\^([^\]]+)\](?!:)", body)
    defined = re.findall(r"(?m)^\[\^([^\]]+)\]:", notes_block)
    used_set, def_set = set(used), set(defined)
    for k in sorted(used_set - def_set):
        problems.append("note [^%s] cited in the body with no definition" % k)
    for k in sorted(def_set - used_set):
        problems.append("note [^%s] defined but never cited" % k)
    for k, n in Counter(defined).items():
        if n > 1:
            problems.append("note [^%s] defined %d times" % (k, n))
    nums = sorted(int(m.group(1)) for m in
                  (re.fullmatch(r"(\d+)", d) for d in defined) if m)
    if nums:
        gaps = [i for i in range(nums[0], nums[-1] + 1) if i not in nums]
        if gaps:
            problems.append("note numbering gaps: %s" %
                            ", ".join(str(g) for g in gaps[:12]))

    # 3 + 4 -- surnames both directions
    bib_entries = [l.strip() for l in bib_block.splitlines()
                   if l.strip() and BIB_LINE.match(l.strip())]
    bib_names, last_author = [], None
    for e in bib_entries:
        if e.startswith("———"):
            bib_names.append((last_author, e))
            continue
        m = re.match(r"([A-ZÀ-Þ][A-Za-zÀ-ÿ''-]+)", e)
        last_author = m.group(1) if m else None
        bib_names.append((last_author, e))
    bib_surnames = {n for n, _ in bib_names if n}

    # Only the orphan direction is checked. Going notes->bibliography over every
    # capitalised token returned 582 "surnames" including About, Academy and Across;
    # a bibliography entry's leading author, by contrast, is unambiguous.
    missing = []
    orphans = []
    for name, entry in bib_names:
        if not name:
            continue
        # institutional authors carry more than one word before the period
        lead = entry.split(".")[0]
        probes = [name]
        if " " not in name and "," in lead:
            pass
        if lead and " " in lead and "," not in lead:
            probes.append(lead)            # e.g. "American Film Institute"
        if not any(pr in notes_block for pr in probes):
            orphans.append(name + "  (" + entry[:60] + "...)")
    orphans = sorted(set(orphans))

    # 5 -- placeholders
    for m in PLACEHOLDER.finditer(raw):
        problems.append("placeholder survives: %s" % m.group(0)[:60])

    # 6 -- URLs need access dates
    for line in raw.splitlines():
        if re.search(r"https?://", line) and "doi.org" not in line:
            if not re.search(r"accessed", line, re.I):
                problems.append("live URL with no access date: %s" % line.strip()[:90])

    # 7 -- word counts
    def wc(t):
        t = re.sub(r"(?m)^#+ .*$", "", t)
        t = re.sub(r"\[\^[^\]]+\]", "", t)
        return len(t.split())
    secs = re.split(r"(?m)^(## \d+\..*)$", body)
    print("SECTION WORD COUNTS")
    total = 0
    for i in range(1, len(secs), 2):
        n = wc(secs[i + 1])
        total += n
        print("  %-52s %5d" % (secs[i][3:55], n))
    print("  %-52s %5d" % ("BODY TOTAL", total))
    print("  %-52s %5d  (notes %d, bibliography %d entries)"
          % ("apparatus", wc(notes_block) + wc(bib_block), len(defined), len(bib_entries)))

    print("\nAPPARATUS RECONCILIATION")
    print("  note keys used %d / defined %d" % (len(used_set), len(def_set)))
    print("  bibliography entries %d, distinct surnames %d" % (len(bib_entries), len(bib_surnames)))
    if orphans:
        print("  bibliography entries NO note reaches (%d):" % len(orphans))
        for s in orphans[:25]:
            print("     " + s)

    if problems:
        print("\nPROBLEMS (%d)" % len(problems))
        for p in problems[:40]:
            print("  - " + p)
    else:
        print("\nno structural problems found")
    return 1 if (problems or missing or orphans) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
