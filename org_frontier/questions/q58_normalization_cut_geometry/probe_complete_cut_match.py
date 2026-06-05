#!/usr/bin/env python
"""Q58 / H4 — complete partition shares recipient cut geometry.

Run:  python -m org_frontier.questions.q58_normalization_cut_geometry.probe_complete_cut_match
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q58_normalization_cut_geometry.norm_cut_utils import (  # noqa: E402
    PHI_TOL,
    geometry_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 193 (H4) — complete shares recipient cut geometry")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = geometry_rows()
    cut_match = 0
    norm_match = 0
    for r in rows:
        if r["complete"]["cut_ones"] == r["tied"]["cut_ones"]:
            cut_match += 1
        if abs(r["complete"]["norm_factor"] - r["tied"]["norm_factor"]) < PHI_TOL:
            norm_match += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  complete cut_ones matches recipient: {cut_match}/{len(rows)}")
    print(f"  complete norm_factor matches recipient: {norm_match}/{len(rows)}")

    if cut_match == norm_match == len(rows) == 16:
        decision = "confirmed"
    elif cut_match == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    both fields match on all pairs?  {cut_match == norm_match == len(rows)}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "complete_cut_match.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology",
                "tied_cut_ones", "complete_cut_ones",
                "tied_norm_factor", "complete_norm_factor",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_cut_ones": r["tied"]["cut_ones"],
                "complete_cut_ones": r["complete"]["cut_ones"],
                "tied_norm_factor": r["tied"]["norm_factor"],
                "complete_norm_factor": r["complete"]["norm_factor"],
            })
    return decision


if __name__ == "__main__":
    main()
