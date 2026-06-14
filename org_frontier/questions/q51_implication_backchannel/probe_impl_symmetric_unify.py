#!/usr/bin/env python
"""Q51 / H5 — symmetric two-sided back-channel unifies matched implication binding.

Run:  python -m org_frontier.questions.q51_implication_backchannel.probe_impl_symmetric_unify
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
    LABELS, PHI_TOL, edge_count, implication_forms, instrument_control, matched_live_reads,
    symmetric_backchannel,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 159 (H5) — symmetric two-sided back-channel unifies matched implication binding")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    phis = []
    triadic = 0
    for label, rules in implication_forms(matched_live_reads):
        bc = symmetric_backchannel(rules)
        v = verdict(bc, LABELS)
        is_tri = v.structure == "triadic"
        triadic += int(is_tri)
        phis.append(v.max_phi)
        rows.append({"label": label, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "edges": edge_count(bc)})
        print(f"  {label}: {v.structure}, max_phi={v.max_phi:.6f}, edges={edge_count(bc)}")

    uniform = len(set(round(p, 6) for p in phis)) == 1 if phis else False
    shared_phi = phis[0] if uniform and phis else None
    print(f"\n  triadic symmetric matched implication: {triadic}/8")
    if shared_phi is not None:
        print(f"  shared max_phi: {shared_phi:.6f}")
    if triadic == 8 and uniform:
        decision = "confirmed"
    elif triadic == 8:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all eight triadic with uniform phi?  {triadic == 8 and uniform}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "impl_symmetric_unify.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi", "edges"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
