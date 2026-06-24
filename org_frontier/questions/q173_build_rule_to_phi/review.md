# q173 — review

## What was built

The shared field bridge `org_frontier/field/rule_to_phi.py` and study 1 of the field line. The
module exposes `rule_to_phi`, `krippendorff_alpha`, `phi_ci`, and `phi_ci_from_rules`, and reuses
`tpm_from_rules`, `classify_rules`, and `verdict` from the classifier and probe library. Φ is not
reimplemented.

## What holds

- Instrument controls pass: the decoupled rule set reads dyadic; the faithful triad reads triadic
  with max Φ_MIP = 2.0; the agreement control returns a degenerate CI [2.0, 2.0] at alpha = 1.
- H1 (verdict reproducibility) supported: 0 verdict-flips over 250 sampled rule forms, plus the
  degenerate CI under perfect agreement.
- H2 (CI coverage) supported: coverage 0.944 over 500 coder panels, inside [0.93, 0.97].
- Output is byte-identical across three runs (deterministic, seeded).

## Limits and open points

- The CI interval is a studentized bootstrap-t. The plain percentile bootstrap under-covers at
  small coder counts (around 0.91 at n = 12 in calibration), so the bootstrap-t was chosen for
  calibration. The studentized interval is calibrated for roughly symmetric coder-noise; a panel
  with strongly skewed coding error would need a BCa or a different studentizing statistic, and
  that case is not exercised here.
- The H2 coder-noise model is mean-zero by construction: a mis-coded cell shifts the reading by a
  symmetric ±0.30. This makes the consensus Φ the true mean, which is what the CI is asked to
  cover. A coding process with systematic bias (all coders slipping in one direction) would shift
  the truth off the panel mean and is out of scope for this validation.
- Coverage 0.944 sits inside the band but below the 0.95 center; at n = 10 coders it falls to
  0.938, still inside [0.93, 0.97] but near the edge. A later study can widen the panel or report
  the coverage curve across coder counts.
- All inputs are synthetic with known ground truth. The bridge scores coded accounts, not
  observed coordinations. The coded-account-to-observation gap is not addressed.

## Verdict

The bridge is valid on its controls and calibrated on the synthetic coverage test. It is ready
for the rest of the field line to import.
