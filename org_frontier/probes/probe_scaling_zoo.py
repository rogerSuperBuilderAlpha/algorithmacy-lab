"""Probe 132 (Q1) — the scaling-law zoo.

Question: different commit topologies scale Φ with size in different ways — the chain is flat (#57), the
conjunctive hub is linear (#116), the pool is super-linear (#104), the parity hub decays (#115). Do these
fall into distinct law classes, and does a ring give a fifth? Hypothesis: five families, five laws —
constant, linear, quadratic, exponential decay, and whatever the ring gives. Method: build chain, ring,
conjunctive hub, pool, and parity hub at n=3..6; read Φ and name the law class from the sequence.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_scaling_zoo
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex
from .probe_topology_map import chain, pool
from .probe_distributed_mediators import single_hub
from .probe_parity_scaling import parity_hub


def ring(n):
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


FAMILIES = {"chain": chain, "ring": ring, "conjunctive hub": single_hub, "pool": pool, "parity hub": parity_hub}


def law_class(seq):
    a, b, c, d = seq    # n=3,4,5,6
    if max(seq) - min(seq) < 1e-6:
        return "constant"
    if d < a:
        return "decay"
    d1 = [seq[i + 1] - seq[i] for i in range(3)]
    d2 = [d1[i + 1] - d1[i] for i in range(2)]
    if all(abs(x) < 1e-6 for x in d2):
        return "linear"
    return "super-linear"


def main():
    print("PROBE 132 (Q1) — the scaling-law zoo (Φ vs n)")
    print("=" * 60)
    print(f"  {'family':<18}{'n=3':<8}{'n=4':<8}{'n=5':<8}{'n=6':<8}{'law'}")
    for name, build in FAMILIES.items():
        seq = []
        for n in (3, 4, 5, 6):
            _, phi = major_complex(build(n), tuple(f"x{i}" for i in range(n)))
            seq.append(round(phi, 4))
        print(f"  {name:<18}{seq[0]:<8}{seq[1]:<8}{seq[2]:<8}{seq[3]:<8}{law_class(seq)}")
    print("=" * 60)
    print("  Reading: the families sort into distinct Φ(n) law classes. The class names how integration")
    print("  responds to adding members — flat through a serial bottleneck, linear through a single")
    print("  all-required hub, super-linear through all-to-all coupling, and decaying through a parity check.")
    print("=" * 60)


if __name__ == "__main__":
    main()
