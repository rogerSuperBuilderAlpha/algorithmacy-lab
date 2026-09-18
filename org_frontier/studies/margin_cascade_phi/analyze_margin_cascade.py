"""Margin-cascade selective exact Φ on unc k=2 panels.

Cheap Probe-131 RF screens; exact IIT-4.0 Φ (cached triadic label) is substituted only on
out-of-fold uncertain forms. Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/margin_cascade_phi/analyze_margin_cascade.py
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
from sklearn.model_selection import cross_val_predict

FEATURES = (
    "n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
    "n_fixed", "n_reachable", "invertible", "max_period",
)
BUDGETS = (0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 1.0)
OP_POINTS = (0.10, 0.20)
N_RANDOM = 20
RANDOM_SEED = 0

PANELS = {
    "n4": {
        "path": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n4_unconstrained/results/"
            "residual_panel_n4_unconstrained.csv",
        ),
        "enriched": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/fn_tail_feature_redesign/results/enriched_n4.csv",
        ),
        "n_sample": 1000,
        "baseline_miss": 75,
        "baseline_fn": 30,
    },
    "n5": {
        "path": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n5_unconstrained/results/"
            "residual_panel_n5_unconstrained.csv",
        ),
        "enriched": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/fn_tail_feature_redesign/results/enriched_n5.csv",
        ),
        "n_sample": 500,
        "baseline_miss": 45,
        "baseline_fn": 21,
    },
}

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def load_panel(cfg):
    rows = list(csv.DictReader(open(cfg["path"])))
    assert len(rows) == cfg["n_sample"]
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    frag = None
    if os.path.exists(cfg["enriched"]):
        erows = list(csv.DictReader(open(cfg["enriched"])))
        assert len(erows) == len(rows)
        frag = np.array([float(r["struct_fragility"]) for r in erows])
    return X, y, frag


def oof_proba(X, y):
    # n_jobs=1: OOF ranks must be bit-stable for CI (parallel RF can reorder ties).
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=1)
    return cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]


def metrics(pred, y):
    pred = np.asarray(pred).astype(int)
    y = np.asarray(y).astype(int)
    n = len(y)
    n_tri = int(y.sum())
    n_dya = n - n_tri
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    miss = int((pred != y).sum())
    return {
        "n": n,
        "n_tri": n_tri,
        "n_miss": miss,
        "miss_rate": miss / n,
        "fp": fp,
        "fn": fn,
        "fn_among_tri": fn / n_tri if n_tri else float("nan"),
        "fp_among_dya": fp / n_dya if n_dya else float("nan"),
    }


def cascade(cheap_pred, y, score, budget):
    """Replace cheap preds with exact labels on the top-budget fraction by score."""
    n = len(y)
    k = int(round(budget * n))
    out = cheap_pred.copy()
    if k <= 0:
        return out, 0
    if k >= n:
        return y.copy(), n
    # higher score → call exact first
    order = np.argsort(-score, kind="mergesort")
    sel = order[:k]
    out = out.copy()
    out[sel] = y[sel]
    return out, k


def rank_avg(a, b):
    """Higher combined rank = more likely to call exact."""
    ra = np.argsort(np.argsort(-a))  # 0 = highest a
    rb = np.argsort(np.argsort(-b))
    # invert so higher score = call first: use negative mean rank
    return -(ra.astype(float) + rb.astype(float)) / 2.0


def curve_for(cheap_pred, y, score, budgets=BUDGETS):
    rows = []
    for b in budgets:
        pred, k = cascade(cheap_pred, y, score, b)
        m = metrics(pred, y)
        m["budget"] = b
        m["n_exact"] = k
        rows.append(m)
    return rows


def random_curve(cheap_pred, y, budgets, n_seeds=N_RANDOM):
    """Mean FN|tri / miss at each budget under random exact calls."""
    rng = np.random.default_rng(RANDOM_SEED)
    n = len(y)
    out = []
    for b in budgets:
        k = int(round(b * n))
        fns, misses = [], []
        for _ in range(n_seeds):
            pred = cheap_pred.copy()
            if k > 0:
                sel = rng.choice(n, size=min(k, n), replace=False)
                pred[sel] = y[sel]
            m = metrics(pred, y)
            fns.append(m["fn_among_tri"])
            misses.append(m["miss_rate"])
        out.append({
            "budget": b,
            "n_exact": k,
            "fn_among_tri_mean": float(np.mean(fns)),
            "fn_among_tri_std": float(np.std(fns)),
            "miss_rate_mean": float(np.mean(misses)),
            "miss_rate_std": float(np.std(misses)),
        })
    return out


def print_curve(tag, rows):
    print(f"  {tag}")
    print(f"    {'B':>5}  {'exact':>5}  {'miss':>8}  {'FN|tri':>10}  {'FP|dya':>8}")
    for m in rows:
        print(f"    {100 * m['budget']:4.0f}%  {m['n_exact']:5d}  "
              f"{100 * m['miss_rate']:6.1f}%  "
              f"{100 * m['fn_among_tri']:7.1f}% ({m['fn']}/{m['n_tri']})  "
              f"{100 * m['fp_among_dya']:6.1f}%")


def at_budget(rows, b):
    for m in rows:
        if abs(m["budget"] - b) < 1e-9:
            return m
    raise KeyError(b)


def instrument_control():
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    X, y, _ = load_panel(PANELS["n4"])
    proba = oof_proba(X, y)
    cheap = (proba >= 0.5).astype(int)
    m = metrics(cheap, y)
    ok = (m["n_miss"] == 75 and m["fn"] == 30)
    print(f"  n4 always-cheap miss/FN: {m['n_miss']}/{m['fn']}  "
          f"{'PASS' if ok else 'FAIL (expected 75/30)'}")
    if not ok:
        raise SystemExit("ABORT: baseline RF does not reproduce panel residual")
    print("  instrument control: PASS")
    print()
    return proba, cheap, y


def eval_panel(name, cfg, write_curves=True):
    X, y, frag = load_panel(cfg)
    proba = oof_proba(X, y)
    cheap = (proba >= 0.5).astype(int)
    margin = 1.0 - 2.0 * np.abs(proba - 0.5)  # high = uncertain
    m0 = metrics(cheap, y)

    margin_curve = curve_for(cheap, y, margin)
    frag_curve = curve_for(cheap, y, frag) if frag is not None else None
    comb_curve = curve_for(cheap, y, rank_avg(margin, frag)) if frag is not None else None
    rand_curve = random_curve(cheap, y, BUDGETS)

    print(f"{name.upper()} PANEL (N={cfg['n_sample']})")
    print("-" * 72)
    print(f"  always-cheap: miss={100 * m0['miss_rate']:.1f}% ({m0['n_miss']}/{m0['n']})  "
          f"FN|tri={100 * m0['fn_among_tri']:.1f}% ({m0['fn']}/{m0['n_tri']})  "
          f"FP|dya={100 * m0['fp_among_dya']:.1f}%")
    print(f"  always-exact: miss=0.0%  FN|tri=0.0%")
    print()
    print_curve("margin gate", margin_curve)
    print()
    if frag_curve is not None:
        print_curve("fragility gate", frag_curve)
        print()
        print_curve("combined gate (rank-avg)", comb_curve)
        print()
    print("  random gate (mean over "
          f"{N_RANDOM} seeds)")
    print(f"    {'B':>5}  {'exact':>5}  {'miss±':>12}  {'FN|tri±':>14}")
    for r in rand_curve:
        print(f"    {100 * r['budget']:4.0f}%  {r['n_exact']:5d}  "
              f"{100 * r['miss_rate_mean']:5.1f}±{100 * r['miss_rate_std']:.1f}%  "
              f"{100 * r['fn_among_tri_mean']:6.1f}±{100 * r['fn_among_tri_std']:.1f}%")
    print()

    if write_curves:
        os.makedirs(RESULTS, exist_ok=True)
        path = os.path.join(RESULTS, f"curve_{name}.csv")
        with open(path, "w", newline="") as fh:
            fields = ["gate", "budget", "n_exact", "miss_rate", "fn_among_tri",
                      "fp_among_dya", "n_miss", "fn", "fp"]
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            for gate, rows in (("margin", margin_curve),
                               ("fragility", frag_curve or []),
                               ("combined", comb_curve or [])):
                for m in rows:
                    w.writerow({
                        "gate": gate,
                        "budget": f"{m['budget']:.2f}",
                        "n_exact": m["n_exact"],
                        "miss_rate": f"{m['miss_rate']:.6f}",
                        "fn_among_tri": f"{m['fn_among_tri']:.6f}",
                        "fp_among_dya": f"{m['fp_among_dya']:.6f}",
                        "n_miss": m["n_miss"],
                        "fn": m["fn"],
                        "fp": m["fp"],
                    })
            for r in rand_curve:
                w.writerow({
                    "gate": "random_mean",
                    "budget": f"{r['budget']:.2f}",
                    "n_exact": r["n_exact"],
                    "miss_rate": f"{r['miss_rate_mean']:.6f}",
                    "fn_among_tri": f"{r['fn_among_tri_mean']:.6f}",
                    "fp_among_dya": "",
                    "n_miss": "",
                    "fn": "",
                    "fp": "",
                })

    return {
        "cheap": m0,
        "margin": margin_curve,
        "fragility": frag_curve,
        "combined": comb_curve,
        "random": rand_curve,
        "proba": proba,
        "y": y,
    }


def main():
    print("MARGIN-CASCADE SELECTIVE EXACT Φ — unc k=2")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  screen: Probe-125/131 RF OOF probs; exact Φ = cached triadic label")
    print("  cited: size series 4.8→7.5→9.0; F28; FN-redesign null (not reopened)")
    print("=" * 72)
    print()
    instrument_control()

    n4 = eval_panel("n4", PANELS["n4"])
    n5 = eval_panel("n5", PANELS["n5"])

    cheap_fn = n4["cheap"]["fn_among_tri"]
    m10 = at_budget(n4["margin"], 0.10)
    m20 = at_budget(n4["margin"], 0.20)
    r10 = at_budget(
        [{"budget": r["budget"], "fn_among_tri": r["fn_among_tri_mean"],
          "miss_rate": r["miss_rate_mean"], "fn": -1, "n_tri": n4["cheap"]["n_tri"],
          "n_exact": r["n_exact"], "n_miss": -1, "fp": -1, "fp_among_dya": float("nan"),
          "n": n4["cheap"]["n"]} for r in n4["random"]],
        0.10,
    )
    # recover r10 from random list properly
    r10_fn = next(r["fn_among_tri_mean"] for r in n4["random"] if abs(r["budget"] - 0.10) < 1e-9)
    c10 = at_budget(n4["combined"], 0.10) if n4["combined"] else None
    f10 = at_budget(n4["fragility"], 0.10) if n4["fragility"] else None

    d_fn_10 = cheap_fn - m10["fn_among_tri"]
    recovery_20 = 1.0 - (m20["fn_among_tri"] / cheap_fn) if cheap_fn > 0 else float("nan")
    d_rand = r10_fn - m10["fn_among_tri"]
    d_comb = (m10["fn_among_tri"] - c10["fn_among_tri"]) if c10 else float("nan")

    h1 = d_fn_10 >= 0.05
    h2 = recovery_20 >= 0.60
    h3 = d_rand >= 0.03
    h4 = d_comb >= 0.02

    cheap5 = n5["cheap"]["fn_among_tri"]
    m5_10 = at_budget(n5["margin"], 0.10)
    d5 = cheap5 - m5_10["fn_among_tri"]
    h5 = d5 >= 0.05

    print("n=4 HYPOTHESIS TESTS")
    print("-" * 72)
    print(f"  always-cheap FN|tri:           {100 * cheap_fn:.1f}% ({n4['cheap']['fn']}/{n4['cheap']['n_tri']})")
    print(f"  margin B=10% FN|tri:           {100 * m10['fn_among_tri']:.1f}% "
          f"({m10['fn']}/{m10['n_tri']})  miss={100 * m10['miss_rate']:.1f}%  exact={m10['n_exact']}")
    print(f"  margin B=20% FN|tri:           {100 * m20['fn_among_tri']:.1f}% "
          f"({m20['fn']}/{m20['n_tri']})  miss={100 * m20['miss_rate']:.1f}%  exact={m20['n_exact']}")
    print(f"  random B=10% FN|tri (mean):    {100 * r10_fn:.1f}%")
    if f10:
        print(f"  fragility B=10% FN|tri:        {100 * f10['fn_among_tri']:.1f}% ({f10['fn']}/{f10['n_tri']})")
    if c10:
        print(f"  combined B=10% FN|tri:         {100 * c10['fn_among_tri']:.1f}% ({c10['fn']}/{c10['n_tri']})")
    print(f"  Δ FN|tri cheap−margin@10%:     {100 * d_fn_10:+.1f} pp")
    print(f"  FN-gap recovery @20%:          {100 * recovery_20:.1f}%")
    print(f"  Δ FN|tri random−margin@10%:    {100 * d_rand:+.1f} pp")
    print(f"  Δ FN|tri margin−combined@10%:  {100 * d_comb:+.1f} pp")
    print(f"  H1 (B=10% FN drop ≥5 pp):      {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (B=20% recover ≥60% gap):   {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (margin beats random ≥3 pp):{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (combined − margin ≥2 pp):  {'SUPPORTED' if h4 else 'REFUTED'}")
    print()

    print("n=5 VALIDATION")
    print("-" * 72)
    print(f"  always-cheap FN|tri:           {100 * cheap5:.1f}% ({n5['cheap']['fn']}/{n5['cheap']['n_tri']})")
    print(f"  margin B=10% FN|tri:           {100 * m5_10['fn_among_tri']:.1f}% "
          f"({m5_10['fn']}/{m5_10['n_tri']})  miss={100 * m5_10['miss_rate']:.1f}%")
    print(f"  Δ FN|tri cheap−margin@10%:     {100 * d5:+.1f} pp")
    print(f"  H5 (n5 B=10% FN drop ≥5 pp):   {'SUPPORTED' if h5 else 'REFUTED'}")
    print()

    wins = sum([h1, h2, h3])
    if h1 and h2:
        reading = "WIN — cascade beats always-cheap at fixed budget"
    elif h1 or h2 or (d_fn_10 > 0 and recovery_20 >= 0.40):
        reading = "PARTIAL — directional cascade gain, below full H1/H2"
    else:
        reading = "NULL — cascade does not beat always-cheap at budget"

    # pick operating point: smallest B in OP_POINTS∪curve with FN|tri ≤ 0.5 * cheap
    half = 0.5 * cheap_fn
    op_b, op_m = None, None
    for m in n4["margin"]:
        if m["budget"] > 0 and m["fn_among_tri"] <= half + 1e-12:
            op_b, op_m = m["budget"], m
            break
    if op_m is None:
        op_b, op_m = 0.20, m20

    print("=" * 72)
    print("SUMMARY")
    print(f"  n4 cheap:     miss={100 * n4['cheap']['miss_rate']:.1f}%  "
          f"FN|tri={100 * cheap_fn:.1f}%")
    print(f"  n4 margin@10: miss={100 * m10['miss_rate']:.1f}%  "
          f"FN|tri={100 * m10['fn_among_tri']:.1f}%  exact={m10['n_exact']}/1000")
    print(f"  n4 margin@20: miss={100 * m20['miss_rate']:.1f}%  "
          f"FN|tri={100 * m20['fn_among_tri']:.1f}%  exact={m20['n_exact']}/1000")
    print(f"  n4 random@10: FN|tri={100 * r10_fn:.1f}% (mean)")
    if c10:
        print(f"  n4 combined@10: FN|tri={100 * c10['fn_among_tri']:.1f}%")
    print(f"  n5 cheap:     FN|tri={100 * cheap5:.1f}%")
    print(f"  n5 margin@10: FN|tri={100 * m5_10['fn_among_tri']:.1f}%")
    print(f"  operating pt: B={100 * op_b:.0f}%  FN|tri={100 * op_m['fn_among_tri']:.1f}%  "
          f"miss={100 * op_m['miss_rate']:.1f}%")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading:      {reading}")
    print("=" * 72)

    summary = {
        "n4_cheap_fn_tri": f"{cheap_fn:.6f}",
        "n4_margin10_fn_tri": f"{m10['fn_among_tri']:.6f}",
        "n4_margin10_miss": f"{m10['miss_rate']:.6f}",
        "n4_margin20_fn_tri": f"{m20['fn_among_tri']:.6f}",
        "n4_margin20_miss": f"{m20['miss_rate']:.6f}",
        "n4_random10_fn_tri": f"{r10_fn:.6f}",
        "n4_combined10_fn_tri": f"{c10['fn_among_tri']:.6f}" if c10 else "",
        "n4_fragility10_fn_tri": f"{f10['fn_among_tri']:.6f}" if f10 else "",
        "n5_cheap_fn_tri": f"{cheap5:.6f}",
        "n5_margin10_fn_tri": f"{m5_10['fn_among_tri']:.6f}",
        "recovery_20": f"{recovery_20:.6f}",
        "op_budget": f"{op_b:.2f}",
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "reading": reading,
    }
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
