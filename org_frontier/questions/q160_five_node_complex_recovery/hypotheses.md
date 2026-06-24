# q160 — Five-node complex recovery by coupling centrality

Question: at four nodes, coupling centrality ranks every major-complex member above every excluded
spectator in 36% of random forms. Five nodes add a party, and deep_pool_all is the worked five-node
case whose irreducible core {S1,S2,C1,C2} excludes the worker. Does full-separation recovery hold at
five nodes, or does the structure-behavior dissociation widen with scale?

## H1 (fixed before computing)
On five-node forms, coupling centrality fully separates the major complex from the excluded
spectators in a fraction lower than the four-node 36% rate, so the dissociation widens with scale.

Null: the five-node full-separation fraction matches the four-node rate, so scale does not widen the
dissociation.

## H2 (fixed before computing)
The worker excluded from deep_pool_all's core is nonetheless among the top-coupled nodes
behaviorally, a reproducible relay-style false positive (the worker out-couples at least one core
member in a majority of seeded runs).

Null: the excluded worker ranks below core members in coupling centrality, so behavior agrees with
the structural exclusion.

## Verdict rule
- H1 SUPPORTED when the pooled five-node full-separation fraction is below 0.36.
- H2 SUPPORTED when the worker out-couples the weakest core member in more than half of the H2 seeds;
  REFUTED otherwise.
