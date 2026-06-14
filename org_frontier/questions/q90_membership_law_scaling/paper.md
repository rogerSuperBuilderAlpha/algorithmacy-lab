# Q90 — Does the core-membership law generalize past three nodes?

## Question

The lab's account of which parties join the irreducible core rests on two conditions: bidirectional
coupling is necessary, and among coupled parties the probability of major-complex membership rises with
pivotality. The account reached rank-AUC 0.89 on the three-node family. It was established on the smallest
systems. Whether it holds as systems grow is the question Q81 left open for the structural law, after
showing a learned surrogate for the verdict fails to cross sizes.

## Method

The full n-node family: each node reads all n−1 others through an arbitrary Boolean function, so a wiring
is n truth tables. This is probe #12's three-node construction lifted to larger n. For each sampled wiring
and each node, two quantities are computed — whether the node is bidirectionally coupled, and its
out-influence, the mean Boolean sensitivity of the other nodes to it — together with whether the node is
in the exact major complex. Sample sizes fall with n because the major complex is expensive: 300 wirings
at n = 3, 150 at n = 4, 15 at n = 5. n = 6 is out of reach at about nine minutes per wiring.

## Results

Coupling is necessary at every size. Across all three sizes and 1,575 node observations, the
non-bidirectional in-core rate is exactly 0.000: a node that does not both read and influence the
coordination never enters the major complex.

The pivotality gradient persists. The probability of membership rises with out-influence at every size,
from 0.54 to 0.74 at n = 3, 0.44 to 0.67 at n = 4, and 0.35 to 0.67 at n = 5. The rank-AUC of out-influence
predicting membership stays in a 0.62 to 0.73 band, with n = 4 within 0.10 of n = 3 and n = 5 no lower than
n = 3. The law does not collapse or sharpen with size; it stays flat.

| n | non-bidir in-core | rank-AUC | P(core) low → high influence |
|---|---|---|---|
| 3 | 0.000 | 0.714 | 0.54 → 0.74 |
| 4 | 0.000 | 0.621 | 0.44 → 0.67 |
| 5 | 0.000 | 0.733 | 0.35 → 0.67 |

| | result |
|---|---|
| H1 coupling necessary at every n | confirmed (0.000) |
| H2 pivotality predicts membership at AUC ≥ 0.75 | refuted (0.62–0.73) |
| H3 gradient persists at n = 4 | confirmed |
| H4 no sharp degradation n = 3 → n = 4 | confirmed |

## Interpretation

The membership law generalizes in kind. Its necessary condition is exact at every size, and its graded
condition keeps the same monotone shape from n = 3 to n = 5 without weakening as parties multiply. The
structural account is not a three-node artifact.

The pivotality predictor is moderately strong on the full family, and weaker than the headline figure. The
0.89 rank-AUC was measured on the strict-mediation family, where the mediator reads two outer parties and
the structure is constrained; the full family, where every node reads every other through an arbitrary
function, is a noisier population, and the n = 3 rank-AUC there is already 0.714. The pre-registered bar of
0.75 was set from the wrong baseline, and H2 fails for that reason rather than because the law degrades
with size, which H4 rules out. Out-influence predicts membership well above chance at every size; it is one
scalar summary, and a richer pivotality measure could sharpen it.

Set beside Q81, the result draws a clean line. A cheap statistical surrogate for the verdict does not
survive a change of size; the structural law that the exact computation reveals does. The account of which
parties are bound into the coordination travels across sizes where a learned shortcut does not.

## Limitations

In-silico; Boolean models with the exact major complex. The n = 5 sample is small (15 wirings, 75 node
observations) because of cost, so its rank-AUC is indicative. n = 6 is untested, beyond the exact ceiling
for major-complex enumeration. Out-influence is a single scalar; the moderate rank-AUC may reflect the
predictor rather than the law, and a higher-order pivotality measure is untested.
