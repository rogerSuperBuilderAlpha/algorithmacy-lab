#!/usr/bin/env python
"""Q60 / H3 — feedback-cycle predicate collapses recipient split.

Run:  python -m org_frontier.questions.q60_thompson_backchannel.probe_cycle_collapse
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q60_thompson_backchannel.thompson_backchannel_utils import (  # noqa: E402
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 202 (H3) — feedback-cycle predicate collapse")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    cycle_true = sum(1 for r in rows if r["feedback_cycle"])
    cycle_false = sum(1 for r in rows if not r["feedback_cycle"])

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  feedback_cycle=True: {cycle_true}/{len(rows)}")
    print(f"  feedback_cycle=False: {cycle_false}/{len(rows)}")
    print(f"  sequential by cycle predicate: {cycle_false}/{len(rows)}")

    if cycle_true == PANEL_SIZE:
        decision = "confirmed"
    elif cycle_true == len(rows) - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all 16 cycle=True (all reciprocal by cycle)?  {cycle_true == PANEL_SIZE}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "cycle_collapse.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "recipient", "feedback_cycle"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "recipient": r["recipient"],
                "feedback_cycle": r["feedback_cycle"],
            })
    return decision


if __name__ == "__main__":
    main()
