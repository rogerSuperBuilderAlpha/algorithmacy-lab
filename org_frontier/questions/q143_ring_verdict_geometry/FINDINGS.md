# q143 — findings

The conjunctive ring reads triadic at every size from n=3 to n=7. The core is the full node set
throughout. The MIP geometry has two regimes: at n=3 the minimal partition is the complete
three-way split with Φ=6.0, and from n=4 onward it is a balanced two-arc cut with Φ=4.0, constant.

| n | structure | max_phi | MIP cut | core | core = full |
|---|-----------|---------|----------------------------|------|-------------|
| 3 | triadic   | 6.0     | 3 parts: {x0,x1,x2}        | full | yes |
| 4 | triadic   | 4.0     | 2 parts: {x0x1,x2x3}       | full | yes |
| 5 | triadic   | 4.0     | 2 parts: {x0x1,x2x3x4}     | full | yes |
| 6 | triadic   | 4.0     | 2 parts: {x0x1x2,x3x4x5}   | full | yes |
| 7 | triadic   | 4.0     | 2 parts: {x0x1x2,x3x4x5x6} | full | yes |

Anchors: the faithful triad control reads triadic at Φ=2.0 (PASS). chain(5) is triadic at Φ=2.0
with a core of two nodes, a serial form that sheds the rest. pool(5) carries Φ=20.0 over a full
five-node core.

## Verdicts

- H1 REFUTED. The triadic-with-Φ>0 clause holds at every n, and the two-arc cut with constant Φ
  holds from n=4 onward. The clause fails at n=3: the minimal partition there is the complete
  three-way split, not a two-arc cut, and its Φ is 6.0 against the 4.0 of the larger rings. The
  rotational-bottleneck intuition is right for n>=4 and breaks for the smallest ring, where cutting
  into two arcs and cutting into three single nodes are both available and the three-way split wins.
- H2 SUPPORTED. The major complex is the full node set at every n=3..7. No node drops, unlike the
  m-hub.

## Scope

Synthetic Boolean forms; exact IIT-4.0 Φ. No real coordination is measured.
