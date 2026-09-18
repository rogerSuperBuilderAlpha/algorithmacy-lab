"""Agenda #7 — party vs mediator flip-noise thresholds.

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: commit_noise_phase (#6 SMOOTH_DECAY pointer);
#27/#38; q7_party_vs_mediator_noise. Estimation/construct/omit closed.

Run:  python org_frontier/studies/party_vs_mediator_noise/analyze_locus.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from functools import reduce

import pyphi
from pyphi import new_big_phi

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
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.probes.lib import verdict as vlib

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

GRID = [round(k * 0.01, 2) for k in range(51)]
THRESH_GAP = 0.02
PHI_GAP_FRAC = 0.15
TOL = 1e-6


def conjunctive_hub(n=3):
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def parity_hub(n=3):
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


FORMS = {
    "conjunctive_hub": {
        "rules": conjunctive_hub(3),
        "labels": ("S", "P1", "P2"),
        "hub_col": 0,
        "party_cols": (1, 2),
        "clean_phi": 2.0,
    },
    "parity_hub": {
        "rules": parity_hub(3),
        "labels": ("S", "P1", "P2"),
        "hub_col": 0,
        "party_cols": (1, 2),
        "clean_phi": 0.5,
    },
}


def noisy_tpm(rules, cols, p):
    """Flip-noise on one or more columns."""
    clean = tpm_from_rules(rules, n=len(rules))
    tpm = clean.copy()
    for c in cols:
        s_clean = clean[:, c]
        tpm[:, c] = (1.0 - p) * s_clean + p * (1.0 - s_clean)
    return tpm


def major_complex_on_tpm(tpm_sbn, cm, labels):
    n = cm.shape[0]
    net = pyphi.Network(tpm_sbn, cm=cm, node_labels=labels[:n])
    best = (None, -1.0)
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        node_indices = getattr(mc, "node_indices", None)
        if node_indices is None:
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in node_indices), float(mc.phi))
    return best


def sweep(name, spec, locus, cols):
    rules = spec["rules"]
    labels = spec["labels"]
    cm = cm_from_rules(rules, n=len(rules))
    rows = []
    for p in GRID:
        tpm = noisy_tpm(rules, cols, p)
        v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
        core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
        n_core = len(core) if core is not None else 0
        core_str = "{" + ",".join(core) + "}" if core else "(none)"
        rows.append({
            "family": name,
            "locus": locus,
            "p": p,
            "phi": float(v.max_phi),
            "structure": v.structure,
            "n_core": n_core,
            "major_complex": core_str,
            "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
        })
    return rows


def first_dyadic(rows):
    for r in rows:
        if r["structure"] == "dyadic":
            return r["p"]
    return None


def analyze_pair(med_rows, party_rows, phi0):
    p_med = first_dyadic(med_rows)
    p_party = first_dyadic(party_rows)
    same_thresh = (p_med is not None and p_party is not None
                   and abs(p_med - p_party) < 1e-12)
    gap = (abs(p_med - p_party)
           if p_med is not None and p_party is not None else float("nan"))

    max_phi_gap = 0.0
    core_diff = False
    for a, b in zip(med_rows, party_rows):
        assert abs(a["p"] - b["p"]) < 1e-12
        if a["p"] >= 0.5:
            continue
        max_phi_gap = max(max_phi_gap, abs(a["phi"] - b["phi"]))
        if a["n_core"] != b["n_core"]:
            core_diff = True

    h1_local = (
        p_med is not None and p_party is not None
        and gap >= THRESH_GAP
    )
    h2_local = same_thresh
    h3_local = h2_local and (
        max_phi_gap >= PHI_GAP_FRAC * phi0 or core_diff
    )
    return {
        "p_mediator": p_med,
        "p_party": p_party,
        "gap": gap,
        "same_thresh": same_thresh,
        "max_phi_gap": max_phi_gap,
        "max_phi_gap_frac": max_phi_gap / max(phi0, TOL),
        "core_diff_interior": core_diff,
        "h1": h1_local,
        "h2": h2_local,
        "h3": h3_local,
    }


def main():
    print("AGENDA #7 — PARTY VS MEDIATOR NOISE")
    print("=" * 80)
    print("  cited: commit_noise_phase (#6 SMOOTH_DECAY); #27/#38; Q7 prior")
    print("  noise: flip-noise on mediator (hub) vs party (P1) columns")
    print("  forms: conjunctive_hub n=3; parity_hub n=3")
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
    for name, spec in FORMS.items():
        v = classify_rules(spec["rules"], labels=spec["labels"])
        ok = (v.structure == "triadic"
              and abs(v.max_phi - spec["clean_phi"]) < 1e-6)
        tpm0 = noisy_tpm(spec["rules"], [spec["hub_col"]], 0.0)
        cm = cm_from_rules(spec["rules"], n=len(spec["rules"]))
        v0n = classify(tpm0, cm, labels=spec["labels"], eps=PHI_EPS)
        ok0 = (v0n.structure == "triadic"
               and abs(v0n.max_phi - spec["clean_phi"]) < 1e-6)
        print(f"  {name}: clean Φ={v.max_phi:.6f}  p=0 hub Φ={v0n.max_phi:.6f}  "
              f"{'PASS' if ok and ok0 else 'FAIL'}")
        ctrl_forms = ctrl_forms and ok and ok0
    ctrl = ctrl_faithful and ctrl_forms
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    all_rows = []
    family_stats = {}
    symmetry = {}

    for name, spec in FORMS.items():
        print(f"SWEEPS — {name}")
        print("-" * 80)
        med = sweep(name, spec, "mediator", [spec["hub_col"]])
        p1 = sweep(name, spec, "party_P1", [spec["party_cols"][0]])
        p2 = sweep(name, spec, "party_P2", [spec["party_cols"][1]])
        all_rows.extend(med)
        all_rows.extend(p1)
        all_rows.extend(p2)

        # P1 vs P2 symmetry
        max_d = max(abs(a["phi"] - b["phi"]) for a, b in zip(p1, p2))
        same_flip = first_dyadic(p1) == first_dyadic(p2)
        symmetry[name] = {"max_phi_diff": max_d, "same_flip": same_flip}
        print(f"  P1↔P2 symmetry: max|ΔΦ|={max_d:.6e}  "
              f"same_p*={same_flip}")

        st = analyze_pair(med, p1, spec["clean_phi"])
        family_stats[name] = st
        print(f"  p*_mediator={st['p_mediator']}  p*_party={st['p_party']}  "
              f"|Δ|={st['gap']}")
        print(f"  max|Φ_p−Φ_m|={st['max_phi_gap']:.4f}  "
              f"(frac {st['max_phi_gap_frac']:.3f})  "
              f"core_diff_interior={st['core_diff_interior']}")

        # print selected points for both loci
        print(f"  {'p':>5}  {'Φ_med':>10}  {'Φ_P1':>10}  {'n_med':>5}  {'n_P1':>5}")
        for a, b in zip(med, p1):
            if abs(a["p"] * 100) % 10 < 1e-9 or a["p"] in (0.0, 0.49, 0.5):
                print(f"  {a['p']:>5.2f}  {a['phi']:>10.6f}  {b['phi']:>10.6f}  "
                      f"{a['n_core']:>5}  {b['n_core']:>5}")
        print()

    h1 = ctrl and any(family_stats[f]["h1"] for f in FORMS)
    h2 = ctrl and all(family_stats[f]["h2"] for f in FORMS)
    h3 = ctrl and any(family_stats[f]["h3"] for f in FORMS)
    # if H1 then not score H2 as primary mutual
    if h1 and h2:
        # shouldn't happen if thresholds differ by ≥0.02 vs exact equal
        h2 = False

    if h1:
        verdict_word = "THRESHOLDS_DIFFER"
        reading = (
            "THRESHOLDS_DIFFER — party and mediator collapse at different p*"
        )
    elif h2 and h3:
        verdict_word = "SAME_THRESHOLD_DIFF_CURVE"
        reading = (
            "SAME_THRESHOLD_DIFF_CURVE — collapse p* matches (both 0.5); "
            "seat shapes Φ (and/or n_core) differently"
        )
    elif h2 and not h3:
        verdict_word = "LOCUS_INDIFFERENT"
        reading = (
            "LOCUS_INDIFFERENT — party and mediator match on threshold, "
            "Φ, and n_core"
        )
    else:
        verdict_word = "LOCUS_MIXED"
        reading = "LOCUS_MIXED — see family stats"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    for name in FORMS:
        st = family_stats[name]
        print(f"  {name}: p*_med={st['p_mediator']} p*_party={st['p_party']}  "
              f"max_Φ_gap_frac={st['max_phi_gap_frac']:.3f}  "
              f"core_diff={st['core_diff_interior']}")
    print(f"  H1 (thresholds differ ≥0.02): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (same threshold both families): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (Φ/n_core differ at same p*): "
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
        fields = ["family", "locus", "p", "phi", "structure", "n_core",
                  "major_complex", "mc_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "family": r["family"],
                "locus": r["locus"],
                "p": f"{r['p']:.2f}",
                "phi": f"{r['phi']:.8f}",
                "structure": r["structure"],
                "n_core": r["n_core"],
                "major_complex": r["major_complex"],
                "mc_phi": f"{r['mc_phi']:.8f}",
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "conj_p_med": family_stats["conjunctive_hub"]["p_mediator"],
            "conj_p_party": family_stats["conjunctive_hub"]["p_party"],
            "conj_max_phi_gap_frac":
                f"{family_stats['conjunctive_hub']['max_phi_gap_frac']:.6f}",
            "parity_p_med": family_stats["parity_hub"]["p_mediator"],
            "parity_p_party": family_stats["parity_hub"]["p_party"],
            "parity_max_phi_gap_frac":
                f"{family_stats['parity_hub']['max_phi_gap_frac']:.6f}",
            "conj_P1P2_max_dphi": f"{symmetry['conjunctive_hub']['max_phi_diff']:.8f}",
            "parity_P1P2_max_dphi": f"{symmetry['parity_hub']['max_phi_diff']:.8f}",
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
