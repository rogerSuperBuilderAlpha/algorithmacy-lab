"""Agenda #8 — parity vs conjunctive hub under commit flip-noise.

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #6 SMOOTH_DECAY, #7 SAME_THRESHOLD_DIFF_CURVE
(pointers); #115; Q8 prior. Estimation/construct/omit closed.

Run:  python org_frontier/studies/parity_vs_conjunctive_noise/analyze_families.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from functools import reduce

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

GRID = [round(k * 0.01, 2) for k in range(51)]
THRESH_GAP = 0.02
TOL = 1e-6
SIZES = (3, 4)


def conjunctive_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def parity_hub(n):
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def clean_phi_expect(kind, n):
    if kind == "conjunctive":
        return float(n - 1)
    if kind == "parity":
        return 2.0 ** (2 - n)
    raise ValueError(kind)


def noisy_hub_tpm(rules, p):
    clean = tpm_from_rules(rules, n=len(rules))
    tpm = clean.copy()
    tpm[:, 0] = (1.0 - p) * clean[:, 0] + p * (1.0 - clean[:, 0])
    return tpm


def sweep(kind, n):
    build = conjunctive_hub if kind == "conjunctive" else parity_hub
    rules = build(n)
    labels = tuple(f"n{i}" for i in range(n))
    cm = cm_from_rules(rules, n=n)
    rows = []
    for p in GRID:
        tpm = noisy_hub_tpm(rules, p)
        v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
        rows.append({
            "family": kind,
            "n": n,
            "p": p,
            "phi": float(v.max_phi),
            "structure": v.structure,
        })
    return rows


def first_dyadic(rows):
    for r in rows:
        if r["structure"] == "dyadic":
            return r["p"]
    return None


def normalized_series(rows):
    phi0 = rows[0]["phi"]
    if phi0 < TOL:
        phi0 = TOL
    return [(r["p"], r["phi"] / phi0, r["structure"]) for r in rows]


def compare_size(n, conj_rows, par_rows):
    p_c = first_dyadic(conj_rows)
    p_p = first_dyadic(par_rows)
    same = p_c is not None and p_p is not None and abs(p_c - p_p) < 1e-12
    gap = (p_c - p_p) if (p_c is not None and p_p is not None) else float("nan")
    # positive gap => parity flips earlier

    nc = normalized_series(conj_rows)
    np_ = normalized_series(par_rows)
    interior = [
        (pc, pp) for (p, pc, sc), (_, pp, sp) in zip(nc, np_)
        if 0.0 < p < 0.5
    ]
    parity_lower = sum(1 for pc, pp in interior if pp < pc - TOL)
    conj_lower = sum(1 for pc, pp in interior if pc < pp - TOL)
    n_int = len(interior)
    mean_conj_minus_par = (
        sum(pc - pp for pc, pp in interior) / n_int if n_int else float("nan")
    )

    h1_local = (
        p_c is not None and p_p is not None and (p_c - p_p) >= THRESH_GAP
    )
    h2_local = same
    # H3: same p* AND parity lower on ≥ half interior
    h3_local = h2_local and n_int > 0 and parity_lower >= 0.5 * n_int

    return {
        "n": n,
        "p_conjunctive": p_c,
        "p_parity": p_p,
        "gap_conj_minus_par": gap,
        "same_p": same,
        "parity_lower_count": parity_lower,
        "conj_lower_count": conj_lower,
        "n_interior": n_int,
        "mean_hat_conj_minus_par": mean_conj_minus_par,
        "h1": h1_local,
        "h2": h2_local,
        "h3": h3_local,
        "phi0_conj": conj_rows[0]["phi"],
        "phi0_par": par_rows[0]["phi"],
    }


def main():
    print("AGENDA #8 — PARITY VS CONJUNCTIVE UNDER NOISE")
    print("=" * 80)
    print("  cited: #6 SMOOTH_DECAY, #7 SAME_THRESHOLD_DIFF_CURVE (pointers);")
    print("         #115; Q8 prior")
    print("  noise: hub-column flip-noise; forms at n=3,4")
    print("  grid: p=0.00..0.50 step 0.01")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_faithful = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl_faithful else 'FAIL'}")

    ctrl_forms = True
    for n in SIZES:
        for kind in ("conjunctive", "parity"):
            build = conjunctive_hub if kind == "conjunctive" else parity_hub
            rules = build(n)
            labels = tuple(f"n{i}" for i in range(n))
            exp = clean_phi_expect(kind, n)
            v = classify_rules(rules, labels=labels)
            ok = v.structure == "triadic" and abs(v.max_phi - exp) < 1e-6
            tpm0 = noisy_hub_tpm(rules, 0.0)
            cm = cm_from_rules(rules, n=n)
            v0n = classify(tpm0, cm, labels=labels, eps=PHI_EPS)
            ok0 = v0n.structure == "triadic" and abs(v0n.max_phi - exp) < 1e-6
            print(f"  {kind}_n{n}: clean Φ={v.max_phi:.6f} (expect {exp})  "
                  f"{'PASS' if ok and ok0 else 'FAIL'}")
            ctrl_forms = ctrl_forms and ok and ok0
    ctrl = ctrl_faithful and ctrl_forms
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    all_rows = []
    size_stats = {}

    for n in SIZES:
        print(f"SWEEP — n={n}")
        print("-" * 80)
        conj = sweep("conjunctive", n)
        par = sweep("parity", n)
        all_rows.extend(conj)
        all_rows.extend(par)
        st = compare_size(n, conj, par)
        size_stats[n] = st
        print(f"  p*_conj={st['p_conjunctive']}  p*_parity={st['p_parity']}  "
              f"gap(conj−par)={st['gap_conj_minus_par']}")
        print(f"  interior Φ̂: parity_lower={st['parity_lower_count']}/"
              f"{st['n_interior']}  conj_lower={st['conj_lower_count']}/"
              f"{st['n_interior']}  mean(Φ̂_c−Φ̂_p)="
              f"{st['mean_hat_conj_minus_par']:+.4f}")
        print(f"  {'p':>5}  {'Φ_conj':>10}  {'Φ̂_c':>8}  "
              f"{'Φ_par':>10}  {'Φ̂_p':>8}")
        phi0c, phi0p = st["phi0_conj"], st["phi0_par"]
        for a, b in zip(conj, par):
            if abs(a["p"] * 100) % 10 < 1e-9 or a["p"] in (0.0, 0.49, 0.5):
                print(f"  {a['p']:>5.2f}  {a['phi']:>10.6f}  "
                      f"{a['phi']/phi0c:>8.4f}  {b['phi']:>10.6f}  "
                      f"{b['phi']/phi0p:>8.4f}")
        print()

    h1 = ctrl and any(size_stats[n]["h1"] for n in SIZES)
    h2 = ctrl and all(size_stats[n]["h2"] for n in SIZES)
    h3 = ctrl and h2 and all(size_stats[n]["h3"] for n in SIZES)
    if h1 and h2:
        h2 = False

    if h1:
        verdict_word = "PARITY_FASTER_FLIP"
        reading = (
            "PARITY_FASTER_FLIP — parity collapses the verdict at lower p* "
            "than conjunctive at matched n"
        )
    elif h2 and h3:
        verdict_word = "SAME_P_PARITY_FASTER_PHI"
        reading = (
            "SAME_P_PARITY_FASTER_PHI — same verdict p*; parity sheds a "
            "larger fraction of clean Φ"
        )
    elif h2 and not h3:
        # note direction of Φ asymmetry in reading
        conj_faster = all(
            size_stats[n]["conj_lower_count"] > size_stats[n]["parity_lower_count"]
            for n in SIZES
        )
        if conj_faster:
            verdict_word = "SAME_P_STAR"
            reading = (
                "SAME_P_STAR — verdict p*=0.5 both families at n=3,4; "
                "conjunctive sheds more normalized Φ (parity not faster)"
            )
        else:
            verdict_word = "SAME_P_STAR"
            reading = (
                "SAME_P_STAR — verdict p* matches; normalized Φ decay not "
                "parity-faster"
            )
    else:
        verdict_word = "FAMILY_NOISE_MIXED"
        reading = "FAMILY_NOISE_MIXED — see size stats"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    for n in SIZES:
        st = size_stats[n]
        print(f"  n={n}: p*_c={st['p_conjunctive']} p*_p={st['p_parity']}  "
              f"parity_lower={st['parity_lower_count']}/{st['n_interior']}  "
              f"mean(Φ̂_c−Φ̂_p)={st['mean_hat_conj_minus_par']:+.4f}")
    print(f"  H1 (parity flips earlier ≥0.02): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (same p* at n=3 and n=4):    "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (parity faster Φ̂ | same p*): "
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
    with open(os.path.join(RESULTS, "sweep.csv"), "w", newline="") as fh:
        fields = ["family", "n", "p", "phi", "structure"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "family": r["family"],
                "n": r["n"],
                "p": f"{r['p']:.2f}",
                "phi": f"{r['phi']:.8f}",
                "structure": r["structure"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "p_star_n3_conj": size_stats[3]["p_conjunctive"],
            "p_star_n3_par": size_stats[3]["p_parity"],
            "p_star_n4_conj": size_stats[4]["p_conjunctive"],
            "p_star_n4_par": size_stats[4]["p_parity"],
            "mean_hat_gap_n3":
                f"{size_stats[3]['mean_hat_conj_minus_par']:.6f}",
            "mean_hat_gap_n4":
                f"{size_stats[4]['mean_hat_conj_minus_par']:.6f}",
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
