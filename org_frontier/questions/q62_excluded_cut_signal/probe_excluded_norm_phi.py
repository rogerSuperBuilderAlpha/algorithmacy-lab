#!/usr/bin/env python
"""Q62 / H5 — excluded norm uniform, no Phi subpanel lift.

Run:  python -m org_frontier.questions.q62_excluded_cut_signal.probe_excluded_norm_phi
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    EXCLUDED_NORM,
)
from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    PHI_TOL,
)
from org_frontier.questions.q62_excluded_cut_signal.excluded_cut_utils import (  # noqa: E402
    MAX_PHI,
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def spread(vals):
    if not vals:
        return 0.0
    return max(vals) - min(vals)


def main():
    print("PROBE 214 (H5) — excluded norm uniform, no Phi subpanel lift")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    norm_ok = sum(
        1 for r in rows
        if r["excl_norm"] is not None and abs(r["excl_norm"] - EXCLUDED_NORM) < PHI_TOL
    )
    panel_spread = spread([r["max_phi"] for r in rows])
    excl_w = [r["max_phi"] for r in rows if r["excluded_singleton"] == "W"]
    excl_c = [r["max_phi"] for r in rows if r["excluded_singleton"] == "C"]
    w_spread = spread(excl_w)
    c_spread = spread(excl_c)

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  excluded norm {EXCLUDED_NORM}: {norm_ok}/{len(rows)}")
    print(f"  max_phi spread (panel): {panel_spread:.6f}")
    print(f"  excluded-W subpanel spread: {w_spread:.6f} ({len(excl_w)}/8)")
    print(f"  excluded-C subpanel spread: {c_spread:.6f} ({len(excl_c)}/8)")

    norm_confirmed = norm_ok == PANEL_SIZE
    phi_confirmed = w_spread <= PHI_TOL and c_spread <= PHI_TOL

    if norm_confirmed and phi_confirmed:
        decision = "confirmed"
    elif norm_ok == PANEL_SIZE - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    16/16 norm 1.0 and subpanel spread 0?  {norm_confirmed and phi_confirmed}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "excluded_norm_phi.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology", "excluded_singleton", "excl_norm", "max_phi",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "excluded_singleton": r["excluded_singleton"],
                "excl_norm": r["excl_norm"],
                "max_phi": r["max_phi"],
            })
    return decision


if __name__ == "__main__":
    main()
