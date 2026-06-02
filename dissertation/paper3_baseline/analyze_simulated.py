"""Paper 3 — analyze the simulated-organization population (simulated_orgs.csv).

Reports: the Φ distribution across the population; what drives Φ (by mediation regime, by
determination function, by size; an OLS with R²); the exotic high-Φ tail; and where the 13
hand-modeled real organizations fall within the simulated population.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/analyze_simulated.py
"""

import csv
import os
import sys

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

_HERE = os.path.dirname(os.path.abspath(__file__))
_P2 = os.path.abspath(os.path.join(_HERE, "..", "paper2_construct"))
for p in (_HERE, _P2):
    if p not in sys.path:
        sys.path.insert(0, p)

import numpy as np


def load():
    with open(os.path.join(_HERE, "results", "simulated_orgs.csv")) as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        for k in ("n", "n_parties", "edges", "mediator_reads_all", "back_channel", "n_reachable"):
            r[k] = int(r[k])
        for k in ("max_phi", "mean_phi"):
            r[k] = float(r[k])
    return rows


def grp(rows, key):
    g = {}
    for r in rows:
        g.setdefault(r[key], []).append(r["max_phi"])
    return {k: (len(v), float(np.mean(v)), float(np.median(v)), float(np.max(v)))
            for k, v in sorted(g.items(), key=lambda kv: str(kv[0]))}


def _full_rank_columns(X):
    """Greedily keep a maximal set of linearly independent columns (prefers earlier columns:
    intercept, n, edges, ...). Returns the kept indices. This makes the design full rank so the
    fit is an actual estimate rather than an arbitrary minimum-norm pseudoinverse split."""
    keep = []
    for j in range(X.shape[1]):
        trial = keep + [j]
        if np.linalg.matrix_rank(X[:, trial]) == len(trial):
            keep.append(j)
    return keep


def ols(rows):
    """Full-rank OLS with standard errors. The simulated population confounds `regime` with the
    `back_channel` count (back_channel is nonzero only for the partial regime), so the naive
    11-column design is rank-deficient; we drop aliased columns and report which. NOTE: the
    predictors here ARE the generator's own design dimensions, so this characterizes the model
    family, not an empirical discovery — see Paper 3 §4.2."""
    regimes = ["dyadic", "strict", "partial"]
    dets = ["AND", "OR", "MAJ", "XOR", "THRESH2"]
    names = ["intercept", "n", "edges", "back_channel_links", "mediator_reads_all"] \
        + [f"regime={g}" for g in regimes[1:]] + [f"det={d}" for d in dets[1:]]
    X, y = [], []
    for r in rows:
        row = [1.0, r["n"], r["edges"], r["back_channel"], float(r["mediator_reads_all"])]
        row += [1.0 if r["regime"] == g else 0.0 for g in regimes[1:]]       # dyadic = baseline
        row += [1.0 if r["determination"] == d else 0.0 for d in dets[1:]]   # AND/'-' = baseline
        X.append(row)
        y.append(r["max_phi"])
    X, y = np.array(X), np.array(y)

    full_rank = np.linalg.matrix_rank(X)
    keep = _full_rank_columns(X)
    dropped = [names[j] for j in range(len(names)) if j not in keep]
    Xr = X[:, keep]
    namesr = [names[j] for j in keep]

    beta, *_ = np.linalg.lstsq(Xr, y, rcond=None)
    resid = y - Xr @ beta
    dof = len(y) - Xr.shape[1]
    sigma2 = float(resid @ resid) / dof
    XtX_inv = np.linalg.inv(Xr.T @ Xr)
    se = np.sqrt(np.maximum(np.diag(sigma2 * XtX_inv), 0.0))
    tstat = beta / se
    r2 = 1 - np.sum(resid ** 2) / np.sum((y - y.mean()) ** 2)
    return {
        "names": namesr, "beta": beta, "se": se, "t": tstat, "r2": r2,
        "rank": full_rank, "ncol": X.shape[1], "dropped": dropped, "dof": dof,
    }


def real_orgs():
    import pyphi
    from typology_phi import ORGS, placement
    pyphi.config.PROGRESS_BARS = False
    pyphi.config.PARALLEL = False
    return [(name, cls, placement(rules, n)["max"]) for name, cls, rules, n in ORGS]


