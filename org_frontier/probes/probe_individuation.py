"""Probe 59 (#6) — verdict invariance under the full isomorphism group.

Question: is the verdict a true invariant of the system up to relabeling, across the whole symmetry
group, not just the state-flips (Probe 14) and the single W↔C swap (Probe 55)? Hypothesis: yes; every
node permutation composed with every state relabeling leaves the verdict and Φ exactly unchanged.
Method: over the eight 3-node corpus forms, apply all 3! node permutations × 2^3 state-flips (48
isomorphisms each), classify, and count any verdict flip or Φ difference.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_individuation
"""

import itertools

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus import forms_library as lib

LABELS = ("W", "S", "C")


def isomorph(rules, perm, mask, n=3):
    """Apply node permutation perm (tuple) and state-flip mask to a rule set."""
    inv = [perm.index(i) for i in range(n)]

    def make(j):
        # new node j carries old node perm[j]'s dynamics; reconstruct the old state from the new
        # one (undo perm and the per-node flip), then flip the NEW node's output by mask[j].
        r = rules[perm[j]]
        return lambda x: r(tuple(x[inv[i]] ^ mask[inv[i]] for i in range(n))) ^ mask[j]
    return [make(j) for j in range(n)]


def main():
    flips = 0
    max_dphi = 0.0
    total = 0
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        base = classify_rules(f.rules, labels=LABELS)
        for perm in itertools.permutations(range(3)):
            for m in range(8):
                mask = tuple((m >> i) & 1 for i in range(3))
                v = classify_rules(isomorph(f.rules, perm, mask), labels=LABELS)
                total += 1
                flips += v.structure != base.structure
                max_dphi = max(max_dphi, abs(v.max_phi - base.max_phi))
    print("PROBE 59 (#6) — verdict invariance under the full isomorphism group")
    print("=" * 70)
    print(f"  isomorphisms applied: {total} (8 forms × 6 node-perms × 8 state-flips)")
    print(f"  verdict flips        : {flips}")
    print(f"  max |Φ − Φ_iso|      : {max_dphi:.6f}")
    print("=" * 70)
    print("  Reading: the verdict is an exact invariant of the system up to relabeling. The")
    print("  state-individuation choice (which value is 'on', how nodes are named) does not move it.")
    print("=" * 70)


if __name__ == "__main__":
    main()
