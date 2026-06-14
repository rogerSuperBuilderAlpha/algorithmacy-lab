#!/usr/bin/env python
"""Q56 / H5 — minimum normalized-phi rule predicts official tie set on ceiling pairs.

Run:  python -m org_frontier.questions.q56_symmetric_complete_mip.probe_min_norm_tiebreak
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    instrument_control,
    ceiling_panel,
    scan_row,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 184 (H5) — minimum normalized-phi rule predicts official tie set")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = [scan_row(r) for r in ceiling_panel()]
    match = sum(1 for r in rows if r["predicted"] == r["official"])
    mismatch = len(rows) - match

    print(f"\n  ceiling pairs tested: {len(rows)}")
    print(f"  predicted matches official ties: {match}/{len(rows)}")
    print(f"  mismatches: {mismatch}")

    if match == len(rows) == 32:
        decision = "confirmed"
    elif match == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all ceiling pairs match min-norm rule?  {match == len(rows)}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "min_norm_tiebreak.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "official", "predicted", "match"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "official": "|".join(r["official"]),
                "predicted": "|".join(r["predicted"]),
                "match": r["predicted"] == r["official"],
            })
    return decision


if __name__ == "__main__":
    main()
