"""Calibrate abstention τ vs top-B% ranking for the margin cascade.

Hypotheses fixed in hypotheses.md before computing. Extends margin_cascade_phi without
reopening that win.

Run:  python org_frontier/studies/margin_cascade_tau/analyze_tau_vs_b.py
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_predict

FEATURES = (
    "n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
    "n_fixed", "n_reachable", "invertible", "max_period",
)
TAU_GRID = (0.02, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40)
B_GRID = (0.05, 0.10, 0.15, 0.20, 0.25, 0.30)
CV = 5
SEED = 0

PANELS = {
    "n4": {
        "path": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n4_unconstrained/results/"
            "residual_panel_n4_unconstrained.csv",
        ),
        "n_sample": 1000,
    },
    "n5": {
        "path": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n5_unconstrained/results/"
            "residual_panel_n5_unconstrained.csv",
        ),
        "n_sample": 500,
    },
}

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def load_panel(cfg):
    rows = list(csv.DictReader(open(cfg["path"])))
    assert len(rows) == cfg["n_sample"]
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    return X, y


def oof_proba(X, y):
    # n_jobs=1: OOF ranks must be bit-stable for CI (parallel RF can reorder ties).
    clf = RandomForestClassifier(n_estimators=400, random_state=SEED, n_jobs=1)
    return cross_val_predict(clf, X, y, cv=CV, method="predict_proba")[:, 1]


def metrics(pred, y):
    pred = np.asarray(pred).astype(int)
    y = np.asarray(y).astype(int)
    n_tri = int(y.sum())
    n_dya = len(y) - n_tri
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    miss = int((pred != y).sum())
    return {
        "n": len(y),
        "n_tri": n_tri,
        "n_miss": miss,
        "miss_rate": miss / len(y),
        "fp": fp,
        "fn": fn,
        "fn_among_tri": fn / n_tri if n_tri else float("nan"),
        "fp_among_dya": fp / n_dya if n_dya else float("nan"),
    }


def apply_exact(cheap, y, mask):
    out = cheap.copy()
    out[mask] = y[mask]
    return out, int(mask.sum())


def top_b_mask(margin, b):
    """margin = |p-0.5|; select smallest B% (most uncertain)."""
    n = len(margin)
    k = int(round(b * n))
    if k <= 0:
        return np.zeros(n, dtype=bool)
    if k >= n:
        return np.ones(n, dtype=bool)
    order = np.argsort(margin, kind="mergesort")  # ascending |p-0.5|
    mask = np.zeros(n, dtype=bool)
    mask[order[:k]] = True
    return mask


def tau_mask(margin, tau):
    return margin < tau


def tau_for_budget(margin, b):
    """Smallest τ such that call rate >= B, via quantile of |p-0.5|."""
    n = len(margin)
    k = int(round(b * n))
    if k <= 0:
        return 0.0
    if k >= n:
        return float(np.max(margin) + 1e-12)
    order = np.sort(margin)
    # forms with margin < τ; to include exactly k smallest, τ just above order[k-1]
    # use mid between order[k-1] and order[k] when possible
    if k >= n:
        return float(order[-1] + 1e-12)
    lo = order[k - 1]
    hi = order[k] if k < n else lo + 1e-12
    return float(0.5 * (lo + hi)) if hi > lo else float(lo + 1e-12)


def curve_top_b(cheap, y, margin, budgets=B_GRID):
    rows = []
    for b in budgets:
        mask = top_b_mask(margin, b)
        pred, k = apply_exact(cheap, y, mask)
        m = metrics(pred, y)
        m["B"] = b
        m["n_exact"] = k
        m["call_rate"] = k / len(y)
        m["tau_equiv"] = tau_for_budget(margin, b)
        rows.append(m)
    return rows


def curve_fixed_tau(cheap, y, margin, taus=TAU_GRID):
    rows = []
    for tau in taus:
        mask = tau_mask(margin, tau)
        pred, k = apply_exact(cheap, y, mask)
        m = metrics(pred, y)
        m["tau"] = tau
        m["n_exact"] = k
        m["call_rate"] = k / len(y)
        rows.append(m)
    return rows


def nested_compare(cheap, y, margin, b, n_splits=CV):
    """Calibrate τ on other folds; apply to held-out. Compare to top-B% on same fold."""
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=SEED)
    pred_tau = cheap.copy()
    pred_top = cheap.copy()
    n_exact_tau = 0
    n_exact_top = 0
    taus = []
    for cal_idx, te_idx in kf.split(margin):
        tau = tau_for_budget(margin[cal_idx], b)
        taus.append(tau)
        m_tau = tau_mask(margin[te_idx], tau)
        m_top = top_b_mask(margin[te_idx], b)
        pred_tau[te_idx] = np.where(m_tau, y[te_idx], cheap[te_idx])
        pred_top[te_idx] = np.where(m_top, y[te_idx], cheap[te_idx])
        n_exact_tau += int(m_tau.sum())
        n_exact_top += int(m_top.sum())
    mt = metrics(pred_tau, y)
    mb = metrics(pred_top, y)
    return {
        "B": b,
        "tau_mean": float(np.mean(taus)),
        "tau_std": float(np.std(taus)),
        "tau_fn": mt["fn_among_tri"],
        "tau_miss": mt["miss_rate"],
        "tau_n_exact": n_exact_tau,
        "tau_call_rate": n_exact_tau / len(y),
        "top_fn": mb["fn_among_tri"],
        "top_miss": mb["miss_rate"],
        "top_n_exact": n_exact_top,
        "top_call_rate": n_exact_top / len(y),
        "abs_fn_delta": abs(mt["fn_among_tri"] - mb["fn_among_tri"]),
        "tau_fn_count": mt["fn"],
        "top_fn_count": mb["fn"],
        "n_tri": mt["n_tri"],
    }


def print_top_curve(tag, rows):
    print(f"  {tag}")
    print(f"    {'B':>5}  {'exact':>5}  {'τ_eq':>7}  {'miss':>7}  {'FN|tri':>12}")
    for m in rows:
        print(f"    {100 * m['B']:4.0f}%  {m['n_exact']:5d}  {m['tau_equiv']:7.4f}  "
              f"{100 * m['miss_rate']:5.1f}%  "
              f"{100 * m['fn_among_tri']:6.1f}% ({m['fn']}/{m['n_tri']})")


def print_tau_curve(tag, rows):
    print(f"  {tag}")
    print(f"    {'τ':>6}  {'call%':>6}  {'exact':>5}  {'miss':>7}  {'FN|tri':>12}")
    for m in rows:
        print(f"    {m['tau']:6.2f}  {100 * m['call_rate']:5.1f}%  {m['n_exact']:5d}  "
              f"{100 * m['miss_rate']:5.1f}%  "
              f"{100 * m['fn_among_tri']:6.1f}% ({m['fn']}/{m['n_tri']})")


def main():
    print("MARGIN-CASCADE τ vs TOP-B% CALIBRATION — unc k=2")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  cited: margin_cascade_phi WIN; size series; F28; FN-redesign null")
    print("=" * 72)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 72)
    X4, y4 = load_panel(PANELS["n4"])
    p4 = oof_proba(X4, y4)
    cheap4 = (p4 >= 0.5).astype(int)
    m0 = metrics(cheap4, y4)
    ok = (m0["n_miss"] == 75 and m0["fn"] == 30)
    print(f"  n4 always-cheap miss/FN: {m0['n_miss']}/{m0['fn']}  "
          f"{'PASS' if ok else 'FAIL (expected 75/30)'}")
    if not ok:
        raise SystemExit("ABORT: baseline RF does not reproduce panel residual")
    print("  instrument control: PASS")
    print()

    margin4 = np.abs(p4 - 0.5)
    top4 = curve_top_b(cheap4, y4, margin4)
    tau4 = curve_fixed_tau(cheap4, y4, margin4)
    # on-panel identity at B=10%
    tau_star = tau_for_budget(margin4, 0.10)
    id_mask = tau_mask(margin4, tau_star)
    top_mask = top_b_mask(margin4, 0.10)
    identity_agree = bool(np.array_equal(id_mask, top_mask))

    print("n=4 FULL-PANEL CURVES")
    print("-" * 72)
    print(f"  always-cheap: miss={100 * m0['miss_rate']:.1f}%  "
          f"FN|tri={100 * m0['fn_among_tri']:.1f}% ({m0['fn']}/{m0['n_tri']})")
    print(f"  on-panel τ*(B=10%)={tau_star:.6f}  identity with top-10%: "
          f"{'YES' if identity_agree else 'NO'}")
    print()
    print_top_curve("top-B% (τ_eq = on-panel quantile)", top4)
    print()
    print_tau_curve("fixed-τ (call rate data-dependent)", tau4)
    print()

    print("n=4 NESTED CALIBRATION (matched budget)")
    print("-" * 72)
    nested_rows = []
    for b in B_GRID:
        nested_rows.append(nested_compare(cheap4, y4, margin4, b))
    print(f"    {'B':>5}  {'τ_mean':>7}  {'τ call%':>8}  {'τ FN':>10}  "
          f"{'top FN':>10}  {'|Δ| pp':>7}")
    for r in nested_rows:
        print(f"    {100 * r['B']:4.0f}%  {r['tau_mean']:7.4f}  "
              f"{100 * r['tau_call_rate']:6.1f}%  "
              f"{100 * r['tau_fn']:6.1f}% ({r['tau_fn_count']})  "
              f"{100 * r['top_fn']:6.1f}% ({r['top_fn_count']})  "
              f"{100 * r['abs_fn_delta']:6.2f}")
    n10 = next(r for r in nested_rows if abs(r["B"] - 0.10) < 1e-9)
    print()

    # n=5
    X5, y5 = load_panel(PANELS["n5"])
    p5 = oof_proba(X5, y5)
    cheap5 = (p5 >= 0.5).astype(int)
    m5 = metrics(cheap5, y5)
    margin5 = np.abs(p5 - 0.5)
    top5 = curve_top_b(cheap5, y5, margin5)
    tau5_curve = curve_fixed_tau(cheap5, y5, margin5)
    top5_10 = next(r for r in top5 if abs(r["B"] - 0.10) < 1e-9)

    # frozen τ* from n4
    mask_frozen = tau_mask(margin5, tau_star)
    pred_frozen, k_frozen = apply_exact(cheap5, y5, mask_frozen)
    mf = metrics(pred_frozen, y5)
    call_frozen = k_frozen / len(y5)
    fn_gap = abs(mf["fn_among_tri"] - top5_10["fn_among_tri"])

    print("n=5 VALIDATION + FROZEN-τ TRANSFER")
    print("-" * 72)
    print(f"  always-cheap: miss={100 * m5['miss_rate']:.1f}%  "
          f"FN|tri={100 * m5['fn_among_tri']:.1f}% ({m5['fn']}/{m5['n_tri']})")
    print(f"  top-B%=10%:   miss={100 * top5_10['miss_rate']:.1f}%  "
          f"FN|tri={100 * top5_10['fn_among_tri']:.1f}% "
          f"({top5_10['fn']}/{top5_10['n_tri']})  exact={top5_10['n_exact']}")
    print(f"  frozen τ*={tau_star:.6f} from n4@10%:")
    print(f"    call rate={100 * call_frozen:.1f}%  exact={k_frozen}/500  "
          f"miss={100 * mf['miss_rate']:.1f}%  "
          f"FN|tri={100 * mf['fn_among_tri']:.1f}% ({mf['fn']}/{mf['n_tri']})")
    print(f"    |FN τ* − FN top10%|={100 * fn_gap:.1f} pp")
    print()
    print_tau_curve("n5 fixed-τ curve", tau5_curve)
    print()

    # hypotheses
    h1 = n10["abs_fn_delta"] <= 0.02
    h2_rate = 0.05 <= call_frozen <= 0.15
    h2_fn = fn_gap <= 0.03
    h2 = h2_rate and h2_fn

    if h1 and h2:
        recommend = "B=10% top-B% (τ*={:.4f} on-panel equivalent; frozen τ transfers)".format(
            tau_star)
        h3 = True
    elif h1 and not h2:
        recommend = "B=10% top-B% only (recompute ranks per panel; frozen τ transfer failed)"
        h3 = True
    elif not h1 and h2:
        recommend = "frozen τ*={:.4f} from n4@10% (nested rules disagreed; transfer ok)".format(
            tau_star)
        h3 = True
    else:
        recommend = "NO STABLE DEFAULT"
        h3 = False

    print("HYPOTHESIS TESTS")
    print("-" * 72)
    print(f"  nested@10% τ FN|tri:           {100 * n10['tau_fn']:.1f}% "
          f"({n10['tau_fn_count']}/{n10['n_tri']})")
    print(f"  nested@10% top FN|tri:         {100 * n10['top_fn']:.1f}% "
          f"({n10['top_fn_count']}/{n10['n_tri']})")
    print(f"  nested@10% |Δ|:                {100 * n10['abs_fn_delta']:.2f} pp")
    print(f"  frozen τ* n5 call rate:        {100 * call_frozen:.1f}% "
          f"(band [5%, 15%]: {'IN' if h2_rate else 'OUT'})")
    print(f"  frozen τ* n5 FN|tri:           {100 * mf['fn_among_tri']:.1f}%")
    print(f"  n5 top-10% FN|tri:             {100 * top5_10['fn_among_tri']:.1f}%")
    print(f"  |FN frozen − top10%|:          {100 * fn_gap:.1f} pp")
    print(f"  H1 (nested |Δ| ≤2 pp @10%):    {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (frozen τ transfers):       {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (stable lab default):       {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  recommend:                     {recommend}")
    print()

    if h1 and h2 and h3:
        reading = "AGREE+TRANSFER — τ ≈ top-B%; frozen τ OK; default B=10%"
    elif h1 and h3 and not h2:
        reading = "AGREE — nested τ ≈ top-B%; prefer top-B% across sizes (frozen τ drifts)"
    elif h3:
        reading = "PARTIAL — stable default despite rule tension"
    else:
        reading = "NULL — no stable (τ, B) recommendation"

    print("=" * 72)
    print("SUMMARY")
    print(f"  n4 cheap FN|tri:               {100 * m0['fn_among_tri']:.1f}%")
    print(f"  n4 top-10% FN|tri:             "
          f"{100 * next(r['fn_among_tri'] for r in top4 if abs(r['B']-0.10)<1e-9):.1f}%")
    print(f"  n4 nested τ@10% FN|tri:        {100 * n10['tau_fn']:.1f}%")
    print(f"  n4 nested top@10% FN|tri:      {100 * n10['top_fn']:.1f}%")
    print(f"  n4 τ*(B=10%):                  {tau_star:.6f}")
    print(f"  n5 top-10% FN|tri:             {100 * top5_10['fn_among_tri']:.1f}%")
    print(f"  n5 frozen-τ FN|tri:            {100 * mf['fn_among_tri']:.1f}%  "
          f"call={100 * call_frozen:.1f}%")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading:                       {reading}")
    print(f"  lab default:                   {recommend}")
    print("=" * 72)

    os.makedirs(RESULTS, exist_ok=True)
    # curves
    with open(os.path.join(RESULTS, "curve_n4_topb.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["B", "n_exact", "tau_equiv", "miss_rate",
                                           "fn_among_tri", "fn", "n_tri"])
        w.writeheader()
        for m in top4:
            w.writerow({
                "B": f"{m['B']:.2f}", "n_exact": m["n_exact"],
                "tau_equiv": f"{m['tau_equiv']:.6f}",
                "miss_rate": f"{m['miss_rate']:.6f}",
                "fn_among_tri": f"{m['fn_among_tri']:.6f}",
                "fn": m["fn"], "n_tri": m["n_tri"],
            })
    with open(os.path.join(RESULTS, "curve_n4_tau.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["tau", "call_rate", "n_exact", "miss_rate",
                                           "fn_among_tri", "fn", "n_tri"])
        w.writeheader()
        for m in tau4:
            w.writerow({
                "tau": f"{m['tau']:.2f}", "call_rate": f"{m['call_rate']:.6f}",
                "n_exact": m["n_exact"], "miss_rate": f"{m['miss_rate']:.6f}",
                "fn_among_tri": f"{m['fn_among_tri']:.6f}",
                "fn": m["fn"], "n_tri": m["n_tri"],
            })
    with open(os.path.join(RESULTS, "nested_n4.csv"), "w", newline="") as fh:
        fields = list(nested_rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in nested_rows:
            row = {k: (f"{v:.6f}" if isinstance(v, float) else v) for k, v in r.items()}
            w.writerow(row)

    summary = {
        "n4_cheap_fn": f"{m0['fn_among_tri']:.6f}",
        "n4_tau_star": f"{tau_star:.6f}",
        "n4_identity_top10": "YES" if identity_agree else "NO",
        "n4_nested10_tau_fn": f"{n10['tau_fn']:.6f}",
        "n4_nested10_top_fn": f"{n10['top_fn']:.6f}",
        "n4_nested10_abs_delta": f"{n10['abs_fn_delta']:.6f}",
        "n5_top10_fn": f"{top5_10['fn_among_tri']:.6f}",
        "n5_frozen_fn": f"{mf['fn_among_tri']:.6f}",
        "n5_frozen_call": f"{call_frozen:.6f}",
        "n5_fn_gap": f"{fn_gap:.6f}",
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "reading": reading,
        "recommend": recommend,
    }
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
