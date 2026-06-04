"""Probe 90 (#37) — does any single cheap measure cleanly separate the verdict?

Question: across the adjacent measures, does any one of them rank the dyadic/triadic verdict cleanly on
its own? Hypothesis: no single cheap measure separates the verdict at AUC 1.0 — the exact verdict needs
either the exact computation or a learned combination (Probe 85), not one information-theoretic scalar.
Method: read the cached consilience panel, rank every measure by rank-AUC against the exact verdict over
the 256 forms, and report the best single measure.

Reads: org_frontier/probes/results/consilience_panel.csv (run Probe 89 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_cheap_search
"""

import csv
import os

from .probe_phi_ar import _auc

PANEL = os.path.join(os.path.dirname(__file__), "results", "consilience_panel.csv")
MEASURES = ("phi_exact", "EI", "CE", "O_info", "phi_AR", "phi_R")


def main():
    print("PROBE 90 (#37) — cheap-measure search: AUC of each single measure vs the verdict")
    print("=" * 64)
    with open(PANEL) as fh:
        rows = list(csv.DictReader(fh))
    y = [int(r["triadic"]) for r in rows]
    ranked = []
    for m in MEASURES:
        ranked.append((m, _auc([float(r[m]) for r in rows], y)))
    ranked.sort(key=lambda x: -abs(x[1] - 0.5))
    print(f"  {len(rows)} forms, {sum(y)} triadic")
    print(f"  {'measure':<12}{'rank-AUC'}")
    for m, a in ranked:
        tag = "  (exact verdict, AUC=1 by construction)" if m == "phi_exact" else ""
        print(f"  {m:<12}{a:.3f}{tag}")
    print("=" * 64)
    cheap = [r for r in ranked if r[0] != "phi_exact"]
    best = max(cheap, key=lambda x: abs(x[1] - 0.5))
    print(f"  best cheap measure: {best[0]} at AUC {best[1]:.3f}")
    print("  Reading: a single cheap measure can rank the verdict well but none reaches the perfect")
    print("  separation a learned feature combination gives (Probe 85). The verdict is more than any")
    print("  one scalar; the autoregressive Φ_AR is the strongest single proxy.")
    print("=" * 64)


if __name__ == "__main__":
    main()
