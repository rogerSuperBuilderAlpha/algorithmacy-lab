#!/usr/bin/env python
"""Q54 / H4 — one-sided Phi=2.0 requires commit-topology alignment.

Run:  python -m org_frontier.questions.q54_xor_parity_mechanism.probe_commit_alignment
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q54_xor_parity_mechanism.mechanism_utils import (  # noqa: E402
    C_CENTRIC,
    LABELS,
    MAX_PHI,
    PHI_TOL,
    W_CENTRIC,
    aligned_one_sided_xor,
    apply_any_topology,
    at_ceiling,
    instrument_control,
    matched_implication_panel,
    s_index,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 173 (H4) — one-sided Phi=2.0 requires commit-topology alignment")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    misalignments = 0
    symmetric_at_ceiling = 0
    worker_ceiling = 0
    counterpart_ceiling = 0

    for label, rules in matched_implication_panel():
        s = s_index(label)
        for topo in ("worker_xor", "counterpart_xor", "symmetric_xor"):
            bc = apply_any_topology(rules, topo)
            v = verdict(bc, LABELS)
            ceiling = at_ceiling(v)
            aligned = aligned_one_sided_xor(label, topo, ceiling)
            if ceiling and not aligned:
                misalignments += 1
            if topo == "worker_xor" and ceiling:
                worker_ceiling += 1
            if topo == "counterpart_xor" and ceiling:
                counterpart_ceiling += 1
            if topo == "symmetric_xor" and ceiling:
                symmetric_at_ceiling += 1
            rows.append({
                "label": label, "s_index": s, "topology": topo,
                "commit_class": "w_centric" if s in W_CENTRIC else "c_centric",
                "structure": v.structure, "max_phi": v.max_phi,
                "at_ceiling": ceiling, "aligned": aligned,
            })
            print(f"  {label} + {topo}: max_phi={v.max_phi:.6f} ceiling={ceiling} aligned={aligned}")

    print(f"\n  misaligned one-sided Phi=2.0 hits: {misalignments}")
    print(f"  worker_xor at ceiling: {worker_ceiling}/8 (expected C-centric {len(C_CENTRIC)} forms)")
    print(f"  counterpart_xor at ceiling: {counterpart_ceiling}/8 (expected W-centric {len(W_CENTRIC)} forms)")
    print(f"  symmetric_xor at ceiling: {symmetric_at_ceiling}/8")

    if misalignments == 0 and symmetric_at_ceiling == 8:
        decision = "confirmed"
    elif misalignments == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    misalignments:  {misalignments}")
    print(f"    symmetric_xor at ceiling:  {symmetric_at_ceiling}/8")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "commit_alignment.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "s_index", "topology", "commit_class", "structure",
                        "max_phi", "at_ceiling", "aligned"],
        )
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["max_phi"] = f"{out['max_phi']:.6f}"
            w.writerow(out)
    return decision


if __name__ == "__main__":
    main()
