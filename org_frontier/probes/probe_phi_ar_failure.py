"""Probe 101 (A3) — what does Φ_AR misrank?

Question: the autoregressive Φ_AR separates the verdict well (AUC 0.959 at Probe 90) but not perfectly,
and at a single threshold it caught only 9 of 24 triadic forms (Probe 89). Which triadic forms does it
miss? Hypothesis: the misses are the parity / pure-higher-order forms (exact Φ = 0.5, Probe 56) — a
linear-Gaussian AR model cannot see binding that exists only in the synergistic whole. Method: from the
cached consilience panel, split triadic forms by exact Φ (the parity Φ=0.5 forms vs the conjunctive Φ=2.0
forms) and compare their Φ_AR scores and ranks.

Reads: org_frontier/probes/results/consilience_panel.csv (run Probe 89 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phi_ar_failure
"""

import csv
import os

import numpy as np

PANEL = os.path.join(os.path.dirname(__file__), "results", "consilience_panel.csv")


def main():
    print("PROBE 101 (A3) — Φ_AR's failure mode")
    print("=" * 64)
    with open(PANEL) as fh:
        rows = list(csv.DictReader(fh))
    par = np.array([float(r["phi_AR"]) for r in rows])
    pex = np.array([float(r["phi_exact"]) for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    # rank all forms by Φ_AR; where do triadic forms sit?
    order = np.argsort(-par)
    ranks = np.empty(len(par), int)
    ranks[order] = np.arange(len(par))
    tri = y == 1
    parity = tri & np.isclose(pex, 0.5)
    conj = tri & (pex > 0.5)
    print(f"  {int(tri.sum())} triadic: {int(conj.sum())} conjunctive (Φ=2.0), {int(parity.sum())} parity (Φ=0.5)")
    print(f"  {'group':<22}{'mean Φ_AR':<14}{'mean rank (0=top)'}")
    print(f"  {'conjunctive triadic':<22}{par[conj].mean():<14.4f}{ranks[conj].mean():.1f}")
    print(f"  {'parity triadic':<22}{par[parity].mean():<14.4f}{ranks[parity].mean():.1f}")
    print(f"  {'dyadic':<22}{par[y==0].mean():<14.4f}{ranks[y==0].mean():.1f}")
    print("=" * 64)
    gap = par[conj].mean() - par[parity].mean()
    print(f"  conjunctive − parity mean Φ_AR = {gap:+.4f}")
    if par[parity].mean() < par[y == 0].mean() + 0.05:
        print("  Reading: the parity triadic forms score as low as dyadic forms under Φ_AR — the linear")
        print("  AR model cannot see purely-synergistic binding, so the parity forms are exactly Φ_AR's")
        print("  false negatives. The proxy's blind spot is the pure-higher-order structure (Probe 56).")
    else:
        print("  Reading: the parity forms are not Φ_AR's main misses; the failure mode lies elsewhere.")
    print("=" * 64)


if __name__ == "__main__":
    main()
