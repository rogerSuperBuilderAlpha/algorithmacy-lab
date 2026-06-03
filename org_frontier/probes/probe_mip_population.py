"""Probe 33 — the MIP fault line across the family (population of Probe 26).

Probe 26 found every triadic CORPUS form cuts at {W,SC} (the worker is the weakest seam). Is that a
property of those curated forms or of the whole family? Tally the minimum-information partition over
every triadic form in the strict-mediation n=3 family.

H33: across the family the worker is the most-frequently-severed element — the triad's weak seam is
systematically the worker, not just in the curated cases.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_mip_population
"""

import collections

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family

LABELS = ("W", "S", "C")


def main():
    cuts = collections.Counter()
    n_tri = 0
    for label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        if v.structure == "triadic":
            n_tri += 1
            cuts[v.mip_partition] += 1

    print("PROBE 33 — MIP fault line across the strict-mediation family")
    print("=" * 70)
    print(f"  triadic forms: {n_tri}")
    print("  MIP cut distribution:")
    for cut, n in cuts.most_common():
        print(f"    {cut:<28} {n}  ({100*n/max(n_tri,1):.0f}%)")
    print("=" * 70)
    print("  Reading: a {W, SC} cut means the worker is the severed singleton — the weakest seam.")
    print("=" * 70)


if __name__ == "__main__":
    main()
