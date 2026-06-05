#!/usr/bin/env python
"""Q54 / H1 — channel-gate bijectivity separates Phi=2.0 from monotone caps.

Run:  python -m org_frontier.questions.q54_xor_parity_mechanism.probe_gate_bijectivity
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
    MAX_PHI,
    PHI_TOL,
    full_panel,
    gate_bijective_in_coupled_bit,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 170 (H1) — channel-gate bijectivity separates Phi=2.0 from monotone caps")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    for op in ("and", "or", "xor", "xnor"):
        print(f"  gate {op} bijective in coupled bit: {gate_bijective_in_coupled_bit(op)}")

    rows = full_panel()
    phi2_rows = [r for r in rows if r["at_ceiling"]]
    non_bijective_phi2 = [r for r in phi2_rows if not r["channel_bijective"]]
    bijective_below = [
        r for r in rows
        if r["channel_bijective"] and r["max_phi"] < MAX_PHI - PHI_TOL
    ]

    print(f"\n  panel pairs: {len(rows)}")
    print(f"  pairs at Phi=2.0: {len(phi2_rows)}")
    print(f"  Phi=2.0 with non-bijective channel: {len(non_bijective_phi2)}")
    print(f"  bijective channel below ceiling: {len(bijective_below)}")

    all_phi2_bijective = len(non_bijective_phi2) == 0
    no_non_bijective_at_ceiling = all(
        not r["at_ceiling"] for r in rows if not r["channel_bijective"]
    )

    if all_phi2_bijective and no_non_bijective_at_ceiling:
        decision = "confirmed"
    elif all_phi2_bijective:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all Phi=2.0 pairs bijective?  {all_phi2_bijective}")
    print(f"    zero non-bijective at ceiling?  {no_non_bijective_at_ceiling}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "gate_bijectivity.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "s_index", "topology", "structure", "max_phi",
                        "at_ceiling", "channel_bijective", "tpm_permutation"],
        )
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["max_phi"] = f"{out['max_phi']:.6f}"
            w.writerow(out)
    return decision


if __name__ == "__main__":
    main()
