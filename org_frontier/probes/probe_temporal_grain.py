"""Probe 32 — temporal grain (one-step vs two-step dynamics).

Φ is computed on the one-step transition. What if a coordination form is observed every two steps?
Compose each corpus form's dynamics with itself (the 2-step map) and recompute the verdict. Does the
triad survive a coarser temporal grain, or does irreducibility change with the observation cadence?

H32: the verdict can change under temporal coarse-graining — some triads wash out (the 2-step map
factors) while others persist — so the verdict is grain-relative, a caveat for empirical sampling.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_temporal_grain
"""

import numpy as np

from org_frontier.classifier.classifier import classify, classify_rules
from org_frontier.corpus import forms_library as lib

LABELS = ("W", "S", "C")


def two_step(rules, n=3):
    """Build the 2-step state-by-node TPM and its connectivity (deterministic compose)."""
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        return tuple(int(rules[j](b)) for j in range(n))
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        once = succ(s)
        s1 = sum(once[j] << j for j in range(n))
        twice = succ(s1)
        for j in range(n):
            tpm[s, j] = float(twice[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def main():
    print("PROBE 32 — temporal grain (1-step vs 2-step)")
    print("=" * 72)
    print(f"  {'form':<24}{'1-step':<16}{'2-step'}")
    flips = 0
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        v1 = classify_rules(f.rules, labels=LABELS)
        tpm2, cm2 = two_step(f.rules)
        v2 = classify(tpm2, cm2, labels=LABELS)
        flip = v1.structure != v2.structure
        flips += flip
        print(f"  {f.key:<24}{v1.structure+' Φ='+format(v1.max_phi,'.2f'):<16}"
              f"{v2.structure+' Φ='+format(v2.max_phi,'.2f')}{'   <- FLIP' if flip else ''}")
    print("=" * 72)
    print(f"  verdict flips under 2-step grain: {flips}")
    print("=" * 72)


if __name__ == "__main__":
    main()
