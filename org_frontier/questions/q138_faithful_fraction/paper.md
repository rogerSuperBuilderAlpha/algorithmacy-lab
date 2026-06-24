# Q138 — The minimum faithful fraction: reviving the coordination, and who pays for it

## Question

A predatory mediator kills the coordination; a regulator can force it to commit the parties' joint
determination on some of its states. Q138 asks how much forced faithfulness revives the coordination, and how
the revived value is distributed.

## Method

The triad W, S, C. The mediator defaults to the predatory constant (always approve); the regulator forces m
of its four input states back to the faithful AND commit, highest-warrant first. For each m the verdict Φ and
the Shapley split at the integrating state. Control: fully faithful (m = 4), reproducing Q111. Full method in
[`methods.md`](methods.md); hypotheses in [`hypotheses.md`](hypotheses.md).

## Results

| faithful states | Φ | mediator share | parties (collective) |
|---|---|---|---|
| 0–2 of 4 | 0.000 | — | — |
| 3 of 4 | 0.500 | 33% | 67% |
| 4 of 4 | 2.000 | 67% | 33% |

The coordination revives only at three-quarters faithfulness, and revives there with an even split — each of
the three parties a third — so the human parties hold two-thirds. The mediator's two-thirds returns only at
full faithfulness, when Φ jumps to 2.0. Raw output in [`results/output.txt`](results/output.txt).

## Discussion

The platform's rent is the fully-faithful commit, not faithfulness as such. Regulation faces a sharp
threshold — below three-quarters committed, there is no coordination and no value — and a distributional twist
above it: the minimum that revives the coordination leaves the parties with the majority of the value, and
only the last increment of faithfulness, completing the commit, hands the mediator the dominant share. The
naive reading, that a faithful platform is a constrained one giving up its rent, is inverted: the most
faithful mediator is the most richly rewarded, and the partially-regulated one that merely keeps the
coordination alive takes the least. A regulator that wanted both a live coordination and a fair split would
stop at the threshold, not push to full faithfulness, because the final increment is what concentrates the
value at the platform.

## Limitations

Exact Φ on the three-node triad with the AND commit and a constant predatory default; the threshold and the
split at it depend on the forcing order and the baseline. The even split at three-quarters is the Q131
equalization of a weakly-integrated (Φ = 0.5) form. Value read at the integrating state; the
Φ-to-economic-value bridge is open (Q122).
