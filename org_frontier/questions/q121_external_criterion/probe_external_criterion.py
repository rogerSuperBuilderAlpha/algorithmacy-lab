"""Probe Q121 (H1-H4) — an external criterion for the verdict (answering the critical review's T1).

Tests two non-Φ criteria, observational (total correlation of the next-state joint) and interventional
(Boolean-network damage spreading), against the exact verdict, on the full 256-form family and on the 40
full-cycle forms where Q117 showed topology and logic split.

Run:  ~/iit-playground/venv-4.0/bin/python -m \
      org_frontier.questions.q121_external_criterion.probe_external_criterion
"""

from org_frontier.questions.q121_external_criterion import forms as F

import csv
import os


def main():
    print("PROBE Q121 (H1-H4) — an external criterion for the verdict")
    print("=" * 78)
    r = F.evaluate()
    print(f"  family: {r['n']} forms ({r['triadic']} triadic); "
          f"hard subset: {r['n_hard']} full-cycle forms ({r['triadic_hard']} triadic)")
    print(f"  FULL family AUC:  cycle(topology)={r['auc_cycle_full']:.3f}  "
          f"observational={r['auc_obs_full']:.3f}  interventional={r['auc_inter_full']:.3f}")
    print(f"  HARD subset AUC:  observational={r['auc_obs_hard']:.3f}  "
          f"interventional={r['auc_inter_hard']:.3f}")

    h1 = r["auc_cycle_full"] > 0.9                        # the full-family bar is trivial (topology clears it)
    h2 = r["auc_obs_hard"] <= 0.6                         # observation fails on the hard cases
    h3 = r["auc_inter_hard"] >= 0.9                       # intervention separates the hard cases
    h4 = r["auc_inter_full"] < 0.999                      # intervention is not a standalone full classifier
    print("=" * 78)
    print(f"  H1 the full-family AUC bar is trivial (cycle alone clears 0.9):   {h1} "
          f"({r['auc_cycle_full']:.3f})")
    print(f"  H2 an observational criterion fails on the hard cases (<=0.6):    {h2} "
          f"({r['auc_obs_hard']:.3f})")
    print(f"  H3 an interventional criterion separates the hard cases (>=0.9):  {h3} "
          f"({r['auc_inter_hard']:.3f})")
    print(f"  H4 the interventional criterion is not a standalone classifier:   {h4} "
          f"(full AUC {r['auc_inter_full']:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "external_criterion.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["scope", "criterion", "auc"])
        w.writerow(["full", "cycle_topology", round(r["auc_cycle_full"], 4)])
        w.writerow(["full", "observational_total_correlation", round(r["auc_obs_full"], 4)])
        w.writerow(["full", "interventional_damage_spreading", round(r["auc_inter_full"], 4)])
        w.writerow(["hard_full_cycle", "observational_total_correlation", round(r["auc_obs_hard"], 4)])
        w.writerow(["hard_full_cycle", "interventional_damage_spreading", round(r["auc_inter_hard"], 4)])


if __name__ == "__main__":
    main()
