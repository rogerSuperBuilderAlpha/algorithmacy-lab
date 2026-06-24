# q198 — review

Strengths.
- The instrument is validated on the canonical faithful triad before any panel number is read; the
  control prints `CONTROL ... PASS`.
- Φ is reused, not reimplemented: the probe imports the shared bridge module, which calls
  `classifier.tpm_from_rules` and `probes.lib.max_phi_float`.
- The run is deterministic (one fixed seed; the bridge and control cohorts each drawn from a freshly
  seeded generator), confirmed byte-identical over three runs.
- Two nulls are reported honestly: a shuffled-Φ placebo (CI includes 0) and a forced-dyadic control
  cohort (Φ_coord constant at 0, predictor undefined by construction).
- H2 separates the Φ effect from baseline competence by controlling the W1 ACS intercept.

Limits and validation gap.
- The panel is SIMULATED. The growth and the Φ-to-slope coupling are synthetic by construction, so the
  supported hypotheses show the pipeline recovers a planted effect, not that the effect exists in a real
  cohort. No worker is measured and no wave file exists.
- Φ_coord takes only two values (0 or 2), so it behaves as a binary commit indicator; β is per unit of
  Φ_coord and the commit-vs-convey slope gap is about twice it. A graded Φ_coord would need a richer form
  family.
- The CIs are normal-theory OLS intervals (z≈t at large dof); they are not bootstrapped and assume the
  planted homoscedastic-noise model.
- The LGC is a per-worker OLS over three equally-spaced points, not a full SEM latent growth model with a
  measurement model; the codebook's pre-registered LGM would replace it on real data.

Verdict. Both H1 and H2 are supported on the synthetic panel, with the placebo and control behaving as
expected. The finding is about the bridge and the growth pipeline on synthetic data.
