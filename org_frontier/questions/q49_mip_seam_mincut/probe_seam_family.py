#!/usr/bin/env python
"""Q49 / H2 — no triadic strict-mediation form has a worker-unique seam.

Ensemble: all 256 strict-mediation n=3 forms (corpus.population.enumerate_family), filtered to triadic.
Measure: per triadic form, the seam set; the indicator (W in seam) == (C in seam).

Instrument control (run first): the canonical triad reads triadic, max_phi=2.0, MIP '2 parts: {W,SC}'.

Decision rule (fixed before run): H2 confirmed if every triadic form has (W in seam) == (C in seam)
(zero forms sever W alone); refuted if at least one triadic form has W in the seam and C not.

Run:  python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_family
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.questions.q49_mip_seam_mincut.seam import seam_set, LABELS  # noqa: E402

CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6, "control failed"
    assert v.mip_partition == "2 parts: {W,SC}", f"control MIP {v.mip_partition!r}"
    return v


def main():
    print("PROBE 141 (H2) — no triadic strict-mediation form has a worker-unique seam")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, Φ={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    n_triadic = 0
    violations = []
    for label, rules in enumerate_family():
        v = verdict(rules, LABELS)
        if v.structure != "triadic":
            continue
        n_triadic += 1
        seam = seam_set(rules, LABELS)
        w_in, c_in = "W" in seam, "C" in seam
        symmetric = (w_in == c_in)
        rows.append({"label": label, "max_phi": f"{v.max_phi:.6f}",
                     "seam_set": "|".join(sorted(seam)), "wc_symmetric": symmetric})
        if not symmetric:
            violations.append((label, sorted(seam)))

    print(f"\n  triadic forms found: {n_triadic}  (corpus #33 reports 24)")
    print(f"  forms with W-in-seam == C-in-seam: {n_triadic - len(violations)}/{n_triadic}")
    print(f"  worker-unique-seam violations: {len(violations)}")
    for lab, seam in violations[:10]:
        print(f"      {lab}: seam {seam}")

    decision = "confirmed" if not violations else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    every triadic form W/C-symmetric in seam?  {not violations}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_family.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "max_phi", "seam_set", "wc_symmetric"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/seam_family.csv ({len(rows)} triadic rows)")
    return decision


if __name__ == "__main__":
    main()
