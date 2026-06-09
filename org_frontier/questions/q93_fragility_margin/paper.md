# Q93 — A margin-to-dyadic metric, and two notions of robustness that diverge

## Question

The verdict is binary at Φ_MIP = 0, with no measure of how close a triadic form sits to the dyadic
boundary. A margin-to-dyadic metric (the smallest structural perturbation that collapses a triadic form)
would turn the binary verdict into a gradient, and might predict the noise robustness Q71 measured without
simulating any noise. This study builds the metric on the n = 3 family and tests whether it predicts noise
survival.

## Method

The 24 triadic forms in the 256-form strict-mediation family are the subject. Each form is eight truth-
table bits: a two-bit read for each outer party off the mediator and a four-bit mediator function. The
structural margin flips one bit at a time, across all eight, and counts how many flips turn the form
dyadic; the robustness fraction is the share of flips that preserve the verdict. The mediator is labelled
parity (XOR/XNOR), monotone (AND/OR/NAND/NOR), or other. Noise survival is the exact Φ of the form's TPM
mixed toward its flipped output by noise 0.1.

## Results

Every triadic form sits on a structural edge: all 24 have at least one single-bit flip that collapses them
to dyadic. The margin is nearly binary. The robustness fraction takes only two values — 0.125 for sixteen
forms and 0.250 for eight — and the split is the mediator's function: the eight parity forms are the
sturdier ones, the sixteen monotone-and-other forms the more fragile.

Noise survival also takes two values, and they line up against the margin. The structurally sturdiest forms
are the dynamically weakest. The eight parity forms hold robustness 0.250 and noise-Φ 0.377; the sixteen
others hold robustness 0.125 and noise-Φ 1.155.

| mediator | count | robustness | noise-Φ |
|---|---|---|---|
| monotone and other | 16 | 0.125 | 1.155 |
| parity | 8 | 0.250 | 0.377 |

| | result |
|---|---|
| H1 every triad sits on a structural edge | confirmed (24/24) |
| H2 the margin varies (range ≥ 0.25) | refuted (range 0.125) |
| H3 margin predicts noise survival | refuted (inverse relationship) |
| H4 parity mediators are sturdier | confirmed (0.250 vs 0.125) |

## Interpretation

Structural robustness and dynamical robustness are different quantities, and the mediator's function drives
them apart. A parity determination binds the triad firmly against rewiring — twice as many single-bit edits
preserve it — and weakly against noise, holding a third of the Φ a monotone determination keeps at the same
noise level. Monotone determinations do the reverse. The structural margin therefore cannot stand in for
noise robustness; on this family it anti-tracks it.

The result extends Finding 4. Parity was known to yield triadic forms twice as often as monotone functions;
it also yields the structurally sturdier triads. The new and opposing fact is that those same parity triads
are the ones noise erodes fastest. Frequency, structural robustness, and dynamical robustness are three
properties of a determination, and parity ranks high on the first two and low on the third.

The margin metric is therefore informative about structure but near-binary at n = 3 and not a proxy for
noise survival. Its value is as a clean separator of parity from monotone, not as a continuous fragility
scale, and not as a shortcut to the dynamical robustness that needs the noise computation to see.

## Limitations

In-silico; Boolean models with exact verdicts and exact Φ. The margin is near-binary on the three-node
family because each form has only eight single-edit neighbours; a richer gradient could appear at larger n
and is untested. Noise survival is read at a single level (0.1) under the repo's output-noise mix. Only
single-bit flips are perturbed; multi-bit and edge-deletion neighbourhoods are not measured. The
pre-registered rank-AUC for H3 was undefined because noise-Φ is constant within each class; the descriptive
cross-tab carries the conclusion, which is against H3.
