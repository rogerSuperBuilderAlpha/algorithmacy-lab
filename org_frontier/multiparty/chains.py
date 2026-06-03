"""Mediator-chain length: does irreducibility survive deeper layers of mediation?

A chain routes coordination through k mediators in series: W -> S1 -> S2 -> ... -> Sk -> C, with no
direct edge between non-adjacent nodes. Each mediator commits jointly from its two neighbours
(Sj' = S_{j-1} AND S_{j+1}); the ends track their adjacent mediator. This models layered platforms,
sub-contracting, and nested intermediation.

Question: as the chain lengthens, does the form stay triadic (irreducible), and does Φ persist?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.chains [max_k]
"""

import csv
import os
import sys
import time

from org_frontier.classifier.classifier import classify_rules

_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def chain_rules(k):
    """W -> S1 -> ... -> Sk -> C. Returns (rules, labels). n = k + 2."""
    rules = [lambda x: x[1]]                                  # W' = S1
    for j in range(1, k + 1):
        lo, hi = j - 1, j + 1
        rules.append(lambda x, lo=lo, hi=hi: x[lo] & x[hi])   # Sj' = S_{j-1} AND S_{j+1}
    rules.append(lambda x, k=k: x[k])                        # C' = Sk
    labels = tuple(["W"] + [f"S{i}" for i in range(1, k + 1)] + ["C"])
    return rules, labels


def main(max_k=3):
    os.makedirs(_RESULTS, exist_ok=True)
    rows = []
    print("MEDIATOR-CHAIN LENGTH — does irreducibility survive deeper mediation?")
    print("=" * 84)
    for k in range(1, max_k + 1):
        rules, labels = chain_rules(k)
        n = k + 2
        t = time.time()
        v = classify_rules(rules, labels=labels)
        print(f"  k={k} mediators (n={n})  {v.structure:<8} Φ={v.max_phi:.4f}  "
              f"states={v.n_states_evaluated:<3} MIP={v.mip_partition}  [{time.time()-t:.1f}s]")
        rows.append({"k_mediators": k, "n": n, "structure": v.structure,
                     "max_phi": f"{v.max_phi:.6f}", "n_states": v.n_states_evaluated,
                     "mip": v.mip_partition})
    path = os.path.join(_RESULTS, "chains.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"\nWrote {path}")
    alltri = all(r["structure"] == "triadic" for r in rows)
    phis = {r["max_phi"] for r in rows}
    print(f"  all chains triadic: {alltri};  distinct Φ values: {sorted(phis)}")
    print("=" * 84)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
