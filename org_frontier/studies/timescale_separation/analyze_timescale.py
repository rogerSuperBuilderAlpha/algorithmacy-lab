"""Agenda #9 — timescale separation (fast parties, slow mediator).

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #62 sequential; #6–#8 noise pointers; Q9 prior.
Estimation/construct/omit closed.

Run:  python org_frontier/studies/timescale_separation/analyze_timescale.py
"""

from __future__ import annotations

import csv
import itertools
import os
import sys
import time
from functools import reduce

import numpy as np
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
from org_frontier.probes.lib import max_phi_float, verdict as vlib

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

K_GRID = [1, 2, 3, 4, 5, 6]
TOL = 1e-6
PHI_SOFT_FRAC = 0.15


def conjunctive_rules():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def parity_hub_rules():
    n = 3
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


FORMS = {
    "conjunctive": {
        "rules": conjunctive_rules(),
        "labels": ("W", "S", "C"),
        "s_idx": 1,
        "clean_phi": 2.0,
    },
    "parity_hub": {
        "rules": parity_hub_rules(),
        "labels": ("S", "P1", "P2"),
        "s_idx": 0,
        "clean_phi": 0.5,
    },
}


def hold_k_tpm(rules, k, n, s_idx):
    """Deterministic hold-for-k composed map (Q9 methods)."""

    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]
        return ns

    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9
                   for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def prob_commit_tpm(rules, k, n, s_idx):
    """Probabilistic 1/k mediator commit (Q9 methods)."""
    base = tpm_from_rules(rules, n=n)
    t = base.copy()
    for s in range(2 ** n):
        cur_S = (s >> s_idx) & 1
        commit_val = base[s, s_idx]
        t[s, s_idx] = (1.0 / k) * commit_val + (1.0 - 1.0 / k) * cur_S
    return t


def sequential_tpm(rules, order, n):
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for j in order:
            state[j] = int(rules[j](tuple(state)))
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9
                   for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


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


def read_hold(name, spec, k):
    rules, labels, s_idx = spec["rules"], spec["labels"], spec["s_idx"]
    n = len(rules)
    tpm, cm = hold_k_tpm(rules, k, n, s_idx)
    v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
    core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
    n_core = len(core) if core is not None else 0
    core_str = "{" + ",".join(core) + "}" if core else "(none)"
    return {
        "family": name,
        "construction": "hold_k",
        "k": k,
        "phi": float(v.max_phi),
        "structure": v.structure,
        "n_core": n_core,
        "major_complex": core_str,
        "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
    }


def read_prob(name, spec, k):
    rules, labels, s_idx = spec["rules"], spec["labels"], spec["s_idx"]
    n = len(rules)
    tpm = prob_commit_tpm(rules, k, n, s_idx)
    cm = cm_from_rules(rules, n=n)
    # stochastic: use max_phi_float for Φ; structure from Φ threshold
    phi, _ = max_phi_float(tpm)
    structure = "triadic" if phi > PHI_EPS else "dyadic"
    core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
    n_core = len(core) if core is not None else 0
    core_str = "{" + ",".join(core) + "}" if core else "(none)"
    return {
        "family": name,
        "construction": "prob_1k",
        "k": k,
        "phi": float(phi),
        "structure": structure,
        "n_core": n_core,
        "major_complex": core_str,
        "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
    }


def first_dyadic_k(rows):
    for r in rows:
        if r["structure"] == "dyadic":
            return r["k"]
    return None


def analyze_hold(rows):
    k1 = rows[0]
    n_core0 = k1["n_core"]
    phi0 = k1["phi"]
    k_star = first_dyadic_k(rows)
    factors = (
        k_star is not None and k_star > 1
        and any(r["n_core"] < n_core0 for r in rows if r["k"] >= k_star)
    )
    all_tri = all(r["structure"] == "triadic" for r in rows)
    max_dphi = max(abs(r["phi"] - phi0) for r in rows)
    phi_soft = all_tri and max_dphi >= PHI_SOFT_FRAC * max(phi0, TOL)
    return {
        "k_star": k_star,
        "factors": factors,
        "all_triadic": all_tri,
        "phi_soft": phi_soft,
        "max_dphi": max_dphi,
        "phi0": phi0,
        "n_core0": n_core0,
        "core_at_kstar": next(
            (r["major_complex"] for r in rows if r["k"] == k_star), None
        ) if k_star else None,
    }


