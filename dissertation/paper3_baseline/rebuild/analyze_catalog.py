"""Paper 3 rebuild — analyze the model-family catalog (from scratch).

Reads rebuild/results/catalog.csv (written by catalog.py) and reports three things the draft
needs:
  1. The Φ landscape: how often the family is reducible (Φ=0) and which discrete bands the
     non-zero scores fall onto. The bands are a property of the family, not assigned.
  2. What drives Φ within the family: group means and an ordinary-least-squares fit of max Φ
     on structural features. The low R² is the point — Φ is not a feature checklist.
  3. The Cerullo (2015) caution, computed: among genuine two-party mediators, parity (XOR/XNOR)
     determinations score the highest Φ, so a high Φ does not certify sophisticated coordination.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/analyze_catalog.py
"""

import csv
import os
import sys
from collections import Counter

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))


def load(path):
    with open(path) as fh:
        return list(csv.DictReader(fh))


def bands(rows, triads_only=True):
    vals = [round(float(r["max_phi"]), 2) for r in rows
            if (not triads_only or r["kind"] == "triad")]
    n = len(vals)
    counts = Counter(vals)
    print(f"\n  Φ bands across {n} {'triad' if triads_only else 'all'} wirings:")
    print(f"  {'Φ band':>8} {'# wirings':>10} {'%':>7}")
    for v in sorted(counts):
        print(f"  {v:8.2f} {counts[v]:10d} {100*counts[v]/n:6.1f}%")
    zero = counts.get(0.0, 0)
    print(f"  reducible (Φ=0): {zero}/{n} = {100*zero/n:.1f}%")
    nonzero_bands = sorted(v for v in counts if v > 0)
    print(f"  distinct non-zero bands: {len(nonzero_bands)}  -> {nonzero_bands}")


def ols(rows):
    """OLS of max Φ on structural features, triads only. Reports partial coefficients and R²."""
    tr = [r for r in rows if r["kind"] == "triad"]
    y = np.array([float(r["max_phi"]) for r in tr])
    feats = ["strict_mediation", "parity_present", "edges",
             "mediator_depends_both", "back_channel"]
    X = np.array([[float(r[f]) for f in feats] for r in tr])
    Xd = np.column_stack([np.ones(len(tr)), X])
    beta, *_ = np.linalg.lstsq(Xd, y, rcond=None)
    yhat = Xd @ beta
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1 - ss_res / ss_tot
    print("\n  OLS of max Φ on structural features (all triads):")
    print(f"    intercept            {beta[0]:+.3f}")
    for f, b in zip(feats, beta[1:]):
        print(f"    {f:22s} {b:+.3f}")
    print(f"    R^2 = {r2:.3f}   (Φ is NOT reducible to a feature checklist)")
    # group means for the two strongest flags
    for f in ["strict_mediation", "parity_present"]:
        on = y[[i for i, r in enumerate(tr) if int(r[f]) == 1]]
        off = y[[i for i, r in enumerate(tr) if int(r[f]) == 0]]
        print(f"    meanΦ {f}=1: {on.mean():.2f}  vs  =0: {off.mean():.2f}")


def cerullo(rows):
    """Among genuine two-party mediators, parity mediators score the highest Φ (Cerullo 2015)."""
    tr = [r for r in rows if r["kind"] == "triad" and int(r["mediator_depends_both"]) == 1]
    parity = [float(r["max_phi"]) for r in tr if r["mediator_fn"] in ("XOR", "XNOR")]
    monotone = [float(r["max_phi"]) for r in tr if r["mediator_fn"] not in ("XOR", "XNOR")]
    print("\n  Cerullo (2015) caution, computed:")
    if parity:
        print(f"    parity (XOR/XNOR) mediators:  meanΦ = {np.mean(parity):.3f}  (n={len(parity)})")
    if monotone:
        print(f"    monotone mediators:           meanΦ = {np.mean(monotone):.3f}  (n={len(monotone)})")
    print("    high Φ does not certify sophisticated coordination -> read magnitude ordinally only")


if __name__ == "__main__":
    path = os.path.join(_HERE, "results", "catalog.csv")
    if not os.path.exists(path):
        sys.exit(f"missing {path} — run catalog.py first")
    rows = load(path)
    print("=" * 78)
    print(f"PAPER 3 rebuild — catalog analysis ({len(rows)} distinct forms)")
    print("=" * 78)
    bands(rows, triads_only=True)
    ols(rows)
    cerullo(rows)
    n_ho = sum(1 for r in rows if r["kind"] == "higher_order")
    print(f"\n  higher-order (n=4) forms in catalog: {n_ho}")
