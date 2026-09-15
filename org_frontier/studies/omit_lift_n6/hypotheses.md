# omit_lift_n6 — hypotheses (fixed before computing)

**Question.** Do the n=5 omit laws — (i) derangement ⇒ single Φ rung, (ii)
3-cycle motif M ⇒ incomplete-core Φ vs cycle-siblings — **hold**, **break**,
or **morph** at n=6 under fixed_k=4 (one omit per node)?

**Already known.**
- **n=5 fixed_k=3:** derangements (!5=44) all Φ=9 full-core; motif M
  (indeg (0,1,1,1,2)+3-cycle+recip=0) ⇒ Φ=5, n_core=4; same-indeg siblings ⇒ Φ=6.
- **`interior_ring_pool` n=6 landmarks:** ring 4, pool 30, interiors 6/8/9/12.
- Exploratory probes (design only, not the registered run) suggested
  derangement cycle types may split and M3 may not separate siblings — this
  study tests that formally.
- Ternary / residual-cascade noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6, fixed_k=4 ⇔ each
node omits exactly one other. !6=265 derangements — sample + designed cycle
types (not full enum; ~45s/cell). Motif lift M3: indeg (0,1,1,1,1,2)+3-cycle+recip=0.

## H1 — single derangement rung (n=5 style)

Every tested derangement (designed cycle types + random sample) shares one
common core Φ with full n_core=6. Null: at least two distinct derangement Φ
values.

## H2 — derangement Φ tracks cycle type

Designed derangements with cycle type 3+3 differ in core Φ from cycle types
{6}, {4,2}, and {2,2,2}. Null: all four designed types share one Φ.

## H3 — M3 lift yields stable incomplete-core Φ

Motif M3 (indeg (0,1,1,1,1,2), cycles=(3,), recip=0) has n_core=5 and a
reproducible core Φ (uniformity: designed witness + one alternate labeling).
Null: M3 forms disagree on Φ or are full-core.

## H4 — 3-cycle sibling discriminant fails to lift

At least one same-indeg sibling of M3 (cycles ≠ (3,) or recip>0) has the
**same** core Φ as M3 (so cycle type no longer separates 5-vs-6 style).
Null: every such sibling differs from M3’s Φ (discriminant lifts cleanly).

## H5 — new atom beyond n=6 landmarks

Some tested form has core Φ outside L6={4,6,8,9,12,30}. Null: all Φ in L6.
