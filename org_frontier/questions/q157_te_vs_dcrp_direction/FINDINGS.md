# q157 — findings

Pairwise transfer entropy recovers the true orientation of a directed read edge far more often
than the DCRP peak-lag sign. The two methods share much of their failure, yet enough of their
errors are complementary that combining them recovers edges neither reads alone.

## The numbers

Pooled over both ensembles: 1016 directed read edges from 302 forms with at least one edge.

| method | recovery |
|---|---|
| DCRP peak-lag sign | 56.5% |
| transfer entropy | 77.2% |
| OR-combine (either correct) | 84.6% |

Per ensemble:

| ensemble | edges | DCRP | TE |
|---|---|---|---|
| rand_form3 | 440 | 58.4% | 80.7% |
| rand_form4 | 576 | 55.0% | 74.5% |

Agreement contingency (per directed edge, pooled):

| cell | count |
|---|---|
| both correct | 498 |
| DCRP only correct | 76 |
| TE only correct | 286 |
| both wrong | 156 |
| phi(DCRP hit, TE hit) | +0.2605 |

## Reading

Transfer entropy beats the DCRP sign by 20.7 percentage points pooled, and by a double-digit
margin in each ensemble separately. The gap is largest at 3 nodes (80.7% against 58.4%) and holds
at 4 nodes (74.5% against 55.0%). On these binary series the recurrence profile sits near its 0.5
floor, so a one-step read lag is a weak signal; the conditional-information estimator separates
lead from follow more sharply.

The errors do share structure. The phi coefficient of the two hit vectors is +0.26, so an edge one
method misses the other is more likely to miss too. The 156 both-wrong edges are the common-failure
core. The off-diagonal cells stay large: 286 edges TE reads and DCRP misses, against 76 the DCRP
sign reads and TE misses. The OR-combine reaches 84.6%, a 7.5-point lift over transfer entropy
alone. The two methods fail on overlapping but not identical edge sets, so combining them helps.

## Verdicts

H1 (TE beats DCRP peak-lag by more than 5 pp): SUPPORTED. TE 77.2% minus DCRP 56.5% is +20.7 pp,
far past the 5-point threshold.

H2 (errors correlated, not complementary; combining would not help): REFUTED. The phi coefficient
is positive (+0.26), so the errors do correlate, but the OR-combine lifts recovery by 7.5 points,
well past the 1-point ceiling the hypothesis set. The errors are partly shared and partly
complementary, so combining the methods raises recovery rather than leaving it flat.

## Scope

In-silico. The forms are synthetic Boolean coordination models and the ground-truth wiring comes
from the exact connectivity matrix the IIT-4.0 machinery uses. The recovery rates describe these
two random ensembles and these two estimators. A different ensemble, a longer trajectory, or a
graded transfer-entropy estimator could shift the margins. The validation gap to coded field
series is open: no organizational time series has been read this way.
