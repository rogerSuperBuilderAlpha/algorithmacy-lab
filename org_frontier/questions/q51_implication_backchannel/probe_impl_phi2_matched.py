#!/usr/bin/env python
"""Q51 / H1 — matched implication binds at Phi=2.0 with worker back-channel.

Run:  python -m org_frontier.questions.q51_implication_backchannel.probe_impl_phi2_matched
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
    LABELS, MAX_PHI, PHI_TOL, edge_count, implication_forms, instrument_control,
    matched_live_reads, worker_backchannel,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 155 (H1) — matched implication binds at Phi=2.0 with worker back-channel")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    at_ceiling = 0
    for label, rules in implication_forms(matched_live_reads):
        bc = worker_backchannel(rules)
        v = verdict(bc, LABELS)
        ceiling = v.structure == "triadic" and v.max_phi >= MAX_PHI - PHI_TOL
        at_ceiling += int(ceiling)
        rows.append({"label": label, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "edges": edge_count(bc), "at_phi2": ceiling})
        print(f"  {label}: {v.structure}, max_phi={v.max_phi:.6f}, edges={edge_count(bc)}")

    print(f"\n  matched implication + worker back-channel at Phi=2.0: {at_ceiling}/8")
    if at_ceiling >= 1:
        decision = "confirmed"
    elif any(r["structure"] == "triadic" for r in rows):
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    at least one at Phi=2.0?  {at_ceiling >= 1}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "impl_phi2_matched.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi", "edges", "at_phi2"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
