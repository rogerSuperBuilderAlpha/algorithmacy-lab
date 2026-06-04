"""Probe 115 (G3) — does the parity family scale like the conjunctive hub?

Question: the conjunctive hub scales with the full core and Φ = n−1 (#105). The parity (XOR) commit at
n=3 is the pure-higher-order Φ=0.5 form (#56). How does the parity family scale? Hypothesis: it stays
pure-higher-order and scales differently from the conjunctive hub — not the clean Φ = n−1 law. Method:
build the all-parity commit (S = XOR of all parties, every party reads S) at n=3,4,5; read Φ and the
core, against the conjunctive hub for reference.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_parity_scaling
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from functools import reduce

from .lib import major_complex
from .probe_distributed_mediators import single_hub


def parity_hub(n):
    """0=S, 1..n-1 = parties. S = XOR of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def main():
    print("PROBE 115 (G3) — parity (XOR) hub scaling vs the conjunctive hub")
    print("=" * 64)
    print(f"  {'n':<5}{'commit':<14}{'verdict':<10}{'Φ':<9}{'core size'}")
    for n in (3, 4, 5):
        for name, build in (("parity (XOR)", parity_hub), ("conjunctive", single_hub)):
            core, phi = major_complex(build(n), tuple(f"n{i}" for i in range(n)))
            sz = len(core) if core else 0
            verdict = "triadic" if phi > 1e-6 else "dyadic"
            print(f"  {n:<5}{name:<14}{verdict:<10}{phi:<9.3f}{sz}")
    print("=" * 64)
    print("  Reading: the parity hub's Φ trajectory shows whether pure-higher-order binding scales with")
    print("  the group or stays a minimal whole. A flat or low Φ with the full core says XOR-style")
    print("  coordination is irreducible but never rich — the opposite of the conjunctive Φ = n−1 law.")
    print("=" * 64)


if __name__ == "__main__":
    main()
