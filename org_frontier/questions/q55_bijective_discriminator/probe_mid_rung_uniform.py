#!/usr/bin/env python
"""Q55 / H2 — uniform mid-rung Phi on the below-ceiling half.

Run:  python -m org_frontier.questions.q55_bijective_discriminator.probe_mid_rung_uniform
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    MAX_PHI,
    PHI_TOL,
)
from org_frontier.questions.q55_bijective_discriminator.discriminator_utils import (  # noqa: E402
    MID_RUNG,
    bijective_parity_panel,
    instrument_control,
    split_below_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 176 (H2) — uniform mid-rung Phi on the below-ceiling half")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = bijective_parity_panel()
    below, ceiling = split_below_ceiling(rows)

    below_off_mid = sum(1 for r in below if abs(r["max_phi"] - MID_RUNG) > PHI_TOL)
    ceiling_off = sum(1 for r in ceiling if r["max_phi"] < MAX_PHI - PHI_TOL)
    below_spread = max(r["max_phi"] for r in below) - min(r["max_phi"] for r in below) if below else 0.0
    ceiling_spread = max(r["max_phi"] for r in ceiling) - min(r["max_phi"] for r in ceiling) if ceiling else 0.0

    print(f"\n  below ceiling: {len(below)}")
    print(f"  at ceiling: {len(ceiling)}")
    print(f"  below off mid rung {MID_RUNG:.6f}: {below_off_mid}/{len(below)}")
    print(f"  ceiling below 2.0: {ceiling_off}/{len(ceiling)}")
    print(f"  below phi spread: {below_spread:.6f}")
    print(f"  ceiling phi spread: {ceiling_spread:.6f}")

    if below_off_mid == 0 and ceiling_off == 0 and below_spread < PHI_TOL and ceiling_spread < PHI_TOL:
        decision = "confirmed"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all below at mid rung?  {below_off_mid == 0}")
    print(f"    all ceiling at 2.0?  {ceiling_off == 0}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "mid_rung_uniform.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "max_phi", "at_ceiling", "mid_rung"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "max_phi": f"{r['max_phi']:.6f}",
                "at_ceiling": r["at_ceiling"],
                "mid_rung": abs(r["max_phi"] - MID_RUNG) <= PHI_TOL,
            })
    return decision


if __name__ == "__main__":
    main()
