#!/usr/bin/env python
"""Q57 / H1 — back-channel recipient determines tied singleton seam.

Run:  python -m org_frontier.questions.q57_channel_direction_mip.probe_recipient_seam_rule
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    back_channel_recipient,
    enriched_rows,
    expected_tied_cut,
    instrument_control,
    tied_outer_cut,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 185 (H1) — back-channel recipient determines tied singleton seam")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_rows()
    match = 0
    for r in rows:
        expected = expected_tied_cut(r["topology"])
        actual = tied_outer_cut(r)
        if actual == expected:
            match += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  recipient matches tied singleton: {match}/{len(rows)}")

    if match == len(rows) == 16:
        decision = "confirmed"
    elif match == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all recipient-to-seam matches?  {match == len(rows)}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "recipient_seam_rule.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "recipient", "expected_tied", "actual_tied", "match"],
        )
        w.writeheader()
        for r in rows:
            expected = expected_tied_cut(r["topology"])
            actual = tied_outer_cut(r)
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "recipient": back_channel_recipient(r["topology"]),
                "expected_tied": expected,
                "actual_tied": actual,
                "match": actual == expected,
            })
    return decision


if __name__ == "__main__":
    main()
