# timescale_separation — hypotheses (fixed before computing)

**Question (agenda #9).** Does separation of timescales — fast parties,
slow mediator — factor the coordination the way sequential update did
(#62)?

**Already known (cited, not reopened).**
- #6–#8 stochastic noise: SMOOTH_DECAY / SAME_THRESHOLD_DIFF_CURVE /
  SAME_P_STAR (pointers only — verdict robust to flip-noise).
- #62: every triadic corpus form → dyadic under sequential
  (one-node-at-a-time) update (`probe_async.py`).
- Q9 prior (`questions/q9_timescale_separation/`): hold-for-k flips;
  prob 1/k holds. Estimation / construct / omit / ladder closed.

**Encoding (candid; two constructions).**
1. **hold-for-k (primary).** Inside one macro step, k micro-steps:
   parties update every micro-step; mediator holds for k−1 then commits
   on the k-th. Deterministic composed state-by-node TPM (Q9 methods).
2. **prob 1/k (construction check).** Mediator commits with probability
   1/k else holds; parties deterministic. Stochastic TPM.

k ∈ {1,2,3,4,5,6}. k=1 = synchronous baseline.

**Forms (designed; candid N).**
1. **conjunctive** — W'=S, S'=W∧C, C'=S (n=3; #62/#27 anchor).
2. **parity_hub** — S'=P1⊕P2, Pi'=S (n=3; small-Φ hub).

**Measures.** Φ_MIP, structure, n_core=|major complex|. #62 sequential
control on the conjunctive form (all 6 orders).

## H1 — factors like sequential (#62)

On **hold-for-k**, some k* with 1 < k* ≤ 6 where structure→dyadic and
n_core drops below the k=1 value, on at least the conjunctive form
(parity reported).

Null: no such interior flip on hold-for-k.

## H2 — verdict robust to timescale ratio

On **hold-for-k**, both forms stay triadic for all k=1…6.

Null: some form flips.

## H3 — Φ changes without verdict flip (hold-for-k)

On hold-for-k for some form: max |Φ(k)−Φ(1)| ≥ **0.15·Φ(1)** across
the grid while structure stays triadic at every k.

Null: every material Φ change co-occurs with a verdict flip, or Φ is
flat.

**Primary verdict word (hold-for-k).**
- H1 → `FACTORS_LIKE_62`
- else H2 → `TIMESCALE_ROBUST`
- else H3 → `PHI_ONLY`
- else → `TIMESCALE_MIXED`

Prob 1/k and #62 sequential are reported as witnesses, not alternate
H gates.
