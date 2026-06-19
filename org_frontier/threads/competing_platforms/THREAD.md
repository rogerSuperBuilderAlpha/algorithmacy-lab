# Thread — a genuine substitute loosens a platform's hold

A prior for the catalog. Two platforms connect the same two parties. When the platforms are identical, a
genuine substitute for one another, no single one holds the bottleneck most of the time and the two split the
credit fairly evenly. When the platforms differ, one becomes the sole bottleneck far more often and the
split runs less even. The presence of a real substitute loosens a platform's hold on the coordination.
Reproduce with `python org_frontier/threads/competing_platforms/competing_platforms.py` (seed 11).

## Setup

Four parties: a worker, a counterpart, and two platforms, the parties reading both platforms under random
rules. In the first form the platforms run the same gate, an AND of the two parties, so either could stand
in for the other. In the second they run different gates, AND and OR, so they are not interchangeable. The
measures are the rate of commitment, whether a platform is in the veto set, and how evenly the two platforms
split the credit.

## The arc

**Identical platforms loosen the bottleneck.** With both platforms running the same gate the form commits in
141 of 400 draws, and a platform is in the veto set in only 103 of 343 integrating forms, under a third. Most
of the time neither platform is the party every integrating coalition must contain, because either can carry
the coordination when the other is dropped. The two split the credit fairly evenly, a smaller-to-larger
Shapley ratio of 0.72. A real substitute means no single platform is indispensable.

**Different platforms restore it.** With the platforms running different gates a platform is in the veto set
in 171 of 319 integrating forms, over half, nearly twice the identical rate, and the split is less even, a
ratio of 0.57. When the platforms are not interchangeable, one does the work the other cannot, and that one
becomes the bottleneck the coordination depends on. Differentiation hands a platform back its hold.

## What the thread establishes

A genuine substitute loosens a platform's hold on a coordination. Two identical platforms leave neither
indispensable most of the time and split the credit fairly evenly; two different platforms let one become the
sole bottleneck and take the larger share. As a prior for reading real coordination: where two channels
between the same parties do the same thing, neither should read as the irreducible bottleneck and the two
should be paid alike, and where the channels differ, the one that does what the other cannot should read as
the holder. This is the outside-option principle as substitution between channels rather than a direct one
between the parties.

## Limits, honestly

Identical and different are two points, the gates AND-and-AND against AND-and-OR; a finer gradient of
similarity would trace the loosening between them. The platforms' substitutability is set by their gates with
random party rules at one seed, four nodes, a registered baseline. The contrast that carries the thread is
the veto rate, 30% against 54%, with the credit ratio confirming it. Everything is in-silico, and a prior is
to be tested against data.
