"""Probe Q117 (H1-H4) — a Φ-free necessary-and-sufficient test for triadicity.

Runs three predicates across the 256-form strict-mediation family: the exact-Φ oracle (ground truth), the
topology-only feedback cycle, and the cycle plus a logical composition condition. Reads whether the cycle is
necessary, whether topology suffices, and whether the logical predicate closes the gap to zero error.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q117_phi_free_test.probe_phi_free_test
"""

import csv
import os

from org_frontier.questions.q117_phi_free_test import forms as F


def main():
    print("PROBE Q117 (H1-H4) — a Φ-free test for triadicity on the 256-form family")
    print("=" * 78)
    r = F.compare_family()
    cyc, full, cf = r["cycle"], r["full"], r["cycle_forms"]
    n_cycle = cf["triadic"] + cf["dyadic"]
    print(f"  forms: {r['n']}   triadic (exact Φ): {r['triadic']}   dyadic: {r['n'] - r['triadic']}")
    print(f"  cycle-only  vs oracle:  TP={cyc['tp']} FP={cyc['fp']} FN={cyc['fn']} TN={cyc['tn']}")
    print(f"  full Φ-free vs oracle:  TP={full['tp']} FP={full['fp']} FN={full['fn']} TN={full['tn']}")
    print(f"  full-cycle forms: {n_cycle}  ({cf['triadic']} triadic, {cf['dyadic']} dyadic, "
          f"same wiring)")

    h1 = cyc["fn"] == 0                                  # cycle necessary: no triadic form lacks it
    h2 = cyc["fp"] > 0                                   # cycle not sufficient: cyclic dyadic forms exist
    h3 = full["fp"] == 0 and full["fn"] == 0             # logical predicate exact
    h4 = cf["triadic"] > 0 and cf["dyadic"] > 0          # the split is within one wiring -> logic decides
    print("=" * 78)
    print(f"  H1 the feedback cycle is necessary (no triadic form lacks it):     {h1}")
    print(f"  H2 the feedback cycle is not sufficient (cyclic dyadic forms):     {h2} "
          f"({cyc['fp']} forms)")
    print(f"  H3 the cycle-plus-logic predicate matches the oracle exactly:      {h3} "
          f"({full['fp'] + full['fn']} errors)")
    print(f"  H4 forms of identical wiring split on the verdict (logic decides): {h4} "
          f"({cf['triadic']} vs {cf['dyadic']})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "phi_free_test.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["predicate", "tp", "fp", "fn", "tn", "errors"])
        for name, c in (("cycle_only", cyc), ("full_phi_free", full)):
            w.writerow([name, c["tp"], c["fp"], c["fn"], c["tn"], c["fp"] + c["fn"]])
        w.writerow(["full_cycle_forms_triadic", cf["triadic"], "", "", "", ""])
        w.writerow(["full_cycle_forms_dyadic", cf["dyadic"], "", "", "", ""])


if __name__ == "__main__":
    main()
