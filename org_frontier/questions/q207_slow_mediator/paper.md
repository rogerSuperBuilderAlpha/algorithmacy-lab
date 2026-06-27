# Commit rate, not arrival time: a half-rate mediator factors the triad

<code + data: org_frontier/questions/q207_slow_mediator/ ; probe #361 in probes/PROBES.md>

## Abstract

A mediating system often commits on a slower cadence than the parties it coordinates. This probe holds the
worker and counterpart at full rate and slows only the mediator to every second step, modeled with a clock
node that gates the mediator's recompute, and asks whether the major complex still holds the triad. It does
not. The synchronous triad is triadic at Φ_MIP = 2.0; the half-rate mediator drops the whole system to
dyadic, Φ_MIP = 0, with no irreducible complex containing the worker, system, and counterpart. The only
integrated structure left is the clock's own two-cycle. A mediator that commits at half the parties' rate
is, for binding them, indistinguishable from one that never commits. Read against q205, which found that
delaying when a commitment arrives leaves the triad triadic, the binding depends on the mediator
recomputing at the parties' rate, not on when its commitment lands.

## Introduction

Whether a coordination form is irreducible is read from a one-step synchronous transition. Real mediation
is rarely synchronous: a standup, a merge window, a batch job commits on a slower cadence than the parties
act. Probe 62 showed that fully sequential update factors the triad, but it changed every party's timing at
once. Agenda Q9 asks the isolated question — hold the parties at full rate, slow only the mediator — and it
was unanswered.

## Related work

Probe 3 found that an exogenous rule-clock stays a spectator outside the core. Probe 62 found that
sequential update factors the triad. The synchronous conjunctive triad and its Φ_MIP = 2.0 verdict are the
lab's reference form. q205 (latency feedback) is the companion result on the same mediator under a
different deformation.

## Hypotheses

H1 (control): F0 reads triadic at Φ = 2.0. H2: the half-rate mediator keeps {W,S,C} in the major complex.
H3: the gating clock is a spectator, not in the core. H4: the half-rate core Φ is below 2.0. H5: a
never-committing mediator factors. Nulls are the negations, fixed in `hypotheses.md` before computing.

## Methods

F0 (n=3): W'=S, S'=W∧C, C'=S. F_slow (n=4, labels W,S,C,K): the clock toggles (K'=¬K) and gates the
mediator, S' = W∧C on a K-tick and S' = S otherwise, with the parties copying S every step. F_held (n=4)
freezes the mediator (S'=S) as the zero-rate control. Verdicts use `probes/lib.verdict`; cores use
`major_complex`. The instrument control passed (triadic, Φ = 2.000000) before any other number was read.

## Results

H1 confirmed. H2 refuted: F_slow is dyadic with Φ_MIP = 0; no subset containing W, S, and C is irreducible,
and the major complex is the clock alone, {K} at Φ = 1.0. H3 refuted: the clock is not a spectator but the
sole core member. H4 confirmed: the half-rate core Φ (1.0) is below the synchronous 2.0. H5 confirmed:
F_held factors to the identical verdict, core, and Φ as F_slow — a frozen mediator and a half-rate mediator
are the same for binding.

## Discussion

A half-rate mediator does not bind the triad; it dissolves it. The result sharpens Probe 3: the exogenous
clock stayed a spectator there because a strong triad existed to spectate, but here the clock's gating is
what removes the triad, so its own two-cycle is the last complex standing. The contrast with q205 is the
substantive finding. q205 delayed when the mediator's commitment reached the parties and the triad stayed
triadic; q207 reduces how often the mediator commits and the triad factors. Arrival time and commit rate
are different operations on the same mediator, and only the rate is load-bearing for irreducibility. A
mediator can be late and still bind, but it cannot be intermittent and bind.

## Limitations

One model of slowness — a clock gating the recompute so the mediator holds between ticks. A mediator that
commits a persistent value while still influencing every step, or a continuous half-rate average, are not
tested and could differ. n ≤ 4, one reference triad, exact Φ. The clock's standalone Φ = 1.0 is a property
of a deterministic two-cycle, not of the coordination. In-silico; no empirical coordination is modeled.

## References

Probe 3, Probe 62 (org_frontier/probes/PROBES.md); q205 (org_frontier/questions/q205_latency_feedback/).
