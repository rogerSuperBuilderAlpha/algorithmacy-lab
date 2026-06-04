"""Probe 122 (K1) — does the single coupling feature transfer across scale?

Question: the full eight-feature surrogate transfers from n=3 to larger sizes (#99), and party coupling
is the signal that catches even the parity forms (#114). Does the single coupling feature — mean pairwise
mutual information — transfer across scale on its own? Hypothesis: it transfers nearly as well as the full
panel, so the cheap instrument reduces to one number. Method: compute the eight aggregate features on
n=3, n=4, n=5 (reusing #99's pipeline), then evaluate mean-pairwise-MI alone — its rank-AUC in-sample at
n=3 and transferred to n=4 and n=5.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_coupling_transfer
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.corpus.population import enumerate_family
from org_frontier.multiparty.scaling import sample_form
from .probe_surrogate_transfer import dataset
from .probe_phi_ar import _auc

MI_COL = 3   # feats() column for mean pairwise MI


def main():
    print("PROBE 122 (K1) — single coupling feature (mean pairwise MI) across scale")
    print("=" * 64)
    rng = np.random.default_rng(122)
    Xtr, ytr = dataset([(3, r) for _, r in enumerate_family()], rng)
    X4, y4 = dataset([(4, sample_form(4, rng)) for _ in range(400)], rng)
    X5, y5 = dataset([(5, sample_form(5, rng)) for _ in range(400)], rng)
    print(f"  trained signal: mean pairwise MI; {len(ytr)} n=3 forms ({int(ytr.sum())} triadic)")
    print(f"  {'set':<10}{'forms':<9}{'triadic':<10}{'AUC (mean-pairwise-MI)'}")
    for name, X, y in (("n=3", Xtr, ytr), ("n=4", X4, y4), ("n=5", X5, y5)):
        auc = _auc(X[:, MI_COL], y) if 0 < y.sum() < len(y) else float("nan")
        print(f"  {name:<10}{len(y):<9}{int(y.sum()):<10}{auc:.3f}")
    print("=" * 64)
    print("  Reading: a transfer AUC near the eight-feature surrogate's (0.98 at n=4, #99) says the cheap")
    print("  instrument is essentially one number — the mutual information between coordinating parties —")
    print("  and it carries across sizes the exact computation cannot reach.")
    print("=" * 64)


if __name__ == "__main__":
    main()
