"""HMC / CMC / AI-MC encoding ladders at n=6.

Trimmed: baseline → pre_AND → last_reads → full_AND/OR → drop.
Hypotheses fixed in hypotheses.md before computing.
Extends construct_ladders_n5 BOUNDARY_TRANSFERS; encoding_ladder_n6.

Run:  python org_frontier/studies/construct_ladders_n6/analyze_ladders.py
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

LH = ("W1", "S", "W2", "W3", "W4", "C")
LC = ("W", "S", "C", "D", "E", "F")
LA = ("W", "A", "C", "D", "E", "F")
N = 6
N_MINUS_1 = 5


def hmc_forms():
    # indices: 0=W1,1=S,2=W2,3=W3,4=W4,5=C
    return [
        (
            "hmc_classical", "HMC", "baseline",
            [lambda x: x[1], lambda x: x[0],
             lambda x: x[2], lambda x: x[3], lambda x: x[4], lambda x: x[5]],
            "W1↔S; others idle",
        ),
        (
            "hmc_pre_AND", "HMC", "pre_boundary",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
            "S=W1∧W2∧W3∧W4; C idle",
        ),
        (
            "hmc_C_reads", "HMC", "commit_read",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "workers bind; C reads only",
        ),
        (
            "hmc_full_AND", "HMC", "flip",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4] & x[5],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S=all outers ∧; all read — flip",
        ),
        (
            "hmc_full_OR", "HMC", "flip",
            [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4] | x[5],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S=all outers ∨; all read — flip",
        ),
        (
            "hmc_drop_C_ro", "HMC", "drop",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "from full: C dropped, still reads",
        ),
    ]


def cmc_forms():
    # 0=W,1=S,2=C,3=D,4=E,5=F
    return [
        (
            "cmc_chain", "CMC", "baseline",
            [lambda x: x[0], lambda x: x[0], lambda x: x[1],
             lambda x: x[2], lambda x: x[3], lambda x: x[4]],
            "W→S→C→D→E→F conveyor",
        ),
        (
            "cmc_pre_AND", "CMC", "pre_boundary",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
            "S=W∧C∧D∧E; F idle",
        ),
        (
            "cmc_F_reads", "CMC", "commit_read",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S=W∧C∧D∧E; F reads only",
        ),
        (
            "cmc_full_AND", "CMC", "flip",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4] & x[5],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S=all ∧; all read — flip",
        ),
        (
            "cmc_full_OR", "CMC", "flip",
            [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4] | x[5],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S=all ∨; all read — flip",
        ),
        (
            "cmc_drop_F_ro", "CMC", "drop",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "from full: F dropped, still reads",
        ),
    ]


def aimc_forms():
    # 0=W,1=A,2=C,3=D,4=E,5=F
    return [
        (
            "aimc_rewrite", "AI-MC", "baseline",
            [lambda x: x[2], lambda x: x[0], lambda x: x[1],
             lambda x: x[3], lambda x: x[4], lambda x: x[5]],
            "W→A→C rewrite; D,E,F idle",
        ),
        (
            "aimc_pre_AND", "AI-MC", "pre_boundary",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
            "A=W∧C∧D∧E; F idle",
        ),
        (
            "aimc_F_reads", "AI-MC", "commit_read",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "A=W∧C∧D∧E; F reads only",
        ),
        (
            "aimc_full_AND", "AI-MC", "flip",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4] & x[5],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "A=all ∧; all read — flip",
        ),
        (
            "aimc_full_OR", "AI-MC", "flip",
            [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4] | x[5],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "A=all ∨; all read — flip",
        ),
        (
            "aimc_drop_F_ro", "AI-MC", "drop",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
             lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "from full: F dropped, still reads",
        ),
    ]


def run_family(forms, labels, by_name, rows):
    for name, family, rung, rules, basis in forms:
        t0 = time.time()
        v = verdict(list(rules), labels)
        core, cphi = major_complex(list(rules), labels)
        core_t = tuple(core) if core else ()
        cphi_f = float(cphi) if cphi is not None and cphi >= 0 else float("nan")
        row = {
            "name": name,
            "family": family,
            "rung": rung,
            "structure": v.structure,
            "whole_phi": float(v.max_phi),
            "core": "|".join(core_t),
            "core_phi": cphi_f,
            "n_core": len(core_t),
            "basis": basis,
            "elapsed_s": round(time.time() - t0, 1),
        }
        rows.append(row)
        by_name[name] = row
        print(
            f"  {name:<22} [{rung}]  whole={v.structure}/{v.max_phi:.3f}  "
            f"core={core_t} Φ={cphi_f:.3f} n_core={len(core_t)}  "
            f"t={row['elapsed_s']}s"
        )


def family_ok(by_name, prefix, last):
    pre = by_name[f"{prefix}_pre_AND"]
    full_a = by_name[f"{prefix}_full_AND"]
    full_o = by_name[f"{prefix}_full_OR"]
    reads = by_name[f"{prefix}_{last}_reads"]
    drop = by_name[f"{prefix}_drop_{last}_ro"]
    tracks = (
        pre["structure"] == "dyadic"
        and pre["n_core"] == N - 1
        and full_a["structure"] == "triadic"
        and full_o["structure"] == "triadic"
        and full_a["n_core"] == N
        and full_o["n_core"] == N
        and abs(full_a["core_phi"] - N_MINUS_1) < PHI_EPS
        and abs(full_o["core_phi"] - N_MINUS_1) < PHI_EPS
    )
    commit_read = (
        last not in reads["core"].split("|")
        and last not in drop["core"].split("|")
        and drop["n_core"] == N - 1
        and drop["structure"] == "dyadic"
    )
    return tracks, commit_read


def main():
    print("CONSTRUCT LADDERS AT n=6 — HMC / CMC / AI-MC")
    print("=" * 80)
    print("  cited: construct_ladders_n5 BOUNDARY_TRANSFERS; "
          "encoding_ladder_n6 PHI_TRACKS_NM1")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  n={N}  n−1={N_MINUS_1}")
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
    by_name = {}
    t_all = time.time()

    print("HMC LADDER")
    print("-" * 80)
    run_family(hmc_forms(), LH, by_name, rows)
    print()
    print("CMC LADDER")
    print("-" * 80)
    run_family(cmc_forms(), LC, by_name, rows)
    print()
    print("AI-MC LADDER")
    print("-" * 80)
    run_family(aimc_forms(), LA, by_name, rows)
    print()

    hmc_t, hmc_cr = family_ok(by_name, "hmc", "C")
    cmc_t, cmc_cr = family_ok(by_name, "cmc", "F")
    aimc_t, aimc_cr = family_ok(by_name, "aimc", "F")

    h1 = ctrl and hmc_t and cmc_t and aimc_t
    h2 = ctrl and not (hmc_t and cmc_t and aimc_t)
    h3 = ctrl and not (hmc_cr and cmc_cr and aimc_cr)

    # baselines sanity (not separate H, but reported)
    hmc_base = by_name["hmc_classical"]
    cmc_base = by_name["cmc_chain"]
    aimc_base = by_name["aimc_rewrite"]

    if h1 and not h2 and not h3:
        verdict_word = "PHI_TRACKS_NM1_ALL"
        reading = (
            "PHI_TRACKS_NM1_ALL — HMC/CMC/AI-MC at n=6: pre_AND→full_AND "
            "flip with Φ=5 (=n−1); COMMIT_READ holds; BOUNDARY_TRANSFERS "
            "scales with PHI_TRACKS_NM1"
        )
        boundary_step = "pre_AND → full_AND (all three)"
    elif h2:
        failed = [f for f, ok in (("HMC", hmc_t), ("CMC", cmc_t), ("AI-MC", aimc_t)) if not ok]
        verdict_word = "FAMILY_MORPHS"
        reading = f"FAMILY_MORPHS — non-tracking families: {'/'.join(failed)}"
        boundary_step = "morphed"
    elif h3:
        verdict_word = "COMMIT_READ_BREAKS"
        reading = "COMMIT_READ_BREAKS — read/drop membership fails on a family"
        boundary_step = "pre_AND → full_AND (COMMIT_READ fail)"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — n=6 construct ladders incomplete"
        boundary_step = "unknown"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  HMC  tracks={hmc_t} COMMIT_READ={hmc_cr}  "
          f"base n_core={hmc_base['n_core']}  "
          f"full Φ={by_name['hmc_full_AND']['core_phi']:.0f}")
    print(f"  CMC  tracks={cmc_t} COMMIT_READ={cmc_cr}  "
          f"base n_core={cmc_base['n_core']}  "
          f"full Φ={by_name['cmc_full_AND']['core_phi']:.0f}")
    print(f"  AI-MC tracks={aimc_t} COMMIT_READ={aimc_cr}  "
          f"base n_core={aimc_base['n_core']}  "
          f"full Φ={by_name['aimc_full_AND']['core_phi']:.0f}")
    print(f"  H1 (all three PHI_TRACKS_NM1): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (some family morphs):       "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (COMMIT_READ breaks):       "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  boundary_step: {boundary_step}")
    print(f"  phi_vs_nm1: Φ={N_MINUS_1} = n−1" if h1 else "phi_vs_nm1: mixed")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "name", "family", "rung", "structure", "whole_phi", "core",
            "core_phi", "n_core", "basis", "elapsed_s",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "family": r["family"],
                "rung": r["rung"],
                "structure": r["structure"],
                "whole_phi": f"{r['whole_phi']:.6f}",
                "core": r["core"],
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "basis": r["basis"],
                "elapsed_s": r["elapsed_s"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "boundary_step": boundary_step,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
