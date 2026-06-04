"""Probe 67 (#49) — which aggregation rules yield triadic governance.

Question: a group decides through an aggregation rule; which rules make the decision form triadic?
Hypothesis: all-required (unanimity / AND) is triadic, majority factors (Probe 10), and the rest map
onto the pivotality story. Method: a decision node S aggregates three members (W, C1, C2) by each
rule; members track the decision. Classify each.

Nodes: 0=W, 1=S (decision), 2=C1, 3=C2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_voting
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C1", "C2")


def maj(a, b, c):
    return (a & b) | (a & c) | (b & c)


RULES = {
    "unanimity (AND)":   lambda x: x[0] & x[2] & x[3],
    "any (OR)":          lambda x: x[0] | x[2] | x[3],
    "majority (2of3)":   lambda x: maj(x[0], x[2], x[3]),
    "veto (W blocks)":   lambda x: x[0] & (x[2] | x[3]),
    "parity (XOR)":      lambda x: x[0] ^ x[2] ^ x[3],
}


def main():
    print("PROBE 67 (#49) — aggregation rules and triadic governance")
    print("=" * 78)
    for name, s in RULES.items():
        rules = [lambda x: x[1], s, lambda x: x[1], lambda x: x[1]]
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        parties = [p for p in ("W", "C1", "C2") if core and p in core]
        print(f"  {name:<18} {v.structure:<8} Φ={v.max_phi:.3f}  parties in core: {parties}")
    print("=" * 78)
    print("  Reading: aggregation rules differ in whether they bind the members into one irreducible")
    print("  decision. Rules where every member is pivotal bind; redundant rules (majority) factor.")
    print("=" * 78)


if __name__ == "__main__":
    main()
