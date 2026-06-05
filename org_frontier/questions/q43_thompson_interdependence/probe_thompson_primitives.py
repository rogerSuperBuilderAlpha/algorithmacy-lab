#!/usr/bin/env python
"""Q43 H5 — only reciprocal is type-robustly triadic; pooled/sequential are encoding artifacts.

Reads the full matched 2x3 panel (pooled / sequential / reciprocal, two encodings each,
all n=3, AND family) as a single table. For each form we code two structural primitives:

  * joint determination present: some node's rule is an AND over >=2 distinct parties
    (read off the rule body, confirmed against cm_from_rules: that node has >=2 in-edges
    and behaves as a conjunction);
  * feedback cycle present: the connectivity matrix from cm_from_rules contains a directed
    cycle through >=2 parties.

We then check two functional-dependence claims:
  (a) verdict is NOT a function of Thompson type (some type maps to both verdicts);
  (b) verdict IS a function of the primitive pair (no two forms share a pair yet differ).

Decision rule (fixed before run): H5 confirmed iff BOTH pooled spans dyadic<->triadic AND
sequential spans dyadic<->triadic (Thompson type not single-valued), AND every form with
joint determination or a cycle reads triadic while every form with neither reads dyadic.
Refuted if Thompson type predicts verdict cleanly, or if two forms with the same primitive
pair disagree.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q43_thompson_interdependence/probe_thompson_primitives.py
"""

import csv
import os
import sys

# Put the repo root on sys.path so this runs as a direct script and via -m.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules  # noqa: E402
from org_frontier.probes.lib import verdict  # noqa: E402

LABELS = ("W", "S", "C")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

# --------------------------------------------------------------------------------------
# The matched 2x3 panel (rules + a structured description for primitive coding).
# Each entry carries an explicit, human-auditable list of which inputs each node's rule
# reads and whether that node combines them with AND, so the primitive coding is read off
# the rule *body*, then cross-checked against cm_from_rules numerically.
# --------------------------------------------------------------------------------------

PANEL = [
    {
        "type": "pooled",
        "encoding": "independent-contribution",
        "rules": [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
        # per-party channels through the shared node; no node ANDs >=2 parties
        "and_nodes": [],  # (node_index, [input parties]) for AND-over->=2 nodes
    },
    {
        "type": "pooled",
        "encoding": "all-required",
        # pool(3): S' = AND of the two non-S parties; each non-S party' = S
        "rules": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "and_nodes": [(1, [0, 2])],
    },
    {
        "type": "sequential",
        "encoding": "propagating-chain",
        "rules": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "and_nodes": [(1, [0, 2])],
    },
    {
        "type": "sequential",
        "encoding": "acyclic-handoff",
        "rules": [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]],
        "and_nodes": [(1, [0, 2])],
    },
    {
        "type": "reciprocal",
        "encoding": "cyclic",
        "rules": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "and_nodes": [(1, [0, 2])],
    },
    {
        "type": "reciprocal",
        "encoding": "bidirectional-acyclic",
        "rules": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],
        "and_nodes": [(1, [0, 2])],
    },
]

# Instrument control: the strict-mediation / pass-through triad (#57).
CONTROL_RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
# Instrument control #2 named in the spec: a pass-through chain n=3 reads triadic Phi=2.0.
# The strict-mediation triad above IS that established triad; we assert it directly.


# --------------------------------------------------------------------------------------
# Primitive coding
# --------------------------------------------------------------------------------------

def has_joint_determination(rules, and_nodes):
    """True iff some node's rule is an AND over >=2 distinct parties.

    Read off the declared rule body (and_nodes), then cross-checked numerically against
    cm_from_rules: each declared AND-node must have >=2 incoming edges, and the rule must
    actually behave as a conjunction (1 only when all declared inputs are 1).
    """
    cm = cm_from_rules(rules)
    n = len(rules)
    for j, inputs in and_nodes:
        in_edges = [i for i in range(n) if cm[i, j]]
        if len(set(inputs)) < 2:
            return False
        if not set(inputs).issubset(set(in_edges)):
            return False
        # confirm conjunction behaviour over the declared inputs
        for s in range(2 ** n):
            cur = tuple((s >> k) & 1 for k in range(n))
            expected = int(all(cur[i] for i in inputs))
            if int(rules[j](cur)) != expected:
                return False
    return bool(and_nodes)


