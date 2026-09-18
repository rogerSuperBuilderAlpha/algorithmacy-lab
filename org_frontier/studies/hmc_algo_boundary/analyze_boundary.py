"""Minimal encoding boundary: HMC/literacy ↔ algorithmacy at n>3.

Designed ladder. Hypotheses fixed in hypotheses.md.
Extends constructs_n_gt3 SCALE_BLURS_CONSTRUCTS.

Run:  python org_frontier/studies/hmc_algo_boundary/analyze_boundary.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def forms():
    L = ("W1", "S", "W2", "C")
    out = []
    # 0 baseline classical HMC on W1↔S; W2,C idle
    out.append((
        "hmc_classical", "baseline", L,
        [lambda x: x[1], lambda x: x[0], lambda x: x[2], lambda x: x[3]],
        "W1↔S; W2,C idle",
    ))
    # 1 H1: add W2 via OR
    out.append((
        "assist_OR", "H1", L,
        [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1], lambda x: x[3]],
        "S=W1∨W2; W1,W2 read S; C idle",
    ))
    # 2 H1: add W2 via AND
    out.append((
        "assist_AND", "H1", L,
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
        "S=W1∧W2; W1,W2 read S; C idle",
    ))
    # 3 H2: C reads S but not in determination (S=W1∧W2)
    out.append((
        "C_reads_not_in_commit", "H2", L,
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
        "S=W1∧W2; C reads S only",
    ))
    # 4 H2: broadcast literacy — S=W1 only; W2 and C read S
    out.append((
        "broadcast_W1", "H2", L,
        [lambda x: x[1], lambda x: x[0], lambda x: x[1], lambda x: x[1]],
        "S=W1; W2,C read S (no multi-commit)",
    ))
    # 5 H3: full joint commit
    out.append((
        "algo_full_AND", "H3", L,
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
        "S=W1∧W2∧C; all read S",
    ))
    # 6 contrast: full OR commit (all in rule)
    out.append((
        "algo_full_OR", "H3", L,
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3], lambda x: x[1], lambda x: x[1]],
        "S=W1∨W2∨C; all read S",
    ))
    # 7 H4: drop C from full AND (C idle)
    out.append((
        "drop_C_idle", "H4", L,
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
        "from full AND: C removed from S, idle",
    ))
    # 8 H4: drop C from full AND but C still reads S
    out.append((
        "drop_C_readonly", "H4", L,
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
        "from full AND: C removed from S, still reads",
    ))
    # 9 H4: drop W2 from full AND (W2 idle)
    out.append((
        "drop_W2_idle", "H4", L,
        [lambda x: x[1], lambda x: x[0] & x[3], lambda x: x[2], lambda x: x[1]],
        "from full AND: W2 removed from S, idle",
    ))
    return out


def main():
    print("HMC ↔ ALGORITHMACY ENCODING BOUNDARY — n=4 ladder")
    print("=" * 80)
    print("  cited: constructs_n_gt3 SCALE_BLURS_CONSTRUCTS; discriminant_boundaries")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    t_all = time.time()
    print("LADDER")
    print("-" * 80)
    by_name = {}
    for name, arm, labels, rules, basis in forms():
        v = verdict(list(rules), labels)
        core, cphi = major_complex(list(rules), labels)
        core_t = tuple(core) if core else ()
        cphi_f = float(cphi) if cphi is not None and cphi >= 0 else float("nan")
        row = {
            "name": name,
            "arm": arm,
            "structure": v.structure,
            "whole_phi": float(v.max_phi),
            "core": "|".join(core_t),
            "core_phi": cphi_f,
            "n_core": len(core_t),
            "basis": basis,
        }
        rows.append(row)
        by_name[name] = row
        print(
            f"  {name:<24} [{arm}]  whole={v.structure}/{v.max_phi:.3f}  "
            f"core={core_t} Φ={cphi_f:.3f} n_core={len(core_t)}"
        )
    print()

    # H1
    base = by_name["hmc_classical"]
    or_r = by_name["assist_OR"]
    and_r = by_name["assist_AND"]
    h1 = (
        ctrl
        and base["n_core"] == 2
        and or_r["n_core"] >= 3
        and and_r["n_core"] >= 3
    )

    # H2: C not in core when only reads; broadcast stays 2
    h2_form = by_name["C_reads_not_in_commit"]
    bcast = by_name["broadcast_W1"]
    h2 = (
        "C" not in h2_form["core"].split("|")
        and bcast["n_core"] == 2
    )

    # H3
    full = by_name["algo_full_AND"]
    h3 = (
        full["structure"] == "triadic"
        and full["core_phi"] >= 3.0 - PHI_EPS
        and full["n_core"] == 4
        and set(full["core"].split("|")) == {"W1", "S", "W2", "C"}
    )

    # H4
    drop_idle = by_name["drop_C_idle"]
    drop_ro = by_name["drop_C_readonly"]
    drop_w2 = by_name["drop_W2_idle"]
    h4 = (
        "C" not in drop_idle["core"].split("|")
        and "C" not in drop_ro["core"].split("|")
        and "W2" not in drop_w2["core"].split("|")
        and drop_idle["n_core"] == 3
        and drop_ro["n_core"] == 3
        and drop_w2["n_core"] == 3
    )

    if h1 and h2 and h3 and h4:
        verdict_word = "COMMIT_READ_BOUNDARY"
        reading = (
            "COMMIT_READ_BOUNDARY — party enters core iff in S’s determination "
            "and reads S; assist expands core; full ∧-commit flips to algorithmacy "
            "Φ=3; dropping commit membership drops core membership"
        )
    elif h1 and h3 and h4 and not h2:
        verdict_word = "COMMIT_ONLY"
        reading = "COMMIT_ONLY — commit membership dominates; read-without-commit still enters"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — encoding boundary incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  baseline n_core={base['n_core']}  OR={or_r['n_core']}  "
          f"AND={and_r['n_core']}")
    print(f"  C_reads core={h2_form['core']}  broadcast n_core={bcast['n_core']}")
    print(f"  full_AND whole={full['structure']}/{full['whole_phi']:.3f}  "
          f"core={full['core']} Φ={full['core_phi']:.3f}")
    print(f"  drop_C_idle core={drop_idle['core']}  "
          f"drop_C_ro core={drop_ro['core']}  drop_W2 core={drop_w2['core']}")
    print(f"  H1 (second human in S expands core):   "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (read-without-commit stays out):    "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (full joint commit → algo Φ≥3):     "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (drop from commit → drop from core): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  minimal HMC→algo: bind all outer parties into S’s rule with all "
          f"reading S (∧-commit); assist alone is not enough")
    print(f"  minimal algo→HMC-like: remove a party from S’s determination")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "name", "arm", "structure", "whole_phi", "core", "core_phi",
            "n_core", "basis",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "arm": r["arm"],
                "structure": r["structure"],
                "whole_phi": f"{r['whole_phi']:.6f}",
                "core": r["core"],
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "basis": r["basis"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
