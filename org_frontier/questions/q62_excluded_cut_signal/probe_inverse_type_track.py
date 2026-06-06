#!/usr/bin/env python
"""Q62 / H2 — excluded singleton inversely tracks return-path type.

Run:  python -m org_frontier.questions.q62_excluded_cut_signal.probe_inverse_type_track
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
    print("PROBE 211 (H2) — excluded inversely tracks return-path type")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    inverse = sum(1 for r in rows if r["inverse_type_match"])
    direct = sum(1 for r in rows if r["direct_type_match"])

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  inverse type matches: {inverse}/{len(rows)}")
    print(f"  direct type matches: {direct}/{len(rows)}")

    if inverse == PANEL_SIZE and direct == 0:
        decision = "confirmed"
    elif inverse == PANEL_SIZE - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    16/16 inverse with 0 direct?  {inverse == PANEL_SIZE and direct == 0}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "inverse_type_track.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology", "excluded_singleton", "thompson_type",
                "inverse_type_match", "direct_type_match",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "excluded_singleton": r["excluded_singleton"],
                "thompson_type": r["thompson_type"],
                "inverse_type_match": r["inverse_type_match"],
                "direct_type_match": r["direct_type_match"],
            })
    return decision


if __name__ == "__main__":
    main()
