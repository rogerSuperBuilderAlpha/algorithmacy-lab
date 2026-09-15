# Spanning mediator atop multi-hub — findings

**Verdict: WIN.** An extra top mediator on a symmetric multi-hub does **not**
raise Φ beyond the pool ceiling. Under recurrent hub-span it **recreates the
shared-mediator merge pattern** for membership (T + hubs + leaves in one major
complex) at the multi-hub Φ level, not a leap past the pool. Full span of every
node can **saturate** the pool (Φ = 12 at n=4, 20 at n=5) without exceeding it.
Feedforward-only tops drop out of the complex.

In-silico; binary exact IIT-4.0; n≤5. Hypotheses fixed in `hypotheses.md`.
Extends q145 / #119; cites `two_triad_shared_member` (shared-S AND Φ=4.0) and
`mediator_hierarchy_census` (closure decides locus). Ternary TOOLING_GAP /
residual-cascade noted only.

## Already known

| prior | result |
|---|---|
| q145 spanning mediator | full span holds all; Φ = n−1; partial caps at span+1 |
| #119 sym_multihub | Φ rises with hub count toward the pool |
| two_triad shared-S AND | five-node merge at Φ = 4.0 |
| hierarchy census | recurrent spans levels; feedforward top-local |

## Census

| cell | n | whole Φ_MIP | major complex | core Φ | vs pool |
|---|---:|---:|---|---:|---|
| pool | 4 | 12.0 | full | **12.0** | ceiling |
| pool | 5 | 20.0 | full | **20.0** | ceiling |
| mh(4,2) | 4 | 4.0 | (H0,H1,P1) | 6.0 | below |
| mh(5,2) | 5 | 6.0 | full hubs+parties | 6.0 | below |
| shared_S_AND | 5 | 4.0 | (W1,C1,W2,C2,S) | **4.0** | merge ref |
| **span_recurrent 2h2p** | 5 | 6.0 | **(T,H0,H1,P0,P1)** | **6.0** | below; full merge |
| span_ff 2h2p | 5 | 0.0 | (H0,H1,P1) | 6.0 | T excluded |
| span_full 2h1p | 4 | 12.0 | full | **12.0** | = pool |
| span_full 3h1p | 5 | 20.0 | full | **20.0** | = pool |
| span_recurrent 2h1p / 3h1p | 4/5 | 4.0/6.0 | hubs+leaf, **T out** | 6.0/12.0 | below |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 control + pool ceilings + shared-S Φ=4.0 | **SUPPORTED** |
| H2 multi-hub below pool | **SUPPORTED** |
| H3 spanning ≤ pool at same n | **SUPPORTED** |
| H4 recurrent 2h2p merges T+hubs+leaves | **SUPPORTED** |
| H5 feedforward top excluded from core | **SUPPORTED** |
| H6 full span reaches pool, does not exceed | **SUPPORTED** |

## Reading

**Beyond the pool?** No. Every spanning cell sits at or below the same-n pool.
The pool remains the ceiling for this family (#119 stands).

**Shared-mediator merge analogy?** Partial yes on the primary cell: recurrent
hub-span at 2 hubs + 2 parties puts T, both hubs, and both parties in one
major complex — the same membership move as shared-S AND. Core Φ = 6.0 matches
same-size `mh(5,2)`, not a jump past the pool and not the Φ=4.0 magnitude of
the flat shared-S merge. On thinner cells (2h1p, 3h1p) the recurrent top is
**excluded** from the core while hubs+leaf stay irreducible — membership merge
is not automatic for every hub/party count.

**Full span.** When T reads every node and every node reads T, the form can
hit the pool exactly (2h1p → 12; 3h1p → 20). That is saturation of the
all-required coupling budget, not a new law above it.

**Feedforward.** A top that only reads hubs never enters the complex (whole
Φ_MIP = 0); integration stays in the multi-hub base — same closure lesson as
the hierarchy census.

## Limits

Exact Φ only through n=5. No claim about real organizations. Pool comparison
is same-n Boolean forms, not asymptotic.

## Best next experiment

**Done next:** `small_world_vs_hierarchy/` (agenda #17) — PICK_ONE; interiors
collapse; no combine of ring cap with hub growth. Follow-on: interior topology
between ring and pool (#19).

## Reproduce

```
python org_frontier/studies/spanning_mediator_multihub/analyze_spanning_multihub.py
```
(~45s)
