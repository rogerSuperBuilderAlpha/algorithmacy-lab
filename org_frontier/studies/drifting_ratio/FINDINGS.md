# The fitted drifting-ratio formula is refuted: measured ratios are 147.065, 76.276 and 41.484 against predicted 199.902, 102.765 and 54.049

The fitted formula for the drifting ratio is refuted. On (1,1,1,3) quota 3 the measured ratios are 147.06517413692788, 76.2763609973792 and 41.48368774874131 at e = 0.05, 0.1 and 0.2, against predicted 199.9024781081887, 102.76545826383659 and 54.04909345311601 (relative errors 0.264, 0.258 and 0.232). The top tie set is {S, P4} at every rate, and quota 4 matches quota 3.

Hypotheses were committed (`8a4b2223`) before computing. The six singleton-winning ratios used to fit the coefficients, and the (1,1,1,2) quota 3 series used only to classify the two families, were taken from `weighted_ratio_law` and `weighted_equivalence` and disclosed in `hypotheses.md`. The harness control recomputed (1,1,2,3) quota 3 at e = 0.1 and recovered the published ratio 49.999952735680445.

## Scores

- **H1 REFUTED.** The formula missed at all three rates, by about a quarter: relative errors 0.26431540254676017, 0.2577626540471427 and 0.23248134060332298. Each prediction was high. The pre-registered match threshold was 1e-3.
- **H2 SUPPORTED.** At every rate the top tie set for (1,1,1,3) quota 3 is exactly {S, P4}.
- **H3 SUPPORTED.** (1,1,1,3) quota 4 gives the same whole Φ, top φ and ratio as quota 3 at every rate (relative error ≤ 6.6e-15). The top state is all-0 at quota 3 and all-1 at quota 4; the tie set is {S, P4} either way.

## Exact numbers

"pred" is the pre-registered formula at R = 7. "rel" is |measured − pred| / pred.

| form | q | e | whole Φ | top φ | ratio | predicted | rel | result |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| (1,1,1,3) | 3 | 0.05 | 0.005980950217204375 | 0.879589485197458 | 147.06517413692788 | 199.9024781081887 | 0.264 | miss |
| (1,1,1,3) | 3 | 0.1 | 0.009995678985128199 | 0.7624340186835554 | 76.2763609973792 | 102.76545826383659 | 0.258 | miss |
| (1,1,1,3) | 3 | 0.2 | 0.012971794290726172 | 0.5381178638973898 | 41.48368774874131 | 54.04909345311601 | 0.232 | miss |
| (1,1,1,3) | 4 | 0.05 | 0.005980950217204338 | 0.8795894851974585 | 147.06517413692885 | 199.9024781081887 | 0.264 | (complement) |
| (1,1,1,3) | 4 | 0.1 | 0.009995678985128199 | 0.7624340186835556 | 76.27636099737921 | 102.76545826383659 | 0.258 | (complement) |
| (1,1,1,3) | 4 | 0.2 | 0.012971794290726176 | 0.5381178638973895 | 41.483687748741275 | 54.04909345311601 | 0.232 | (complement) |

Generalized R is 7 for both quotas, as pre-registered. Whole Φ at e = 0.2 equals the Φ(0.2, 0) value measured for this rule in `majority_factor_split` (0.012971794290726172), a consistency check across the two noise constructions when party-side noise is zero.

## What it means

A three-parameter formula fitted to two published singleton-winning rules, (1,1,1,2) quota 2 (R = 4) and (1,1,2,3) quota 3 (R = 5), does not predict the drifting ratio on a third such rule, (1,1,1,3) quota 3 (R = 7). The classification still holds: the new rule is in the falling-ratio family, the unique strongest part is the coordinator with the heavy party, and complement quotas agree. The fitted curve in e and R is not a general rule.

## Limits

One run; the stated rules and rates only; independent input noise (probe 464), parties copy S. The formula was a least-squares fit, not a derived identity. A post-hoc observation, not a claimed law: the new ratios are close to 2.5 times the published (1,1,1,2) quota 2 ratios (relative differences 0.0085, 0.0013 and 0.00027). That scale does not describe the published R = 4 to R = 5 step, so it is recorded only as a prompt for a later test.

## Reproduce

```sh
python org_frontier/studies/drifting_ratio/run.py --quick   # CI subset, ~40 s
python org_frontier/studies/drifting_ratio/run.py --write   # full run, ~30 s on 8 cores
```
