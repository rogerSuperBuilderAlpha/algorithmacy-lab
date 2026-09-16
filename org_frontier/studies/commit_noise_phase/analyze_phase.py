"""Agenda #6 — Φ phase transition vs smooth decay under commit noise.

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #27, #38, q6_noise_phase_transition. Estimation /
construct / omit / ladder closed.

Run:  python org_frontier/studies/commit_noise_phase/analyze_phase.py
"""

from __future__ import annotations

import csv
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
from org_frontier.probes.lib import verdict as vlib

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

GRID = [round(k * 0.01, 2) for k in range(51)]
PHI_JUMP_FRAC = 0.25
CORE_FLAT_FRAC = 0.05
TOL = 1e-6


def conjunctive_hub(n=3):
    """0=S hub, 1..n-1 parties. S'=AND(parties); Pi'=S."""
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def parity_hub(n=3):
    """0=S hub, 1..n-1 parties. S'=XOR(parties); Pi'=S."""
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
        "clean_phi": 2.0,
    },
    "parity_hub": {
        "rules": parity_hub(3),
        "labels": ("S", "P1", "P2"),
        "hub_col": 0,
        "clean_phi": 0.5,
    },
}


def noisy_tpm(rules, hub_col, p):
    clean = tpm_from_rules(rules, n=len(rules))
    tpm = clean.copy()
    s_clean = clean[:, hub_col]
    tpm[:, hub_col] = (1.0 - p) * s_clean + p * (1.0 - s_clean)
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


def sweep_form(name, spec):
    rules = spec["rules"]
    labels = spec["labels"]
    hub_col = spec["hub_col"]
    cm = cm_from_rules(rules, n=len(rules))
    rows = []
    for p in GRID:
        tpm = noisy_tpm(rules, hub_col, p)
        v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
        core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
        n_core = len(core) if core is not None else 0
        core_str = "{" + ",".join(core) + "}" if core else "(none)"
        rows.append({
            "family": name,
            "p": p,
            "phi": float(v.max_phi),
            "structure": v.structure,
            "n_core": n_core,
            "major_complex": core_str,
            "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
        })
    return rows


def analyze_family(rows):
    """Return per-family flags for H1/H2/H3."""
    phis = [r["phi"] for r in rows]
    structs = [r["structure"] for r in rows]
    cores = [r["n_core"] for r in rows]
    ps = [r["p"] for r in rows]
    total_fall = phis[0] - phis[-1]
    if total_fall < TOL:
        total_fall = max(phis[0], TOL)

    # H1 pieces
    interior_dyadic = any(
        structs[i] == "dyadic" and 0.0 < ps[i] < 0.5 for i in range(len(ps))
    )
    phi_jumps = []
    for i in range(len(ps) - 1):
        drop = phis[i] - phis[i + 1]
        if drop >= PHI_JUMP_FRAC * total_fall:
            phi_jumps.append((ps[i], ps[i + 1], drop))
    # interior Φ jump: step whose left endpoint is < 0.5 and not only the final [0.49,0.50]
    # Count any step including endpoint for H1(b) if left p < 0.5... H1 says interior p*.
    # A jump on [0.49,0.50] is at the degenerate edge — score as endpoint, not H1.
    interior_phi_jump = any(a < 0.49 for a, b, d in phi_jumps)

    h1_family = interior_dyadic or interior_phi_jump

    # H2 pieces
    monotone = all(phis[i + 1] <= phis[i] + TOL for i in range(len(phis) - 1))
    no_big_step = len(phi_jumps) == 0 or (
        len(phi_jumps) == 1 and phi_jumps[0][0] >= 0.49
        and phi_jumps[0][1] == 0.5
        and phi_jumps[0][2] < PHI_JUMP_FRAC * total_fall
    )
    # clearer: no step with drop >= 25% of total
    no_big_step = not any(
        (phis[i] - phis[i + 1]) >= PHI_JUMP_FRAC * total_fall
        for i in range(len(phis) - 1)
    )
    triadic_until_end = all(
        structs[i] == "triadic" for i in range(len(ps)) if ps[i] < 0.5
    )
    dyadic_only_end = structs[-1] == "dyadic" and ps[-1] == 0.5
    h2_family = monotone and no_big_step and triadic_until_end and dyadic_only_end

    # H3 pieces — interior steps only (left p < 0.5)
    core_wo_phi = False
    phi_wo_core = False
    for i in range(len(ps) - 1):
        if ps[i] >= 0.5 - 1e-12:
            continue
        if ps[i + 1] >= 0.5 - 1e-12:
            continue  # exclude step into the degenerate endpoint
        dphi = abs(phis[i] - phis[i + 1])
        dcore = cores[i] != cores[i + 1]
        if dcore and dphi < CORE_FLAT_FRAC * phis[0]:
            core_wo_phi = True
        if (phis[i] - phis[i + 1]) >= PHI_JUMP_FRAC * total_fall and not dcore:
            phi_wo_core = True
    h3_family = core_wo_phi or phi_wo_core

    first_dyadic = next((ps[i] for i in range(len(ps)) if structs[i] == "dyadic"), None)
    max_step = max(
        (phis[i] - phis[i + 1]) for i in range(len(phis) - 1)
    ) if len(phis) > 1 else 0.0

    return {
        "h1": h1_family,
        "h2": h2_family,
        "h3": h3_family,
        "interior_dyadic": interior_dyadic,
        "interior_phi_jump": interior_phi_jump,
        "monotone": monotone,
        "no_big_step": no_big_step,
        "triadic_until_end": triadic_until_end,
        "dyadic_only_end": dyadic_only_end,
        "core_wo_phi": core_wo_phi,
        "phi_wo_core": phi_wo_core,
        "first_dyadic": first_dyadic,
        "phi0": phis[0],
        "phi05": phis[-1],
        "max_step": max_step,
        "max_step_frac": max_step / total_fall,
        "n_phi_jumps": sum(
            1 for i in range(len(phis) - 1)
            if (phis[i] - phis[i + 1]) >= PHI_JUMP_FRAC * total_fall
        ),
    }


