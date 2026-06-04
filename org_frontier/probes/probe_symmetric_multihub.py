"""Probe 118 (H3) — was the two-hub fragmentation an artifact of asymmetry?

Question: the two-hub form dropped one party-group from the core (#103), but its build was asymmetric —
each hub gated only its own group. Does a symmetric two-hub, where both hubs read all parties and every
party reads both hubs, keep the full core? Hypothesis: the fragmentation came from the asymmetric design;
a symmetric two-hub holds the whole group like the single hub. Method: build a symmetric two-hub at n=6
and n=7 (each hub = the other hub AND all parties; each party = both hubs) and compare its core to the
single hub and to the asymmetric two-hub of #103.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_symmetric_multihub
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_distributed_mediators import single_hub, two_hub


def sym_two_hub(n):
    """0=S1, 1=S2, 2..n-1 = parties. Each hub = the other hub AND all parties; each party reads both hubs."""
    parties = list(range(2, n))
    rules = [None] * n
    rules[0] = lambda x: int(x[1] and all(x[i] for i in parties))
    rules[1] = lambda x: int(x[0] and all(x[i] for i in parties))
    for i in parties:
        rules[i] = (lambda x, i=i: int(x[0] and x[1]))
    return rules


def main():
    print("PROBE 118 (H3) — symmetric vs asymmetric two-hub mediation")
    print("=" * 66)
    print(f"  {'n':<4}{'topology':<20}{'Φ':<9}{'core size':<11}{'full core'}")
    for n in (6, 7):
        labels = tuple(f"n{i}" for i in range(n))
        for name, build in (("single-hub", single_hub), ("two-hub (asym)", two_hub),
                            ("two-hub (sym)", sym_two_hub)):
            core, phi = major_complex(build(n), labels)
            sz = len(core) if core else 0
            print(f"  {n:<4}{name:<20}{phi:<9.3f}{sz:<11}{sz == n}")
    print("=" * 66)
    print("  Reading: a symmetric two-hub that keeps the full core shows the #103 fragmentation came from")
    print("  the asymmetric build, where one group reached the rest through a longer path. A symmetric")
    print("  build that still drops members shows distributed mediation fragments the core on its own.")
    print("=" * 66)


if __name__ == "__main__":
    main()
