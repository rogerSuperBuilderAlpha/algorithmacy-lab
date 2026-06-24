# q174 — review

## Claim under test

The propagated Φ-CI width is a faithful read of coder disagreement, and there is a stable
agreement floor below which the verdict goes indeterminate. Both hypotheses resolve on
synthetic data: H1 supported (rho = -0.988, p = 4.26e-06), H2 confirmed (alpha* = 0.329 in
both ensembles).

## What would break it

- **The forms are engineered to flip.** Each triad is paired with a dyadic collapse one
  coupling-bit away. That pairing is what lets the CI cross zero. A form with no nearby
  collapse would widen with disagreement but never cross zero, so H2's threshold is a property
  of borderline forms, not of all forms. The probe should not be read as claiming every coded
  account has an alpha*.
- **alpha is injected, not observed.** The sweep sets disagreement by construction so alpha
  runs a clean grid. Real coders disagree in structured, non-uniform ways; the monotone width
  could be rougher on field data.
- **Eight coders.** The bootstrap-t is calibrated for small panels but remains an approximation,
  and the cross-zero fraction is averaged over only three forms, so it moves in coarse 1/3 steps.
- **The collapse Φ is exactly 0.** The zero-crossing is clean because the alternative reading
  sits at Φ = 0. A collapse to a small positive Φ would blur the indeterminacy boundary.

## What holds

- The control passes and is meaningful: it distinguishes magnitude disagreement (wide CI, lower
  bound above zero) from verdict disagreement (CI crosses zero).
- The relation is monotone and strong, not a single jump: width climbs across 0.34, 0.92, 1.57,
  2.27 as alpha falls, so the correlation is not an artifact of one outlier.
- alpha* is byte-identical across seeds, so the threshold claim is not seed-fishing.

## Scope

In-silico. Synthetic coder panels, Boolean forms, exact IIT-4.0 Φ via the shared bridge. No
worker is measured. The study validates the instrument; the field test is the open question.
