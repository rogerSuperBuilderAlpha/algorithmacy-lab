# A shared counterpart does not merge two triads

<code + data: org_frontier/questions/q210_shared_counterpart/ ; probe #364 in probes/PROBES.md>

## Abstract

Two conjunctive triads that share one counterpart might fold into a single larger irreducible core. They do
not. Across three rules for how the shared counterpart combines its two mediators — none, AND, OR — the
major complex never spans both triads and never carries more than the single-triad value of Φ=2.0. The
maximal complex is always one local structure: the first triad when the counterpart reads one mediator or
either, and a single worker-mediator pair when it requires both. The bridge rule changes the whole-system
verdict — an AND bridge makes the five-node system irreducible at Φ_MIP=2.0 while none and OR leave it
factorable — but it never merges the two cores. One shared peripheral party is too weak a link to bind two
triads into one whole.

## Introduction

Most of the lab's results concern one triad. Real coordination links many, and the simplest link is a
shared member: a platform that mediates a worker and a counterpart in one market often mediates the same
counterpart in a second. The multi-role study (#73) showed that a single node carrying two roles can pull
two cores together or hold them apart. Whether two complete triads, each with its own mediator, merge when
they share one counterpart is the next question.

## Related work

#73 (multi-role) is the predecessor, on a shared role rather than two full triads. The conjunctive triad
and its Φ_MIP=2.0 verdict are the single-triad reference. The multiparty pool (#119) is the upper reference
for what a fully merged multi-party core could reach.

## Hypotheses

H1 (control): the single triad reads triadic at Φ=2.0. H2: the AND bridge merges both mediators into one
major complex. H3: the shared counterpart is in the merged core. H4: the merged core is super-additive,
Φ>2.0. H5: the AND bridge gives a higher core Φ than the OR bridge. Nulls are the negations, fixed in
`hypotheses.md` before computing.

## Methods

Node order (n=5): W1, S1, W2, S2, C. S1'=W1∧C, S2'=W2∧C, W1'=S1, W2'=S2, and C'=bridge(S1,S2) with the
bridge swept over none (C'=S1), AND (C'=S1∧S2), and OR (C'=S1∨S2). Verdicts use `probes/lib.verdict`, cores
`major_complex`. The instrument control passed (triadic, Φ=2.000000) before any other number was read.

## Results

H1 confirmed. H2, H3, H4, H5 all refuted. Under the AND bridge the major complex is {W2,S2}, a single
worker-mediator pair at Φ=2.0, not both mediators and not C. Under none and OR the whole system factors to
Φ_MIP=0 and the major complex is the first triad {W1,S1,C} at Φ=2.0. Every core sits at exactly 2.0, so
merging adds no integration and the AND and OR cores are equal. The bridge rule changes the whole-system
verdict — AND triadic at Φ_MIP=2.0, none and OR dyadic at 0 — but not the core. The AND core is one of two
symmetric pairs, the tie broken arbitrarily.

## Discussion

A single shared counterpart does not bind two triads into one core. The mediators couple only through the
shared node, and that indirect mediator-counterpart-mediator path does not integrate them: the maximal
complex stays a single local triad or pair at the one-triad value. What the shared party's combination rule
controls is the whole-system verdict. Requiring both mediators (AND) makes the whole arrangement
irreducible; reading one or either leaves it factorable. Irreducibility of the whole and merger of the
cores come apart here: the AND form is triadic as a system while its maximal complex is only a pair. The
result bounds how far the triad's integration extends through a shared member, and it sets up the
complementary question of whether a direct mediator-mediator channel, absent here, would merge what a
shared counterpart cannot.

## Limitations

One model of two shared triads, the shared node a counterpart, three bridge rules, no direct
mediator-mediator channel. n=5, conjunctive coupling, exact Φ. The AND core is tie-broken by symmetry.
In-silico; no empirical coordination is modeled.

## References

#73 (org_frontier/probes/PROBES.md); #119 (multiparty); the single-triad synthesis.
