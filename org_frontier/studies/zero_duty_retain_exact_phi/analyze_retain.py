"""Zero-duty vs party–mediator retain under exact Φ (RESEARCH_AGENDA_V4 #3).

When a party has zero duty, does exact-Φ ranking cliff, and does an
induced party–mediator retain path still hold — clarifying missing
party–party joints vs any missing node?

Exact binary IIT-4.0 via classify_rules. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/zero_duty_retain_exact_phi/analyze_retain.py
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

_V41 = os.path.join(
    _REPO_ROOT, "org_frontier", "studies", "joint_obs_cliff_exact_phi",
    "analyze_transfer.py",
)
_spec = importlib.util.spec_from_file_location("v41_transfer", _V41)
_v41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v41)

SEED = 43
HOLD_AUC = 0.85
HOLD_GAP = 0.10
CLIFF_AUC = 0.70
CLIFF_DROP = 0.20


def holds(auc, auc_ref):
    if np.isnan(auc) or np.isnan(auc_ref):
        return False
    return auc >= HOLD_AUC or (auc_ref - auc) <= HOLD_GAP


def cliffs(auc, auc_ref):
    if np.isnan(auc_ref):
        return False
    if np.isnan(auc):
        return auc_ref >= HOLD_AUC
    return auc < CLIFF_AUC or (auc_ref - auc) >= CLIFF_DROP


def score_phi(form):
    n = form["n"]
    rules = form["rules"]
    a, m, b = _v41.roles_for(form["family"], n)
    phi_full = form["phi_full"]
    keep_omit_b = tuple(i for i in range(n) if i != b)
    keep_omit_m = tuple(i for i in range(n) if i != m)
    phi_zero, _ = _v41.phi_of(rules, n, keep_omit_b)
    phi_retain, _ = _v41.phi_of(rules, n, (m, a))
    phi_omit_m, _ = _v41.phi_of(rules, n, keep_omit_m)
    phi_ma, _ = _v41.phi_of(rules, n, (m, a))
    phi_mb, _ = _v41.phi_of(rules, n, (m, b))
    phi_alt = 0.5 * (phi_ma + phi_mb)
    return {
        "phi_full": phi_full,
        "phi_zero_duty_B": phi_zero,
        "phi_retain_MA": phi_retain,
        "phi_omit_M": phi_omit_m,
        "phi_alt": phi_alt,
        "zero_eq_retain": abs(phi_zero - phi_retain) < 1e-9,
    }


def panel_auc(rows, key):
    return _v41.oriented_auc(
        [r[key] for r in rows], [r["triadic"] for r in rows]
    )


def main():
    print("AGENDA V4 #3 — ZERO-DUTY vs PARTY–MEDIATOR RETAIN (EXACT Φ)")
    print("=" * 80)
    print("  cited: V4 #1 TRANSFER_PARTIAL_EXACT_PHI; V4 #2 PHASE_RESTORES_JOINT")
    print("  pointer: missing party–party joints vs any missing node")
    print(
        f"  protocol: hold AUC≥{HOLD_AUC} or within {HOLD_GAP} of full; "
        f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}"
    )
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl else 'FAIL'}"
    )
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rng = np.random.default_rng(SEED)
    t_all = time.time()

    print("BUILD PANELS (V4 #1 constructors)")
    print("-" * 80)
    family = _v41.build_family_n3(rng)
    multi = _v41.build_multifamily()
    print(
        f"  family_n3: {len(family)} "
        f"({sum(r['triadic'] for r in family)} tri)"
    )
    print(
        f"  multifamily: {len(multi)} "
        f"({sum(r['triadic'] for r in multi)} tri)"
    )
    print()

    print("SCORE exact-Φ screens")
    print("-" * 80)
    t0 = time.time()
    for row in family + multi:
        row.update(score_phi(row))
    print(f"  scored {len(family) + len(multi)} forms ({time.time() - t0:.1f}s)")
    n3_same = sum(1 for r in family if r["zero_eq_retain"])
    multi_same = sum(1 for r in multi if r["zero_eq_retain"])
    print(
        f"  zero≡retain: family_n3 {n3_same}/{len(family)}; "
        f"multifamily {multi_same}/{len(multi)}"
    )
    print()

    aucs = {}
    print("PANEL AUCs")
    print("-" * 80)
    keys = [
        "phi_full", "phi_zero_duty_B", "phi_retain_MA", "phi_omit_M", "phi_alt",
    ]
    for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
        for key in keys:
            auc, orient = panel_auc(rows, key)
            aucs[f"{panel_name}:{key}"] = (auc, orient)
            print(
                f"  {panel_name:12s} {key:16s}  AUC={auc:.3f}  "
                f"orient={orient:+d}"
            )
    print()

    def A(panel, key):
        return aucs[f"{panel}:{key}"][0]

    auc_full_m = A("multifamily", "phi_full")
    auc_zero_m = A("multifamily", "phi_zero_duty_B")
    auc_ret_m = A("multifamily", "phi_retain_MA")
    auc_omit_m = A("multifamily", "phi_omit_M")
    auc_full_f = A("family_n3", "phi_full")
    auc_zero_f = A("family_n3", "phi_zero_duty_B")
    auc_ret_f = A("family_n3", "phi_retain_MA")

    h1 = ctrl and cliffs(auc_zero_m, auc_full_m)
    h2 = ctrl and holds(auc_ret_m, auc_full_m)
    h3 = ctrl and cliffs(auc_zero_f, auc_full_f)
    h4 = ctrl and cliffs(auc_omit_m, auc_full_m)
    h5 = (
        ctrl
        and holds(auc_full_m, auc_full_m)
        and holds(auc_full_f, auc_full_f)
        and auc_full_m >= HOLD_AUC
        and auc_full_f >= HOLD_AUC
        and n3_same == len(family)
    )

    if not h5:
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H5={h5}; full_m={auc_full_m:.3f} "
            f"full_f={auc_full_f:.3f}; n3_same={n3_same}/{len(family)}"
        )
    elif not h1:
        verdict = "ZERO_DUTY_SOFT"
        reading = (
            f"ZERO_DUTY_SOFT — multifamily zero_duty={auc_zero_m:.3f} "
            f"does not cliff vs full={auc_full_m:.3f}; retain={auc_ret_m:.3f}"
        )
    elif h1 and h2:
        verdict = "RETAIN_SAVES_ZERO_DUTY"
        reading = (
            f"RETAIN_SAVES_ZERO_DUTY — zero-duty cliffs on multifamily "
            f"({auc_full_m:.3f}→{auc_zero_m:.3f}) but retain_MA holds "
            f"({auc_ret_m:.3f}); omit_M={auc_omit_m:.3f}; "
            f"family zero={auc_zero_f:.3f}"
        )
    else:
        # H1 and not H2
        verdict = "RETAIN_FAILS_WITH_ZERO"
        reading = (
            f"RETAIN_FAILS_WITH_ZERO — zero-duty cliffs on multifamily "
            f"({auc_full_m:.3f}→{auc_zero_m:.3f}) and retain_MA also "
            f"fails to hold ({auc_ret_m:.3f}); omit_M={auc_omit_m:.3f} "
            f"(H4={'Y' if h4 else 'N'}); family zero={auc_zero_f:.3f} "
            f"retain={auc_ret_f:.3f}; no escape via party–mediator pair alone"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  multifamily: full={auc_full_m:.3f}  zero={auc_zero_m:.3f}  "
        f"retain={auc_ret_m:.3f}  omit_M={auc_omit_m:.3f}"
    )
    print(
        f"  family_n3:   full={auc_full_f:.3f}  zero={auc_zero_f:.3f}  "
        f"retain={auc_ret_f:.3f}"
    )
    print(
        f"  H1 (zero-duty cliffs multifamily):        "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (retain_MA holds multifamily):         "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (zero-duty cliffs family_n3):          "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (omit-mediator cliffs multifamily):    "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (full holds + n=3 zero≡retain):        "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
        f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
        f"H5={('SUPPORTED' if h5 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(
        f"  metrics: full_m={auc_full_m:.3f}; zero_m={auc_zero_m:.3f}; "
        f"retain_m={auc_ret_m:.3f}; omit_M_m={auc_omit_m:.3f}; "
        f"full_f={auc_full_f:.3f}; zero_f={auc_zero_f:.3f}; "
        f"retain_f={auc_ret_f:.3f}; n3_same={n3_same}/{len(family)}; "
        f"multi_same={multi_same}/{len(multi)}"
    )
    print("  best next:         V4 #4 ring-prior under exact-Φ scoring")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["panel", "screen", "n_forms", "n_tri", "auc", "orient"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
            n_tri = sum(r["triadic"] for r in rows)
            for key in keys:
                auc, orient = aucs[f"{panel_name}:{key}"]
                w.writerow({
                    "panel": panel_name,
                    "screen": key,
                    "n_forms": len(rows),
                    "n_tri": n_tri,
                    "auc": f"{auc:.6f}" if not np.isnan(auc) else "",
                    "orient": orient,
                })

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = [
            "panel", "family", "n", "name", "triadic",
            "phi_full", "phi_zero_duty_B", "phi_retain_MA", "phi_omit_M",
            "phi_alt", "zero_eq_retain",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
            for r in rows:
                w.writerow({
                    "panel": panel_name,
                    "family": r["family"],
                    "n": r["n"],
                    "name": r["name"],
                    "triadic": r["triadic"],
                    "phi_full": f"{r['phi_full']:.6f}",
                    "phi_zero_duty_B": f"{r['phi_zero_duty_B']:.6f}",
                    "phi_retain_MA": f"{r['phi_retain_MA']:.6f}",
                    "phi_omit_M": f"{r['phi_omit_M']:.6f}",
                    "phi_alt": f"{r['phi_alt']:.6f}",
                    "zero_eq_retain": int(r["zero_eq_retain"]),
                })

    summary = {
        "verdict": verdict,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "phi_full_multi_auc": round(float(auc_full_m), 6),
        "phi_zero_multi_auc": round(float(auc_zero_m), 6),
        "phi_retain_multi_auc": round(float(auc_ret_m), 6),
        "phi_omit_m_multi_auc": round(float(auc_omit_m), 6),
        "phi_full_family_auc": round(float(auc_full_f), 6),
        "phi_zero_family_auc": round(float(auc_zero_f), 6),
        "phi_retain_family_auc": round(float(auc_ret_f), 6),
        "n3_zero_eq_retain": f"{n3_same}/{len(family)}",
        "multi_zero_eq_retain": f"{multi_same}/{len(multi)}",
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
