"""Agenda #23 — sample complexity of the cheap #122 screen.

Nested trajectory prefixes; exact IIT-4.0 labels. Hypotheses fixed in
hypotheses.md before computing.

Cited: #122, probe_surrogate_transfer, probe_phiid_length. #22 pointer only.
Construct/omit/ladder/indeg closed.

Run:  python org_frontier/studies/sample_complexity_screen/analyze_complexity.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.multiparty.scaling import sample_form
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import (
    entropy,
    mutual_information,
    o_information,
    transfer_entropy,
)
from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

LENGTHS = (125, 250, 500, 1000, 2000, 4000)
T_MAX = max(LENGTHS)
NOISE_LAB = 0.08
NOISE_HI = 0.16
AUC_TARGET = 0.90
SEED = 23
RF_N = 200


def feats(traj, n):
    """Probe-99 eight aggregate features."""
    ent = [entropy(traj, [i]) for i in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    mi = [mutual_information(traj, [a], [b]) for a, b in pairs]
    te = [
        transfer_entropy(traj, a, b)
        for a in range(n) for b in range(n) if a != b
    ]
    oi = o_information(traj, list(range(n)))
    return np.array([
        np.mean(ent), np.min(ent), np.max(ent),
        np.mean(mi), np.max(mi), np.mean(te), np.max(te), float(oi),
    ], dtype=float)


def mean_mi(traj, n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return float(np.mean([mutual_information(traj, [a], [b]) for a, b in pairs]))


def _auc(scores, labels):
    scores = np.asarray(scores, float)
    labels = np.asarray(labels, int)
    if labels.sum() == 0 or labels.sum() == len(labels):
        return float("nan")
    try:
        return float(roc_auc_score(labels, scores))
    except ValueError:
        return float("nan")


def labels_for(n):
    if n == 3:
        return ("W", "S", "C")
    return tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)])


def build_panels(rng):
    """Balanced-ish panels with exact labels cached."""
    panels = {}

    # n=3: all triadic + equal dyadic sample from strict-mediation
    tri, dya = [], []
    for name, rules in enumerate_family():
        v = classify_rules(rules, labels=labels_for(3))
        bucket = tri if v.structure == "triadic" else dya
        bucket.append((name, rules, int(v.structure == "triadic"), float(v.max_phi)))
    n_take = min(24, len(tri), len(dya))
    pick_t = [tri[i] for i in rng.choice(len(tri), n_take, replace=False)]
    pick_d = [dya[i] for i in rng.choice(len(dya), n_take, replace=False)]
    panels[3] = pick_t + pick_d

    for n, want in ((4, 32), (5, 16)):
        forms = []
        # oversample then balance
        pool = []
        for k in range(want * 6):
            rules = sample_form(n, rng)
            v = classify_rules(rules, labels=labels_for(n))
            pool.append((f"n{n}_{k}", rules, int(v.structure == "triadic"),
                         float(v.max_phi)))
        tri = [p for p in pool if p[2] == 1]
        dya = [p for p in pool if p[2] == 0]
        half = min(want // 2, len(tri), len(dya))
        if half < 4:
            # fall back: take whatever we have, pad with more draws
            forms = pool[:want]
        else:
            forms = (
                [tri[i] for i in rng.choice(len(tri), half, replace=False)]
                + [dya[i] for i in rng.choice(len(dya), half, replace=False)]
            )
        panels[n] = forms

    return panels


def simulate_long(rules, n, noise, rng):
    tpm = add_noise(tpm_from_rules(rules), noise)
    return exact_phi.simulate_trajectory(tpm, n, T_MAX, rng)


def curve_for_panel(forms, n, noise, rng):
    """Return per-T rows: mi_auc, rf_auc, n_forms, n_tri."""
    # one long traj per form
    trajs = []
    y = []
    for _, rules, tri, _ in forms:
        trajs.append(simulate_long(rules, n, noise, rng))
        y.append(tri)
    y = np.asarray(y, int)

    rows = []
    for T in LENGTHS:
        mi_scores = []
        X = []
        for traj in trajs:
            prefix = traj[:T]
            mi_scores.append(mean_mi(prefix, n))
            X.append(feats(prefix, n))
        mi_scores = np.asarray(mi_scores, float)
        X = np.vstack(X)
        mi_auc = _auc(mi_scores, y)

        rf_auc = float("nan")
        if 0 < y.sum() < len(y) and len(y) >= 8:
            clf = RandomForestClassifier(
                n_estimators=RF_N, random_state=SEED, n_jobs=1
            )
            cv = min(5, int(y.sum()), int(len(y) - y.sum()))
            if cv >= 2:
                skf = StratifiedKFold(n_splits=cv, shuffle=True, random_state=SEED)
                try:
                    proba = cross_val_predict(
                        clf, X, y, cv=skf, method="predict_proba"
                    )[:, 1]
                    rf_auc = _auc(proba, y)
                except Exception:
                    rf_auc = float("nan")

        rows.append({
            "n": n,
            "noise": noise,
            "T": T,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": mi_auc,
            "rf_auc": rf_auc,
        })
    return rows


def t_star(curve_rows):
    """Smallest T with mi_auc ≥ target; None if never."""
    for r in sorted(curve_rows, key=lambda z: z["T"]):
        if not np.isnan(r["mi_auc"]) and r["mi_auc"] >= AUC_TARGET:
            return int(r["T"])
    return None


def main():
    print("AGENDA #23 — SAMPLE COMPLEXITY OF THE CHEAP SCREEN")
    print("=" * 80)
    print("  cited: #122 mean-MI screen; Probe-99 eight-feat RF; Probe 86 Φ_R")
    print("  pointer: structure_aware_surrogate NO_STRUCTURE_GAIN (#22)")
    print("  protocol: nested traj prefixes; exact IIT-4.0 labels; AUC target "
          f"{AUC_TARGET}")
    print(f"  T grid: {list(LENGTHS)}  T_max={T_MAX}")
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
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rng = np.random.default_rng(SEED)
    t_all = time.time()
    print("BUILD PANELS (exact labels)")
    print("-" * 80)
    panels = build_panels(rng)
    for n, forms in sorted(panels.items()):
        n_tri = sum(f[2] for f in forms)
        print(f"  n={n}: {len(forms)} forms ({n_tri} triadic / "
              f"{len(forms) - n_tri} dyadic)")
    print()

    all_curves = []

    print("CURVES — noise=0.08 (lab)")
    print("-" * 80)
    stars = {}
    for n in (3, 4, 5):
        t0 = time.time()
        rows = curve_for_panel(panels[n], n, NOISE_LAB, rng)
        all_curves.extend(rows)
        ts = t_star(rows)
        stars[(n, NOISE_LAB)] = ts
        print(f"  n={n}  T*={ts if ts is not None else 'NONE'}  "
              f"({time.time() - t0:.1f}s)")
        print(f"    {'T':>6}  {'MI-AUC':>8}  {'RF-AUC':>8}")
        for r in rows:
            rf_s = f"{r['rf_auc']:.3f}" if not np.isnan(r["rf_auc"]) else "nan"
            print(f"    {r['T']:>6}  {r['mi_auc']:.3f}     {rf_s}")
        print()

    print("CURVES — noise=0.16 (n=3 stress)")
    print("-" * 80)
    t0 = time.time()
    rows_hi = curve_for_panel(panels[3], 3, NOISE_HI, rng)
    all_curves.extend(rows_hi)
    ts_hi = t_star(rows_hi)
    stars[(3, NOISE_HI)] = ts_hi
    print(f"  n=3 noise=0.16  T*={ts_hi if ts_hi is not None else 'NONE'}  "
          f"({time.time() - t0:.1f}s)")
    print(f"    {'T':>6}  {'MI-AUC':>8}  {'RF-AUC':>8}")
    for r in rows_hi:
        rf_s = f"{r['rf_auc']:.3f}" if not np.isnan(r["rf_auc"]) else "nan"
        print(f"    {r['T']:>6}  {r['mi_auc']:.3f}     {rf_s}")
    print()

    t3 = stars[(3, NOISE_LAB)]
    t4 = stars[(4, NOISE_LAB)]
    t5 = stars[(5, NOISE_LAB)]
    t3_hi = stars[(3, NOISE_HI)]

    h1 = ctrl and t3 is not None and t3 <= 1000
    # H2: grows with n
    if t3 is not None and t5 is not None:
        h2 = ctrl and t5 >= 2 * t3
    elif t3 is not None and t5 is None:
        h2 = ctrl  # n=5 never reaches — counts as growth/harder
    else:
        h2 = False
    # also note n=4
    h2_note = f"T*(3)={t3} T*(4)={t4} T*(5)={t5}"

    if t3 is not None and t3_hi is not None:
        h3 = ctrl and t3_hi >= 1.5 * t3
    elif t3 is not None and t3_hi is None:
        h3 = ctrl
    else:
        h3 = False

    if h1 and h2:
        verdict_word = "TSTAR_GROWS_WITH_N"
        reading = (
            f"TSTAR_GROWS_WITH_N — n=3 T*≤1000; size raises need ({h2_note}); "
            f"noise=0.16 T*={t3_hi}"
        )
    elif h1 and not h2:
        verdict_word = "TSTAR_FLAT_OR_EARLY"
        reading = (
            f"TSTAR_FLAT_OR_EARLY — n=3 reliable by T≤1000; T* does not "
            f"double by n=5 ({h2_note})"
        )
    elif not h1 and h2:
        verdict_word = "SLOW_AND_GROWS"
        reading = (
            f"SLOW_AND_GROWS — n=3 needs T*>1000; larger n harder ({h2_note})"
        )
    else:
        verdict_word = "SAMPLE_COMPLEXITY_MIXED"
        reading = (
            f"SAMPLE_COMPLEXITY_MIXED — H1/H2 fail pattern; "
            f"{h2_note}; noise T*={t3_hi}"
        )

    # refine with H3 in reading
    if h3:
        reading += "; higher noise raises T*"
    else:
        reading += "; higher noise does not clearly raise T*"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  T*(n=3, noise=0.08) = {t3}")
    print(f"  T*(n=4, noise=0.08) = {t4}")
    print(f"  T*(n=5, noise=0.08) = {t5}")
    print(f"  T*(n=3, noise=0.16) = {t3_hi}")
    print(f"  H1 (n=3 T*≤1000 at noise=0.08): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (T* grows with n):             "
          f"{'SUPPORTED' if h2 else 'REFUTED'}  ({h2_note})")
    print(f"  H3 (noise raises T* ≥1.5×):       "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  Tstar_n3={t3}  Tstar_n4={t4}  Tstar_n5={t5}  "
          f"Tstar_n3_noise16={t3_hi}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["n", "noise", "T", "n_forms", "n_tri", "mi_auc", "rf_auc"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_curves:
            w.writerow({
                "n": r["n"],
                "noise": r["noise"],
                "T": r["T"],
                "n_forms": r["n_forms"],
                "n_tri": r["n_tri"],
                "mi_auc": f"{r['mi_auc']:.6f}" if not np.isnan(r["mi_auc"]) else "",
                "rf_auc": (
                    f"{r['rf_auc']:.6f}" if not np.isnan(r["rf_auc"]) else ""
                ),
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "Tstar_n3": "" if t3 is None else t3,
            "Tstar_n4": "" if t4 is None else t4,
            "Tstar_n5": "" if t5 is None else t5,
            "Tstar_n3_noise16": "" if t3_hi is None else t3_hi,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)

    # panel inventory
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=["n", "name", "triadic", "max_phi"]
        )
        w.writeheader()
        for n, forms in sorted(panels.items()):
            for name, _, tri, phi in forms:
                w.writerow({
                    "n": n, "name": name, "triadic": tri,
                    "max_phi": f"{phi:.6f}",
                })


if __name__ == "__main__":
    main()
