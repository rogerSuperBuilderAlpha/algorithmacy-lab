"""Agenda #25 — active label acquisition for the cheap surrogate.

Reuses spectral_invariant panel (exact Φ labels + features). Hypotheses
fixed in hypotheses.md before computing.

Cited: ESTIMATION_ARC (#21–#23). Construct/omit/ladder closed.

Run:  python org_frontier/studies/active_label_acquisition/analyze_active.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PANEL = os.path.join(
    HERE, "..", "spectral_invariant", "results", "panel.csv"
)

FEATURE_COLS = [
    "mean_mi", "tc_per_node", "abs_oinfo",
    "adj_spectral_radius", "lap_lambda2", "lap_lambda_max",
    "lap_gap", "graph_energy", "vn_entropy",
    "P_second_mod", "P_spectral_gap",
]
POLICIES = ("random", "uncertainty", "diversity", "topo_balance")
SEED0 = 25
RF_N = 200
N_SEEDS_POOLED = 20
N_SEEDS_LOFO = 10
SEED_LABELED = 4
AUC_HIT = 0.85


def load_panel():
    with open(PANEL, newline="") as fh:
        rows = list(csv.DictReader(fh))
    X = np.array([[float(r[c]) for c in FEATURE_COLS] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    fam = np.array([r["family"] for r in rows])
    names = np.array([r["name"] for r in rows])
    return X, y, fam, names


def fit_proba(X_lab, y_lab, X_query, rng_state):
    if len(np.unique(y_lab)) < 2:
        # degenerate: predict majority
        p = float(y_lab.mean()) if len(y_lab) else 0.5
        return np.full(len(X_query), p)
    clf = RandomForestClassifier(
        n_estimators=RF_N, random_state=int(rng_state) % (2**31 - 1),
        n_jobs=1,
    )
    clf.fit(X_lab, y_lab)
    return clf.predict_proba(X_query)[:, 1]


def auc_safe(y, p):
    y = np.asarray(y, int)
    if y.sum() == 0 or y.sum() == len(y):
        return float("nan")
    try:
        return float(roc_auc_score(y, p))
    except ValueError:
        return float("nan")


def pick_seed(y, pool_idx, rng, k=SEED_LABELED):
    """Balanced seed from pool when possible."""
    pool_idx = np.asarray(pool_idx)
    tri = pool_idx[y[pool_idx] == 1]
    dya = pool_idx[y[pool_idx] == 0]
    half = k // 2
    chosen = []
    if len(tri) and len(dya):
        nt = min(half, len(tri))
        nd = min(k - nt, len(dya))
        chosen.extend(rng.choice(tri, nt, replace=False).tolist())
        chosen.extend(rng.choice(dya, nd, replace=False).tolist())
    while len(chosen) < min(k, len(pool_idx)):
        rem = [i for i in pool_idx if i not in chosen]
        if not rem:
            break
        chosen.append(int(rng.choice(rem)))
    return np.array(chosen, dtype=int)


def acquire_one(policy, labeled, unlabeled, X, y, fam, rng, proba_unlab):
    unlabeled = list(unlabeled)
    if not unlabeled:
        return None
    if policy == "random":
        return int(rng.choice(unlabeled))
    if policy == "uncertainty":
        # smallest |p-0.5|
        margins = np.abs(proba_unlab - 0.5)
        # map to unlabeled order
        return unlabeled[int(np.argmin(margins))]
    if policy == "diversity":
        Xs = StandardScaler().fit_transform(X)
        lab = np.asarray(labeled)
        unl = np.asarray(unlabeled)
        # distance to nearest labeled
        dmin = []
        for i in unl:
            d = np.linalg.norm(Xs[lab] - Xs[i], axis=1).min()
            dmin.append(d)
        return int(unl[int(np.argmax(dmin))])
    if policy == "topo_balance":
        # fewest labeled in family; tie-break uncertainty
        from collections import Counter
        counts = Counter(fam[i] for i in labeled)
        scores = []
        for j, i in enumerate(unlabeled):
            fam_count = counts.get(fam[i], 0)
            unc = abs(proba_unlab[j] - 0.5)
            scores.append((fam_count, unc, i))
        scores.sort()  # low fam_count, then low unc
        return int(scores[0][2])
    raise ValueError(policy)


def run_pooled_curve(X, y, fam, policy, rng):
    n = len(y)
    # stratified-ish test: take ~1/3, balanced
    idx = np.arange(n)
    tri = idx[y == 1]
    dya = idx[y == 0]
    n_te = max(4, n // 3)
    n_te_t = min(len(tri), n_te // 2)
    n_te_d = min(len(dya), n_te - n_te_t)
    te = np.concatenate([
        rng.choice(tri, n_te_t, replace=False),
        rng.choice(dya, n_te_d, replace=False),
    ])
    pool = np.array([i for i in idx if i not in set(te.tolist())])
    labeled = pick_seed(y, pool, rng)
    unlabeled = [i for i in pool if i not in set(labeled.tolist())]

    curve = []
    while True:
        p_te = fit_proba(X[labeled], y[labeled], X[te], rng.integers(1e9))
        curve.append({
            "n_labeled": len(labeled),
            "auc": auc_safe(y[te], p_te),
        })
        if not unlabeled:
            break
        p_u = fit_proba(
            X[labeled], y[labeled], X[unlabeled], rng.integers(1e9)
        )
        nxt = acquire_one(
            policy, labeled, unlabeled, X, y, fam, rng, p_u
        )
        labeled = np.append(labeled, nxt)
        unlabeled = [i for i in unlabeled if i != nxt]
    return curve


def run_lofo_curve(X, y, fam, policy, test_fam, rng):
    te = np.where(fam == test_fam)[0]
    pool = np.where(fam != test_fam)[0]
    if len(te) < 2 or len(pool) < SEED_LABELED + 2:
        return None
    if y[te].sum() == 0 or y[te].sum() == len(te):
        return None  # mono-class test — skip
    labeled = pick_seed(y, pool, rng)
    unlabeled = [i for i in pool if i not in set(labeled.tolist())]
    curve = []
    while True:
        p_te = fit_proba(X[labeled], y[labeled], X[te], rng.integers(1e9))
        curve.append({
            "n_labeled": len(labeled),
            "auc": auc_safe(y[te], p_te),
        })
        if not unlabeled:
            break
        p_u = fit_proba(
            X[labeled], y[labeled], X[unlabeled], rng.integers(1e9)
        )
        nxt = acquire_one(
            policy, labeled, unlabeled, X, y, fam, rng, p_u
        )
        labeled = np.append(labeled, nxt)
        unlabeled = [i for i in unlabeled if i != nxt]
    return curve


def mean_curve(curves):
    """Average AUC at each n_labeled across curves (nan-safe)."""
    if not curves:
        return [], []
    ns = sorted({c["n_labeled"] for curve in curves for c in curve})
    xs, ys = [], []
    for n in ns:
        vals = []
        for curve in curves:
            for c in curve:
                if c["n_labeled"] == n and not np.isnan(c["auc"]):
                    vals.append(c["auc"])
                    break
        if vals:
            xs.append(n)
            ys.append(float(np.mean(vals)))
    return xs, ys


def area(xs, ys, n_min):
    """Mean AUC for n_labeled > n_min."""
    pts = [y for x, y in zip(xs, ys) if x > n_min]
    return float(np.mean(pts)) if pts else float("nan")


def labels_to_hit(xs, ys, thr=AUC_HIT):
    for x, y in zip(xs, ys):
        if y >= thr:
            return int(x)
    return None


def main():
    print("AGENDA #25 — ACTIVE LABEL ACQUISITION")
    print("=" * 80)
    print("  cited: ESTIMATION_ARC (#21–#23); spectral_invariant panel")
    print("  oracle: exact Φ labels (precomputed); RF on spectral+coupling feats")
    print("  policies: random / uncertainty / diversity / topo_balance")
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

    t_all = time.time()
    X, y, fam, names = load_panel()
    print(f"PANEL  N={len(y)}  tri={int(y.sum())}  "
          f"families={sorted(set(fam.tolist()))}")
    print(f"  features: {len(FEATURE_COLS)}  "
          f"(from spectral_invariant/results/panel.csv)")
    print()

    # ---- Pooled holdout ----
    print("POOLED HOLDOUT CURVES")
    print("-" * 80)
    pooled_curves = {p: [] for p in POLICIES}
    for s in range(N_SEEDS_POOLED):
        rng = np.random.default_rng(SEED0 + s)
        for policy in POLICIES:
            # fresh rng stream per policy for fair seed labels... use same seed base
            rng_p = np.random.default_rng(SEED0 * 1000 + s * 17 + hash(policy) % 997)
            # Actually for fair comparison, same test split & seed labels per seed:
            pass
        # shared split/seed labels across policies
        rng_split = np.random.default_rng(SEED0 + s)
        idx = np.arange(len(y))
        tri = idx[y == 1]
        dya = idx[y == 0]
        n_te = max(4, len(y) // 3)
        n_te_t = min(len(tri), n_te // 2)
        n_te_d = min(len(dya), n_te - n_te_t)
        te = np.concatenate([
            rng_split.choice(tri, n_te_t, replace=False),
            rng_split.choice(dya, n_te_d, replace=False),
        ])
        pool = np.array([i for i in idx if i not in set(te.tolist())])
        labeled0 = pick_seed(y, pool, rng_split)

        for policy in POLICIES:
            rng_p = np.random.default_rng(SEED0 + s * 100 + POLICIES.index(policy))
            labeled = labeled0.copy()
            unlabeled = [i for i in pool if i not in set(labeled.tolist())]
            curve = []
            while True:
                p_te = fit_proba(
                    X[labeled], y[labeled], X[te], rng_p.integers(1e9)
                )
                curve.append({
                    "n_labeled": int(len(labeled)),
                    "auc": auc_safe(y[te], p_te),
                })
                if not unlabeled:
                    break
                p_u = fit_proba(
                    X[labeled], y[labeled], X[unlabeled], rng_p.integers(1e9)
                )
                nxt = acquire_one(
                    policy, labeled, unlabeled, X, y, fam, rng_p, p_u
                )
                labeled = np.append(labeled, nxt)
                unlabeled = [i for i in unlabeled if i != nxt]
            pooled_curves[policy].append(curve)

    pooled_mean = {}
    print(f"  {'policy':<14}{'meanAUC(>seed)':>16}{'T_to_0.85':>12}")
    for policy in POLICIES:
        xs, ys = mean_curve(pooled_curves[policy])
        pooled_mean[policy] = (xs, ys)
        a = area(xs, ys, SEED_LABELED)
        hit = labels_to_hit(xs, ys, AUC_HIT)
        hit_s = str(hit) if hit is not None else "NONE"
        print(f"  {policy:<14}{a:>16.3f}{hit_s:>12}")
    print()

    # ---- Topology holdout ----
    print("TOPOLOGY HOLDOUT (mixed-class families)")
    print("-" * 80)
    families = sorted(set(fam.tolist()))
    lofo_curves = {p: [] for p in POLICIES}
    usable = []
    for test_fam in families:
        te = np.where(fam == test_fam)[0]
        if len(te) < 2 or y[te].sum() == 0 or y[te].sum() == len(te):
            continue
        usable.append(test_fam)
        for s in range(N_SEEDS_LOFO):
            for policy in POLICIES:
                rng = np.random.default_rng(
                    SEED0 + 5000 + s * 50 + hash(test_fam + policy) % 10007
                )
                curve = run_lofo_curve(X, y, fam, policy, test_fam, rng)
                if curve is not None:
                    lofo_curves[policy].append(curve)

    print(f"  usable test families: {usable}")
    lofo_mean = {}
    # mid-budget: half of typical train size (~ (N - mean_test)/2 )
    mid_ns = []
    for policy in POLICIES:
        xs, ys = mean_curve(lofo_curves[policy])
        lofo_mean[policy] = (xs, ys)
        if xs:
            mid = xs[len(xs) // 2]
            mid_ns.append(mid)
    mid_n = int(np.median(mid_ns)) if mid_ns else SEED_LABELED + 4

    def auc_at(xs, ys, n):
        # nearest n_labeled
        if not xs:
            return float("nan")
        j = int(np.argmin([abs(x - n) for x in xs]))
        return ys[j]

    print(f"  mid-budget n_labeled≈{mid_n}")
    print(f"  {'policy':<14}{'AUC@mid':>10}{'meanAUC(>seed)':>16}")
    for policy in POLICIES:
        xs, ys = lofo_mean[policy]
        a_mid = auc_at(xs, ys, mid_n)
        a = area(xs, ys, SEED_LABELED)
        print(f"  {policy:<14}{a_mid:>10.3f}{a:>16.3f}")
    print()

    # ---- Hypothesis tests ----
    xs_r, ys_r = pooled_mean["random"]
    xs_u, ys_u = pooled_mean["uncertainty"]
    area_r = area(xs_r, ys_r, SEED_LABELED)
    area_u = area(xs_u, ys_u, SEED_LABELED)
    hit_r = labels_to_hit(xs_r, ys_r, AUC_HIT)
    hit_u = labels_to_hit(xs_u, ys_u, AUC_HIT)

    h1_area = (not np.isnan(area_u) and not np.isnan(area_r)
               and area_u >= area_r + 0.05)
    h1_hit = (
        hit_u is not None and hit_r is not None and hit_u <= 0.80 * hit_r
    )
    h1 = ctrl and (h1_area or h1_hit)

    xs_tb, ys_tb = lofo_mean["topo_balance"]
    xs_ul, ys_ul = lofo_mean["uncertainty"]
    mid_tb = auc_at(xs_tb, ys_tb, mid_n)
    mid_u = auc_at(xs_ul, ys_ul, mid_n)
    h2 = ctrl and (not np.isnan(mid_tb)) and (not np.isnan(mid_u)) and (
        mid_tb >= mid_u + 0.05
    )

    # H3: no policy beats random by 0.03 on pooled mean AUC
    best_nonrand = max(
        area(pooled_mean[p][0], pooled_mean[p][1], SEED_LABELED)
        for p in POLICIES if p != "random"
    )
    h3 = ctrl and (not np.isnan(best_nonrand)) and (
        best_nonrand <= area_r + 0.03
    )
    # mutual exclusion: if H1 then not H3
    if h1 and h3:
        h3 = False

    if h1 and h2:
        verdict_word = "UNCERTAINTY_AND_TOPO"
        reading = (
            "UNCERTAINTY_AND_TOPO — uncertainty beats random on pooled; "
            "topo_balance beats uncertainty under family holdout"
        )
    elif h1 and not h2:
        verdict_word = "UNCERTAINTY_WINS"
        reading = (
            "UNCERTAINTY_WINS — margin sampling beats random on pooled "
            "label-efficiency; topo_balance does not add under holdout"
        )
    elif h2 and not h1:
        verdict_word = "TOPO_HOLDOUT_GAINS"
        reading = (
            "TOPO_HOLDOUT_GAINS — topology-aware acquisition helps under "
            "family holdout; pooled uncertainty does not clear H1"
        )
    elif h3:
        verdict_word = "AL_NO_GAIN"
        reading = (
            "AL_NO_GAIN — no acquisition policy beats random by ≥0.03 on "
            "pooled curves; label order secondary on this panel"
        )
    else:
        verdict_word = "AL_PARTIAL"
        reading = (
            "AL_PARTIAL — mixed active-learning gains; see curves"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  pooled meanAUC  random={area_r:.3f}  uncertainty={area_u:.3f}  "
          f"Δ={area_u - area_r:+.3f}")
    print(f"  labels-to-{AUC_HIT}  random={hit_r}  uncertainty={hit_u}")
    print(f"  LOFO @mid  uncertainty={mid_u:.3f}  topo_balance={mid_tb:.3f}  "
          f"Δ={mid_tb - mid_u:+.3f}")
    print(f"  H1 (uncertainty ≻ random pooled): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (topo_balance ≻ unc. LOFO):    "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (no policy beats random):      "
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
    # write mean curves
    with open(os.path.join(RESULTS, "pooled_curves.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["policy", "n_labeled", "mean_auc"])
        w.writeheader()
        for policy in POLICIES:
            xs, ys = pooled_mean[policy]
            for x, yv in zip(xs, ys):
                w.writerow({
                    "policy": policy, "n_labeled": x,
                    "mean_auc": f"{yv:.6f}",
                })
    with open(os.path.join(RESULTS, "lofo_curves.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["policy", "n_labeled", "mean_auc"])
        w.writeheader()
        for policy in POLICIES:
            xs, ys = lofo_mean[policy]
            for x, yv in zip(xs, ys):
                w.writerow({
                    "policy": policy, "n_labeled": x,
                    "mean_auc": f"{yv:.6f}",
                })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "area_random": f"{area_r:.6f}",
            "area_uncertainty": f"{area_u:.6f}",
            "mid_uncertainty": f"{mid_u:.6f}",
            "mid_topo_balance": f"{mid_tb:.6f}",
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
