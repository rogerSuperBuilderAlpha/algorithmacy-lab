# Findings: negative_phi_survey

Hypotheses were committed (3e34ab73) before computing. Values seen beforehand: the OR3/ANY4 all-zero
full-group values from `high_noise_tie_onset` (η 0.31–0.39) and the published numbers of the source studies.

## Scores

- **H1 REFUTED.** Negative φ already appears at η = 0.3: OR3/AND3 have 6 negative values (the three
  {S,Pi} pairs at 2 states, each −0.131783); ANY4/ALL4 have 20 (min −0.157747). None of these are the full
  group (the full group first goes negative between 0.3 and 0.4, as `high_noise_tie_onset` located).
- **H2 SUPPORTED.** For all 56 panel-A cases, whole Φ, top φ and tie-set size match `tie_set_membership`
  exactly when negatives are kept. No negative value enters any tie set; every case with published whole
  Φ > 0 has positive max full-group φ.
- **H3 SUPPORTED.** For (1,2,2,2) quotas 2 and 4 at all three rates, the full group's raw φ is 0 within
  1e-9 at every reachable state. The published whole Φ = 0 is not a floored negative.

## Where the negatives are

| forms | η with negatives | count per case | min φ |
|---|---|---|---|
| OR3, AND3 | 0.3, 0.4, 0.45 | 6, 14, 14 | −0.131783 (0.3) |
| ANY4, ALL4 | 0.3, 0.4, 0.45 | 20, 30, 30 | −0.157747 (0.3) |
| 2of4, 3of4 | 0.45 | 28 | −0.082206 |
| MAJ3 | none | 0 | — |

Total: 284 of 4,676 values. Every negative sits at one of two states per case: the parties all 0 (S = 0 or 1)
for OR3, ANY4 and 2of4, and the parties all 1 for AND3, ALL4 and 3of4. Each dual pair (OR3/AND3, ANY4/ALL4,
2of4/3of4) has identical counts and values at bit-flipped states.

## What this means

Negative φ is outside what IIT 4.0 defines. We report it as PyPhi's output and do not interpret it. For these
panels the `max(0, ·)` floor in earlier studies did not change any reported number, but it did hide that
the low-quorum unanimous state stops contributing at high noise, which is the mechanism behind the
`high_noise_tie_onset` cliff.
