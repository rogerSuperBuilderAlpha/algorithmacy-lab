# q161 — Methods

## Corpus

Sixteen forms: the eight curated 3-node forms in `forms_library`, and the named multiparty forms
in `multiparty/forms` (n = 4 and n = 5). One form (`pure_relay`) has a sub-dyadic structural core
and is dropped, since it is neither triadic nor dyadic. The kept corpus is seven triadic and nine
dyadic.

## Structural ground truth (fixed, flip-independent)

Each form's transition matrix is built from its Boolean rules and its connectivity matrix is read
numerically. The maximal complex is computed by exact IIT-4.0 Φ over the reachable states, taking
the state that maximizes Φ. From that one complex three ground truths are read:

- triadic/dyadic label: triadic when the core has three or more nodes, dyadic when it has two.
- per-node membership vector: 1 for an in-core node, 0 for an excluded spectator.
- bottleneck set: the argmax of the leave-one-node-out drop in major-complex Φ. Freezing node k
  to a constant and recomputing the complex gives node k's load; the argmax set is the structural
  articulation node(s). A tie marks several equally load-bearing nodes.

The ground truth does not depend on flip.

## CRQA verdicts recomputed at each flip

Flip is swept over {0.02, 0.05, 0.08, 0.12, 0.18, 0.30}. At each flip a stochastic trajectory of
400 steps (20 warm-up) is sampled for every form, repeated over 20 seeds. From each run three
CRQA verdicts are read and scored against the fixed ground truth:

- triadic/dyadic: the prominence spread (count of ordered pairwise lead-lag links above a 0.05
  prominence floor) is read against a per-node-count threshold calibrated once at the natural flip
  0.08. Triadic if the spread is at or above the threshold, dyadic otherwise. Agreement is 1 when
  the call matches the structural label.
- membership: each node's coupling centrality is read against the form's own median centrality. A
  node is called in-core when its centrality is above the median. Agreement is the fraction of
  nodes whose call matches the structural membership vector.
- bottleneck: the argmax of coupling centrality is scored against the structural argmax-drop set.
  Agreement is 1 when the behavioral argmax lies in that set.

Each verdict's agreement is averaged over the 20 seeds, then over the corpus, at each flip.

## Intrinsic update entropy

A flip-independent property of the form: the mean over nodes of the Bernoulli entropy of each
node's deterministic next-state output across the uniform state distribution. A constant column
has entropy 0; a column that is 1 in exactly half the states has entropy 1. This measures how
balanced the form's truth-table columns are, set by the rule, not by the analyst's flip rate.

## Optimum and correlation

For each form the optimal flip is the swept rate maximizing the mean of the three verdict
agreements. The Spearman rank correlation between the per-form optimal flip and the intrinsic
update entropy tests H2.

## Determinism

Every trajectory uses `numpy.random.default_rng(seed)` over a fixed seed loop, and the Φ library
seeds its state search with `numpy.random.default_rng(0)`. Two runs produce byte-identical output.

## Instrument control

The worker-system-counterpart triad `[x[1], x[0]&x[2], x[1]]` with labels (W, S, C) reads
structurally triadic with max_phi 2.0 and a full {W, S, C} core, and its coupling-centrality
argmax at the natural flip is the mediator S (node 1). The probe asserts all four and prints
`CONTROL ... PASS` before computing the study.

## Scope

Exact IIT-4.0 Φ on small synthetic Boolean coordination forms. "Verdict", "membership",
"bottleneck", "coupling centrality", and "update noise" name graph-and-Φ quantities. The CRQA arm
runs on synthetic trajectories, so every agreement rate is a synthetic-data baseline. No field
organization is measured.
