# Q215 findings — binding is measure-robust; the subtle factorings belong to IIT 4.0

Two of five hypotheses confirmed, three refuted, and the refutations sort by a clean rule. Every
verdict of **binds** replicates across the Φ family: the quorum extremes, the rotation, and the full
dispatch triad carry positive Φ under both IIT 4.0 (`new_big_phi`) and IIT 3.0 (`pyphi.compute`,
`DIRECTED_BI` partitions), as do both instrument controls. Every *disagreement* runs one way: IIT 3.0
assigns positive Φ to forms where the 4.0 minimum-information partition finds a costless cut. The
factorings that carry the OT manuscript's "connection is not constitution" argument — the interior
quorum, the lockstep veto, the maximally-wired triad — are properties of the 4.0 measure, not of the
Φ family.

| form | 4.0 Φmax | 3.0 Φmax | sign |
|---|---|---|---|
| CTRL+ read-recipient triad | 2.000 | 3.500 | agree (binds) |
| CTRL− two disjoint dyads | 0.000 | 0.000 | agree (factors) |
| E1 quorum 1-of-3 | 3.000 | 6.250 | agree (binds) |
| E2 quorum 2-of-3 | **0.000** | **1.269** | **split** |
| E3 quorum 3-of-3 | 3.000 | 6.250 | agree (binds) |
| E4 rotation (4-cycle) | 2.000 | 2.000 | agree (binds) |
| E5 one-sided veto (lockstep) | **0.000** | **1.415** | **split** |
| E6 dispatch, full triad | 2.000 | 2.415 | agree (binds) |
| E7 dispatch, rider dropped | 0.000 | 0.000 | agree (factors) |
| E8 maximal wiring | **0.000** | **0.692** | **split** |

| H | Claim | Verdict |
|---|---|---|
| H1 | quorum extremes law measure-robust | **refuted** (k=2 splits) |
| H2 | rotation binds in both | confirmed |
| H3 | synchronization factoring measure-robust | **refuted** |
| H4 | dispatch pair measure-robust in both directions | confirmed |
| H5 | maximal wiring factors in both, every state | **refuted** |

From `probe_phi_family_robustness.py`; per-state values in `results/phi_family.csv`.

## What it says

The two measures agree wherever the verdict is driven by gross structure: joint reads that bind
(positive verdicts), and factorings by literal disconnection (the disjoint dyads) or by a party the
determination ignores (the dropped rider). They part company on exactly the three forms whose
factoring is *subtle* — substitutability at an interior threshold, synchronization freezing a wired
party, dense wiring without joint determination. On those forms IIT 3.0 registers residual
mechanism-level irreducibility as positive system Φ, while the 4.0 minimum-information partition
finds a party-respecting cut that loses nothing.

This is consistent with the known character of the two formalisms: IIT 3.0's Φ is famously generous
to connected systems, and IIT 4.0's revised system-level partition returns zero far more readily.
For the constitution criterion the direction of the disagreement is the substance. A criterion needs
zeros — a measure that calls nearly every connected system a whole cannot separate configurations
from aggregates — and the zeros that do the criterion's distinctive work come from the 4.0 partition
scheme specifically. The manuscript should say so: the borrowed criterion is IIT 4.0's
minimum-information partition, chosen because its partition family includes the cuts that test
substitutability; verdicts of *binds* are robust across the family, and verdicts of *factors* beyond
the trivial cases are claims about that measure.

## Scope

Eight forms and two controls, 3–4 nodes, deterministic Boolean rules, whole-system Φ maximized over
reachable states, one 3.0 configuration (`DIRECTED_BI`, sequential). No claim about other members of
the wider Φ family (stochastic measures, 2.0, geometric variants), other partition schemes for 3.0,
or larger systems.

## Instrument note

Two configuration facts this dev build required, recorded for reuse: `config.PARALLEL = False` alone
does not make the 3.0 pipeline sequential (`_ces`/`_sia_map_reduce` pass the `PARALLEL_*_EVALUATION`
mapping itself as the truthy `parallel` flag, demanding ray); setting the three `PARALLEL_*_EVALUATION`
options to `{}` runs in-process. And the 3.0 pipeline requires `SYSTEM_PARTITION_TYPE='DIRECTED_BI'`
(the global default is 4.0's `SET_UNI/BI`), applied here per-call via `config.override`.
