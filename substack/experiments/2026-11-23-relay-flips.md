# A go-between who reverses the message changes nothing; one with an outside switch splits the group

*Pass a platform's decision along straight or reversed, and the group stays just as tightly bound. Give the go-between a switch that nothing inside the group controls, and the whole comes apart.*

## The question

The [last post](2026-11-23-relay-length.md) found that a platform's loop can pass through a chain of up to
three go-betweens without any loss: the whole group stays bound at Φ = 2. Every go-between there passed the
message on exactly. What if one reverses it, or passes it on only when some outside switch is on?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

A platform listens to two people. The first hears the platform directly; the second hears it through a
go-between. We varied the go-between: copy the message, reverse it, have two go-betweens that each reverse
it, or pass it on only when an outside switch is on (the switch just keeps its own setting). We also tried
a platform that says "go" when exactly one of the two is in (instead of both), and a setup with go-betweens
on both sides, one on one side and two on the other. Seven cases, about 85 seconds. Predictions were
committed first.

## What we found

| go-between | platform rule | members | whole-system Φ |
|---|---|---:|---:|
| copies | both in | 4 | 2.0 |
| reverses | both in | 4 | 2.0 |
| two, each reverses | both in | 5 | 2.0 |
| passes on only if switch is on | both in | 5 | 0 |
| copies | exactly one in | 4 | 0.5 |
| reverses | exactly one in | 4 | 0.5 |
| one on one side, two on the other | both in | 6 | 2.0 |

**Reversing the message costs nothing.** One reversal under either platform rule, or two reversals under
the both-in rule: the numbers match plain copying, down to which groups tie for tightest-bound.

**An outside switch splits the group.** With the switch added, the five-member group has Φ = 0 in all 16
states it can be in. The loop through the go-between still binds at Φ = 2 when the switch is on, but the
switch is never part of the tightest-bound group. Most of the time (11 of 16 states) the switch on its
own, holding its setting, is the top unit at Φ = 1.

**Uneven chains are fine.** One go-between on one side and two on the other still gives Φ = 2 for the
whole group of six.

Four of five predictions held. We had predicted the switch would join the bound core. It did not.

## What it means

Whether a go-between passes a platform's decision on straight or reversed makes no difference to how
tightly the platform and its people are bound. What breaks the whole is a go-between who also answers to
something the group cannot influence. For algorithmacy, a platform's binding reach runs along chains of
people relaying its decisions. It stops at anyone whose relaying depends on an outside condition that
the platform and its people do not shape.

## Limits

Yes/no units, everyone updates at once, no copying errors, one kind of switch (one that only keeps its own
setting), at most six members. Ties are judged at a 1e-9 cutoff, pooled over all states where the top
value appears.

## The code

- Study: [org_frontier/studies/relay_flips/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/relay_flips)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/relay_flips/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/relay_flips/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/relay_flips/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
