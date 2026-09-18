# mediator_hierarchy_census — hypotheses (fixed before computing)

**Question (agenda #15).** In a hierarchy of mediators (org-chart style), which
**level** holds the major complex, and does Φ scale by **depth** or by **breadth**?

**Already known (cited, not reopened).**
- **q144:** balanced recurrent AND trees — Φ flat in depth at chain constant 2.0;
  grows linearly in breadth at fixed depth; cores reported as whole-tree sets.
- **q148:** feedforward hub chains — major complex stays at the **top** hub+party
  at every depth; break at first hub seam.
- **multiparty/chains:** W→S1→…→Sk→C stays triadic at Φ=2.0 (depth preserves).
- **two_triad_shared_member:** shared *mediator* AND merges two triads (Φ=4.0);
  shared leaves do not. Ternary lift blocked (`shared_mediator_ternary/` TOOLING_GAP).

**Gap this census fills.** q144 answers depth/breadth scaling but does not score
**which level** holds the complex when families differ. q148 answers top-local
cores for feedforward hubs only. This study tags every node by level
(apex / mid / leaf), runs a compact exact-Φ grid on both **recurrent trees**
(q144 family) and **feedforward hub chains** (q148 family), plus one crossed
recurrent cell (depth=2, breadth=2, one leaf per mid, n=5), and asks which level
holds the complex under each closure.

**Universe.** Binary exact IIT-4.0. Primary gate: conjunctive AND. n ≤ 5 for
recurrent trees; feedforward hub chains at L=2 (n=4) and L=3 (n=6). Optional OR
contrast on one recurrent breadth cell if cheap.

## Level tags

- **apex** — top mediator / first hub
- **mid** — internal mediators (absent when depth=1)
- **leaf** — workers / parties

**Span levels** = number of distinct tags present in the major complex.
**Top-local** = core ⊆ {apex} ∪ apex's own group (feedforward), or core tags ⊆ {apex}.

## H1 — instrument + q144 depth flat

Faithful triad control. Recurrent tree depth axis (b=1, d=1..4): core Φ = 2.0
flat (replicates q144 H1).

## H2 — q144 breadth grows

Recurrent tree breadth axis (d=1, b=2..4): core Φ strictly increases with b
(replicates q144 breadth direction).

## H3 — recurrent trees: complex spans all present levels

On every recurrent-tree cell in the grid (including crossed d=2,b=2 n=5), the
major complex includes at least one node from every occupied level (apex, and
mid if present, and leaf). Null: some recurrent cell is missing a level.

## H4 — feedforward hub chains: complex is top-local

On hub-chain L=2 and L=3 (q148 family), the major complex is confined to the
top hub and its party (does not include downstream hubs/parties). Null: a
downstream hub or party enters the core.

## H5 — closure decides level locus

At comparable size, recurrent trees are multi-level spanning (H3) while
feedforward hub chains are top-local (H4). Null: both families show the same
level locus (both spanning or both top-local).
