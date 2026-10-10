"""Graded party channel under exact Φ (RESEARCH_AGENDA_V4 #11).

Does the V4 #1 joint-observation cliff survive a graded party channel: the
mediating system reads each party through a lossy channel, correct with
probability q and otherwise reading the default 0, while party duty stays
perfectly correlated? The exact binary IIT-4.0 whole-form Φ screen is scored
on the V4 #1 multifamily panel and the V4 #7 logged panel, with the
alternation and phase anchors recomputed for comparability.

Hypotheses fixed in hypotheses.md before computing.

Run:
  python org_frontier/studies/graded_channel_exact_phi/analyze_graded.py
  python org_frontier/studies/graded_channel_exact_phi/analyze_graded.py --full
"""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import (
    classify_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import max_phi_float, verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

_V41_PATH = os.path.join(
    _REPO_ROOT, "org_frontier", "studies",
    "joint_obs_cliff_exact_phi", "analyze_transfer.py",
)
_spec = importlib.util.spec_from_file_location("v41_transfer", _V41_PATH)
_v41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v41)

_V47_PATH = os.path.join(
    _REPO_ROOT, "org_frontier", "studies",
    "logged_alt_duty_exact_phi", "analyze_logged.py",
)
_spec47 = importlib.util.spec_from_file_location("v47_logged", _V47_PATH)
_v47 = importlib.util.module_from_spec(_spec47)
_spec47.loader.exec_module(_v47)

HOLD_AUC = _v41.HOLD_AUC
HOLD_GAP = _v41.HOLD_GAP
CLIFF_AUC = _v41.CLIFF_AUC
CLIFF_DROP = _v41.CLIFF_DROP

Q_GRID = (1.0, 0.75, 0.5, 0.25)
FULL_FLAG = "--full" in sys.argv


def panel_auc(rows, key):
    scores = [row[key] for row in rows]
    labels = [row["triadic"] for row in rows]
    return _v41.oriented_auc(scores, labels)


def garbled_tpm(rules, n, mediator, parties):
    """State-by-node TPM whose mediator rows are computed with party reads at
    the default 0. Non-mediator rows are the deterministic full rows."""
    rows = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            if j == mediator:
                g = list(cur)
                for p in parties:
                    g[p] = 0
                rows[s, j] = float(rules[j](tuple(g)))
            else:
                rows[s, j] = float(rules[j](cur))
    return rows


def mixed_tpm(rules, n, mediator, parties, q):
    """q * full + (1 - q) * garbled: the mediating system's party reads are
    correct with probability q and the default 0 otherwise."""
    full = tpm_from_rules(rules)
    garb = garbled_tpm(rules, n, mediator, parties)
    return q * full + (1.0 - q) * garb


def score_form(form, q, seed=7):
    """Whole-form exact IIT-4.0 Φ under the symmetric graded channel."""
    n = form["n"]
    _pa, med, _pb = _v41.roles_for(form["family"], n)
    parties = [j for j in range(n) if j != med]
    tpm = mixed_tpm(form["rules"], n, med, parties, q)
    rng = np.random.default_rng(seed)
    phi, _cm = max_phi_float(tpm, rng)
    return float(phi)


def asym_score_form(form, q, seed=7):
    """Whole-form exact Φ under an asymmetric graded channel: only the
    mediator's read of the first party is lossy (the counterpart read)."""
    n = form["n"]
    pa, med, _pb = _v41.roles_for(form["family"], n)
    parties = [pa] if pa != med else [j for j in range(n) if j != med][0]
    tpm = mixed_tpm(form["rules"], n, med, parties, q)
    rng = np.random.default_rng(seed)
    phi, _cm = max_phi_float(tpm, rng)
    return float(phi)


