# Thread — a coordination needs a threshold of coupling, and commits more readily as it densifies

A prior for the catalog. The cyclic thread found a sparse coordination has no bottleneck and a dense one
commits readily. This one makes that quantitative: how much coupling a three-party coordination needs before
it can bind. There is a threshold and a monotone rise. Below six dependency edges a form never commits; at
six it begins, and the commitment rate climbs with every added edge to the fully connected maximum. Reproduce
with `python org_frontier/threads/coupling_density/coupling_density.py` (seed 11).

## Setup

Three-party forms drawn with random rules, binned by the number of dependency edges in the connectivity
matrix — how many node-reads-node relations the rules actually use, from the four-edge minimum a triad could
have to the nine of full connectivity. The measure is the fraction of forms in each bin that commit, that
read as triadic.

## The arc

**There is a floor.** Forms with four or five dependency edges never commit, 0 of 4 and 0 of 32. Too few
couplings leave the parties too loosely tied for an irreducible structure, and the form factors however the
edges are arranged. A coordination needs a minimum of mutual dependence before integration is even possible.

**Above it, density buys commitment.** At six edges the rate is 20%, at seven 45%, at eight 49%, and at the
nine edges of full connectivity 62%. Each added coupling raises the chance the form binds. The relation is
monotone: a more densely wired coordination is more likely to read as one irreducible whole, with no peak
short of full connectivity in this range.

## What the thread establishes

Commitment has a coupling threshold and rises with density above it. Below six dependency edges a three-party
coordination cannot bind; from six up the commitment rate climbs monotonically to 62% at full connectivity.
As a prior for reading real coordination: an arrangement whose parties depend on one another only sparsely
should not read as an irreducible whole, and the denser the mutual dependence the more readily it should,
with full mutual coupling the most likely of all to bind. The bottleneck and credit findings of the other
threads sit on top of this: they describe forms that have already cleared the coupling threshold.

## Limits, honestly

The edge count is the number of dependencies the rules use, and the bins below six are small, 4 and 32
forms, though their zero rate is unambiguous; the larger bins carry the monotone trend. The relation is over
random rules at one seed, three nodes, so the specific rates are a registered baseline for this population.
The connection to the program's earlier floor work is direct, read here as a density threshold. Everything is
in-silico, and a prior is to be tested against data.
