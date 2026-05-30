"""Profile the bestiary and explore how level and character of consciousness differ.

Usage:
    python -m consciousness_range.explore
"""

import csv
import pickle

import numpy as np

from .profile import profile

BESTIARY_PATH = "consciousness_range/results/bestiary.pkl"
SUMMARY_PATH = "consciousness_range/results/profiles.csv"
PLOT_PATH = "consciousness_range/results/range_of_minds.png"


def _order_str(hist):
    return ", ".join(f"{o}:{c}" for o, c in sorted(hist.items())) if hist else "—"


def main():
    creatures = pickle.load(open(BESTIARY_PATH, "rb"))
    profs = [p for p in (profile(c) for c in creatures) if p is not None]
    profs.sort(key=lambda p: p["phi"])

    print("\nA RANGE OF MINDS — IIT-4.0 Φ-structure profiles (ordered by Φ)\n")
    hdr = f"{'creature':<18}{'Φ':>6}{'#dist':>6}{'order(o:n)':>14}{'#rel':>8}{'Σφ_dist':>9}"
    print(hdr); print("-" * len(hdr))
    for p in profs:
        print(f"{p['name']:<18}{p['phi']:>6.3f}{p['n_distinctions']:>6}"
              f"{_order_str(p['order_hist']):>14}{p['n_relations']:>8}"
              f"{p['sum_phi_distinctions']:>9.2f}")

    # The centerpiece: the matched-Φ "twins".
    twins = [p for p in profs if abs(p["phi"] - 0.415) < 0.02]
    if len(twins) >= 2:
        print("\nSAME LEVEL, DIFFERENT MINDS — three systems at Φ ≈ 0.415:")
        for p in sorted(twins, key=lambda p: p["n_relations"]):
            print(f"  {p['name']:<14} Φ={p['phi']:.3f}  "
                  f"{p['n_distinctions']:>2} distinctions, {p['n_relations']:>6} relations, "
                  f"max order {p['max_order']}")
        rr = [p["n_relations"] for p in twins]
        print(f"  → identical Φ, yet structural richness spans {min(rr)}–{max(rr)} relations "
              f"({max(rr) / max(1, min(rr)):.0f}× range).")

    # Does level (Φ) track character (structure)?
    phi = np.array([p["phi"] for p in profs])
    nrel = np.array([p["n_relations"] for p in profs], float)
    cons = phi > 1e-6
    print(f"\n{int(cons.sum())}/{len(profs)} creatures are 'subjects' (Φ>0). "
          f"Among them, Φ vs #relations: Pearson r = "
          f"{np.corrcoef(phi[cons], np.log1p(nrel[cons]))[0, 1]:+.2f} (log richness).")

    with open(SUMMARY_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "desc", "n_nodes", "state", "phi",
                                          "n_distinctions", "n_relations",
                                          "sum_phi_distinctions", "sum_phi_relations",
                                          "mean_order", "max_order"])
        w.writeheader()
        for p in profs:
            w.writerow({k: p[k] for k in w.fieldnames})
    print(f"\nWrote {SUMMARY_PATH}")
    _plot(profs)


def _plot(profs):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plot.")
        return
    phi = np.array([p["phi"] for p in profs])
    nrel = np.array([p["n_relations"] for p in profs], float)
    fig, ax = plt.subplots(figsize=(10, 6))
    is_twin = np.array([abs(p["phi"] - 0.415) < 0.02 for p in profs])
    ax.scatter(phi[~is_twin], nrel[~is_twin] + 0.5, s=80, alpha=0.7, color="#4477aa")
    ax.scatter(phi[is_twin], nrel[is_twin] + 0.5, s=120, color="#cc3311",
               zorder=5, label="Φ ≈ 0.415 'twins'")
    for p in profs:
        ax.annotate(p["name"], (p["phi"], p["n_relations"] + 0.5),
                    fontsize=8, xytext=(5, 3), textcoords="offset points")
    ax.set_yscale("log")
    ax.set_xlabel("Φ  —  'level of consciousness'")
    ax.set_ylabel("number of relations + 1  —  structural richness ('character')")
    ax.set_title("A range of minds: level (Φ) vs character (Φ-structure)\n"
                 "the red points share a level but not an experience")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=120, bbox_inches="tight")
    print(f"Wrote {PLOT_PATH}")


if __name__ == "__main__":
    main()
