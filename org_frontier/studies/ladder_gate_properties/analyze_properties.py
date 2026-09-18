"""Boolean-property classifier for ladder-gate regimes A/B/C.

Designed gates spanning property space at n=5; anchors from
encoding_ladder_gates. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/ladder_gate_properties/analyze_properties.py
"""

from __future__ import annotations

import csv
import itertools
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
N_OUT = 4
WT_EXTREMAL = {1, (1 << N_OUT) - 1}  # {1, 15}


def _props(fn):
    """Boolean properties of a 4-input gate fn(a,b,c,d)."""
    wt = sum(fn(*bits) for bits in itertools.product([0, 1], repeat=4))
    dep = []
    for i in range(4):
        differs = False
        for bits in itertools.product([0, 1], repeat=4):
            b2 = list(bits)
            b2[i] = 1 - b2[i]
            if fn(*bits) != fn(*b2):
                differs = True
                break
        dep.append(differs)
    mono_inc, mono_dec = [], []
    for i in range(4):
        inc = dec = True
        for bits in itertools.product([0, 1], repeat=4):
            if bits[i] == 1:
                continue
            lo = list(bits)
            hi = list(bits)
            hi[i] = 1
            if fn(*hi) < fn(*lo):
                inc = False
            if fn(*hi) > fn(*lo):
                dec = False
        mono_inc.append(inc)
        mono_dec.append(dec)
    unate = all(mono_inc[i] or mono_dec[i] for i in range(4))
    monotone = all(mono_inc) or all(mono_dec)
    # affine over GF(2)
    fz = fn(0, 0, 0, 0)
    affine = True
    for x in itertools.product([0, 1], repeat=4):
        for y in itertools.product([0, 1], repeat=4):
            xy = tuple(x[i] ^ y[i] for i in range(4))
            if fn(*x) ^ fn(*y) ^ fz ^ fn(*xy):
                affine = False
                break
        if not affine:
            break
    canal = False
    for i in range(4):
        for val in (0, 1):
            outs = {
                fn(*bits)
                for bits in itertools.product([0, 1], repeat=4)
                if bits[i] == val
            }
            if len(outs) == 1:
                canal = True
                break
        if canal:
            break
    return {
        "wt": wt,
        "all_dep": all(dep),
        "monotone": monotone,
        "unate": unate,
        "affine": affine,
        "canalizing": canal,
        "extremal_wt": wt in WT_EXTREMAL,
    }


def _predict(p):
    """Proposed minimal rule."""
    if p["all_dep"] and p["affine"]:
        return "B"
    if p["all_dep"] and p["monotone"] and p["extremal_wt"]:
        return "A"
    return "C"


def _assist2(fn):
    """2-arg assist restriction: freeze unused inputs to 0 or 1;
    prefer a restriction that depends on both W1 and W2."""
    def dep2(g):
        d0 = g(0, 0) != g(1, 0) or g(0, 1) != g(1, 1)
        d1 = g(0, 0) != g(0, 1) or g(1, 0) != g(1, 1)
        return d0 and d1

    cands = [
        lambda a, b, f=fn: f(a, b, 0, 0),
        lambda a, b, f=fn: f(a, b, 1, 1),
        lambda a, b, f=fn: f(a, b, 0, 1),
        lambda a, b, f=fn: f(a, b, 1, 0),
    ]
    chosen = next((g for g in cands if dep2(g)), cands[0])
    return lambda x, g=chosen: g(x[0], x[2])


