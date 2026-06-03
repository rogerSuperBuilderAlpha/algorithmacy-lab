"""Probe 14 — is the binary verdict encoding-robust?

Paper 2 concedes Φ magnitude is encoding-dependent but claims the dyadic/triadic verdict is robust.
Stress-test that with two batteries:

  (A) Isomorphism invariance: relabel each node's 0/1 state meaning (8 masks). This is an IIT
      symmetry, so Φ AND the verdict must be EXACTLY invariant — a well-definedness check.
  (B) Determination re-encoding: replace the mediator's rule with each of AND/OR/NAND/NOR/XOR over
      the same two inputs (all "read both"), keeping the parties' reads. The dissertation predicts
      the verdict holds while magnitude moves.

H14: verdict-flip rate = 0 under (A) with zero Φ variance; under (B) verdict stays triadic while Φ
varies (magnitude is the soft part, verdict the hard part).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_robustness
"""

import numpy as np

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus import forms_library as lib

LABELS = ("W", "S", "C")


def relabel(rules, mask, n=3):
    """Flip the 0/1 meaning of nodes in `mask` (tuple of 0/1). An IIT isomorphism."""
    def make(j):
        r = rules[j]
        return lambda x: r(tuple(x[i] ^ mask[i] for i in range(n))) ^ mask[j]
    return [make(j) for j in range(n)]


def battery_A():
    print("  (A) Isomorphism invariance — Φ and verdict must be EXACTLY invariant")
    flips = 0
    phi_var = 0.0
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        base = classify_rules(f.rules, labels=LABELS)
        phis, verdicts = [], []
        for m in range(8):
            mask = tuple((m >> i) & 1 for i in range(3))
            v = classify_rules(relabel(f.rules, mask), labels=LABELS)
            phis.append(v.max_phi)
            verdicts.append(v.structure)
        flips += sum(s != base.structure for s in verdicts)
        phi_var = max(phi_var, np.ptp(phis))
        print(f"    {f.key:<22} base {base.structure:<8} Φ={base.max_phi:.3f}  "
              f"verdict-flips={sum(s != base.structure for s in verdicts)}/8  Φ-range={np.ptp(phis):.2e}")
    print(f"  -> total verdict flips under relabeling: {flips} ; max Φ range: {phi_var:.2e}")
    return flips


def battery_B():
    print("\n  (B) Determination re-encoding — verdict stable, magnitude varies")
    # canonical triad: S reads W (x0) and C (x2); parties track S.
    reencodings = {
        "AND":  lambda x: x[0] & x[2],
        "OR":   lambda x: x[0] | x[2],
        "NAND": lambda x: 1 - (x[0] & x[2]),
        "NOR":  lambda x: 1 - (x[0] | x[2]),
        "XOR":  lambda x: x[0] ^ x[2],
    }
    phis, verdicts = [], []
    for name, s in reencodings.items():
        rules = [lambda x: x[1], s, lambda x: x[1]]
        v = classify_rules(rules, labels=LABELS)
        phis.append(v.max_phi)
        verdicts.append(v.structure)
        print(f"    S'={name:<5} {v.structure:<8} Φ={v.max_phi:.3f}")
    tri = sum(s == "triadic" for s in verdicts)
    print(f"  -> {tri}/{len(reencodings)} re-encodings triadic ; Φ range {min(phis):.2f}–{max(phis):.2f} "
          f"(CV={np.std(phis)/max(np.mean(phis),1e-9):.2f})")


def main():
    print("PROBE 14 — verdict robustness to encoding")
    print("=" * 84)
    battery_A()
    battery_B()
    print("=" * 84)


if __name__ == "__main__":
    main()
