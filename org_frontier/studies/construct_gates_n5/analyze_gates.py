"""CMC / AI-MC non-monotone full-bind at n=5 vs HMC GATE_SPLITS.

AND control + XOR + MAJ (≥3/4). Hypotheses fixed in hypotheses.md.
Extends encoding_ladder_gates, construct_ladders_n5, CONSTRUCT_LADDER_ARC.

Run:  python org_frontier/studies/construct_gates_n5/analyze_gates.py
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
# HMC anchors from encoding_ladder_gates FINDINGS (cited, not re-run)
HMC_ANCHORS = {
    "AND": {"regime": "A", "flip": True, "phi": 4.0},
    "XOR": {"regime": "B", "flip": True, "phi": 0.125},
    "MAJ": {"regime": "C", "flip": False, "phi": float("nan")},
}


def _maj4(a, b, c, d, k=3):
    return 1 if (a + b + c + d) >= k else 0


def gate_fn(gname, a, b, c, d):
    if gname == "AND":
        return a & b & c & d
    if gname == "XOR":
        return a ^ b ^ c ^ d
    if gname == "MAJ":
        return _maj4(a, b, c, d, k=3)
    raise ValueError(gname)


def full_forms(family, labels, mediator_idx=1):
    """Full-bind: mediator = gate(all outers); every node reads mediator."""
    out = []
    # outers are all indices except mediator
    outers = [i for i in range(len(labels)) if i != mediator_idx]
    assert len(outers) == 4
    for gname in ("AND", "XOR", "MAJ"):
        def make_rules(g=gname):
            def med(x, g=g):
                return gate_fn(g, x[outers[0]], x[outers[1]],
                               x[outers[2]], x[outers[3]])
            rules = []
            for i in range(len(labels)):
                if i == mediator_idx:
                    rules.append(med)
                else:
                    rules.append(lambda x, m=mediator_idx: x[m])
            return rules

        note = {
            "AND": f"{labels[mediator_idx]}=∧ of outers; all read",
            "XOR": f"{labels[mediator_idx]}=⊕ of outers; all read",
            "MAJ": f"{labels[mediator_idx]}=maj≥3/4; all read",
        }[gname]
        out.append((
            f"{family.lower()}_{gname}_full", family, gname, "full",
            make_rules(), note,
        ))
    return out


def classify(row):
    """Return regime letter and flip bool from a full-bind row."""
    flip = (
        row["structure"] == "triadic"
        and row["n_core"] == N
        and abs(row["core_phi"] - N_MINUS_1) < PHI_EPS
    )
    # Regime A: flip with Φ≈n−1
    if (
        row["structure"] == "triadic"
        and row["n_core"] == N
        and abs(row["core_phi"] - N_MINUS_1) < PHI_EPS
    ):
        return "A", True
    # Regime B: flip with Φ≪1
    if (
        row["structure"] == "triadic"
        and row["n_core"] == N
        and row["core_phi"] < 1.0
    ):
        return "B", True
    # Regime C: no flip
    return "C", False


def main():
    print("CONSTRUCT GATE TRANSFER AT n=5 — CMC / AI-MC vs HMC anchors")
    print("=" * 80)
    print("  cited: encoding_ladder_gates GATE_SPLITS_LADDER; "
          "construct_ladders_n5 BOUNDARY_TRANSFERS")
    print("  synthesis: CONSTRUCT_LADDER_ARC.md")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  n={N}  n−1={N_MINUS_1}  gates: AND, XOR, MAJ")
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

    print("HMC ANCHORS (cited from encoding_ladder_gates)")
    print("-" * 80)
    for g, a in HMC_ANCHORS.items():
        phi_s = "—" if math.isnan(a["phi"]) else f"{a['phi']}"
        print(f"  HMC {g}: regime={a['regime']} flip={a['flip']} Φ={phi_s}")
    print()

    rows = []
    by_name = {}
    t_all = time.time()

    for family, labels in (("CMC", LC), ("AI-MC", LA)):
        print(f"{family} FULL-BIND")
        print("-" * 80)
        for name, fam, gate, rung, rules, basis in full_forms(family, labels):
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
            phi_s = (
                f"{cphi_f:.3f}" if not math.isnan(cphi_f) else "nan"
            )
            print(
                f"  {name:<22} whole={v.structure}/{v.max_phi:.3f}  "
                f"core={core_t} Φ={phi_s} n_core={len(core_t)}  "
                f"regime={regime}  t={row['elapsed_s']}s"
            )
        print()

    # Hypothesis evaluation
    def family_gate(fam_prefix, gate):
        return by_name[f"{fam_prefix}_{gate}_full"]

    xor_ok = True
    maj_ok = True
    for pref in ("cmc", "aimc"):
        xr = family_gate(pref, "XOR")
        mj = family_gate(pref, "MAJ")
        an = family_gate(pref, "AND")
        # AND sanity: must be A
        and_a = an["regime"] == "A"
        if not and_a:
            print(f"  WARN: {pref} AND not Regime A ({an['regime']})")
        xor_ok = xor_ok and xr["regime"] == "B"
        maj_ok = maj_ok and mj["regime"] == "C"

    h1 = ctrl and xor_ok
    h2 = ctrl and maj_ok
    h3 = ctrl and not (xor_ok and maj_ok)

    if h1 and h2 and not h3:
        verdict_word = "GATE_REGIMES_TRANSFER"
        reading = (
            "GATE_REGIMES_TRANSFER — CMC/AI-MC full-bind: XOR→B (Φ≪n−1), "
            "MAJ→C (no flip), AND→A; HMC GATE_SPLITS regimes transfer"
        )
    elif h3:
        failed = []
        if not xor_ok:
            failed.append("XOR")
        if not maj_ok:
            failed.append("MAJ")
        verdict_word = "GATE_REGIME_MORPHS"
        reading = (
            f"GATE_REGIME_MORPHS — non-transferring: {'/'.join(failed)}"
        )
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — construct gate transfer incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    for pref, label in (("cmc", "CMC"), ("aimc", "AI-MC")):
        for g in ("AND", "XOR", "MAJ"):
            r = family_gate(pref, g)
            phi_s = (
                f"{r['core_phi']:.3f}"
                if not math.isnan(r["core_phi"]) else "nan"
            )
            print(
                f"  {label} {g}: regime={r['regime']} "
                f"flip={r['flipped']} Φ={phi_s} "
                f"n_core={r['n_core']} whole={r['structure']}"
            )
    print(f"  H1 (XOR → Regime B both):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (MAJ → Regime C both):  "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (some family morphs):   "
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
