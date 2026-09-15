"""Feature redesign for the triadic FN tail on unc k=2 panels.

Baseline = Probe-125/131 ten features. Redesign adds F28-motivated cheap fragility and
algebraic table features. Exact Φ remains the label. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/fn_tail_feature_redesign/analyze_fn_redesign.py
      python org_frontier/studies/fn_tail_feature_redesign/analyze_fn_redesign.py --rebuild
"""

import argparse
import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_predict

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.multiparty.run import _fn, _rand_table
from org_frontier.studies.holistic_residual_n4.analyze_residual_n4 import (
    FEATURES as BASE_FEATURES,
    _dynamics,
    _strongly_connected,
    node_synergy,
)

PARITY = {(0, 1, 1, 0), (1, 0, 0, 1)}
NEW_FEATURES = (
    "struct_fragility", "dyn_fragility", "syn_fragility",
    "n_parity", "n_affine", "n_both_dep", "mean_balance",
)
ALL_FEATURES = tuple(BASE_FEATURES) + NEW_FEATURES

PANELS = {
    "n4": {
        "path": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n4_unconstrained/results/"
            "residual_panel_n4_unconstrained.csv",
        ),
        "n_nodes": 4, "n_sample": 1000, "seed": 40,
        "baseline_miss": 75, "baseline_fn_tri": 30, "baseline_n_tri": 297,
    },
    "n5": {
        "path": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n5_unconstrained/results/"
            "residual_panel_n5_unconstrained.csv",
        ),
        "n_nodes": 5, "n_sample": 500, "seed": 50,
        "baseline_miss": 45, "baseline_fn_tri": 21, "baseline_n_tri": 85,
    },
}

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def sample_k2(rng, n_nodes):
    rules = [None] * n_nodes
    tables = [None] * n_nodes
    inputs = [None] * n_nodes
    for j in range(n_nodes):
        others = [k for k in range(n_nodes) if k != j]
        idxs = tuple(int(x) for x in rng.choice(others, size=2, replace=False))
        t = _rand_table(rng, 2)
        rules[j] = _fn(t, idxs)
        tables[j] = t
        inputs[j] = idxs
    return rules, tables, inputs


def is_affine_2(t):
    return t[3] == (t[0] ^ t[1] ^ t[2])


def depends_both(t):
    return ((t[0] != t[1]) or (t[2] != t[3])) and ((t[0] != t[2]) or (t[1] != t[3]))


def table_balance(t):
    return abs(2.0 * sum(t) / 4.0 - 1.0)


def enrich_form(tables, inputs, n_nodes):
    """Cheap redesign features; no exact Φ."""
    base_rules = [_fn(tables[j], inputs[j]) for j in range(n_nodes)]
    cm0 = cm_from_rules(base_rules)
    e0 = int(cm0.sum())
    b0 = int(sum((cm0[:, i].sum() > 0 and cm0[i, :].sum() > 0) for i in range(n_nodes)))
    sc0 = int(_strongly_connected(cm0))
    fix0, reach0, inv0, per0 = _dynamics(base_rules)
    syn0 = sum(node_synergy(t, 2) for t in tables)

    n_struct = n_dyn = 0
    syn_deltas = []
    n_neigh = 0
    for node in range(n_nodes):
        for bit in range(4):
            nt = list(tables[node])
            nt[bit] = 1 - nt[bit]
            new_tables = list(tables)
            new_tables[node] = tuple(nt)
            rules = [_fn(new_tables[j], inputs[j]) for j in range(n_nodes)]
            cm = cm_from_rules(rules)
            e = int(cm.sum())
            b = int(sum((cm[:, i].sum() > 0 and cm[i, :].sum() > 0) for i in range(n_nodes)))
            sc = int(_strongly_connected(cm))
            fix, reach, inv, per = _dynamics(rules)
            syn = sum(node_synergy(t, 2) for t in new_tables)
            n_neigh += 1
            n_struct += int((e, b, sc) != (e0, b0, sc0))
            n_dyn += int((fix, reach, inv, per) != (fix0, reach0, inv0, per0))
            syn_deltas.append(abs(syn - syn0))

    return {
        "struct_fragility": n_struct / n_neigh,
        "dyn_fragility": n_dyn / n_neigh,
        "syn_fragility": float(np.mean(syn_deltas)),
        "n_parity": sum(1 for t in tables if t in PARITY),
        "n_affine": sum(1 for t in tables if is_affine_2(t)),
        "n_both_dep": sum(1 for t in tables if depends_both(t)),
        "mean_balance": float(np.mean([table_balance(t) for t in tables])),
    }


