"""Probe 104 (B2) — which topology classes keep the verdict and grow Φ with size?

Question: chains and trees preserve Φ=2.0 (Probes 57, 58), pools grow Φ with size (Probe 65), and random
single-hub mediation vanishes (Probe 97). Charting these together: which topology classes stay triadic,
and which grow Φ as the group grows? Hypothesis: distributed topologies (pool, two-hub) grow Φ with size,
while serial topologies (chain) keep a fixed Φ=2.0 and the single hub does not grow. Method: build chain,
single-hub, two-hub, and all-required pool forms at n=4 and n=5; report the verdict, Φ, and the change in
Φ from n=4 to n=5.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_topology_map
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_distributed_mediators import single_hub, two_hub


def chain(n):
    """Linear bidirectional chain: each node = AND of its neighbors; ends read their one neighbor."""
    rules = [None] * n
    for i in range(n):
        nb = [j for j in (i - 1, i + 1) if 0 <= j < n]
        rules[i] = (lambda x, nb=nb: int(all(x[j] for j in nb)))
    return rules


def pool(n):
    """All-required pool: each node = AND of all the others."""
    rules = [None] * n
    for i in range(n):
        others = [j for j in range(n) if j != i]
        rules[i] = (lambda x, others=others: int(all(x[j] for j in others)))
    return rules


TOPOS = {"chain": chain, "single-hub": single_hub, "two-hub": two_hub, "pool": pool}


def main():
    print("PROBE 104 (B2) — topology map: verdict and Φ-growth with size")
    print("=" * 64)
    print(f"  {'topology':<14}{'Φ(n=4)':<10}{'Φ(n=5)':<10}{'ΔΦ':<9}{'verdict(n=5)'}")
    for name, build in TOPOS.items():
        phis = {}
        for n in (4, 5):
            _, phi = major_complex(build(n), tuple(f"n{i}" for i in range(n)))
            phis[n] = phi
        d = phis[5] - phis[4]
        verdict = "triadic" if phis[5] > 1e-6 else "dyadic"
        print(f"  {name:<14}{phis[4]:<10.3f}{phis[5]:<10.3f}{d:<+9.3f}{verdict}")
    print("=" * 64)
    print("  Reading: topologies whose Φ rises from n=4 to n=5 scale their integration with the group;")
    print("  a flat Φ keeps a fixed bottleneck; a fall toward zero is a topology that cannot hold a")
    print("  larger group in one irreducible whole. Topology, not size alone, sets whether the triad scales.")
    print("=" * 64)


if __name__ == "__main__":
    main()
