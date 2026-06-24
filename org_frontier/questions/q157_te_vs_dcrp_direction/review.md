# q157 — review

## What the study claims

On a random Boolean ensemble, pairwise transfer entropy recovers the orientation of a directed
read edge at 77.2%, against 56.5% for the DCRP peak-lag sign. The errors correlate (phi +0.26) but
combining the methods still lifts recovery to 84.6%.

## Checks

- Ground truth is the exact `cm_from_rules` connectivity matrix, the same wiring the IIT-4.0
  machinery reads. The orientation labels are not inferred from behavior, so the scoring is not
  circular.
- The instrument control passes: the faithful triad reads triadic at max_phi 2.0, and the
  transfer-entropy estimator is directional on a clean one-way driver (forward 0.9986 against
  reverse 0.0006).
- Determinism holds: ensemble draws, trajectory sampling, and the control driver are all seeded.
  Two runs are byte-identical.
- Both ensembles show the same ordering and a double-digit gap, so the pooled result is not an
  artifact of one node count.

## Limits

- The transfer-entropy estimator is the plug-in binary lag-1 form. It is biased upward in small
  samples; the 800-step trajectory keeps the bias modest but does not remove it. The comparison is
  fair because both methods read the same trajectory, but the absolute TE rate could move with a
  bias-corrected estimator.
- A tie in transfer entropy and a zero DCRP lag both count as misses. The convention is fixed
  before scoring and applied to both methods, so it does not favor either.
- The OR-combine is an upper bound on a combined reader; it knows which method to trust per edge
  only in the sense of "either was right." A deployable combine would need a selection rule. The
  7.5-point lift shows the headroom exists, not that a blind combine captures it.
- In-silico. The forms are synthetic. The recovery rates do not transfer to coded field series
  without the open validation step.

## Verdict

The result is sound and the verdicts follow from the numbers. H1 supported, H2 refuted. The
honest surprise is H2: the methods were expected to fail together, and they partly do, but their
complementary errors leave real room for a combine.
