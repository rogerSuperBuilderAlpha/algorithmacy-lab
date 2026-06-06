# The core of an agent chain is a symmetric end pair; closing the loop binds the whole

## Abstract

Q65 found that an agent chain's irreducible core is not the whole chain, reading the d = 2 result as a
recipient-facing pair {A2, R}. This study maps the core boundary across depth and under loop closure with
exact IIT-4.0 Φ. Four pre-registered hypotheses are tested. The open-chain maximal complex is a
two-element end pair at every depth from two to four agents, but it is not specifically the recipient end:
at depths two and three it is {Ad, R}, and at depth four it is {E, A1}, the sender end. The two ends are
symmetric maximal complexes of equal Φ = 2.0, so Q65's recipient-facing reading was a tie-break, now
revised to a symmetric end pair. Closing the chain into a conjunctive ring makes the maximal complex the
whole element set, at Φ = 4.0, double the open chain. Three hypotheses confirmed, one refuted; the
refutation corrects the prior interpretation.

## Introduction

Q65 established that the agent chain stays triadic at every depth but that its irreducible core localizes,
reading the two-agent case as the recipient-facing pair. Whether that localization holds across depth, and
what closing the chain into a feedback loop does, were left open. This study answers both, and in doing so
tests whether the recipient-facing reading was a genuine asymmetry or an artifact of which of two
symmetric complexes the computation returned.

## Related work

Integrated information theory identifies the maximal complex as the subset whose integrated information is
locally maximal, with surrounding elements feeding it without belonging to it [oizumi2014phenomenology;
albantakis2023iit4; mayner2018pyphi]. The lab's program distinguishes a directed path through mediators
from a closed feedback loop, finding the verdict in the causal structure rather than the wiring graph.
Coordination theory frames chained mediators as nested coordination [malone1994interdisciplinary]; the
outreach framing carries over from Q63–Q65 [spence1973job; rao2012economics; hancock2020aimc;
jakesch2019aimc].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: the open-chain core is {Ad, R} at every depth. H2: the
core is size two at every depth. H3: a closed ring binds the whole element set. H4: the ring's core Φ
exceeds the open chain's 2.0.

## Methods

The open chain reuses `multiparty.chains.chain_rules`; the ring sets each element's next state to the
conjunction of its two cyclic neighbours. Maximal complexes are read with `probes.lib.major_complex` and
Φ over the minimum-information partition with `classifier.classify_rules`. Every probe validates the
instrument on a decoupled relay (dyadic) and a fully-coupled triad (triadic, Φ = 2.0) first. Exact forms
and decision rules are in `methods.md`.

## Results

The control passed in both probes (relay Φ = 0.000; triad Φ = 0.830).

**H1 (refuted).** The open-chain maximal complex is {A2, R} at d = 2 and {A3, R} at d = 3, but {E, A1} at
d = 4. The core is an end pair, and which end the computation returns changes with chain length. The two
ends carry equal Φ = 2.0, so they are symmetric maximal complexes and the selection is a tie-break, not a
recipient bias.

**H2 (confirmed).** The maximal complex has exactly two elements at d = 2, 3, 4. The sender and all
upstream agents, or the recipient and all downstream agents, are excluded; only one end pair is the core.

**H3 (confirmed).** The conjunctive ring's maximal complex is the full element set at d = 2 (n = 4) and
d = 3 (n = 5). Closing the loop binds every element into the core.

**H4 (confirmed).** The ring's maximal-complex Φ is 4.0 at both sizes, against the open chain's 2.0. A
closed feedback loop integrates more than an open path of the same elements.

## Discussion

The open chain's core is a two-element end pair, symmetric between the sender and recipient ends. Q65's
recipient-facing reading was the tie-break at d = 2; the symmetric reading supersedes it, and a correction
to Q65 is warranted. The result sharpens the picture of agent-to-agent outreach: the irreducible
coordination in an open pipeline is a single end pair, while the interior agents are conduits, and the
end that registers as the core is not determined by direction. Closing the loop is the structural change
that matters. When the recipient's state flows back to the sender, the whole structure binds into one
core at twice the integration, the same distinction between a directed path and a closed causal loop the
program has found elsewhere. For outreach, a one-way pipeline localizes the coordination to an end pair; a
genuine two-way loop binds the whole exchange.

## Limitations

H1's refutation shows the recipient-facing prediction was wrong and corrects Q65. Results are in-silico:
Boolean models, evidence about the models, not real agent pipelines [axtell1996aligning]. Φ magnitude is
encoding-dependent and read ordinally. The chain and ring use conjunctive commits; other commit functions
are untested. Hypotheses were fixed before computing [chamberlin1965method; platt1964strong;
brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