def main():
    t_all = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("AGENDA V4 #11 — GRADED PARTY CHANNEL UNDER EXACT Φ")
    print("=" * 80)
    print("  cited: V4 #1 TRANSFER_PARTIAL_EXACT_PHI; "
          "V4 #2 PHASE_RESTORES_JOINT; V4 #7 CLIFF_RECREATES_ON_LOGGED")
    print("  channel: mediator reads parties correctly w.p. q, default 0 else; "
          "party duty correlated")
    print(f"  protocol: hold AUC≥{HOLD_AUC} or within {HOLD_GAP} of q=1; "
          f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    control = vlib([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
                   ("W", "S", "C"))
    ctrl_tri = (
        control.structure == "triadic" and abs(control.max_phi - 2.0) < 1e-6
    )
    sticky = vlib(
        [lambda x: x[1], lambda x: (x[0] & x[2]) | x[1], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_dya = sticky.structure == "dyadic"
    ctrl_ok = ctrl_tri and ctrl_dya
    print(f"  faithful triad: {control.structure} Φ={control.max_phi:.6f}  "
          f"{'PASS' if ctrl_tri else 'FAIL'}")
    print(f"  sticky:         {sticky.structure} Φ={sticky.max_phi:.6f}  "
          f"{'PASS' if ctrl_dya else 'FAIL'}")
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("BUILD PANELS")
    print("-" * 80)
    multi = _v41.build_multifamily()
    for row in multi:
        row["panel"] = "multifamily"
        row["source"] = "synthetic"
    logged = _v47.build_logged_panel()
    for row in logged:
        row["panel"] = "logged"
    for row in multi + logged:
        row["structure"] = "triadic" if row["triadic"] else "dyadic"

    n_tri_m = sum(r["triadic"] for r in multi)
    n_tri_l = sum(r["triadic"] for r in logged)
    print(f"  multifamily: {len(multi)} forms "
          f"({n_tri_m} tri / {len(multi) - n_tri_m} dya)")
    print(f"  logged:      {len(logged)} forms "
          f"({n_tri_l} tri / {len(logged) - n_tri_l} dya)")
    if n_tri_m == 0 or n_tri_l == 0:
        raise SystemExit("ABORT: a panel lacks both structure classes")
    print()

    print("SCORE exact-Φ channel sweep")
    print("-" * 80)
    t0 = time.time()
    for row in multi + logged:
        for q in Q_GRID:
            key = "phi_q%03d" % round(q * 100)
            row[key] = score_form(row, q)
        if FULL_FLAG:
            for q in (0.5,):
                row["phi_asym%03d" % round(q * 100)] = asym_score_form(row, q)
    print(f"  scored {len(multi) + len(logged)} forms "
          f"({time.time() - t0:.1f}s)")
    print()

    print("ANCHORS (alternation / phase, recomputed)")
    print("-" * 80)
    t0 = time.time()
    for row in multi + logged:
        row.update(_v47.score_phi(row))
    print(f"  anchors scored ({time.time() - t0:.1f}s)")
    print()

    auc = {}
    for panel_name, rows in (("multifamily", multi), ("logged", logged)):
        row_keys = ["phi_q100", "phi_q075", "phi_q050", "phi_q025"]
        if FULL_FLAG:
            row_keys.append("phi_asym050")
        row_keys += ["phi_alt", "phi_phase"]
        for key in row_keys:
            a, orient = panel_auc(rows, key)
            auc[f"{panel_name}:{key}"] = a
            print(f"  {panel_name:12s} {key:12s}  AUC={a:.3f}  orient={orient:+d}")
    print()

    full_m = auc["multifamily:phi_q100"]
    q75_m = auc["multifamily:phi_q075"]
    q50_m = auc["multifamily:phi_q050"]
    q25_m = auc["multifamily:phi_q025"]
    alt_m = auc["multifamily:phi_alt"]
    phase_m = auc["multifamily:phi_phase"]
    full_l = auc["logged:phi_q100"]
    q50_l = auc["logged:phi_q050"]
    q25_l = auc["logged:phi_q025"]
    alt_l = auc["logged:phi_alt"]

    h1 = (
        ctrl_ok
        and _v41.holds(full_m, full_m)
        and _v41.holds(full_l, full_l)
        and _v41.cliffs(alt_m, full_m)
        and _v41.cliffs(alt_l, full_l)
    )
    h2 = ctrl_ok and _v41.holds(q50_m, full_m)
    monotone = all(
        auc["multifamily:phi_q%03d" % round(q * 100)] >=
        auc["multifamily:phi_q%03d" % round(qn * 100)] - 1e-9
        for q, qn in zip(Q_GRID[:-1], Q_GRID[1:])
    )
    interior_cliff = any(
        _v41.cliffs(auc["multifamily:phi_q%03d" % round(q * 100)], full_m)
        for q in (0.75, 0.5, 0.25)
    )
    h3 = ctrl_ok and monotone and not interior_cliff
    h4 = ctrl_ok and (q50_m - alt_m) >= 0.10
    h5 = (
        ctrl_ok
        and _v41.holds(q50_l, full_l) == h2
        and (monotone and not interior_cliff) == h3
    )

    if not h1:
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — full_m={full_m:.3f} full_l={full_l:.3f} "
            f"alt_m={alt_m:.3f} alt_l={alt_l:.3f}"
        )
    elif h2 and h3:
        verdict = "GRADED_HOLDS"
        reading = (
            f"GRADED_HOLDS — the q=0.5 graded channel holds the exact-Φ "
            f"screen ({full_m:.3f}→{q50_m:.3f}) where hard alternation cliffs "
            f"({full_m:.3f}→{alt_m:.3f}); degradation is smooth, so the "
            f"cliff tracks duty correlation, not channel granularity"
        )
    elif h2:
        verdict = "GRADED_HOLDS_ROUGH"
        reading = (
            f"GRADED_HOLDS_ROUGH — q=0.5 holds ({full_m:.3f}→{q50_m:.3f}) but "
            f"the degradation path is not monotone/cliff-free "
            f"(q75={q75_m:.3f} q50={q50_m:.3f} q25={q25_m:.3f})"
        )
    elif (q50_m - alt_m) >= 0.10:
        verdict = "GRADED_PARTIAL"
        reading = (
            f"GRADED_PARTIAL — q=0.5 does not hold ({full_m:.3f}→{q50_m:.3f}) "
            f"but stays above alternation by ≥0.10 (alt={alt_m:.3f}); "
            f"degradation is graded, not binary"
        )
    else:
        verdict = "GRADED_CLIFFS"
        reading = (
            f"GRADED_CLIFFS — the graded channel recreates the cliff "
            f"({full_m:.3f}→{q50_m:.3f} vs alt {alt_m:.3f}); information "
            f"quality, not only duty correlation, carries the screen"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (controls replicate anchors):       "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (graded q=0.5 holds):              "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (smooth monotone degradation):     "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (graded beats alternation ≥0.10):  "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (logged panel replicates):         "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()

    print("MULTIFAMILY FORMS (q sweep → alternation anchor)")
    print("-" * 80)
    for row in multi:
        print(
            f"  {row['name']:20s} {row['structure']:8s} "
            f"n={row['n']} "
            f"1.0:{row['phi_q100']:6.3f} 0.75:{row['phi_q075']:6.3f} "
            f"0.5:{row['phi_q050']:6.3f} 0.25:{row['phi_q025']:6.3f} "
            f"→ alt {row['phi_alt']:6.3f} phase {row['phi_phase']:6.3f}"
        )
    print()

    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict}")
    print(f"  reading: {reading}")
    metrics = (
        f"  metrics: full_m={full_m:.3f}; q75_m={q75_m:.3f}; "
        f"q50_m={q50_m:.3f}; q25_m={q25_m:.3f}; alt_m={alt_m:.3f}; "
        f"phase_m={phase_m:.3f}; full_l={full_l:.3f}; q50_l={q50_l:.3f}; "
        f"q25_l={q25_l:.3f}; alt_l={alt_l:.3f}; n_multi={len(multi)}; "
        f"n_logged={len(logged)}; n_tri_m={n_tri_m}"
    )
    print(metrics)
    if FULL_FLAG:
        asym_m = auc["multifamily:phi_asym050"]
        asym_l = auc["logged:phi_asym050"]
        print(f"  asym050_m={asym_m:.3f}; asym050_l={asym_l:.3f}")
    print("  best next:         strand E residual #12 (M3 subset-Φ fidelity "
          "on third_party/pyphi_iit4_mv)")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    fields = [
        "name", "panel", "family", "n", "structure", "triadic",
        "phi_q100", "phi_q075", "phi_q050", "phi_q025",
        "phi_alt", "phi_phase",
    ]
    if FULL_FLAG:
        fields.append("phi_asym050")
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for panel_name, rows in (("multifamily", multi), ("logged", logged)):
            for row in rows:
                out = dict(row)
                out["family"] = row.get("family", "")
                writer.writerow({k: out.get(k, "") for k in fields})

    summary = {
        "verdict": verdict,
        "reading": reading,
        "h1": bool(h1),
        "h2": bool(h2),
        "h3": bool(h3),
        "h4": bool(h4),
        "h5": bool(h5),
        "auc": {k: v for k, v in auc.items()},
        "n_multi": len(multi),
        "n_logged": len(logged),
        "n_tri_m": n_tri_m,
        "n_tri_l": n_tri_l,
        "control_pass": bool(ctrl_ok),
        "full_flag": bool(FULL_FLAG),
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)


if __name__ == "__main__":
    main()
