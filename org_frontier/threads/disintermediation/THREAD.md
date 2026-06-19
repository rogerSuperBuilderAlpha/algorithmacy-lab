# Thread — disintermediation needs a symmetric channel; a one-way channel entrenches the mediator

A prior for the catalog. The designed-mediator and back-edge threads built a mediator and asked what makes it
commit. This one asks what unmakes its bottleneck: a direct channel between the parties, the structural form
of an outside option. The expectation a reader would bring is that any direct contact between the parties
bypasses the mediator. The models say the opposite for the asymmetric case. A one-way channel — one party
reading the other — entrenches the mediator, raising commitment and concentrating more credit on it. Only a
symmetric two-way channel disintermediates. Reproduce with
`python org_frontier/threads/disintermediation/disintermediation.py` (seed 11; slow).

## Setup

Three architectures share the strict mediator S = node 1 reading both parties W and C, with the parties
otherwise meeting only through S. The first adds no direct channel. The second adds a one-way channel, C
reading W as well as S. The third adds a two-way channel, W and C reading each other. The rules are drawn at
random, so commitment is open. The measures are the rate of commitment (triadic forms), whether S is the
veto player in every integrating coalition, and S's share of the Shapley credit when the form commits.

## The arc

**The strict mediator is the sole bottleneck.** With no direct channel, S is the veto player in every
integrating form, 252 of 252, commitment runs at 10%, and S takes a 0.55 credit share when the form commits.
This is the baseline the other two move from.

**A one-way channel entrenches the mediator.** Adding C → W raises commitment to 29%, keeps S the veto player
in every integrating form, 311 of 311, and lifts S's credit share to 0.88. A partial bypass makes the system
more integrated and the mediator more dominant. The reason is that the one-way edge adds coupling without
giving the parties a mutual channel: C now reads W, but W still reads only S, so W cannot bind to C except
through S, and S stays the bottleneck while the extra structure concentrates more of the credit on it.

**A two-way channel disintermediates.** With W and C reading each other, S is the veto player in only 45% of
integrating forms, down from 100%, and its credit share falls to 0.31, below an equal third. Commitment is
high, 57%, because the system is richly coupled, but the mediator is no longer the party every integrating
coalition needs. The parties can bind without it. A symmetric direct channel is what strips the mediator of
its veto and its credit.

## What the thread establishes

Disintermediation is a property of a symmetric channel between the parties, and a one-way channel does the
reverse. A mediated triad keeps its bottleneck — and the mediator keeps and even grows its credit — when one
party gains a direct read of the other, and loses the bottleneck only when the read is mutual. As a prior
for reading real coordination: one-sided direct contact between two parties is no evidence that the mediator
is bypassable, and can mark the opposite, while a mutual direct channel is what predicts the mediator's hold
should weaken. The structural outside option that frees the parties is the one each can use on the other.

## Limits, honestly

The entrenchment under a one-way channel is specific to this asymmetric wiring, where the bypassing party
reads the other while the other still reads only the mediator; a different asymmetry could behave
differently, and the thread surveys one. The rates are over random rules at one seed, three architectures,
three nodes, so the numbers are a registered baseline rather than a measured fact about real
disintermediation. The verdict that a direct back-channel collapses a strict-mediation triad is one the
program found before; what is added here is the asymmetry, that a one-way channel does not collapse it but
strengthens the mediator, and the cooperative-game reading of both, the veto and the credit moving together.
Everything is in-silico, and a prior is to be tested against data, not asserted of it.
