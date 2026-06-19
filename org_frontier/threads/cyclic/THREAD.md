# Thread — cyclic coordination has no bottleneck and shares the credit

A prior for the catalog. The engagement thread found that closing a feedback cycle raises commitment. This
one takes the cycle to its limit: a directed ring of three parties, each reading the one before it, with no
designated mediator, and compares it to the mediated star. The topology decides whether a bottleneck exists.
The star makes one party the bottleneck and lets it concentrate the credit; the ring, being rotationally
symmetric, has no single bottleneck and splits the credit exactly evenly. Reproduce with
`python org_frontier/threads/cyclic/cyclic.py` (seed 11).

## Setup

Three architectures over the same parties, with random rules. The mediated star has the parties meeting only
through S. The directed ring has A reading C, B reading A, C reading B, a single loop with no privileged
node. The fully connected form has every party reading the other two. The measures are the rate of
commitment, whether the veto set is empty or a single party in the integrating forms, and the top party's
share of the Shapley credit when the form commits.

## The arc

**The star makes a bottleneck.** In the mediated star a single party is the veto player in 30% of
integrating forms and the veto set is never empty, and the top party takes a 0.55 credit share when the form
commits. The bottleneck and the credit concentration the cooperative-game cluster studied are features of
this topology.

**The ring has none, and shares the credit exactly.** In the directed ring no integrating form has a single
veto player, 0 of 78, and every committing form splits the credit perfectly evenly, a top share of 0.333,
one third each. Rotational symmetry leaves no party in a privileged position, so there is no bottleneck to
hold and no credit to concentrate. Commitment is a touch higher than the star's, 13% against 10%, because
every party closes a loop.

**Full connection commits often but concentrates anyway.** The fully connected form commits in 57% of forms,
far more than either, since every party is coupled to every other. Yet the credit concentrates, a top share
of 0.94, and a single party is the veto player in 40% of integrating forms. The symmetry of the wiring does
not carry into the credit, because the random rules break it: with every edge present, one party's rule
usually does the integrating work, and it takes the credit and the veto with it.

## What the thread establishes

Whether a coordination has a bottleneck is a fact about its topology, not about coordination as such. The
mediated star concentrates a bottleneck and its credit on one party; the directed ring, rotationally
symmetric, has no single veto player and splits the credit into exact thirds; the fully connected form
commits most readily but lets the rules pick a winner that takes the credit and the bottleneck. As a prior
for reading real coordination: a cyclic arrangement with no privileged position predicts no party should
hold the others, and an even division of whatever credit there is, while a star or a richly wired form
predicts a holder.

## Limits, honestly

The exact-thirds credit split in the ring follows from its rotational symmetry, so it is structural rather
than a surprise, and the value is the contrast with the star and the fully connected form. The fully
connected concentration is over random rules and would move with a structured rule family. Rates are over
random rules at one seed, three architectures, three nodes, a registered baseline rather than a measured
fact about real coordination. Everything is in-silico, and a prior is to be tested against data.
