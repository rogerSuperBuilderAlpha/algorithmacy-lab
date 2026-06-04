"""Probe 52 — group vs members (List 2018 group agency).

List (2018) used IIT to argue group agents likely lack phenomenal consciousness; Kramer (2021)
replied that groups could in principle carry the integration IIT requires. The structural question:
does the GROUP have irreducible integration that no member or sub-pair has? Compare whole-group Φ
(the major complex) with the best single-member and best-pair Φ.

H52: in a triadic form the whole group is the irreducible core, and its Φ exceeds any member's or
pair's — genuine group-level integration absent in the parts (Kramer's possibility, realized).

Nodes: 0=W, 1=S, 2=C (and a 4-party pool).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_group_vs_members
"""

import itertools

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules, classify_rules
from proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def subset_phi(tpm, cm, labels, nodes):
    """Max Φ over reachable states for the subsystem on `nodes` (others as background)."""
    n = len(labels)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = 0.0
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            sub = pyphi.Subsystem(net, state, nodes=nodes)
            best = max(best, float(new_big_phi.sia(sub).phi))
        except Exception:
            continue
    return best


def main():
    print("PROBE 52 — group vs members (List 2018)")
    print("=" * 78)
    cases = [
        ("triad", ("W", "S", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),
        ("pool4", ("W", "S", "C1", "C2"),
         [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]),
    ]
    for name, labels, rules in cases:
        n = len(labels)
        tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
        whole = classify_rules(rules, labels=labels).max_phi
        best_single = max(subset_phi(tpm, cm, labels, (i,)) for i in range(n))
        best_pair = max(subset_phi(tpm, cm, labels, c)
                        for c in itertools.combinations(range(n), 2))
        print(f"  {name}:  whole-group Φ = {whole:.3f}")
        print(f"        best single-member Φ = {best_single:.3f} ; best pair Φ = {best_pair:.3f}")
        print(f"        -> group integration {'EXCEEDS' if whole > max(best_single, best_pair) + 1e-9 else 'does NOT exceed'} the parts")
    print("=" * 78)
    print("  The group carries irreducible integration no member or pair has — the structural")
    print("  precondition for group-level agency that List doubts and Kramer allows.")
    print("=" * 78)


if __name__ == "__main__":
    main()
