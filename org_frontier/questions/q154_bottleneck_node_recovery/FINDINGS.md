# q154 — Findings

Coupling centrality does not recover the node exact-Φ marks as the form's articulation point. On the
two forms with a unique structural bottleneck it lands on the right node 28.3% of the time, near the
25% chance rate and far below the 70% the hypothesis fixed. Transfer-entropy throughput does better,
66.7% on the same forms, so the cheaper directed-information picker beats coupling centrality here.

| form | base_Φ | loo_drops | gt_set | unique | cc_rec | te_rec |
|---|---|---|---|---|---|---|
| ats_strict_bottleneck | 2.00 | [2.0, 2.0, 2.0] | [0, 1, 2] | False | 30/30 | 30/30 |
| joint_bottleneck | 2.00 | [0.0, 2.0, 0.0, 0.0] | [1] | True | 0/30 | 24/30 |
| degree_bottleneck | 2.00 | [2.0, 0.0, 0.0, 0.0] | [0] | True | 17/30 | 16/30 |

Pooled recovery, unique-articulation forms: coupling centrality 28.3%, TE throughput 66.7%.
Pooled recovery, all forms: coupling centrality 52.2%, TE throughput 77.8%.

The `ats_strict_bottleneck` row carries no recovery test. Its AND mediator dies when any input is
frozen, so all three nodes tie for the largest drop and every node is an articulation point. A tied
ground-truth set makes recovery automatic (30/30 for both pickers) and uninformative. The result
rests on the two forms with a single articulation point.

The control behaves: on a degree-matched XOR-ring with equal load on every node, the behavioral
picks spread across all four nodes (max single-node share: cc 37%, te 30%, against 25% chance). The
pickers invent no bottleneck where the structure has none. The failure on the bottleneck forms is a
failure to find a real articulation point, not a tendency to manufacture false ones.

The split between the two unique-articulation forms is informative. On `degree_bottleneck` the
articulation node is also the high-degree node the trajectory couples to most, so coupling centrality
half-recovers it (17/30). On `joint_bottleneck` the articulation node is a hub whose behavioral
coupling is weak relative to the redundant cluster around it, and coupling centrality never finds it
(0/30) while throughput usually does (24/30). Structural load and behavioral prominence come apart
when the load-bearing node is quiet.

## Verdicts

- H1 (coupling centrality recovers the bottleneck in >70% of seeded runs): **REFUTED**. 28.3% on
  unique-articulation forms, near the 25% chance rate.
- H2 (coupling centrality beats TE throughput): **NOT SUPPORTED**. Coupling centrality 28.3% trails
  TE throughput 66.7%; the null that throughput matches or beats it holds.

## Scope

Exact IIT-4.0 Φ on small Boolean forms. The bottleneck, the freezing ablation, and the centrality and
throughput readings are graph-and-Φ quantities, not measured organizations. The empirical arms run on
synthetic trajectories, so the recovery rates are baselines on synthetic data. The Φ-to-organization
bridge is open.
