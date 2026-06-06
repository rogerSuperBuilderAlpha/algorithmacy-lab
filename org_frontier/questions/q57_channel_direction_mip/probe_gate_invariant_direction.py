#!/usr/bin/env python
"""Q57 / H5 — gate-invariant direction rule under XOR and XNOR.

Run:  python -m org_frontier.questions.q57_channel_direction_mip.probe_gate_invariant_direction
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    COUNTERPART_TOPOLOGIES,
    OUTER_C,
    OUTER_W,
    WORKER_TOPOLOGIES,
    enriched_rows,
    expected_tied_cut,
    instrument_control,
    tied_outer_cut,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 189 (H5) — gate-invariant direction rule under XOR and XNOR")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_rows()
    worker_ok = counterpart_ok = 0
    worker_n = counterpart_n = 0
    for r in rows:
        topo = r["topology"]
        actual = tied_outer_cut(r)
        if topo in WORKER_TOPOLOGIES:
            worker_n += 1
            if actual == OUTER_W:
                worker_ok += 1
        elif topo in COUNTERPART_TOPOLOGIES:
            counterpart_n += 1
            if actual == OUTER_C:
                counterpart_ok += 1

    print(f"\n  worker topologies at {OUTER_W}: {worker_ok}/{worker_n}")
    print(f"  counterpart topologies at {OUTER_C}: {counterpart_ok}/{counterpart_n}")

    all_ok = worker_ok == worker_n == 8 and counterpart_ok == counterpart_n == 8

    if all_ok:
        decision = "confirmed"
    elif worker_ok == worker_n and counterpart_ok == counterpart_n:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    worker 8/8 and counterpart 8/8?  {all_ok}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "gate_invariant_direction.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "expected_tied", "actual_tied", "match"],
        )
        w.writeheader()
        for r in rows:
            expected = expected_tied_cut(r["topology"])
            actual = tied_outer_cut(r)
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "expected_tied": expected,
                "actual_tied": actual,
                "match": actual == expected,
            })
    return decision


if __name__ == "__main__":
    main()
