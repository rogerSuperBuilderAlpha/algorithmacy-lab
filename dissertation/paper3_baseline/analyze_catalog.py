"""Paper 3 — analyze the catalog of the W–S–C model family.

Reads results/catalog.csv (built by catalog.py: exact Φ over the complete 16^3 triad family
plus the higher-order family) and answers the three questions the paper needs. NOTE: every
result below is a fact about the MODEL FAMILY — all Boolean wirings of three W–S–C nodes —
not about "the space of coordination." Most wirings are not coordination forms; the
enumeration is a coverage check that locates the hand-modeled organizations within the family.

  1. WHAT LEVELS EMERGE in the model family?  The distribution of Φ across all wirings — do
     scores cluster into a small number of bands, and do the bands the 13-organization
     typology occupies (0, ~0.5, ~0.83, 2.0, ...) fall out of the family rather than being
     hand-set?
  2. WHAT DRIVES Φ within the family?  Group means and a linear model of Φ on structural
     features (edges, mediator-depends-both, strict mediation, back-channel, parity) — so we
     can say which structural features move the score, computed not asserted. A low R² is
     itself the point: Φ is not a relabeling of any feature count.
  3. WHERE DO THE HAND-MODELED ORGANIZATIONS LAND in the family?  The 13 typology
     organizations located on the populated bands of the model family.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/analyze_catalog.py
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


def load(path):
    with open(path) as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        for k in ("n", "n_reachable", "edges", "mediator_depends_both",
                  "strict_mediation", "back_channel", "parity_present"):
            r[k] = int(r[k])
        for k in ("max_phi", "mean_phi"):
            r[k] = float(r[k])
    return rows


def levels(rows, tol=0.02):
    """Cluster max_phi into bands (round to nearest tol-grid), report counts."""
    vals = sorted(r["max_phi"] for r in rows)
    bands = {}
    for v in vals:
        key = round(v / tol) * tol
        bands.setdefault(round(key, 4), 0)
        bands[round(key, 4)] += 1
    return bands


def group_means(rows, feature):
    g = {}
    for r in rows:
        g.setdefault(r[feature], []).append(r["max_phi"])
    return {k: (len(v), float(np.mean(v)), float(np.max(v))) for k, v in sorted(g.items())}


def linear_model(rows):
    """OLS of max_phi on structural features; report coefficients and R²."""
    feats = ["edges", "mediator_depends_both", "strict_mediation", "back_channel",
             "parity_present"]
    X = np.array([[1.0] + [r[f] for f in feats] for r in rows])
    y = np.array([r["max_phi"] for r in rows])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return ["intercept"] + feats, beta, r2


def place_orgs():
    """Compute the 13 typology organizations' Φ + features, to locate them in the landscape."""
    import pyphi
    from phi_instrument import cm_from_rules
    from typology_phi import ORGS, placement
    from catalog import triad_features

    pyphi.config.PROGRESS_BARS = False
    pyphi.config.PARALLEL = False

    out = []
    for name, cls, rules, n in ORGS:
        r = placement(rules, n)
        cm = cm_from_rules(rules, n)
        if n == 3:
            feat = triad_features(cm, 8)
        else:
            parties = [0, 2, 3]
            strict = all(cm[1, p] and sum(cm[q, p] for q in parties if q != p) == 0
                         for p in parties)
            back = any(sum(cm[q, p] for q in parties if q != p) > 0 for p in parties)
            feat = {"strict_mediation": int(bool(strict)), "back_channel": int(bool(back)),
                    "mediator_depends_both": int(cm[0, 1] + cm[2, 1] + cm[3, 1] >= 2)}
        out.append((name, cls, n, r["max"], feat))
    return out


