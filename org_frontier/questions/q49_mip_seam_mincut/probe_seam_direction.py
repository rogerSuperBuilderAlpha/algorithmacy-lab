#!/usr/bin/env python
"""Q49 / H4 — the broken seam follows the read direction.

Panel (n=3, all built on the canonical triad S'=W&C with both parties reading S):
  worker-side channel     W'=S&C  -> [x[1]&x[2], x[0]&x[2], x[1]]      (adds C->W)
  counterpart-side channel C'=S&W -> [x[1], x[0]&x[2], x[1]&x[0]]      (adds W->C)
  symmetric two-sided      both    -> [x[1]&x[2], x[0]&x[2], x[1]&x[0]]
Measure: verdict; seam set per form.

Instrument control (run first): canonical triad triadic, Φ=2.0, seam {W,C}.

Decision rule (fixed before run): H4 confirmed if worker-side seam == {C}, counterpart-side seam == {W},
symmetric seam == {W,C}; refuted otherwise.

Run:  python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_direction
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q49_mip_seam_mincut.seam import seam_set, LABELS  # noqa: E402

CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
PANEL = {
    "worker_side  (W'=S&C, adds C->W)": [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1]],
    "counterpart  (C'=S&W, adds W->C)": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[0]],
    "symmetric    (both channels)    ": [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1] & x[0]],
}
EXPECT = {"worker_side  (W'=S&C, adds C->W)": {"C"},
          "counterpart  (C'=S&W, adds W->C)": {"W"},
          "symmetric    (both channels)    ": {"W", "C"}}
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6, "control failed"
    assert seam_set(CANON, LABELS) == {"W", "C"}, "control seam set != {W,C}"
    return v


def main():
    print("PROBE 143 (H4) — the broken seam follows the read direction")
    print("=" * 64)
    instrument_control()
    print("[instrument control] canonical triad: triadic, Φ=2.0, seam {C, W}  -> PASS")

    rows = []
    all_match = True
    for name, rules in PANEL.items():
        v = verdict(rules, LABELS)
        seam = seam_set(rules, LABELS) if v.structure == "triadic" else set()
        match = seam == EXPECT[name]
        all_match = all_match and match
        rows.append({"form": name.strip(), "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
                     "seam_set": "|".join(sorted(seam)), "expected": "|".join(sorted(EXPECT[name])),
                     "match": match})
        print(f"\n  {name}")
        print(f"      structure={v.structure}, Φ={v.max_phi:.6f}, seam={sorted(seam)}, "
              f"expected={sorted(EXPECT[name])}, match={match}")

    decision = "confirmed" if all_match else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all three panel forms match the read-direction prediction?  {all_match}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_direction.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["form", "structure", "max_phi", "seam_set", "expected", "match"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
