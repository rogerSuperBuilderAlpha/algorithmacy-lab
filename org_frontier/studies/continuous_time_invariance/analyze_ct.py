"""Agenda #12 — continuous-time grain/schedule invariance vs #112.

Exact IIT-4.0 Φ on CTMC→expm(Q·Δt) embeddings (proxy; native CT Φ
unavailable on PyPhi pin). Hypotheses fixed in hypotheses.md before
computing. Cited: #112; STOCH_TEMPORAL_ARC. Estimation/construct/omit
closed.

Run:  python org_frontier/studies/continuous_time_invariance/analyze_ct.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np
from scipy.linalg import expm

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
from org_frontier.corpus.population import enumerate_family
from org_frontier.probes.lib import max_phi_float, verdict as vlib
from org_frontier.probes.probe_invariant_verdict import seq_tpm, two_step_tpm
from pyphi import convert
from pyphi.exceptions import ConditionallyDependentError
from pyphi.tpm import ExplicitTPM

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

LABELS = ("W", "S", "C")
N = 3
NS = 2 ** N

DTS = [0.1, 1.0, 5.0]
SCHEDULES = {
    "equal": (1.0, 1.0, 1.0),
    "slow_S": (1.0, 0.1, 1.0),
    "seq_like": (100.0, 10.0, 1.0),
}


def build_Q(rules, rates):
    """Async CT Boolean network rate matrix (competing clocks)."""
    Q = np.zeros((NS, NS), dtype=float)
    for s in range(NS):
        cur = tuple((s >> i) & 1 for i in range(N))
        for i in range(N):
            nxt = list(cur)
            nxt[i] = int(rules[i](cur))
            t = sum(nxt[j] << j for j in range(N))
            if t != s:
                Q[s, t] += rates[i]
        Q[s, s] = -float(np.sum(Q[s]))
    return Q


def embed_sbn(Q, dt):
    """P=expm(Q·dt) → marginal state-by-node TPM (CI projection input)."""
    P = expm(Q * dt)
    P = np.clip(P, 0.0, None)
    row = P.sum(axis=1, keepdims=True)
    row = np.where(row > 0, row, 1.0)
    P = P / row
    sbn = np.zeros((NS, N), dtype=float)
    for s in range(NS):
        for t in range(NS):
            for i in range(N):
                if (t >> i) & 1:
                    sbn[s, i] += P[s, t]
    return np.clip(sbn, 0.0, 1.0), P


def sbs_ci_residual(P):
    try:
        ExplicitTPM(P, validate=False).conditionally_independent()
        return 0.0
    except ConditionallyDependentError:
        back = convert.state_by_node2state_by_state(
            convert.state_by_state2state_by_node(P)
        )
        return float(np.max(np.abs(P - back)))


def is_tri_tpm(tpm):
    phi, _ = max_phi_float(tpm)
    return bool(phi > PHI_EPS)


def triadic_corpus():
    out = []
    for name, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        if v.structure == "triadic":
            out.append((name, rules, float(v.max_phi)))
    return out


def main():
    print("AGENDA #12 — CONTINUOUS-TIME GRAIN/SCHEDULE INVARIANCE")
    print("=" * 80)
    print("  cited: #112; STOCH_TEMPORAL_ARC (discrete lane otherwise closed)")
    print("  native CT Φ: UNAVAILABLE on IIT-4.0/PyPhi pin")
    print("  proxy: async CTMC Q → P=expm(Q·Δt) → exact Φ on CI-projected SBN")
    print("  panel: 24 #112 triadic corpus forms; Δt∈{0.1,1,5}; 3 rate schedules")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    t_all = time.time()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    faithful = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v0 = vlib(faithful, LABELS)
    ctrl_f = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad sync: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl_f else 'FAIL'}"
    )

    # embedding sanity
    Q0 = build_Q(faithful, (1.0, 1.0, 1.0))
    sbn0, P0 = embed_sbn(Q0, 1.0)
    resid0 = sbs_ci_residual(P0)
    row_ok = bool(np.allclose(P0.sum(axis=1), 1.0))
    v_emb = classify(sbn0, cm_from_rules(faithful), labels=LABELS, eps=PHI_EPS)
    ctrl_emb = row_ok and resid0 > 1e-9 and v_emb.structure in ("triadic", "dyadic")
    print(
        f"  embed dt=1 equal: row-stochastic={row_ok}  "
        f"non-CI resid={resid0:.4f}  Φ={v_emb.max_phi:.4f} {v_emb.structure}  "
        f"{'PASS' if ctrl_emb else 'FAIL'}"
    )
    print("  note: native continuous-time IIT-4.0 Φ is not implemented in PyPhi")

    corpus = triadic_corpus()
    n = len(corpus)
    print(f"  corpus triadic forms: {n}")
    if n != 24:
        raise SystemExit(f"ABORT: expected 24 triadic forms, got {n}")

    # Discrete #112 reaffirm
    print()
    print("DISCRETE #112 REAFFIRM")
    print("-" * 80)
    n_g1 = n_g2 = n_seq = n_maj = 0
    disc_rows = []
    for name, rules, phi0 in corpus:
        g1 = is_tri_tpm(tpm_from_rules(rules))
        g2 = is_tri_tpm(two_step_tpm(rules))
        sq = is_tri_tpm(seq_tpm(rules))
        maj = (int(g1) + int(g2) + int(sq)) >= 2
        n_g1 += g1
        n_g2 += g2
        n_seq += sq
        n_maj += maj
        disc_rows.append({
            "form": name,
            "phi0": phi0,
            "grain1": int(g1),
            "grain2": int(g2),
            "sequential": int(sq),
            "majority": int(maj),
        })
    ctrl_112 = n_g1 == n and n_g2 == 0 and n_seq == 0 and n_maj == 0
    print(f"  grain-1 sync : {n_g1}/{n}")
    print(f"  grain-2 sync : {n_g2}/{n}")
    print(f"  sequential   : {n_seq}/{n}")
    print(f"  majority tri : {n_maj}/{n}  {'PASS' if ctrl_112 else 'FAIL'}")

    ctrl = ctrl_f and ctrl_emb and ctrl_112
    if not ctrl:
        # H3 path if embedding unusable
        if not ctrl_emb:
            print()
            print("HYPOTHESIS TESTS")
            print("-" * 80)
            print("  H1 (CT restores invariance): REFUTED")
            print("  H2 (still schedule/grain dependent): REFUTED")
            print("  H3 (NOT_TESTABLE on PyPhi pin):     SUPPORTED")
            print()
            print("=" * 80)
            print("SUMMARY")
            print("  verdict: NOT_TESTABLE")
            print("  H1=REFUTED  H2=REFUTED  H3=SUPPORTED")
            print(
                "  reading: NOT_TESTABLE — native CT Φ unavailable and "
                "embedding proxy failed instrument gate"
            )
            print("=" * 80)
            os.makedirs(RESULTS, exist_ok=True)
            with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=[
                    "h1", "h2", "h3", "verdict", "reading",
                ])
                w.writeheader()
                w.writerow({
                    "h1": "REFUTED", "h2": "REFUTED", "h3": "SUPPORTED",
                    "verdict": "NOT_TESTABLE",
                    "reading": "embedding proxy failed instrument gate",
                })
            return
        raise SystemExit("ABORT: instrument / #112 control failed")

    # CT grid
    print()
    print("CT EMBEDDING GRID")
    print("-" * 80)
    print(
        f"  {'form':<14} {'sched':<10} {'dt':>5}  {'Φ':>10}  struct  "
        f"sbs_resid"
    )
    ct_rows = []
    n_ct_tri = 0
    n_ct_cells = 0
    forms_flipped = set()
    # summary per schedule
    by_sched = {k: {"tri": 0, "n": 0} for k in SCHEDULES}
    by_dt = {dt: {"tri": 0, "n": 0} for dt in DTS}

    # print only flips + a few witnesses to keep log short; full CSV has all
    witness_printed = 0
    for name, rules, phi0 in corpus:
        cm = cm_from_rules(rules)
        for sn, rates in SCHEDULES.items():
            Q = build_Q(rules, rates)
            for dt in DTS:
                sbn, P = embed_sbn(Q, dt)
                resid = sbs_ci_residual(P)
                v = classify(sbn, cm, labels=LABELS, eps=PHI_EPS)
                n_ct_cells += 1
                by_sched[sn]["n"] += 1
                by_dt[dt]["n"] += 1
                tri = v.structure == "triadic" and v.max_phi > PHI_EPS
                # guard numerical negatives
                if v.max_phi <= PHI_EPS:
                    tri = False
                    structure = "dyadic"
                    phi = 0.0 if v.max_phi < 0 else float(v.max_phi)
                else:
                    structure = v.structure
                    phi = float(v.max_phi)
                if tri:
                    n_ct_tri += 1
                    by_sched[sn]["tri"] += 1
                    by_dt[dt]["tri"] += 1
                else:
                    forms_flipped.add(name)
                    print(
                        f"  {name:<14} {sn:<10} {dt:>5.1f}  {phi:>10.6f}  "
                        f"{structure:<6}  {resid:.4f}  FLIP"
                    )
                ct_rows.append({
                    "form": name,
                    "schedule": sn,
                    "rates": ",".join(str(r) for r in rates),
                    "dt": dt,
                    "phi": phi,
                    "structure": structure,
                    "sbs_residual": resid,
                    "flipped": int(not tri),
                })
                if witness_printed < 6 and sn == "equal" and name == corpus[0][0]:
                    print(
                        f"  {name:<14} {sn:<10} {dt:>5.1f}  {phi:>10.6f}  "
                        f"{structure:<6}  {resid:.4f}"
                    )
                    witness_printed += 1

    print()
    print("CT AGGREGATES")
    print("-" * 80)
    print(f"  CT cells triadic: {n_ct_tri}/{n_ct_cells}  "
          f"({100 * n_ct_tri / n_ct_cells:.1f}%)")
    print(f"  forms flipped on any CT cell: {len(forms_flipped)}/{n}")
    for sn, st in by_sched.items():
        print(f"  schedule {sn:<10}: {st['tri']}/{st['n']} triadic")
    for dt, st in by_dt.items():
        print(f"  dt={dt:<4}: {st['tri']}/{st['n']} triadic")
    if forms_flipped:
        print(f"  flipped forms: {sorted(forms_flipped)}")

    # Hypotheses
    h3 = False  # proxy ran
    h1 = ctrl and n_ct_tri == n_ct_cells
    h2 = ctrl and n_ct_tri < n_ct_cells

    if h1:
        verdict_word = "CT_INVARIANT"
        reading = (
            "CT_INVARIANT — CTMC embedding keeps all grain×schedule "
            "cells triadic on the #112 panel (discrete grain-2/seq wipe "
            "out 24/24)"
        )
    elif h2:
        verdict_word = "STILL_DEPENDENT"
        reading = (
            "STILL_DEPENDENT — CTMC→expm embedding softens #112's wipeout "
            f"({n_ct_tri}/{n_ct_cells} cells triadic) but extreme rate "
            f"asymmetry still flips {len(forms_flipped)}/{n} forms; native "
            "CT Φ remains unavailable on the PyPhi pin"
        )
    else:
        verdict_word = "CT_MIXED"
        reading = "CT_MIXED — see aggregates"

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (CT restores invariance):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (still schedule/grain dependent): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (NOT_TESTABLE on PyPhi pin):  "
          f"{'SUPPORTED' if h3 else 'REFUTED'} "
          f"(proxy ran; native CT Φ still absent)")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "discrete112.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "form", "phi0", "grain1", "grain2", "sequential", "majority",
        ])
        w.writeheader()
        for r in disc_rows:
            w.writerow({**r, "phi0": f"{r['phi0']:.8f}"})

    with open(os.path.join(RESULTS, "ct_grid.csv"), "w", newline="") as fh:
        fields = ["form", "schedule", "rates", "dt", "phi", "structure",
                  "sbs_residual", "flipped"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in ct_rows:
            w.writerow({
                **r,
                "dt": f"{r['dt']:.2f}",
                "phi": f"{r['phi']:.8f}",
                "sbs_residual": f"{r['sbs_residual']:.8e}",
            })

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "n_forms": n,
            "n_ct_triadic": n_ct_tri,
            "n_ct_cells": n_ct_cells,
            "n_forms_flipped": len(forms_flipped),
            "discrete_g1": n_g1,
            "discrete_g2": n_g2,
            "discrete_seq": n_seq,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
