"""Probe 35 — the minimal-edge triad at n=4.

Probe 30 found every triadic n=3 strict-mediation form has exactly 4 edges. What is the minimal edge
budget for an irreducible n=4 form (worker, system, two counterparts)? Sample the strict-mediation
n=4 family and find the fewest causal edges among triadic forms.

H35: the n=4 minimal triad needs more edges than n=3's four — the joint determination must read all
three outer parties and they must read back, so the floor rises.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_min_triad_n4 [N] [seed]
"""

import collections
import sys

import numpy as np

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.multiparty.scaling import sample_form

LABELS = ("W", "S", "C1", "C2")


def main(N=1500, seed=7):
    rng = np.random.default_rng(seed)
    edges = collections.Counter()
    n_tri = 0
    for _ in range(N):
        rules = sample_form(4, rng)
        v = classify_rules(rules, labels=LABELS)
        if v.structure == "triadic":
            n_tri += 1
            edges[int(cm_from_rules(rules).sum())] += 1
    print(f"PROBE 35 — minimal-edge triad at n=4 (sample N={N})")
    print("=" * 60)
    print(f"  triadic forms found: {n_tri}")
    if n_tri:
        print(f"  minimal edge count among triadic: {min(edges)}  (n=3 was 4)")
        print("  edge-count distribution among triadic:")
        for e in sorted(edges):
            print(f"    {e} edges: {edges[e]}")
    print("=" * 60)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    main(N, seed)
