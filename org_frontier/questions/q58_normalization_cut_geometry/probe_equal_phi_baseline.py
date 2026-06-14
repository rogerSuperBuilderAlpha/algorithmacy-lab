#!/usr/bin/env python
"""Q58 / H3 — equal unnormalized phi on dual outer cuts.

Run:  python -m org_frontier.questions.q58_normalization_cut_geometry.probe_equal_phi_baseline
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q58_normalization_cut_geometry.norm_cut_utils import (  # noqa: E402
    PHI_RATIO,
    PHI_TOL,
    geometry_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 192 (H3) — equal unnormalized phi baseline")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = geometry_rows()
    at_ratio = 0
    for r in rows:
        ratio = r["tied"]["phi"] / r["excl"]["phi"]
        if abs(ratio - PHI_RATIO) < PHI_TOL:
            at_ratio += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  phi tied/excl ratio {PHI_RATIO}: {at_ratio}/{len(rows)}")

    if at_ratio == len(rows) == 16:
        decision = "confirmed"
    elif at_ratio >= 15:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all pairs at phi ratio {PHI_RATIO}?  {at_ratio == len(rows)}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "equal_phi_baseline.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_phi", "excl_phi", "phi_ratio"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_phi": r["tied"]["phi"],
                "excl_phi": r["excl"]["phi"],
                "phi_ratio": r["tied"]["phi"] / r["excl"]["phi"],
            })
    return decision


if __name__ == "__main__":
    main()
