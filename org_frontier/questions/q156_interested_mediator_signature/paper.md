# q156 — A CRQA signature for the interested mediator

A mediator coordinates two parties. A faithful mediator commits a neutral joint determination of
their warrants and treats the parties as interchangeable. An interested mediator weights one
party's warrant over the other's, serving an objective. The question is whether interestedness
leaves a behavioral trace that structure misses: does the diagonal cross-recurrence prominence on
the mediator's outgoing edges separate interested from faithful mediators once wiring and
structural Phi-core are held fixed?

## Setup

One wiring graph carries every form: W' = S, C' = S, S' = f(W, S, C). The mediator reads both
parties and its own previous state; the parties read the mediator. A rule is faithful when it is
symmetric under swapping the two parties and interested when it is asymmetric. Keeping only rules
that read all three inputs and whose exact IIT-4.0 major complex is the full {W, S, C} gives 27
faithful and 18 interested forms, matched on wiring graph and on structural core.

The behavioral measure is the DCRP peak prominence on the mediator's two outgoing edges, S to W
and S to C, averaged and read from a sampled run. A high value means the parties' states recur at a
fixed lag behind the mediator's, the trace of the mediator steering them. Each form's value is the
mean over 16 seeded trajectories.

## Result

The two pools share the {W, S, C} core, so structural Phi-membership does not distinguish them.
This was the design: it makes any separation behavioral. On the behavioral measure the interested
pool trends lower in mean outgoing prominence, 0.3041 against 0.3303, the predicted direction. The
effect is weak. Matched-pair separation reaches 0.5720, short of the 0.70 bar, and a one-sided
Mann-Whitney test does not clear significance (p=0.21). H1 is refuted. H2 is confirmed: membership
alone misses interestedness, but here the behavioral arm misses it too.

## What it means

Interestedness, as the asymmetry of a mediator's rule, is invisible to major-complex membership
and nearly invisible to outgoing-edge prominence. The construct splits the rule space cleanly, yet
the split does not surface in either reading on this graph. A behavioral signature for
interestedness, if one exists, is not the outgoing-edge prominence tested here. Candidates for a
follow-up are the asymmetry between the two outgoing edges rather than their average, or a
lead-lag read that contrasts the favored party against the disfavored one.

## Scope

Every number is exact IIT-4.0 Phi and CRQA on synthetic Boolean coordination forms. No field
organization is measured, and "interested", "agenda", and "faithful" name the symmetry of a rule,
not measured intent. The behavioral arm runs on synthetic trajectories. The validation gap stays
open: this is an in-silico study of the construct and the instrument.
