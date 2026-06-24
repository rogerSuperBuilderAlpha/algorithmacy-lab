# q160 — Coupling-centrality recovery of the major complex at five parties

At four nodes, behavioral coupling centrality ranks every major-complex member above every excluded
spectator in 36% of random forms. The structure and the behavior agree about a third of the time. A
fifth party is the next scale, and `deep_pool_all` is the worked five-node case: its irreducible core
is {S1,S2,C1,C2} at Φ=3.0, and the worker sits outside it. This study asks whether the partial
recovery holds at five nodes or erodes, and whether the worker that structure excludes shows up as a
behavioral false positive.

## What the probe computes

The structural ground truth is the major complex from `complex_over_states`, the node set carrying
the maximal Φ over reachable states. The behavioral ranking is `coupling_centrality` from a sampled
trajectory. A form fully separates when every core member out-couples every excluded node. Forms run
are the named five-node multiparty forms, three inline peers that place the excluded party at
different indices, and a 40-draw `rand_form5` ensemble. The four-node 36% rate is the control
baseline. The instrument control reads the faithful triad: major complex {W,S,C} at Φ=2.0 with the
mediator top-coupled.

## Result

The pooled five-node full-separation fraction is 15 of 43 testable forms, 34.9%. The named forms give
2 of 4, the ensemble 13 of 39 (33.3%). The four-node baseline is 36%. The five-node rate sits one
form below the four-node rate, within the noise of a single draw, so the dissociation does not widen
with scale. The partial-recovery finding from three and four nodes carries to five.

On `deep_pool_all` the worker is the lowest-coupled node. Across 20 trajectory seeds it out-couples
the weakest core member in 5 seeds and holds a mean coupling rank of 3.45 of 5, near the bottom. The
worker reads a single input as a chain endpoint, so its behavioral coupling is weak. Behavior agrees
with the structural exclusion. The worker is not a relay-style false positive.

## Verdicts

H1, that the five-node full-separation fraction is lower than the four-node 36% rate, is SUPPORTED on
the literal threshold and substantively null: 34.9% is below 36% by one form, a rate indistinguishable
from the four-node baseline. H2, that the excluded worker is among the top-coupled nodes, is REFUTED:
the worker ranks near the bottom and confirms the structural exclusion.

## Scope

Exact IIT-4.0 Φ on small Boolean coordination forms. "worker", "core", "spectator", and "coupling
centrality" name graph-and-Φ quantities, not measured organizations. The CRQA arm runs on synthetic
trajectories, so the separation fractions are baselines on synthetic data. The Φ-to-organization
bridge is open; no worker is measured here.
