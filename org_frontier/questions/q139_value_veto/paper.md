# Q139 — Value and veto: Q112's decoupling is the integration

## Question

Q112 found a coordination's destruction democratic but its value concentrated: every party can collapse the
triad, yet the mediator takes two-thirds. Q139 asks whether that decoupling of equal destructive power from
unequal value is fixed, or moves as the mediator turns interested.

## Method

The Q126/Q127 interested mediator on the sparse AND baseline (self-interest destroys) and the balanced XOR
(self-interest re-integrates), approve agenda. At each interestedness level with positive Φ: the veto count
(parties whose knockout collapses the form), the mediator's Shapley value share, and the gap between that
share and 1/3, its equal share of the universal veto. Control: the faithful triad. Full method in
[`methods.md`](methods.md); hypotheses in [`hypotheses.md`](hypotheses.md).

## Results

| baseline | k | Φ | veto | mediator value | gap |
|---|---|---|---|---|---|
| AND | faithful | 2.0 | 3/3 | 67% | +1/3 |
| AND | interested | 0.5 | 3/3 | 33% | 0 |
| XOR | faithful | 0.5 | 3/3 | 33% | 0 |
| XOR | interested | 2.0 | 3/3 | 67% | +1/3 |

Veto is universal at every level. The value-veto gap is +1/3 wherever Φ = 2.0 and 0 wherever Φ = 0.5,
independent of baseline or interestedness — it tracks the integration, not the agenda. Raw output in
[`results/output.txt`](results/output.txt).

## Discussion

The decoupling Q112 read as a feature of platform power is the form's integration measured a second way. The
mediator's value above its equal veto share is exactly the gap between a fully integrated coordination, where
the bottleneck commands two-thirds, and a weakly integrated one, where the value splits evenly. The veto — the
parties' equal power to dissolve the coordination — does not move; only the value does, and it moves with Φ.
Interest is the lever: self-interest that loosens a sharp mediation democratizes the value to match the veto,
and self-interest that sharpens a loose one re-concentrates it. The political-economy reading is that the
parties' structural leverage is constant and their share is not: what they are paid for the veto they all hold
is the integration the mediator's faithful commitment creates, and an interested mediator changes that pay by
changing the integration, in whichever direction its agenda moves the form.

## Limitations

Exact Φ on the three-node triad, two baselines, approve agenda (deny mirrors by Q133). Veto is binary; the
integration window is narrow (Φ ∈ {2.0, 0.5}). Value at the integrating state; the Φ-to-economic-value bridge
is open (Q122).
