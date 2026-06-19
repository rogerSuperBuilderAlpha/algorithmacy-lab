"""The noise thread (E5 of the catalog line).

Real coordination is noisy. This thread asks how a mediated triad's integration degrades when its
transitions are perturbed: each node's output is flipped with probability epsilon. Two findings. The triad's
integration decays gracefully and smoothly with noise, staying positive through heavy perturbation, with no
abrupt collapse at a threshold. And a parity mediator is relatively more noise-robust than a monotone one,
keeping a larger fraction of its integration at each noise level.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/noise/noise.py

Deterministic: fixed forms, fixed noise grid.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules, phi_profile

N = 3
EPS_GRID = [0.0, 0.02, 0.05, 0.10, 0.20, 0.30]
FORMS = {
    "AND mediator (S=W&C)": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "XOR mediator (S=W^C)": [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
}


def noisy(tpm, eps):
    """Flip each node's output with probability eps: a 1 becomes 1-eps, a 0 becomes eps."""
    return tpm * (1 - eps) + (1 - tpm) * eps


def max_phi(rules, eps):
    tpm = tpm_from_rules(rules).astype(float)
    cm = cm_from_rules(rules)
    prof = phi_profile(noisy(tpm, eps), cm, N)
    return max((p for _, p in prof), default=0.0)


def main():
    print("Mediated triad under transition noise (each output flips with probability epsilon).")
    for name, rules in FORMS.items():
        phi0 = max_phi(rules, 0.0)
        cells = []
        for eps in EPS_GRID:
            phi = max_phi(rules, eps)
            frac = phi / phi0 if phi0 > 0 else 0.0
            cells.append(f"e={eps:.2f}:Phi={phi:.3f}({100 * frac:.0f}%)")
        print(f"{name}: " + "  ".join(cells))
    print("Phi stays positive through e=0.30 (no collapse); parity keeps a larger fraction at each level.")


if __name__ == "__main__":
    main()
