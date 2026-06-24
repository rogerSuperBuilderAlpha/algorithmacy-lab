# q156 — findings

Interested and faithful mediators that share a wiring graph and a full {W, S, C} Φ-core do not
separate on outgoing-edge DCRP prominence. Structure already cannot tell them apart, and the
behavioral signature tested here cannot either.

## The numbers

Matched pools on the wiring graph W'=S, C'=S, S'=f(W,S,C): 27 faithful (symmetric rule), 18
interested (asymmetric rule). Every form reads all three inputs and has the full {W, S, C} core.

| measure | faithful | interested |
|---|---|---|
| outgoing DCRP prominence (mean over 16 seeds) | 0.3303 | 0.3041 |
| prominence sd | 0.1113 | 0.0975 |
| major-complex core | {W, S, C} | {W, S, C} |

| H1 test | value |
|---|---|
| matched pairs interested < faithful | 278/486 = 0.5720 |
| separation threshold | 0.70 |
| one-sided Mann-Whitney (interested < faithful) | U=208.0, p=0.2121 |

## Reading

Interested mediators do trend lower in mean outgoing prominence (0.3041 against 0.3303), the
direction H1 predicted, but the effect is weak. Only 57.2% of matched pairs separate, short of the
0.70 bar, and the Mann-Whitney test does not clear alpha = 0.05 (p=0.21). The outgoing-edge
prominence does not distinguish the two pools.

Both pools carry the identical {W, S, C} core by construction and by check, so major-complex
membership does not distinguish them. Phi-membership alone misses interestedness here. The hope was
that behavior would recover what structure misses; on this measure it does not.

## Verdicts

- H1: REFUTED. Matched-pair separation is 0.5720 and the Mann-Whitney test is not significant, so
  outgoing prominence is statistically indistinguishable between the pools.
- H2: CONFIRMED. The two pools share the {W, S, C} core, so structural membership does not
  separate them. Interestedness leaves no trace in Phi-membership. The behavioral arm does not
  recover it either, so on this study interestedness is invisible to both readings.
