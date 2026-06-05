#!/usr/bin/env python
"""Q45 / H5 — global 4-edge triadic maximum is conjunctive-only.

Run:  python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_global_floor
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q45_edge_floor_uniqueness.floor_utils import (  # noqa: E402
    LABELS, edge_count, enumerate_all_wirings, instrument_control, is_conjunctive_strict,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
FLOOR = 4
MAX_PHI = 2.0


def main():
    print("PROBE 149 (H5) — global 4-edge triadic maximum is conjunctive-only")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    hits = []
    violations = []
    n_triadic_4edge = 0
    for idx, rules in enumerate_all_wirings():
        v = verdict(rules, LABELS)
        ec = edge_count(rules)
        if v.structure != "triadic" or ec != FLOOR:
            continue
        n_triadic_4edge += 1
        if v.max_phi >= MAX_PHI - 1e-9:
            conj = is_conjunctive_strict(rules)
            hits.append({"idx": idx, "max_phi": f"{v.max_phi:.6f}",
                         "conjunctive_strict": conj})
            if not conj:
                violations.append(idx)

    print(f"\n  triadic forms at exactly {FLOOR} edges (4096 space): {n_triadic_4edge}")
    print(f"  triadic at {FLOOR} edges with max Phi={MAX_PHI}: {len(hits)}")
    print(f"  non-conjunctive-strict counterexamples: {len(violations)}")
    for idx in violations[:5]:
        print(f"      wiring index {idx}")

    decision = "confirmed" if not violations else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    every max-Phi 4-edge form is conjunctive strict?  {not violations}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "global_floor.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["idx", "max_phi", "conjunctive_strict"])
        w.writeheader()
        w.writerows(hits)
    print(f"\n  wrote results/global_floor.csv ({len(hits)} max-Phi rows)")
    return decision


if __name__ == "__main__":
    main()
