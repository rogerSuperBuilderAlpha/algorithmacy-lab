# q152 — Review

## What was tested

Whether the whole-system verdict (triadic/dyadic) and major-complex membership disagree
across the studied topologies at n = 5, 6, and whether a zero-Shapley node marks the
disagreement.

## Strengths

- Reuses the studies 1-9 topology builders and the existing `verdict` / `major_complex` /
  `shapley` machinery verbatim; Φ is not reimplemented.
- Instrument control validates the triad (verdict triadic, max_phi 2.0, full core, no
  zero-Shapley party) before any new computation.
- The H2 test is a strict biconditional with both counterexample classes reported, so a
  near-miss correlation cannot be mistaken for confirmation.
- Deterministic: seeded RNG, exact enumeration, byte-identical re-runs.

## Limitations

- n is capped at 5, 6 by exact-Φ cost; larger systems are not probed, so the prevalence of
  disagreement at scale is unmeasured.
- The topology set is the pre-disclosed catalog, not an exhaustive sweep of Boolean forms;
  disagreement classes outside the catalog are not characterized.
- "Disagreement" is defined as any core exclusion under a triadic verdict; it does not
  weight how many parties are dropped or how central they are.
- Entirely in-silico. No field data; the result is a property of the diagnostics on
  synthetic forms, not a finding about organizations. The validation gap is open.

## Reading

A triadic verdict and a full-party core are distinct claims, and the catalog already
contains forms where the first holds without the second. Downstream studies that infer
membership from the whole-system verdict — or vice versa — should read both. The Shapley
value is not a substitute marker for core exclusion.
