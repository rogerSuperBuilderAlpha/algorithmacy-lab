# q152 — Findings

The whole-system verdict and major-complex membership disagree on the studied catalog.
Seven of the nineteen topologies at n = 5, 6 read triadic at the whole-system level while
their major complex excludes at least one party. The two readouts are separate diagnostics.

The zero-Shapley marker does not track the disagreement. Every one of the seven disagreeing
topologies carries zero nodes with an exactly-zero Shapley value; the excluded parties have
small-positive or negative marginal contributions instead. The hub-chain forms carry
zero-Shapley nodes yet read dyadic, so they raise no triadic exclusion. The biconditional
`disagree <=> has-zero-Shapley` is false in both directions.

## Disagreeing topologies (triadic verdict, party excluded)

| topology              | n | verdict | maxΦ  | core | full | zeroShap | disagree |
|-----------------------|---|---------|-------|------|------|----------|----------|
| chain                 | 5 | triadic | 2.000 | 2    | no   | 0        | YES      |
| two_hub               | 5 | triadic | 2.000 | 4    | no   | 0        | YES      |
| sym_multihub(m=3)     | 5 | triadic | 6.000 | 4    | no   | 0        | YES      |
| chain                 | 6 | triadic | 2.000 | 2    | no   | 0        | YES      |
| two_hub               | 6 | triadic | 2.000 | 4    | no   | 0        | YES      |
| sym_multihub(m=3)     | 6 | triadic | 9.000 | 4    | no   | 0        | YES      |
| sym_multihub(m=4)     | 6 | triadic | 8.000 | 5    | no   | 0        | YES      |

Full-core triadic forms (ring, pool, single_hub, low-m sym_multihub) and the dyadic
hub-chains do not disagree. The control (worker-system-counterpart triad) reads triadic at
max_phi 2.0 with a full-party core and no zero-Shapley party.

Counts: 7/19 disagree; 0 cases where a zero-Shapley node sits inside a full triadic core;
the dyadic hub_chain(L=3,g=1,n=6) carries 6 zero-Shapley nodes without any triadic exclusion.

## Verdicts

- H1 (a triadic verdict can exclude a party): **SUPPORTED**.
- H2 (disagreement is exactly the zero-Shapley marker): **NOT SUPPORTED**.

## Scope

Exact IIT-4.0 Φ on synthetic Boolean coordination forms. In-silico only; the result is a
property of the two diagnostics on a prior catalog of topologies, not a measurement of any
empirical organization. The validation gap to field data is open.
