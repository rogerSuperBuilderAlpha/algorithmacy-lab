"""Probe 91 (#39) — does the effective-information/Φ relationship from Probe 49 generalize?

Question: Probe 49 found effective information and exact Φ related on a few forms. Does that hold across
the whole 256-form family, and is causal emergence systematically tied to the verdict? Hypothesis: EI
rises with Φ across the family (triadic forms carry more effective information), and causal emergence is
not what distinguishes triadic from dyadic. Method: read the cached panel; correlate EI with exact Φ,
compare EI and causal emergence between the verdict groups.

Reads: org_frontier/probes/results/consilience_panel.csv (run Probe 89 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ei_family
"""

import csv
import os

import numpy as np

PANEL = os.path.join(os.path.dirname(__file__), "results", "consilience_panel.csv")


def main():
    print("PROBE 91 (#39) — EI and causal emergence vs the verdict across the family")
    print("=" * 68)
    with open(PANEL) as fh:
        rows = list(csv.DictReader(fh))
    phi = np.array([float(r["phi_exact"]) for r in rows])
    ei = np.array([float(r["EI"]) for r in rows])
    ce = np.array([float(r["CE"]) for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    r_phi_ei = float(np.corrcoef(phi, ei)[0, 1])
    print(f"  {len(rows)} forms, {int(y.sum())} triadic")
    print(f"  corr(EI, exact Φ) across the family = {r_phi_ei:+.3f}")
    print(f"  {'group':<10}{'mean EI':<12}{'mean CE':<12}{'mean Φ'}")
    for g, name in ((1, "triadic"), (0, "dyadic")):
        mask = y == g
        print(f"  {name:<10}{ei[mask].mean():<12.4f}{ce[mask].mean():<12.4f}{phi[mask].mean():.4f}")
    print("=" * 68)
    print("  Reading: a positive EI–Φ correlation says effective information tracks integration across")
    print("  the family, generalizing Probe 49. If causal emergence does not differ between the groups,")
    print("  coarse-graining gain is not what the dyadic/triadic verdict measures.")
    print("=" * 68)


if __name__ == "__main__":
    main()
