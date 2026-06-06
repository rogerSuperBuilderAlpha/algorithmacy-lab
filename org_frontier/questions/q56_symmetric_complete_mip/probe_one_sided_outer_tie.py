#!/usr/bin/env python
"""Q56 / H2 — aligned one-sided ceiling pairs tie one outer-party cut with complete.

Run:  python -m org_frontier.questions.q56_symmetric_complete_mip.probe_one_sided_outer_tie
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
    one_sided_ceiling,
    scan_row,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 181 (H2) — one-sided ceiling pairs tie one outer-party cut with complete")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = [scan_row(r) for r in one_sided_ceiling()]
    dual_tie = 0
    for r in rows:
        has_complete = COMPLETE in r["official"]
        if r["outer_count_official"] == 1 and has_complete and len(r["official"]) == 2:
            dual_tie += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  one outer-party + complete ties: {dual_tie}/{len(rows)}")

    if dual_tie == len(rows) == 16:
        decision = "confirmed"
    elif dual_tie == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all one-sided dual-tie pattern?  {dual_tie == len(rows)}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "one_sided_outer_tie.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "official", "outer_in_official"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "official": "|".join(r["official"]),
                "outer_in_official": "|".join(r["outer_in_official"]),
            })
    return decision


if __name__ == "__main__":
    main()
