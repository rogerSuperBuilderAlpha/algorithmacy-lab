# encoding_ladder_n6 — hypotheses (fixed before computing)

**Question.** At n=6, does the encoding ladder flip with Φ tracking
n−1 (=5), or does the boundary morph relative to n=5 FULL_JOINT_FLIP?

**Already known (`encoding_ladder_n5` FULL_JOINT_FLIP).**
- Assist grows core 2→3→4 with dyadic wholes; core Φ can hit 3 pre-flip.
- Boundary step: `workers_AND_Cidle → algo_full_AND` → whole triadic,
  n_core=5, Φ=4 (= n−1).
- COMMIT_READ_BOUNDARY: party ∈ core iff in S’s determination ∧ reads S.

**Universe.** Binary exact IIT-4.0. Labels
`("W1","S","W2","W3","W4","C")`. Conjunctive AND (OR at the flip).
Designed encoding ladder — reuse n=5 rung names; add one assist rung
(+W4). Honest N (n=6; full-bind cells ~40 s). Report whole
structure/Φ_MIP and major complex (core, Φ, n_core).

**Proposed ladder order.**
1. Classical HMC — 2-core.
2. Assist +W2 — 3-core; dyadic.
3. Assist +W2+W3 — 4-core; dyadic.
4. Assist +W2+W3+W4 — 5-core; dyadic (new rung).
5. C reads without commit — C out.
6. Broadcast literacy — 2-core.
7. Workers full-AND, C idle — pre-boundary; dyadic.
8. Full joint bind — **candidate flip** (Φ=? vs n−1).
9. Drop last party — reverse.

## Competing claims (pick one)

### H1 — flip at full joint bind with Φ = n−1

S = conjunction (or disjunction) of **all** outer parties, each reading S,
yields whole **triadic**, n_core=6, core Φ = 5 (= n−1). Pre-boundary
(workers bound, C idle) stays dyadic. Assist path expands core stepwise
without flipping. Boundary step same form as n=5. Null: Φ ≠ 5, or flip
earlier, or n_core < 6.

### H2 — Φ saturates below n−1

Full joint bind flips to whole triadic with all parties in core, but
core Φ < 5 (saturates). Null: Φ = 5.

### H3 — assist path or boundary step morphs at n=6

Either (a) some assist rung before full bind is already whole-triadic, or
(b) the pre-boundary form is already algorithmacy, or (c) commit/read
membership no longer tracks core (COMMIT_READ_BOUNDARY fails). Null:
same boundary form as n=5; COMMIT_READ holds.
