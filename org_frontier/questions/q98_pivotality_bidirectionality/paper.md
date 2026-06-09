# Q98 — Reading and influence: a hard gate at the corners, a soft one inside

## Question

Finding 8 ties core membership to bidirectional coupling and pivotality, held together. A node's
bidirectionality has two sides — how much it reads, the dependence of its own update on others, and how
much it is read, the dependence of others on it. Whether these are independently necessary, or whether a
large value on one compensates a small value on the other, is unmapped. The question decides whether a
party can enter the coordination by influence alone, or must genuinely both read and be read.

## Method

The full three-node family (each node reads the other two through an arbitrary Boolean function), reusing
Q90's sampler. For each node, in-influence is the mean Boolean sensitivity of its own update to its inputs,
and out-influence is the mean sensitivity of the other nodes to it. Membership is whether the node is in
the major complex. Over 1,200 wirings (3,600 node observations), membership probability is read in three
cells (strong influence with zero reading, strong reading with zero influence, strong on both), and the
minimum and the sum of the two influences are compared as predictors of membership.

## Results

The corners are a hard conjunction. A node maximal in out-influence and zero in in-influence is in the
core with probability 0.000 across 33 nodes; the mirror case is 0.000 across 29; a node maximal on both is
in the core with probability 1.000 across 28. Neither axis compensates the other at the extremes, and
balanced strength guarantees membership.

The interior is not conjunctive. The sum of the two influences predicts membership at rank-AUC 0.783,
slightly above the minimum's 0.772, so in the mid-range the two sides trade off rather than the weaker one
governing.

| condition | P(in core) | n |
|---|---|---|
| strong influence, zero reading | 0.000 | 33 |
| strong reading, zero influence | 0.000 | 29 |
| strong on both | 1.000 | 28 |
| min(read, influence) → core | rank-AUC 0.772 | 3600 |
| sum(read, influence) → core | rank-AUC 0.783 | 3600 |

| | result |
|---|---|
| H1 strong influence cannot compensate zero reading | confirmed (0.000) |
| H2 strong reading cannot compensate zero influence | confirmed (0.000) |
| H3 membership tracks the minimum, not the sum | refuted |
| H4 balanced-high membership near-certain | confirmed (1.000) |

## Interpretation

The membership gate is a soft-AND. Each side of bidirectionality is independently necessary: zero reading
or zero influence excludes the node with no leakage, the corners sitting exactly at 0.000. Balanced
strength is sufficient, the both-maximal corner sitting exactly at 1.000. Between these extremes the gate
relaxes, and the boundary between excluded and included follows the total constraint a node both gives and
receives rather than its weaker side. A node that reads strongly and influences moderately is about as
bound as one balanced at the average.

This sharpens the membership law in two directions at once. The coupling-necessary half is strengthened:
the two sides of bidirectionality are each independently necessary, so a party cannot buy its way
into the coordination by influence while reading nothing, nor by reading while influencing nothing. The
graded half is qualified: pivotality is better read as the sum of a party's reading and influence than as
the weaker of the two, so within the bidirectional region the two sides substitute for each other.

For the security reading that Q84 and Q97 pursue, the strict corners matter. An agent positioned to
influence the coordination without being constrained by it (high out-influence, zero in-influence) does
not enter the core, at probability exactly zero. Influence without reception is not membership.

## Limitations

In-silico; Boolean models with the exact major complex. The corner cells rest on 28 to 33 observations, so
the 0.000 and 1.000 rates are clean but small, and the family is n = 3 only. In- and out-influence are mean
Boolean sensitivities; a higher-order measure could shift the interior trade-off and is untested. The sum
and minimum are close (0.783 against 0.772), so the interior result is a slight lean.
