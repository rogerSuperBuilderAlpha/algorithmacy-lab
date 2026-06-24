# q147 hypotheses

Fixed before computing.

## H1 — recurrence topology predicts triadicity

Triadicity probability rises with short-cycle (recurrence) density and falls with diameter.
A network whose dependency graph carries short directed cycles holds feedback, and feedback is
the topological substrate of irreducibility. So a recurrence statistic separates triadic from
dyadic ensembles better than mean degree, which counts edges without regard to whether they
close a loop.

Null: no graph statistic separates triadic from dyadic ensembles above chance.

Decision rule: H1 is supported if a recurrence statistic (cycle density up, or diameter down)
outranks mean degree in absolute correlation with the verdict, the direction matches the
prediction, and the recurrence statistic's separation is significant at p < 0.05.

## H2 — Φ rises with the core's in-degree

Among triadic networks, Φ increases with the mean in-degree of the maximal-complex nodes. The
nodes that carry the integration are the ones that read many others, so a more densely fed core
sustains a larger irreducible structure.

Null: Φ is uncorrelated with the core nodes' in-degree.

Decision rule: H2 is supported if the Pearson correlation between core mean in-degree and the
maximal complex's Φ is positive and significant at p < 0.05.
