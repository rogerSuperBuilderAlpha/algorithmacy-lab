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


def ols(rows):
    regimes = ["dyadic", "strict", "partial"]
    dets = ["AND", "OR", "MAJ", "XOR", "THRESH2"]
    X, y = [], []
    for r in rows:
        row = [1.0, r["n"], r["edges"], r["back_channel"], float(r["mediator_reads_all"])]
        row += [1.0 if r["regime"] == g else 0.0 for g in regimes[1:]]       # dyadic = baseline
        row += [1.0 if r["determination"] == d else 0.0 for d in dets[1:]]   # AND/'-' = baseline
        X.append(row)
        y.append(r["max_phi"])
    X, y = np.array(X), np.array(y)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    r2 = 1 - np.sum((y - yhat) ** 2) / np.sum((y - y.mean()) ** 2)
    names = ["intercept", "n", "edges", "back_channel_links", "mediator_reads_all"] \
        + [f"regime={g}" for g in regimes[1:]] + [f"det={d}" for d in dets[1:]]
    return names, beta, r2


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

    names, beta, r2 = ols(rows)
    print(f"\n[what drives Φ]  OLS  max Φ ~ design features   (R² = {r2:.3f})")
    for nm, b in zip(names, beta):
        print(f"    {nm:>22}: {b:+.3f}")

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
