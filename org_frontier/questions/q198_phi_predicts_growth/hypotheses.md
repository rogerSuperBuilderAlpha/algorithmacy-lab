# q198 — hypotheses

Question: does a worker's baseline (W1) Φ_coord predict the individual latent growth slope of
algorithmacy competence (ACS-total) over the program (waves W1-W3) in the simulated panel?

Fixed before computing.

**H1.** W1 Φ_coord positively predicts the individual latent ACS-growth slope (β > 0, 95% CI excludes
0): workers in more irreducible W1 coordination forms gain competence faster.
Null: the W1-Φ-to-slope β CI includes 0.

**H2.** W1 Φ_coord predicts the slope above and beyond the W1 ACS intercept (incremental over baseline
competence): the partial β for Φ_coord with the W1 ACS intercept controlled has a 95% CI that excludes 0.
Null: once the W1 ACS intercept is controlled, W1 Φ_coord adds nothing to the slope.

Controls fixed in advance:
- a shuffled-Φ placebo predictor (W1 Φ_coord permuted across workers) is expected to give a β whose CI
  includes 0;
- a forced-dyadic control cohort sets Φ_coord to 0 for every worker, so the predictor has no variance and
  the regression is undefined by construction — the form of the null, not a number.
