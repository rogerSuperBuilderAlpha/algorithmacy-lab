"""Probe 103 (B1) — does distributed mediation sustain triadicity at scale?

Question: triadicity through a single mediator vanishes by n=6 (Probe 97). Does splitting the mediation
across two linked mediators sustain it where one hub cannot? Hypothesis: a modular topology — two
mediators each binding a subset of parties, coupled to each other — keeps a large irreducible core at
n=6 and n=7, where the single conjunctive hub is fragile. Method: build a single-hub form (one mediator
reading all parties, parties reading it) and a two-hub form (two mediators each gating their own group
and reading each other) at n=6 and n=7; compare the verdict, Φ, and core size.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_distributed_mediators
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex


def single_hub(n):
    """0=S, 1..n-1 = parties. S = AND of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def two_hub(n):
    """0=S1, 1=S2, 2..n-1 = parties split in two groups. Each hub = other hub AND its own group;
    each party reads its hub."""
    parties = list(range(2, n))
    half = max(1, len(parties) // 2)
    gA, gB = parties[:half], parties[half:]
    rules = [None] * n
    rules[0] = lambda x: int(x[1] and all(x[i] for i in gA))
    rules[1] = lambda x: int(x[0] and all(x[i] for i in gB))
    for i in gA:
        rules[i] = (lambda x, i=i: x[0])
    for i in gB:
        rules[i] = (lambda x, i=i: x[1])
    return rules


def main():
    print("PROBE 103 (B1) — single hub vs distributed (two-hub) mediation at scale")
    print("=" * 70)
    print(f"  {'n':<4}{'topology':<14}{'verdict':<10}{'Φ':<8}{'core size':<11}{'core'}")
    sizes = {}
    for n in (6, 7):
        labels = tuple([f"n{i}" for i in range(n)])
        for name, build in (("single-hub", single_hub), ("two-hub", two_hub)):
            core, phi = major_complex(build(n), labels)
            sz = len(core) if core else 0
            sizes[(n, name)] = (sz, phi)
            print(f"  {n:<4}{name:<14}{('triadic' if phi>1e-6 else 'dyadic'):<10}{phi:<8.3f}{sz:<11}{core}")
    print("=" * 70)
    single_bigger = all(sizes[(n, "single-hub")][0] >= sizes[(n, "two-hub")][0] for n in (6, 7))
    if single_bigger:
        print("  Reading: the single all-required hub holds the whole group in one core at higher Φ; the")
        print("  two-hub form keeps a smaller core (one party-group drops out) at lower Φ. Distributing")
        print("  the mediation fragments the coordination rather than scaling it — what scales a large")
        print("  irreducible group is one all-demanding commit, not splitting the mediator (cf. Probe 105).")
    else:
        print("  Reading: the two-hub form keeps the larger core, so distributed mediation scales the triad")
        print("  where a single hub cannot.")
    print("=" * 70)


if __name__ == "__main__":
    main()