def has_feedback_cycle(rules):
    """True iff cm_from_rules contains a directed cycle through >=2 distinct parties.

    Self-loops (cm[i,i]) are ignored; we require a cycle traversing >=2 nodes.
    """
    cm = cm_from_rules(rules)
    n = len(rules)
    # adjacency i -> j when node j depends on node i (cm[i, j] == 1), i != j
    adj = {i: [j for j in range(n) if i != j and cm[i, j]] for i in range(n)}

    def reaches(start, target, visited):
        for nxt in adj[start]:
            if nxt == target:
                return True
            if nxt not in visited:
                visited.add(nxt)
                if reaches(nxt, target, visited):
                    return True
        return False

    for i in range(n):
        # cycle of length >=2 through i: i can reach some j (j!=i) that returns to i
        for j in adj[i]:
            if reaches(j, i, {i, j}):
                return True
    return False


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # ---- Instrument control: must reproduce triadic at Phi=2.0, MIP {W,SC}. ----
    ctrl = verdict(CONTROL_RULES, LABELS)
    print("INSTRUMENT CONTROL (strict-mediation / pass-through triad #57):")
    print(f"  structure={ctrl.structure}  max_phi={ctrl.max_phi:.6f}  "
          f"mip={ctrl.mip_partition}")
    ok = (ctrl.structure == "triadic"
          and abs(ctrl.max_phi - 2.0) < 1e-6
          and "W,SC" in ctrl.mip_partition.replace(" ", ""))
    assert ok, (
        "Instrument control failed: expected triadic, Phi=2.0, MIP {W,SC}; "
        f"got structure={ctrl.structure}, max_phi={ctrl.max_phi}, "
        f"mip={ctrl.mip_partition}. Halting."
    )
    print("  control PASSED.\n")

    # ---- Run the panel. ----
    rows = []
    for form in PANEL:
        v = verdict(form["rules"], LABELS)
        jd = has_joint_determination(form["rules"], form["and_nodes"])
        fc = has_feedback_cycle(form["rules"])
        rows.append({
            "thompson_type": form["type"],
            "encoding": form["encoding"],
            "joint_determination": jd,
            "feedback_cycle": fc,
            "verdict": v.structure,
            "max_phi": round(v.max_phi, 6),
            "mip_partition": v.mip_partition,
        })

    # ---- Print the 2x3 table. ----
    print("PANEL (matched 2x3: node count=3, AND family fixed; Thompson label + primitives vary)")
    hdr = f"{'type':<11}{'encoding':<24}{'joint_det':<11}{'cycle':<8}{'verdict':<9}{'max_phi':<10}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['thompson_type']:<11}{r['encoding']:<24}"
              f"{str(r['joint_determination']):<11}{str(r['feedback_cycle']):<8}"
              f"{r['verdict']:<9}{r['max_phi']:<10}")
    print()

    # ---- Claim (a): verdict NOT a function of Thompson type. ----
    by_type = {}
    for r in rows:
        by_type.setdefault(r["thompson_type"], set()).add(r["verdict"])
    pooled_spans = by_type.get("pooled") == {"dyadic", "triadic"}
    sequential_spans = by_type.get("sequential") == {"dyadic", "triadic"}
    type_multivalued = any(len(vs) > 1 for vs in by_type.values())
    print("CLAIM (a) verdict is NOT a function of Thompson type:")
    for t, vs in by_type.items():
        print(f"  {t:<11} -> {sorted(vs)}")
    print(f"  pooled spans dyadic<->triadic: {pooled_spans}")
    print(f"  sequential spans dyadic<->triadic: {sequential_spans}")
    print(f"  some Thompson type maps to BOTH verdicts: {type_multivalued}\n")

    # ---- Claim (b): verdict IS a function of the primitive pair. ----
    by_pair = {}
    pair_conflict = False
    for r in rows:
        pair = (r["joint_determination"], r["feedback_cycle"])
        by_pair.setdefault(pair, set()).add(r["verdict"])
    for pair, vs in by_pair.items():
        if len(vs) > 1:
            pair_conflict = True
    primitive_predicts = not pair_conflict
    # Stronger predicted mapping: (jd OR fc) -> triadic; (neither) -> dyadic
    mapping_as_predicted = True
    for r in rows:
        present = r["joint_determination"] or r["feedback_cycle"]
        if present and r["verdict"] != "triadic":
            mapping_as_predicted = False
        if not present and r["verdict"] != "dyadic":
            mapping_as_predicted = False
    print("CLAIM (b) verdict IS a function of the primitive pair (jd, cycle):")
    for pair, vs in sorted(by_pair.items()):
        print(f"  (jd={pair[0]}, cycle={pair[1]}) -> {sorted(vs)}")
    print(f"  no two forms share a pair yet differ in verdict: {primitive_predicts}")
    print(f"  (jd OR cycle)->triadic & (neither)->dyadic for every form: {mapping_as_predicted}\n")

    # ---- Decision rule (fixed before run). ----
    confirmed = (pooled_spans and sequential_spans
                 and primitive_predicts and mapping_as_predicted)
    # refuted if Thompson type predicts verdict cleanly (no type multivalued) OR pair conflict
    type_predicts_cleanly = not type_multivalued
    refuted = type_predicts_cleanly or pair_conflict

    if confirmed:
        decision = "confirmed"
    elif refuted:
        decision = "refuted"
    else:
        decision = "partial"

    print("DECISION:")
    print(f"  pooled_spans={pooled_spans}  sequential_spans={sequential_spans}")
    print(f"  primitive_pair_predicts={primitive_predicts}  "
          f"mapping_as_predicted={mapping_as_predicted}")
    print(f"  type_predicts_cleanly={type_predicts_cleanly}  pair_conflict={pair_conflict}")
    print(f"  VERDICT: {decision.upper()}")

    # ---- Write CSV. ----
    csv_path = os.path.join(RESULTS_DIR, "thompson_primitives.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "thompson_type", "encoding", "joint_determination",
            "feedback_cycle", "verdict", "max_phi", "mip_partition"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {csv_path}")

    return decision


if __name__ == "__main__":
    main()
