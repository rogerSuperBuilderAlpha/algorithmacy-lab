# fixed_k_atoms_n5 — hypotheses (fixed before computing)

**Question.** Are the n=5 random-coupling atoms Φ=5 and Φ=9 **rare outliers**,
**new discrete rungs**, or the start of a **continuum**?

**Already known.**
- **n=4 ensemble:** DISCRETE_LANDMARKS — every Φ ∈ {2,4,6,12}.
- **n=5 ensemble (PARTIAL_N5):** 92 samples, 95.7% on L5={2,3,4,6,8,12,20};
  off-landmark **5.0** (×3) and **9.0** (×1), all from `fixed_k=3`.
- **Four outliers reconstructed:** all mean_degree=6, clustering=1. The Φ=9
  form has an omit-function that is a **derangement** (each node omits a unique
  other); the three Φ=5 forms have non-bijective omits and **4-node** cores.
- **`interior_ring_pool`:** designed n=5 landmarks; chord c=3 at n=6 gave Φ=9.
- Ternary / residual-cascade noted only.

**Structural fact used.** At n=5, fixed_k=3 ⇔ each node omits exactly one other
(in-degree 3 of 4 possible). Omit functions with no fixed points that are
bijective are the **derangements** of 5 (!5 = 44).

**Universe.** Binary exact IIT-4.0. Conjunctive AND. Primary: full enumeration
of 44 derangement omits + denser non-derangement fixed_k=3 sample + fixed_k=2
contrast. Candid: derangement arm ~4 min; total ~10–12 min.

## H1 — atom 9 is a derangement rung

Every derangement-omit fixed_k=3 form at n=5 has core Φ = 9.0 with full
five-node core and triadic whole. Null: some derangement yields Φ ≠ 9.

## H2 — atom 9 is derangement-specific

In the non-derangement fixed_k=3 sample, Φ = 9 never appears. Null: at least
one non-derangement sample has core Φ = 9.

## H3 — atom 5 is a recurring non-derangement atom (not a one-off)

In the non-derangement fixed_k=3 sample (N≥40), Φ = 5 appears at least twice,
and every Φ=5 case has incomplete core (n_core < 5). Null: Φ=5 absent or only
once, or a Φ=5 full-core form appears.

## H4 — no continuum under denser fixed_k=3

Among all fixed_k=3 forms in this study (derangements + non-derangement sample),
the set of distinct rounded core Φ values has size ≤ 8 and every value is in
{2,3,4,5,6,8,9,12,20} (L5 ∪ {5,9}). Null: ≥3 distinct Φ values outside that
set, or ≥12 distinct Φ values total (continuum-like spray).

## H5 — fixed_k=2 contrast stays on known atoms

Denser fixed_k=2 sample (N≥20) has on_landmark fraction ≥ 0.90 for
L5 ∪ {5,9}, and does not produce Φ=9 (derangement/k=3 phenomenon). Null:
on_landmark < 0.90 or a fixed_k=2 sample hits Φ=9.
