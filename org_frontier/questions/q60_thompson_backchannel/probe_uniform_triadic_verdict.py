#!/usr/bin/env python
"""Q60 / H2 — uniform triadic verdict on back-channel ceiling panel.

Run:  python -m org_frontier.questions.q60_thompson_backchannel.probe_uniform_triadic_verdict
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import PHI_TOL  # noqa: E402
from org_frontier.questions.q60_thompson_backchannel.thompson_backchannel_utils import (  # noqa: E402
    MAX_PHI,
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 201 (H2) — uniform triadic verdict")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    triadic = sum(1 for r in rows if r["structure"] == "triadic")
    at_phi = sum(1 for r in rows if abs(r["max_phi"] - MAX_PHI) < PHI_TOL)
    phis = [r["max_phi"] for r in rows]
    spread = max(phis) - min(phis) if phis else None

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  triadic structure: {triadic}/{len(rows)}")
    print(f"  max_phi={MAX_PHI}: {at_phi}/{len(rows)}")
    print(f"  max_phi spread: {spread:.6f}" if spread is not None else "  max_phi spread: n/a")

    if triadic == PANEL_SIZE and at_phi == PANEL_SIZE:
        decision = "confirmed"
    elif triadic == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all triadic at max_phi=2.0?  {triadic == PANEL_SIZE and at_phi == PANEL_SIZE}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "uniform_triadic_verdict.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "structure", "max_phi"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "structure": r["structure"],
                "max_phi": r["max_phi"],
            })
    return decision


if __name__ == "__main__":
    main()
