"""Probe 80 (#18) — do Φ and coordination success decouple over learning?

Question: as a worker is "trained" toward higher coordination success, does Φ track it? Hypothesis: no
— success and Φ are orthogonal (Probe 48), so a learning path that climbs in success need not climb in
Φ. Method: hold the system fixed (S'=W∧C, C'=S) and sweep the worker's policy over candidate update
functions; for each compute the success rate (mean attractor match-rate) and exact Φ. A learning loop
visits increasing-success policies; report whether Φ tracks success along that ordering.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_learning
"""

from org_frontier.classifier.classifier import classify_rules
from .probe_variance import success_rate

LABELS = ("W", "S", "C")

# candidate worker policies (W' as a function of the state); S'=W∧C, C'=S fixed
POLICIES = {
    "reactive (S)":      lambda x: x[1],
    "persistent (S∨W)":  lambda x: x[1] | x[0],
    "eager (1)":         lambda x: 1,
    "cautious (S∧W)":    lambda x: x[1] & x[0],
    "contrarian (¬S)":   lambda x: 1 - x[1],
    "withdrawn (0)":     lambda x: 0,
}


def main():
    rows = []
    for name, wp in POLICIES.items():
        rules = [wp, lambda x: x[0] & x[2], lambda x: x[1]]
        v = classify_rules(rules, labels=LABELS)
        rows.append((name, success_rate(rules), v.max_phi, v.structure))
    rows.sort(key=lambda r: r[1])  # order by ascending success (the learning path)
    print("PROBE 80 (#18) — Φ vs success along the learning path")
    print("=" * 70)
    print(f"  {'policy':<20}{'success':<10}{'Φ':<8}{'verdict'}")
    for name, sr, phi, struct in rows:
        print(f"  {name:<20}{sr:<10.2f}{phi:<8.3f}{struct}")
    print("=" * 70)
    # does Φ rise monotonically with success along the ordering?
    phis = [r[2] for r in rows]
    monotone = all(phis[i] <= phis[i + 1] + 1e-9 for i in range(len(phis) - 1))
    print(f"  Φ monotone in success along the path: {monotone}")
    print("  Reading: if Φ does not climb with success, training a worker toward better coordination")
    print("  does not make the form more triadic — success is the level, Φ is the kind (Probe 48).")
    print("=" * 70)


if __name__ == "__main__":
    main()
