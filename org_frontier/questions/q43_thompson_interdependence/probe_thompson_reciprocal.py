"""Q43 H4 — Reciprocal requires a feedback cycle, not bidirectional labels.

H4: Reciprocal reads triadic only when the coupling closes an actual feedback cycle through both
parties, not merely when each party is nominally labeled as influencing the other; a
bidirectional-but-acyclic variant reads dyadic.

Form / ensemble (n=3, AND family, labels (W,S,C)):
  Cyclic reciprocal (return arrow closes the loop):
      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]   (#5/#39)
  Bidirectionally-labeled but acyclic (return arrow drawn, C'=C does not close a cycle):
      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]   (#5/#39)

Measure: verdict().structure and .max_phi for both; major_complex() and .mip_partition for the
cyclic form. Both forms carry two-way arrows by label and differ only in whether the return edge
closes a cycle (read off cm_from_rules); same node count, same AND family.

Decision rule (fixed before run): H4 confirmed if cyclic reads triadic and acyclic-bidirectional
reads dyadic; refuted if both triadic (labels alone suffice) or both dyadic.
Predicted: cyclic triadic Φ=2.0, worker on the weakest seam, MIP {W,SC}, major complex {W,S,C};
bidirectional-acyclic dyadic Φ=0.

Run:
  ~/iit-playground/venv-4.0/bin/python \
      org_frontier/questions/q43_thompson_interdependence/probe_thompson_reciprocal.py
"""

import csv
import os
import sys

# Repo root onto sys.path so org_frontier.* and proxy_audit.* import as a direct script too.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.probes.lib import verdict, major_complex

LABELS = ("W", "S", "C")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

# Instrument control: the strict-mediation / pass-through propagating chain (#57).
INSTRUMENT_CONTROL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# H4 forms.
CYCLIC_RECIPROCAL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]      # #5/#39
ACYCLIC_BIDIRECTIONAL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]  # #5/#39


def _cm_str(rules):
    cm = cm_from_rules(rules)
    return "; ".join(
        f"{LABELS[i]}->{LABELS[j]}"
        for i in range(cm.shape[0])
        for j in range(cm.shape[1])
        if cm[i, j]
    )


def main():
    print("Q43 H4 — reciprocal requires a feedback cycle, not bidirectional labels")
    print("=" * 78)

    # ---- Instrument control (run first; abort on failure) ----
    ctrl = verdict(INSTRUMENT_CONTROL, LABELS)
    print("Instrument control (strict-mediation triad #57):")
    print(f"  structure={ctrl.structure}  max_phi={ctrl.max_phi:.6f}  MIP={ctrl.mip_partition}")
    ok = (ctrl.structure == "triadic"
          and abs(ctrl.max_phi - 2.0) < 1e-6
          and "{W,SC}" in ctrl.mip_partition.replace(" ", ""))
    assert ok, (
        f"Instrument control FAILED: expected triadic Φ=2.0 MIP 2 parts: {{W,SC}}, "
        f"got {ctrl.structure} Φ={ctrl.max_phi:.6f} MIP {ctrl.mip_partition}. Halting."
    )
    print("  instrument control PASSED (triadic, Φ=2.0, MIP {W,SC})")
    print("-" * 78)

    # ---- H4 forms ----
    cyc = verdict(CYCLIC_RECIPROCAL, LABELS)
    acy = verdict(ACYCLIC_BIDIRECTIONAL, LABELS)
    cyc_core, cyc_core_phi = major_complex(CYCLIC_RECIPROCAL, LABELS)

    print("Cyclic reciprocal  [x[1], x[0]&x[2], x[1]]  (return arrow closes the loop):")
    print(f"  edges: {_cm_str(CYCLIC_RECIPROCAL)}")
    print(f"  structure={cyc.structure}  max_phi={cyc.max_phi:.6f}")
    print(f"  mip_partition={cyc.mip_partition}  max_phi_state={cyc.mip_state}")
    print(f"  major_complex core={cyc_core}  phi={cyc_core_phi:.6f}")
    print()
    print("Bidirectional-acyclic  [x[1], x[0]&x[2], x[2]]  (return arrow drawn, no cycle):")
    print(f"  edges: {_cm_str(ACYCLIC_BIDIRECTIONAL)}")
    print(f"  structure={acy.structure}  max_phi={acy.max_phi:.6f}")
    print(f"  mip_partition={acy.mip_partition}")
    print("-" * 78)

    # ---- Decision rule ----
    cyc_triadic = cyc.structure == "triadic"
    acy_dyadic = acy.structure == "dyadic"
    if cyc_triadic and acy_dyadic:
        v = "confirmed"
    elif cyc.structure == "triadic" and acy.structure == "triadic":
        v = "refuted (both triadic — labels alone suffice)"
    elif cyc.structure == "dyadic" and acy.structure == "dyadic":
        v = "refuted (both dyadic)"
    else:
        v = "refuted (other)"
    print(f"VERDICT: H4 {v}")
    print(f"  cyclic={cyc.structure} Φ={cyc.max_phi:.3f} | "
          f"acyclic-bidirectional={acy.structure} Φ={acy.max_phi:.3f}")

    # ---- CSV ----
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h4_reciprocal.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "rules", "edges", "structure", "max_phi",
                    "mip_partition", "major_complex_core", "major_complex_phi"])
        w.writerow(["instrument_control", "[x[1], x[0]&x[2], x[1]]",
                    _cm_str(INSTRUMENT_CONTROL), ctrl.structure, f"{ctrl.max_phi:.6f}",
                    ctrl.mip_partition, "", ""])
        w.writerow(["cyclic_reciprocal", "[x[1], x[0]&x[2], x[1]]",
                    _cm_str(CYCLIC_RECIPROCAL), cyc.structure, f"{cyc.max_phi:.6f}",
                    cyc.mip_partition, str(cyc_core), f"{cyc_core_phi:.6f}"])
        w.writerow(["acyclic_bidirectional", "[x[1], x[0]&x[2], x[2]]",
                    _cm_str(ACYCLIC_BIDIRECTIONAL), acy.structure, f"{acy.max_phi:.6f}",
                    acy.mip_partition, "", ""])
    print(f"  wrote {csv_path}")


if __name__ == "__main__":
    main()
