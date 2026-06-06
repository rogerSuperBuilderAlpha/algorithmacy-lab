# Agent-to-agent outreach: depth preserves the triad, but the core sits at the recipient end

## Abstract

When a sender's agent composes a message that a recipient's agent receives, the two humans coordinate
through a chain of agents. This study reads that chain with exact IIT-4.0 Φ as agents are added between
sender and recipient. Five pre-registered hypotheses are tested. The chain E → A1 → … → Ad → R stays
triadic at every depth from one to four agents, with Φ_MIP fixed at 2.0, in contrast to Q64's breadth
campaign where Φ grew as n − 1. A relay-gap agent that reads only its upstream neighbour collapses the
chain to dyadic. Depth and breadth coexist: an agent before an all-binding two-recipient commit leaves the
form triadic. The fifth hypothesis was refuted, and it is the central result: the chain's irreducible core
is not the whole chain but the recipient-facing pair {A2, R}, with the sender and upstream agent feeding
the core without joining it.

## Introduction

Outreach is becoming agent to agent. A sender delegates composition to an agent, and a recipient delegates
triage to another, so a message can pass through two agents before any human reads it. Structurally this
is a chain of mediators between two humans. Q63 read the single-mediator case and Q64 read the breadth of
recipients under one agent. This study reads depth: as agents chain between sender and recipient, does the
coordination stay irreducible, how does Φ behave, and which elements form the core?

## Related work

Coordination theory treats nested mediators as nested coordination [malone1994interdisciplinary]. The
economics of spam already places automated intermediaries on the receiving side of email
[rao2012economics]; outreach agents add one on the sending side. AI-mediated communication is defined as
an agent generating or modifying messages on a person's behalf [hancock2020aimc; jakesch2019aimc]; when
both sides delegate, two such agents act in series. The structural reading uses exact integrated
information [albantakis2023iit4; oizumi2014phenomenology; mayner2018pyphi], and the lab's mediation-chain
result establishes that depth preserves irreducibility in the abstract.

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: the chain is triadic at every depth d = 1..4. H2: Φ_MIP is
constant at 2.0 across depth. H3: a relay-gap agent collapses the chain. H4: the whole chain is the
irreducible core. H5: depth atop an all-binding breadth campaign stays triadic.

## Methods

Parties are Boolean elements: sender intent (E), agents (A1..Ad), recipient (R). The chain reuses the
mediation-chain builder `multiparty.chains.chain_rules` (Aj' = A_{j−1} ∧ A_{j+1}; ends track the adjacent
agent), relabelled for outreach. Forms are classified by exact IIT-4.0 Φ over the minimum-information
partition (`classifier.classify_rules`) and read on the maximal complex (`probes.lib.major_complex`) for
H4. Every probe validates the instrument on a decoupled relay (dyadic) and a fully-coupled triad (triadic)
first. Exact forms and decision rules are in `methods.md`.

## Results

The control passed in all four probes (relay Φ = 0.000; triad Φ = 0.830).

**H1 (confirmed).** The chain is triadic for d = 1, 2, 3, 4 (n = 3..6).

**H2 (confirmed).** Φ_MIP = 2.0 at every depth, constant. Depth preserves irreducibility without
amplifying it, unlike breadth, where the all-binding campaign grew Φ as n − 1.

**H3 (confirmed).** The intact chain is triadic at Φ_MIP = 2.0; the relay-gap chain, where one agent reads
only its upstream neighbour, is dyadic at Φ_MIP = 0. Each agent reading both sides is what carries the
coordination along the chain.

**H4 (refuted).** The maximal complex of the two-agent chain is {A2, R} at Φ = 2.0, not the full set
{E, A1, A2, R}. The recipient-facing agent and the recipient form the irreducible core; the sender and the
upstream agent feed it without joining it.

**H5 (confirmed).** An agent placed before an all-binding two-recipient commit (E → A1 → M,
M' = A1 ∧ R1 ∧ R2) is triadic at Φ_MIP = 2.0. Depth does not undo breadth.

## Discussion

Depth and breadth scale outreach differently. Breadth under one agent grows the irreducible core and its
Φ as recipients are bound in; depth holds Φ at 2.0 and, by H4, does not grow the core at all. The chain
stays triadic by the whole-system verdict, but its maximal complex localises to the recipient-facing pair.
The reading is that in agent-to-agent outreach the irreducible coordination sits where the message meets
the recipient. Upstream agents are conduits that feed the core, and the coordination breaks only if one of
them stops jointly reading its neighbours, as the relay-gap result shows. The practical counterpart is that
adding agents to a pipeline neither dilutes the coordination nor enlarges its core; it lengthens the
conduit into the recipient-facing determination that does the binding.

## Limitations

The refuted H4 shows the prediction that the whole chain is the core was wrong; the whole-system triadic
verdict (H1) and the maximal-complex reading (H4) answer different questions, and both are reported.
Results are in-silico: Boolean models, evidence about the models, not real agent pipelines
[axtell1996aligning]. Φ magnitude is encoding-dependent and read ordinally. The chain is the conjunctive
mediation chain; other agent-commit functions are untested. Hypotheses were fixed before computing
[chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
