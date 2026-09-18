"""n=6 encoding ladder: does Φ track n−1 at the full-joint flip?

Designed minimal edits (commit / read / assist / joint-bind / idle).
Hypotheses fixed in hypotheses.md before computing.
Extends encoding_ladder_n5 FULL_JOINT_FLIP.

Run:  python org_frontier/studies/encoding_ladder_n6/analyze_ladder.py
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

L = ("W1", "S", "W2", "W3", "W4", "C")
N = len(L)
N_MINUS_1 = N - 1  # 5


def forms():
    out = []
    # 0 baseline classical HMC
    out.append((
        "hmc_classical", "baseline",
        [lambda x: x[1], lambda x: x[0],
         lambda x: x[2], lambda x: x[3], lambda x: x[4], lambda x: x[5]],
        "W1↔S; W2,W3,W4,C idle",
    ))
    # 1–2 assist +W2
    out.append((
        "assist_OR_W2", "assist",
        [lambda x: x[1], lambda x: x[0] | x[2],
         lambda x: x[1], lambda x: x[3], lambda x: x[4], lambda x: x[5]],
        "S=W1∨W2; W1,W2 read S; W3,W4,C idle",
    ))
    out.append((
        "assist_AND_W2", "assist",
        [lambda x: x[1], lambda x: x[0] & x[2],
         lambda x: x[1], lambda x: x[3], lambda x: x[4], lambda x: x[5]],
        "S=W1∧W2; W1,W2 read S; W3,W4,C idle",
    ))
    # 3–4 assist +W2+W3
    out.append((
        "assist_OR_W2W3", "assist",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3],
         lambda x: x[1], lambda x: x[1], lambda x: x[4], lambda x: x[5]],
        "S=W1∨W2∨W3; W1,W2,W3 read S; W4,C idle",
    ))
    out.append((
        "assist_AND_W2W3", "assist",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3],
         lambda x: x[1], lambda x: x[1], lambda x: x[4], lambda x: x[5]],
        "S=W1∧W2∧W3; W1,W2,W3 read S; W4,C idle",
    ))
    # 5–6 assist +W2+W3+W4 (new rung vs n=5)
    out.append((
        "assist_OR_W2W3W4", "assist",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
        "S=W1∨W2∨W3∨W4; workers read; C idle",
    ))
    out.append((
        "assist_AND_W2W3W4", "assist",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
        "S=W1∧W2∧W3∧W4; workers read; C idle",
    ))
    # 7 C reads, not in commit
    out.append((
        "C_reads_not_in_commit", "commit_read",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1∧W2∧W3∧W4; C reads S only",
    ))
    # 8 broadcast literacy
    out.append((
        "broadcast_W1", "commit_read",
        [lambda x: x[1], lambda x: x[0],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1; W2,W3,W4,C read S (no multi-commit)",
    ))
    # 9 pre-boundary
    out.append((
        "workers_AND_Cidle", "pre_boundary",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
        "S=W1∧W2∧W3∧W4; workers read; C idle (pre-boundary)",
    ))
    # 10–11 full joint bind
    out.append((
        "algo_full_AND", "flip",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4] & x[5],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1∧W2∧W3∧W4∧C; all read S — flip",
    ))
    out.append((
        "algo_full_OR", "flip",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4] | x[5],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W1∨W2∨W3∨W4∨C; all read S — flip",
    ))
    # 12–14 drops
    out.append((
        "drop_C_idle", "drop",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[5]],
        "from full AND: C removed from S, idle",
    ))
    out.append((
        "drop_C_readonly", "drop",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "from full AND: C removed from S, still reads",
    ))
    out.append((
        "drop_W4_idle", "drop",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[5],
         lambda x: x[1], lambda x: x[1], lambda x: x[4], lambda x: x[1]],
        "from full AND: W4 removed from S, idle",
    ))
    return out


def main():
    print("n=6 ENCODING LADDER — Φ vs (n−1) at full-joint flip")
    print("=" * 80)
    print("  cited: encoding_ladder_n5 FULL_JOINT_FLIP; hmc_algo_boundary")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  labels: {L}  n={N}  n−1={N_MINUS_1}")
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
        t0 = time.time()
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
            "elapsed_s": round(time.time() - t0, 1),
        }
        rows.append(row)
        by_name[name] = row
        print(
            f"  {name:<24} [{arm}]  whole={v.structure}/{v.max_phi:.3f}  "
            f"core={core_t} Φ={cphi_f:.3f} n_core={len(core_t)}  "
            f"t={row['elapsed_s']}s"
        )
    print()

    base = by_name["hmc_classical"]
    a_w2 = by_name["assist_AND_W2"]
    a_w23 = by_name["assist_AND_W2W3"]
    a_w234 = by_name["assist_AND_W2W3W4"]
    a_or_w2 = by_name["assist_OR_W2"]
    a_or_w23 = by_name["assist_OR_W2W3"]
    a_or_w234 = by_name["assist_OR_W2W3W4"]
    pre = by_name["workers_AND_Cidle"]
    full_and = by_name["algo_full_AND"]
    full_or = by_name["algo_full_OR"]
    c_ro = by_name["C_reads_not_in_commit"]
    bcast = by_name["broadcast_W1"]
    drop_idle = by_name["drop_C_idle"]
    drop_ro = by_name["drop_C_readonly"]
    drop_w4 = by_name["drop_W4_idle"]

    all_parties = set(L)

    # Assist path: stepwise expand, wholes dyadic
    assist_ok = (
        base["n_core"] == 2 and base["structure"] == "dyadic"
        and a_w2["n_core"] == 3 and a_w2["structure"] == "dyadic"
        and a_or_w2["n_core"] == 3 and a_or_w2["structure"] == "dyadic"
        and a_w23["n_core"] == 4 and a_w23["structure"] == "dyadic"
        and a_or_w23["n_core"] == 4 and a_or_w23["structure"] == "dyadic"
        and a_w234["n_core"] == 5 and a_w234["structure"] == "dyadic"
        and a_or_w234["n_core"] == 5 and a_or_w234["structure"] == "dyadic"
    )

    # COMMIT_READ_BOUNDARY
    commit_read = (
        "C" not in c_ro["core"].split("|")
        and bcast["n_core"] == 2
        and "C" not in drop_idle["core"].split("|")
        and "C" not in drop_ro["core"].split("|")
        and "W4" not in drop_w4["core"].split("|")
        and drop_idle["structure"] == "dyadic"
        and drop_ro["structure"] == "dyadic"
        and drop_w4["structure"] == "dyadic"
    )

    # Pre-boundary not algo
    pre_ok = (
        pre["structure"] == "dyadic"
        and pre["n_core"] == 5
        and "C" not in pre["core"].split("|")
    )

    # Full flip
    flip_triadic = (
        full_and["structure"] == "triadic"
        and full_or["structure"] == "triadic"
        and full_and["n_core"] == N
        and full_or["n_core"] == N
        and set(full_and["core"].split("|")) == all_parties
        and set(full_or["core"].split("|")) == all_parties
    )
    phi_and = full_and["core_phi"]
    phi_or = full_or["core_phi"]
    phi_eq_nm1 = (
        abs(phi_and - N_MINUS_1) < PHI_EPS
        and abs(phi_or - N_MINUS_1) < PHI_EPS
    )
    phi_below_nm1 = (
        flip_triadic
        and phi_and < N_MINUS_1 - PHI_EPS
        and phi_or < N_MINUS_1 - PHI_EPS
    )

    # H1: flip + Φ=n−1 + assist path + same boundary form + COMMIT_READ
    h1 = (
        ctrl and assist_ok and pre_ok and flip_triadic and phi_eq_nm1
        and commit_read
    )

    # H2: flip but Φ saturates below n−1
    h2 = (
        ctrl and flip_triadic and phi_below_nm1 and pre_ok
    )

    # H3: assist/boundary morphs OR COMMIT_READ fails
    early_flip = any(
        by_name[n]["structure"] == "triadic"
        for n in (
            "assist_AND_W2", "assist_AND_W2W3", "assist_AND_W2W3W4",
            "assist_OR_W2", "assist_OR_W2W3", "assist_OR_W2W3W4",
            "workers_AND_Cidle",
        )
    )
    h3 = early_flip or not commit_read or (flip_triadic and not pre_ok)

    if h1 and not h2 and not h3:
        verdict_word = "PHI_TRACKS_NM1"
        reading = (
            "PHI_TRACKS_NM1 — n=6 ladder same form as n=5; boundary "
            "workers_AND_Cidle → algo_full_AND; flip whole triadic "
            f"n_core={N} Φ={N_MINUS_1} (=n−1); COMMIT_READ_BOUNDARY holds"
        )
        boundary_step = "workers_AND_Cidle → algo_full_AND"
        phi_vs_nm1 = f"Φ={phi_and:.0f} = n−1"
    elif h2 and not h1:
        verdict_word = "PHI_SATURATES"
        reading = (
            f"PHI_SATURATES — flip at full joint but Φ={phi_and:.3f} < n−1={N_MINUS_1}"
        )
        boundary_step = "workers_AND_Cidle → algo_full_AND"
        phi_vs_nm1 = f"Φ={phi_and:.3f} < n−1"
    elif h3 and not h1:
        verdict_word = "BOUNDARY_MORPHS"
        reading = (
            "BOUNDARY_MORPHS — assist path or COMMIT_READ changes at n=6"
        )
        boundary_step = "morphed"
        phi_vs_nm1 = f"Φ={phi_and:.3f}"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — n=6 encoding ladder incomplete"
        boundary_step = "unknown"
        phi_vs_nm1 = f"Φ_and={phi_and:.3f} Φ_or={phi_or:.3f}"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  baseline n_core={base['n_core']}  "
          f"AND_W2={a_w2['n_core']} AND_W2W3={a_w23['n_core']} "
          f"AND_W2W3W4={a_w234['n_core']}")
    print(f"  C_reads core={c_ro['core']}  broadcast n_core={bcast['n_core']}")
    print(f"  pre-boundary whole={pre['structure']}/{pre['whole_phi']:.3f}  "
          f"core={pre['core']} Φ={pre['core_phi']:.3f}")
    print(f"  full_AND whole={full_and['structure']}/{full_and['whole_phi']:.3f}  "
          f"core={full_and['core']} Φ={full_and['core_phi']:.3f}")
    print(f"  full_OR  whole={full_or['structure']}/{full_or['whole_phi']:.3f}  "
          f"core={full_or['core']} Φ={full_or['core_phi']:.3f}")
    print(f"  drop_C_idle core={drop_idle['core']}  "
          f"drop_C_ro core={drop_ro['core']}  drop_W4 core={drop_w4['core']}")
    print(f"  H1 (flip + Φ=n−1 + same boundary):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (Φ saturates below n−1):         "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (assist/boundary morphs at n=6): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  COMMIT_READ_BOUNDARY:               "
          f"{'HOLDS' if commit_read else 'FAILS'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  boundary_step: {boundary_step}")
    print(f"  phi_vs_nm1: {phi_vs_nm1}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "name", "arm", "structure", "whole_phi", "core", "core_phi",
            "n_core", "basis", "elapsed_s",
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
                "elapsed_s": r["elapsed_s"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "commit_read": "HOLDS" if commit_read else "FAILS",
            "verdict": verdict_word,
            "boundary_step": boundary_step,
            "phi_vs_nm1": phi_vs_nm1,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