def build_enriched(name, cfg):
    rows = list(csv.DictReader(open(cfg["path"])))
    assert len(rows) == cfg["n_sample"]
    rng = np.random.default_rng(cfg["seed"])
    out = []
    start = time.time()
    print(f"ENRICH {name} — N={cfg['n_sample']} n_nodes={cfg['n_nodes']} seed={cfg['seed']}")
    for k, row in enumerate(rows):
        _, tables, inputs = sample_k2(rng, cfg["n_nodes"])
        extra = enrich_form(tables, inputs, cfg["n_nodes"])
        rec = {f: float(row[f]) for f in BASE_FEATURES}
        rec["triadic"] = int(row["triadic"])
        rec["idx"] = k
        rec.update(extra)
        out.append(rec)
        if (k + 1) % 200 == 0 or (k + 1) == cfg["n_sample"]:
            print(f"  {k + 1}/{cfg['n_sample']}  ({time.time() - start:.0f}s)")
    path = os.path.join(RESULTS, f"enriched_{name}.csv")
    os.makedirs(RESULTS, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    print(f"  wrote {path}")
    print()
    return out


def load_enriched(name):
    path = os.path.join(RESULTS, f"enriched_{name}.csv")
    return list(csv.DictReader(open(path)))


def eval_features(rows, feature_names, label=""):
    X = np.array([[float(r[f]) for f in feature_names] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    miss = pred != y
    n = len(y)
    n_tri = int(y.sum())
    n_dya = n - n_tri
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    auc = float(roc_auc_score(y, proba)) if len(set(y)) > 1 else float("nan")
    # importances from a full fit (descriptive)
    clf.fit(X, y)
    imp = sorted(zip(feature_names, clf.feature_importances_), key=lambda t: -t[1])
    return {
        "label": label,
        "n": n,
        "n_tri": n_tri,
        "n_miss": int(miss.sum()),
        "miss_rate": float(miss.mean()),
        "fp": fp,
        "fn": fn,
        "fn_among_tri": fn / n_tri if n_tri else float("nan"),
        "fp_among_dya": fp / n_dya if n_dya else float("nan"),
        "auc": auc,
        "n_pred_tri": int(pred.sum()),
        "importances": imp,
        "proba": proba,
        "pred": pred,
        "y": y,
    }


def transfer_eval(train_rows, test_rows, feature_names, label=""):
    Xtr = np.array([[float(r[f]) for f in feature_names] for r in train_rows])
    ytr = np.array([int(r["triadic"]) for r in train_rows])
    Xte = np.array([[float(r[f]) for f in feature_names] for r in test_rows])
    yte = np.array([int(r["triadic"]) for r in test_rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    clf.fit(Xtr, ytr)
    proba = clf.predict_proba(Xte)[:, 1]
    pred = (proba >= 0.5).astype(int)
    n_tri = int(yte.sum())
    n_dya = len(yte) - n_tri
    fp = int(((pred == 1) & (yte == 0)).sum())
    fn = int(((pred == 0) & (yte == 1)).sum())
    auc = float(roc_auc_score(yte, proba)) if len(set(yte)) > 1 else float("nan")
    return {
        "label": label,
        "n": len(yte),
        "n_tri": n_tri,
        "n_miss": int((pred != yte).sum()),
        "miss_rate": float((pred != yte).mean()),
        "fp": fp,
        "fn": fn,
        "fn_among_tri": fn / n_tri if n_tri else float("nan"),
        "fp_among_dya": fp / n_dya if n_dya else float("nan"),
        "auc": auc,
    }


def print_metrics(m, tag):
    print(f"  {tag:<28} miss={100 * m['miss_rate']:.1f}% ({m['n_miss']}/{m['n']})  "
          f"FN|tri={100 * m['fn_among_tri']:.1f}% ({m['fn']}/{m['n_tri']})  "
          f"FP|dya={100 * m['fp_among_dya']:.1f}%  AUC={m['auc']:.3f}")


def instrument_control():
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    # baseline on n4 committed panel must reproduce 75 misses / 30 FN
    rows = list(csv.DictReader(open(PANELS["n4"]["path"])))
    base = eval_features(rows, BASE_FEATURES, "baseline-check")
    ok = (base["n_miss"] == 75 and base["fn"] == 30)
    print(f"  n4 baseline miss/FN: {base['n_miss']}/{base['fn']}  "
          f"{'PASS' if ok else 'FAIL (expected 75/30)'}")
    if not ok:
        raise SystemExit("ABORT: baseline RF does not reproduce panel residual")
    print("  instrument control: PASS")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true",
                    help="recompute enriched feature CSVs (cheap; no exact Φ)")
    args = ap.parse_args()

    print("FN-TAIL FEATURE REDESIGN — unc k=2 panels")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  baseline: Probe-125/131 features; redesign: +fragility +algebraic")
    print("  size series cited: 4.8% → 7.5% → 9.0% (not reopened)")
    print("=" * 72)
    print()
    instrument_control()

    data = {}
    for name, cfg in PANELS.items():
        path = os.path.join(RESULTS, f"enriched_{name}.csv")
        if args.rebuild or not os.path.exists(path):
            data[name] = build_enriched(name, cfg)
        else:
            data[name] = load_enriched(name)
            print(f"LOADED enriched_{name}.csv ({len(data[name])} rows)")
    print()

    print("n=4 COMPARISON (primary)")
    print("-" * 72)
    b4 = eval_features(data["n4"], BASE_FEATURES, "baseline")
    r4 = eval_features(data["n4"], ALL_FEATURES, "redesign")
    print_metrics(b4, "baseline")
    print_metrics(r4, "redesign")
    d_fn = b4["fn_among_tri"] - r4["fn_among_tri"]
    d_miss = b4["miss_rate"] - r4["miss_rate"]
    h1 = d_fn >= 0.05
    h2 = d_miss >= 0.01
    print(f"  Δ FN|tri (base − redes):    {100 * d_fn:+.1f} pp")
    print(f"  Δ miss (base − redes):      {100 * d_miss:+.1f} pp")
    print(f"  H1 (FN|tri drop ≥5 pp):     {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (miss drop ≥1 pp):       {'SUPPORTED' if h2 else 'REFUTED'}")
    print("  top redesign importances:")
    for nm, v in r4["importances"][:8]:
        mark = " *" if nm in NEW_FEATURES else ""
        print(f"    {nm:<22}{v:.3f}{mark}")
    print()

    print("n=5 COMPARISON (secondary, in-distribution CV)")
    print("-" * 72)
    b5 = eval_features(data["n5"], BASE_FEATURES, "baseline")
    r5 = eval_features(data["n5"], ALL_FEATURES, "redesign")
    print_metrics(b5, "baseline")
    print_metrics(r5, "redesign")
    d_fn5 = b5["fn_among_tri"] - r5["fn_among_tri"]
    h3 = d_fn5 >= 0.05
    print(f"  Δ FN|tri (base − redes):    {100 * d_fn5:+.1f} pp")
    print(f"  H3 (n=5 FN|tri drop ≥5 pp): {'SUPPORTED' if h3 else 'REFUTED'}")
    print()

    print("TRANSFER n=4 → n=5")
    print("-" * 72)
    tb = transfer_eval(data["n4"], data["n5"], BASE_FEATURES, "baseline-transfer")
    tr = transfer_eval(data["n4"], data["n5"], ALL_FEATURES, "redesign-transfer")
    print_metrics(tb, "baseline transfer")
    print_metrics(tr, "redesign transfer")
    d_fn_t = tb["fn_among_tri"] - tr["fn_among_tri"]
    h4 = d_fn_t >= 0.05
    print(f"  Δ FN|tri (base − redes):    {100 * d_fn_t:+.1f} pp")
    print(f"  H4 (transfer FN drop ≥5 pp):{'SUPPORTED' if h4 else 'REFUTED'}")
    print()

    # overall reading
    if h1:
        reading = "WIN on n=4 FN tail"
    elif d_fn > 0 or d_miss > 0:
        reading = "PARTIAL (directionally helpful, below threshold)"
    else:
        reading = "NULL (no FN-tail improvement)"

    print("=" * 72)
    print("SUMMARY")
    print(f"  n4 baseline:  miss={100 * b4['miss_rate']:.1f}%  FN|tri={100 * b4['fn_among_tri']:.1f}%  AUC={b4['auc']:.3f}")
    print(f"  n4 redesign:  miss={100 * r4['miss_rate']:.1f}%  FN|tri={100 * r4['fn_among_tri']:.1f}%  AUC={r4['auc']:.3f}")
    print(f"  n5 baseline:  miss={100 * b5['miss_rate']:.1f}%  FN|tri={100 * b5['fn_among_tri']:.1f}%  AUC={b5['auc']:.3f}")
    print(f"  n5 redesign:  miss={100 * r5['miss_rate']:.1f}%  FN|tri={100 * r5['fn_among_tri']:.1f}%  AUC={r5['auc']:.3f}")
    print(f"  transfer base FN|tri:       {100 * tb['fn_among_tri']:.1f}%")
    print(f"  transfer redes FN|tri:      {100 * tr['fn_among_tri']:.1f}%")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  H4={('SUPPORTED' if h4 else 'REFUTED')}")
    print(f"  reading:                    {reading}")
    print("=" * 72)

    summary = {
        "n4_base_miss": f"{b4['miss_rate']:.6f}",
        "n4_base_fn_tri": f"{b4['fn_among_tri']:.6f}",
        "n4_base_auc": f"{b4['auc']:.6f}",
        "n4_redes_miss": f"{r4['miss_rate']:.6f}",
        "n4_redes_fn_tri": f"{r4['fn_among_tri']:.6f}",
        "n4_redes_auc": f"{r4['auc']:.6f}",
        "n5_base_fn_tri": f"{b5['fn_among_tri']:.6f}",
        "n5_redes_fn_tri": f"{r5['fn_among_tri']:.6f}",
        "transfer_base_fn_tri": f"{tb['fn_among_tri']:.6f}",
        "transfer_redes_fn_tri": f"{tr['fn_among_tri']:.6f}",
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "reading": reading,
    }
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
