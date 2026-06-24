# q155 — Methods

## Corpus

The corpus is 89 synthetic Boolean coordination forms: the 9 named multiparty forms from
`org_frontier.multiparty.forms` plus 80 random forms drawn from the same generator family used in
`bridge_four` (random input sets per node, single-input rules from a four-rule alphabet, multi-input
rules from random truth tables). Random forms have 3 to 5 nodes. The random draw is seeded with
`numpy.random.default_rng(0)`; trajectory seeds are fixed per form, so the whole run reproduces
byte-for-byte.

## Ground truth and score

For each form the maximal complex is read by exact IIT-4.0 Φ over reachable states
(`complex_over_states`). Each node gets a binary label: 1 if its index is in the complex's
`node_indices`, else 0 (`node_membership_labels`). The per-node score is `coupling_centrality` from
a seeded stochastic trajectory of the same form (`trajectory`, 600 steps, flip 0.08).

## Scoring

All nodes are pooled across the corpus. ROC-AUC is computed exactly from the Mann-Whitney rank
statistic, with ties counted at 0.5. The decision threshold is the score that maximizes balanced
accuracy over the pooled set. A label-shuffled null AUC is computed from a fixed permutation of the
labels.

Each form is tagged by topology from its connectivity matrix (`topology_of`): star, chain,
reciprocal, mediator, or other. The per-topology table reports AUC within each class and the
false-positive rate per node at the pooled threshold. H2 reads whether chain forms lead on
false positives.

## Instrument control

The probe first validates the machinery on the faithful triad `[x1, x0&x2, x1]`, which reads verdict
triadic with max_phi 2.0 and a full three-node core. The AUC routine is checked on a perfectly
separable case (AUC 1.0), a fully tied case (AUC 0.5), and a label-shuffled null near 0.5. The run
prints `CONTROL ... PASS` only when all checks hold.

## Scope and validation gap

Every form is a synthetic Boolean coordination model. The numbers are in-silico readings of how a
behavioral centrality tracks structural membership. No field organization is measured, and no claim
is made that coupling centrality recovers membership in real coordinations. The validation gap
between these synthetic forms and any field system is open.