def main():
    rows = load()
    print("=" * 76)
    print(f"SIMULATED-ORGANIZATION POPULATION — {len(rows)} organizations "
          f"(n={sorted(set(r['n'] for r in rows))})")
    print("=" * 76)

    phis = np.array([r["max_phi"] for r in rows])
    print(f"\nΦ distribution: min={phis.min():.2f}  median={np.median(phis):.2f}  "
          f"mean={phis.mean():.2f}  max={phis.max():.2f}")
    print(f"  reducible (Φ=0): {int((phis == 0).sum())}/{len(rows)} "
          f"({100*(phis==0).mean():.0f}%)")
    exotic = [r for r in rows if r["max_phi"] >= 4]
    print(f"  exotic high-Φ tail (Φ≥4): {len(exotic)} — "
          f"{', '.join(sorted(set(r['regime']+'/'+r['determination'] for r in exotic)))} "
          f"(OR + dense back-channel; Cerullo territory, read with caution)")

    print("\n[by mediation regime]   n   meanΦ  medianΦ  maxΦ")
    for k, (nn, m, md, mx) in grp(rows, "regime").items():
        print(f"  {k:<10} {nn:>5} {m:>7.3f} {md:>7.2f} {mx:>7.2f}")
    print("\n[by determination function]")
    for k, (nn, m, md, mx) in grp(rows, "determination").items():
        print(f"  {k:<10} {nn:>5} {m:>7.3f} {md:>7.2f} {mx:>7.2f}")
    print("\n[by party count n]")
    for k, (nn, m, md, mx) in grp(rows, "n").items():
        print(f"  n={k:<8} {nn:>5} {m:>7.3f} {md:>7.2f} {mx:>7.2f}")

    # Φ by regime WITHIN each party count, so the regime effect is not confounded by size
    # (the population is dominated by larger n; only a few forms are n=3).
    print("\n[Φ by regime, stratified by party count n]   (mean max Φ; count in parens)")
    regimes_order = ["dyadic", "strict", "partial"]
    ns = sorted(set(r["n"] for r in rows))
    print(f"  {'n':<5}" + "".join(f"{g:>16}" for g in regimes_order))
    for nv in ns:
        cells = []
        for g in regimes_order:
            vs = [r["max_phi"] for r in rows if r["n"] == nv and r["regime"] == g]
            cells.append(f"{np.mean(vs):.2f} (n={len(vs)})" if vs else "—")
        print(f"  {nv:<5}" + "".join(f"{c:>16}" for c in cells))

    fit = ols(rows)
    print(f"\n[what drives Φ]  OLS  max Φ ~ design features   (R² = {fit['r2']:.3f}, "
          f"dof={fit['dof']})")
    print(f"  design rank {fit['rank']} of {fit['ncol']} columns; "
          f"dropped as aliased: {', '.join(fit['dropped']) or '(none)'}")
    print(f"    {'term':>22} {'coef':>9} {'std.err':>9} {'t':>7}")
    for nm, b, s, t in zip(fit["names"], fit["beta"], fit["se"], fit["t"]):
        star = "  *" if abs(t) >= 2 else ""
        print(f"    {nm:>22} {b:>+9.3f} {s:>9.3f} {t:>7.2f}{star}")
    print("  NOTE: predictors are the generator's own design dimensions — this characterizes")
    print("  the model family, not an empirical finding (Paper 3 §4.2). '*' = |t| >= 2.")

    print("\n[the 13 real organizations, placed in the simulated population]")
    try:
        ro = real_orgs()
        for name, cls, phi in sorted(ro, key=lambda t: t[2]):
            pct = 100 * (phis <= phi).mean()
            print(f"  Φ={phi:5.2f}  ({pct:>3.0f}th pct)  {name:46s} [{cls}]")
    except Exception as e:
        print(f"  (could not place real orgs: {e})")

    # figure: Φ by regime (box-ish) + real-org markers
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8.5, 4.6))
        regimes = ["dyadic", "strict", "partial"]
        data = [[r["max_phi"] for r in rows if r["regime"] == g] for g in regimes]
        ax.boxplot(data, tick_labels=regimes, showfliers=True)
        ax.set_ylabel("max system Φ")
        ax.set_title("Simulated-organization population: Φ by mediation regime\n"
                     f"{len(rows)} organizations, exact IIT-4.0 Φ, party count 3–"
                     f"{max(r['n'] for r in rows)}")
        fig.tight_layout()
        fig.savefig(os.path.join(_HERE, "results", "simulated_orgs.png"), dpi=130)
        print(f"\nfigure -> {os.path.join(_HERE, 'results', 'simulated_orgs.png')}")
    except Exception as e:
        print(f"(figure skipped: {e})")


if __name__ == "__main__":
    main()
