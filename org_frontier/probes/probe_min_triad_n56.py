"""Probe 96 (#3) — is the 2(n−1) edge floor tight at n=5 and n=6?

Question: triadic forms need bidirectional coupling, giving a conjectured 2(n−1) edge floor (each of the
n−1 outer parties needs an edge in and an edge out through the mediator). Is that floor reached at n=5
and n=6? Hypothesis: yes — the leanest triadic forms sit exactly at 2(n−1) edges (8 at n=5, 10 at n=6).
Method: sample strict-mediation forms at n=5 and n=6, classify, and report the minimum edge count among
triadic forms against the 2(n−1) floor.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_min_triad_n56 [N5] [N6]
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.multiparty.scaling import sample_form


def survey(n, N, rng):
    labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)])
    tri_edges, n_tri = [], 0
    for _ in range(N):
        rules = sample_form(n, rng)
        v = classify_rules(rules, labels=labels)
        if v.structure == "triadic":
            n_tri += 1
            tri_edges.append(int(cm_from_rules(rules).sum()))
    return n_tri, tri_edges


def main(N5=300, N6=150):
    print("PROBE 96 (#3) — minimum triadic edge count at n=5 and n=6")
    print("=" * 60)
    rng = np.random.default_rng(6)
    for n, N in ((5, N5), (6, N6)):
        n_tri, edges = survey(n, N, rng)
        floor = 2 * (n - 1)
        if edges:
            print(f"  n={n} (N={N}): {n_tri} triadic, min edges={min(edges)}, "
                  f"floor 2(n-1)={floor}  {'(tight)' if min(edges)==floor else '(above floor)'}")
        else:
            print(f"  n={n} (N={N}): 0 triadic sampled — rate too low to bound the floor")
    print("=" * 60)
    print("  Reading: if the minimum triadic edge count equals 2(n-1) at both sizes, the bidirectional-")
    print("  coupling floor is tight as the group grows — irreducible coordination cannot be leaner.")
    print("=" * 60)


if __name__ == "__main__":
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 150
    main(a, b)
