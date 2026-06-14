"""Probe Q90 (H1-H4) — does the core-membership law generalize past the n=3 family?

Replicates probe #12's two-condition test (bidirectional coupling necessary; among coupled nodes,
pivotality predicts major-complex membership) at n = 3, 4, 5 on the full family. The n=3 result was
rank-AUC 0.89; this asks whether the law holds, degrades, or breaks as parties multiply.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q90_membership_law_scaling.probe_membership_law_scaling
"""

import csv
import os

import numpy as np

from org_frontier.questions.q90_membership_law_scaling import forms as F

# Sample sizes fall with n because major-complex cost rises steeply (n=5 is ~27s per wiring).
PLAN = {3: (300, 31), 4: (150, 41), 5: (15, 51)}   # n: (wirings, seed)


def rank_auc(pos, neg):
    if not pos or not neg:
        return float("nan")
    wins = sum(p > q for p in pos for q in neg)
    ties = sum(p == q for p in pos for q in neg)
    return (wins + 0.5 * ties) / (len(pos) * len(neg))


def main():
    print("PROBE Q90 (H1-H4) — core-membership law across n = 3, 4, 5")
    print("=" * 78)
    summary = {}
    all_rows = []
    for n, (N, seed) in PLAN.items():
        rows = F.observations(n, N, np.random.default_rng(seed))
        all_rows.extend(rows)
        nonbidir = [r for r in rows if not r["bidirectional"]]
        bidir = [r for r in rows if r["bidirectional"]]
        nb_rate = sum(r["in_core"] for r in nonbidir) / max(len(nonbidir), 1)
        pos = [r["out_influence"] for r in bidir if r["in_core"]]
        neg = [r["out_influence"] for r in bidir if not r["in_core"]]
        auc = rank_auc(pos, neg)
        # terciles of influence among bidirectional, for monotonicity
        infl = sorted(r["out_influence"] for r in bidir)
        lo_thr = infl[len(infl) // 3] if infl else 0
        hi_thr = infl[2 * len(infl) // 3] if infl else 1
        lo = [r for r in bidir if r["out_influence"] <= lo_thr]
        hi = [r for r in bidir if r["out_influence"] >= hi_thr]
        p_lo = sum(r["in_core"] for r in lo) / max(len(lo), 1)
        p_hi = sum(r["in_core"] for r in hi) / max(len(hi), 1)
        summary[n] = {"nb_rate": nb_rate, "auc": auc, "p_lo": p_lo, "p_hi": p_hi,
                      "n_obs": len(rows), "n_bidir": len(bidir)}
        print(f"  n={n}: {len(rows):>4} node-obs, {len(bidir):>4} bidirectional | "
              f"non-bidir in-core={nb_rate:6.3f} | rank-AUC={auc:.3f} | "
              f"P(core) low-infl={p_lo:.2f} high-infl={p_hi:.2f}")

    h1 = all(summary[n]["nb_rate"] < 0.05 for n in (3, 4, 5))
    h2 = all(summary[n]["auc"] >= 0.75 for n in (3, 4, 5))
    h3 = summary[4]["p_hi"] > summary[4]["p_lo"]
    h4 = summary[4]["auc"] >= summary[3]["auc"] - 0.15
    print("=" * 78)
    print(f"  H1 coupling necessary at every n (non-bidir in-core < 0.05): {h1}")
    print(f"  H2 pivotality predicts membership at every n (AUC >= 0.75):  {h2}")
    print(f"  H3 P(core) rises with influence at n=4:                      {h3} "
          f"({summary[4]['p_lo']:.2f} -> {summary[4]['p_hi']:.2f})")
    print(f"  H4 no sharp degradation n=3 -> n=4 (AUC drop <= 0.15):       {h4} "
          f"({summary[3]['auc']:.3f} -> {summary[4]['auc']:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "membership_law_scaling.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n", "n_obs", "n_bidir", "nonbidir_in_core_rate", "rank_auc",
                    "p_core_low_infl", "p_core_high_infl"])
        for n in (3, 4, 5):
            s = summary[n]
            w.writerow([n, s["n_obs"], s["n_bidir"], f"{s['nb_rate']:.4f}", f"{s['auc']:.4f}",
                        f"{s['p_lo']:.4f}", f"{s['p_hi']:.4f}"])


if __name__ == "__main__":
    main()
