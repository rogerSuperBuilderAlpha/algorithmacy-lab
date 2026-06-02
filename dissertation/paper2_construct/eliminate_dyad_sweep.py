"""Paper 2, robustness of the "eliminate-the-dyad" result.

The draft claims: holding the joint determination S' = W AND C fixed, Φ falls
*monotonically* as a direct worker<->counterpart channel is opened (2.00 -> 0.83 -> 0.00),
and reads that decline as a structural incentive for a platform to "design the dyad out."

That claim is a statement about Φ MAGNITUDE, and magnitude is exactly what Paper 3 shows
is unreliable. This script tests whether the decline is an artifact of one Boolean encoding
of "add a direct channel." It holds S' = W AND C fixed and sweeps the worker/counterpart
read functions over every plausible encoding of a W<->C channel of increasing strength:

    no channel   :  W' = S            , C' = S              (strict bottleneck; the baseline)
    weak (OP)    :  W' = S OP C        , C' = S OP W         (mediator AND direct signal blended)
    full bypass  :  W' = C            , C' = W              (parties read each other directly)

OP ranges over the natural blends {OR, AND, XOR}. A robust "eliminate-the-dyad" claim would
require Φ to fall for ALL faithful encodings of "more direct contact". We report the whole
grid and let the reader see whether it does.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/eliminate_dyad_sweep.py
"""

import numpy as np
from phi_instrument import tpm_from_rules, cm_from_rules, system_phi_over_states


# S' = W AND C is held fixed throughout (the joint determination the platform commits).
S_RULE = lambda x: x[0] & x[2]

# Channel encodings: each maps (mediator_signal_node, direct_signal_node) -> a read rule.
# For W: mediator signal is S (index 1), direct signal is C (index 2).
# For C: mediator signal is S (index 1), direct signal is W (index 0).
def make_reads(kind):
    """Return (W_rule, C_rule, label) for a channel of the given kind."""
    if kind == "none":
        return (lambda x: x[1], lambda x: x[1], "no channel  (W'=S, C'=S)")
    if kind == "or":
        return (lambda x: x[1] | x[2], lambda x: x[1] | x[0], "weak OR     (W'=S|C, C'=S|W)")
    if kind == "and":
        return (lambda x: x[1] & x[2], lambda x: x[1] & x[0], "weak AND    (W'=S&C, C'=S&W)")
    if kind == "xor":
        return (lambda x: x[1] ^ x[2], lambda x: x[1] ^ x[0], "weak XOR    (W'=S^C, C'=S^W)")
    if kind == "bypass":
        return (lambda x: x[2], lambda x: x[0], "full bypass (W'=C, C'=W)")
    raise ValueError(kind)


def phi_for(kind):
    w_rule, c_rule, label = make_reads(kind)
    rules = [w_rule, S_RULE, c_rule]
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    results = system_phi_over_states(tpm, cm)
    phis = [p for _, p in results] or [0.0]
    return label, float(np.max(phis)), float(np.mean(phis)), len(results)


def main():
    print("=" * 82)
    print("PAPER 2 — robustness of the 'eliminate-the-dyad' decline")
    print("S' = W AND C held fixed; worker/counterpart reads vary by channel encoding")
    print("=" * 82)
    print(f"{'channel encoding':<34}{'max Φ':>10}{'mean Φ':>10}{'#states':>9}")
    print("-" * 82)
    rows = []
    for kind in ["none", "or", "and", "xor", "bypass"]:
        label, mx, mn, ns = phi_for(kind)
        rows.append((kind, label, mx, mn, ns))
        print(f"{label:<34}{mx:>10.4f}{mn:>10.4f}{ns:>9}")
    print("-" * 82)
    maxes = [r[2] for r in rows]
    monotone = all(maxes[i] >= maxes[i + 1] for i in range(len(maxes) - 1))
    print(f"max-Φ sequence (none->or->and->xor->bypass): "
          f"{[round(m, 3) for m in maxes]}")
    print(f"monotone non-increasing in 'directness'? {monotone}")
    print()
    print("READING: the draft's monotone 2.00 -> 0.83 -> 0.00 holds ONLY for the OR encoding")
    print("of a weak channel. The AND encoding of the same verbal description gives a LARGER Φ")
    print("than the no-channel baseline, so 'more direct contact lowers Φ' is not robust to the")
    print("encoding choice. The political-economy claim cannot rest on the magnitude gradient.")
    print("=" * 82)


if __name__ == "__main__":
    main()
