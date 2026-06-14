# Q117 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether a Φ-free predicate reproduces the exact verdict. The program reads triadicity with
exact IIT-4.0 Φ; this asks whether a predicate computed without Φ, from the truth tables alone, matches the
oracle on the whole 256-form strict-mediation family (Q93). Written and committed before the run; the
instrument was validated.

Two Φ-free predicates are tested against the exact-Φ oracle: the topology-only feedback cycle, and the cycle
plus a logical composition condition.

## H1 — The feedback cycle is necessary

- **Claim:** Every triadic form exhibits the full effective feedback cycle: the mediator depends on both
  outer parties and both outer parties depend on the mediator. No triadic form lacks it.
- **H0:** Some triadic form lacks the full cycle.
- **Predicted outcome:** the cycle predicate has no false negatives. H0 refuted. The cycle is a necessary
  screen for triadicity.

## H2 — The feedback cycle is not sufficient

- **Claim:** Some forms with the full feedback cycle are dyadic; the topology alone does not decide the
  verdict.
- **H0:** Every full-cycle form is triadic — topology suffices.
- **Predicted outcome:** the cycle predicate has false positives. H0 refuted. A connectivity check cannot
  replace the oracle.

## H3 — The cycle plus a logical condition matches the oracle exactly

- **Claim:** A Φ-free predicate combining the cycle with a composition condition (a parity mediator always
  binds; a non-parity mediator binds iff the outer reads' phase alignment matches the mediator's symmetry
  under swapping its inputs) reproduces the exact verdict on all 256 forms with zero error.
- **H0:** The predicate misclassifies at least one form.
- **Predicted outcome:** zero errors. H0 refuted. A Φ-free necessary-and-sufficient test for triadicity
  exists on this family. This is the study's genuinely uncertain claim — the composition condition could
  equally have failed on some form, leaving the oracle irreplaceable.

## H4 — The deciding factor is logic, not wiring

- **Claim:** Among the forms that share the full-cycle wiring, the verdict splits into triadic and dyadic; the
  two classes differ only in the truth-table composition, not the connectivity diagram.
- **H0:** No such split — the wiring fixes the verdict.
- **Predicted outcome:** the full-cycle forms split. H0 refuted. The verdict is a property of the
  determination's logic, not its graph alone.
