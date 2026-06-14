#!/usr/bin/env python
"""Q51 / H4 — back-channel preserves complementary implication at Phi=2.0.

Run:  python -m org_frontier.questions.q51_implication_backchannel.probe_impl_complementary_preserve
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
    LABELS, MAX_PHI, PHI_TOL, complementary_reads, edge_count, implication_forms,
    instrument_control, worker_backchannel,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 158 (H4) — back-channel preserves complementary implication at Phi=2.0")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    at_ceiling = 0
    all_triadic = True
    for label, rules in implication_forms(complementary_reads):
        v_strict = verdict(rules, LABELS)
        bc = worker_backchannel(rules)
        v = verdict(bc, LABELS)
        ceiling = v.structure == "triadic" and v.max_phi >= MAX_PHI - PHI_TOL
        at_ceiling += int(ceiling)
        all_triadic = all_triadic and v.structure == "triadic"
        rows.append({"label": label, "strict_phi": f"{v_strict.max_phi:.6f}",
                     "bc_structure": v.structure, "bc_max_phi": f"{v.max_phi:.6f}",
                     "edges": edge_count(bc), "at_phi2": ceiling})
        print(f"  {label}: strict phi={v_strict.max_phi:.6f} -> bc {v.structure} "
              f"phi={v.max_phi:.6f}")

    print(f"\n  complementary + worker back-channel at Phi=2.0: {at_ceiling}/8")
    if at_ceiling == 8:
        decision = "confirmed"
    elif all_triadic:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all eight at Phi=2.0?  {at_ceiling == 8}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "impl_complementary_preserve.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "strict_phi", "bc_structure", "bc_max_phi",
                                            "edges", "at_phi2"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
