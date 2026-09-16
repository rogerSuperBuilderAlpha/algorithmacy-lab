"""CMC and AI-MC encoding ladders at n=5 vs HMC FULL_JOINT_FLIP.

Hypotheses fixed in hypotheses.md before computing.
Extends encoding_ladder_n5, hmc_algo_boundary, constructs_n_gt3.

Run:  python org_frontier/studies/construct_ladders_n5/analyze_ladders.py
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

LC = ("W", "S", "C", "D", "E")
LA = ("W", "A", "C", "D", "E")
N = 5
N_MINUS_1 = 4


def cmc_forms():
    out = []
    out.append((
        "cmc_chain", "CMC", "baseline",
        [lambda x: x[0], lambda x: x[0], lambda x: x[1],
         lambda x: x[2], lambda x: x[3]],
        "W→S→C→D→E one-way conveyor",
    ))
    out.append((
        "cmc_echo", "CMC", "baseline",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        "S=W; C,D,E read S (broadcast convey)",
    ))
    out.append((
        "cmc_assist_OR", "CMC", "assist",
        [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1],
         lambda x: x[3], lambda x: x[4]],
        "S=W∨C; W,C read S; D,E idle",
    ))
    out.append((
        "cmc_pre_AND", "CMC", "pre_boundary",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1],
         lambda x: x[1], lambda x: x[4]],
        "S=W∧C∧D; readers; E idle (pre-boundary)",
    ))
    out.append((
        "cmc_E_reads", "CMC", "commit_read",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        "S=W∧C∧D; E reads only",
    ))
    out.append((
        "cmc_full_AND", "CMC", "flip",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W∧C∧D∧E; all read S — flip",
    ))
    out.append((
        "cmc_full_OR", "CMC", "flip",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "S=W∨C∨D∨E; all read S — flip",
    ))
    out.append((
        "cmc_drop_E_ro", "CMC", "drop",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        "from full AND: E removed from S, still reads",
    ))
    return out


def aimc_forms():
    out = []
    out.append((
        "aimc_rewrite", "AI-MC", "baseline",
        [lambda x: x[2], lambda x: x[0], lambda x: x[1],
         lambda x: x[3], lambda x: x[4]],
        "W→A→C rewrite loop; D,E idle",
    ))
    out.append((
        "aimc_blend", "AI-MC", "baseline",
        [lambda x: x[2], lambda x: x[0] | x[2], lambda x: x[1],
         lambda x: x[3], lambda x: x[4]],
        "A blends W with C-context; D,E idle",
    ))
    out.append((
        "aimc_all_read_A", "AI-MC", "transform",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        "A=W transform; all read A (still no multi-commit)",
    ))
    out.append((
        "aimc_pre_AND", "AI-MC", "pre_boundary",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1],
         lambda x: x[1], lambda x: x[4]],
        "A commits W∧C∧D; E idle (pre-boundary)",
    ))
    out.append((
        "aimc_E_reads", "AI-MC", "commit_read",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        "A=W∧C∧D; E reads only",
    ))
    out.append((
        "aimc_full_AND", "AI-MC", "flip",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "A=W∧C∧D∧E; all read A — flip",
    ))
    out.append((
        "aimc_full_OR", "AI-MC", "flip",
        [lambda x: x[1], lambda x: x[0] | x[2] | x[3] | x[4],
         lambda x: x[1], lambda x: x[1], lambda x: x[1]],
        "A=W∨C∨D∨E; all read A — flip",
    ))
    out.append((
        "aimc_drop_E_ro", "AI-MC", "drop",
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        "from full AND: E removed from A, still reads",
    ))
    return out


def run_family(forms, labels, by_name, rows):
    for name, family, rung, rules, basis in forms:
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
        }
        rows.append(row)
        by_name[name] = row
        print(
            f"  {name:<22} [{rung}]  whole={v.structure}/{v.max_phi:.3f}  "
            f"core={core_t} Φ={cphi_f:.3f} n_core={len(core_t)}"
        )


def main():
    print("CMC / AI-MC ENCODING LADDERS AT n=5 — vs HMC FULL_JOINT_FLIP")
    print("=" * 80)
    print("  cited: encoding_ladder_n5; hmc_algo_boundary; constructs_n_gt3")
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
    by_name = {}
    t_all = time.time()

    print("CMC LADDER")
    print("-" * 80)
    run_family(cmc_forms(), LC, by_name, rows)
    print()
    print("AI-MC LADDER")
    print("-" * 80)
    run_family(aimc_forms(), LA, by_name, rows)
    print()

    # H1 CMC classical
    chain = by_name["cmc_chain"]
    echo = by_name["cmc_echo"]
    h1 = (
        ctrl
        and chain["structure"] == "dyadic"
        and echo["structure"] == "dyadic"
        and chain["n_core"] <= 2
        and echo["n_core"] <= 2
    )

    # H2 AI-MC baseline
    rew = by_name["aimc_rewrite"]
    h2 = (
        rew["structure"] == "dyadic"
        and rew["n_core"] >= 3
        and rew["core_phi"] > PHI_EPS
    )

    # H3 full flip both families
    def is_flip(row):
        return (
            row["structure"] == "triadic"
            and row["n_core"] == N
            and abs(row["core_phi"] - N_MINUS_1) < PHI_EPS
        )

    h3 = (
        is_flip(by_name["cmc_full_AND"])
        and is_flip(by_name["cmc_full_OR"])
        and is_flip(by_name["aimc_full_AND"])
        and is_flip(by_name["aimc_full_OR"])
    )

    # H4 COMMIT_READ
    cmc_ero = by_name["cmc_E_reads"]
    aimc_ero = by_name["aimc_E_reads"]
    cmc_drop = by_name["cmc_drop_E_ro"]
    aimc_drop = by_name["aimc_drop_E_ro"]
    h4 = (
        "E" not in cmc_ero["core"].split("|")
        and "E" not in aimc_ero["core"].split("|")
        and "E" not in cmc_drop["core"].split("|")
        and "E" not in aimc_drop["core"].split("|")
        and cmc_drop["n_core"] == 4
        and aimc_drop["n_core"] == 4
        and cmc_drop["structure"] == "dyadic"
        and aimc_drop["structure"] == "dyadic"
    )

    # H5 pre-boundary not flip; boundary = last party
    cmc_pre = by_name["cmc_pre_AND"]
    aimc_pre = by_name["aimc_pre_AND"]
    h5 = (
        cmc_pre["structure"] == "dyadic"
        and aimc_pre["structure"] == "dyadic"
        and cmc_pre["n_core"] == 4
        and aimc_pre["n_core"] == 4
        and "E" not in cmc_pre["core"].split("|")
        and "E" not in aimc_pre["core"].split("|")
        and h3
    )

    if h1 and h2 and h3 and h4 and h5:
        verdict_word = "BOUNDARY_TRANSFERS"
        reading = (
            "BOUNDARY_TRANSFERS — CMC and AI-MC ladders share HMC’s "
            "last-party commit flip (whole triadic Φ=4, n_core=5) and "
            "COMMIT_READ; classical convey/transform baselines stay "
            "non-algo / ≥3-core-dyadic respectively"
        )
        boundary_step = "pre_AND → full_AND (CMC and AI-MC)"
    elif h3 and h5 and not (h1 and h2):
        verdict_word = "FLIP_ONLY"
        reading = "FLIP_ONLY — flip transfers; baselines morph"
        boundary_step = "full_AND"
    elif h1 and h2 and not h3:
        verdict_word = "BOUNDARY_MORPHS"
        reading = "BOUNDARY_MORPHS — baselines hold; flip fails on a family"
        boundary_step = "morphed"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — construct ladders incomplete"
        boundary_step = "unknown"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  CMC chain n_core={chain['n_core']} echo n_core={echo['n_core']}")
    print(f"  AI-MC rewrite whole={rew['structure']} n_core={rew['n_core']} "
          f"Φ={rew['core_phi']:.3f}")
    print(f"  CMC pre={cmc_pre['structure']}/{cmc_pre['n_core']}  "
          f"full_AND={by_name['cmc_full_AND']['structure']}/"
          f"{by_name['cmc_full_AND']['core_phi']:.0f}")
    print(f"  AI-MC pre={aimc_pre['structure']}/{aimc_pre['n_core']}  "
          f"full_AND={by_name['aimc_full_AND']['structure']}/"
          f"{by_name['aimc_full_AND']['core_phi']:.0f}")
    print(f"  H1 (CMC classical non-algo):              "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (AI-MC ≥3-core boundary, whole dyadic): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (full joint flip Φ=n−1 both families):  "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (COMMIT_READ transfers):               "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (boundary step transfers):             "
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
            "name", "family", "rung", "structure", "whole_phi", "core",
            "core_phi", "n_core", "basis",
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
