"""Probe 60 (#7) — the temporal-grain threshold.

Question: Probe 32 found the 2-step map washes the triad out; at what grain does each triadic form
flip, and how does that relate to its attractor period? Hypothesis: a triadic form survives up to a
grain tied to its dynamics, so there is a detectable band. Method: compose the k-step map for k=1..6
on the triadic corpus forms and find the first k at which the verdict flips, alongside the form's
attractor period.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_grain_threshold
"""

import numpy as np

from org_frontier.classifier.classifier import classify, classify_rules
from org_frontier.corpus import forms_library as lib

LABELS = ("W", "S", "C")


def k_step(rules, k, n=3):
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        return sum(int(rules[j](b)) << j for j in range(n))
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        t = s
        for _ in range(k):
            t = succ(t)
        for j in range(n):
            tpm[s, j] = float((t >> j) & 1)
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def attractor_period(rules, n=3):
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        return sum(int(rules[j](b)) << j for j in range(n))
    periods = []
    for s0 in range(2 ** n):
        seen, s = [], s0
        while s not in seen:
            seen.append(s); s = succ(s)
        periods.append(len(seen) - seen.index(s))
    return max(periods)


def main():
    print("PROBE 60 (#7) — temporal-grain threshold")
    print("=" * 70)
    print(f"  {'form':<24}{'flip-k':<8}{'attractor period'}")
    for f in lib.FORMS:
        if len(f.rules) != 3 or classify_rules(f.rules, labels=LABELS).structure != "triadic":
            continue
        flip_k = None
        for k in range(1, 7):
            tpm, cm = k_step(f.rules, k)
            if classify(tpm, cm, labels=LABELS).structure == "dyadic":
                flip_k = k
                break
        per = attractor_period(f.rules)
        print(f"  {f.key:<24}{str(flip_k):<8}{per}")
    print("=" * 70)
    print("  Reading: the grain at which the triad disappears is short for these collapsing forms,")
    print("  so empirical sampling must be fine relative to the coordination's own cycle.")
    print("=" * 70)


if __name__ == "__main__":
    main()
