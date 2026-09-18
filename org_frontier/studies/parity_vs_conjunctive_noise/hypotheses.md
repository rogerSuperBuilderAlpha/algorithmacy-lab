# parity_vs_conjunctive_noise — hypotheses (fixed before computing)

**Question (agenda #8).** Under noise, does the parity hub (which
decays as 2^(2−n), #115) lose its verdict faster than the conjunctive
hub at the same size?

**Already known (cited, not reopened).**
- #6 `commit_noise_phase/` — **SMOOTH_DECAY** (pointer only).
- #7 `party_vs_mediator_noise/` — **SAME_THRESHOLD_DIFF_CURVE**
  (pointer only).
- #115 parity scaling Φ=2^(2−n); Q8 prior on n=3/4 hub flip-noise.
- Estimation / construct / omit / ladder closed.

**Noise model (fixed).** Hub-column flip-noise as in #6/#7:
`P(out=1)=(1−p)·clean+p·(1−clean)` on S. p ∈ {0.00, 0.01, …, 0.50}.
Exact binary IIT-4.0 Φ.

**Forms (matched n; candid N).**
- **conjunctive_hub** at n=3,4 — S′=AND(parties); Pi′=S. Clean Φ=n−1.
- **parity_hub** at n=3,4 — S′=XOR(parties); Pi′=S. Clean Φ=2^(2−n).

**Collapse threshold p*.** First grid p with structure=dyadic.
**Normalized Φ̂(p)=Φ(p)/Φ(0).**

## H1 — parity loses verdict sooner

At some matched n, p*_parity ≤ p*_conjunctive − **0.02**.

Null: no such gap at n=3 or n=4.

## H2 — same p*

At **both** n=3 and n=4, p*_parity = p*_conjunctive (exact on grid).

Null: thresholds differ at some size.

## H3 — Φ decays faster for parity; verdict matches

H2 holds, and at each size, Φ̂_parity(p) < Φ̂_conjunctive(p) on at
least **half** of interior grid points (parity sheds a larger fraction
of clean Φ).

Null: same p* but parity is not the faster normalized decay (ties or
conjunctive sheds more).

**Primary verdict word.**
- H1 → `PARITY_FASTER_FLIP`
- else H2 and H3 → `SAME_P_PARITY_FASTER_PHI`
- else H2 and not H3 → `SAME_P_STAR`
- else → `FAMILY_NOISE_MIXED`
