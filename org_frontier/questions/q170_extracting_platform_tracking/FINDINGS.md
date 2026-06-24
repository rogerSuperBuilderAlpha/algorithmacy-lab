# Q170 findings — the worker tracks an extractor worse, and worst where extraction equalizes

Both hypotheses hold. After equal probing the worker's recovered model fits a faithful mediator up to
the half-bit floor the hidden counterpart sets, fits an interested mediator worse, and fits it worst at
the exact k where the mediator's Shapley share falls to parity with the parties. Extraction and
unrecoverability are the same point on the ladder.

Approve agenda, probing budget 4000, counterpart hidden and uniform (synthetic data):

| k | mediator Shapley share | KL(true || recovered), bits | recoverable fraction |
|---|---|---|---|
| 0 (faithful) | 66.6% | 0.50 | 0.75 |
| 1 (value-equalization) | 33.4% | 1.00 | 0.50 |
| 2 | 0.0% | 0.50 | 0.75 |
| 3 | 0.0% | 0.00 | 1.00 |
| 4 (predatory) | 0.0% | 0.00 | 1.00 |

| H | Result |
|---|---|
| H1 (recovered-model KL higher for the interested mediator than the faithful one) | SUPPORTED -- faithful 0.50 bits, interested peaks at 1.00 bits |
| H2 (fidelity loss peaks at the Q131 value-equalization k) | CONFIRMED -- KL peak, steepest recoverable-fraction drop, and value-equalization all land at k = 1 |

## Reading

The faithful mediator (k = 0) already hides half a bit: the output is W AND C, and the worker who can set
only W and never see C recovers P(out | W) but not the C-dependence. That half-bit is the opacity floor
the predictive-processing battery names. The interested mediator at k = 1 imposes the approve agenda on
the one state where the parties least warrant it, which adds a second aliased state on top of the hidden
one, and the recovered W-marginal now misreads two of the four states rather than one. The KL doubles to
a full bit and the recoverable fraction halves to 0.50.

The alignment with extraction is the result. Q131 reads the same k = 1 as the value-equalization point:
there the mediator's Shapley share drops from two-thirds to a third, equal to each party. The level where
the agenda has extracted the mediator down to parity is the level where the worker's model of the rule is
least recoverable. Past it, at k >= 3, the mediator goes constant, its rule stops depending on W or C, and
the worker recovers it perfectly from W alone -- a model that tracks a platform which no longer reads her.

## Limitations

Exact Phi and a simulated probing loop on the three-node triad; the worker reads only W and never the
counterpart. The probing data are synthetic, so the empirical claim is about the construct under the
model, not a measured worker. Value read at the integrating state with Q111's all-ones background; the
Phi-to-money bridge is open (Q122). The deny agenda is not charted here because it collapses at k = 1; the
graceful approve ladder carries the comparison.
