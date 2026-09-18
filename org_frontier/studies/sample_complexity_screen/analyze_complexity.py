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
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import (
    entropy,
    mutual_information,
    o_information,
    transfer_entropy,
)
from org_frontier.probes.lib import verdict as vlib
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_threshold_scaling import threshold_hub
from org_frontier.probes.probe_symmetric_multihub import sym_two_hub

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


def broadcast(n):
    rules = [None] * n
    rules[0] = lambda x: x[1] if n > 1 else 0
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def chain_feedforward(n):
    rules = [None] * n
    rules[0] = lambda x: x[0]
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[i - 1])
    return rules


def broken_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n - 1):
        rules[i] = (lambda x, i=i: x[0])
    rules[n - 1] = lambda x: x[n - 1]
    return rules


def hub_family_forms(n):
    """Same mediation class across sizes (for H2 size scaling)."""
    return [
        ("and_hub", single_hub(n)),
        ("or_hub", or_hub(n)),
        ("parity_hub", parity_hub(n)),
        ("broadcast", broadcast(n)),
        ("broken_hub", broken_hub(n)),
        ("maj_hub", threshold_hub(n, (n - 1) // 2 + 1)),
        ("or_thresh", threshold_hub(n, 1)),
        ("and_thresh2", threshold_hub(n, min(2, n - 1))),
    ]


def cross_topo_forms(n):
    """Multi-topology panel (#134 stress) — secondary."""
    out = hub_family_forms(n) + [
        ("chain_and", chain(n)),
        ("chain_ff", chain_feedforward(n)),
        ("pool_and", pool(n)),
    ]
    if n >= 4:
        out.append(("two_hub", two_hub(n)))
    if n >= 5:
        out.append(("two_hub_sym", sym_two_hub(n)))
    return out


def label_forms(tag_rules, n):
    forms = []
    for name, rules in tag_rules:
        v = classify_rules(rules, labels=labels_for(n))
        forms.append((
            f"{name}_n{n}", rules,
            int(v.structure == "triadic"), float(v.max_phi),
        ))
    return forms


def build_panels(rng):
    """family_n3 + hub size series + cross-topo secondary."""
    panels = {}

    tri, dya = [], []
    for name, rules in enumerate_family():
        v = classify_rules(rules, labels=labels_for(3))
        bucket = tri if v.structure == "triadic" else dya
        bucket.append((name, rules, int(v.structure == "triadic"), float(v.max_phi)))
    n_take = min(24, len(tri), len(dya))
    pick_t = [tri[i] for i in rng.choice(len(tri), n_take, replace=False)]
    pick_d = [dya[i] for i in rng.choice(len(dya), n_take, replace=False)]
    panels["family_n3"] = pick_t + pick_d

    for n in (3, 4, 5):
        panels[f"hub_n{n}"] = label_forms(hub_family_forms(n), n)
    for n in (4, 5):
        panels[f"cross_n{n}"] = label_forms(cross_topo_forms(n), n)

    return panels


def simulate_long(rules, n, noise, rng):
    tpm = add_noise(tpm_from_rules(rules), noise)
    return exact_phi.simulate_trajectory(tpm, n, T_MAX, rng)


def curve_for_panel(forms, n, noise, rng, panel_id):
    """Return per-T rows: mi_auc, rf_auc, n_forms, n_tri."""
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
        if 0 < y.sum() < len(y) and len(y) >= 6:
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
            "panel": panel_id,
            "n": n,
            "noise": noise,
            "T": T,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": mi_auc,
            "rf_auc": rf_auc,
        })
    return rows


def t_star(curve_rows, key="mi_auc"):
    """Smallest T with score ≥ target; None if never."""
    for r in sorted(curve_rows, key=lambda z: z["T"]):
        v = r[key]
        if not np.isnan(v) and v >= AUC_TARGET:
            return int(r["T"])
    return None


