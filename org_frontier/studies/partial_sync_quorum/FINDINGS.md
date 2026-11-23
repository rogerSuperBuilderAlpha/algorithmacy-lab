# The whole group binds only if the mediator acts first and with at least one party

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `c70dfeb5` before computation. Controls passed: 75 ordered partitions; the one-block schedule
equals the synchronous hub TPM (OR3 3.0, MAJ3 0, AND3 3.0); every one-at-a-time schedule equals
`update_order_quorum.order_tpm`.

## Setup

Mediator S over three parties (OR3, MAJ3, AND3; parties copy S), no noise. A schedule splits
{S, P1, P2, P3} into blocks that update in order; members of a block update together. All 75 ordered
partitions × 3 forms = 225 cases, ~23 s. Notation: `SP1|P2P3` = S and P1 together, then P2 and P3
together.

## Result

OR3 and AND3 give identical whole-Φ counts. Whole Φ > 0 in **13 of 75** schedules, exactly those whose
first block contains S and at least one party:

| first block | rest | schedules | whole Φ (OR3 and AND3) | full group in top tie set |
|---|---|---:|---:|---|
| S + all three parties (synchronous) | — | 1 | 3.0 | yes |
| S + two parties | the third party | 3 | 2.0 | yes (tied with smaller units at 2.0) |
| S + one party | the other two, together or in either order | 9 | 1.0 | no (top 2.0) |
| any other | | 62 | 0 | no |

MAJ3 has whole Φ 0 under all 75 schedules.

Top φ across the 75 OR3 schedules: 2.0 in 39, 6.0 in 22, 1.0 in 13, 3.0 in 1 (AND3 identical). With S
alone first, then all parties together (`S|P1P2P3`), the top unit is {P1,P2,P3} at 6.0; with all parties
first, then S (`P1P2P3|S`), it is {S} at 1.0. Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** OR3 is whole-system irreducible under 13 schedules, not only the synchronous one.
- **H2 REFUTED.** The same 13 for AND3.
- **H3 SUPPORTED.** MAJ3 whole Φ 0 under all 75.
- **H4 SUPPORTED.** Under `S|P1P2P3`, OR3's top unit is {P1,P2,P3} at φ 6.0.

Descriptive: the rule "S updates in the first block, together with at least one party" separates all
225 cases (it also covers MAJ3 trivially, since MAJ3 is 0 everywhere). Whole Φ falls with the number of
parties that act with S: 3.0, 2.0, 1.0 for three, two, one. We found the rule by reading the table; it
was not pre-registered.

## Limits

Deterministic three-party hubs, no noise; fixed schedules, not random ones; tie cutoff 1e-9.
