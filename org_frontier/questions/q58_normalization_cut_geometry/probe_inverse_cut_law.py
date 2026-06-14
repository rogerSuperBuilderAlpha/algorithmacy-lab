#!/usr/bin/env python
"""Q58 / H5 — inverse cut-size law for normalized_phi.

Run:  python -m org_frontier.questions.q58_normalization_cut_geometry.probe_inverse_cut_law
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
    print("PROBE 194 (H5) — inverse cut-size law for normalized_phi")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = geometry_rows()
    at_law = 0
    for r in rows:
        norm_phi_ratio = r["excl"]["norm_phi"] / r["tied"]["norm_phi"]
        cut_ones_ratio = r["tied"]["cut_ones"] / r["excl"]["cut_ones"]
        if abs(norm_phi_ratio - cut_ones_ratio) < PHI_TOL:
            at_law += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  norm_phi ratio equals cut_ones ratio: {at_law}/{len(rows)}")

    if at_law == len(rows) == 16:
        decision = "confirmed"
    elif at_law >= 15:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    identity holds on all pairs?  {at_law == len(rows)}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "inverse_cut_law.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology",
                "norm_phi_ratio", "cut_ones_ratio",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "norm_phi_ratio": r["excl"]["norm_phi"] / r["tied"]["norm_phi"],
                "cut_ones_ratio": r["tied"]["cut_ones"] / r["excl"]["cut_ones"],
            })
    return decision


if __name__ == "__main__":
    main()
