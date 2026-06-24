# q178 — review

## Claim under test

Collapsing a 3-valued coded action to one bit at different cut points changes the Φ verdict for
more than 20% of accounts (H1), and a coder panel split across the cut carries a Φ CI more than 2x
wider than a single-cut panel (H2).

## What the probe does

It builds a graded-to-binary calibration step (`b = 1[g >= t]`) on top of the q173 bridge, sweeps
the two cut points over a seeded 200-account panel, counts verdict flips, and compares the
propagated `phi_ci` widths of a split-threshold and a same-threshold coder panel on one
boundary-grade account.

## Controls

- Instrument control: faithful triad reads triadic at Φ = 2.0. PASS.
- Threshold-invariance control: monotone grades 0 and 2 do not flip. PASS.
- Single-cut CI control: the same-threshold panel uses one cut, giving the reading-noise baseline
  width the split panel is measured against.

## Strengths

- The grade-to-bit map is transparent and the flip behavior follows from it deterministically, so
  the 0.33 flip rate is the share of boundary-grade accounts in the panel, not an artifact of a
  contrived mix. The draw is uniform over the three grades.
- H2 uses a non-degenerate single-cut baseline (small seeded reading jitter) rather than a
  zero-width point, so the width ratio is finite and well-defined. The negative alpha on the split
  panel correctly localizes the spread to the cut.

## Limits and threats

- Synthetic throughout. No worker action is measured; the grade is stipulated, not observed. The
  map from a coded grade to a real action is not validated.
- The action is 3-valued with two cut points. Finer grades or more parties would change the flip
  rate; the 0.33 figure is specific to this construction.
- The CI width ratio depends on the chosen jitter scale (sd = 0.02). A larger within-coder noise
  would shrink the ratio. The qualitative result (split >> same) is robust to the scale, but the
  47.6 figure is not a universal constant.
- Only the boundary grade flips by design, so H1 tests whether boundary accounts are common enough
  to matter, not whether the machinery can flip at all.

## Verdict

H1 SUPPORTED (flip rate 0.33 > 0.20). H2 SUPPORTED (width ratio 47.6 > 2). Output is deterministic
and byte-identical across three runs. The conclusions hold for the synthetic construction and motivate
fixing and reporting the bit cut in any real coding protocol.
