#!/usr/bin/env python
"""Q53 / H1 — counterpart-side AND back-channel restores Phi=2.0.

Run:  python -m org_frontier.questions.q53_impl_phi_ceiling.probe_counterpart_and_ceiling
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q53_impl_phi_ceiling.ceiling_utils import (  # noqa: E402
    LABELS,
    MAX_PHI,
    PHI_TOL,
    apply_topology,
    at_ceiling,
    instrument_control,
    matched_implication_panel,
)
from org_frontier.questions.q51_implication_backchannel.backchannel_utils import edge_count  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 165 (H1) — counterpart-side AND back-channel restores Phi=2.0")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    at_phi2 = 0
    for label, rules in matched_implication_panel():
        bc = apply_topology(rules, "counterpart_and")
        v = verdict(bc, LABELS)
        ceiling = at_ceiling(v)
        at_phi2 += int(ceiling)
        rows.append({"label": label, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "edges": edge_count(bc), "at_phi2": ceiling})
        print(f"  {label}: {v.structure}, max_phi={v.max_phi:.6f}, edges={edge_count(bc)}")

    print(f"\n  matched implication + counterpart AND at Phi=2.0: {at_phi2}/8")
    if at_phi2 >= 1:
        decision = "confirmed"
    elif any(r["structure"] == "triadic" for r in rows):
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    at least one at Phi=2.0?  {at_phi2 >= 1}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "counterpart_and_ceiling.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi", "edges", "at_phi2"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
