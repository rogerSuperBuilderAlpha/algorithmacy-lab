# Q218 — The chicken-and-egg feed · Stage 1 review

**Question.** When a celebrity's controversial post spreads, is the arrangement a one-way chain with a
clear first cause (dyadic: it factors, Φ = 0) or does an engagement-ranked feed that reacts to the audience,
and an audience that reacts to the feed, form a mutual-dependence loop in which no part comes first
(triadic: irreducible, Φ > 0, algorithmacy)? Which ingredient decides it: the algorithm, the audience's
mutual visibility, or whether the celebrity reacts back?

**Agenda id.** New question, outside the written agendas.

## Prior work that bears on this

| source | finding | how it relates |
|---|---|---|
| IIT itself (Oizumi et al. 2014; Albantakis et al. 2023) | a system with a unidirectional cut has Φ = 0; purely feedforward systems are not integrated | the "first cause" intuition has a known formal counterpart; H1 restates it as a control, not a finding |
| atlas (`studies/coordination_logic_atlas/`) | a one-way gate that feeds the determination but never reads back sinks whole-system Φ while the core survives; a rotation (ring of copyists) is irreducible | predicts that an unmoved celebrity sinks the whole system and that a ring binds |
| `studies/hybrid_ff_recurrent_seam/` | a recurrent cycle feeding a feedforward chain keeps the major complex inside the recurrent zone; the feedforward tail is excluded | predicts where the core sits when a loop is fed by a one-way source |
| canonical triad (`classifier/`) | W'=S, S'=W∧C, C'=S triadic at Φ = 2.0 | the template for a feed that reads two sides that read it |
| Q215 | interior factorings can be specific to IIT 4.0 | measure dependence |
| recurrence arm (`org_frontier/recurrence/`) | cross-recurrence reads which party leads in a trajectory | a behavioral "who comes first" measure; not used here, noted as the complementary instrument |

## The gap

The lab has established that one-way sources factor and rings bind, but it has not applied this to
information spread, nor separated three candidate sources of "no first cause": an engagement-reactive
algorithm, an audience that sees itself, and a source that reacts to its own reception. The question asks
which of the three is necessary and sufficient in small models, and states openly which parts of the
answer are already implied by IIT.
