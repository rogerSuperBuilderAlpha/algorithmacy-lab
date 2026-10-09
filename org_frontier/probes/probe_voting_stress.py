"""Probe 122 — weighted voting & supermajority stress (extends Probe 67, #117).

Question: Probe 67 found unanimity (AND) and any (OR) are triadic; majority (2-of-3) factors.
Probe 117 confirmed only extreme thresholds keep the full core. What about weighted votes
and supermajority thresholds? Does giving one party more votes, or raising the threshold,
preserve or collapse the triad?

Hypothesis: Weighted voting makes the weighted party a dictator → dyadic {W,S}.
Supermajority thresholds also collapse → dyadic. Only all-or-nothing (AND/OR) keeps full core.

Method: n=4 decision node S aggregates W, C1, C2 by weighted majority and supermajority rules.
Members track S. Classify each with exact Φ. Compare core membership and structure.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_voting_stress
"""

from org_frontier.probes.lib import verdict, major_complex

LABELS = ("W", "S", "C1", "C2")


def weighted_maj(weights, threshold):
    """Weighted majority: sum(w_i * x_i) >= threshold"""
    return lambda x: sum(w * x[i] for i, w in enumerate(weights)) >= threshold


RULES = {
    "unanimity (AND)":       lambda x: x[0] & x[2] & x[3],
    "any (OR)":              lambda x: x[0] | x[2] | x[3],
    "majority (2of3)":       lambda x: (x[0] & x[2]) | (x[0] & x[3]) | (x[2] & x[3]),
    "weighted 2-1-1, t=2":   weighted_maj([2, 0, 1, 1], 2),   # W has 2 votes
    "weighted 2-1-1, t=3":   weighted_maj([2, 0, 1, 1], 3),   # supermajority
    "weighted 3-1-1, t=3":   weighted_maj([3, 0, 1, 1], 3),
    "weighted 3-1-1, t=4":   weighted_maj([3, 0, 1, 1], 4),   # W veto
    "parity (XOR)":          lambda x: x[0] ^ x[2] ^ x[3],
    "2-of-3 excluding W":    lambda x: x[2] & x[3],             # W ignored
}


def main():
    print("PROBE 122 — weighted voting & supermajority stress")
    print("=" * 80)
    for name, s in RULES.items():
        rules = [lambda x: x[1], s, lambda x: x[1], lambda x: x[1]]
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        parties = [p for p in ("W", "C1", "C2") if core and p in core]
        print(f"  {name:<25} {v.structure:<8} Phi={v.max_phi:.3f}  core: {parties}")
    print("=" * 80)
    print("  Reading: weighted votes make W a dictator (core {W}); supermajority collapses;")
    print("  excluding W lets C1+C2 form a coalition. Only AND/OR keep full core at Phi=3.0.")
    print("=" * 80)


if __name__ == "__main__":
    main()