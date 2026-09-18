"""Seal GATE_REGIMES_TRANSFER: XNOR + AND_negE on CMC (AI-MC) at n=5.

Hypotheses fixed in hypotheses.md before computing.
Extends construct_gates_n5, ladder_gate_properties, CONSTRUCT_LADDER_ARC.

Run:  python org_frontier/studies/construct_gates_seal/analyze_seal.py
"""

from __future__ import annotations

import csv
import math
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

# HMC anchors cited (not re-run)
HMC_ANCHORS = {
    "XNOR": {"regime": "B", "phi": 0.125, "source": "encoding_ladder_gates"},
    "AND_negC": {"regime": "C", "phi": float("nan"), "source": "ladder_gate_properties"},
}

GATES = ("XNOR", "AND_negE")
FAMILY_PREFIX = {"CMC": "cmc", "AI-MC": "aimc"}


def gate_fn(gname, a, b, c, d):
    if gname == "XNOR":
        return 1 - (a ^ b ^ c ^ d)
    if gname == "AND_negE":
        # mixed-polarity extremal: AND of outers with last negated
        return a & b & c & (1 - d)
    raise ValueError(gname)


def full_cell(family, labels, gname, mediator_idx=1):
    prefix = FAMILY_PREFIX[family]
    outers = [i for i in range(len(labels)) if i != mediator_idx]
    assert len(outers) == 4

    def med(x, g=gname):
        return gate_fn(g, x[outers[0]], x[outers[1]],
                       x[outers[2]], x[outers[3]])

    rules = []
    for i in range(len(labels)):
        if i == mediator_idx:
            rules.append(med)
        else:
            rules.append(lambda x, m=mediator_idx: x[m])
    note = {
        "XNOR": f"{labels[mediator_idx]}=¬⊕ outers; all read",
        "AND_negE": f"{labels[mediator_idx]}=W∧…∧¬last; all read",
    }[gname]
    return (
        f"{prefix}_{gname}_full", family, gname, "full", rules, note,
    )


def classify(row):
    if (
        row["structure"] == "triadic"
        and row["n_core"] == N
        and abs(row["core_phi"] - N_MINUS_1) < PHI_EPS
    ):
        return "A", True
    if (
        row["structure"] == "triadic"
        and row["n_core"] == N
        and row["core_phi"] < 1.0
    ):
        return "B", True
    return "C", False


def main():
    print("CONSTRUCT GATE SEAL — XNOR + AND_negE (n=5)")
    print("=" * 80)
    print("  cited: construct_gates_n5 GATE_REGIMES_TRANSFER; "
          "encoding_ladder_gates; ladder_gate_properties")
    print("  synthesis: CONSTRUCT_LADDER_ARC.md")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  cells: CMC + AI-MC × {list(GATES)}")
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

    print("HMC ANCHORS (cited)")
    print("-" * 80)
    for g, a in HMC_ANCHORS.items():
        phi_s = "—" if math.isnan(a["phi"]) else str(a["phi"])
        print(f"  HMC {g}: regime={a['regime']} Φ={phi_s}  ({a['source']})")
    print()

    rows = []
    by_name = {}
    t_all = time.time()

    for family, labels in (("CMC", LC), ("AI-MC", LA)):
        print(f"{family}")
        print("-" * 80)
        for gname in GATES:
            name, fam, gate, rung, rules, basis = full_cell(
                family, labels, gname
            )
            t0 = time.time()
            v = verdict(list(rules), labels)
            core, cphi = major_complex(list(rules), labels)
            core_t = tuple(core) if core else ()
            cphi_f = (
                float(cphi) if cphi is not None and cphi >= 0 else float("nan")
            )
            row = {
                "name": name,
                "family": fam,
                "gate": gate,
                "rung": rung,
                "structure": v.structure,
                "whole_phi": float(v.max_phi),
                "core": "|".join(core_t),
                "core_phi": cphi_f,
                "n_core": len(core_t),
                "basis": basis,
                "elapsed_s": round(time.time() - t0, 1),
            }
            regime, flipped = classify(row)
            row["regime"] = regime
            row["flipped"] = flipped
            rows.append(row)
            by_name[name] = row
            phi_s = f"{cphi_f:.3f}" if not math.isnan(cphi_f) else "nan"
            print(
                f"  {name:<24} whole={v.structure}/{v.max_phi:.3f}  "
                f"core={core_t} Φ={phi_s} n_core={len(core_t)}  "
                f"regime={regime}  t={row['elapsed_s']}s"
            )
        print()

    xnor_ok = all(
        by_name[f"{p}_XNOR_full"]["regime"] == "B"
        for p in ("cmc", "aimc")
    )
    neg_ok = all(
        by_name[f"{p}_AND_negE_full"]["regime"] == "C"
        for p in ("cmc", "aimc")
    )

    h1 = ctrl and xnor_ok
    h2 = ctrl and neg_ok
    h3 = ctrl and not (xnor_ok and neg_ok)

    if h1 and h2 and not h3:
        verdict_word = "GATE_SEAL_HOLDS"
        reading = (
            "GATE_SEAL_HOLDS — CMC/AI-MC XNOR→B (Φ≪n−1), AND_negE→C; "
            "GATE_REGIMES_TRANSFER sealed; construct/gate arc closable"
        )
    elif h3:
        failed = []
        if not xnor_ok:
            failed.append("XNOR")
        if not neg_ok:
            failed.append("AND_negE")
        verdict_word = "GATE_SEAL_BREAKS"
        reading = f"GATE_SEAL_BREAKS — morph on: {'/'.join(failed)}"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — gate seal incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    for pref, label in (("cmc", "CMC"), ("aimc", "AI-MC")):
        for g in GATES:
            r = by_name[f"{pref}_{g}_full"]
            phi_s = (
                f"{r['core_phi']:.3f}"
                if not math.isnan(r["core_phi"]) else "nan"
            )
            print(
                f"  {label} {g}: regime={r['regime']} "
                f"Φ={phi_s} n_core={r['n_core']} whole={r['structure']}"
            )
    print(f"  H1 (XNOR → Regime B):       "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (AND_negE → Regime C):   "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (surprise flip / morph): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "name", "family", "gate", "rung", "structure", "whole_phi",
            "core", "core_phi", "n_core", "regime", "flipped", "basis",
            "elapsed_s",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "family": r["family"],
                "gate": r["gate"],
                "rung": r["rung"],
                "structure": r["structure"],
                "whole_phi": f"{r['whole_phi']:.6f}",
                "core": r["core"],
                "core_phi": (
                    f"{r['core_phi']:.6f}"
                    if not math.isnan(r["core_phi"]) else ""
                ),
                "n_core": r["n_core"],
                "regime": r["regime"],
                "flipped": r["flipped"],
                "basis": r["basis"],
                "elapsed_s": r["elapsed_s"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
