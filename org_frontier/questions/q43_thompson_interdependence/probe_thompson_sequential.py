"""Q43 / H3 — "sequential" is verdict-ambiguous; the split turns on the return path.

Two sequential encodings at n=3, AND family, differing only in the return edge:

  Propagating chain (#57): the worker's effect is read at the far end.
      W' = S,  S' = W & C,  C' = S
      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
  S' = W & C reads C back into the chain (a return edge closes the loop).

  Acyclic source->sink hand-off (#39): each stage only sources the next, nothing returns.
      W' = W,  S' = W & C,  C' = C
      [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]]
  Stages carry their own prior state forward with no return edge.

Decision rule (fixed before run): H3 is confirmed if the two encodings split —
propagating chain triadic, acyclic hand-off dyadic. H3 is refuted if both give the same
verdict. Predicted: propagating chain triadic at max_phi = 2.0 with a balanced near-middle
MIP {W,SC}; acyclic hand-off dyadic (max_phi = 0).

Instrument control (run first): the pass-through mediator chain is the propagating form
itself; it must reproduce triadic at max_phi = 2.0 with MIP 2 parts {W,SC} before any
comparison verdict is trusted. Abort if it fails.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q43_thompson_interdependence/probe_thompson_sequential.py
"""

import csv
import os
import sys

# Put the repo root on sys.path so this also runs as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi

from org_frontier.classifier.classifier import (
    classify_rules,
    cm_from_rules,
    PHI_EPS,
)
from org_frontier.probes.lib import verdict

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("W", "S", "C")

# Propagating chain (#57) — also the instrument control / strict-mediation triad.
PROPAGATING = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
# Acyclic source->sink hand-off (#39).
HANDOFF = [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]]

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    # --- Instrument control: the propagating chain must read triadic Φ=2.0, MIP {W,SC}. ---
    ctrl = verdict(PROPAGATING, LABELS)
    print("Instrument control (pass-through mediator chain #57):")
    print(f"  structure = {ctrl.structure}")
    print(f"  max_phi   = {ctrl.max_phi:.6f}")
    print(f"  mip       = {ctrl.mip_partition}")
    ctrl_ok = (
        ctrl.structure == "triadic"
        and abs(ctrl.max_phi - 2.0) < 1e-6
        and "W" in ctrl.mip_partition
        and ("S" in ctrl.mip_partition and "C" in ctrl.mip_partition)
    )
    if not ctrl_ok:
        print("INSTRUMENT CONTROL FAILED — aborting; do not trust comparison verdicts.")
        sys.exit(1)
    print("  -> instrument control PASSED (triadic, Φ=2.0, MIP separates W from SC).\n")

    # --- Test: the two sequential encodings. ---
    prop = verdict(PROPAGATING, LABELS)  # same form as the control
    hand = verdict(HANDOFF, LABELS)

    print("Propagating chain (#57)  W'=S, S'=W&C, C'=S:")
    print(f"  structure = {prop.structure}")
    print(f"  max_phi   = {prop.max_phi:.6f}")
    print(f"  mip       = {prop.mip_partition}")
    print(f"  cm =\n{cm_from_rules(PROPAGATING)}")

    print("\nAcyclic source->sink hand-off (#39)  W'=W, S'=W&C, C'=C:")
    print(f"  structure = {hand.structure}")
    print(f"  max_phi   = {hand.max_phi:.6f}")
    print(f"  mip       = {hand.mip_partition}")
    print(f"  cm =\n{cm_from_rules(HANDOFF)}")

    # --- Decision rule (fixed before run). ---
    split = (prop.structure == "triadic") and (hand.structure == "dyadic")
    same = prop.structure == hand.structure
    if split:
        verdict_label = "confirmed"
    elif same:
        verdict_label = "refuted"
    else:
        verdict_label = "partial"
    print(f"\nPHI_EPS = {PHI_EPS}")
    print(f"H3 verdict: {verdict_label.upper()}")
    print(
        f"  propagating={prop.structure}/{prop.max_phi:.4f}  "
        f"handoff={hand.structure}/{hand.max_phi:.4f}"
    )

    # --- Write CSV. ---
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h3_sequential.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["form", "rules", "structure", "max_phi", "mip_partition"])
        w.writerow([
            "propagating_chain_#57",
            "W'=S, S'=W&C, C'=S",
            prop.structure,
            f"{prop.max_phi:.6f}",
            prop.mip_partition,
        ])
        w.writerow([
            "acyclic_handoff_#39",
            "W'=W, S'=W&C, C'=C",
            hand.structure,
            f"{hand.max_phi:.6f}",
            hand.mip_partition,
        ])
    print(f"\nWrote {csv_path}")
    return verdict_label


if __name__ == "__main__":
    main()
