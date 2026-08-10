#!/usr/bin/env python3
"""Merge the seven per-dossier extractions into one claims table, and audit it.

Phase 0 fans out one extractor per research dossier. Each returns a table of facts
with a provenance class. This merges them, finds the same fact claimed twice with
two different classes, and reports the class distribution -- which is the number that
decides how much of the chapter can be written without a library card.

The provenance classes:

  A  the dossier retrieved the source and the quotation is verbatim on record
  B  convergence-verified across secondary sources; no page image, primary unopened
  C  second-hand, abstract-only, or a paraphrase of a source nobody opened
  D  needs a person: the Criterion disc, a physical copy, a paywall, or a browser

The distinction between A and B is the one that matters most. An extractor found
Bordwell and Chatman quotations presented as verbatim that were in fact reconstructed
by triangulating across books quoting them, and downgraded them. A chapter that cites
those as if from the page is making a claim its own research never checked.

Usage:
    python3 v4/tools/merge_claims.py
    python3 v4/tools/merge_claims.py --audit-only
"""
import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXTRACT = ROOT / "v4" / "extract"
OUT = ROOT / "v4" / "factbase" / "CLAIMS.md"

ROW = re.compile(r"^\|\s*(S\d-\d+[^|]*)\|(.*)$")
CLASSCELL = re.compile(r"^\s*\**([ABCD])\**\s*$")

# A qualified class cell -- "A (abstract only)", "A — single-lens" -- is not class A.
# Class A means the source was retrieved and the quotation is verbatim on record. An
# abstract is not the source for a claim about the body, and one lens is not the
# dossier's own three-lens standard. These downgrade on sight; the qualifier survives
# as a note so nothing is lost, only re-rated.
DOWNGRADE = [
    (re.compile(r"abstract", re.I), "C", "abstract only -- body unread"),
    (re.compile(r"metadata|crossref", re.I), "C", "bibliographic metadata only"),
    (re.compile(r"single.lens|one of three|not corrob", re.I), "C", "single lens, uncorroborated"),
    (re.compile(r"second.?hand|characteriz|paraphrase|no explicit", re.I), "C", "second-hand"),
    (re.compile(r"unread|unreachable|needs (?:the )?(?:disc|library|direct)|paywall", re.I), "D",
     "source not obtained"),
    (re.compile(r"do.not.cite|UNVERIFIED", re.I), "X", "forbidden or unverified"),
]

# Rows whose "source" is the dossier itself: search budgets, retrieval logs, vote counts.
# True records, but records of the research process rather than facts about the film,
# the city, the literature, or the platforms. A drafter must never cite one.
PROCESS = re.compile(r"dossier|search record|retrieval record|self.report|research run|"
                     r"synthesis|do.NOT.use section|verification-outcome|access-status", re.I)


def classify(cell):
    """Return (class_letter, note). Qualified cells downgrade."""
    m = CLASSCELL.match(cell)
    if m:
        return m.group(1), ""
    lead = re.match(r"\s*\**([ABCD])\b", cell)
    letter = lead.group(1) if lead else "?"
    for pat, newclass, why in DOWNGRADE:
        if pat.search(cell):
            if letter == "?" or newclass == "X" or newclass > letter:
                return newclass, "%s (was %s)" % (why, letter if letter != "?" else cell[:30])
    return letter, cell.strip() if letter != "?" else cell.strip()[:40]


