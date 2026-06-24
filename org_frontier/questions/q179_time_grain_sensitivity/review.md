# q179 — review

## What the probe shows

The update time-grain is a coding choice that moves the dyadic/triadic verdict. On 80 synthetic
accounts triadic per tick, 43 (0.537) flip to dyadic under a 2-tick coarse-graining (H1). The
flipping subset is verdict-indeterminate under a split coder panel (43/43) while the
grain-invariant subset is not (0/37), and a structural score read from the rule orbit predicts
the flip at AUC 0.666 (H2). The instrument control passes and the run is byte-identical across
three executions.

## Strengths

- Φ is not reimplemented; the probe reuses the bridge `rule_to_phi` and `phi_ci` and the
  classifier's exact-Φ oracle.
- The control is a genuine known-answer test on both poles: a cyclic triad that flips and a
  feedforward triple that does not, plus a predictor-ordering check.
- H1 and H2 thresholds were fixed before the computation and the verdict logic reports them
  mechanically from the numbers.
- The coder-disagreement arm is wired through the actual bridge CI rather than a separate
  calculation.

## Limits and threats

- The indeterminacy criterion is operationalized as the panel straddling the dyadic floor
  (minimum reading at Φ ≈ 0) rather than a strict CI-crosses-zero test. The bridge's bootstrap-t
  does not push the lower bound to zero for a discrete 0/positive panel, so the boundary-straddle
  criterion is the faithful read of verdict-indeterminacy here. This is stated in methods; a
  reviewer should know the CI itself does not numerically cross zero.
- AUC 0.666 clears the 0.6 bar but is modest. The flag is a screen, not a substitute for
  computing Φ at both grains.
- Only one coarse grain (k = 2) is tested. Larger strides and odd strides are unexplored.
- The ensemble is random Boolean truth tables over three parties, not coded field accounts. The
  effect size is in silico.

## Verdict

Both hypotheses supported on synthetic data. The claim is appropriately scoped: the grain is a
load-bearing coding choice, its effect is bounded on an ensemble, and the disagreement it
produces is carried into the bridge interval. No field validation is claimed.
