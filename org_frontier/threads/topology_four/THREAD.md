# Thread — topology sets the credit distribution at four parties too

A prior for the catalog. The cyclic thread found, at three parties, that a symmetric ring shares the credit
while a star concentrates it. This one carries the finding to four. A four-party ring splits the credit into
exact quarters with no bottleneck; a star concentrates it on the hub; a line falls between, its middle
positions holding more than its ends. Topology sets the credit distribution at four parties as it did at
three. Reproduce with `python org_frontier/threads/topology_four/topology_four.py` (seed 11).

## Setup

Three four-party topologies with random rules: a directed ring, each party reading the one before it; a star,
three parties reading one hub and the hub reading all; and a line, each party reading its neighbours. The
measures are the rate of commitment, whether the veto set is empty in the integrating forms, and the top
party's share of the Shapley credit, against the 0.25 of an equal four-way split.

## The arc

**The ring shares exactly.** The directed ring commits in 18 forms and the top party's share is 0.250,
exactly one quarter, with no integrating form having an empty veto in the sense of a privileged node — the
rotational symmetry leaves no party above the others. As at three parties, the ring has no bottleneck and
divides the credit evenly, into quarters now instead of thirds.

**The star concentrates.** The star commits in 5 forms and the hub takes a top share of 0.556, more than
double an equal quarter. The hub reads all three parties and is read by them, the one position every path
runs through, and it holds the credit the way the three-party mediator did.

**The line falls between.** The line commits in 4 forms with a top share of 0.469, between the ring's quarter
and the star's hub share, and a quarter of its integrating forms have no single veto player, 26 of 149. A
line has two interior positions and two ends, so its credit concentrates on the middle without reaching the
star's single-hub extreme, and its bottleneck is sometimes split between the two interior parties.

## What the thread establishes

Topology sets how a coordination's credit is distributed, at four parties as at three. A ring shares it into
exact quarters with no bottleneck; a star concentrates it on the hub past half; a line holds the middle above
the ends. As a prior for reading real coordination: a rotationally symmetric arrangement should divide its
credit evenly and have no holder, a hub-and-spoke arrangement should concentrate it on the hub, and a chain
should favour its middle, and these shapes hold as the arrangement grows from three parties to four.

## Limits, honestly

The commitment rates are low for the star and line, 5 and 4 forms, so their top-share figures are
indicative; the ring's exact 0.250 over 18 forms is the robust result and follows from its rotational
symmetry. The three topologies are representatives with random rules at one seed, four nodes, a registered
baseline. Everything is in-silico, and a prior is to be tested against data.