# (name, fn, anchor?)
GATES = [
    # anchors from encoding_ladder_gates (+ NOR)
    ("AND", lambda a, b, c, d: a & b & c & d, True),
    ("OR", lambda a, b, c, d: a | b | c | d, True),
    ("NAND", lambda a, b, c, d: 1 - (a & b & c & d), True),
    ("NOR", lambda a, b, c, d: 1 - (a | b | c | d), True),
    ("XOR", lambda a, b, c, d: a ^ b ^ c ^ d, True),
    ("XNOR", lambda a, b, c, d: 1 - (a ^ b ^ c ^ d), True),
    ("MAJ3", lambda a, b, c, d: 1 if a + b + c + d >= 3 else 0, True),
    ("MIXED", lambda a, b, c, d: (a & b) | (c & d), True),
    # property-space probes
    ("T2", lambda a, b, c, d: 1 if a + b + c + d >= 2 else 0, False),
    ("MIN1", lambda a, b, c, d: 1 if a + b + c + d <= 1 else 0, False),
    ("AND_negC", lambda a, b, c, d: a & b & c & (1 - d), False),
    ("OR_negC", lambda a, b, c, d: a | b | c | (1 - d), False),
    ("AND_negAB", lambda a, b, c, d: (1 - a) & (1 - b) & c & d, False),
    ("OR_negAB", lambda a, b, c, d: (1 - a) | (1 - b) | c | d, False),
    ("AND_of_ORs", lambda a, b, c, d: (a | b) & (c | d), False),
    ("XOR3_and_D", lambda a, b, c, d: (a ^ b ^ c) & d, False),
]


def _observed_regime(structure, n_core, core_phi):
    flip = structure == "triadic" and n_core == N
    if flip and abs(core_phi - N_MINUS_1) < PHI_EPS:
        return "A"
    if flip and core_phi < 1.0:
        return "B"
    if not flip:
        return "C"
    return "?"


