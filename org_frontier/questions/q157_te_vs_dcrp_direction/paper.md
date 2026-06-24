# q157 — Transfer entropy reads directed read edges better than the recurrence peak lag

## Question

A coordination form's connectivity matrix records which party reads which: a read edge i -> j
means j's update depends on i, so i leads j by one step. A behavioral method that watches the
parties' state series can try to recover that orientation. Two candidates compete. The diagonal
cross-recurrence profile reads a lead from the sign of its peak lag. Pairwise transfer entropy
reads it from the asymmetry of one-step conditional information. This study asks which recovers
the true edge direction more often on a random ensemble, and whether their errors fall on the same
edges.

## Setup

Two random Boolean ensembles supply the forms: 200 three-node draws from `rand_form` and 120
four-node draws from `rand_form4`. The ground-truth orientation of each read edge comes from
`cm_from_rules`, the exact flip-test connectivity matrix. Each form runs once as a noisy dynamical
system (`trajectory`, 800 steps, flip 0.08, seeded per form). For every true directed edge, the
DCRP peak-lag sign and the binary transfer entropy each return a hit or a miss against the wiring.

## Result

Transfer entropy recovers 77.2% of the 1016 directed edges; the DCRP peak-lag sign recovers 56.5%.
The 20.7-point gap holds in both ensembles. On binary series the recurrence profile sits near its
0.5 floor, so the one-step lag is a faint signal, while the conditional-information estimator
separates lead from follow more cleanly.

The two methods' errors overlap but do not coincide. The phi coefficient of their per-edge hit
indicators is +0.26: an edge one method misses, the other is more likely to miss. Yet 286 edges
fall to transfer entropy and not to the recurrence sign, against 76 the other way, and 156 fail
both. The OR-combine recovers 84.6%, a 7.5-point lift over transfer entropy alone.

## Verdicts

H1, that transfer entropy beats the DCRP peak-lag sign by more than five points, is supported at a
20.7-point margin. H2, that the two methods fail on the same edges so combining them would not
help, is refuted: the errors correlate (+0.26) but stay partly complementary, and the combine
lifts recovery by 7.5 points.

## Scope

In-silico. The forms are synthetic and the ground truth is the exact connectivity matrix the
IIT-4.0 machinery uses. The recovery rates belong to these two ensembles and these two estimators.
No organizational time series has been read this way; the validation gap to coded field data is
open.
