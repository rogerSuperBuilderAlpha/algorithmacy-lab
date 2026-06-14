#!/usr/bin/env python
"""Q60 / H1 — return-path Thompson typing tracks back-channel recipient.

Run:  python -m org_frontier.questions.q60_thompson_backchannel.probe_return_path_tracks_recipient
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
    print("PROBE 200 (H1) — return-path typing tracks recipient")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    worker_seq = sum(
        1 for r in rows if r["recipient"] == "W" and r["thompson_type"] == "sequential"
    )
    counterpart_rec = sum(
        1 for r in rows if r["recipient"] == "C" and r["thompson_type"] == "reciprocal"
    )
    other = sum(1 for r in rows if r["thompson_type"] == "other")
    matched = sum(1 for r in rows if r["recipient_match"])

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  worker -> sequential: {worker_seq}/8")
    print(f"  counterpart -> reciprocal: {counterpart_rec}/8")
    print(f"  other typing: {other}/{len(rows)}")
    print(f"  recipient match total: {matched}/{len(rows)}")

    if matched == PANEL_SIZE and worker_seq == 8 and counterpart_rec == 8 and other == 0:
        decision = "confirmed"
    elif matched == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    8/8 worker sequential and 8/8 counterpart reciprocal?  "
          f"{worker_seq == 8 and counterpart_rec == 8 and other == 0}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "return_path_tracks_recipient.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "recipient", "thompson_type", "recipient_match"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "recipient": r["recipient"],
                "thompson_type": r["thompson_type"],
                "recipient_match": r["recipient_match"],
            })
    return decision


if __name__ == "__main__":
    main()
