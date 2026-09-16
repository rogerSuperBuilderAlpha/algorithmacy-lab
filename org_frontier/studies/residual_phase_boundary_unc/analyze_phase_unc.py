"""F28 on unconstrained k=2 residual misses (n=4 primary, n=5 secondary).

One-bit truth-table perturbations; exact IIT-4.0 Φ. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_unc.py
      python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_unc.py --rebuild
      python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_unc.py --rebuild --n5
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
from sklearn.model_selection import cross_val_predict

from org_frontier.classifier.classifier import classify_rules
from org_frontier.multiparty.run import _fn, _rand_table
from org_frontier.studies.holistic_residual_n4.analyze_residual_n4 import FEATURES

NEAR = 0.25
FAR = 0.40
CTRL_SEED = 28

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

CONFIGS = {
    "n4": {
        "n_nodes": 4,
        "n_sample": 1000,
        "seed": 40,
        "labels": ("A", "B", "C", "D"),
        "panel": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n4_unconstrained/results/"
            "residual_panel_n4_unconstrained.csv",
        ),
        "expected_misses": 75,
    },
    "n5": {
        "n_nodes": 5,
        "n_sample": 500,
        "seed": 50,
        "labels": ("A", "B", "C", "D", "E"),
        "panel": os.path.join(
            _REPO_ROOT,
            "org_frontier/studies/holistic_residual_n5_unconstrained/results/"
            "residual_panel_n5_unconstrained.csv",
        ),
        "expected_misses": 45,
    },
}


def sample_k2(rng, n_nodes):
    """Match holistic_residual_n*_unconstrained RNG order; also return tables and input idxs."""
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


def replay_forms(cfg):
    rng = np.random.default_rng(cfg["seed"])
    return [sample_k2(rng, cfg["n_nodes"]) for _ in range(cfg["n_sample"])]


def residual_sets(cfg):
    rows = list(csv.DictReader(open(cfg["panel"])))
    assert len(rows) == cfg["n_sample"]
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    miss = pred != y
    margin = np.abs(proba - 0.5)
    return {
        "y": y,
        "proba": proba,
        "miss_idx": np.where(miss)[0],
        "near_hit": np.where((~miss) & (margin < NEAR))[0],
        "far_hit": np.where((~miss) & (margin >= FAR))[0],
        "near_miss": np.where(miss & (margin < NEAR))[0],
    }


def rules_from_tables(tables, inputs):
    return [_fn(tables[j], inputs[j]) for j in range(len(tables))]


def one_bit_neighbours(tables, inputs):
    n_nodes = len(tables)
    for node in range(n_nodes):
        for bit in range(4):
            new_tables = list(tables)
            nt = list(tables[node])
            nt[bit] = 1 - nt[bit]
            new_tables[node] = tuple(nt)
            yield node, bit, rules_from_tables(new_tables, inputs)


def is_triadic(rules, labels):
    v = classify_rules(rules, labels=labels)
    return v.structure == "triadic", float(v.max_phi)


def sample_controls(miss_idx, near_hit, far_hit, rng):
    n = len(miss_idx)
    near_ctrl = np.array(near_hit) if len(near_hit) <= n else rng.choice(near_hit, size=n, replace=False)
    if len(far_hit) < n:
        raise SystemExit("ABORT: fewer far-hit controls than residual misses")
    far_ctrl = rng.choice(far_hit, size=n, replace=False)
    return near_ctrl, far_ctrl


def sweep_seed(idx, group, form, labels, y, proba):
    rules, tables, inputs = form
    base_tri, base_phi = is_triadic(rules, labels)
    if int(base_tri) != int(y[idx]):
        raise SystemExit(
            f"ABORT: panel/recompute mismatch idx={idx}: panel={y[idx]} got={int(base_tri)}"
        )
    n_neigh = 0
    n_flip = 0
    n_tri_to_dya = 0
    n_dya_to_tri = 0
    rows = []
    for node, bit, neigh_rules in one_bit_neighbours(tables, inputs):
        tri, phi = is_triadic(neigh_rules, labels)
        flip = int(tri != base_tri)
        n_neigh += 1
        n_flip += flip
        if flip and base_tri and not tri:
            n_tri_to_dya += 1
        if flip and (not base_tri) and tri:
            n_dya_to_tri += 1
        rows.append({
            "group": group,
            "seed_idx": int(idx),
            "seed_triadic": int(base_tri),
            "seed_phi": f"{base_phi:.6f}",
            "seed_p": f"{float(proba[idx]):.6f}",
            "node": node,
            "bit": bit,
            "neigh_triadic": int(tri),
            "neigh_phi": f"{phi:.6f}",
            "flipped": flip,
        })
    return {
        "n_flip": n_flip,
        "n_neigh": n_neigh,
        "flip_rate": n_flip / n_neigh,
        "any_flip": int(n_flip > 0),
        "tri_to_dya": n_tri_to_dya,
        "dya_to_tri": n_dya_to_tri,
        "rows": rows,
    }


def run_universe(name, cfg, do_rebuild):
    per_seed_path = os.path.join(RESULTS, f"per_seed_{name}.csv")
    sweep_path = os.path.join(RESULTS, f"perturbation_sweep_{name}.csv")

    print(f"UNIVERSE {name} — n={cfg['n_nodes']} unc k=2")
    print("-" * 72)
    sets = residual_sets(cfg)
    n_miss = len(sets["miss_idx"])
    print(f"  panel misses:               {n_miss}/{cfg['n_sample']} "
          f"(expected {cfg['expected_misses']})")
    print(f"  near-boundary among misses: {len(sets['near_miss'])}  (|p-0.5|<{NEAR})")
    print(f"  near-hit / far-hit pools:   {len(sets['near_hit'])} / {len(sets['far_hit'])}")
    if n_miss != cfg["expected_misses"]:
        raise SystemExit(f"ABORT: miss count {n_miss} != expected {cfg['expected_misses']}")

    if do_rebuild or not os.path.exists(per_seed_path):
        forms = replay_forms(cfg)
        rng = np.random.default_rng(CTRL_SEED)
        near_ctrl, far_ctrl = sample_controls(
            sets["miss_idx"], sets["near_hit"], sets["far_hit"], rng
        )
        groups = [
            ("residual", sets["miss_idx"]),
            ("near_hit_control", near_ctrl),
            ("far_hit_control", far_ctrl),
        ]
        all_rows = []
        per_seed = []
        start = time.time()
        print(f"  perturbation: one-bit table flips "
              f"({cfg['n_nodes'] * 4} neighbours/seed), exact Φ")
        for group, indices in groups:
            rates = []
            for k, idx in enumerate(indices):
                out = sweep_seed(
                    int(idx), group, forms[int(idx)], cfg["labels"],
                    sets["y"], sets["proba"],
                )
                rates.append(out["flip_rate"])
                all_rows.extend(out["rows"])
                per_seed.append({
                    "universe": name,
                    "group": group,
                    "seed_idx": int(idx),
                    "n_flip": out["n_flip"],
                    "n_neigh": out["n_neigh"],
                    "flip_rate": f"{out['flip_rate']:.6f}",
                    "any_flip": out["any_flip"],
                    "tri_to_dya": out["tri_to_dya"],
                    "dya_to_tri": out["dya_to_tri"],
                    "seed_triadic": int(sets["y"][idx]),
                    "seed_p": f"{float(sets['proba'][idx]):.6f}",
                    "near_boundary": int(abs(float(sets["proba"][idx]) - 0.5) < NEAR),
                })
                if (k + 1) % 25 == 0 or (k + 1) == len(indices):
                    print(f"    {group:<20} {k + 1}/{len(indices)}  "
                          f"({time.time() - start:.0f}s)")
            print(f"    {group:<20} mean flip={float(np.mean(rates)):.3f}  "
                  f"frac≥1={float(np.mean([r > 0 for r in rates])):.3f}")
        os.makedirs(RESULTS, exist_ok=True)
        with open(sweep_path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
            w.writeheader()
            w.writerows(all_rows)
        with open(per_seed_path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(per_seed[0].keys()))
            w.writeheader()
            w.writerows(per_seed)
        print(f"  wrote {per_seed_path}")
        print(f"  wrote {sweep_path}")
    else:
        per_seed = list(csv.DictReader(open(per_seed_path)))
        print(f"  LOADED {per_seed_path} ({len(per_seed)} seeds)")
    print()
    return analyze_universe(name, per_seed)


def analyze_universe(name, per_seed):
    print(f"F28 HYPOTHESES — {name}")
    print("-" * 72)
    stats = {}
    for group in ("residual", "near_hit_control", "far_hit_control"):
        rows = [r for r in per_seed if r["group"] == group]
        rates = np.array([float(r["flip_rate"]) for r in rows])
        any_flip = np.array([int(r["any_flip"]) for r in rows])
        t2d = sum(int(r["tri_to_dya"]) for r in rows)
        d2t = sum(int(r["dya_to_tri"]) for r in rows)
        near_rows = [r for r in rows if int(r.get("near_boundary", 0)) == 1]
        stats[group] = {
            "n": len(rows),
            "mean_rate": float(rates.mean()),
            "any_frac": float(any_flip.mean()),
            "median_rate": float(np.median(rates)),
            "tri_to_dya": t2d,
            "dya_to_tri": d2t,
            "near_n": len(near_rows),
            "near_mean": float(np.mean([float(r["flip_rate"]) for r in near_rows]))
            if near_rows else float("nan"),
        }
        print(f"  {group:<20} n={len(rows)}  mean flip={stats[group]['mean_rate']:.3f}  "
              f"median={stats[group]['median_rate']:.3f}  "
              f"frac≥1={stats[group]['any_frac']:.3f}  "
              f"tri→dya={t2d} dya→tri={d2t}")

    r, near_c, far_c = stats["residual"], stats["near_hit_control"], stats["far_hit_control"]
    h1 = (r["mean_rate"] >= 0.25) and (r["any_frac"] >= 0.80)
    h2 = (r["mean_rate"] - far_c["mean_rate"]) >= 0.10
    h3 = (r["mean_rate"] - near_c["mean_rate"]) >= 0.05
    print()
    print(f"  residual − far-hit:         {100 * (r['mean_rate'] - far_c['mean_rate']):+.1f} pp")
    print(f"  residual − near-hit:        {100 * (r['mean_rate'] - near_c['mean_rate']):+.1f} pp")
    if r["near_n"]:
        print(f"  near-boundary residual mean:{r['near_mean']:.3f} (n={r['near_n']})")
    print(f"  H1 (mean≥0.25 and ≥80% any-flip): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (residual − far-hit ≥10 pp):   {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (residual − near-hit ≥5 pp):   {'SUPPORTED' if h3 else 'REFUTED'}")
    if h1 and h2:
        reading = "PHASE BOUNDARY"
    elif h1:
        reading = "UNSTABLE BUT NOT ABOVE CONTROLS"
    else:
        reading = "NOT A PHASE BOUNDARY"
    print(f"  F28 reading ({name}):       {reading}")
    print()
    return {
        "universe": name,
        "residual_n": r["n"],
        "residual_mean_flip": r["mean_rate"],
        "residual_any_flip": r["any_frac"],
        "near_hit_mean_flip": near_c["mean_rate"],
        "far_hit_mean_flip": far_c["mean_rate"],
        "tri_to_dya": r["tri_to_dya"],
        "dya_to_tri": r["dya_to_tri"],
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "reading": reading,
    }


def instrument_control():
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    conj = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = classify_rules(conj, labels=("W", "S", "C"))
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    print(f"  n=3 conjunctive triad: {v.structure} Φ={v.max_phi:.6f}  "
          f"{'PASS' if ok else 'FAIL'}")
    rng = np.random.default_rng(0)
    _, tables, inputs = sample_k2(rng, 4)
    n_neigh = sum(1 for _ in one_bit_neighbours(tables, inputs))
    ok2 = n_neigh == 16
    print(f"  n=4 Hamming-1 neighbourhood: {n_neigh}  {'PASS' if ok2 else 'FAIL'}")
    if not (ok and ok2):
        raise SystemExit("ABORT: instrument control failed")
    print("  instrument control: PASS")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--n5", action="store_true", help="also run n=5 secondary universe")
    args = ap.parse_args()

    print("RESIDUAL PHASE BOUNDARY (UNC) — F28 on k=2 residual misses")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  size series cited: 4.8% → 7.5% → 9.0% (not reopened)")
    print("=" * 72)
    print()
    instrument_control()

    summaries = []
    summaries.append(run_universe("n4", CONFIGS["n4"], args.rebuild))
    n5_path = os.path.join(RESULTS, "per_seed_n5.csv")
    if args.n5 or os.path.exists(n5_path):
        # Rebuild n5 only when explicitly requested with --rebuild --n5 (or --rebuild when
        # forcing both via --n5). Loading uses committed per_seed_n5.csv when present.
        summaries.append(run_universe("n5", CONFIGS["n5"], bool(args.rebuild and args.n5)))
    elif args.rebuild:
        print("NOTE: re-run with --rebuild --n5 to include the n=5 secondary sweep.")
        print()

    print("=" * 72)
    print("SUMMARY")
    for s in summaries:
        print(f"  {s['universe']}: mean flip={s['residual_mean_flip']:.3f}  "
              f"any={s['residual_any_flip']:.3f}  "
              f"far={s['far_hit_mean_flip']:.3f} near={s['near_hit_mean_flip']:.3f}  "
              f"H1={s['h1']} H2={s['h2']} H3={s['h3']}  {s['reading']}")
        print(f"       direction flips: tri→dya={s['tri_to_dya']} dya→tri={s['dya_to_tri']}")
    primary = summaries[0]
    print(f"  F28 primary (n4):           {primary['reading']}")
    print("=" * 72)

    summary_path = os.path.join(RESULTS, "summary.csv")
    os.makedirs(RESULTS, exist_ok=True)
    with open(summary_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summaries[0].keys()))
        w.writeheader()
        w.writerows(summaries)


if __name__ == "__main__":
    main()
