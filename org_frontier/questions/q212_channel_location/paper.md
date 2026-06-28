# The merging channel must run between the mediators

<code + data: org_frontier/questions/q212_channel_location/ ; probe #366 in probes/PROBES.md>

## Abstract

A direct channel between two triads' mediators merges them into one core. A channel between any other pair of
nodes does not. The same AND cross-triad link is placed at three homologous node pairs — mediator, worker,
counterpart — across two conjunctive triads. Only the mediator-mediator placement produces a major complex
spanning both triads, at Φ=3.0. The worker and counterpart placements leave the maximal complex inside one
triad at Φ=2.0, and they agree with each other, as the triad's leaf symmetry predicts. Every placement makes
the whole six-node system irreducible, so whole-system irreducibility and core merger come apart by where the
link sits.

## Introduction

q211 merged two triads with a direct mediator-mediator channel and explained the merger by the mediator's
role: the channel joined the parts that already carry each triad's integration. That explanation predicts
that moving the channel off the mediators should break the merger. The prediction is testable directly, by
placing the same channel at the worker and counterpart positions and reading whether the cores still merge.

## Related work

q211 (#365) is the result this localizes: a direct mediator channel merged two triads at Φ=3.0. q210 (#364)
is the negative reference, where an indirect link through a shared counterpart merged nothing. The single
conjunctive triad at Φ=2.0 is the per-triad baseline.

## Hypotheses

H1 (control and replication): the single triad reads Φ=2.0, and the mediator channel reproduces q211 —
spanning core at Φ=3.0. H2: a worker-worker channel merges. H3: a counterpart-counterpart channel merges and
matches the worker by leaf symmetry. H4: the mediator channel gives the highest core Φ. H5: channel location
matters. Nulls are the negations, fixed in `hypotheses.md` before computing.

## Methods

Node order (n=6): W1, S1, C1, W2, S2, C2. Both triads are the standard conjunctive triad (W'=S, S'=W∧C,
C'=S). A single AND channel adds one cross-triad conjunct at one homologous node pair: mediator
(S1'=(W1∧C1)∧S2), worker (W1'=S1∧W2), or counterpart (C1'=S1∧C2), and symmetrically for triad 2. Verdicts
use `probes/lib.verdict`, cores `major_complex`; a core spans both triads when it contains a member of each.
The instrument control passed (single triad triadic, Φ=2.000000) before any other number was read.

## Results

H1 and H4 confirmed, H5 confirmed, H2 and H3 refuted on their merge claims. The mediator channel reproduces
q211 exactly: whole system triadic at Φ_MIP=2.0, major complex {S1,W2,S2,C2} at Φ=3.0, spanning both triads.
The worker channel gives a whole-system triadic verdict at Φ_MIP=2.0 but a major complex {S1,C1} inside
triad 1 at Φ=2.0. The counterpart channel gives the same: whole system triadic, major complex {W1,S1} inside
triad 1 at Φ=2.0. The worker and counterpart cores match in Φ and in not spanning, as the leaf symmetry
predicts. Only the mediator placement merges, and only it exceeds the single-triad Φ=2.0.

## Discussion

The merger localizes to the mediator. A direct cross-triad link is not sufficient on its own: the worker and
counterpart channels are equally direct and equally make the whole system irreducible, yet neither merges the
cores. What the mediator channel adds is a link between the two conjunctive nodes, the ones that read both
other members of their triad and carry the triad's integration. Linking those merges the cores; linking the
leaves does not.

The result also separates two effects that q211 left together. Any cross-triad AND link makes the whole
six-node system irreducible — the whole-system verdict is triadic for all three placements. Merging the
maximal complex into one core that spans both triads is the stronger and rarer effect, and it happens only at
the mediator. Whole-system irreducibility is cheap; core merger is not. The two are controlled by different
things, and the channel's position decides the second.

## Limitations

One model of two triads, one AND channel rule, three node placements. n=6, conjunctive coupling, exact Φ. The
non-mediator cores are tie-broken inside triad 1 by the model's symmetry. In-silico; evidence about where a
direct link must sit to bind two model coordinations, not a measurement of any organization.

## References

q211 (org_frontier/questions/q211_direct_mediator_channel); q210 (org_frontier/questions/q210_shared_counterpart);
the single-triad synthesis.
