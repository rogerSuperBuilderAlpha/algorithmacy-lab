# encoding_ladder_n5 — hypotheses (fixed before computing)

**Question.** At n=5, which minimal encoding edits walk classical HMC /
literacy up to algorithmacy-irreducible, and which rung is the
literacy→algorithmacy boundary?

**Already known (`hmc_algo_boundary` COMMIT_READ_BOUNDARY at n=4).**
- Party ∈ core iff in S’s determination **and** reads S.
- Assist (second human in S’s rule) → 3-core blur; whole stays dyadic.
- Full joint bind of all outer parties → whole triadic, Φ=3, n_core=4.
- Drop from commit removes the party from the core.

**Universe.** Binary exact IIT-4.0. Labels `("W1","S","W2","W3","C")`.
Conjunctive AND (OR checked at the flip). Designed encoding ladder —
minimal edits of commit / read / assist / joint-bind / idle. Honest small
N (n=5; ~0.3–5 s/cell). Report whole structure/Φ_MIP and major complex
(core, Φ, n_core).

**Proposed ladder order (rung → expected flip).**
1. Classical HMC (W1↔S; others idle) — 2-core.
2. Assist +W2 into S — 3-core; still literacy/HMC blur.
3. Assist +W2+W3 into S — 4-core; still not algorithmacy (whole dyadic).
4. C reads without commit — C stays out.
5. Broadcast literacy (S=W1; others read) — 2-core.
6. Workers full-AND, C idle — pre-boundary; still dyadic whole.
7. Full joint bind (all outer parties in S ∧ all read) — **algorithmacy flip**.
8. Drop last party from commit — reverse step.

## H1 — progressive assist expands core without flipping

Adding W2 into S’s rule (∨ or ∧) with W2 reading S yields n_core=3;
adding W3 likewise yields n_core=4. Whole structure stays dyadic at both
rungs. Null: core stays 2, or whole flips triadic before full joint bind.

## H2 — read-without-commit does not add a party

A party that reads S but is absent from S’s determination stays outside
the major complex. Broadcast (S=W1 only; others read) stays n_core=2.
Null: such a party appears in the core.

## H3 — full joint bind is the algorithmacy flip

S = conjunction (or disjunction) of **all** outer parties, each reading S,
yields whole structure **triadic** with n_core=5 and core Φ ≥ 3. Null:
still dyadic whole or incomplete core.

## H4 — removing a party from the commit drops them

From the full joint-bind form, dropping one outer party from S’s
determination (idle or read-only) removes that party from the core and
returns the whole to dyadic. Null: core membership unchanged.

## H5 — pre-boundary is not algorithmacy

Workers fully bound (S=W1∧W2∧W3, all three read) with C idle is still
dyadic whole — the literacy→algorithmacy boundary is the **last** outer
party’s commit into S, not the multi-worker assist alone. Null: that
pre-boundary form is already whole-triadic.