def main():
    path = os.path.join(_HERE, "results", "catalog.csv")
    if not os.path.exists(path):
        sys.exit(f"catalog.csv not found at {path} — run catalog.py first.")
    rows = load(path)
    triads = [r for r in rows if r["n"] == 3]
    ho = [r for r in rows if r["n"] == 4]

    print("=" * 80)
    print(f"PAPER 3 CATALOG ANALYSIS — {len(rows)} distinct forms "
          f"({len(triads)} triad, {len(ho)} higher-order)")
    print("=" * 80)

    # 1. Levels that emerge -------------------------------------------------------------
    print("\n[1] THE Φ LANDSCAPE — distribution of max Φ over the whole space")
    bands = levels(triads)
    nonzero = {k: v for k, v in bands.items() if k > 0}
    zero_n = bands.get(0.0, 0)
    print(f"  triads at Φ = 0 (reducible / dyadic):  {zero_n} of {len(triads)} "
          f"({100*zero_n/len(triads):.1f}%)")
    print(f"  distinct nonzero Φ bands: {len(nonzero)}")
    print(f"  {'Φ band':>8} {'count':>7}")
    for k in sorted(bands):
        print(f"  {k:>8.3f} {bands[k]:>7}")
    print(f"  max Φ among triads: {max(r['max_phi'] for r in triads):.4f}")
    if ho:
        print(f"  higher-order (n=4) Φ range: "
              f"{min(r['max_phi'] for r in ho):.3f} – {max(r['max_phi'] for r in ho):.3f}")

    # 2. What drives Φ ------------------------------------------------------------------
    print("\n[2] WHAT DRIVES Φ — group means of max Φ (triads)")
    for feat in ["mediator_depends_both", "strict_mediation", "back_channel", "parity_present"]:
        print(f"  by {feat}:")
        for k, (n_, mean_, max_) in group_means(triads, feat).items():
            print(f"      {feat}={k}:  n={n_:>4}  meanΦ={mean_:.4f}  maxΦ={max_:.4f}")
    print("  by mediator function (only forms where the mediator reads both parties):")
    med = [r for r in triads if r["mediator_depends_both"] == 1]
    for k, (n_, mean_, max_) in sorted(group_means(med, "mediator_fn").items(),
                                       key=lambda t: -t[1][1]):
        print(f"      S={k:>6}:  n={n_:>4}  meanΦ={mean_:.4f}  maxΦ={max_:.4f}")

    names, beta, r2 = linear_model(triads)
    print(f"\n  linear model  max Φ ~ structural features   (R² = {r2:.3f}):")
    for nm, b in zip(names, beta):
        print(f"      {nm:>22}: {b:+.4f}")

    # 3. Where real organizations land --------------------------------------------------
    print("\n[3] REAL ORGANIZATIONS placed in the computed landscape")
    orgs = []
    try:
        orgs = place_orgs()
        for name, cls, n, phi, feat in sorted(orgs, key=lambda t: t[3]):
            tags = []
            if feat.get("strict_mediation"):
                tags.append("strict")
            elif feat.get("back_channel"):
                tags.append("partial(back-channel)")
            if feat.get("mediator_depends_both"):
                tags.append("mediator-binds-both")
            print(f"  Φ={phi:5.2f}  {name:46s} [{cls:28s}] {' '.join(tags)}")
    except Exception as e:
        print(f"  (could not place orgs: {e})")

    # Figure: the Φ landscape with real organizations marked --------------------------
    try:
        plot_landscape(triads, orgs)
        print(f"\n  figure -> {os.path.join(_HERE, 'results', 'catalog_landscape.png')}")
    except Exception as e:
        print(f"  (figure skipped: {e})")

    print("\n" + "=" * 80)


def plot_landscape(triads, orgs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    bands = levels(triads)
    keys = sorted(bands)
    counts = [bands[k] for k in keys]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar([f"{k:.2f}" for k in keys], counts, color="#4C72B0", width=0.7)
    ax.set_xlabel("max system Φ (model-internal score)")
    ax.set_ylabel("number of wirings in the model family")
    ax.set_title("Paper 3 — the Φ landscape of the W–S–C model family\n"
                 f"exact Φ over all {len(triads)} three-node wirings; "
                 "the bands are a property of the family, not assigned")
    # mark where real organizations sit
    org_phis = sorted({round(p, 2) for _, _, _, p, _ in orgs if p <= max(keys) + 0.1})
    for op in org_phis:
        # nearest band index
        idx = min(range(len(keys)), key=lambda i: abs(keys[i] - op))
        ax.annotate("orgs here", xy=(idx, counts[idx]), xytext=(idx, counts[idx] + max(counts) * 0.06),
                    ha="center", fontsize=8, color="#C44E52",
                    arrowprops=dict(arrowstyle="->", color="#C44E52"))
    fig.tight_layout()
    fig.savefig(os.path.join(_HERE, "results", "catalog_landscape.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    main()
