#!/usr/bin/env python
"""Q52 / H1 — W-centric commits split by party-read polarity at (W=1,C=0).

Run:  python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_wcentric_polarity
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q52_phi_ladder_mechanism.ladder_utils import (  # noqa: E402
    LABELS, W_CENTRIC, commit_out_at, implication_forms, instrument_control,
    ladder_rung, matched_live_reads, s_index, w_centric_high_predicted,
    worker_backchannel, w_index,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 160 (H1) — W-centric commits split by party-read polarity at (W=1,C=0)")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    mismatches = 0
    for label, rules in implication_forms(matched_live_reads):
        if s_index(label) not in W_CENTRIC:
            continue
        bc = worker_backchannel(rules)
        v = verdict(bc, LABELS)
        iw = w_index(label)
        out_10 = commit_out_at(label, 1, 0)
        predicted_high = w_centric_high_predicted(label)
        predicted = "high" if predicted_high else "dyadic"
        observed = ladder_rung(label, v.structure, v.max_phi)
        ok = predicted == observed
        mismatches += int(not ok)
        rows.append({
            "label": label, "s_index": s_index(label), "w_index": iw,
            "out_10": out_10, "predicted_rung": predicted, "observed_rung": observed,
            "structure": v.structure, "max_phi": f"{v.max_phi:.6f}", "match": ok,
        })
        print(f"  {label}: out(1,0)={out_10} iw={iw} predicted={predicted} "
              f"observed={observed} max_phi={v.max_phi:.6f}")

    print(f"\n  W-centric matched forms: {len(rows)}  mismatches: {mismatches}")
    decision = "confirmed" if mismatches == 0 else ("partial" if mismatches < len(rows) else "refuted")
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero mismatches?  {mismatches == 0}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "wcentric_polarity.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
