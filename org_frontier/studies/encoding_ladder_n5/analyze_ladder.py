"""n=5 encoding ladder: classical HMC / literacy → algorithmacy.

Designed minimal edits (commit / read / assist / joint-bind / idle).
Hypotheses fixed in hypotheses.md before computing.
Extends hmc_algo_boundary COMMIT_READ_BOUNDARY.

Run:  python org_frontier/studies/encoding_ladder_n5/analyze_ladder.py
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

L = ("W1", "S", "W2", "W3", "C")


def forms():
    out = []
    # 0 baseline classical HMC
    out.append((
        "hmc_classical", "baseline",
        [lambda x: x[1], lambda x: x[0], lambda x: x[2], lambda x: x[3], lambda x: x[4]],
        "W1↔S; W2,W3,C idle",
    ))
    # 1–2 H1: assist +W2
    out.append((
        "assist_OR_W2", "H1",
        [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1], lambda x: x[3], lambda x: x[4]],
        "S=W1∨W2; W1,W2 read S; W3,C idle",
    ))
    out.append((
        "assist_AND_W2", "H1",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3], lambda x: x[4]],
        "S=W1∧W2; W1,W2 read S; W3,C idle",
    ))
    # 3–4 H1: assist +W2+W3
    out.append((
        "assist_OR_W2W3", "H1",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3], lambda x: x[1], lambda x: x[1], lambda x: x[4]],
        "S=W1∨W2∨W3; W1,W2,W3 read S; C idle",
    ))
    out.append((
        "assist_AND_W2W3", "H1",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[4]],
        "S=W1∧W2∧W3; W1,W2,W3 read S; C idle",
    ))
    # 5 H2: C reads, not in commit
    out.append((
        "C_reads_not_in_commit", "H2",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1∧W2∧W3; C reads S only",
    ))
    # 6 H2: broadcast literacy
    out.append((
        "broadcast_W1", "H2",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1; W2,W3,C read S (no multi-commit)",
    ))
    # 7 H5: pre-boundary — workers full AND, C idle
    out.append((
        "workers_AND_Cidle", "H5",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[4]],
        "S=W1∧W2∧W3; workers read; C idle (pre-boundary)",
    ))
    # 8–9 H3: full joint bind
    out.append((
        "algo_full_AND", "H3",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1∧W2∧W3∧C; all read S — flip",
    ))
    out.append((
        "algo_full_OR", "H3",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1∨W2∨W3∨C; all read S — flip",
    ))
    # 10–12 H4: drops
    out.append((
        "drop_C_idle", "H4",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[4]],
        "from full AND: C removed from S, idle",
    ))
    out.append((
        "drop_C_readonly", "H4",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "from full AND: C removed from S, still reads",
    ))
    out.append((
        "drop_W3_idle", "H4",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[4], lambda x: x[1], lambda x: x[3], lambda x: x[1]],
        "from full AND: W3 removed from S, idle",
    ))
    return out


def main():
    print("n=5 ENCODING LADDER — HMC / literacy → algorithmacy")
    print("=" * 80)
    print("  cited: hmc_algo_boundary COMMIT_READ_BOUNDARY; constructs_n_gt3")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  labels:", L)
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
    for name, arm, rules, basis in forms():
        v = verdict(list(rules), L)
        core, cphi = major_complex(list(rules), L)
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

    base = by_name["hmc_classical"]
    or_w2 = by_name["assist_OR_W2"]
    and_w2 = by_name["assist_AND_W2"]
    or_w23 = by_name["assist_OR_W2W3"]
    and_w23 = by_name["assist_AND_W2W3"]
    h1 = (
        ctrl
        and base["n_core"] == 2
        and base["structure"] == "dyadic"
        and or_w2["n_core"] == 3
        and and_w2["n_core"] == 3
        and or_w2["structure"] == "dyadic"
        and and_w2["structure"] == "dyadic"
        and or_w23["n_core"] == 4
        and and_w23["n_core"] == 4
        and or_w23["structure"] == "dyadic"
        and and_w23["structure"] == "dyadic"
    )

    c_ro = by_name["C_reads_not_in_commit"]
    bcast = by_name["broadcast_W1"]
    h2 = (
        "C" not in c_ro["core"].split("|")
        and bcast["n_core"] == 2
        and "W2" not in bcast["core"].split("|")
        and "W3" not in bcast["core"].split("|")
        and "C" not in bcast["core"].split("|")
    )

    full_and = by_name["algo_full_AND"]
    full_or = by_name["algo_full_OR"]
    all_parties = {"W1", "S", "W2", "W3", "C"}
    h3 = (
        full_and["structure"] == "triadic"
        and full_or["structure"] == "triadic"
        and full_and["n_core"] == 5
        and full_or["n_core"] == 5
        and set(full_and["core"].split("|")) == all_parties
        and set(full_or["core"].split("|")) == all_parties
        and full_and["core_phi"] >= 3.0 - PHI_EPS
        and full_or["core_phi"] >= 3.0 - PHI_EPS
    )

    drop_idle = by_name["drop_C_idle"]
    drop_ro = by_name["drop_C_readonly"]
    drop_w3 = by_name["drop_W3_idle"]
    h4 = (
        "C" not in drop_idle["core"].split("|")
        and "C" not in drop_ro["core"].split("|")
        and "W3" not in drop_w3["core"].split("|")
        and drop_idle["n_core"] == 4
        and drop_ro["n_core"] == 4
        and drop_w3["n_core"] == 4
        and drop_idle["structure"] == "dyadic"
        and drop_ro["structure"] == "dyadic"
        and drop_w3["structure"] == "dyadic"
    )

    pre = by_name["workers_AND_Cidle"]
    h5 = (
        pre["structure"] == "dyadic"
        and pre["n_core"] == 4
        and "C" not in pre["core"].split("|")
        and set(pre["core"].split("|")) == {"W1", "S", "W2", "W3"}
    )

    if h1 and h2 and h3 and h4 and h5:
        verdict_word = "FULL_JOINT_FLIP"
        reading = (
            "FULL_JOINT_FLIP — assist grows core 2→3→4 with dyadic wholes; "
            "literacy→algorithmacy boundary is last outer party’s commit into S "
            "(whole triadic Φ=4, n_core=5); COMMIT_READ_BOUNDARY holds at n=5"
        )
        boundary_step = "workers_AND_Cidle → algo_full_AND"
    elif h1 and h3 and h4 and h5 and not h2:
        verdict_word = "COMMIT_ONLY"
        reading = "COMMIT_ONLY — commit membership dominates; read-without-commit still enters"
        boundary_step = "algo_full_AND (H2 failed)"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — n=5 encoding ladder incomplete"
        boundary_step = "unknown"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  baseline n_core={base['n_core']}  "
          f"OR_W2={or_w2['n_core']} AND_W2={and_w2['n_core']}  "
          f"OR_W2W3={or_w23['n_core']} AND_W2W3={and_w23['n_core']}")
    print(f"  C_reads core={c_ro['core']}  broadcast n_core={bcast['n_core']}")
    print(f"  pre-boundary whole={pre['structure']}/{pre['whole_phi']:.3f}  "
          f"core={pre['core']} Φ={pre['core_phi']:.3f}")
    print(f"  full_AND whole={full_and['structure']}/{full_and['whole_phi']:.3f}  "
          f"core={full_and['core']} Φ={full_and['core_phi']:.3f}")
    print(f"  full_OR  whole={full_or['structure']}/{full_or['whole_phi']:.3f}  "
          f"core={full_or['core']} Φ={full_or['core_phi']:.3f}")
    print(f"  drop_C_idle core={drop_idle['core']}  "
          f"drop_C_ro core={drop_ro['core']}  drop_W3 core={drop_w3['core']}")
    print(f"  H1 (progressive assist expands, wholes dyadic): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (read-without-commit stays out):             "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (full joint bind → algo Φ≥3, n_core=5):      "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (drop from commit → drop from core):         "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (pre-boundary not yet algorithmacy):         "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  boundary_step: {boundary_step}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
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
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "verdict": verdict_word,
            "boundary_step": boundary_step,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
