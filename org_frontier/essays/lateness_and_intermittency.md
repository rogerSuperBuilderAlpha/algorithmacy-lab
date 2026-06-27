# Lateness and intermittency: how a mediator's timing shapes irreducibility

## Abstract

A mediating system rarely acts in lockstep with the parties it coordinates. It can answer late, and it can
answer on a slower cadence than the parties act. Four exact-Φ studies (q205, q207, q208, q209) deform the
timing of a single integrated triad and measure what happens to its irreducibility. The two deformations
come apart cleanly. Delaying when the mediator's commitment reaches the parties leaves the coordination
triadic at full Φ, at every delay depth tested. Slowing how often the mediator recomputes its commitment
destroys the coordination at any period above one, leaving only a clock. A mediator can be arbitrarily late
and still bind every party; a mediator that commits even every second step binds none. One caveat sits on
the latency side: a delay that is not given explicit nodes is invisible to a one-step instrument, so a low
reading there measures the model's grain rather than the coordination. The results are exact and in-silico,
on Boolean models of one reference triad with conjunctive coupling, evidence about the models and not about
any organization.

## The reference triad and two ways to deform its timing

The worked form is the conjunctive triad: a worker W, a mediating system S, and a counterpart C, with
W' = S, S' = W ∧ C, C' = S. The mediator reads both parties and commits a value that depends on both; the
parties read the mediator. The form is triadic with whole-system Φ_MIP = 2.0, the maximal complex spanning
all three nodes. It is the lab's standard model of an arrangement that binds all three parties at once.

Two knobs change the mediator's timing without changing what it computes. The first is latency: the
mediator's committed value reaches the parties after a delay, modeled as a line of buffer nodes that hold
and pass the value along. The second is cadence: the mediator recomputes W ∧ C only once every p steps and
holds its previous value in between, modeled with a clock or counter that gates the recompute. Latency
moves when a commitment lands. Cadence moves how often one is made. The two knobs turn out to do opposite
things to irreducibility.

## Latency, represented: the triad holds at every depth

q205 inserts one buffer between the mediator and the parties, so the parties read the mediator's value one
step late. The triad stays triadic. Whole-system Φ_MIP falls to 1.0, the buffer joins the irreducible core,
and the worker drops out of the maximal complex, which reads as the delay node taking over the worker's
place in the loop.

q208 sweeps the delay deeper, from one buffer to three. The reading at depth one turns out to be a special
case. Whole-system Φ_MIP runs 2.0, 1.0, 2.0, 2.0 across depths zero through three: it dips at depth one and
returns to the full value at depth two and beyond, where the worker rejoins the core and the entire delay
line plus all three parties forms one irreducible complex at Φ = 2.0. The worker displacement and the
halved Φ that q205 found are artifacts of a single buffer feeding both parties the same value. A second
buffer turns the path into a clean multi-step feedback loop that binds every node. Represented delay, then,
is benign for irreducibility. A coordination can be made arbitrarily late and stays as integrated as the
synchronous form, with the delay line a load-bearing member of the core.

## Latency, hidden: a measurement caveat, not a structural one

The benign reading holds only when the delay has explicit nodes. q205 also runs the same delayed dynamics
observed through a one-step transition matrix over the parties and the mediator alone, with the buffer
marginalized out. That estimate factors: the verdict reads dyadic at Φ ≈ 0, because the worker's next state
depends on the mediator's value one step earlier, which the current observed state does not carry. The same
estimation applied to the undelayed triad still reads triadic at Φ = 0.765, so the collapse is specific to
the unrepresented lag. A low one-step Φ on a coordination known to be lagged is a sign that the lag sits
below the model's grain, and adding the delay as a node recovers the integration. This is a fact about the
instrument. It bounds what a one-step reading can claim, and it leaves the structural conclusion intact:
where the delay is in the model, the triad is irreducible.

## Cadence: any slowing is fatal, and the residual is invariant

q207 slows the mediator to every second step. The triad dissolves. The whole system reads dyadic at
Φ_MIP = 0, no triad member in the major complex, and the only surviving irreducible structure is the gating
clock's own two-cycle at Φ = 1.0. A mediator that recomputes every second step and a mediator that never
recomputes return the identical verdict, core, and Φ. For the purpose of binding the parties, holding a
stale commitment half the time is the same as holding it forever.

q209 sweeps the period from one to four with a mod-p counter gating the recompute. The result is flat.
Period one binds at Φ = 2.0; every period of two, three, and four factors the triad at Φ = 0, with no
threshold and no recovery. Synchronous commitment is the single cadence that binds. The structure left
behind is the same at every period: a single self-toggling bit at Φ = 1.0, the toggle at period two and one
counter bit at periods three and four. A longer counter does not carry more residual integration, because
its carry runs one way and the bits are not mutually irreducible, so only one of them stands as a complex.
The cadence axis is flat and fatal where the depth axis is flat and benign.

## The asymmetry, and what it says

The two deformations are opposite in outcome and alike in shape. Depth holds full integration at every
depth. Period destroys it at every period. The variable that matters is not how far a commitment travels
before it lands, but whether the mediator remakes it at the parties' rate. A mediator can be late without
cost. A mediator that goes intermittent, by any amount, breaks the binding it would otherwise hold.

The mechanism is visible in the models. A delayed-but-continuous mediator still closes a feedback loop on
every step; the loop is longer, and the parties feel the commitment later, and the loop is still one
irreducible object. A gated mediator opens that loop. On the steps it holds, the mediator's next state
is its own held value, and the coordination has no step on which all three are bound together. The clock that does the gating is the one thing left turning, so it is the one thing the
instrument finds.

## Scope

The four studies share one reference triad, conjunctive coupling, and exact Φ at six nodes or fewer, with
one model of delay (a buffer line) and one model of slowness (a counter that holds between ticks). Other
couplings, other ways to make a mediator slow, and larger forms are not tested. The latency caveat is a
property of a one-step instrument applied to a lagged process, which is the instrument an analyst would use
on a real lagged series. Nothing here measures an organization. The claim is about Boolean models of a
mediated triad: in those models, lateness is free for irreducibility and intermittency is total, and the
line between them is whether the mediating system remakes its determination as often as the parties act.