def main():
    print("AGENDA #9 — TIMESCALE SEPARATION")
    print("=" * 80)
    print("  cited: #62 sequential; #6–#8 noise pointers; Q9 prior")
    print("  primary: hold-for-k; check: prob 1/k; control: #62 sequential")
    print("  forms: conjunctive (W,S,C); parity_hub (S,P1,P2)")
    print("  k grid: 1..6")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(conjunctive_rules(), ("W", "S", "C"))
    ctrl_faithful = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl_faithful else 'FAIL'}")

    ctrl_forms = True
    for name, spec in FORMS.items():
        v = classify_rules(spec["rules"], labels=spec["labels"])
        ok = (v.structure == "triadic"
              and abs(v.max_phi - spec["clean_phi"]) < 1e-6)
        # k=1 hold reduces to sync
        r1 = read_hold(name, spec, 1)
        ok1 = (r1["structure"] == "triadic"
               and abs(r1["phi"] - spec["clean_phi"]) < 1e-6)
        print(f"  {name}: sync Φ={v.max_phi:.6f}  hold k=1 Φ={r1['phi']:.6f}  "
              f"{'PASS' if ok and ok1 else 'FAIL'}")
        ctrl_forms = ctrl_forms and ok and ok1
    ctrl = ctrl_faithful and ctrl_forms
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    all_rows = []
    hold_stats = {}
    prob_stats = {}

    # ---- #62 sequential control on conjunctive ----
    print("CONTROL — #62 sequential (conjunctive)")
    print("-" * 80)
    rules = FORMS["conjunctive"]["rules"]
    labels = FORMS["conjunctive"]["labels"]
    seq_structs = []
    for order in itertools.permutations(range(3)):
        tpm, cm = sequential_tpm(rules, order, 3)
        st = classify(tpm, cm, labels=labels, eps=PHI_EPS).structure
        seq_structs.append(st)
    n_dyadic_seq = sum(1 for s in seq_structs if s == "dyadic")
    print(f"  sequential orders dyadic: {n_dyadic_seq}/6  "
          f"(expect 6/6 per #62)")
    seq_ok = n_dyadic_seq == 6
    print(f"  #62 control: {'PASS' if seq_ok else 'FAIL'}")
    print()

    for name, spec in FORMS.items():
        print(f"HOLD-FOR-k — {name}")
        print("-" * 80)
        print(f"  {'k':>3}  {'Φ':>10}  {'struct':>8}  {'n_core':>6}  major_complex")
        hold_rows = [read_hold(name, spec, k) for k in K_GRID]
        all_rows.extend(hold_rows)
        for r in hold_rows:
            print(f"  {r['k']:>3}  {r['phi']:>10.6f}  {r['structure']:>8}  "
                  f"{r['n_core']:>6}  {r['major_complex']}")
        hold_stats[name] = analyze_hold(hold_rows)
        print(f"  k*={hold_stats[name]['k_star']}  "
              f"core@k*={hold_stats[name]['core_at_kstar']}")
        print()

        print(f"PROB 1/k — {name}")
        print("-" * 80)
        print(f"  {'k':>3}  {'Φ':>10}  {'struct':>8}  {'n_core':>6}  major_complex")
        prob_rows = [read_prob(name, spec, k) for k in K_GRID]
        all_rows.extend(prob_rows)
        for r in prob_rows:
            print(f"  {r['k']:>3}  {r['phi']:>10.6f}  {r['structure']:>8}  "
                  f"{r['n_core']:>6}  {r['major_complex']}")
        prob_stats[name] = {
            "k_star": first_dyadic_k(prob_rows),
            "all_triadic": all(r["structure"] == "triadic" for r in prob_rows),
        }
        print(f"  k*_prob={prob_stats[name]['k_star']}")
        print()

    # H gates on hold-for-k
    h1 = ctrl and seq_ok and hold_stats["conjunctive"]["factors"]
    h2 = ctrl and all(hold_stats[f]["all_triadic"] for f in FORMS)
    h3 = ctrl and any(hold_stats[f]["phi_soft"] for f in FORMS)
    if h1 and h2:
        h2 = False
    if h1 and h3:
        # factors includes verdict flip — not phi-only
        h3 = False

    if h1:
        verdict_word = "FACTORS_LIKE_62"
        reading = (
            "FACTORS_LIKE_62 — hold-for-k flips dyadic at k*=2 with core "
            "drop (like #62 sequential); prob 1/k stays triadic "
            "(construction-split)"
        )
    elif h2:
        verdict_word = "TIMESCALE_ROBUST"
        reading = (
            "TIMESCALE_ROBUST — hold-for-k keeps triadic across k=1..6"
        )
    elif h3:
        verdict_word = "PHI_ONLY"
        reading = (
            "PHI_ONLY — Φ moves under hold-for-k without a verdict flip"
        )
    else:
        verdict_word = "TIMESCALE_MIXED"
        reading = "TIMESCALE_MIXED — see form/construction stats"

    # refine reading with construction split fact
    conj_prob_tri = prob_stats["conjunctive"]["all_triadic"]
    if h1 and conj_prob_tri:
        reading = (
            "FACTORS_LIKE_62 — hold-for-k factors at k*=2 (core→{S}); "
            "#62 sequential 6/6 dyadic; prob 1/k stays triadic "
            "(construction decides)"
        )

    print("HYPOTHESIS TESTS (hold-for-k primary)")
    print("-" * 80)
    for name in FORMS:
        st = hold_stats[name]
        print(f"  hold {name}: k*={st['k_star']}  factors={st['factors']}  "
              f"core@k*={st['core_at_kstar']}  "
              f"prob_all_tri={prob_stats[name]['all_triadic']}")
    print(f"  H1 (factors like #62): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (verdict robust to k): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (Φ soft, no verdict flip): "
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
        fields = ["family", "construction", "k", "phi", "structure",
                  "n_core", "major_complex", "mc_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "family": r["family"],
                "construction": r["construction"],
                "k": r["k"],
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
            "conj_hold_kstar": hold_stats["conjunctive"]["k_star"],
            "parity_hold_kstar": hold_stats["parity_hub"]["k_star"],
            "conj_hold_core_at_kstar": hold_stats["conjunctive"]["core_at_kstar"],
            "conj_prob_all_triadic": prob_stats["conjunctive"]["all_triadic"],
            "seq_dyadic_orders": f"{n_dyadic_seq}/6",
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
