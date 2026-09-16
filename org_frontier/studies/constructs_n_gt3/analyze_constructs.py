"""HMC / CMC / AI-MC constructs at n>3 — exact Φ scale arm of #42.

Designed forms from lab definitions (discriminant_boundaries / probes 15–20).
Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/constructs_n_gt3/analyze_constructs.py
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


def _id(i):
    return lambda x, i=i: x[i]


def forms():
    """Designed construct forms at n=4 and n=5."""
    out = []

    # ---- HMC: W↔S machine partner; extra parties unconstituted / idle ----
    out.append((
        "hmc_pad4", "HMC", 4, ("W", "S", "C", "D"),
        [
            lambda x: x[1],
            lambda x: x[0],
            lambda x: x[2],
            lambda x: x[3],
        ],
        "W↔S loop; C,D idle (unconstituted)",
    ))
    out.append((
        "hmc_pad5", "HMC", 5, ("W", "S", "C", "D", "E"),
        [
            lambda x: x[1],
            lambda x: x[0],
            lambda x: x[2],
            lambda x: x[3],
            lambda x: x[4],
        ],
        "W↔S loop; C,D,E idle",
    ))
    # parallel HMC: two workers each loop with S, no cross-commit
    out.append((
        "hmc_parallel4", "HMC", 4, ("W1", "S", "W2", "D"),
        [
            lambda x: x[1],          # W1 ← S
            lambda x: x[0] | x[2],   # S ← W1 or W2 (assist, not joint commit)
            lambda x: x[1],          # W2 ← S
            lambda x: x[3],          # idle
        ],
        "two workers chat with S; S ORs them (no ∧ commit)",
    ))

    # ---- CMC: convey chains / relays ----
    out.append((
        "cmc_chain4", "CMC", 4, ("W", "S", "C", "D"),
        [
            lambda x: x[0],
            lambda x: x[0],
            lambda x: x[1],
            lambda x: x[2],
        ],
        "W→S→C→D one-way conveyor",
    ))
    out.append((
        "cmc_echo4", "CMC", 4, ("W", "S", "C", "D"),
        [
            lambda x: x[1],
            lambda x: x[0],
            lambda x: x[1],
            lambda x: x[3],
        ],
        "S echoes W; C reads S; D idle",
    ))
    out.append((
        "cmc_chain5", "CMC", 5, ("W", "S1", "S2", "C", "D"),
        [
            lambda x: x[0],
            lambda x: x[0],
            lambda x: x[1],
            lambda x: x[2],
            lambda x: x[3],
        ],
        "W→S1→S2→C→D conveyor depth",
    ))

    # ---- AI-MC: transform on sender's side ----
    # n=3 pattern W'=C, A'=W, C'=A padded
    out.append((
        "aimc_rewrite4", "AI-MC", 4, ("W", "A", "C", "D"),
        [
            lambda x: x[2],
            lambda x: x[0],
            lambda x: x[1],
            lambda x: x[3],
        ],
        "W→A→C rewrite loop; D idle (n=3 AI-MC lift)",
    ))
    out.append((
        "aimc_blend4", "AI-MC", 4, ("W", "A", "C", "D"),
        [
            lambda x: x[2],
            lambda x: x[0] | x[2],
            lambda x: x[1],
            lambda x: x[3],
        ],
        "A blends W with C-context; still sender-side",
    ))
    out.append((
        "aimc_dual5", "AI-MC", 5, ("W", "A1", "A2", "C", "D"),
        [
            lambda x: x[3],
            lambda x: x[0],
            lambda x: x[1],
            lambda x: x[2],
            lambda x: x[4],
        ],
        "W→A1→A2→C transform chain; D idle",
    ))

    # ---- Algorithmacy controls ----
    out.append((
        "algo_joint4", "ALGO", 4, ("W", "S", "C", "D"),
        [
            lambda x: x[1],
            lambda x: x[0] & x[2],
            lambda x: x[1],
            lambda x: x[3],
        ],
        "faithful triad + idle D",
    ))
    out.append((
        "algo_joint5", "ALGO", 5, ("W", "S", "C", "D", "E"),
        [
            lambda x: x[1],
            lambda x: x[0] & x[2],
            lambda x: x[1],
            lambda x: x[3],
            lambda x: x[4],
        ],
        "faithful triad + idle D,E",
    ))
    out.append((
        "algo_multiparty4", "ALGO", 4, ("W", "S", "C1", "C2"),
        [
            lambda x: x[1],
            lambda x: x[0] & x[2] & x[3],
            lambda x: x[1],
            lambda x: x[1],
        ],
        "S commits over W∧C1∧C2; all read S",
    ))
    return out


def main():
    print("CONSTRUCTS HMC/CMC/AI-MC AT n>3 — #42 construct arm")
    print("=" * 80)
    print("  cited: discriminant_boundaries; probes 15/19/20; OMIT_ATOM_ARC")
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
    print("CENSUS")
    print("-" * 80)
    for name, fam, n, labels, rules, basis in forms():
        v = verdict(list(rules), labels)
        core, cphi = major_complex(list(rules), labels)
        core_t = tuple(core) if core else ()
        cphi_f = float(cphi) if cphi is not None and cphi >= 0 else float("nan")
        row = {
            "name": name,
            "family": fam,
            "n": n,
            "structure": v.structure,
            "whole_phi": float(v.max_phi),
            "core": "|".join(core_t),
            "core_phi": cphi_f,
            "n_core": len(core_t),
            "basis": basis,
        }
        rows.append(row)
        print(
            f"  {name:<18} [{fam:<5}] n={n}  whole={v.structure}/{v.max_phi:.3f}  "
            f"core={core_t} Φ={cphi_f:.3f} n_core={len(core_t)}"
        )
    print()

    def fam_rows(fam):
        return [r for r in rows if r["family"] == fam]

    hmc = fam_rows("HMC")
    cmc = fam_rows("CMC")
    aimc = fam_rows("AI-MC")
    algo = fam_rows("ALGO")

    # H1: HMC cores are 2-party (or smaller) — not ≥3 algorithmacy cores
    h1 = ctrl and all(r["n_core"] <= 2 for r in hmc)

    # H2: CMC wholes factor (Φ_MIP≈0) OR n_core<=2 without joint-commit
    h2 = all(
        abs(r["whole_phi"]) < PHI_EPS or r["n_core"] <= 2
        for r in cmc
    )

    # H3: some AI-MC has n_core>=3 and core_phi>0
    h3 = any(r["n_core"] >= 3 and r["core_phi"] > PHI_EPS for r in aimc)

    # H4: algo controls have core_phi>0 and n_core>=3
    h4 = all(r["core_phi"] > PHI_EPS and r["n_core"] >= 3 for r in algo)

    if h1 and h2 and h3 and h4:
        verdict_word = "CONSTRUCTS_HOLD"
        reading = (
            "CONSTRUCTS_HOLD — HMC stays ≤2-core; CMC non-commit; "
            "AI-MC boundary (n_core≥3) persists; algorithmacy controls irreducible"
        )
    elif h1 and h2 and h4 and not h3:
        verdict_word = "BOUNDARY_COLLAPSES"
        reading = (
            "BOUNDARY_COLLAPSES — HMC/CMC/ALGO hold; AI-MC loses ≥3-core at n>3"
        )
    elif not h1 or not h2:
        verdict_word = "SCALE_BLURS_CONSTRUCTS"
        reading = (
            "SCALE_BLURS_CONSTRUCTS — HMC or CMC reads as algorithmacy-like at n>3"
        )
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — mixed construct scale results"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  HMC n_cores={[r['n_core'] for r in hmc]}")
    print(f"  CMC whole_Φ={[round(r['whole_phi'],3) for r in cmc]}  "
          f"n_cores={[r['n_core'] for r in cmc]}")
    print(f"  AI-MC n_cores={[r['n_core'] for r in aimc]}  "
          f"core_Φ={[round(r['core_phi'],3) for r in aimc]}")
    print(f"  ALGO n_cores={[r['n_core'] for r in algo]}  "
          f"core_Φ={[round(r['core_phi'],3) for r in algo]}")
    print(f"  H1 (HMC ≤2-core / non-algorithmacy): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (CMC non-commit at n>3):          "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (AI-MC ≥3-core boundary persists): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (algorithmacy controls irreducible): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  vs omit-atom picture: constructs track commit/convey party roles; "
          f"omit atoms track digraph motifs — complementary, not the same axis")
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
            "name", "family", "n", "structure", "whole_phi", "core",
            "core_phi", "n_core", "basis",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "family": r["family"],
                "n": r["n"],
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
