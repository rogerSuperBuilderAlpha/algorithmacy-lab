"""Probe Q91 (H1-H4) — does a lossy read collapse the triad sharply or gradually?

Sweeps the channel error on the mediator's read of the recipient and reads the exact Φ at each level.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q91_lossy_channel.probe_lossy_channel
"""

import csv
import os

from org_frontier.probes.lib import max_phi_float
from org_frontier.questions.q91_lossy_channel import forms as F


def main():
    print("PROBE Q91 (H1-H4) — lossy channel on the mediator's read of the recipient")
    print("=" * 74)
    phis = {}
    for e in F.ERRORS:
        phi, _ = max_phi_float(F.lossy_tpm(e))
        phis[e] = float(phi)
        print(f"  channel error e={e:<4} Φ={phi:.4f} ({'triadic' if phi > 1e-6 else 'dyadic'})")

    seq = [phis[e] for e in F.ERRORS]
    h1 = phis[0.0] > 1e-6
    h2 = phis[0.5] <= 1e-6
    h3 = all(seq[i] <= seq[i - 1] + 1e-9 for i in range(1, len(seq))) and seq[0] > seq[-1]
    h4 = phis[0.4] > 1e-6
    print("=" * 74)
    print(f"  H1 perfect channel (e=0) is triadic:             {h1} ({phis[0.0]:.3f})")
    print(f"  H2 zero-capacity channel (e=0.5) is dyadic:      {h2} ({phis[0.5]:.3f})")
    print(f"  H3 Φ decays monotonically with channel error:    {h3}")
    print(f"  H4 the triad survives substantial loss (e=0.4):  {h4} ({phis[0.4]:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "lossy_channel.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["channel_error", "phi"])
        for e in F.ERRORS:
            w.writerow([e, f"{phis[e]:.4f}"])


if __name__ == "__main__":
    main()
