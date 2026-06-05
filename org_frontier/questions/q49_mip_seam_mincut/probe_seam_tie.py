#!/usr/bin/env python
"""Q49 / H1 — the canonical worker seam is a tie, not a unique fault line.

Form: the canonical strict-mediation triad W'=S, S'=W&C, C'=S (rules [x[1], x[0]&x[2], x[1]]).
Measure: the MIP tie set at the max-Φ state; the seam set (parties severed as a singleton by a tied
two-part partition).

Instrument control (run first): the same canonical triad must read triadic, max_phi=2.0, MIP
'2 parts: {W,SC}'. Abort if it fails.

Decision rule (fixed before run): H1 confirmed if the tie set contains both a {W,SC} and a {WS,C}
two-part partition (seam set superset of {W,C}) and not {S,WC}; refuted if {W,SC} is the unique MIP.

Run:  python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_tie
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q49_mip_seam_mincut.seam import mip_ties, seam_set, LABELS  # noqa: E402

CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r} != 'triadic'"
    assert abs(v.max_phi - 2.0) < 1e-6, f"control max_phi {v.max_phi} != 2.0"
    assert v.mip_partition == "2 parts: {W,SC}", f"control MIP {v.mip_partition!r}"
    return v


def main():
    print("PROBE 140 (H1) — the canonical worker seam is a tie")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: structure={ctrl.structure}, "
          f"max_phi={ctrl.max_phi:.6f}, MIP={ctrl.mip_partition!r}  -> PASS")

    v, sia, lines = mip_ties(CANON, LABELS)
    seam = seam_set(CANON, LABELS)
    print(f"\n  max-Φ state = {v.mip_state}, system Φ = {float(sia.phi):.6f}")
    print(f"  tie set ({len(lines)} partitions at Φ={float(sia.phi):.3f}):")
    for ln in lines:
        print(f"      {ln}")
    print(f"  seam set (singleton-severing two-part cuts): {sorted(seam)}")

    has_w = "W" in seam
    has_c = "C" in seam
    has_s = "S" in seam
    decision = "confirmed" if (has_w and has_c and not has_s) else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    {{W,SC}} tied (W in seam)?  {has_w}")
    print(f"    {{WS,C}} tied (C in seam)?  {has_c}")
    print(f"    {{S,WC}} in seam?           {has_s}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_tie.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "system_phi", "seam_set", "tie_lines", "h1"])
        w.writerow(["canonical_triad", f"{float(sia.phi):.6f}", "|".join(sorted(seam)),
                    " ; ".join(lines), decision])
    return decision


if __name__ == "__main__":
    main()
