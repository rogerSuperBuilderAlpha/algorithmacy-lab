#!/usr/bin/env python
"""Q58 / H1 — severed-connection count ratio on min-norm partitions.

Run:  python -m org_frontier.questions.q58_normalization_cut_geometry.probe_severed_edge_ratio
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q58_normalization_cut_geometry.norm_cut_utils import (  # noqa: E402
    CUT_RATIO,
    PHI_TOL,
    geometry_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 190 (H1) — severed-connection count ratio")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = geometry_rows()
    at_ratio = 0
    ratios = []
    for r in rows:
        ratio = r["tied"]["cut_ones"] / r["excl"]["cut_ones"]
        ratios.append(ratio)
        if abs(ratio - CUT_RATIO) < PHI_TOL:
            at_ratio += 1

    spread = max(ratios) - min(ratios) if ratios else None

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  cut_ones tied/excl ratio {CUT_RATIO}: {at_ratio}/{len(rows)}")
    print(f"  cut_ones spread: {spread:.6f}" if spread is not None else "  cut_ones spread: n/a")

    if at_ratio == len(rows) == 16 and spread is not None and spread < PHI_TOL:
        decision = "confirmed"
    elif at_ratio == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all pairs at cut ratio {CUT_RATIO}?  {at_ratio == len(rows)}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "severed_edge_ratio.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_cut_ones", "excl_cut_ones", "cut_ratio"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_cut_ones": r["tied"]["cut_ones"],
                "excl_cut_ones": r["excl"]["cut_ones"],
                "cut_ratio": r["tied"]["cut_ones"] / r["excl"]["cut_ones"],
            })
    return decision


if __name__ == "__main__":
    main()
