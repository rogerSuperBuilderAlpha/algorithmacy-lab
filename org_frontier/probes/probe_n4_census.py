"""Probe 95 (#4) — the n=4 strict-mediation triadic rate and edge distribution.

Question: the n=3 strict-mediation census found 9.4% of forms triadic. What is the rate at n=4, and how
many edges do triadic forms carry? Hypothesis: the triadic rate stays low (single digits) and triadic
forms cluster near the minimum edge count, as the irreducible cases are sparse and lean. Method: large-
sample the n=4 strict-mediation family (S reads all parties, each party reads S), classify each with the
exact verdict, and report the triadic rate and the edge-count distribution by group.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_n4_census [N]
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


def main(N=3000):
    print(f"PROBE 95 (#4) — n=4 strict-mediation census (large sample N={N})")
    print("=" * 64)
    rng = np.random.default_rng(4)
    labels = ("W", "S", "C1", "C2")
    tri_edges, dya_edges, n_tri = [], [], 0
    for _ in range(N):
        rules = sample_form(4, rng)
        v = classify_rules(rules, labels=labels)
        e = int(cm_from_rules(rules).sum())
        if v.structure == "triadic":
            n_tri += 1
            tri_edges.append(e)
        else:
            dya_edges.append(e)
    print(f"  triadic rate = {n_tri}/{N} = {100*n_tri/N:.1f}%  (n=3 reference: 9.4%)")
    if tri_edges:
        print(f"  edges among triadic: min={min(tri_edges)}, mean={np.mean(tri_edges):.1f}  "
              f"(floor 2(n-1)=6)")
    print(f"  edges among dyadic:  mean={np.mean(dya_edges):.1f}")
    print("=" * 64)
    print("  Reading: a low triadic rate with triadic forms near the edge floor says irreducible n=4")
    print("  coordination is sparse and lean, the same shape the n=3 census showed.")
    print("=" * 64)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
