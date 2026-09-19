"""Phase-locked same-slot duty under exact Φ (RESEARCH_AGENDA_V4 #2).

At matched mean duty δ=0.5, does phase-lock (joint) restore exact-Φ
ranking where alternation (no joint) cliffs — i.e. is joint observation
the causal factor, not mean duty?

Exact binary IIT-4.0 via classify_rules. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/phase_lock_exact_phi/analyze_phase.py
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
from sklearn.metrics import roc_auc_score

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import mutual_information
from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

# Reuse panel builders + phi helpers from V4 #1
_V41 = os.path.join(
    _REPO_ROOT, "org_frontier", "studies", "joint_obs_cliff_exact_phi",
    "analyze_transfer.py",
)
_spec = importlib.util.spec_from_file_location("v41_transfer", _V41)
_v41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v41)

T = 2000
NOISE = 0.08
SEED = 42
MIN_PAIR_STEPS = 20
HOLD_AUC = 0.85
HOLD_GAP = 0.10
CLIFF_AUC = 0.70
CLIFF_DROP = 0.20
DUTY = 0.5


def _stable_seed(*parts, base=SEED):
    h = hashlib.md5("|".join(str(p) for p in parts).encode()).hexdigest()
    return base + (int(h[:8], 16) % 10_000)


def oriented_auc(scores, labels):
    return _v41.oriented_auc(scores, labels)


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


def mean_mi_masked(traj, obs_mask):
    return _v41.mean_mi_masked(traj, obs_mask)


def simulate(rules, n, rng):
    tpm = add_noise(tpm_from_rules(rules), NOISE)
    return exact_phi.simulate_trajectory(tpm, n, T, rng)


def mask_phase(Tlen, n, party_a, party_b, duty=DUTY, rng=None):
    """Both parties on the same slots (joint); mediator always on."""
    m = np.ones((Tlen, n), dtype=bool)
    if duty <= 0.0:
        on = np.zeros(Tlen, dtype=bool)
    elif duty >= 1.0:
        on = np.ones(Tlen, dtype=bool)
    else:
        # deterministic half-slots for duty=0.5; else random shared mask
        if abs(duty - 0.5) < 1e-9:
            on = np.arange(Tlen) % 2 == 0
        else:
            assert rng is not None
            on = rng.random(Tlen) < duty
    m[:, party_a] = on
    m[:, party_b] = on
    return m


def mask_alt(Tlen, n, party_a, party_b):
    """Anti-correlated parties; mean duty 0.5 each; never joint."""
    m = np.ones((Tlen, n), dtype=bool)
    even = np.arange(Tlen) % 2 == 0
    m[:, party_a] = even
    m[:, party_b] = ~even
    return m


def duty_of(mask, idx):
    return float(np.mean(mask[:, idx]))


def score_phi(form):
    n = form["n"]
    rules = form["rules"]
    a, m, b = _v41.roles_for(form["family"], n)
    phi_full = form["phi_full"]
    phi_ma, _ = _v41.phi_of(rules, n, (m, a))
    phi_mb, _ = _v41.phi_of(rules, n, (m, b))
    phi_alt = 0.5 * (phi_ma + phi_mb)
    # phase design admits full joint form → exact Φ of full system
    phi_phase = phi_full
    return {
        "phi_full": phi_full,
        "phi_alt": phi_alt,
        "phi_phase": phi_phase,
        "phi_MA": phi_ma,
        "phi_MB": phi_mb,
    }


def score_mi(form, rng):
    n = form["n"]
    a, _m, b = _v41.roles_for(form["family"], n)
    traj = simulate(form["rules"], n, rng)
    m_full = np.ones((T, n), dtype=bool)
    m_alt = mask_alt(T, n, a, b)
    m_phase = mask_phase(T, n, a, b, duty=DUTY, rng=rng)
    return {
        "mi_full": mean_mi_masked(traj, m_full),
        "mi_alt": mean_mi_masked(traj, m_alt),
        "mi_phase": mean_mi_masked(traj, m_phase),
        "duty_alt_a": duty_of(m_alt, a),
        "duty_alt_b": duty_of(m_alt, b),
        "duty_phase_a": duty_of(m_phase, a),
        "duty_phase_b": duty_of(m_phase, b),
    }


def panel_auc(rows, key):
    return oriented_auc([r[key] for r in rows], [r["triadic"] for r in rows])


def main():
    print("AGENDA V4 #2 — PHASE-LOCK vs ALT UNDER EXACT Φ (MATCHED DUTY)")
    print("=" * 80)
    print("  cited: V4 #1 TRANSFER_PARTIAL_EXACT_PHI; V3 #16; V2 #24")
    print("  pointer: joint vs mean duty at δ=0.5; exact Φ + MI")
    print(
        f"  protocol: hold AUC≥{HOLD_AUC} or within {HOLD_GAP} of full; "
        f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}; duty={DUTY}"
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

    print("BUILD PANELS (same constructors as V4 #1)")
    print("-" * 80)
    family = _v41.build_family_n3(rng)
    multi = _v41.build_multifamily()
    print(
        f"  family_n3: {len(family)} forms "
        f"({sum(r['triadic'] for r in family)} tri)"
    )
    print(
        f"  multifamily: {len(multi)} forms "
        f"({sum(r['triadic'] for r in multi)} tri)"
    )
    print()

    print("SCORE exact-Φ screens")
    print("-" * 80)
    t0 = time.time()
    for row in family + multi:
        row.update(score_phi(row))
    print(f"  scored {len(family) + len(multi)} forms ({time.time() - t0:.1f}s)")
    print()

    print("SCORE MI screens + duty check")
    print("-" * 80)
    t0 = time.time()
    duty_rows = []
    for row in family + multi:
        local = np.random.default_rng(_stable_seed("mi", row["name"]))
        mi = score_mi(row, local)
        row.update(mi)
        duty_rows.append(mi)
    print(f"  scored {len(family) + len(multi)} forms ({time.time() - t0:.1f}s)")
    mean_duty_alt = float(np.mean(
        [0.5 * (r["duty_alt_a"] + r["duty_alt_b"]) for r in duty_rows]
    ))
    mean_duty_phase = float(np.mean(
        [0.5 * (r["duty_phase_a"] + r["duty_phase_b"]) for r in duty_rows]
    ))
    print(f"  mean party duty alt={mean_duty_alt:.4f}  phase={mean_duty_phase:.4f}")
    print()

    aucs = {}
    print("PANEL AUCs")
    print("-" * 80)
    for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
        for key in ("phi_full", "phi_alt", "phi_phase", "mi_full", "mi_alt", "mi_phase"):
            auc, orient = panel_auc(rows, key)
            aucs[f"{panel_name}:{key}"] = (auc, orient)
            print(
                f"  {panel_name:12s} {key:10s}  AUC={auc:.3f}  "
                f"orient={orient:+d}"
            )
    print()

    def A(panel, key):
        return aucs[f"{panel}:{key}"][0]

    auc_phi_full_m = A("multifamily", "phi_full")
    auc_phi_alt_m = A("multifamily", "phi_alt")
    auc_phi_phase_m = A("multifamily", "phi_phase")
    auc_phi_full_f = A("family_n3", "phi_full")
    auc_phi_phase_f = A("family_n3", "phi_phase")
    auc_phi_alt_f = A("family_n3", "phi_alt")
    auc_mi_full_f = A("family_n3", "mi_full")
    auc_mi_alt_f = A("family_n3", "mi_alt")
    auc_mi_phase_f = A("family_n3", "mi_phase")

    h1 = ctrl and cliffs(auc_phi_alt_m, auc_phi_full_m)
    h2 = ctrl and holds(auc_phi_phase_m, auc_phi_full_m)
    h3 = ctrl and holds(auc_phi_phase_f, auc_phi_full_f)
    h4 = (
        ctrl
        and holds(auc_mi_phase_f, auc_mi_full_f)
        and cliffs(auc_mi_alt_f, auc_mi_full_f)
    )
    h5 = (
        ctrl
        and abs(mean_duty_alt - DUTY) <= 0.01
        and abs(mean_duty_phase - DUTY) <= 0.01
    )

    if (not h4) or (not h5):
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H4={h4} H5={h5}; mi_phase={auc_mi_phase_f:.3f} "
            f"mi_alt={auc_mi_alt_f:.3f}; duty_alt={mean_duty_alt:.3f} "
            f"duty_phase={mean_duty_phase:.3f}"
        )
    elif not h1:
        verdict = "NO_ALT_CLIFF"
        reading = (
            f"NO_ALT_CLIFF — multifamily phi_alt={auc_phi_alt_m:.3f} "
            f"vs full={auc_phi_full_m:.3f}; cannot test phase restore"
        )
    elif h1 and h2 and h5:
        verdict = "PHASE_RESTORES_JOINT"
        reading = (
            f"PHASE_RESTORES_JOINT — at matched δ={DUTY}, exact-Φ phase "
            f"holds on multifamily ({auc_phi_phase_m:.3f}) where alt "
            f"cliffs ({auc_phi_alt_m:.3f}); family_n3 phase="
            f"{auc_phi_phase_f:.3f}; MI phase={auc_mi_phase_f:.3f} "
            f"alt={auc_mi_alt_f:.3f}; joint observation not mean duty"
        )
    elif h1 and (not h2):
        verdict = "PHASE_FAILS_EXACT_PHI"
        reading = (
            f"PHASE_FAILS_EXACT_PHI — alt cliffs ({auc_phi_alt_m:.3f}) but "
            f"phase fails hold ({auc_phi_phase_m:.3f} vs full "
            f"{auc_phi_full_m:.3f})"
        )
    else:
        verdict = "PHASE_MIXED"
        reading = (
            f"PHASE_MIXED — H1={h1} H2={h2} H3={h3} H4={h4} H5={h5}; "
            f"phi_phase_m={auc_phi_phase_m:.3f} phi_alt_m={auc_phi_alt_m:.3f}"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  multifamily: phi_full={auc_phi_full_m:.3f}  "
        f"phi_alt={auc_phi_alt_m:.3f}  phi_phase={auc_phi_phase_m:.3f}"
    )
    print(
        f"  family_n3:   phi_full={auc_phi_full_f:.3f}  "
        f"phi_alt={auc_phi_alt_f:.3f}  phi_phase={auc_phi_phase_f:.3f}"
    )
    print(
        f"  family_n3:   mi_full={auc_mi_full_f:.3f}  "
        f"mi_alt={auc_mi_alt_f:.3f}  mi_phase={auc_mi_phase_f:.3f}"
    )
    print(f"  duty check:  alt={mean_duty_alt:.4f}  phase={mean_duty_phase:.4f}")
    print(
        f"  H1 (exact-Φ alt cliffs multifamily):      "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (exact-Φ phase holds multifamily):     "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (exact-Φ phase holds family_n3):       "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (MI phase holds / alt cliffs family):  "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (mean duty matched at δ={DUTY}):         "
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
        f"  metrics: phi_full_m={auc_phi_full_m:.3f}; "
        f"phi_alt_m={auc_phi_alt_m:.3f}; phi_phase_m={auc_phi_phase_m:.3f}; "
        f"phi_phase_f={auc_phi_phase_f:.3f}; mi_phase_f={auc_mi_phase_f:.3f}; "
        f"mi_alt_f={auc_mi_alt_f:.3f}; duty_alt={mean_duty_alt:.3f}; "
        f"duty_phase={mean_duty_phase:.3f}"
    )
    print("  best next:         V4 #3 exact-Φ zero-duty vs induced pair retain")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["panel", "screen", "n_forms", "n_tri", "auc", "orient"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
            n_tri = sum(r["triadic"] for r in rows)
            for key in ("phi_full", "phi_alt", "phi_phase", "mi_full", "mi_alt", "mi_phase"):
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
            "phi_full", "phi_alt", "phi_phase",
            "mi_full", "mi_alt", "mi_phase",
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
                    "phi_alt": f"{r['phi_alt']:.6f}",
                    "phi_phase": f"{r['phi_phase']:.6f}",
                    "mi_full": f"{r['mi_full']:.6f}",
                    "mi_alt": f"{r['mi_alt']:.6f}",
                    "mi_phase": f"{r['mi_phase']:.6f}",
                })

    summary = {
        "verdict": verdict,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "phi_full_multi_auc": round(float(auc_phi_full_m), 6),
        "phi_alt_multi_auc": round(float(auc_phi_alt_m), 6),
        "phi_phase_multi_auc": round(float(auc_phi_phase_m), 6),
        "phi_phase_family_auc": round(float(auc_phi_phase_f), 6),
        "mi_phase_family_auc": round(float(auc_mi_phase_f), 6),
        "mi_alt_family_auc": round(float(auc_mi_alt_f), 6),
        "mean_duty_alt": round(mean_duty_alt, 6),
        "mean_duty_phase": round(mean_duty_phase, 6),
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
