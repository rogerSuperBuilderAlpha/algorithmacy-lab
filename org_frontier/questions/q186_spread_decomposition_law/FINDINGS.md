# q186 — Findings

The three spread components carry separate information across the synthetic census. They do not
collapse onto one axis.

## Census summary

| quantity | value |
|---|---|
| account pairs | 43 (28 at n=3, 15 at n=4) |
| Spearman rho: verdict_disagree vs phi_gap | +0.2302 |
| Spearman rho: verdict_disagree vs core_div | +0.5122 |
| Spearman rho: phi_gap vs core_div | -0.0946 |
| agree-but-gapped pairs | 14 |
| disagree-but-same-core pairs | 1 |
| any off-diagonal pair | 15 / 43 = 0.3488 |

All three rank correlations sit well below 1, and one is slightly negative. A rank-one census would
force every pair onto a single monotone ordering with all correlations at +1. The census does not.

Two off-diagonal patterns are populated. A pair can agree on verdict yet differ in Phi: the faithful
triad and the XOR triad both read 'triadic', share an identical core, and still post a phi_gap of
1.5. A pair can disagree on verdict yet share an identical core: a two-node dyad and a triadic-reading
account both place exactly {A, B} in the major complex, so core_jaccard = 1.0 while
verdict_agreement = 0 and phi_gap = 0.415.

## Verdicts

- H1 (three components not rank-one collinear): SUPPORTED. Both off-diagonal cells are non-empty
  (14 and 1) and every Spearman rho is below 1.
- H2 (off-diagonal fraction exceeds 10 percent): CONFIRMED. 34.88 percent of the census shows at
  least one off-diagonal pattern, far above the < 1 percent noise floor.

## Scope
Results are on synthetic, coder-supplied accounts. No worker is measured. The finding is a property
of the spread construct on this census, not a measurement of any real coordination.
