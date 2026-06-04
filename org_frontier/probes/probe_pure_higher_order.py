"""Probe 56 (#47) — pure higher-order binding.

Question: is there a triadic form whose irreducibility appears only at the whole, with no irreducible
proper subset? Hypothesis: yes; the parity (Φ=0.5) forms bind synergistically with no lower-order
seed. Method: over the triadic forms of the strict-mediation n=3 family, compute the max Φ over all
proper subsystems (every single node and pair, with the others as background). A triadic form whose
best proper subset has Φ = 0 is purely higher-order.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_pure_higher_order
"""

import itertools

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family
from proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
LABELS = ("W", "S", "C")


def best_proper_subset_phi(tpm, cm):
    net = pyphi.Network(tpm, cm=cm, node_labels=LABELS)
    best = 0.0
    subsets = [c for k in (1, 2) for c in itertools.combinations(range(3), k)]
    for s in reachable_states(tpm, 3):
        state = tuple((s >> i) & 1 for i in range(3))
        for nodes in subsets:
            try:
                sub = pyphi.Subsystem(net, state, nodes=nodes)
                best = max(best, float(new_big_phi.sia(sub).phi))
            except Exception:
                continue
    return best


def main():
    pure = []
    seeded = []
    for label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        if v.structure != "triadic":
            continue
        tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
        sub_phi = best_proper_subset_phi(tpm, cm)
        (pure if sub_phi < 1e-9 else seeded).append((label, round(v.max_phi, 3), round(sub_phi, 3)))
    print("PROBE 56 (#47) — pure higher-order binding (triadic forms, n=3 family)")
    print("=" * 74)
    print(f"  triadic forms examined: {len(pure) + len(seeded)}")
    print(f"  PURE higher-order (no irreducible proper subset): {len(pure)}")
    for lab, phi, sp in pure[:6]:
        print(f"    {lab:<16} whole Φ={phi}  best-subset Φ={sp}")
    print(f"  seeded (some proper subset already irreducible): {len(seeded)}")
    for lab, phi, sp in seeded[:6]:
        print(f"    {lab:<16} whole Φ={phi}  best-subset Φ={sp}")
    print("=" * 74)


if __name__ == "__main__":
    main()
