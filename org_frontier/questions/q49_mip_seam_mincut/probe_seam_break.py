#!/usr/bin/env python
"""Q49 / H3 — a one-sided back-channel breaks the seam tie.

Form: worker-side back-channel W'=S&C, S'=W&C, C'=S (rules [x[1]&x[2], x[0]&x[2], x[1]]) — the canonical
triad plus a direct C->W read (#24).
Measure: verdict and max_phi (must stay triadic); the seam set; the count of severed singletons.

Instrument control (run first): the canonical triad reads triadic, Φ=2.0, MIP '2 parts: {W,SC}',
seam set {W,C} (the symmetric baseline from H1).

Decision rule (fixed before run): H3 confirmed if the back-channel form is triadic (max_phi >= 2.0-1e-9)
and its seam set is a single party; refuted if the seam set stays {W,C}; void if the form is dyadic.

Run:  python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_break
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
BACKCHANNEL_W = [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1]]
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6, "control failed"
    assert v.mip_partition == "2 parts: {W,SC}", f"control MIP {v.mip_partition!r}"
    assert seam_set(CANON, LABELS) == {"W", "C"}, "control seam set != {W,C}"
    return v


def main():
    print("PROBE 142 (H3) — a one-sided back-channel breaks the seam tie")
    print("=" * 64)
    instrument_control()
    print("[instrument control] canonical triad: triadic, Φ=2.0, seam {C, W}  -> PASS")

    v, sia, lines = mip_ties(BACKCHANNEL_W, LABELS)
    print(f"\n  back-channel W'=S&C (adds C->W):  structure={v.structure}, max_phi={v.max_phi:.6f}")
    if v.structure != "triadic":
        print("  form is dyadic — premise fails, test VOID")
        return "void"
    seam = seam_set(BACKCHANNEL_W, LABELS)
    print(f"  max-Φ state = {v.mip_state}, system Φ = {float(sia.phi):.6f}")
    print(f"  tie set ({len(lines)}):")
    for ln in lines:
        print(f"      {ln}")
    print(f"  seam set: {sorted(seam)}  (canonical was {{C, W}})")

    triadic = v.max_phi >= 2.0 - 1e-9
    broken = len(seam) == 1
    decision = "confirmed" if (triadic and broken) else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    stays triadic (Φ>=2.0)?        {triadic}")
    print(f"    seam tie broken to one party?  {broken}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_break.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "structure", "max_phi", "seam_set", "h3"])
        w.writerow(["backchannel_W", v.structure, f"{v.max_phi:.6f}", "|".join(sorted(seam)), decision])
    return decision


if __name__ == "__main__":
    main()
