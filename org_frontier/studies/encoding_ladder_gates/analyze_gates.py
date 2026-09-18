"""Encoding ladder gate-family robustness at n=5.

Swap S’s determination gate across AND/OR/NAND/XOR/XNOR/MAJ/MIXED.
Hypotheses fixed in hypotheses.md before computing.
Extends encoding_ladder_n5 FULL_JOINT_FLIP / encoding_ladder_n6 PHI_TRACKS_NM1.

Run:  python org_frontier/studies/encoding_ladder_gates/analyze_gates.py
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
N = len(L)
N_MINUS_1 = N - 1  # 4


def _maj(*bits, k):
    return 1 if sum(bits) >= k else 0


# Gate: (name, s_from_outers(w1,w2,w3,c) -> bit, note)
GATES = [
    ("AND", lambda a, b, c, d: a & b & c & d, "S=W1∧W2∧W3∧C"),
    ("OR", lambda a, b, c, d: a | b | c | d, "S=W1∨W2∨W3∨C"),
    ("NAND", lambda a, b, c, d: 1 - (a & b & c & d), "S=¬(W1∧W2∧W3∧C)"),
    ("XOR", lambda a, b, c, d: a ^ b ^ c ^ d, "S=W1⊕W2⊕W3⊕C"),
    ("XNOR", lambda a, b, c, d: 1 - (a ^ b ^ c ^ d), "S=¬(W1⊕W2⊕W3⊕C)"),
    ("MAJ", lambda a, b, c, d: _maj(a, b, c, d, k=3), "S=maj≥3/4"),
    ("MIXED", lambda a, b, c, d: (a & b) | (c & d), "S=(W1∧W2)∨(W3∧C)"),
]


def forms_for_gate(gname, gate_fn, note):
    """Key rungs: assist_W2, assist_W2W3, workers_Cidle, full, C_ro, drop_C_ro."""
    out = []

    # Assist W2: only W1,W2 in determination — gate restricted to those bits.
    # For 2-input: AND/OR/XOR/NAND/XNOR/MAJ(≥2)/MIXED need sensible 2-ary forms.
    def assist_w2_s(x):
        a, b = x[0], x[2]
        if gname == "AND":
            return a & b
        if gname == "OR":
            return a | b
        if gname == "NAND":
            return 1 - (a & b)
        if gname == "XOR":
            return a ^ b
        if gname == "XNOR":
            return 1 - (a ^ b)
        if gname == "MAJ":
            return 1 if (a + b) >= 2 else 0  # = AND of 2
        if gname == "MIXED":
            return a & b  # first conjunct only
        raise ValueError(gname)

    out.append((
        f"{gname}_assist_W2", gname, "assist_W2",
        [lambda x: x[1], assist_w2_s, lambda x: x[1],
         lambda x: x[3], lambda x: x[4]],
        f"{gname} assist +W2; W3,C idle",
    ))

    def assist_w23_s(x):
        a, b, c = x[0], x[2], x[3]
        if gname == "AND":
            return a & b & c
        if gname == "OR":
            return a | b | c
        if gname == "NAND":
            return 1 - (a & b & c)
        if gname == "XOR":
            return a ^ b ^ c
        if gname == "XNOR":
            return 1 - (a ^ b ^ c)
        if gname == "MAJ":
            return 1 if (a + b + c) >= 2 else 0
        if gname == "MIXED":
            return (a & b) | c  # degenerate mixed
        raise ValueError(gname)

    out.append((
        f"{gname}_assist_W2W3", gname, "assist_W2W3",
        [lambda x: x[1], assist_w23_s, lambda x: x[1],
         lambda x: x[1], lambda x: x[4]],
        f"{gname} assist +W2+W3; C idle",
    ))

    # workers_Cidle = same as assist_W2W3 for 3 workers (pre-boundary)
    out.append((
        f"{gname}_workers_Cidle", gname, "workers_Cidle",
        [lambda x: x[1], assist_w23_s, lambda x: x[1],
         lambda x: x[1], lambda x: x[4]],
        f"{gname} workers bind; C idle (pre-boundary)",
    ))

    # C reads not in commit
    out.append((
        f"{gname}_C_reads", gname, "C_reads",
        [lambda x: x[1], assist_w23_s, lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        f"{gname} workers bind; C reads only",
    ))

    # full joint bind
    def full_s(x):
        return gate_fn(x[0], x[2], x[3], x[4])

    out.append((
        f"{gname}_full", gname, "full",
        [lambda x: x[1], full_s, lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        f"{note}; all read S — flip candidate",
    ))

    # drop C readonly (workers still bound under same gate family)
    out.append((
        f"{gname}_drop_C_ro", gname, "drop_C_ro",
        [lambda x: x[1], assist_w23_s, lambda x: x[1],
         lambda x: x[1], lambda x: x[1]],
        f"{gname} from full: C removed from S, still reads",
    ))
    return out


def main():
    print("ENCODING LADDER — GATE FAMILY ROBUSTNESS (n=5)")
    print("=" * 80)
    print("  cited: encoding_ladder_n5 FULL_JOINT_FLIP; encoding_ladder_n6 PHI_TRACKS_NM1")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  labels: {L}  gates: {[g[0] for g in GATES]}")
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
    by_name = {}
    print("PER-GATE LADDER")
    print("-" * 80)
    for gname, gate_fn, note in GATES:
        for name, gate, rung, rules, basis in forms_for_gate(gname, gate_fn, note):
            t0 = time.time()
            v = verdict(list(rules), L)
            core, cphi = major_complex(list(rules), L)
            core_t = tuple(core) if core else ()
            cphi_f = float(cphi) if cphi is not None and cphi >= 0 else float("nan")
            row = {
                "name": name,
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
            rows.append(row)
            by_name[name] = row
            print(
                f"  {name:<28} whole={v.structure}/{v.max_phi:.3f}  "
                f"core={core_t} Φ={cphi_f:.3f} n_core={len(core_t)}  "
                f"t={row['elapsed_s']}s"
            )
        print()

    # --- Hypothesis evaluation ---
    flip_ok = {}       # gate -> bool whole triadic n_core=5
    phi_nm1 = {}       # gate -> bool Φ≈4
    phi_at_flip = {}   # gate -> phi
    assist_multiparty = {}  # gate -> assist grows n_core>=3 on assist_W2
    commit_read = {}   # gate -> C not in C_reads core; C not in drop core when was in full

    for gname, _, _ in GATES:
        full = by_name[f"{gname}_full"]
        assist = by_name[f"{gname}_assist_W2"]
        workers = by_name[f"{gname}_workers_Cidle"]
        c_ro = by_name[f"{gname}_C_reads"]
        drop = by_name[f"{gname}_drop_C_ro"]

        flip_ok[gname] = (
            full["structure"] == "triadic"
            and full["n_core"] == N
            and set(full["core"].split("|")) == set(L)
        )
        phi_at_flip[gname] = full["core_phi"]
        phi_nm1[gname] = (
            flip_ok[gname]
            and abs(full["core_phi"] - N_MINUS_1) < PHI_EPS
        )
        # AND-like assist: n_core>=3 with W1,S,W2 in core
        core_set = set(assist["core"].split("|")) if assist["core"] else set()
        assist_multiparty[gname] = (
            assist["n_core"] >= 3
            and {"W1", "S", "W2"}.issubset(core_set)
            and assist["structure"] == "dyadic"
        )
        # COMMIT_READ: C out when not in determination
        c_out_reads = "C" not in (c_ro["core"].split("|") if c_ro["core"] else [])
        c_out_drop = "C" not in (drop["core"].split("|") if drop["core"] else [])
        # Only require drop check when full had C in core
        if flip_ok[gname]:
            commit_read[gname] = c_out_reads and c_out_drop
        else:
            commit_read[gname] = c_out_reads  # still: read-without-commit stays out

    # H1: all gates flip with Φ=n−1
    h1 = ctrl and all(phi_nm1[g] for g, _, _ in GATES)

    # H2: some gate stays non-triadic at full bind
    h2 = ctrl and any(not flip_ok[g] for g, _, _ in GATES)

    # H3: some gate's assist path ≠ AND multiparty growth
    and_assist = assist_multiparty["AND"]
    h3 = ctrl and and_assist and any(
        not assist_multiparty[g] for g, _, _ in GATES if g != "AND"
    )

    nm1_gates = [g for g, _, _ in GATES if phi_nm1[g]]
    flip_low_phi = [g for g, _, _ in GATES if flip_ok[g] and not phi_nm1[g]]
    no_flip = [g for g, _, _ in GATES if not flip_ok[g]]
    assist_break = [g for g, _, _ in GATES if not assist_multiparty[g]]

    def _slash(xs):
        return "/".join(xs) if xs else "∅"

    if (not h1) and h2 and h3:
        verdict_word = "GATE_SPLITS_LADDER"
        reading = (
            "GATE_SPLITS_LADDER — AND/OR/NAND: flip Φ=n−1; "
            f"parity {_slash(flip_low_phi)}: flip Φ≪n−1; "
            f"{_slash(no_flip)}: no triadic flip; "
            f"assist breaks on {_slash(assist_break)}"
        )
    elif h1:
        verdict_word = "GATE_ROBUST"
        reading = "GATE_ROBUST — flip + Φ=n−1 across all tested gates"
    elif h2 and not h3:
        verdict_word = "FLIP_GATE_SENSITIVE"
        reading = "FLIP_GATE_SENSITIVE — some gates no flip; assist path stable"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — gate-family ladder incomplete"

    print("PER-GATE SUMMARY")
    print("-" * 80)
    print(f"  {'gate':<8} {'flip':<6} {'Φ':>8} {'=n−1':<6} {'assist≥3':<10} {'COMMIT_READ'}")
    for gname, _, _ in GATES:
        print(
            f"  {gname:<8} {'Y' if flip_ok[gname] else 'N':<6} "
            f"{phi_at_flip[gname]:>8.3f} "
            f"{'Y' if phi_nm1[gname] else 'N':<6} "
            f"{'Y' if assist_multiparty[gname] else 'N':<10} "
            f"{'HOLDS' if commit_read[gname] else 'FAILS'}"
        )
    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (flip + Φ=n−1 robust across gates): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (some gates stay dyadic at full bind): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (assist path changes with gate):       "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  Φ=n−1 gates: {nm1_gates}")
    print(f"  flip Φ≪n−1:  {flip_low_phi}")
    print(f"  no flip:     {no_flip}")
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
            "name", "gate", "rung", "structure", "whole_phi", "core",
            "core_phi", "n_core", "basis", "elapsed_s",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "gate": r["gate"],
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
            "nm1_gates": "|".join(nm1_gates),
            "flip_low_phi": "|".join(flip_low_phi),
            "no_flip": "|".join(no_flip),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
