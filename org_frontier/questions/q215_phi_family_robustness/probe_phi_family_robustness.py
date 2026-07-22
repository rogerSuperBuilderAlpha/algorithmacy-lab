"""Probe Q215 (H1-H5) — Φ-family sign-robustness of the OT-manuscript headline verdicts.

Computes each headline form's whole-system Φ under IIT 4.0 (pyphi.new_big_phi, the lab's standard
instrument) and IIT 3.0 (pyphi.compute), on identical TPMs over identical reachable states, and
reads whether the qualitative verdict (binds vs factors) agrees in sign. Hypotheses and decision
rule are pre-registered in hypotheses.md; forms and sources in methods.md.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q215_phi_family_robustness.probe_phi_family_robustness
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import exceptions, new_big_phi

# Force the IIT 3.0 pipeline sequential. config.PARALLEL=False is not enough in this
# dev build: compute.subsystem._ces / _sia_map_reduce pass the PARALLEL_*_EVALUATION
# Mapping itself as MapReduce's `parallel` flag, and a non-empty dict is truthy, which
# demands ray. An empty Mapping is type-valid and falsy, so both arms run in-process.
pyphi.config.PARALLEL = False
pyphi.config.PARALLEL_CUT_EVALUATION = {}
pyphi.config.PARALLEL_CONCEPT_EVALUATION = {}
pyphi.config.PARALLEL_COMPLEX_EVALUATION = {}
pyphi.config.PROGRESS_BARS = False

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states

EPS = 1e-9

FORMS = [
    # (id, name, rules, labels)
    ("CTRL+", "read-recipient triad",
     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("E", "M", "R")),
    ("CTRL-", "two disjoint dyads",
     [lambda x: x[1], lambda x: x[0], lambda x: x[3], lambda x: x[2]], ("A", "B", "C", "D")),
    ("E1", "quorum 1-of-3",
     [lambda x: x[3], lambda x: x[3], lambda x: x[3],
      lambda x: int(x[0] + x[1] + x[2] >= 1)], ("P0", "P1", "P2", "S")),
    ("E2", "quorum 2-of-3",
     [lambda x: x[3], lambda x: x[3], lambda x: x[3],
      lambda x: int(x[0] + x[1] + x[2] >= 2)], ("P0", "P1", "P2", "S")),
    ("E3", "quorum 3-of-3",
     [lambda x: x[3], lambda x: x[3], lambda x: x[3],
      lambda x: int(x[0] + x[1] + x[2] >= 3)], ("P0", "P1", "P2", "S")),
    ("E4", "rotation (4-cycle of copyists)",
     [lambda x: x[3], lambda x: x[0], lambda x: x[1], lambda x: x[2]], ("A", "B", "C", "D")),
    ("E5", "one-sided veto (lockstep)",
     [lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]], ("W", "S", "C")),
    ("E6", "dispatch, full triad",
     [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])], ("W", "S", "C")),
    ("E7", "dispatch, rider dropped",
     [lambda x: 1 - x[1], lambda x: x[0], lambda x: x[2] & (1 - x[1])], ("W", "S", "C")),
    ("E8", "maximal wiring (6 edges, no constants)",
     [lambda x: 1 - (x[1] | x[2]), lambda x: (1 - x[0]) & x[2], lambda x: 1 - (x[0] & x[1])],
     ("W", "S", "C")),
]

# Pre-registered expected verdicts (both arms), from hypotheses.md.
EXPECT = {"CTRL+": "BINDS", "CTRL-": "FACTORS",
          "E1": "BINDS", "E2": "FACTORS", "E3": "BINDS",
          "E4": "BINDS", "E5": "FACTORS",
          "E6": "BINDS", "E7": "FACTORS", "E8": "FACTORS"}


def per_state_phis(rules, labels):
    """[(state, phi40, phi30)] over reachable states of the whole system."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    rows = []
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        phis = []
        for arm in ("40", "30"):
            try:
                sub = pyphi.Subsystem(net, state)
                if arm == "40":
                    phi = float(new_big_phi.sia(sub).phi)
                else:
                    # The 3.0 pipeline requires its own partition scheme; the dev
                    # build's global default is 4.0's SET_UNI/BI.
                    with pyphi.config.override(SYSTEM_PARTITION_TYPE="DIRECTED_BI"):
                        phi = float(pyphi.compute.sia(sub).phi)
            except exceptions.StateUnreachableError:
                phi = float("nan")
            phis.append(phi)
        rows.append((state, phis[0], phis[1]))
    return rows


def main():
    print("PROBE Q215 (H1-H5) — Φ-family sign-robustness (IIT 4.0 vs IIT 3.0)")
    print("=" * 78)
    results = {}
    csv_rows = []
    for fid, name, rules, labels in FORMS:
        rows = per_state_phis(rules, labels)
        max40 = max(p for _, p, _ in rows)
        max30 = max(p for _, _, p in rows)
        v40 = "BINDS" if max40 > EPS else "FACTORS"
        v30 = "BINDS" if max30 > EPS else "FACTORS"
        agree = v40 == v30
        ok = agree and v40 == EXPECT[fid]
        results[fid] = (v40, v30, max40, max30, ok, rows)
        print(f"  {fid:5s} {name:38s} 4.0 Φmax={max40:.4f} {v40:7s}  "
              f"3.0 Φmax={max30:.4f} {v30:7s}  sign-{'AGREE' if agree else 'SPLIT'}"
              f"  expect={EXPECT[fid]:7s} {'PASS' if ok else 'FAIL'}")
        for state, p40, p30 in rows:
            csv_rows.append([fid, name, "".join(map(str, state)), p40, p30])

    # Controls gate the comparison.
    controls_ok = results["CTRL+"][4] and results["CTRL-"][4]
    print("=" * 78)
    print(f"  instrument controls (both arms): {'PASS' if controls_ok else 'FAIL - ABORT'}")
    if not controls_ok:
        sys.exit(1)

    h = {
        "H1": all(results[k][4] for k in ("E1", "E2", "E3")),
        "H2": results["E4"][4],
        "H3": results["E5"][4],
        "H4": results["E6"][4] and results["E7"][4],
        "H5": (results["E8"][0] == results["E8"][1] == "FACTORS"
               and all(p40 <= EPS and p30 <= EPS for _, p40, p30 in results["E8"][5])),
    }
    names = {"H1": "quorum extremes law measure-robust",
             "H2": "rotation binds in both",
             "H3": "synchronization factoring measure-robust",
             "H4": "dispatch pair measure-robust both directions",
             "H5": "maximal wiring factors in both, every reachable state"}
    for k in ("H1", "H2", "H3", "H4", "H5"):
        print(f"  {k} ({names[k]}): {'CONFIRMED' if h[k] else 'REFUTED'}")
    robust = sum(1 for k in ("E1","E2","E3","E4","E5","E6","E7","E8") if results[k][4])
    print(f"  headline forms sign-robust: {robust}/8")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "phi_family.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "name", "state", "phi_iit40", "phi_iit30"])
        w.writerows(csv_rows)
    print(f"  per-state values -> {os.path.join(d_, 'phi_family.csv')}")


if __name__ == "__main__":
    main()
