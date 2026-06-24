# q154 — Methods

## Forms

Three named bottleneck forms, each a per-node Boolean rule list over the little-endian current-state
tuple, with the articulation node placed at a different index so a recovery is not a positional
artifact.

- `ats_strict_bottleneck` (n=3): the canonical strict mediator `[x1, x0 & x2, x1]`, labels (W, S, C).
- `joint_bottleneck` (n=4): a hub (node 1) bridges one party (node 0) to a redundant cluster
  (nodes 2, 3). The cluster's internal redundancy keeps the integration alive when 0, 2, or 3 is
  frozen; freezing the hub collapses it.
- `degree_bottleneck` (n=4): a high-degree connector (node 0) read by two parties with a back-up
  read of node 3. Freezing the connector collapses the complex; the periphery does not.

## Structural ground truth

For each form, freeze node k to the constant 0 and recompute the maximal complex over reachable
states with `org_frontier.probes.lib.major_complex`. Node k's load is `base_Φ − Φ(freeze k)`. The
ground-truth bottleneck set is the argmax of the loads. A single index is a unique articulation
point; several tied indices mean the nodes carry the irreducibility equally. A tied set makes
recovery automatic, so the unique-articulation subset is the test that decides H1 and H2.

## Behavioral pickers

For each of 30 seeds, `crqa.trajectory` samples a 400-step run (flip 0.05, warmup 20) from the form.
Two argmax picks are read: `coupling_centrality` (summed prominent CRQA coupling per node) and
TE-throughput (per node, the sum of `transfer_entropy` in and out over all partners). A run is a
recovery when the behavioral argmax lies in the ground-truth set. Recovery rates are pooled over all
forms and over the unique-articulation subset.

## Control

A degree-matched symmetric XOR-ring of four nodes, each reading its two ring neighbours. Every node
has the same degree and the same Φ load, so no node is an articulation point. The behavioral pickers
must spread across the four nodes rather than concentrate on one.

## Determinism

Every trajectory uses `numpy.random.default_rng(seed)` over a fixed seed loop, and the Φ library
seeds its state search with `numpy.random.default_rng(0)`. Three consecutive runs are byte-identical.

## Reuse

The probe imports `verdict`, `major_complex` (`org_frontier.probes.lib`), `trajectory`,
`coupling_centrality` (`org_frontier.recurrence.crqa`), and `transfer_entropy`
(`org_frontier.probes._info`). Φ is not reimplemented.

## Validation gap

Exact IIT-4.0 Φ on small Boolean forms. The freezing ablation and the centrality and throughput
quantities are graph-and-Φ readings, not field measurements. In-silico scope; the empirical arms run
on synthetic trajectories.
