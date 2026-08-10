#!/usr/bin/env python3
"""Compare two independent codings of the film's 34 transitions and report the band.

The chapter's one original empirical claim is a count of how many joins between the
film's dialogue segments a viewer can hear. Two coders worked the same scheme blind to
each other. This compares them transition by transition, reports where they agree, and
publishes the disagreements rather than averaging them away -- which is condition 1 of
the amended rule in ASSUMPTIONS.md A3a.

Agreement is reported as raw percent and as Cohen's kappa, which corrects for the
agreement two coders would reach by chance given how lopsided the categories are. With
NONE this common, raw agreement flatters; kappa is the honest number.

Usage:
    python3 v4/tools/reconcile_census.py
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FB = ROOT / "v4" / "factbase"
CODES = ("SPOKEN-BRIDGE", "ECHO", "NONE", "EQUIVOCAL", "DELIBERATE", "INCIDENTAL")


def parse(path):
    """{transition: (link, agency)} from a coder's table."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.match(r"^\**\s*(\d+)\s*(?:→|->|&rarr;)\s*(\d+)", cells[0])
        if not m:
            continue
        key = "%s→%s" % (m.group(1), m.group(2))
        link = next((c for c in CODES if re.search(r"\b%s\b" % c, cells[1], re.I)), None)
        agency = next((c for c in CODES if re.search(r"\b%s\b" % c, cells[2], re.I)), None)
        if link or agency:
            out[key] = (link, agency)
    return out


def kappa(pairs):
    """Cohen's kappa over (a, b) label pairs."""
    pairs = [(a, b) for a, b in pairs if a and b]
    n = len(pairs)
    if not n:
        return float("nan")
    po = sum(1 for a, b in pairs if a == b) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(ca) | set(cb))
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def report(dim, idx, c1, c2, keys):
    pairs = [(c1[k][idx], c2[k][idx]) for k in keys]
    both = [(a, b) for a, b in pairs if a and b]
    agree = [1 for a, b in both if a == b]
    print("%s" % dim)
    print("  coder 1: %s" % dict(Counter(a for a, _ in both)))
    print("  coder 2: %s" % dict(Counter(b for _, b in both)))
    print("  agreement %d/%d = %.0f%%   kappa %.2f"
          % (len(agree), len(both), 100 * len(agree) / len(both), kappa(both)))
    diffs = [(k, a, b) for k, (a, b) in zip(keys, pairs) if a and b and a != b]
    if diffs:
        print("  disagreements:")
        for k, a, b in diffs:
            print("    %-8s coder1 %-14s coder2 %s" % (k, a, b))
    print()
    return both, diffs


def main():
    p1, p2 = FB / "handoff_census_coder1.md", FB / "handoff_census_coder2.md"
    for p in (p1, p2):
        if not p.exists():
            sys.exit("missing %s" % p)
    c1, c2 = parse(p1), parse(p2)
    keys = sorted(set(c1) & set(c2), key=lambda k: int(k.split("→")[0]))
    print("handoff census reconciliation")
    print("  coder 1 coded %d transitions, coder 2 coded %d, %d in common"
          % (len(c1), len(c2), len(keys)))
    missing = sorted(set(range(1, 35)) - {int(k.split("→")[0]) for k in keys})
    if missing:
        print("  NOT coded by both: %s" % missing)
    print()

    link_pairs, link_diffs = report("AUDIBLE LINK", 0, c1, c2, keys)
    ag_pairs, ag_diffs = report("AGENCY", 1, c1, c2, keys)

    # the band: an audible link is a spoken bridge or an echo
    def audible(labels):
        return sum(1 for x in labels if x in ("SPOKEN-BRIDGE", "ECHO"))

    a1 = audible([a for a, _ in link_pairs])
    a2 = audible([b for _, b in link_pairs])
    eq1 = sum(1 for a, _ in link_pairs if a == "EQUIVOCAL")
    eq2 = sum(1 for _, b in link_pairs if b == "EQUIVOCAL")
    d1 = sum(1 for a, _ in ag_pairs if a == "DELIBERATE")
    d2 = sum(1 for _, b in ag_pairs if b == "DELIBERATE")

    print("THE BAND  (what the chapter may assert)")
    print("  audible link (spoken bridge or echo): %d-%d of %d"
          % (min(a1, a2), max(a1, a2), len(link_pairs)))
    print("  equivocal:                            %d-%d" % (min(eq1, eq2), max(eq1, eq2)))
    print("  produced by a deliberate act:         %d-%d of %d"
          % (min(d1, d2), max(d1, d2), len(ag_pairs)))
    print()
    print("  A point estimate is not available and must not be printed. The two")
    print("  dimensions are not interchangeable: roughly a third of audible links are")
    print("  incidental -- someone overheard rather than someone handing off.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
