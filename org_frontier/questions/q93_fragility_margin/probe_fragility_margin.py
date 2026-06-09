"""Probe Q93 (H1-H4) — a margin-to-dyadic fragility metric and whether it predicts noise survival.

For every triadic form in the 256-form strict-mediation family, counts how many single-bit truth-table
flips collapse it to dyadic (the structural margin), classifies its mediator (parity / monotone / other),
and measures its exact Φ under noise 0.1. Tests whether triadic forms sit on a structural edge, whether
the margin varies, whether it predicts noise survival, and whether parity mediators are the robust ones.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q93_fragility_margin.probe_fragility_margin
"""

import csv
import os

import numpy as np

from org_frontier.questions.q93_fragility_margin import forms as F

NOISE = 0.1


def rank_auc(pos, neg):
    if not pos or not neg:
        return float("nan")
    wins = sum(p > q for p in pos for q in neg)
    ties = sum(p == q for p in pos for q in neg)
    return (wins + 0.5 * ties) / (len(pos) * len(neg))


def main():
    print("PROBE Q93 (H1-H4) — margin-to-dyadic fragility of triadic forms")
    print("=" * 78)
    rows = []
    for bits, rules in F.enumerate_family():
        if not F.is_triadic(rules):
            continue
        collapses, total = F.collapse_count(bits)
        robustness = (total - collapses) / total          # fraction of single flips that PRESERVE triadic
        rows.append({
            "bits": "".join(map(str, bits)),
            "kind": F.mediator_kind(bits),
            "collapses": collapses,
            "robustness": robustness,
            "noise_phi": F.noise_phi(rules, NOISE),
        })

    ntri = len(rows)
    fragile = [r for r in rows if r["collapses"] >= 1]
    frac_fragile = len(fragile) / ntri
    rob_vals = [r["robustness"] for r in rows]
    rob_range = max(rob_vals) - min(rob_vals)
    # H3: does robustness rank-separate high- from low-noise-survival forms?
    med = float(np.median([r["noise_phi"] for r in rows]))
    hi = [r["robustness"] for r in rows if r["noise_phi"] > med]
    lo = [r["robustness"] for r in rows if r["noise_phi"] <= med]
    auc = rank_auc(hi, lo)
    # H4: parity mediators vs monotone mediators
    par = [r["robustness"] for r in rows if r["kind"] == "parity"]
    mon = [r["robustness"] for r in rows if r["kind"] == "monotone"]
    par_mean = float(np.mean(par)) if par else float("nan")
    mon_mean = float(np.mean(mon)) if mon else float("nan")

    print(f"  triadic forms: {ntri}")
    print(f"  on a structural edge (>=1 collapsing single flip): {len(fragile)}/{ntri} ({frac_fragile:.2f})")
    print(f"  robustness fraction: min={min(rob_vals):.3f} max={max(rob_vals):.3f} range={rob_range:.3f}")
    print(f"  margin predicts noise survival: rank-AUC={auc:.3f} (noise Φ median={med:.3f})")
    print(f"  parity-mediator robustness mean={par_mean:.3f} (n={len(par)}) vs "
          f"monotone mean={mon_mean:.3f} (n={len(mon)})")

    h1 = frac_fragile > 0.5
    h2 = rob_range >= 0.25
    h3 = auc >= 0.60
    h4 = (par and mon) and par_mean > mon_mean
    print("=" * 78)
    print(f"  H1 majority sit on a structural edge (>0.5 fragile):     {h1} ({frac_fragile:.2f})")
    print(f"  H2 the margin varies (robustness range >= 0.25):         {h2} ({rob_range:.3f})")
    print(f"  H3 margin predicts noise survival (rank-AUC >= 0.60):    {h3} ({auc:.3f})")
    print(f"  H4 parity mediators more robust than monotone:           {bool(h4)} "
          f"({par_mean:.3f} vs {mon_mean:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", bool(h4))]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "fragility_margin.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["bits", "kind", "collapses", "robustness", "noise_phi"])
        w.writeheader()
        for r in rows:
            w.writerow({**r, "robustness": f"{r['robustness']:.4f}", "noise_phi": f"{r['noise_phi']:.4f}"})


if __name__ == "__main__":
    main()
