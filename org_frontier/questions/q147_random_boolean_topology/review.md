# q147 review

## What was tested

Whether a graph statistic of the dependency graph predicts the triadic/dyadic verdict (H1) and
whether core in-degree predicts Φ among triadic networks (H2), over 160 random Boolean networks
at n=4 and n=5.

## Strengths

- The control validates both the Φ instrument (faithful triad, Φ = 2.0) and the graph-statistic
  code (ring and hub against hand values) before any sampling.
- Seeded sampling; the run reproduces byte-identically across re-runs.
- The dependency graph is read by flip-test, so statistics reflect realized dependencies, not the
  nominal arity drawn during sampling.
- H1's decision rule was fixed in advance: the recurrence statistic must outrank mean degree,
  match the predicted direction, and clear p < 0.05.

## Weaknesses and threats

- Cycle density and mean degree are correlated in this ensemble (denser graphs hold more loops).
  The result is that cycle density carries more separating signal, not that degree is irrelevant.
  A degree-matched resample would sharpen the claim.
- 32 triadic networks is a thin base for H2. The null is "no detectable effect at this size."
- The p-values use a Fisher-z normal approximation for determinism, not a permutation test; for
  these sample sizes the approximation is adequate but not exact.
- n is capped at 5 by exact Φ, so the ensemble is small graphs. Whether the ranking holds for
  larger networks is untested.
- Synthetic data throughout. No field validation.

## Verdict

H1 supported, H2 refuted. The refutation is reported as such. The finding that recurrence
outranks degree is robust to the stated caveats; the H2 null should be read as inconclusive at
this sample size rather than as a demonstrated zero.
