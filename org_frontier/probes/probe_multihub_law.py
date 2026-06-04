"""Probe 119 (J1) — how does Φ move with the number of symmetric mediators?

Question: a symmetric two-hub holds the full core at higher Φ than a single hub (#118). How does Φ scale
with the number of mediators at fixed group size? Hypothesis: Φ rises with the mediator count, approaching
the all-to-all pool (#104) as every node becomes a mediator — more symmetric mediation means more
integration, up to the pool ceiling. Method: a symmetric m-hub at fixed n (m hubs each reading all parties
and all other hubs; each party reading all hubs); sweep m from 1 to n−1 and read Φ and the core.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_multihub_law
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex


def sym_multihub(n, m):
    """0..m-1 = hubs, m..n-1 = parties. Each hub = AND(all parties AND all other hubs); each party = AND(all hubs)."""
    hubs = list(range(m))
    parties = list(range(m, n))
    rules = [None] * n
    for h in hubs:
        oh = [x for x in hubs if x != h]
        rules[h] = (lambda x, oh=oh: int(all(x[i] for i in parties) and all(x[i] for i in oh)))
    for p in parties:
        rules[p] = (lambda x: int(all(x[i] for i in hubs)))
    return rules


def main():
    print("PROBE 119 (J1) — Φ vs the number of symmetric mediators (fixed n)")
    print("=" * 60)
    for n in (5, 6):
        print(f"  n={n}:")
        print(f"    {'m hubs':<9}{'parties':<10}{'Φ':<10}{'core size':<11}{'full core'}")
        for m in range(1, n):
            core, phi = major_complex(sym_multihub(n, m), tuple(f"x{i}" for i in range(n)))
            sz = len(core) if core else 0
            print(f"    {m:<9}{n-m:<10}{phi:<10.3f}{sz:<11}{sz == n}")
    print("=" * 60)
    print("  Reading: Φ as a function of the mediator count shows whether spreading mediation raises")
    print("  integration and how far. A rise toward the all-to-all pool says every node acting as a")
    print("  mediator is the most integrated arrangement; a peak at an interior m would name an optimal")
    print("  number of mediators for a group of that size.")
    print("=" * 60)


if __name__ == "__main__":
    main()
