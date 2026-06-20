# The constitutive triad under exact Φ: a prior exploration for the neonatal-third study

The study reads the NICU bedside against the lab's coordination catalog. Before any parent or
nurse is interviewed, the catalog's instruments already constrain what the proposed structure can
be. This note runs that constraint. Four probes turn the study's verbal claims into measured rates
over random Boolean coordination forms, each built from a harness already on `main`. The script is
[`iit_probes.py`](iit_probes.py); the numbers below are 400 forms at seed 11.

The wiring uses four roles. P is the parent, S is the apparatus-and-nurse that the study calls the
committing tertius, T is the care team, I is the infant. An edge a←b means a reads b's state.

This is a prior, held open. The fieldwork can depart from every number here, and the departure is
where the study's contribution gets built. What the probes settle is narrower: what the existing
formal apparatus already says the structure must look like, and the one place the apparatus runs
out — which turns out to be the study's central claim.

## What the probes find

**The committing tertius is a veto player (Probe 1).** A strict star P–S–T, with the apparatus in
the middle, produces an irreducible "triadic" commit in about 10% of random forms. In every form
that integrates at all, the apparatus S sits in the veto set: 159 of 159. No coalition closes the
loop without it. This is the catalog's [veto_player](../../threads/veto_player/THREAD.md) signature
and it matches the [designed_mediator](../../threads/designed_mediator/THREAD.md) result. It is the
formal content of the word "constitutive": there is no path to coordination that routes around the
apparatus.

**The realistic four-node bedside keeps the apparatus pivotal (Probe 2).** Wiring the infant in as
the study describes — treated by the team (I←T) and sensed by the apparatus (S←I), with both
parties reading the apparatus — the apparatus is a veto player in 214 of 214 integrating forms and
sits in the major complex every time. The infant sits in the major complex 17% of the time. The
commit rate drops to 6%, the expected cost of the extra coupled node.

**A pure observer stays out; an emitter can be in (Probe 3).** Add a fourth node and vary only
its coupling. A node that reads the apparatus but is read by no one — a pure spectator, the watching
grandparent, the bedside display with no actuation — never enters the major complex: 0 of 164. This
is the catalog's [observer](../../threads/observer/THREAD.md) result. A node that emits a state the
apparatus reads but takes no input from the others enters the major complex 34% of the time. The two
half-coupled nodes are duals, and the infant is the second kind. The infant emits.
The apparatus reads it. By the measure Φ computes, that coupling makes the infant a member a third
of the time.

**The parent–team tie is disintermediable; the parent–infant tie is not (Probe 4).** Start from the
committing triad, where the apparatus vetoes 100% of integrating forms, and add a channel between
parent and team. A one-way parent→team channel changes nothing: still 100%. A symmetric parent↔team
back-channel drops the apparatus's veto to 45%. This is the catalog's
[disintermediation](../../threads/disintermediation/THREAD.md) result: a reciprocal tie dissolves
the middle. The parent and the team can build that tie — they can talk. The parent and the infant
cannot, because a symmetric channel needs the infant to take up the parent's state, and the infant
has no uptake. So the triad is constitutive asymmetrically. It is dissolvable on the team side and
permanent on the referent side. That asymmetry is the study's "moderated dyad versus constitutive
triad" distinction, measured.

## The boundary the apparatus runs out on

Probe 3 is the one that matters, and it cuts against the study's first framing. The study says the
infant is the referent the parent reaches care *about*, a third that is coordinated over and never
coordinates. Φ disagrees. The infant emits a physiological state, the
apparatus reads it, and that read coupling puts the infant in the irreducible core a third of the
time. By the measure, the infant is a participant.

The disagreement marks exactly what each one measures. Φ measures *causal* irreducibility: whether
the system's parts can be split
without loss, given who drives whom. On that measure the infant is coupled, because the apparatus's
next state depends on the infant's now. The study's claim is about *communicative* coordination:
whether a party can take up another's state as a message and answer it. On that measure the infant
holds nothing, because it has no uptake.

The infant is the case that pries the two apart. A pure observer lacks both — unread, so not a
causal member; mute of intent, so not a coordinator — and the instrument and the construct agree it
is outside. The infant has the first and lacks the second. It is causally in the loop and
communicatively absent. The catalog has no other node like it. Every coordinating party in the
corpus that is read also reads; the half-coupled nodes elsewhere are spectators, which lack the
causal tie too.

This is the wedge the study should carry into the field, stated as a finding the formal arm
produces rather than a limitation it confesses. The grounding literature (Clark and Brennan 1991)
treats a partner who cannot take up a message as a degraded channel, a partner reached with more
effort. The probes say something sharper. The infant is a full *causal* participant with no
communicative uptake at all, and the gap between those two is not a matter of degree. The grounding
literature's degraded partner sits at one end of a scale; the infant is off the scale on one axis
and absent on the other. A nurse who treats the apparatus's read of the infant as the infant's
"answer" is doing real causal work and no communicative work, and the bedside runs on the parents
not feeling the difference. That is the thing to watch for in the interviews.

## Connections to the catalog

- [veto_player](../../threads/veto_player/THREAD.md) and
  [designed_mediator](../../threads/designed_mediator/THREAD.md) — the apparatus's 100% veto is the
  constitutive claim in causal form (Probes 1, 2).
- [observer](../../threads/observer/THREAD.md) — the pure spectator's exclusion, and the duality
  that shows the infant is the other kind of half-coupled node (Probe 3).
- [disintermediation](../../threads/disintermediation/THREAD.md) — the parent–team tie dissolves
  the middle; the parent–infant tie cannot, which is where the triad's permanence lives (Probe 4).
- the `gig_false_dyad` corpus form ([forms_library.py](../../corpus/forms_library.py)) — where an
  unseen counterpart is constitutive; the infant is its limiting case, a counterpart that can never
  communicate at all.

## What would change these numbers

The forms are random Booleans, not elicited rules. A model-bound run of this study would replace the
random ensemble with the determination rules the nurses actually report, and the rates would become
single verdicts. The causal-versus-communicative split is the robust part: it follows from the
infant's wiring, not from any particular rule, so the fieldwork can move the rates without touching
the boundary. What the fieldwork can overturn is the mapping — if the parents and nurses describe a
back-channel to the infant that the probes treat as impossible (a felt mutuality the model does not
encode), that account is the finding, and it is what the interview guide is built to surface.
