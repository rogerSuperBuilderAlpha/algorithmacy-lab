# q157 — hypotheses

Both hypotheses were fixed before any number was computed.

## Setup

A directed read edge i -> j means node j's rule depends on node i (`cm[i, j] = 1`), so i leads j.
Two behavioral methods read orientation from a sampled trajectory and are scored against this
ground truth:

- DCRP peak-lag sign: a positive peak lag of the diagonal cross-recurrence profile for the
  ordered pair (i, j) says i leads j.
- pairwise transfer entropy: TE(i -> j) against TE(j -> i); the larger direction wins.

## H1

Pairwise transfer entropy recovers true directed-edge orientation at a higher rate than DCRP
peak-lag sign on the random ensemble, exceeding it by more than 5 percentage points.

Null: the two methods recover direction at indistinguishable rates.

Verdict rule: SUPPORTED when the TE recovery rate minus the DCRP recovery rate exceeds 5
percentage points, REFUTED otherwise.

## H2

DCRP and transfer entropy fail on the same edges (common-driver and reciprocal pairs), so their
errors are correlated rather than complementary. Combining the two methods would not raise
recovery.

Null: their errors are independent, so the OR-combine of the two methods raises recovery above
either alone.

Verdict rule: SUPPORTED when the phi coefficient of the per-edge hit indicators is positive and
the OR-combine lifts recovery by at most 1 percentage point over the better single method.
REFUTED otherwise. The two conditions can split: a positive phi shows the errors share structure,
while a real OR-lift shows the errors are still partly complementary.
