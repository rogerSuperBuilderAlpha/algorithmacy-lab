# q180 — Findings

Where the coder draws the party boundary moves the Phi verdict. Splitting a coded party flips the
dyadic/triadic reading for nearly half the synthetic cases. The rule_to_phi confidence interval
separates benign re-coding from load-bearing re-coding by a wide margin, but the separation falls
just short of the pre-registered 90 percent bar, so H2 as written is refuted.

## Census summary

| quantity | value |
|---|---|
| split cases (7 accounts x 3 parties x 2 modes) | 42 |
| verdict flips, all splits | 19 / 42 = 0.452 |
| flips, re-aggregable splits of triadic accounts | 4 / 15 = 0.267 |
| flips, function-changing splits of triadic accounts | 15 / 15 = 1.000 |
| CI crosses 0, function-changing splits | 13 / 15 = 0.867 |
| CI crosses 0, re-aggregable splits | 5 / 15 = 0.333 |

## Reading

A function-changing split clamps the party's output and drives whole-system Phi to 0. Every
triadic account flips to dyadic under it. A re-aggregable split preserves the party's joint
function and merges back to the base TPM exactly, yet it still flips the verdict in 4 of 15 cases.
Those flips are the or_triad family and one xor_triad case, where AND-aggregating two copies of an
OR or XOR hub changes which states the system can reach, and the lost reachability removes the
state that carried the integration. Individuation is not verdict-neutral even when it preserves the
party's function.

The confidence interval tracks this. For function-changing splits the panel Phi clusters near 0 and
the CI crosses 0 in 13 of 15 cases. For re-aggregable splits the CI stays above 0 in 10 of 15. The
two modes separate at 0.867 versus 0.333. Two function-changing cases keep enough residual Phi from
a node other than the clamped party that their CI stays above 0, which holds the function-changing
crossing rate to 0.867, below the 0.90 threshold fixed in H2.

## Verdicts

- H1 (splitting flips the verdict for more than 20 percent of accounts): SUPPORTED. The flip rate
  is 0.452, well past the 0.20 line and far past the 0.05 null.
- H2 (CI separates function-changing from re-aggregable splits, with function-changing crossing 0
  in more than 90 percent of cases): REFUTED on the strict threshold. The CI separates the modes
  strongly (0.867 versus 0.333 crossing 0, and 1.000 versus 0.267 flipping), but the
  function-changing crossing rate is 0.867, short of 0.90. The module distinguishes benign from
  load-bearing individuation in direction and degree; it does not clear the pre-registered bar.

## Scope

Results are on synthetic, coder-supplied accounts. No worker is measured. The finding is a property
of the split operator and the CI construct on this palette, not a measurement of any real
coordination.
