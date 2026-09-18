# oscillatory_scaling — hypotheses (fixed before computing)

**Question (agenda #11).** Do oscillatory forms (limit-cycle
attractors) carry a different Φ scaling law than the fixed-point
families in the zoo (#132)?

**Already known (cited, not reopened).**
- #10 `commit_response_delay/` — **DELAY_CORE_SHIFT** (pointer only).
- #132 zoo: chain constant, AND-ring cap Φ=4 (n≥4), conjunctive hub
  Φ=n−1, pool super-linear, parity hub Φ=2^(2−n).
- Q11 prior (`questions/q11_oscillatory_scaling/`).
- Estimation / construct / omit / ladder closed.

**Oscillatory construction (candid).**
- **rot_ring(n):** pure cyclic shift — node i copies left neighbor
  `(i−1)%n`. Traveling wave; synchronous attractor period = n
  (limit cycle, not a fixed point).

**Fixed-point zoo baselines (matched n).**
- **and_ring(n)** — #132 capped ring (AND of two neighbors).
- **conjunctive_hub(n)** — Φ=n−1 landmark.
- **parity_hub(n)** — Φ=2^(2−n) landmark.

**Sizes.** n ∈ {3,4,5} (candid; n=6 deferred — exact major-complex
cost). Exact IIT-4.0 major-complex Φ; structure; attractor period.

## H1 — different Φ scaling law

rot_ring's Φ(n) sequence is **not** equal (tol 1e-6) to and_ring at
every matched n≥4, and is not the conjunctive (n−1) or parity
(2^(2−n)) landmark sequence. Separable fifth shape.

Null: rot_ring reproduces and_ring (or another zoo landmark) over n.

## H2 — same landmarks / laws

rot_ring matches and_ring Φ within 1e-6 at every n∈{4,5,6} (same cap
law), OR matches conjunctive/parity landmarks pointwise.

Null: no such match (H1's claim).

## H3 — verdict differs more than magnitude law

Across n=3..5, rot_ring and and_ring disagree on structure
(triadic/dyadic) at some n, while Φ sequences could still be close —
verdict divergence dominates.

Null: both stay the same structure class at every n (magnitude-law
question only).

**Primary verdict word.**
- H1 and not H2 → `DIFFERENT_LAW`
- H2 → `SAME_LAW`
- H3 and not H1 → `VERDICT_SPLIT`
- else → `OSC_MIXED`
