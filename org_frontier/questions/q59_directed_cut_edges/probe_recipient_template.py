#!/usr/bin/env python
"""Q59 / H5 — recipient-class edge templates gate-invariant.

Run:  python -m org_frontier.questions.q59_directed_cut_edges.probe_recipient_template
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    WORKER_TOPOLOGIES,
)
from org_frontier.questions.q59_directed_cut_edges.cut_edge_utils import (  # noqa: E402
    edge_detail_rows,
    expected_templates,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 199 (H5) — recipient-template gate invariance")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = edge_detail_rows()
    worker_match = 0
    counterpart_match = 0
    mismatches = 0
    for r in rows:
        exp_tied, exp_excl = expected_templates(r["topology"])
        ok = r["only_tied"] == exp_tied and r["only_excl"] == exp_excl
        if r["topology"] in WORKER_TOPOLOGIES:
            if ok:
                worker_match += 1
            else:
                mismatches += 1
        else:
            if ok:
                counterpart_match += 1
            else:
                mismatches += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  worker template match: {worker_match}/8")
    print(f"  counterpart template match: {counterpart_match}/8")
    print(f"  mismatches: {mismatches}")

    if worker_match == 8 and counterpart_match == 8 and mismatches == 0:
        decision = "confirmed"
    elif mismatches == 1:
        decision = "partial"
    else:
        decision = "refuted" if mismatches >= 2 else "partial"

    if worker_match == 8 and counterpart_match == 8:
        decision = "confirmed"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    worker 8/8 and counterpart 8/8?  {worker_match == 8 and counterpart_match == 8}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "recipient_template.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "only_tied", "only_excl", "match"],
        )
        w.writeheader()
        for r in rows:
            exp_tied, exp_excl = expected_templates(r["topology"])
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "only_tied": ";".join(sorted(r["only_tied"])),
                "only_excl": ";".join(sorted(r["only_excl"])),
                "match": r["only_tied"] == exp_tied and r["only_excl"] == exp_excl,
            })
    return decision


if __name__ == "__main__":
    main()
