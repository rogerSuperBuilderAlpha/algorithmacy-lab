#!/usr/bin/env python
"""Q61 / H1 — official singleton seam tracks return-path type bijection.

Run:  python -m org_frontier.questions.q61_seam_return_typing.probe_seam_tracks_type
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q61_seam_return_typing.seam_return_utils import (  # noqa: E402
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 205 (H1) — singleton seam tracks return-path type bijection")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    matched = sum(1 for r in rows if r["seam_match"])
    w_seq = sum(1 for r in rows if r["singleton"] == "W" and r["thompson_type"] == "sequential")
    c_rec = sum(1 for r in rows if r["singleton"] == "C" and r["thompson_type"] == "reciprocal")
    mismatches = PANEL_SIZE - matched
    other = sum(1 for r in rows if r["thompson_type"] == "other")

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  W seam + sequential: {w_seq}/8")
    print(f"  C seam + reciprocal: {c_rec}/8")
    print(f"  seam-type matches: {matched}/{len(rows)}")
    print(f"  mismatches: {mismatches}/{len(rows)}")
    print(f"  other typing: {other}/{len(rows)}")

    if matched == PANEL_SIZE and w_seq == 8 and c_rec == 8 and other == 0:
        decision = "confirmed"
    elif matched == len(rows) - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    16/16 seam-type bijection?  {matched == PANEL_SIZE}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_tracks_type.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "singleton", "thompson_type", "seam_match"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "singleton": r["singleton"],
                "thompson_type": r["thompson_type"],
                "seam_match": r["seam_match"],
            })
    return decision


if __name__ == "__main__":
    main()
