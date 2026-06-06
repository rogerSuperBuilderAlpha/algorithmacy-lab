# A recipient-side triage agent joins the coordination only when bidirectionally coupled, and displaces the sender

## Abstract

A recipient who runs an agent to triage incoming messages adds a gatekeeper between sender and recipient.
This study asks whether that triage agent is part of the irreducible coordination, using exact IIT-4.0 Φ
and the major complex. Four pre-registered hypotheses are tested over an outreach triad (sender E,
message M, recipient R) with a triage agent T. A triage agent that only monitors the message, or only
gates delivery without reading, stays outside the major complex; the core remains {E, M, R}. A triage
agent that both reads the message and gates delivery joins the core, confirming the lab's bidirectional
core-membership condition in the triage frame. In the bidirectional case the major complex becomes
{M, R, T}, with the sender displaced from the core. All four hypotheses confirmed.

## Introduction

The receiving side of outreach is increasingly automated: filters and triage agents decide which messages
reach a person [rao2012economics]. When both sides delegate to agents, the recipient's triage agent sits
between the sender's message and the recipient [hancock2020aimc]. Is that triage agent part of the
irreducible coordination, or an external filter? The lab's principal/gating finding says a gatekeeper
joins the core only under bidirectional coupling; this study tests that for a recipient-side triage agent.

## Related work

The economics of spam frames receiving-side filtering as a defence against unsolicited volume
[rao2012economics]. AI-mediated communication places agents on both sides of an exchange [hancock2020aimc;
jakesch2019aimc]. Coordination theory treats a constraining gatekeeper as part of the structure
[malone1994interdisciplinary]. Integrated information theory decides membership by the major complex
[oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi], and the lab found a principal joins it iff
bidirectionally coupled.

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: a monitoring-only triage agent stays out of the core. H2:
a gating-only triage agent stays out. H3: a bidirectional triage agent joins the core. H4: the base
coordination stays triadic in every configuration.

## Methods

The base triad is E'=M, M'=E∧R, R'=M (Q63 read_recipient). The triage agent T takes three couplings:
monitoring_only (T'=M, no gate), gating_only (R'=M∧T, T'=T frozen), bidirectional (T'=M and R'=M∧T). Each
form is read on the major complex (`probes.lib.major_complex`) with exact IIT-4.0 Φ; the instrument is
validated on a decoupled relay and a fully-coupled triad first. Exact forms and decision rules are in
`methods.md`.

## Results

The control passed (relay Φ = 0.000; triad Φ = 0.830).

**H1 (confirmed).** Monitoring-only: the major complex is {E, M, R} at Φ = 2.0; T is excluded.

**H2 (confirmed).** Gating-only: the major complex is {E, M, R} at Φ = 2.0; T is excluded.

**H3 (confirmed).** Bidirectional: T joins the major complex. The core is {M, R, T} at Φ = 2.0.

**H4 (confirmed).** The major complex is triadic at Φ = 2.0 in all three configurations; adding the triage
agent never collapses the coordination.

## Discussion

A recipient-side triage agent is part of the irreducible coordination only when it both reads the message
and gates delivery. Monitoring alone leaves it a read-only observer outside the core, and gating alone
leaves it an emit-only switch outside the core; only bidirectional coupling brings it in. This is the
bidirectional core-membership condition holding in the triage frame. The bidirectional case adds a result
worth stating: when the triage agent joins, the sender drops out, and the core becomes the message, the
recipient, and the triage agent. A recipient-side gatekeeper that genuinely participates does not enlarge
the coordination to four; it takes the sender's place in a triad of three. The coordination that was about
sender, message, and recipient becomes about message, recipient, and the recipient's gatekeeper. For
outreach this means an aggressive triage layer can recentre the irreducible coordination on the receiving
side, with the sender outside the core it is trying to reach.

## Limitations

The study is confirmatory; the four predictions followed from the principal/gating finding, and the
sender's displacement is the notable detail. Results are in-silico: Boolean models, evidence about the
models [axtell1996aligning]. Φ is read ordinally. One triage topology is tested, over the read-recipient
triad; multi-recipient or chained triage is untested. Hypotheses were fixed before computing
[chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
