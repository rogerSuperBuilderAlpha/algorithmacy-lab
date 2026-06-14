#!/usr/bin/env python
"""Q60 / H5 — no Phi discrimination between Thompson subpanels.

Run:  python -m org_frontier.questions.q60_thompson_backchannel.probe_no_phi_discrimination
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
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 204 (H5) — no Phi discrimination between subpanels")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    seq = [r for r in rows if r["thompson_type"] == "sequential"]
    rec = [r for r in rows if r["thompson_type"] == "reciprocal"]

    def panel_stats(panel):
        phis = [r["max_phi"] for r in panel]
        structs = {r["structure"] for r in panel}
        spread = max(phis) - min(phis) if phis else None
        mean = sum(phis) / len(phis) if phis else None
        return structs, spread, mean

    seq_struct, seq_spread, seq_mean = panel_stats(seq)
    rec_struct, rec_spread, rec_mean = panel_stats(rec)

    print(f"\n  sequential subpanel: n={len(seq)}")
    print(f"    structures: {sorted(seq_struct)}")
    print(f"    max_phi mean: {seq_mean:.6f}" if seq_mean is not None else "    max_phi mean: n/a")
    print(f"    max_phi spread: {seq_spread:.6f}" if seq_spread is not None else "    max_phi spread: n/a")
    print(f"  reciprocal subpanel: n={len(rec)}")
    print(f"    structures: {sorted(rec_struct)}")
    print(f"    max_phi mean: {rec_mean:.6f}" if rec_mean is not None else "    max_phi mean: n/a")
    print(f"    max_phi spread: {rec_spread:.6f}" if rec_spread is not None else "    max_phi spread: n/a")

    uniform = (
        seq_struct == {"triadic"}
        and rec_struct == {"triadic"}
        and seq_spread is not None
        and rec_spread is not None
        and seq_spread < PHI_TOL
        and rec_spread < PHI_TOL
        and abs(seq_mean - MAX_PHI) < PHI_TOL
        and abs(rec_mean - MAX_PHI) < PHI_TOL
    )

    if uniform:
        decision = "confirmed"
    elif seq_struct == rec_struct == {"triadic"}:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    both subpanels triadic at max_phi=2.0 spread 0?  {uniform}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "no_phi_discrimination.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "thompson_type", "structure", "max_phi"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "thompson_type": r["thompson_type"],
                "structure": r["structure"],
                "max_phi": r["max_phi"],
            })
    return decision


if __name__ == "__main__":
    main()
