"""Validate the instrument on its own controls BEFORE trusting any verdict.

The repo's load-bearing rule (RESEARCH_PLAYBOOK.md): validate the instrument on its own
controls before computing any comparison, and compute, do not assert. Two controls plus the
built-in regression suite:

  1. FACTORING control   — a form with a causally decoupled party must classify DYADIC (Φ ≈ 0).
  2. IRREDUCIBLE control — a fully coupled 3-node network must classify TRIADIC (Φ > 0).
  3. Regression suite     — every built-in form matches its EXPECTED structural verdict.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.validate
Exit code is non-zero if any control fails.
"""

import sys

from .classifier import classify_rules, PHI_EPS
from . import forms


def factoring_control():
    """W and S coupled, C decoupled. Splits into {W,S} ⊗ {C}; must be DYADIC.
        W' = S,  S' = W,  C' = C."""
    return [lambda x: x[1], lambda x: x[0], lambda x: x[2]]


def irreducible_control():
    """Canonical integrated 3-node network; every node reads the other two. Must be TRIADIC.
        W' = S OR C,  S' = W AND C,  C' = W XOR S."""
    return [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]


def main() -> int:
    print("=" * 80)
    print("LITERACY-OR-ALGORITHMACY CLASSIFIER — instrument validation")
    print("=" * 80)
    failures = 0

    print("\n[1/3] Controls")
    for name, rules, expect in [
        ("factoring   (C decoupled)", factoring_control(), "dyadic"),
        ("irreducible (full coupling)", irreducible_control(), "triadic"),
    ]:
        v = classify_rules(rules)
        ok = v.structure == expect
        failures += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name:<30} -> {v.structure:<8} "
              f"(Φ_MIP max {v.max_phi:.4f}; expected {expect})")

    print("\n[2/3] Built-in forms (regression suite)")
    for fname, builder in forms.FORMS.items():
        v = classify_rules(builder())
        expect = forms.EXPECTED[fname]
        ok = v.structure == expect
        failures += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {fname:<22} -> {v.structure:<8} "
              f"({v.competence:<12} Φ_MIP max {v.max_phi:.4f}; expected {expect})")

    print("\n[3/3] Summary")
    print(f"  PHI_EPS = {PHI_EPS:g}")
    if failures:
        print(f"  {failures} FAILURE(S) — do not trust verdicts until resolved.")
        return 1
    print("  All controls and built-in forms pass. Instrument validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
