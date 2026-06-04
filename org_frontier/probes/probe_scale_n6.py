"""Probe 97 (#11) — does the triadic rate floor or hit zero past n=5?

Question: the strict-mediation triadic rate fell with group size (n=3: 9.4%, lower at n=4, n=5). Does it
keep falling toward zero at n=6, or floor at a small positive rate? Hypothesis: it floors at a small
positive rate rather than vanishing — irreducible coordination stays possible at every size, just rare.
Method: sample strict-mediation n=6 forms, classify, and report the triadic rate with a comparison to
the smaller sizes.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_scale_n6 [N]
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules
from org_frontier.multiparty.scaling import sample_form


def main(N=300):
    print(f"PROBE 97 (#11) — strict-mediation triadic rate at n=6 (N={N})")
    print("=" * 60)
    rng = np.random.default_rng(16)
    labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, 5)])
    n_tri = 0
    for k in range(N):
        if classify_rules(sample_form(6, rng), labels=labels).structure == "triadic":
            n_tri += 1
        if (k + 1) % 100 == 0:
            print(f"  {k+1}/{N}  triadic so far: {n_tri}")
    rate = 100 * n_tri / N
    print("-" * 60)
    print(f"  n=6 triadic rate = {n_tri}/{N} = {rate:.1f}%   (n=3 reference 9.4%)")
    print("=" * 60)
    if n_tri > 0:
        print("  Reading: a small positive rate at n=6 says irreducible coordination does not vanish with")
        print("  size — it floors at a low rate, so triadic forms exist at every group size, just rarely.")
    else:
        print("  Reading: no triadic form sampled at n=6 — the rate is at or near zero, so irreducible")
        print("  strict-mediation coordination may effectively disappear at this size for this family.")
    print("=" * 60)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 300)
