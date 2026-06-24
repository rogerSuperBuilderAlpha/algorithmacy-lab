# q150 — findings

A single chord across a conjunctive ring leaves the whole-system Φ flat but moves the cut and
redistributes the Shapley split toward the chord endpoints.

## Φ and the major complex

| form | structure | max Φ_MIP | MIP cut | major complex | core Φ |
|---|---|---|---|---|---|
| unchorded ring | triadic | 4.0000 | {ABC,DEF} | ABCDEF | 4.0000 |
| chord A-D | triadic | 4.0000 | {BC,ADEF} | ABCDEF | 4.0000 |

The chord does not change Φ (4.0 to 4.0) and does not change the major complex, which stays the
full six-node ring. The minimum-information cut moves: the unchorded ring splits into two halves
{ABC,DEF}, separating A from D; the chorded ring cuts off the two-node arc {BC} and keeps the chord
endpoints A and D together in {ADEF}. The cut now avoids running between the chorded nodes.

## Shapley split

| form | A | B | C | D | E | F | total |
|---|---|---|---|---|---|---|---|
| unchorded ring | 0.667 | 0.667 | 0.667 | 0.667 | 0.667 | 0.667 | 4.000 |
| chord A-D | 1.100 | 0.450 | 0.450 | 1.100 | 0.450 | 0.450 | 4.000 |

The unchorded ring splits its Φ evenly: every node holds 0.667. The chord lifts the two endpoints
to 1.100 each and drops the four far-arc nodes to 0.450 each. The endpoint pair rises from 1.334 to
2.200 and the far arc falls from 2.668 to 1.800, with the total held at 4.000.

## Verdicts

H1 chord raises ring Φ and shifts MIP cut off the chord: **REFUTED**. The cut does move off the
chord, but Φ is unchanged, so the conjunction fails. The chord shortens the integration cycle
without buying more whole-system Φ in this case.

H2 chord endpoints gain Shapley value at the expense of the far arc: **SUPPORTED**. One long-range
tie redistributes captured Φ toward its endpoints while leaving the total fixed.

## Scope

In-silico. Both forms are synthetic Boolean coordination models. The numbers describe an exact-Φ
read of a six-node ring under one chord. No real group is measured.
