# Q84 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether an added agent X can change the coordination's verdict from outside the core.
The verdict is read on the maximal complex (per the Q74 rule). Written and committed before any test runs.

## H1 — A read-only agent leaves the core unchanged

- **Claim:** A read-only X (reads M, read by none) leaves the maximal complex {E, M, R} triadic (Φ > 0).
- **H0:** A read-only X changes the core or its verdict.
- **Predicted outcome:** core {E, M, R}, triadic. H0 refuted.

## H2 — An emit-only agent leaves the core unchanged

- **Claim:** An emit-only X (a constant source the determination ignores) leaves the maximal complex
  {E, M, R} triadic.
- **H0:** An emit-only X changes the core or its verdict.
- **Predicted outcome:** core {E, M, R}, triadic. H0 refuted.

## H3 — A bidirectional, pivotal agent changes the core

- **Claim:** A bidirectional, pivotal X (M reads X so M'=E∧R∧X, and X reads M) changes the maximal
  complex; X joins or alters it.
- **H0:** The bidirectional-pivotal X leaves the core {E, M, R}.
- **Predicted outcome:** the core is not {E, M, R}. H0 refuted.

## H4 — No non-core coupling flips the core verdict

- **Claim:** Neither the read-only nor the emit-only coupling makes the core verdict dyadic; influence over
  the verdict requires membership.
- **H0:** A non-core coupling flips the core verdict to dyadic.
- **Predicted outcome:** the core stays triadic under both non-core couplings. H0 refuted.
