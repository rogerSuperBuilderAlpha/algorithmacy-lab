# q167 — Capture meets the agenda: interest does not lower the worker's displacement threshold

## Question

battery_extended_mind models extended-mind capture with a four-node core. The parties and the platform
read the system (W' = S, C' = S, P' = S), and the system commits a g-weighted mix of the worker's joint
determination and the platform's, S = (1 − g)·(W ∧ C) + g·platform(P, C). With a faithful platform branch
P ∧ C the platform input supplants the worker as g rises, and the worker leaves the major complex at a low
capture threshold g*. q167 makes the platform interested: its branch becomes Q126's mediator(agenda, k)
over the platform's own inputs (P, C), imposing a preferred output on the states those inputs least
warrant. The question is whether an interested platform displaces the worker at a lower g than a faithful
one.

## Method

The grid sweeps g ∈ {0.00, …, 0.50} for the faithful control and for the interested platform at approve
(a = 1) k = 1..4 and deny (a = 0) k = 1. For each setting the reading is the maximal complex of the
16-state TPM (battery_extended_mind's exact reader, max over states): g* is the first g > 0 at which W
leaves the core, and the post-displacement core is the core at g*. Full method in [`methods.md`](methods.md);
hypotheses fixed before computing in [`hypotheses.md`](hypotheses.md).

## Results

Both hypotheses are refuted.

| setting | g* (W exits) | post-core | core at g = 0.00 → 0.25 → 0.50 |
|---|---|---|---|
| faithful | 0.05 | SC | WSC → SC → SC |
| approve k=1 | 0.40 | SC | WSC → WSC → SCP |
| approve k=2 | 0.05 | SC | WSC → SC → SC |
| approve k=3 | none | — | WSC → WSC → WSC |
| approve k=4 | none | — | WSC → WSC → WSC |
| deny k=1 | none | — | WSC → WSC → WSC |

g* is non-monotone in interest. The faithful branch captures at g* = 0.05; raising interest does not push
the threshold lower. Approve k = 2 matches the faithful threshold because its branch still reads both P and
C. Approve k = 1 raises g* to 0.40. The constant-agenda settings (approve k = 3, k = 4, deny k = 1) keep
the worker across the whole grid, because a constant platform branch carries no information to compete with
the worker's term. Where the worker is displaced she lands on the core SC, the same as under the faithful
platform; the agenda node P enters the core only for approve k = 1 and only at g = 0.50, past the
threshold. Raw output in [`results/output.txt`](results/output.txt).

## Interpretation

A faithful platform branch P ∧ C reads both the platform input and the counterpart, so a small capture
share outweighs the worker's term and takes her seat. An agenda displaces the worker only where its branch
stays informative about (P, C): approve k = 2 reads NOT-P-or-C and captures at the same low threshold,
approve k = 1 reads P-equals-C and needs a larger share, and the constant agendas carry no information so
the worker's W ∧ C term governs and she keeps her seat. The replacement, when it happens, is the
counterpart C, the input the platform still reads, not the agenda's invariant value. Interest is a second
axis from capture. It changes who the worker is replaced by and whether she is replaced at all, and it does
not collapse into one lower threshold. The compounding the hypothesis expected does not hold in this model;
informativeness of the platform branch, not the strength of the agenda, sets the threshold.

## Limitations

Exact Φ on a four-node Boolean model; evidence about the construct and the instrument, not a claim about a
real platform. "Capture", "agenda", "approve", "deny" label a mixing weight and committed output values,
not measured intent. The empirical arm of this line runs on synthetic data. The faithful baseline branch is
AND and the platform mixes linearly with it; an OR baseline or a different mixing rule would relabel which
(P, C) states each agenda overrides and is the natural robustness extension. The deny agenda is degenerate
past k = 1 under AND, so its informative range is one level here.
