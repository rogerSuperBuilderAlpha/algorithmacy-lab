# Q11 — oscillatory forms (limit-cycle attractors) and the Φ(n) scaling law · Stage 1 review

**Question.** Do coordination forms whose dynamics settle onto a limit cycle (an oscillatory
attractor) carry a Φ(n) scaling law distinct from the fixed-point families in the scaling-law zoo
(Probe 132) — the conjunctive hub Φ=n−1 (Probe 116), the pool Φ=n(n−1), the parity hub Φ=2^(2−n),
and the period-capped ring? Build limit-cycle forms (a ring with a rotating update, or a mediated
form with a periodic commit) at n=3,4,5,6, compute Φ_MIP and the dyadic/triadic verdict for each,
and determine whether a limit-cycle attractor gives a distinct law (logarithmic, capped, linear, or
otherwise) and whether the cycle period enters the law.

**Agenda id.** Q11 — oscillatory Φ scaling (sibling of the scaling-zoo probes #132, #115, #116, #119,
#133; touches the attractor/grain probes #32, #60, #81, #125, #127, #130).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #132 (scaling-law zoo) | Five families, four laws: chain constant Φ=2, **ring constant Φ=4 for n≥4**, conjunctive hub linear Φ=n−1, pool super-linear Φ=n(n−1), parity hub decaying Φ=2^(2−n). | The direct anchor. It established the zoo of fixed-point laws Q11 wants to compare against. The ring it built uses an **AND-of-neighbors** update (`int(x[a] & x[b])`), which collapses to a fixed point, not a rotating limit cycle. So the one form named "ring" in the zoo is *not* oscillatory; Q11 asks whether a genuinely cycling ring (rotating update) gives a fifth law or reproduces the capped Φ=4. |
| #116 (conjunctive law) | The AND-all hub holds the full node set in its core with Φ=n−1 at n=4..7; OR-all matches. An all-required commit binds every member into one irreducible whole, Φ growing one bit per added member. | One of the fixed-point laws Q11 measures against. It is the linear benchmark. A limit-cycle form whose Φ also grew linearly would be law-equivalent to the conjunctive hub; the question is whether oscillation breaks from it. |
| #115 (parity scaling) / #120 (parity dissolution) | The XOR hub stays triadic with the full core at every size while Φ halves each step: Φ=2^(2−n), below any floor near n=22. | The decaying fixed-point law. Notable because XOR is the natural single-step "flip" rule, the building block of a rotating update — a rotating ring is a spatial chain of such flips. #115 is the closest existing result to a cycling rule, but it is a *hub* (every node reads the shared commit) settling to a fixed point, not a ring running a traveling wave. Whether distributing the flip around a ring changes the law from 2^(2−n) is exactly what Q11 opens. |
| #133 (party peer coupling) | Lateral party-to-party edges restore the full multi-hub core and lift Φ to the pool value n(n−1); the center-periphery drop (#128) was a missing-edge artifact. | Shows that local lateral coupling among peers (the ring's defining edge pattern) can push integration toward the quadratic pool law. A ring is the minimal lateral-coupling topology, so #133 gives a prior that a ring's law could sit anywhere between the capped Φ=4 (#132) and the pool — and a rotating update may move it again. |
| #32 (temporal grain) | All three triadic corpus forms flip to dyadic under the 2-step composed map (Φ 2.0→0); dyadic forms stay dyadic. Observing too coarsely washes out the triad. | The period enters the verdict here, but as a *sampling* caveat, not as a term in a Φ(n) law. A limit-cycle form has a natural period p; #32 warns that reading it at a grain coarse relative to p can collapse the verdict, so Q11 must report the oscillatory law at grain 1 and watch how the verdict behaves across grain — distinct from asking whether p enters the scaling law itself. |
| #60 (grain threshold) | Triadic corpus forms flip to dyadic at grain k=2, with **attractor periods 1–2**; the detectable band is narrow for short-period forms. | The probe that explicitly tied the grain-flip point to the attractor period. It is the one place "period" already appears as a quantity in the program, but only for short-period (1–2) fixed-point/short-cycle corpus forms and only as a flip threshold. Q11 builds forms with deliberately longer periods (a rotating ring of size n has period n or a divisor), so #60 predicts a wider detectable band and lets Q11 ask the new question of whether p enters Φ(n) rather than only the grain band. |
| #81 (criticality) | Sweeping the parties' tracking phase p, Φ is symmetric: 2.0 at both deterministic extremes (in-phase and anti-phase) and 0 at random tracking (p=0.5). Φ tracks coupling determinism, not phase sign; the interior is a trough. | The nearest the program comes to a *phase/oscillation* axis. It found phase sign irrelevant to Φ and no interior peak, but it varied a stochastic tracking probability on a fixed small form, not a deterministic limit cycle across sizes. It gives a prior that the *sign* of an oscillation will not matter, while leaving open whether a sustained cycle scales differently in n. |
| #125 (residual characterization) | The dyadic false-positive residual forms **collapse fast to a fixed point** (mean max-period 1.08 vs 2.32 for the rest) and are never invertible; there is a dynamical signature connectivity misses. | Establishes a link between attractor type and the verdict at n=3: dyadic residual forms are the fixed-point collapsers, triadic forms more often sustain longer periods and invertible maps. This motivates the hypothesis behind Q11 — that sustaining a cycle is associated with irreducibility — but #130 (below) shows the link does not hold as a clean predicate. |
| #127 (dynamics ablation) | Adding global-dynamics features (reachability, period) lifts classifier accuracy +0.029 over connectivity+synergy, closing ~half the 7% residual. Attractor structure carries part of the verdict the graph and function tables miss. | Confirms attractor/period information is *verdict-relevant* in aggregate. Q11 turns this from a classifier feature into a structural question: build forms whose attractor is a cycle by construction and read Φ(n) directly, rather than mining period as one feature among ten. |
| #130 (attractor condition) | Among 2576 three-way-coupled wirings, **no attractor predicate separates the verdict**. A collapsed map covers 264/288 dyadic residual forms but 562 triadic forms collapse the same way; the best combination reaches only 0.92, below baseline. Collapsing dynamics does not isolate the residual. | The key tempering result. It refutes the simple "fixed point ⇒ dyadic, cycle ⇒ triadic" hypothesis that the question's framing leans on. Many triadic forms have fixed-point attractors and many cyclers are dyadic, so a limit cycle is **neither necessary nor sufficient** for triadicity. Q11 is therefore not "does a cycle make it triadic" (answered no, #130) but the untouched scaling question: *given* a triadic limit-cycle family, what is its Φ(n) law and does the period p appear in it. |
| #57 (chain theorem) | Chains k=1..4 (n=3..6) are triadic at Φ exactly 2.0 with a balanced MIP near the middle; depth adds intermediaries, not integration. | The constant-law benchmark and a structural cousin of the ring (a ring is a chain closed into a loop). The closure is what can create a rotating cycle, so #57 gives the open-chain baseline (flat Φ=2) against which a closed, rotating ring's law is measured. |

## The gap

The scaling-law zoo is mapped for fixed-point attractors. Probe 132 sorted five topologies into four
Φ(n) laws — constant (chain, and the AND-neighbor ring at Φ=4 for n≥4), linear (conjunctive hub,
Φ=n−1, #116), super-linear (pool, Φ=n(n−1)), and decaying (parity hub, Φ=2^(2−n), #115/#120) — and
every one of those forms settles to a fixed point. The "ring" in the zoo runs an AND-of-neighbors
update that collapses, so the zoo contains no form that settles onto a sustained limit cycle. The
period has appeared only as a sampling caveat: a coarse observation grain relative to the attractor
period flips the verdict (#32, #60), and attractor structure carries a few points of classifier
accuracy in aggregate (#127). The hypothesis that a cycle drives irreducibility is also already
tempered — #130 shows that collapsing-vs-cycling does not separate the verdict, so a limit cycle is
neither necessary nor sufficient for a triadic form. What no probe has done is build a coordination
form whose dynamics settle onto a genuine limit cycle — a ring with a rotating update, or a mediated
form with a periodic commit — at n=3,4,5,6, compute exact Φ_MIP and the verdict for each, and read
off the Φ(n) law. So the open question is specifically a scaling-law question, not an irreducibility
one: does an oscillatory attractor give a fifth law distinct from constant, linear, super-linear, and
decaying, or does it reproduce one of them (most plausibly the period-capped Φ=4 ring or the linear
hub), and does the cycle period p enter the law as a term — does Φ depend on p, on n, or on their
relation — in a way the static fixed-point families never exhibit. No prior probe answers this; the
nearest ones either build only collapsing forms (#132's ring) or use period as a classifier feature
or grain threshold (#60, #127, #130) rather than as a variable in a measured Φ(n) scaling law.
