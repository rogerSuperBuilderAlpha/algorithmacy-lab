# A direct mediator channel merges two triads

<code + data: org_frontier/questions/q211_direct_mediator_channel/ ; probe #365 in probes/PROBES.md>

## Abstract

A shared counterpart did not bind two coordination triads into one core. A direct channel between their two
mediators does. Two complete conjunctive triads are joined only by a link between mediators — S1 reads S2,
S2 reads S1 — swept over three rules: none, AND, OR. Under the AND channel the major complex spans both
triads and reads Φ=3.0, above the single-triad value of 2.0. Under OR the whole system factors, yet the two
mediators still form a Φ=2.0 core across the triad boundary. Both rules cross a boundary that no bridge
through a shared counterpart could. The merger is super-additive, and the obstacle in the shared-counterpart
case was the indirect path, not the principle.

## Introduction

q210 asked whether two triads sharing one counterpart fold into a single larger core, and found they do
not: across three bridge rules the major complex stayed one local triad at Φ=2.0. That result left one
question open. The shared counterpart linked the two mediators only indirectly, through a third node both
fed. Either two self-contained triads resist fusion through any single binary link, or the specific failure
was the length of the path. Replacing the shared counterpart with a direct channel between the mediators
settles which.

## Related work

q210 (shared counterpart) is the immediate predecessor and the negative reference: a peripheral shared party
did not merge two triads. #73 (multi-role) showed that the right shared structure can pull two cores
together, establishing that merger is possible in principle. The conjunctive triad at Φ=2.0 is the
single-triad baseline each core is measured against.

## Hypotheses

H1 (control): the single triad reads triadic at Φ=2.0, and with no channel the two triads stay separate.
H2: the AND channel produces a major complex spanning both triads. H3: that merged core is super-additive,
Φ>2.0. H4: a direct channel merges where the shared counterpart did not. H5: the channel rule matters, AND
and OR giving different cores. Nulls are the negations, fixed in `hypotheses.md` before computing.

## Methods

Node order (n=6): W1, S1, C1, W2, S2, C2. Each triad is the standard conjunctive form, W'=S, C'=S, with the
mediator update carrying the channel: S1'=channel(W1∧C1, S2) and S2'=channel(W2∧C2, S1). The channel is
swept over none (S1'=W1∧C1), AND (S1'=W1∧C1∧S2), and OR (S1'=(W1∧C1)∨S2). Verdicts use `probes/lib.verdict`,
cores `major_complex`; a core spans both triads when it contains a member of {W1,S1,C1} and a member of
{W2,S2,C2}. The instrument control passed (single triad triadic, Φ=2.000000) before any other number was
read.

## Results

All five hypotheses confirmed. With no channel the whole system factors (Φ_MIP=0) and the major complex is
one triad {W1,S1,C1} at Φ=2.0, two separate coordinations. The AND channel makes the whole system
irreducible at Φ_MIP=2.0 and its major complex is {S1,W2,S2,C2} at Φ=3.0, spanning both triads and carrying
more integration than either alone. The OR channel leaves the whole system factorable (Φ_MIP=0) but its
major complex is {S1,S2} at Φ=2.0, the two mediators bound across the boundary. The AND core (Φ=3.0) and the
OR core (Φ=2.0) differ in size and value, so the rule matters.

## Discussion

The five results give a clean contrast with q210. There a shared counterpart, feeding both mediators,
merged nothing; here a direct mediator-mediator channel merges both cores. The difference is the path. The
indirect mediator-counterpart-mediator route did not integrate the two coordinations, while a direct link
does. Two triads are not intrinsically unmergeable, as the q210 null alone might have suggested. What they
need is a direct channel between the parts that already carry each triad's integration, the mediators.

The merger builds something larger than its parts. The AND-channel core reads Φ=3.0 against a single triad's
2.0, so binding the mediators directly adds integration rather than concatenating two coordinations. The
core is asymmetric, one full triad plus the other's mediator, and by the model's symmetry the mirror core
carries the same Φ with the tie broken arbitrarily. The channel rule sets how much binds: AND makes the
whole system irreducible and yields the four-node Φ=3.0 core, while OR leaves the whole factorable yet still
binds the two mediators into a Φ=2.0 core. Even the weaker rule crosses the boundary no q210 bridge reached.

## Limitations

One model of two triads with a direct mediator-mediator channel, three channel rules. n=6, conjunctive
coupling, exact Φ. The AND-channel core is tie-broken by the two-triad symmetry. The channel is a binary
mediator-to-mediator link; richer or weighted channels are a separate question. In-silico; evidence about
how a direct link binds two model coordinations, not a measurement of any organization.

## References

q210 (org_frontier/questions/q210_shared_counterpart); #73 (multi-role, org_frontier/probes/PROBES.md); the
single-triad synthesis.