def print_curve(label, rows, ts_mi, ts_rf, dt):
    print(f"  {label}  T*_MI={ts_mi if ts_mi is not None else 'NONE'}  "
          f"T*_RF={ts_rf if ts_rf is not None else 'NONE'}  ({dt:.1f}s)")
    print(f"    {'T':>6}  {'MI-AUC':>8}  {'RF-AUC':>8}")
    for r in rows:
        rf_s = f"{r['rf_auc']:.3f}" if not np.isnan(r["rf_auc"]) else "nan"
        mi_s = f"{r['mi_auc']:.3f}" if not np.isnan(r["mi_auc"]) else "nan"
        print(f"    {r['T']:>6}  {mi_s:>8}  {rf_s:>8}")
    print()


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
    for pid, forms in panels.items():
        n_tri = sum(f[2] for f in forms)
        print(f"  {pid}: {len(forms)} forms ({n_tri} tri / "
              f"{len(forms) - n_tri} dya)")
    print()

    all_curves = []
    stars = {}

    def run(panel_id, n, noise, label):
        t0 = time.time()
        rows = curve_for_panel(panels[panel_id], n, noise, rng, panel_id)
        # tag noise in panel key for curves
        for r in rows:
            r["panel"] = f"{panel_id}_noise{noise}"
        all_curves.extend(rows)
        ts_mi = t_star(rows, "mi_auc")
        ts_rf = t_star(rows, "rf_auc")
        stars[(panel_id, noise)] = (ts_mi, ts_rf)
        print_curve(label, rows, ts_mi, ts_rf, time.time() - t0)
        return ts_mi, ts_rf

    print("CURVES — family n=3 + hub size series (noise=0.08)")
    print("-" * 80)
    t3_mi, t3_rf = run("family_n3", 3, NOISE_LAB, "family_n3")
    hub_mi = {}
    hub_rf = {}
    for n in (3, 4, 5):
        mi, rf = run(f"hub_n{n}", n, NOISE_LAB, f"hub_n{n}")
        hub_mi[n], hub_rf[n] = mi, rf

    print("CURVES — cross-topo secondary (noise=0.08)")
    print("-" * 80)
    for n in (4, 5):
        run(f"cross_n{n}", n, NOISE_LAB, f"cross_n{n}")

    print("CURVES — noise=0.16 (family n=3 stress)")
    print("-" * 80)
    t3_hi_mi, t3_hi_rf = run("family_n3", 3, NOISE_HI, "family_n3 noise=0.16")

    h1 = ctrl and t3_mi is not None and t3_mi <= 1000

    hm3, hm5 = hub_mi[3], hub_mi[5]
    if hm3 is not None and hm5 is not None:
        h2 = ctrl and hm5 >= 2 * hm3
    elif hm3 is not None and hm5 is None:
        h2 = ctrl
    else:
        h2 = False
    h2_note = f"hub T*_MI n3={hm3} n4={hub_mi[4]} n5={hm5}"

    if t3_mi is not None and t3_hi_mi is not None:
        h3 = ctrl and t3_hi_mi >= 1.5 * t3_mi
    elif t3_mi is not None and t3_hi_mi is None:
        h3 = ctrl
    else:
        h3 = False

    if h1 and h2:
        verdict_word = "FAST_N3_HARDER_WITH_N"
        reading = (
            f"FAST_N3_HARDER_WITH_N — family n=3 T*_MI={t3_mi}; "
            f"within-hub size raises need ({h2_note}); "
            f"noise0.16 T*={t3_hi_mi}"
        )
    elif h1 and not h2:
        verdict_word = "FAST_WITHIN_FAMILY"
        reading = (
            f"FAST_WITHIN_FAMILY — family n=3 T*_MI={t3_mi}≤1000; "
            f"within-hub T* does not double by n=5 ({h2_note}); "
            f"noise0.16 T*={t3_hi_mi}"
        )
    else:
        verdict_word = "SAMPLE_COMPLEXITY_MIXED"
        reading = (
            f"SAMPLE_COMPLEXITY_MIXED — H1/H2 pattern; family T*={t3_mi}; "
            f"{h2_note}; noise T*={t3_hi_mi}"
        )
    if h3:
        reading += "; higher noise raises T*"
    else:
        reading += "; higher noise does not raise T*"
    # cross-topo note always
    cross4 = stars.get(("cross_n4", NOISE_LAB), (None, None))[0]
    cross5 = stars.get(("cross_n5", NOISE_LAB), (None, None))[0]
    reading += (
        f"; cross-topo MI T* n4={cross4} n5={cross5} "
        f"(longer T does not fix #134)"
    )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  T*_MI family_n3 noise0.08 = {t3_mi}  (RF {t3_rf})")
    print(f"  T*_MI hub n3/n4/n5         = {hm3}/{hub_mi[4]}/{hm5}  "
          f"(RF {hub_rf[3]}/{hub_rf[4]}/{hub_rf[5]})")
    print(f"  T*_MI family_n3 noise0.16  = {t3_hi_mi}  (RF {t3_hi_rf})")
    print(f"  T*_MI cross n4/n5          = {cross4}/{cross5}")
    print(f"  H1 (family n=3 T*≤1000):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (hub T* grows with n): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}  ({h2_note})")
    print(f"  H3 (noise raises T*≥1.5×):"
          f" {'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  Tstar_family_n3={t3_mi}  Tstar_hub_n3={hm3}  "
          f"Tstar_hub_n5={hm5}  Tstar_noise16={t3_hi_mi}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["panel", "n", "noise", "T", "n_forms", "n_tri",
                  "mi_auc", "rf_auc"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_curves:
            w.writerow({
                "panel": r["panel"],
                "n": r["n"],
                "noise": r["noise"],
                "T": r["T"],
                "n_forms": r["n_forms"],
                "n_tri": r["n_tri"],
                "mi_auc": (
                    f"{r['mi_auc']:.6f}" if not np.isnan(r["mi_auc"]) else ""
                ),
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
            "Tstar_family_n3": "" if t3_mi is None else t3_mi,
            "Tstar_hub_n3": "" if hm3 is None else hm3,
            "Tstar_hub_n5": "" if hm5 is None else hm5,
            "Tstar_noise16": "" if t3_hi_mi is None else t3_hi_mi,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=["panel", "n", "name", "triadic", "max_phi"]
        )
        w.writeheader()
        for pid, forms in panels.items():
            n = 3 if "n3" in pid or pid == "family_n3" else (
                4 if "n4" in pid else 5
            )
            for name, _, tri, phi in forms:
                w.writerow({
                    "panel": pid, "n": n, "name": name, "triadic": tri,
                    "max_phi": f"{phi:.6f}",
                })


if __name__ == "__main__":
    main()
