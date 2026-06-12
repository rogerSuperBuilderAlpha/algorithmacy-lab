# Q9 — separation of timescales (fast parties, slow mediator) · Stage 1 review

**Question.** In a triadic conjunctive mediated form (worker W, mediator/system S, counterpart C),
does running the parties on a fast clock and the mediator on a slow clock — S holds its previous value
for k steps, or commits with probability 1/k per step — factor the coordination the way sequential
(asynchronous) update did in Probe 62? Compute Φ_MIP, the dyadic/triadic verdict, and the major complex
as a function of the timescale ratio k against the synchronous baseline, and determine whether a slow
mediator changes the verdict or only the Φ magnitude, and whether it pushes S out of the major complex.

**Agenda id.** Q9 — timescale separation (follows Q8; sibling of the schedule/grain modeling-choice
probes #32, #60, #62, #112).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #62 (async) | Every triadic corpus form becomes **dyadic** under sequential (one-node-at-a-time) update, for all 6 orders, while simultaneous update is triadic. Within-step sequential composition lets information pass through in one step and collapses the joint determination. | The direct precedent and the question's anchor. Sequential update is one way to break the synchronous tie between the nodes; timescale separation is another (the mediator updates on its own slower clock). Q9 asks whether slowing one node reproduces the #62 collapse or behaves differently. The mechanism is not the same: #62 changes *within-step ordering*, Q9 changes *update frequency* and adds a hold/memory on S. |
| #43 (self-ref) | A **sticky** mediator (S' = (W∧C)∨S) COLLAPSES the triad to a self-absorbed core {S} — the parties factor out; a parity-memory (XOR) mediator stays triadic. Mediator inertia can break the triad. | The closest existing analogue to a *slow* mediator. A mediator that holds its value is exactly a mediator with self-memory, and the deterministic-hold version of Q9's clock (S' reads S for k−1 of every k steps) is a sticky/self-referential S. #43 shows one inertial S form ejecting **the parties** (core {S}), the opposite of the hypothesis that slowing S ejects **S**. Q9 must reconcile which way the timescale hold pushes membership, and a probabilistic 1/k commit is a softer inertia than the hard OR-stick #43 used. |
| #57 (chain) | Mediator chains k=1..4 are all triadic at Φ exactly 2.0 with a balanced MIP near the middle. Depth adds intermediaries but not integration. | Establishes that lengthening the mediator path does not factor the triad. A slow mediator is a *temporal* analogue of a longer path (S effectively responds every k steps), so #57 gives a prior that the mediator staying in the loop, just slower, might preserve the verdict — a contrast to the #62 collapse. |
| #63 (lifted regime) | A bidirectionally-coupled regime that switches the rule does not join the core; the switch destabilizes the worker out (core {S,C}). Temporal-tracking is not structural even with two-way coupling. | The prior on adding a slow/temporal node to the triad: a slow clock as an *exogenous* regime stayed a spectator (#3), and even coupled it disrupted rather than bound. Q9 differs because the slow clock is not a separate node — it is the mediator's own update cadence — so #63 says the timescale ratio should not enter the core as a new element, but does not settle what slowing S does to S's own membership. |
| #32 (temporal grain) | ALL three triadic corpus forms flip to **dyadic** under the 2-step composed map (Φ 2.0→0); dyadic forms stay dyadic. Observing the coordination too coarsely washes out the triad. | The other timing modeling-choice that flips the verdict. A slow mediator and a coarse grain both compose multiple fast-clock steps into one observed transition. Q9's k-step hold is close to grain-k *on the mediator only*, so #32 predicts a possible collapse, but applied to the whole system, not one node — Q9 isolates the grain change to S. |
| #60 (grain threshold) | Triadic corpus forms flip to dyadic at grain k=2, with attractor periods 1–2; the detectable band is narrow for short-period forms. | Sharpens #32 into a threshold and ties the flip point to the attractor period. Gives Q9 a quantitative prior: the verdict change, if any, should arrive at a k near the form's natural period, and the timescale ratio is the analogous knob. |
| #112 (modeling-invariant verdict) | Of 24 triadic forms, synchronous grain-1 keeps all 24; grain-2 keeps 0; sequential update keeps 0; an across-condition majority keeps 0. There is no modeling-free invariant; the verdict must be reported at the finest grain with synchronous update. | The frame for the whole question. Q9 adds a third timing axis (timescale ratio) to the two #112 already showed are load-bearing (grain #32/#60, schedule #62). It tests whether timescale separation is a *fourth* way to break the synchronous verdict, or whether a slow mediator behaves unlike both grain and schedule. Either way the result extends #112's catalogue of modeling choices the verdict depends on. |
| #109 (hysteresis) | A sticky mediator produces a hysteresis loop as the engagement drive ramps up then down (loop area 0.071); a memoryless mediator does not. With memory, a coordination latches. | The dynamical face of mediator memory. A slow mediator is a memory device, so Q9's hold may introduce path-dependence (the verdict at ratio k could depend on history), which #109 says sticky mediators do. Relevant if Q9 reads the verdict on trajectories rather than the stationary TPM. |
| #27 (reliability) | Φ falls smoothly (2.0→0.14) with mediator unreliability and the verdict holds triadic until reliability 0.5 (random), where it collapses. | The template for a "magnitude-soft, verdict-robust" result on a mediator parameter. If the timescale ratio behaves like reliability, Q9 would find Φ sliding with k but the verdict holding until a degenerate endpoint — the alternative to the #62/#32 categorical flip. |
| #61 (shared shock) | A static common source leaves the verdict unchanged; true correlated *output* noise needs a state-by-state TPM the state-by-node form cannot express. | A modeling flag Q9 must heed. A probabilistic 1/k commit makes S's update stochastic in a way that may not be expressible in a pure state-by-node TPM, so the deterministic k-step-hold construction (a stuttered/composed map, as in #32) is the form that stays inside the instrument; the probabilistic version may need the same probabilistic-TPM care #61 flagged. |

## The gap

The two timing axes that flip the verdict are mapped: coarse observation grain collapses every triadic
form at grain 2 (#32, #60), and sequential within-step update collapses every triadic form for all
orders (#62). Both compose several fast-clock steps into one transition and let information pass through
the mediator inside a single observed step, which is what destroys the joint determination. Q9 asks
about a third, distinct mechanism: not coarse observation and not within-step ordering, but a mediator
that updates less often than the parties — holding its committed value for k steps, or committing with
probability 1/k. No probe has run this. The nearest results split on which way it should go. The
sticky-mediator collapse (#43) and grain collapse (#32) say slowing S could factor the coordination,
but #43 ejected the *parties* into a {S} core, the opposite of the hypothesis that a slow mediator gets
pushed *out* the way sequential update factored it in #62. The chain result (#57) and the reliability
result (#27) point the other way: a mediator that stays in the loop but responds slower might keep the
triad and only grade Φ down, since depth and noise both preserve the verdict until a degenerate point.
And the regime probes (#3, #63) say the timescale ratio itself should not enter the core as a new
element, since it is S's own cadence rather than a separate node. So the specific question — does a slow
mediator relative to fast parties change the *verdict* or only the Φ *magnitude*, and does it eject S
from the major complex as the question proposes, or eject the parties as the sticky analogue #43 did, as
a function of the ratio k against the synchronous baseline — is open. It is the live next axis in the
#112 catalogue of timing choices the verdict depends on, with the deterministic k-step-hold as the
construction that stays inside the state-by-node instrument and the probabilistic 1/k commit flagged for
the same TPM care #61 raised.
