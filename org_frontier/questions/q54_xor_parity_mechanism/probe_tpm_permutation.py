#!/usr/bin/env python
"""Q54 / H2 — global TPM permutation accompanies Phi=2.0 restoration.

Run:  python -m org_frontier.questions.q54_xor_parity_mechanism.probe_tpm_permutation
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q54_xor_parity_mechanism.mechanism_utils import (  # noqa: E402
    LABELS,
    apply_any_topology,
    at_ceiling,
    instrument_control,
    matched_implication_panel,
    tpm_is_permutation,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 171 (H2) — global TPM permutation accompanies Phi=2.0 restoration")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    phi2_non_perm = 0
    and_perm = 0
    for label, rules in matched_implication_panel():
        for topo in ("symmetric_xor", "worker_xor", "counterpart_xor", "symmetric_xnor"):
            bc = apply_any_topology(rules, topo)
            v = verdict(bc, LABELS)
            perm = tpm_is_permutation(bc)
            if at_ceiling(v) and not perm:
                phi2_non_perm += 1
            if topo == "symmetric_and":
                pass
            rows.append({
                "label": label, "topology": topo, "structure": v.structure,
                "max_phi": v.max_phi, "at_ceiling": at_ceiling(v), "tpm_permutation": perm,
            })
        bc_and = apply_any_topology(rules, "symmetric_and")
        v_and = verdict(bc_and, LABELS)
        perm_and = tpm_is_permutation(bc_and)
        if perm_and:
            and_perm += 1
        rows.append({
            "label": label, "topology": "symmetric_and", "structure": v_and.structure,
            "max_phi": v_and.max_phi, "at_ceiling": at_ceiling(v_and), "tpm_permutation": perm_and,
        })

    phi2_rows = [r for r in rows if r["at_ceiling"]]
    phi2_all_perm = all(r["tpm_permutation"] for r in phi2_rows)

    print(f"\n  Phi=2.0 pairs checked: {len(phi2_rows)}")
    print(f"  Phi=2.0 non-permutation TPM: {phi2_non_perm}")
    print(f"  symmetric-AND permutation TPM: {and_perm}/8")

    if phi2_all_perm and and_perm == 0:
        decision = "confirmed"
    elif phi2_all_perm:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all Phi=2.0 pairs permutation TPM?  {phi2_all_perm}")
    print(f"    symmetric-AND permutation count:  {and_perm}/8")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "tpm_permutation.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "structure", "max_phi", "at_ceiling", "tpm_permutation"],
        )
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["max_phi"] = f"{out['max_phi']:.6f}"
            w.writerow(out)
    return decision


if __name__ == "__main__":
    main()
