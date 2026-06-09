"""Probe Q98 (H1-H4) — is core membership a conjunctive gate on reading and influence?

Over the full three-node family, records each node's in-influence (how much it reads) and out-influence
(how much it is read), and whether it is in the major complex. Tests whether one axis can compensate the
other, or whether membership needs both substantial.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q98_pivotality_bidirectionality.probe_pivotality_bidirectionality
"""

import csv
import os

import numpy as np

from org_frontier.questions.q98_pivotality_bidirectionality import forms as F

N_WIRINGS = 1200
SEED = 98


def rank_auc(score, label):
    pos = [s for s, y in zip(score, label) if y]
    neg = [s for s, y in zip(score, label) if not y]
    if not pos or not neg:
        return float("nan")
    wins = sum(p > q for p in pos for q in neg)
    ties = sum(p == q for p in pos for q in neg)
    return (wins + 0.5 * ties) / (len(pos) * len(neg))


def main():
    print("PROBE Q98 (H1-H4) — reading vs influence as a gate on core membership")
    print("=" * 78)
    rows = F.observations(3, N_WIRINGS, np.random.default_rng(SEED))
    inf_in = np.array([r["in_influence"] for r in rows])
    inf_out = np.array([r["out_influence"] for r in rows])
    core = np.array([r["in_core"] for r in rows])

    hi = inf_in.max()                        # top influence value on the discrete grid (1.0)

    # H1: strong influence cannot compensate zero reading.
    m = (inf_out >= hi) & (inf_in == 0.0)
    p_strongout_noread = core[m].mean() if m.any() else float("nan")
    m2 = (inf_out >= hi) & (inf_in >= hi)
    p_strongout_strongread = core[m2].mean() if m2.any() else float("nan")
    # H2: strong reading cannot compensate zero influence.
    m3 = (inf_in >= hi) & (inf_out == 0.0)
    p_strongread_noinfl = core[m3].mean() if m3.any() else float("nan")
    # H3: membership tracks the minimum of the two better than the sum.
    auc_min = rank_auc(np.minimum(inf_in, inf_out).tolist(), core.tolist())
    auc_sum = rank_auc((inf_in + inf_out).tolist(), core.tolist())
    # H4: balanced-high membership near-certain.
    p_balanced_high = p_strongout_strongread

    print(f"  {len(rows)} node-obs")
    print(f"  P(core | strong influence, zero reading)  = {p_strongout_noread:.3f}  (n={int(m.sum())})")
    print(f"  P(core | strong reading, zero influence)  = {p_strongread_noinfl:.3f}  (n={int(m3.sum())})")
    print(f"  P(core | strong both)                     = {p_strongout_strongread:.3f}  (n={int(m2.sum())})")
    print(f"  rank-AUC  min(read,infl) -> core = {auc_min:.3f}   sum -> core = {auc_sum:.3f}")

    h1 = (not np.isnan(p_strongout_noread)) and p_strongout_noread < 0.10
    h2 = (not np.isnan(p_strongread_noinfl)) and p_strongread_noinfl < 0.10
    h3 = (not np.isnan(auc_min)) and (not np.isnan(auc_sum)) and auc_min > auc_sum
    h4 = (not np.isnan(p_balanced_high)) and p_balanced_high >= 0.85
    print("=" * 78)
    print(f"  H1 strong influence cannot compensate zero reading (P<0.10):  {h1} ({p_strongout_noread:.3f})")
    print(f"  H2 strong reading cannot compensate zero influence (P<0.10):  {h2} ({p_strongread_noinfl:.3f})")
    print(f"  H3 membership tracks the minimum better than the sum:         {h3} ({auc_min:.3f} > {auc_sum:.3f})")
    print(f"  H4 balanced-high membership near-certain (P>=0.85):           {h4} ({p_balanced_high:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "pivotality_bidirectionality.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["metric", "value", "n"])
        w.writerow(["p_core_strongout_noread", f"{p_strongout_noread:.4f}", int(m.sum())])
        w.writerow(["p_core_strongread_noinfl", f"{p_strongread_noinfl:.4f}", int(m3.sum())])
        w.writerow(["p_core_strong_both", f"{p_strongout_strongread:.4f}", int(m2.sum())])
        w.writerow(["rank_auc_min", f"{auc_min:.4f}", len(rows)])
        w.writerow(["rank_auc_sum", f"{auc_sum:.4f}", len(rows)])


if __name__ == "__main__":
    main()