def main():
    print("LADDER-GATE BOOLEAN PROPERTY CLASSIFIER (n=5)")
    print("=" * 80)
    print("  cited: encoding_ladder_gates GATE_SPLITS_LADDER")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  labels: {L}  n_gates={len(GATES)}")
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
    for name, fn, anchor in GATES:
        p = _props(fn)
        pred = _predict(p)
        sfn = lambda x, f=fn: f(x[0], x[2], x[3], x[4])
        rules = [lambda x: x[1], sfn, lambda x: x[1], lambda x: x[1], lambda x: x[1]]
        t0 = time.time()
        v = verdict(list(rules), L)
        core, cphi = major_complex(list(rules), L)
        core_t = tuple(core) if core else ()
        cphi_f = float(cphi) if cphi is not None and cphi >= 0 else float("nan")
        obs = _observed_regime(v.structure, len(core_t), cphi_f if cphi_f == cphi_f else -1.0)

        # assist secondary
        asfn = _assist2(fn)
        arules = [lambda x: x[1], asfn, lambda x: x[1], lambda x: x[3], lambda x: x[4]]
        va = verdict(list(arules), L)
        acore, acphi = major_complex(list(arules), L)
        acore_t = tuple(acore) if acore else ()
        acphi_f = float(acphi) if acphi is not None and acphi >= 0 else float("nan")
        assist_mp = (
            len(acore_t) >= 3
            and {"W1", "S", "W2"}.issubset(set(acore_t))
        )

        row = {
            "name": name,
            "anchor": int(anchor),
            "wt": p["wt"],
            "all_dep": int(p["all_dep"]),
            "monotone": int(p["monotone"]),
            "unate": int(p["unate"]),
            "affine": int(p["affine"]),
            "canalizing": int(p["canalizing"]),
            "extremal_wt": int(p["extremal_wt"]),
            "pred": pred,
            "obs": obs,
            "match": int(pred == obs),
            "structure": v.structure,
            "whole_phi": float(v.max_phi),
            "core": "|".join(core_t),
            "core_phi": cphi_f,
            "n_core": len(core_t),
            "assist_n_core": len(acore_t),
            "assist_multiparty": int(assist_mp),
            "elapsed_s": round(time.time() - t0, 1),
        }
        rows.append(row)
        mark = "✓" if pred == obs else "✗"
        print(
            f"  {name:<14} obs={obs} pred={pred} {mark}  "
            f"Φ={cphi_f if cphi_f == cphi_f else float('nan'):7.3f}  "
            f"wt={p['wt']:2} mono={p['monotone']} aff={p['affine']} "
            f"canal={p['canalizing']} ext={p['extremal_wt']}  "
            f"asst_mp={assist_mp}  t={row['elapsed_s']}s"
        )
    print()

    # Hypothesis tests
    by_name = {r["name"]: r for r in rows}
    matches = all(r["match"] for r in rows)

    # H1: A iff monotone ∧ extremal_wt ∧ all_dep
    h1 = True
    for r in rows:
        props_A = bool(r["all_dep"] and r["monotone"] and r["extremal_wt"])
        if (r["obs"] == "A") != props_A:
            h1 = False
            break
    h1 = h1 and ctrl

    # H2: B iff affine ∧ all_dep
    h2 = True
    for r in rows:
        props_B = bool(r["all_dep"] and r["affine"])
        if (r["obs"] == "B") != props_B:
            h2 = False
            break
    h2 = h2 and ctrl

    # H3: non-A-non-B → C
    h3 = True
    for r in rows:
        props_C = not (
            (r["all_dep"] and r["affine"])
            or (r["all_dep"] and r["monotone"] and r["extremal_wt"])
        )
        if props_C and r["obs"] != "C":
            h3 = False
            break
    h3 = h3 and ctrl

    # H4: weaker filters fail to characterize A
    # canalizing alone
    canal_eq_A = all(
        (bool(r["canalizing"]) == (r["obs"] == "A")) for r in rows
    )
    # extremal wt alone
    ext_eq_A = all(
        (bool(r["extremal_wt"]) == (r["obs"] == "A")) for r in rows
    )
    # unate ∧ canal ∧ extremal (no monotone)
    weak_eq_A = all(
        (
            bool(r["unate"] and r["canalizing"] and r["extremal_wt"])
            == (r["obs"] == "A")
        )
        for r in rows
    )
    # H4 SUPPORTED means weaker filters do NOT predict A (i.e. those eqs fail)
    h4 = ctrl and (not canal_eq_A) and (not ext_eq_A) and (not weak_eq_A)

    # Counterexamples to weaker rules
    weak_ce = [
        r["name"] for r in rows
        if r["unate"] and r["canalizing"] and r["extremal_wt"] and r["obs"] != "A"
    ]

    if h1 and h2 and h3 and matches:
        verdict_word = "MONO_EXTREMAL_VS_AFFINE"
        reading = (
            "MONO_EXTREMAL_VS_AFFINE — A iff monotone∧wt∈{1,15}∧alldep; "
            "B iff affine∧alldep; else C; weaker canal/weight rules fail "
            f"(CE: {'/'.join(weak_ce) if weak_ce else '∅'})"
        )
    elif matches:
        verdict_word = "RULE_FITS"
        reading = "RULE_FITS — proposed rule matches all gates; hypothesis bundle incomplete"
    else:
        verdict_word = "PARTIAL"
        mismatches = [r["name"] for r in rows if not r["match"]]
        reading = f"PARTIAL — rule mismatches: {'/'.join(mismatches)}"

    n_match = sum(r["match"] for r in rows)
    print("PROPERTY → REGIME")
    print("-" * 80)
    print(f"  {'gate':<14} {'obs':<4} {'pred':<4} mono aff canal ext wt  asst")
    for r in rows:
        print(
            f"  {r['name']:<14} {r['obs']:<4} {r['pred']:<4} "
            f"{r['monotone']}    {r['affine']}   {r['canalizing']}     "
            f"{r['extremal_wt']}   {r['wt']:<2}  {r['assist_multiparty']}"
        )
    print(f"  classifier accuracy: {n_match}/{len(rows)}")
    print(f"  weak-rule counterexamples (unate∧canal∧ext but not A): {weak_ce}")
    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (A ↔ monotone∧extremal∧alldep):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (B ↔ affine∧alldep):             "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (residual → C):                  "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (weaker props fail to predict A): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  accuracy: {n_match}/{len(rows)}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = list(rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["whole_phi"] = f"{r['whole_phi']:.6f}"
            out["core_phi"] = f"{r['core_phi']:.6f}"
            w.writerow(out)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "verdict": verdict_word,
            "accuracy": f"{n_match}/{len(rows)}",
            "weak_ce": "|".join(weak_ce),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
