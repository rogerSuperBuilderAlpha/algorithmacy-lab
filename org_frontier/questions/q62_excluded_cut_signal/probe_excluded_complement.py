#!/usr/bin/env python
"""Q62 / H1 — excluded singleton is complement of tied singleton.

Run:  python -m org_frontier.questions.q62_excluded_cut_signal.probe_excluded_complement
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q62_excluded_cut_signal.excluded_cut_utils import (  # noqa: E402
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 210 (H1) — excluded complement of tied singleton")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    matches = sum(1 for r in rows if r["complement_match"])
    mismatches = len(rows) - matches

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  complement matches: {matches}/{len(rows)}")
    print(f"  complement mismatches: {mismatches}/{len(rows)}")

    if matches == PANEL_SIZE:
        decision = "confirmed"
    elif matches == PANEL_SIZE - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    16/16 complement matches?  {matches == PANEL_SIZE}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "excluded_complement.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_singleton", "excluded_singleton", "complement_match"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_singleton": r["tied_singleton"],
                "excluded_singleton": r["excluded_singleton"],
                "complement_match": r["complement_match"],
            })
    return decision


if __name__ == "__main__":
    main()
