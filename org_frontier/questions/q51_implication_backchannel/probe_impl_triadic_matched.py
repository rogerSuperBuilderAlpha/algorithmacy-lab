#!/usr/bin/env python
"""Q51 / H2 — worker back-channel enables triadic binding for most matched forms.

Run:  python -m org_frontier.questions.q51_implication_backchannel.probe_impl_triadic_matched
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    LABELS, edge_count, implication_forms, instrument_control, matched_live_reads, worker_backchannel,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 156 (H2) — worker back-channel enables triadic binding for most matched forms")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    triadic = 0
    for label, rules in implication_forms(matched_live_reads):
        bc = worker_backchannel(rules)
        v = verdict(bc, LABELS)
        is_tri = v.structure == "triadic"
        triadic += int(is_tri)
        rows.append({"label": label, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "edges": edge_count(bc)})
        print(f"  {label}: {v.structure}, max_phi={v.max_phi:.6f}")

    print(f"\n  triadic matched implication + worker back-channel: {triadic}/8")
    if triadic >= 6:
        decision = "confirmed"
    elif triadic >= 1:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    at least six triadic?  {triadic >= 6}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "impl_triadic_matched.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi", "edges"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
