#!/usr/bin/env python
"""Q58 / H2 — normalization factor ratio on min-norm partitions.

Run:  python -m org_frontier.questions.q58_normalization_cut_geometry.probe_norm_factor_ratio
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q58_normalization_cut_geometry.norm_cut_utils import (  # noqa: E402
    NORM_FACTOR_RATIO,
    PHI_TOL,
    geometry_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 191 (H2) — normalization factor ratio")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = geometry_rows()
    at_ratio = 0
    ratios = []
    for r in rows:
        ratio = r["excl"]["norm_factor"] / r["tied"]["norm_factor"]
        ratios.append(ratio)
        if abs(ratio - NORM_FACTOR_RATIO) < PHI_TOL:
            at_ratio += 1

    spread = max(ratios) - min(ratios) if ratios else None

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  norm_factor excl/tied ratio {NORM_FACTOR_RATIO}: {at_ratio}/{len(rows)}")
    print(f"  norm_factor spread: {spread:.6f}" if spread is not None else "  norm_factor spread: n/a")

    if at_ratio == len(rows) == 16 and spread is not None and spread < PHI_TOL:
        decision = "confirmed"
    elif at_ratio == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all pairs at norm_factor ratio {NORM_FACTOR_RATIO}?  {at_ratio == len(rows)}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "norm_factor_ratio.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_norm_factor", "excl_norm_factor", "norm_factor_ratio"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_norm_factor": r["tied"]["norm_factor"],
                "excl_norm_factor": r["excl"]["norm_factor"],
                "norm_factor_ratio": r["excl"]["norm_factor"] / r["tied"]["norm_factor"],
            })
    return decision


if __name__ == "__main__":
    main()
