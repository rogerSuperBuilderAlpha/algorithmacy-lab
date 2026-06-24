# q149 — findings

The mediator rent does not spread out as mediation is carried by more hubs. It concentrates. The
per-hub Shapley share stays high and rises at the most-distributed end, and in the multi-hub forms
the parties take negative Shapley value: the hubs capture more than the whole of the subsystem Φ at
the integrating state. Symmetry, by contrast, forces exact value equality.

## Hub-vs-party split (share of total Φ)

| topology       | n | hubs | Φ_total | hub_share | per_hub |
|----------------|---|------|---------|-----------|---------|
| single_hub     | 5 | 1    | 4.000   | 0.550     | 2.200   |
| sym_multihub m=2 | 5 | 2  | 6.000   | 0.683     | 2.050   |
| sym_multihub m=3 | 5 | 3  | 6.000   | 1.167     | 2.333   |
| two_hub        | 5 | 2    | 2.000   | 1.084     | 1.083   |
| single_hub     | 6 | 1    | 5.000   | 0.533     | 2.667   |
| sym_multihub m=2 | 6 | 2  | 8.000   | 0.600     | 2.400   |
| sym_multihub m=4 | 6 | 4  | 8.000   | 1.417     | 2.833   |

The per-hub share ordered by hub count is [2.20, 2.20, 2.05, 2.33] at n=5 and
[2.67, 2.67, 2.40, 2.35, 2.83] at n=6: non-monotone, and higher at the most-distributed end than at
the single hub. Where the hub share exceeds 1.0 the party sum is negative, so a party's average
marginal contribution to the integrating-state Φ is a drag, not a credit.

## Symmetric topologies (spread of node values)

| topology | n | Φ_total | spread | equal |
|----------|---|---------|--------|-------|
| ring     | 5 | 4.000   | 0.000  | True  |
| pool     | 5 | 20.000  | 0.000  | True  |
| ring     | 6 | 4.000   | 0.000  | True  |
| pool     | 6 | 30.000  | 0.000  | True  |

## Control

The read-recipient triad reads a total Φ of 2.000 with the mediator at share 0.666 (~2/3) and the two
outer parties equal at 0.333: PASS.

## Verdicts

- H1 (per-hub Shapley share falls monotonically as mediation distributes): REFUTED. Distributing
  mediation does not distribute the rent. The per-hub share does not fall, and the symmetric multi-hub
  drives the party sum negative.
- H2 (ring and pool yield equal Shapley values within tolerance): SUPPORTED. Every spread is 0.000 at
  n = 5 and n = 6.

## Scope

In-silico. Synthetic Boolean coordination forms, not measured organizations. The result describes the
behavior of the exact-Φ Shapley split across these families. It is not a measurement of value capture
in any real group.
