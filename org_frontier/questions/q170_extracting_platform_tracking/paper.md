# q170 — Does the worker's generative model track an extracting platform?

## Question

The active-inference worker keeps a generative model of the system and probes her own input to reduce its
prediction error. The interested-mediator line gives the system an agenda, and the value-capture study
(Q131) shows that agenda extracts value up to the point where the mediator's value-share equalizes with
the parties. This study asks whether her probing recovers an interested mediator's rule as well as it
recovers a faithful one.

## Method

The worker sets W uniformly and observes the output, with the counterpart C hidden and uniform; after a
fixed budget she fits a recovered model P(out | W). The true rule is the Q126 mediator over the approve
ladder k = 0..4. Model-fidelity loss is the KL of the recovered model from the true rule, averaged over
the four (W, C) states, with the recoverable fraction as a second read. The value-equalization k is
computed from Q131's Shapley split. The probing loop and the fidelity measures are the shared bridge in
`org_frontier.cognition.predictive_processing`, seeded for determinism. Full method in
[`methods.md`](methods.md); hypotheses in [`hypotheses.md`](hypotheses.md).

## Results

| k | mediator share | KL(true ‖ recovered), bits | recoverable fraction |
|---|---|---|---|
| 0 (faithful) | 66.6% | 0.50 | 0.75 |
| 1 (value-equalization) | 33.4% | 1.00 | 0.50 |
| 2 | 0.0% | 0.50 | 0.75 |
| 3 | 0.0% | 0.00 | 1.00 |
| 4 | 0.0% | 0.00 | 1.00 |

The recovered model loses more of an interested mediator's rule than a faithful one (0.50 bits faithful,
1.00 bits at the peak), so H1 holds. The peak loss, the steepest drop in recoverable fraction, and the
value-equalization k all land at k = 1, so H2 holds. Raw output in
[`results/output.txt`](results/output.txt).

## Discussion

A faithful mediator already hides half a bit from the worker who can set only W: the output is W ∧ C and
the C-dependence stays outside a W-only model. The interested mediator at k = 1 aliases a second state on
top of that, doubling the loss to a full bit and halving the recoverable fraction. The level where this
happens is the level where the mediator's Shapley share has fallen from two-thirds to a third. The agenda
that extracts the mediator down to parity with the parties is the same agenda that makes its rule least
recoverable to the worker probing it.

Past the equalization point the mediator turns constant. Its rule stops reading W or C, and the worker
recovers it perfectly from her own input — a faithful model of a platform that no longer reads her. The
worst case for tracking is not the predatory extreme but the middle, where the agenda still mixes with the
joint determination and the worker cannot tell the two apart from her side of the channel.

## Limitations

Exact Φ and a simulated probing loop on the three-node triad; the worker reads only W. The probing data
are synthetic, so the empirical claim is about the construct under the model, not a measured worker. Value
read at the integrating state with Q111's all-ones background; the Φ-to-money bridge is open (Q122). The
deny agenda collapses at k = 1 and is not charted; the approve ladder carries the comparison.
