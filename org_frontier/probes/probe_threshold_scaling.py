"""Probe 117 (H2) — which threshold commits keep the whole group in the core?

Question: AND-all and OR-all keep the full core (#116); majority factors at n=3 (#10, #67). Across the
k-of-n threshold commits, which keep every member in one irreducible core as the group grows? Hypothesis:
only the extreme thresholds (k=1 OR, k=n AND) keep the full core; intermediate thresholds (majority)
factor, because no single member is pivotal there. Method: build the k-of-n threshold commit (S=1 iff the
party count ≥ k, every party reads S) at n=4 and n=5; for each k read the verdict, Φ, and core size.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_threshold_scaling
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex


def threshold_hub(n, k):
    """0=S, 1..n-1 = parties. S = 1 iff at least k parties are on; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x, k=k, n=n: int(sum(x[i] for i in range(1, n)) >= k)
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def main():
    print("PROBE 117 (H2) — k-of-n threshold commits and the full core")
    print("=" * 60)
    for n in (4, 5):
        n_parties = n - 1
        print(f"  n={n} ({n_parties} parties):")
        print(f"    {'k':<5}{'rule':<14}{'verdict':<10}{'Φ':<9}{'core size'}")
        for k in range(1, n_parties + 1):
            core, phi = major_complex(threshold_hub(n, k), tuple(f"n{i}" for i in range(n)))
            sz = len(core) if core else 0
            verdict = "triadic" if phi > 1e-6 else "dyadic"
            rule = "OR (k=1)" if k == 1 else ("AND (k=all)" if k == n_parties else f"{k}-of-{n_parties}")
            print(f"    {k:<5}{rule:<14}{verdict:<10}{phi:<9.3f}{sz}")
    print("=" * 60)
    print("  Reading: the core size across k shows which commits hold the whole group. Full core only at")
    print("  the extremes (any-suffices and all-required) and a shrunken or factored core in between marks")
    print("  the intermediate thresholds as the ones where no member is pivotal enough to stay bound.")
    print("=" * 60)


if __name__ == "__main__":
    main()
