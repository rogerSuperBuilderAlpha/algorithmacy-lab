# Thread — degree predicts the bottleneck but does not determine it

A prior for the catalog. Is a coordination's bottleneck simply the most-connected party? Almost, and not
quite. When a form has a single veto player it is among the highest-degree nodes nine times in ten, but a
tenth of the time a less-connected party holds the bottleneck. Connectivity predicts the bottleneck without
fixing it; the cooperative-game position is not reducible to raw degree. Reproduce with
`python org_frontier/threads/degree_bottleneck/degree_bottleneck.py` (seed 11).

## Setup

Three-party forms with random rules, restricted to those with a single veto player — a single party in every
integrating coalition. For each, the veto player's degree, the number of dependency edges into and out of it,
is compared with the maximum degree in the form. The measures are how often the veto player has the maximum
degree, and how often it is the unique node with that degree.

## The arc

**The bottleneck is usually the most connected.** Of 788 single-veto forms the veto player has the maximum
degree in 719, 91%. The party every integrating coalition must contain is, nine times in ten, among the
most wired into the coordination. Connectivity tracks the bottleneck closely.

**But not always, and rarely uniquely.** In the remaining 9% the veto player is below the maximum degree: a
less-connected party holds the bottleneck while a more-connected one does not. And the veto player is the
unique most-connected node in only 141 forms, 18%, because in these dense forms several parties usually tie
for the top degree. So degree narrows the field but does not pick the bottleneck out of it: most of the time
the maximum is shared, and a tenth of the time the holder is not even at the maximum.

## What the thread establishes

Degree predicts the bottleneck and does not determine it. The single veto player is among the highest-degree
nodes in 91% of forms but is the unique most-connected node in only 18%, and in 9% it is below the maximum
degree entirely. As a prior for reading real coordination: the most-connected party is a good first guess
for who holds the arrangement, right about nine times in ten, but connectivity is not the whole story, and a
less-connected party can sit at the bottleneck where the structure, not the edge count, puts it. The
cooperative-game reading the other threads use is what resolves the cases degree leaves open.

## Limits, honestly

Degree here counts dependency edges in and out, a plain graph measure; a weighted or directed refinement
would track the bottleneck differently. The result is over the single-veto forms among random rules at one
seed, three nodes, a registered baseline. The 9% below-maximum is the load-bearing figure, the gap between
connectivity and the cooperative-game position. Everything is in-silico, and a prior is to be tested against
data.
