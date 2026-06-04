"""Probe 62 (#10) — update scheduling.

Question: is the verdict stable under sequential (one-node-at-a-time) update rather than simultaneous
update? Hypothesis: the verdict can depend on the update schedule, since sequential composition is a
different deterministic map. Method: for the triadic corpus forms, build the sequential-update TPM
(apply each node's rule in a fixed order within a step, each seeing the latest values) for a few orders,
classify, and compare with the simultaneous verdict.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_async
"""

import itertools

import numpy as np

from org_frontier.classifier.classifier import classify, classify_rules
from org_frontier.corpus import forms_library as lib

LABELS = ("W", "S", "C")


def sequential_tpm(rules, order, n=3):
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for j in order:                       # update in `order`, each sees latest values
            state[j] = int(rules[j](tuple(state)))
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def main():
    print("PROBE 62 (#10) — update scheduling (simultaneous vs sequential)")
    print("=" * 78)
    print(f"  {'form':<24}{'simultaneous':<14}{'sequential orders (verdicts)'}")
    for f in lib.FORMS:
        if len(f.rules) != 3 or classify_rules(f.rules, labels=LABELS).structure != "triadic":
            continue
        sim = classify_rules(f.rules, labels=LABELS).structure
        seq = []
        for order in itertools.permutations(range(3)):
            tpm, cm = sequential_tpm(f.rules, order)
            seq.append(classify(tpm, cm, labels=LABELS).structure[:3])
        print(f"  {f.key:<24}{sim:<14}{seq}")
    print("=" * 78)
    print("  Reading: where the sequential verdicts differ from the simultaneous one, the verdict")
    print("  is schedule-relative — another reason the modeling choice (here, update timing) must")
    print("  be stated with the verdict.")
    print("=" * 78)


if __name__ == "__main__":
    main()