def main():
    print("AGENDA #6 — COMMIT-NOISE PHASE TRANSITION")
    print("=" * 80)
    print("  cited: #27, #38; q6_noise_phase_transition (prior fine grid)")
    print("  noise: P(out=1)=(1-p)*clean + p*(1-clean) on hub column")
    print("  forms: conjunctive_hub n=3; parity_hub n=3")
    print("  grid: p=0.00..0.50 step 0.01 (N_p=51)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    # Faithful mediated triad control (label order W,S,C)
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
        ok = (
            v.structure == "triadic"
            and abs(v.max_phi - spec["clean_phi"]) < 1e-6
        )
        # p=0 noisy endpoint
        tpm0 = noisy_tpm(spec["rules"], spec["hub_col"], 0.0)
        cm = cm_from_rules(spec["rules"], n=len(spec["rules"]))
        v0n = classify(tpm0, cm, labels=spec["labels"], eps=PHI_EPS)
        ok0 = v0n.structure == "triadic" and abs(v0n.max_phi - spec["clean_phi"]) < 1e-6
        print(f"  {name}: clean {v.structure} Φ={v.max_phi:.6f}  "
              f"p=0 Φ={v0n.max_phi:.6f}  {'PASS' if ok and ok0 else 'FAIL'}")
        ctrl_forms = ctrl_forms and ok and ok0

    ctrl = ctrl_faithful and ctrl_forms
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    all_rows = []
    family_stats = {}
    for name, spec in FORMS.items():
        print(f"SWEEP — {name}")
        print("-" * 80)
        print(f"  {'p':>5}  {'Φ':>10}  {'struct':>8}  {'n_core':>6}  major_complex")
        rows = sweep_form(name, spec)
        all_rows.extend(rows)
        for r in rows:
            if abs(r["p"] * 100) % 5 < 1e-9 or r["p"] in (0.0, 0.49, 0.5):
                print(f"  {r['p']:>5.2f}  {r['phi']:>10.6f}  {r['structure']:>8}  "
                      f"{r['n_core']:>6}  {r['major_complex']}")
        st = analyze_family(rows)
        family_stats[name] = st
        print(f"  first_dyadic={st['first_dyadic']}  "
              f"max_step_frac={st['max_step_frac']:.4f}  "
              f"monotone={st['monotone']}")
        print()

    # Aggregate hypotheses
    h1 = ctrl and any(family_stats[f]["h1"] for f in FORMS)
    h2 = ctrl and all(family_stats[f]["h2"] for f in FORMS)
    h3 = ctrl and any(family_stats[f]["h3"] for f in FORMS)

    # Mutual exclusion for primary word
    if h1:
        verdict_word = "PHASE_TRANSITION"
        reading = (
            "PHASE_TRANSITION — interior verdict flip or ≥25% Φ step under "
            "commit noise"
        )
    elif h2 and not h3:
        verdict_word = "SMOOTH_DECAY"
        reading = (
            "SMOOTH_DECAY — Φ monotone glide on conjunctive and parity hubs; "
            "verdict holds to p=0.5; no core/Φ decoupling"
        )
    elif h3 and not h1:
        verdict_word = "CORE_DECOUPLE"
        reading = (
            "CORE_DECOUPLE — core membership and Φ change on different "
            "schedules under commit noise"
        )
    else:
        verdict_word = "NOISE_MIXED"
        reading = (
            "NOISE_MIXED — mixed smooth/decouple signals; see family stats"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    for name in FORMS:
        st = family_stats[name]
        print(f"  {name}: Φ(0)={st['phi0']:.6f} Φ(0.5)={st['phi05']:.6f}  "
              f"first_dyadic={st['first_dyadic']}  "
              f"max_step_frac={st['max_step_frac']:.4f}")
        print(f"    H1-local={st['h1']}  H2-local={st['h2']}  H3-local={st['h3']}  "
              f"core_wo_phi={st['core_wo_phi']}  phi_wo_core={st['phi_wo_core']}")
    print(f"  H1 (sharp phase / interior): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (only smooth decay):      "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (core/Φ decoupling):      "
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
        fields = ["family", "p", "phi", "structure", "n_core",
                  "major_complex", "mc_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "family": r["family"],
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
            "conj_first_dyadic": family_stats["conjunctive_hub"]["first_dyadic"],
            "parity_first_dyadic": family_stats["parity_hub"]["first_dyadic"],
            "conj_max_step_frac": f"{family_stats['conjunctive_hub']['max_step_frac']:.6f}",
            "parity_max_step_frac": f"{family_stats['parity_hub']['max_step_frac']:.6f}",
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
