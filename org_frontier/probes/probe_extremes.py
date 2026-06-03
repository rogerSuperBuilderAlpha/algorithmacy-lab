"""Probe 30 — the structural extremes of the triad.

Over the complete strict-mediation n=3 family (reusing corpus.population.enumerate_family), find the
SPARSEST triadic form (fewest causal edges) and the MOST integrated form (highest Φ). What is the
minimal structure that makes coordination irreducible, and what maximizes it?

H30: the minimal triad has exactly the edges of a joint determination read back by both parties
(no slack); the maximal-Φ forms cluster on a specific determination type.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_extremes
"""

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family

LABELS = ("W", "S", "C")


def main():
    triadic = []
    for label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        if v.structure == "triadic":
            edges = int(cm_from_rules(rules).sum())
            triadic.append((label, edges, v.max_phi))

    if not triadic:
        print("no triadic forms"); return
    min_edges = min(t[1] for t in triadic)
    max_phi = max(t[2] for t in triadic)
    sparsest = [t for t in triadic if t[1] == min_edges]
    densest_phi = [t for t in triadic if t[2] == max_phi]

    print("PROBE 30 — structural extremes of the triad (strict-mediation family)")
    print("=" * 74)
    print(f"  triadic forms in family: {len(triadic)}")
    print(f"  edge counts among triadic: {sorted(set(t[1] for t in triadic))}")
    print(f"  Φ values among triadic: {sorted(set(round(t[2],3) for t in triadic))}")
    print(f"\n  SPARSEST triadic: {min_edges} edges ({len(sparsest)} forms), e.g. {sparsest[0][0]} "
          f"(Φ={sparsest[0][2]:.2f})")
    print(f"  MAX-Φ triadic: Φ={max_phi:.2f} ({len(densest_phi)} forms), e.g. {densest_phi[0][0]}")
    print("=" * 74)
    print("  Reading: the minimal triad is the leanest joint determination both parties read back;")
    print("  below that edge count, no strict-mediation form is irreducible.")
    print("=" * 74)


if __name__ == "__main__":
    main()
