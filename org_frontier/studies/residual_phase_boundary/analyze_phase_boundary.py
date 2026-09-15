"""F28 — do near-boundary holistic residual forms sit on a Φ verdict phase boundary?

One-bit truth-table perturbations of Probe-131 residual forms; exact IIT-4.0 Φ labels.
Hypotheses fixed in hypotheses.md before this run.

Run:  python org_frontier/studies/residual_phase_boundary/analyze_phase_boundary.py
      python org_frontier/studies/residual_phase_boundary/analyze_phase_boundary.py --rebuild
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

PANEL = os.path.join(_REPO_ROOT, "org_frontier", "probes", "results", "residual_panel.csv")
FEATURES = ("n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
            "n_fixed", "n_reachable", "invertible", "max_period")
LABELS = ("A", "B", "C")
NEAR = 0.25
FAR = 0.40
CTRL_SEED = 28

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
SWEEP = os.path.join(RESULTS, "perturbation_sweep.csv")
SUMMARY = os.path.join(RESULTS, "summary.csv")


def tables_from_idx(idx):
    """Probe-125 enumeration order: for ta in 0..15 for tb in 0..15 for tc in 0..15."""
    tc = idx % 16
    tb = (idx // 16) % 16
    ta = idx // 256
    return int(ta), int(tb), int(tc)


def rules_from_masks(ma, mb, mc):
    ta = tuple((ma >> k) & 1 for k in range(4))
    tb = tuple((mb >> k) & 1 for k in range(4))
    tc = tuple((mc >> k) & 1 for k in range(4))

    def fa(a, b, t=ta):
        return t[(a & 1) | ((b & 1) << 1)]

    def fb(a, b, t=tb):
        return t[(a & 1) | ((b & 1) << 1)]

    def fc(a, b, t=tc):
        return t[(a & 1) | ((b & 1) << 1)]

    return [lambda x: fa(x[1], x[2]), lambda x: fb(x[0], x[2]), lambda x: fc(x[0], x[1])]


def is_triadic(ma, mb, mc):
    v = classify_rules(rules_from_masks(ma, mb, mc), labels=LABELS)
    return v.structure == "triadic", float(v.max_phi)


def one_bit_neighbours(ma, mb, mc):
    for node in range(3):
        masks = [ma, mb, mc]
        for bit in range(4):
            flipped = list(masks)
            flipped[node] = masks[node] ^ (1 << bit)
            yield node, bit, tuple(flipped)


def residual_sets():
    rows = list(csv.DictReader(open(PANEL)))
    assert len(rows) == 4096
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    miss = pred != y
    margin = np.abs(proba - 0.5)
    near_res = np.where(miss & (margin < NEAR))[0]
    near_hit = np.where((~miss) & (margin < NEAR))[0]
    far_hit = np.where((~miss) & (margin >= FAR))[0]
    return {
        "y": y,
        "proba": proba,
        "miss": miss,
        "near_res": near_res,
        "near_hit": near_hit,
        "far_hit": far_hit,
    }


def sample_controls(near_res, near_hit, far_hit, rng):
    n = len(near_res)
    # Use the full near-hit pool when it is smaller than the residual set (means still comparable).
    near_ctrl = np.array(near_hit) if len(near_hit) <= n else rng.choice(near_hit, size=n, replace=False)
    if len(far_hit) < n:
        raise SystemExit("ABORT: fewer far-hit controls than near residual forms")
    far_ctrl = rng.choice(far_hit, size=n, replace=False)
    return near_ctrl, far_ctrl


def sweep_seed(idx, group, y, proba):
    ma, mb, mc = tables_from_idx(idx)
    base_tri, base_phi = is_triadic(ma, mb, mc)
    # panel label must match recomputed verdict (instrument sanity per seed)
    if int(base_tri) != int(y[idx]):
        raise SystemExit(
            f"ABORT: panel/recompute mismatch at idx={idx}: panel={y[idx]} recompute={int(base_tri)}"
        )
    n_flip = 0
    rows = []
    for node, bit, (a, b, c) in one_bit_neighbours(ma, mb, mc):
        tri, phi = is_triadic(a, b, c)
        flip = int(tri != base_tri)
        n_flip += flip
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
    return n_flip, rows


def run_sweep(sets):
    rng = np.random.default_rng(CTRL_SEED)
    near_ctrl, far_ctrl = sample_controls(
        sets["near_res"], sets["near_hit"], sets["far_hit"], rng
    )
    groups = [
        ("near_residual", sets["near_res"]),
        ("near_hit_control", near_ctrl),
        ("far_hit_control", far_ctrl),
    ]
    all_rows = []
    per_seed = []
    start = time.time()
    print("PERTURBATION SWEEP — 12 Hamming-1 neighbours per seed, exact Φ")
    print("-" * 72)
    for group, indices in groups:
        flips = []
        for k, idx in enumerate(indices):
            n_flip, rows = sweep_seed(int(idx), group, sets["y"], sets["proba"])
            flips.append(n_flip / 12.0)
            all_rows.extend(rows)
            per_seed.append({
                "group": group,
                "seed_idx": int(idx),
                "n_flip": n_flip,
                "flip_rate": f"{n_flip / 12.0:.6f}",
                "any_flip": int(n_flip > 0),
                "seed_triadic": int(sets["y"][idx]),
                "seed_p": f"{float(sets['proba'][idx]):.6f}",
            })
            if (k + 1) % 50 == 0 or (k + 1) == len(indices):
                print(f"  {group:<20} {k + 1}/{len(indices)}  ({time.time() - start:.0f}s)")
        mean_rate = float(np.mean(flips))
        any_frac = float(np.mean([f > 0 for f in flips]))
        print(f"  {group:<20} mean flip rate={mean_rate:.3f}  "
              f"frac with ≥1 flip={any_frac:.3f}")
    os.makedirs(RESULTS, exist_ok=True)
    with open(SWEEP, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)
    seed_path = os.path.join(RESULTS, "per_seed.csv")
    with open(seed_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(per_seed[0].keys()))
        w.writeheader()
        w.writerows(per_seed)
    print(f"  wrote {SWEEP}")
    print(f"  wrote {seed_path}")
    print()
    return per_seed


def load_per_seed():
    path = os.path.join(RESULTS, "per_seed.csv")
    return list(csv.DictReader(open(path)))


def analyze(per_seed):
    print("F28 — PHASE BOUNDARY HYPOTHESES")
    print("-" * 72)
    stats = {}
    for group in ("near_residual", "near_hit_control", "far_hit_control"):
        rows = [r for r in per_seed if r["group"] == group]
        rates = np.array([float(r["flip_rate"]) for r in rows])
        any_flip = np.array([int(r["any_flip"]) for r in rows])
        stats[group] = {
            "n": len(rows),
            "mean_rate": float(rates.mean()),
            "any_frac": float(any_flip.mean()),
            "median_rate": float(np.median(rates)),
        }
        print(f"  {group:<20} n={len(rows)}  mean flip={stats[group]['mean_rate']:.3f}  "
              f"median={stats[group]['median_rate']:.3f}  "
              f"frac≥1 flip={stats[group]['any_frac']:.3f}")

    r = stats["near_residual"]
    near_c = stats["near_hit_control"]
    far_c = stats["far_hit_control"]

    h1 = (r["mean_rate"] >= 0.25) and (r["any_frac"] >= 0.80)
    h2 = (r["mean_rate"] - far_c["mean_rate"]) >= 0.10
    h3 = (r["mean_rate"] - near_c["mean_rate"]) >= 0.05

    print()
    print(f"  residual − far-hit:         {100 * (r['mean_rate'] - far_c['mean_rate']):+.1f} pp")
    print(f"  residual − near-hit:        {100 * (r['mean_rate'] - near_c['mean_rate']):+.1f} pp")
    print(f"  H1 (residual mean≥0.25 and ≥80% any-flip): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (residual exceeds far-hit by ≥10 pp):   "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (residual exceeds near-hit by ≥5 pp):   "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()

    # overall F28 reading
    if h1 and h2:
        reading = "PHASE BOUNDARY"
    elif h1 and not h2:
        reading = "UNSTABLE BUT NOT DISTINCT FROM TYPICAL FORMS"
    else:
        reading = "NOT A PHASE BOUNDARY"

    print(f"  F28 reading:                {reading}")
    print("  note: F26/F27 not reopened (n=4 shrink; affine residual refuted).")
    print()

    summary = {
        "near_residual_n": r["n"],
        "near_residual_mean_flip": r["mean_rate"],
        "near_residual_any_flip": r["any_frac"],
        "near_hit_mean_flip": near_c["mean_rate"],
        "far_hit_mean_flip": far_c["mean_rate"],
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "reading": reading,
    }
    with open(SUMMARY, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)
    return summary


def instrument_control():
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    # known triad
    and_m = 0b1000  # AND table (0,0,0,1) -> bit3 = f(1,1)=1 → mask 8
    # wait: bits little-endian: bit0=f(0,0), bit1=f(1,0), bit2=f(0,1), bit3=f(1,1)
    # AND: (0,0,0,1) -> mask = 8
    # party copy of mediator in unconstrained form is different; use catalog conjunctive via masks
    # For unconstrained A'=f(B,C), B'=f(A,C), C'=f(A,B):
    # faithful-like: A'=B (table depends only on first input of (B,C)? A reads B,C.
    # Simpler: use idx for a known form from panel that is triadic.
    conj = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    from org_frontier.classifier.classifier import classify_rules as cr
    v = cr(conj, labels=("W", "S", "C"))
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    print(f"  n=3 conjunctive triad: {v.structure} Φ={v.max_phi:.6f}  "
          f"{'PASS' if ok else 'FAIL'}")
    # one-bit neighbour of XOR hub-like unconstrained: verify flip machinery runs
    # XOR mask for 2-input: (0,1,1,0) = bits 1 and 2 -> mask 6
    xor = 6
    # a wiring with all XOR: may or may not be triadic; just check neighbour count
    n_neigh = sum(1 for _ in one_bit_neighbours(xor, xor, xor))
    ok2 = n_neigh == 12
    print(f"  Hamming-1 neighbourhood size: {n_neigh}  {'PASS' if ok2 else 'FAIL'}")
    if not (ok and ok2):
        raise SystemExit("ABORT: instrument control failed")
    print("  instrument control: PASS")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true",
                    help="recompute exact-Φ perturbation sweep; default loads committed results")
    args = ap.parse_args()

    print("RESIDUAL PHASE BOUNDARY — RESEARCH_AGENDA_50_V2 F28")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  perturbation: one bit in one node's 4-bit table (12 neighbours)")
    print("=" * 72)
    print()

    instrument_control()

    if args.rebuild or not os.path.exists(os.path.join(RESULTS, "per_seed.csv")):
        sets = residual_sets()
        n_miss = int(sets["miss"].sum())
        print("RESIDUAL SETS (Probe 131 protocol)")
        print("-" * 72)
        print(f"  RF misses:                  {n_miss}/4096 ({100 * n_miss / 4096:.1f}%)")
        print(f"  near-boundary residual:     {len(sets['near_res'])}  (|p-0.5|<{NEAR})")
        print(f"  near-hit pool:              {len(sets['near_hit'])}")
        print(f"  far-hit pool:               {len(sets['far_hit'])}  (|p-0.5|≥{FAR})")
        print()
        per_seed = run_sweep(sets)
    else:
        per_seed = load_per_seed()
        print(f"LOADED SWEEP — {os.path.join(RESULTS, 'per_seed.csv')} "
              f"({len(per_seed)} seeds)")
        print()

    summary = analyze(per_seed)
    print("=" * 72)
    print("SUMMARY")
    print(f"  near-boundary residual n:   {summary['near_residual_n']}")
    print(f"  mean one-bit flip rate:     {summary['near_residual_mean_flip']:.3f}")
    print(f"  frac with ≥1 flip:          {summary['near_residual_any_flip']:.3f}")
    print(f"  near-hit control mean:      {summary['near_hit_mean_flip']:.3f}")
    print(f"  far-hit control mean:       {summary['far_hit_mean_flip']:.3f}")
    print(f"  H1={summary['h1']}  H2={summary['h2']}  H3={summary['h3']}")
    print(f"  F28:                        {summary['reading']}")
    print("=" * 72)


if __name__ == "__main__":
    main()
