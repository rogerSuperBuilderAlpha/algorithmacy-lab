# Q98 findings — the membership gate is hard at the corners, soft inside

Three hypotheses confirmed, one refuted. A node that does not read, or is not read, never enters the core,
and a node strong on both axes always does. But across the interior, the two influences trade off
additively: the sum predicts membership as well as the minimum, so the gate is not the strict conjunction
the third hypothesis posited.

| condition | P(in core) | n |
|---|---|---|
| strong influence, zero reading | 0.000 | 33 |
| strong reading, zero influence | 0.000 | 29 |
| strong on both | 1.000 | 28 |
| rank-AUC: min(read, influence) → core | 0.772 | 3600 |
| rank-AUC: sum(read, influence) → core | 0.783 | 3600 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | strong influence cannot compensate zero reading (P < 0.10) | confirmed (0.000) |
| H2 | strong reading cannot compensate zero influence (P < 0.10) | confirmed (0.000) |
| H3 | membership tracks the minimum better than the sum | refuted (0.772 < 0.783) |
| H4 | balanced-high membership near-certain (P ≥ 0.85) | confirmed (1.000) |

From `probe_pivotality_bidirectionality.py` (1,200 wirings, 3,600 node observations).

## What it says

At the corners the gate is a hard conjunction. A node with maximal out-influence but zero in-influence —
read strongly by others, reading nothing itself — is in the core with probability exactly 0.000 across 33
such nodes. The mirror case, maximal reading and zero influence, is also 0.000 across 29 nodes. Neither
axis buys the other: a party cannot enter the coordination by influence alone, nor by reading alone. And a
node maximal on both axes is in the core with probability 1.000 across 28 nodes. Bidirectional coupling is
strictly necessary, and balanced strength is sufficient.

Across the interior the gate is not conjunctive. The third hypothesis predicted that membership would track
the minimum of the two influences — that a node is only as bound as its weaker side. It does not. The sum
of the two influences predicts membership slightly better than the minimum, rank-AUC 0.783 against 0.772,
so in the mid-range the two sides compensate: a node that reads strongly and influences moderately is bound
about as well as one balanced at the average. The strict conjunction holds only at the zero and maximum
extremes, and softens to an additive trade-off between them.

The membership gate is therefore a soft-AND. Each axis is independently necessary — zero on either side
excludes — and jointly sufficient at the top, but the boundary between excluded and included runs along the
sum rather than the minimum. Pivotality and reading are both required, and within the required region they
substitute for each other.

## What this adds to the law

Finding 8 and Q90 establish that bidirectional coupling is necessary and pivotality graded. Q98 separates
the two sides of bidirectionality and finds they are independently necessary at zero and compensatory above
it. The necessity is strict (the corners are 0.000 and 1.000, with no leakage), which strengthens the
coupling-necessary half of the law. The interior trade-off qualifies the graded half: the relevant
gradient is closer to the total constraint a party both gives and receives than to its weaker side alone.

## Caveats

- **Mixed result.** H1, H2, H4 confirmed; H3 refuted, with the sum and minimum close (0.783 vs 0.772).
- **Small corner cells.** The zero-reading and zero-influence corners rest on 33 and 29 observations; the
  0.000 rates are clean but the cells are small. n = 3 only.
- **Two scalar summaries.** In- and out-influence are mean Boolean sensitivities; a higher-order measure of
  reading or influence could change the interior trade-off, and is untested.
- **In-silico.** Boolean models, exact major complex.
