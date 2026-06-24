# q147 — Which graph statistic predicts a triadic verdict, and how large Φ is

## Question

Across an ensemble of random Boolean networks, which statistic of the dependency graph predicts
whether the whole-system verdict is triadic, and which predicts how large Φ is? Three candidate
statistics stand in for three intuitions: mean degree for raw connectivity, clustering for local
density, diameter for spread, and a short-cycle density for recurrence.

## Approach

Sample 160 random per-node Boolean rule sets (120 at n=4, 40 at n=5). Read each network's
realized dependency graph with a flip-test, so a rule that ignores an input adds no edge.
Compute mean degree, clustering, diameter, and short-cycle density from the connectivity matrix.
Run the exact IIT-4.0 verdict for the triadic/dyadic call and max Φ, and the maximal complex for
the integrating core. Separate the verdict with each statistic by point-biserial correlation;
among triadic networks, correlate Φ against the core's mean in-degree. The control validates the
verdict on the faithful triad (Φ = 2.0) and the graph statistics on a hand-computed ring and
hub.

## Result

Short-cycle density is the best single predictor of a triadic verdict, with point-biserial
r = +0.501, above mean degree at +0.431. Diameter runs negative (r = -0.304): networks whose
parts sit closer together are more often triadic. Clustering separates the verdict weakly
(+0.253). All four are significant, so dependency-graph topology carries genuine signal for
irreducibility, and the recurrence statistic carries the most. Triadic networks average a
per-node short-cycle count of 8.78 against the dyadic 4.18.

The Φ result is a null. Among the 32 triadic networks, the maximal complex's Φ does not rise
with the core nodes' mean in-degree; the correlation is -0.252 (p = 0.166), insignificant and
the wrong sign. A more densely fed core is not a more integrated one.

## Reading

Recurrence, not edge count, is the topological mark of a triadic verdict. A graph that closes
short directed loops can hold the feedback that makes a system irreducible along its party lines.
The magnitude of Φ is a separate question, and core in-degree does not answer it, which fits the
program's standing position that the size of Φ depends on the encoding rather than on a simple
count of connections.

## Scope

Synthetic Boolean networks; exact Φ at n<=5. No worker, market, or platform is measured here.
The correlations describe this in-silico ensemble. The Φ-to-organizational-value bridge is open
(q122).
