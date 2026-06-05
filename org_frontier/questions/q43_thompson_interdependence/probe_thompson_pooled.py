"""Q43 H2 — "pooled" is verdict-ambiguous; the split turns on joint determination.

Two pooled encodings over the same parts, same node count, AND family:
  - Independent-contribution pool: per-party channels through a shared node, no
    joint determination. [lambda x: x[1], lambda x: x[0], lambda x: x[1]] at n=3.
  - All-required pool (#116): S' = AND of all non-S parties, every non-S party = S.
    The pool(n) helper from probe_group_surplus.py. Run at n=3 and n=4.

Decision rule (fixed before run): H2 confirmed if the two encodings give opposite
verdicts at n=3 (independent-contribution dyadic, all-required triadic); refuted if
both give the same verdict.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q43_thompson_interdependence/probe_thompson_pooled.py
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.probes.probe_group_surplus import pool, best_proper_subset_phi  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

PHI_EPS = 1e-9
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    """Strict-mediation / pass-through chain triad (#57) must read triadic at Φ=2.0,
    MIP 2 parts {W,SC}. Abort the whole probe if it does not."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    print("INSTRUMENT CONTROL — pass-through mediator chain (#57)")
    print(f"  rules: W'=S, S'=W&C, C'=S   labels={labels}")
    print(f"  structure={v.structure}  max_phi={v.max_phi:.6f}  MIP={v.mip_partition}")
    assert v.structure == "triadic", f"control structure {v.structure} != triadic"
    assert abs(v.max_phi - 2.0) < 1e-6, f"control max_phi {v.max_phi} != 2.0"
    print("  control PASSED (triadic, Φ=2.0)\n")
    return v


def main():
    instrument_control()

    rows = []

    # --- Independent-contribution pool (no joint determination), n=3 ---
    indep_rules = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]
    indep_labels = ("W", "S", "C")
    vi = verdict(indep_rules, indep_labels)
    mc_core, mc_phi = major_complex(indep_rules, indep_labels)
    print("INDEPENDENT-CONTRIBUTION POOL (#25/#40), n=3")
    print(f"  rules: W'=S, S'=W, C'=S   labels={indep_labels}")
    print(f"  structure={vi.structure}  max_phi={vi.max_phi:.6f}  MIP={vi.mip_partition}")
    print(f"  major complex: core={mc_core}  phi={mc_phi:.6f}\n")
    rows.append({
        "encoding": "independent_contribution_pool",
        "n": 3,
        "structure": vi.structure,
        "max_phi": f"{vi.max_phi:.6f}",
        "major_complex_core": "".join(mc_core) if mc_core else "",
        "major_complex_phi": f"{mc_phi:.6f}",
        "best_proper_subset_phi": "",
        "group_surplus": "",
    })

    # --- All-required pool (#116), n=3 and n=4 ---
    print("ALL-REQUIRED POOL (#116) — S'=AND(non-S), every non-S = S")
    for n in (3, 4):
        prules, plabels = pool(n)
        vp = verdict(prules, plabels)
        best = best_proper_subset_phi(prules, plabels)
        surplus = vp.max_phi - best
        print(f"  n={n}  labels={plabels}")
        print(f"    structure={vp.structure}  max_phi={vp.max_phi:.6f}  MIP={vp.mip_partition}")
        print(f"    best_proper_subset_phi={best:.6f}  group_surplus={surplus:+.6f}")
        rows.append({
            "encoding": "all_required_pool",
            "n": n,
            "structure": vp.structure,
            "max_phi": f"{vp.max_phi:.6f}",
            "major_complex_core": "",
            "major_complex_phi": "",
            "best_proper_subset_phi": f"{best:.6f}",
            "group_surplus": f"{surplus:+.6f}",
        })
    print()

    # --- Decision rule ---
    indep_struct = vi.structure
    allreq_n3 = next(r for r in rows if r["encoding"] == "all_required_pool" and r["n"] == 3)
    allreq_struct = allreq_n3["structure"]
    opposite = (indep_struct == "dyadic" and allreq_struct == "triadic")
    same = (indep_struct == allreq_struct)

    print("DECISION (fixed before run)")
    print(f"  independent-contribution (n=3): {indep_struct}")
    print(f"  all-required pool (n=3):        {allreq_struct}")
    if opposite:
        verdict_word = "CONFIRMED"
        reason = "opposite verdicts at n=3 (independent dyadic, all-required triadic)"
    elif same:
        verdict_word = "REFUTED"
        reason = "both encodings give the same verdict"
    else:
        verdict_word = "PARTIAL"
        reason = f"split but not the predicted direction (indep={indep_struct}, allreq={allreq_struct})"
    print(f"  H2 {verdict_word}: {reason}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "thompson_pooled.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {csv_path}")
    return verdict_word


if __name__ == "__main__":
    main()
