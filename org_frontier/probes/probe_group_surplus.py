"""Probe 65 (#15) — when does group integration exceed the members'?

Question: Probe 52 found the whole exceeds its best pair at n=4 (the pool) but not at the n=3 triad.
Where does the group surplus emerge across sizes and forms? Hypothesis: the all-required pool shows a
growing surplus with n; the surplus is the whole Φ minus the best proper-subset Φ. Method: for the
all-required pool at n=3,4,5, compute whole Φ and the best proper-subset Φ; report the surplus.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_group_surplus
"""

import itertools

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def pool(n):
    outer = [0] + list(range(2, n))
    rules = [None] * n
    def s_rule(x, outer=tuple(outer)):
        r = 1
        for i in outer:
            r &= x[i]
        return r
    rules[1] = s_rule
    for i in outer:
        rules[i] = lambda x: x[1]
    labels = tuple(["W", "S"] + [f"C{k}" for k in range(1, n - 1)])
    return rules, labels


def best_proper_subset_phi(rules, labels):
    n = len(labels)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    subsets = [c for k in range(1, n) for c in itertools.combinations(range(n), k)]
    best = 0.0
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        for nodes in subsets:
            try:
                best = max(best, float(new_big_phi.sia(pyphi.Subsystem(net, state, nodes=nodes)).phi))
            except Exception:
                continue
    return best


def main():
    print("PROBE 65 (#15) — group surplus (whole Φ − best proper-subset Φ), all-required pool")
    print("=" * 76)
    print(f"  {'n':<4}{'whole Φ':<10}{'best subset Φ':<16}{'surplus'}")
    for n in (3, 4, 5):
        rules, labels = pool(n)
        whole = classify_rules(rules, labels=labels).max_phi
        best = best_proper_subset_phi(rules, labels)
        print(f"  {n:<4}{whole:<10.3f}{best:<16.3f}{whole - best:+.3f}")
    print("=" * 76)
    print("  Reading: a positive surplus means the group carries integration no proper subset has —")
    print("  group-level binding that emerges with size, the structural basis for group agency.")
    print("=" * 76)


if __name__ == "__main__":
    main()
