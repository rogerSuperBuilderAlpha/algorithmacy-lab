# Q90 findings — the membership law generalizes in kind, at moderate strength

Three hypotheses confirmed, one refuted. The core-membership law holds past the three-node family in its
essential structure: bidirectional coupling stays strictly necessary at every size, and pivotality keeps
predicting membership through a monotone gradient that neither sharpens nor collapses as parties multiply.
The predictor's strength is moderate in the full family, below the pre-registered bar.

| n | node-obs | bidirectional | non-bidir in-core | rank-AUC | P(core) low→high influence |
|---|---|---|---|---|---|
| 3 | 900 | 712 | 0.000 | 0.714 | 0.54 → 0.74 |
| 4 | 600 | 599 | 0.000 | 0.621 | 0.44 → 0.67 |
| 5 | 75 | 75 | 0.000 | 0.733 | 0.35 → 0.67 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | coupling necessary at every n (non-bidir in-core < 0.05) | confirmed (0.000 at every n) |
| H2 | pivotality predicts membership at every n (AUC ≥ 0.75) | refuted (0.62–0.73) |
| H3 | P(core) rises with influence at n = 4 | confirmed (0.44 → 0.67) |
| H4 | no sharp degradation n = 3 → n = 4 (AUC drop ≤ 0.15) | confirmed (0.714 → 0.621) |

From `probe_membership_law_scaling.py`. n = 6 was not sampled; one major-complex computation there is
about nine minutes.

## What it says

The stronger half of the law generalizes cleanly. Across n = 3, 4, and 5, no non-bidirectional node ever
enters the major complex: the non-bidirectional in-core rate is exactly 0.000 at all three sizes, over
1,575 node observations. Bidirectional constraining coupling is necessary at every size tested, without
exception.

The pivotality half generalizes in kind. The probability of membership rises with out-influence at every
size (0.54 to 0.74 at n = 3, 0.44 to 0.67 at n = 4, 0.35 to 0.67 at n = 5), so the monotone gradient that
the law rests on persists as parties multiply (H3). And it does not collapse with size: the rank-AUC at
n = 4 is within 0.10 of n = 3, and n = 5 is no lower than n = 3 (H4). More parties do not break the law.

The pivotality predictor is only moderately strong in this family, and H2 fails. The pre-registered bar of
0.75 was set from the headline rank-AUC of 0.89, but that figure was measured on the strict-mediation
family, where the mediator reads two outer parties and the structure is constrained. Q90 samples the full
family, where every node reads every other through an arbitrary function — a noisier, less structured
population — and there even the n = 3 rank-AUC is 0.714, below the bar. The predictor stays in the 0.62 to
0.73 band across sizes. The honest reading is that out-influence predicts membership well above chance at
every size, and the law's qualitative structure holds, but the single-number pivotality predictor is
weaker on the full family than the strict-mediation headline implies, and the size trend is flat rather
than degrading.

## What this means with Q81

Q81 showed a learned surrogate for the *verdict* does not generalize past the size it trains on. Q90 shows
the structural *membership law* does generalize in kind, with coupling-necessary exact and the pivotality
gradient intact at n = 3, 4, 5. The two are consistent: a cheap statistical predictor of the verdict
breaks across sizes, while the structural law that the exact computation reveals holds. The structural
account travels where the cheap one does not.

## Caveats

- **Mixed result.** H1, H3, H4 confirmed; H2 refuted, on a bar calibrated from the strict-mediation family
  rather than the full family this study samples.
- **Small n = 5 sample.** Fifteen wirings, 75 node observations, because each major complex is ~27s at
  n = 5. The n = 5 rank-AUC (0.733) is indicative, not tight.
- **n = 6 untested.** Beyond the exact ceiling for major-complex enumeration (~9 min per wiring).
- **In-silico.** Boolean models, exact major complex. Out-influence is one scalar summary of pivotality;
  a higher-order measure could predict membership better and is untested.
