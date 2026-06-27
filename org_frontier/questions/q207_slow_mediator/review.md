# Q207 — Does a half-rate mediator (updating every two steps) still bind the triad, or does it factor? · Stage 1 review

**Question.** When the mediator recomputes its commitment only every second step while the parties update
every step, does the major complex still hold the worker–system–counterpart triad, or does the slower
mediator let the coordination factor?

**Agenda id.** Agenda Q9 (timescale separation).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #3 | An exogenous rule-clock stays a spectator (emit-only, not in the core); an outcome-tracking regime destabilizes the core | The clock that gates the mediator's update rate is exactly such an exogenous clock; predicts it stays a spectator |
| #62 | Sequential (asynchronous) update factors the triad | Motivates the question: a non-synchronous schedule changed the verdict; a half-rate mediator is a controlled form of that |
| synthesis | The conjunctive triad W'=S, S'=W∧C, C'=S is triadic, Φ_MIP=2.0 | The synchronous reference the slow mediator is built from |

## The gap

The lab's instrument reads a one-step synchronous transition. Real coordination is rarely synchronous: a
mediating system often commits on a slower cadence than the parties it coordinates — a daily standup, a
weekly merge window, a batch job — while the parties act continuously. Probe 62 showed that one
non-synchronous schedule, fully sequential update, factors the triad, but it did not isolate the mediator's
rate: sequential update changes everyone's timing at once. Agenda Q9 asks the cleaner question — hold the
parties at full rate and slow only the mediator to every second step — and it is unanswered. The slowing is
modeled with an explicit clock node that gates the mediator's recompute, so the system stays a deterministic
one-step form the instrument reads directly, and the major complex says whether the triad survives the
mediator's slower cadence and whether the clock is a spectator (Probe 3) or a member.