def parse(path):
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = ROW.match(line.strip())
        if not m:
            continue
        # split on unescaped pipes only -- claim text legitimately contains "\|"
        cells = [c.strip().replace("\\|", "|")
                 for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if len(cells) < 6:
            continue
        if len(cells) > 6:
            # an over-split row: keep the last cell as class, fold the excess into claim
            cid, klass = cells[0], cells[-1]
            claim, source, locator, retrieved = cells[1], cells[-4], cells[-3], cells[-2]
            claim = " ".join([claim] + cells[2:-4])
            cells = [cid, claim, source, locator, retrieved, klass]
        cid, claim, source, locator, retrieved, klass = cells[:6]
        letter, note = classify(klass)
        rows.append({
            "id": cid.strip(),
            "claim": claim,
            "source": source,
            "locator": locator,
            "retrieved": retrieved,
            "class": letter,
            "note": note,
            "process": bool(PROCESS.search(source)),
            "file": path.name,
            "line": n,
        })
    return rows


def norm_source(s):
    s = re.sub(r"[*_`\[\]]", "", s.lower())
    s = re.sub(r"\(\d{4}[a-z]?\)|\b(19|20)\d{2}\b", " ", s)
    s = re.sub(r"[^a-z ]", " ", s)
    toks = [t for t in s.split() if len(t) > 3]
    return " ".join(sorted(set(toks))[:5])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit-only", action="store_true")
    args = ap.parse_args()

    files = sorted(EXTRACT.glob("s?_CLAIMS.md"))
    if not files:
        sys.exit("no extractions found in %s" % EXTRACT)

    allrows = []
    for f in files:
        got = parse(f)
        allrows.extend(got)
        print("  %-18s %4d rows" % (f.name, len(got)))
    print()

    rows = [r for r in allrows if not r["process"]]
    process = [r for r in allrows if r["process"]]
    print("PROCESS ROWS SEPARATED")
    print("  %d of %d rows record the research process rather than a fact about the" % (len(process), len(allrows)))
    print("  film, the city, the literature, or the platforms -- search budgets, retrieval")
    print("  logs, three-lens vote counts. True, but nothing a chapter can cite.")
    print("  They go to PROCESS_NOTES.md, not the fact base.")
    print()

    counts = Counter(r["class"] for r in rows)
    total = len(rows)
    print("PROVENANCE  (fact rows only)")
    labels = {"A": "retrieved, verbatim on record", "B": "convergence-verified, primary unopened",
              "C": "second-hand, abstract-only, or single-lens", "D": "needs a person",
              "X": "forbidden or explicitly unverified", "?": "unparsed"}
    for k in ("A", "B", "C", "D", "X", "?"):
        n = counts.get(k, 0)
        if n:
            print("  class %s  %4d  %5.1f%%   %s" % (k, n, 100 * n / total, labels[k]))
    print("  total    %4d" % total)
    downgraded = [r for r in rows if r["note"] and "was" in r["note"]]
    print()
    print("  %d rows carried a qualified class cell and were re-rated downward." % len(downgraded))
    print("  An abstract is not the source for a claim about the body, and one lens is not")
    print("  the dossiers' own three-lens standard.")
    for r in downgraded[:8]:
        print("    %-10s -> %s   %s" % (r["id"], r["class"], r["note"][:56]))
    if len(downgraded) > 8:
        print("    ... and %d more" % (len(downgraded) - 8))
    print()

    # rows with no locator
    noloc = [r for r in rows if r["locator"].strip().upper() in ("NONE", "", "-", "—")]
    print("LOCATORS")
    print("  %d of %d rows carry no locator (%.0f%%)" % (len(noloc), total, 100 * len(noloc) / total))
    aloc = [r for r in noloc if r["class"] == "A"]
    if aloc:
        print("  %d of those are class A -- a retrieved source with nothing to pin it to:" % len(aloc))
        for r in aloc[:10]:
            print("    %-10s %s" % (r["id"], r["claim"][:78]))
        if len(aloc) > 10:
            print("    ... and %d more" % (len(aloc) - 10))
    print()

    # same source claimed at two classes
    by_source = defaultdict(list)
    for r in rows:
        key = norm_source(r["source"])
        if key:
            by_source[key].append(r)
    conflicts = []
    for key, group in by_source.items():
        classes = {r["class"] for r in group if r["class"] in "ABCD"}
        if len(classes) > 1:
            conflicts.append((key, group, classes))

    print("CLASS CONFLICTS  (one source, two provenance verdicts)")
    if not conflicts:
        print("  none")
    else:
        print("  %d sources classed inconsistently across dossiers." % len(conflicts))
        print("  The rule is that the LOWER class wins until someone opens the source.")
        for key, group, classes in sorted(conflicts, key=lambda c: -len(c[1]))[:12]:
            print("    %-40s %s" % (key[:40], "/".join(sorted(classes))))
            for r in group[:3]:
                print("      %-10s [%s] %s" % (r["id"], r["class"], r["source"][:60]))
    print()

    if args.audit_only:
        return 0

    lines = [
        "# CLAIMS — the v4 fact base",
        "",
        "Every verified fact and quotable passage available to the rebuild, merged from the",
        "seven per-section research dossiers. One row per fact. Interpretive verdicts are not",
        "here — they live in `GLOSSES.md`, quarantined, because a wrong gloss recorded in the v3",
        "outline propagated through four review panels unread and produced a fatal error.",
        "",
        "**Provenance classes.** `A` the dossier retrieved the source and the quotation is verbatim",
        "on record. `B` convergence-verified across secondary sources, primary never opened. `C`",
        "second-hand, abstract-only, or a paraphrase of an unopened source. `D` needs a person —",
        "the Criterion disc, a physical copy, a paywall, or a browser.",
        "",
        "**The rule for drafting.** A and B may be written from. C must be marked in the draft as",
        "second-hand or replaced. D may not be asserted at all until the author supplies it.",
        "",
        "Merged %s from %d dossier extractions, %d rows." % ("2026-08-10", len(files), total),
        "",
        "| ID | Claim | Source | Locator | Retrieved | Class | Provenance note |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in sorted(rows, key=lambda x: x["id"]):
        lines.append("| %s | %s | %s | %s | %s | %s | %s |"
                     % (r["id"], r["claim"], r["source"], r["locator"],
                        r["retrieved"], r["class"], r["note"]))
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote %s (%d fact rows)" % (OUT.relative_to(ROOT), total))

    pn = OUT.parent / "PROCESS_NOTES.md"
    plines = [
        "# Process notes — what the research runs recorded about themselves",
        "",
        "Rows the extraction produced whose source is a dossier's own record: search budgets,",
        "retrieval logs, three-lens vote counts, fetch failures. They are true and they are",
        "useful for judging how far to trust a finding. They are not facts about the film, the",
        "city, the literature, or the platforms, and **nothing here may be cited in the chapter.**",
        "",
        "Separated out of the fact base on 2026-08-10, %d rows." % len(process),
        "",
        "| ID | Record | Source | Class |",
        "|---|---|---|---|",
    ]
    for r in sorted(process, key=lambda x: x["id"]):
        plines.append("| %s | %s | %s | %s |" % (r["id"], r["claim"], r["source"], r["class"]))
    pn.write_text("\n".join(plines) + "\n", encoding="utf-8")
    print("wrote %s (%d process rows)" % (pn.relative_to(ROOT), len(process)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
