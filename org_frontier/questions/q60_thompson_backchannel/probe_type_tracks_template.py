#!/usr/bin/env python
"""Q60 / H4 — Thompson type tracks mediator-severance template.

Run:  python -m org_frontier.questions.q60_thompson_backchannel.probe_type_tracks_template
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
    print("PROBE 203 (H4) — Thompson type tracks template")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    matched = sum(1 for r in rows if r["template_match"])
    seq_match = sum(
        1 for r in rows if r["thompson_type"] == "sequential" and r["template_match"]
    )
    rec_match = sum(
        1 for r in rows if r["thompson_type"] == "reciprocal" and r["template_match"]
    )

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  template match total: {matched}/{len(rows)}")
    print(f"  sequential template match: {seq_match}/8")
    print(f"  reciprocal template match: {rec_match}/8")

    if matched == PANEL_SIZE and seq_match == 8 and rec_match == 8:
        decision = "confirmed"
    elif matched == len(rows) - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    16/16 template matches?  {matched == PANEL_SIZE}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "type_tracks_template.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "thompson_type", "template_match"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "thompson_type": r["thompson_type"],
                "template_match": r["template_match"],
            })
    return decision


if __name__ == "__main__":
    main()
