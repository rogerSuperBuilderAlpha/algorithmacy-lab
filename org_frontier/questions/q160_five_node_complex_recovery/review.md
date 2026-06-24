# Review — q160

## Claim under test
Coupling centrality recovers major-complex membership at five parties at roughly the four-node rate,
and the worker excluded from `deep_pool_all`'s core is not a behavioral false positive.

## Checks
- Instrument control passes: the faithful triad reads major complex {W,S,C} at Φ=2.0 with the
  mediator top-coupled. The machinery is the published bridge code (`major_complex`, `separates`,
  `coupling_centrality`), reused unchanged.
- Determinism: output is byte-identical across three runs. Trajectory seeds are fixed; the Φ library
  seeds its state search internally.
- The pooled fraction rests on 43 testable forms. The named set is small (4 testable), so the ensemble
  carries the estimate. A 40-draw ensemble gives a wide confidence interval, so the 34.9% point is not
  precise to a percent.

## Weaknesses
- H1's SUPPORTED verdict is on a threshold the result barely clears: 34.9% versus 36% is one form out
  of 43. The honest reading is no widening, recorded in FINDINGS and the paper. A reader should not
  take H1 as evidence the dissociation grows with scale.
- The four-node 36% baseline comes from a different ensemble size and draw seed, so the comparison is
  between two point estimates, not a matched test. The conclusion is the weaker "no meaningful change",
  which the data support.
- A single trajectory per form sets the separation call; H2 uses 20 seeds and is robust, but the
  ensemble separation fractions could shift a few points under a different trajectory seed.

## Scope
In-silico. Exact Φ on Boolean forms; CRQA on synthetic trajectories. No organization is measured. The
result bounds how well a cheap behavioral instrument tracks the structural core, a baseline for the
field protocol on a real recorded series.
