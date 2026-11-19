"""Validate the instrument on its own controls before trusting any verdict.

Two controls and a five-form regression suite:

  1. FACTORING control   - a structure with a causally decoupled party must read DYADIC (Φ = 0).
  2. IRREDUCIBLE control - a fully coupled three-node network must read TRIADIC (Φ > 0).
  3. Regression suite    - each built-in form must match its expected verdict.

Run:  python -m irreducibility.validate      (exit code is non-zero if anything fails)
"""

import sys

from .core import classify_rules, PHI_EPS


def factoring_control():
    """W and S coupled, C decoupled: W' = S, S' = W, C' = C. Must be DYADIC."""
    return [lambda x: x[1], lambda x: x[0], lambda x: x[2]]


def irreducible_control():
    """Every node reads the other two: W' = S OR C, S' = W AND C, C' = W XOR S. Must be TRIADIC."""
    return [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]


# Built-in forms (W = worker, S = system/mediator, C = counterpart).
FORMS = {
    # chat with a language model: W and S loop; no third party (C decoupled)
    "chat_dyad": lambda: [lambda x: x[1], lambda x: x[0], lambda x: x[2]],
    # rideshare as a dyadic model sees it: the rider is dropped from dispatch
    "gig_dyadic_model": lambda: [lambda x: 1 - x[1], lambda x: x[0], lambda x: x[2] & (1 - x[1])],
    # résumé -> applicant-tracking system -> hiring manager, strict bottleneck
    "strict_mediation_triad": lambda: [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    # same strict topology with feedback reads that break liveness: it factors
    "ats_feedback_factors": lambda: [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[1] | x[2]],
    # the rider is constitutive of dispatch: presents as a dyad, reads the unseen third party
    "gig_false_dyad": lambda: [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])],
}

EXPECTED = {
    "chat_dyad": "dyadic",
    "gig_dyadic_model": "dyadic",
    "strict_mediation_triad": "triadic",
    "ats_feedback_factors": "dyadic",
    "gig_false_dyad": "triadic",
}


def controls_pass() -> bool:
    """True iff both controls read as expected (for scripts that must refuse to run otherwise)."""
    return (classify_rules(factoring_control()).structure == "dyadic"
            and classify_rules(irreducible_control()).structure == "triadic")


def main() -> int:
    print("=" * 80)
    print("IRREDUCIBILITY PIPELINE - instrument validation")
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
    for fname, builder in FORMS.items():
        v = classify_rules(builder())
        expect = EXPECTED[fname]
        ok = v.structure == expect
        failures += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {fname:<24} -> {v.structure:<8} "
              f"(Φ_MIP max {v.max_phi:.4f}; expected {expect})")

    print("\n[3/3] Summary")
    print(f"  PHI_EPS = {PHI_EPS:g}")
    if failures:
        print(f"  {failures} FAILURE(S) - do not trust verdicts until resolved.")
        return 1
    print("  All controls and built-in forms pass. Instrument validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
