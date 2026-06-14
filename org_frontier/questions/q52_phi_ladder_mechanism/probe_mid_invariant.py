#!/usr/bin/env python
"""Q52 / H3 — mid rung invariant across party-read pairing for s in {4,11}.

Run:  python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_mid_invariant
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    IMPLICATION_INDICES, complementary_reads, matched_live_reads, s_index, worker_backchannel,
)
from org_frontier.questions.q52_phi_ladder_mechanism.ladder_utils import (  # noqa: E402
    C_CENTRIC, LABELS, MID_PHI, PHI_TOL, instrument_control, ladder_rung,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def mid_commit_forms():
    for label, rules in enumerate_family():
        if s_index(label) not in C_CENTRIC:
            continue
        iw = int(label[1])
        ic = int(label.split("_C")[1])
        if matched_live_reads(iw, ic) or complementary_reads(iw, ic):
            pairing = "matched" if matched_live_reads(iw, ic) else "complementary"
            yield label, rules, pairing


def main():
    print("PROBE 162 (H3) — mid rung invariant across party-read pairing")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    at_mid = 0
    for label, rules, pairing in mid_commit_forms():
        bc = worker_backchannel(rules)
        v = verdict(bc, LABELS)
        mid_ok = v.structure == "triadic" and abs(v.max_phi - MID_PHI) < PHI_TOL
        at_mid += int(mid_ok)
        rows.append({
            "label": label, "pairing": pairing, "structure": v.structure,
            "max_phi": f"{v.max_phi:.6f}", "rung": ladder_rung(label, v.structure, v.max_phi),
            "at_mid": mid_ok,
        })
        print(f"  {label} ({pairing}): {v.structure}, max_phi={v.max_phi:.6f}")

    print(f"\n  s in {{4,11}} at mid rung: {at_mid}/8")
    if at_mid == 8:
        decision = "confirmed"
    elif at_mid >= 1:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    eight of eight at mid?  {at_mid == 8}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "mid_invariant.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
