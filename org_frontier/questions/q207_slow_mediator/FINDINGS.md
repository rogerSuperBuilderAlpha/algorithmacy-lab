# Q207 — findings

Small deterministic Boolean forms, exact IIT-4.0 Φ. The mediator's update rate is slowed with a gating
clock node K while the parties update every step.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | F0 synchronous triad: triadic, Φ_MIP = 2.000000 |
| H2 half-rate mediator keeps {W,S,C} in the core | refuted | F_slow is dyadic (Φ_MIP = 0); its major complex is {K} alone |
| H3 the gating clock is a spectator | refuted | K is the *only* core member: core = {K}, Φ = 1.000 |
| H4 half-rate mediation lowers core Φ below 2.0 | confirmed | F_slow core Φ = 1.000 < 2.0 |
| H5 a never-committing mediator factors | confirmed | F_held: dyadic, core = {K}, Φ = 1.000 — identical to F_slow |

## A half-rate mediator does not bind; it factors the triad

Slowing the mediator to every second step dissolves the coordination. The synchronous triad is triadic at
Φ_MIP = 2.0; gating the mediator's recompute with a clock drops the whole system to dyadic, Φ_MIP = 0. No
subset containing the worker, system, and counterpart forms an irreducible complex. The only integrated
structure left is the clock's own two-cycle (K' = ¬K), which carries Φ = 1.0 by itself and becomes the
major complex by default. A mediator that commits on half the parties' cadence is, for the purpose of
binding them, indistinguishable from one that never commits: F_held — the frozen mediator — returns the
identical verdict, core, and Φ.

This sharpens Probe 3. There an exogenous rule-clock stayed a spectator, outside the core. That held
because a strong triad existed for the clock to be a spectator to. Here the clock's gating is what dissolves
the triad, so once the triad is gone the clock's self-oscillation is the last complex standing — the
spectator becomes the sole member not by joining a coordination but by outlasting it.

## The contrast with q205: arrival time versus commit rate

q205 found that delaying *when* a mediator's commitment reaches the parties keeps the triad triadic — a
represented one-step delay left the form irreducible and pulled the buffer into the core. q207 finds that
reducing *how often* the mediator commits destroys it. The two are different operations on the same
mediator. A delayed-but-every-step mediator still binds; a punctual-but-intermittent one does not. The
binding depends on the mediator recomputing its commitment at the parties' rate, not on when that
commitment lands.

## Caveats

One model of a slow mediator: a clock that gates the recompute so the mediator holds its prior value
between ticks. Other encodings of slowness — a mediator that commits a value engineered to persist while
still influencing every step, or a continuous half-rate average — are not tested and could differ. n ≤ 4,
one reference triad, exact Φ. The clock's standalone Φ = 1.0 is a property of a deterministic two-cycle, not
of the coordination. In-silico; evidence about how a mediator's update rate shapes irreducibility, not a
measurement of any organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q207_slow_mediator.probe_slow_mediator`
