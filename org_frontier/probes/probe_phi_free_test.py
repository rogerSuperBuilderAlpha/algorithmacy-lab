"""Probe 54 (#44) — a Φ-free structural test for triadicity.

Question: is the verdict equivalent to a graph/function predicate computable without Φ? Hypothesis: a
connectivity predicate (the mediator reads both parties and both parties read the mediator) is
necessary but over-predicts, because the corpus shows forms with all those edges that still factor
(the feedback case); a pivotality-augmented predicate gets closer. Method: over the complete
strict-mediation n=3 family (`enumerate_family`, 256 forms), compute two Φ-free predicates from the
connectivity / function sensitivities and compare each to the exact verdict.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phi_free_test
"""

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family

LABELS = ("W", "S", "C")


def main():
    n = tp = tn = fp = fn = 0
    for _label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        triadic = v.structure == "triadic"
        cm = cm_from_rules(rules)
        # Φ-free predicate: S reads W and C, and W and C each read S (all four edges present).
        pred = bool(cm[0, 1] and cm[2, 1] and cm[1, 0] and cm[1, 2])
        n += 1
        tp += pred and triadic
        tn += (not pred) and (not triadic)
        fp += pred and (not triadic)
        fn += (not pred) and triadic
    acc = (tp + tn) / n
    print("PROBE 54 (#44) — Φ-free connectivity predicate vs exact verdict (256 forms)")
    print("=" * 74)
    print(f"  predicate: S reads W and C, and W and C each read S (4 edges present)")
    print(f"  accuracy = {acc:.3f}   TP={tp} TN={tn} FP={fp} FN={fn}")
    print(f"  false positives (predicate triadic, verdict dyadic) = {fp}")
    print(f"  false negatives (predicate dyadic, verdict triadic) = {fn}")
    print("=" * 74)
    if fn == 0 and fp > 0:
        print("  Reading: the connectivity predicate is NECESSARY (no false negatives) but not")
        print("  sufficient (it over-predicts) — the function-level liveness Φ checks is not captured")
        print("  by edges alone. A Φ-free test needs a pivotality term, not just connectivity.")
    elif fn == 0 and fp == 0:
        print("  Reading: the connectivity predicate matches the verdict exactly — a Φ-free test.")
    print("=" * 74)


if __name__ == "__main__":
    main()
