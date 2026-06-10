"""Probe Q100 (H1-H4) — does the cause-effect structure fingerprint the coordination kind?

Reads the structural fingerprint of a keystone triad of six coordination kinds and tests whether the
fingerprints separate the kinds, span dual types, break Φ-degeneracy, and scale with Φ.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q100_structure_fingerprint.probe_structure_fingerprint
"""

import csv
import os

from org_frontier.questions.q100_structure_fingerprint import forms as F


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for rank, i in enumerate(order):
            r[i] = rank
        return r
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    d2 = sum((rx[i] - ry[i]) ** 2 for i in range(n))
    return 1 - 6 * d2 / (n * (n * n - 1))


def main():
    print("PROBE Q100 (H1-H4) — cause-effect-structure fingerprints of coordination kinds")
    print("=" * 84)
    rows = {}
    for name, (rules, labels) in F.KEYSTONES.items():
        fp = F.fingerprint(rules, labels)
        rows[name] = fp
        print(f"  {name:<22} Φ={fp['phi']:<5} dists={fp['n_distinctions']:<2} "
              f"rels={fp['n_relations']:<3} max_order={fp['max_order']} type={fp['dual_type']}")

    keys = list(rows)
    sigs = [(rows[k]["n_distinctions"], rows[k]["n_relations"], rows[k]["max_order"], rows[k]["dual_type"])
            for k in keys]
    n_distinct = len(set(sigs))
    types = {rows[k]["dual_type"] for k in keys}
    # Φ-degeneracy: a pair with equal phi, different fingerprint
    degenerate = any(rows[a]["phi"] == rows[b]["phi"] and sigs[i] != sigs[j]
                     for i, a in enumerate(keys) for j, b in enumerate(keys) if i < j)
    rho = spearman([rows[k]["phi"] for k in keys], [rows[k]["n_relations"] for k in keys])

    h1 = n_distinct >= 4
    h2 = len(types) >= 2
    h3 = degenerate
    h4 = rho > 0.5
    print("=" * 84)
    print(f"  distinct fingerprints: {n_distinct}/6 | dual types present: {sorted(types)} | "
          f"Spearman(Φ, relations)={rho:.2f}")
    print(f"  H1 at least four distinct fingerprints:        {h1} ({n_distinct})")
    print(f"  H2 at least two dual types present:            {h2} ({len(types)})")
    print(f"  H3 equal Φ with different structure exists:    {h3}")
    print(f"  H4 relation count scales with Φ (ρ>0.5):       {h4} ({rho:.2f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "structure_fingerprint.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["kind", "phi", "n_distinctions", "n_relations", "max_order", "dual_type"])
        for k in keys:
            r = rows[k]
            w.writerow([k, r["phi"], r["n_distinctions"], r["n_relations"], r["max_order"], r["dual_type"]])


if __name__ == "__main__":
    main()
