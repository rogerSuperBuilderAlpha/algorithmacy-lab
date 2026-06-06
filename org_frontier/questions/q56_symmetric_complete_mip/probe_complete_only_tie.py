#!/usr/bin/env python
"""Q56 / H1 — symmetric ceiling pairs have complete-only official tie set.

Run:  python -m org_frontier.questions.q56_symmetric_complete_mip.probe_complete_only_tie
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    COMPLETE,
    instrument_control,
    scan_row,
    symmetric_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 180 (H1) — symmetric ceiling pairs have complete-only official tie set")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = [scan_row(r) for r in symmetric_ceiling()]
    complete_only = sum(1 for r in rows if r["official"] == [COMPLETE])
    with_outer = sum(1 for r in rows if r["outer_count_official"] > 0)

    print(f"\n  symmetric ceiling pairs: {len(rows)}")
    print(f"  complete-only official ties: {complete_only}/{len(rows)}")
    print(f"  with outer-party in official ties: {with_outer}/{len(rows)}")

    if complete_only == len(rows) == 16 and with_outer == 0:
        decision = "confirmed"
    elif complete_only == len(rows) and with_outer == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all symmetric complete-only?  {complete_only == len(rows)}")
    print(f"    zero outer-party in ties?  {with_outer == 0}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "complete_only_tie.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "official", "outer_count_official"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "official": "|".join(r["official"]),
                "outer_count_official": r["outer_count_official"],
            })
    return decision


if __name__ == "__main__":
    main()
