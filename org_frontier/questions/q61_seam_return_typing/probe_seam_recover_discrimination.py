#!/usr/bin/env python
"""Q61 / H5 — singleton seam recovers verdict-lost typing discrimination.

Run:  python -m org_frontier.questions.q61_seam_return_typing.probe_seam_recover_discrimination
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q60_thompson_backchannel.thompson_backchannel_utils import MAX_PHI  # noqa: E402
from org_frontier.questions.q61_seam_return_typing.seam_return_utils import (  # noqa: E402
    PHI_TOL,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 209 (H5) — seam recovers verdict-lost discrimination")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    phis = [r["max_phi"] for r in rows]
    spread = max(phis) - min(phis) if phis else 0.0

    w_seq_match = sum(
        1 for r in rows if r["singleton"] == "W" and r["thompson_type"] == "sequential"
    )
    c_rec_match = sum(
        1 for r in rows if r["singleton"] == "C" and r["thompson_type"] == "reciprocal"
    )
    subpanel_match = w_seq_match + c_rec_match

    seq_rows = [r for r in rows if r["thompson_type"] == "sequential"]
    rec_rows = [r for r in rows if r["thompson_type"] == "reciprocal"]
    w_rows = [r for r in rows if r["singleton"] == "W"]
    c_rows = [r for r in rows if r["singleton"] == "C"]

    def subpanel_spread(panel):
        vals = [r["max_phi"] for r in panel]
        return max(vals) - min(vals) if vals else 0.0

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  max_phi spread (panel): {spread:.6f}")
    print(f"  sequential subpanel spread: {subpanel_spread(seq_rows):.6f}")
    print(f"  reciprocal subpanel spread: {subpanel_spread(rec_rows):.6f}")
    print(f"  W-seam subpanel spread: {subpanel_spread(w_rows):.6f}")
    print(f"  C-seam subpanel spread: {subpanel_spread(c_rows):.6f}")
    print(f"  W-seam = sequential: {w_seq_match}/8")
    print(f"  C-seam = reciprocal: {c_rec_match}/8")
    print(f"  subpanel match total: {subpanel_match}/16")

    spread_ok = spread <= PHI_TOL
    subpanels_ok = w_seq_match == 8 and c_rec_match == 8
    if subpanels_ok and spread_ok:
        decision = "confirmed"
    elif subpanel_match == 15:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    subpanels match with uniform max_phi?  {subpanels_ok and spread_ok}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_recover_discrimination.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology", "singleton", "thompson_type",
                "max_phi", "subpanel_match",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "singleton": r["singleton"],
                "thompson_type": r["thompson_type"],
                "max_phi": f"{r['max_phi']:.6f}",
                "subpanel_match": r["seam_match"],
            })
    return decision


if __name__ == "__main__":
    main()
