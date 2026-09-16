# Mediator hierarchy census — findings

**Verdict: WIN.** In recurrent AND org-chart trees the major complex **spans every
occupied level** (apex, mid if present, leaf); Φ is **flat in depth** (2.0 at
b=1) and **grows with breadth** (2→3→4 at d=1). In feedforward hub chains the
complex is **top-local** (H0,P0 only) at every tested depth. **Closure decides
the level locus**; depth vs breadth scaling replicates q144.

In-silico; binary exact IIT-4.0; n≤5 recurrent, n≤6 hub-chain. Hypotheses fixed
in `hypotheses.md`. Extends q144 / q148 / multiparty chains; cites
`two_triad_shared_member` (shared mediator merges). Ternary TOOLING_GAP noted
only (`shared_mediator_ternary/`). Residual/cascade not reopened.

## Already known

| prior | result |
|---|---|
| q144 recurrent AND trees | Φ flat in depth; grows in breadth; cores whole-tree |
| q148 feedforward hub chains | core = top hub+party only; break at first seam |
| multiparty/chains | W→…→C stays triadic Φ=2.0 |

## Census (level-tagged)

| family | cell | n | core Φ | core levels | note |
|---|---|---:|---:|---|---|
| recurrent depth | d=1..4, b=1 | 2–5 | **2.0** | all occupied | flat |
| recurrent breadth | d=1, b=2..4 | 3–5 | **2,3,4** | apex+leaf | grows |
| recurrent crossed | d=2,b=2 trunc. | 5 | 2.0 | apex+mid+leaf | one branch (S0,S2,L2) |
| hub chain | L=2,3 | 4,6 | 2.0 | apex+leaf (H0,P0) | **top-local** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 depth flat Φ=2.0 (q144) | **SUPPORTED** |
| H2 breadth Φ increases (q144) | **SUPPORTED** |
| H3 recurrent spans all occupied levels | **SUPPORTED** |
| H4 feedforward hub-chain top-local | **SUPPORTED** |
| H5 closure decides level locus | **SUPPORTED** |

## Reading

**Which level holds the complex?** Under recurrent leaf↔apex closure, every
level that exists appears in the major complex — depth does not push integration
into the apex alone. Under feedforward hub-to-hub AND seams, integration stays
at the **top loop**; mid and downstream parties drop (q148). The crossed
recurrent cell (n=5) still places apex, mid, and leaf tags in the core, but on
**one branch** only (S0–S2–L2), not both mids — level span ≠ full horizontal
span.

**Depth vs breadth.** Depth is a serial bottleneck (Φ=2.0). Breadth adds
integration roughly one Φ unit per added leaf at d=1 (linear on this grid),
matching q144 and short of a fully-coupled pool.

## Best next experiment

**Done next:** `spanning_mediator_multihub/` (agenda #20) — spanning top does
not beat the pool; recurrent hub-span merges membership like shared-S.
Follow-on: small-world rewire vs hierarchy (#17) at fixed n.

## Reproduce

```
python org_frontier/studies/mediator_hierarchy_census/analyze_hierarchy.py
```
(~2 min; deepest recurrent cell n=5 ~85s)
