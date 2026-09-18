# party_vs_mediator_noise — hypotheses (fixed before computing)

**Question (agenda #7).** Does intrinsic noise in the parties (not the
mediator) collapse the triad at a different threshold than mediator
noise?

**Already known (cited, not reopened).**
- #6 `commit_noise_phase/` — **SMOOTH_DECAY** under hub/mediator
  commit noise (pointer only).
- #27 / #38 reliability; Q7
  (`questions/q7_party_vs_mediator_noise/`) on the mediated AND triad.
- Estimation / construct / omit / ladder closed.

**Noise model (fixed).** Same flip-noise as #6:
`P(out=1)=(1−p)·clean+p·(1−clean)` on selected TPM column(s).
p ∈ {0.00, 0.01, …, 0.50}. Exact binary IIT-4.0 Φ.

**Forms (same as #6; candid N).**
1. **conjunctive_hub** n=3 — S′=P1∧P2, Pi′=S. Clean Φ=2.0.
2. **parity_hub** n=3 — S′=P1⊕P2, Pi′=S. Clean Φ=0.5.

**Loci.**
- **mediator** — hub column S.
- **party** — single party column P1 (P2 checked for symmetry).

**Collapse threshold p*.** First grid p with structure=dyadic
(Φ≤PHI_EPS).

## H1 — thresholds differ

On some family, |p*_party − p*_mediator| ≥ **0.02**.

Null: |Δp*| < 0.02 on every family.

## H2 — same threshold

On **both** families, p*_party = p*_mediator (exact on the grid).

Null: some family has unequal collapse points.

## H3 — different effect on n_core vs Φ

Even when H2 holds: on some family, either (a) max interior
|Φ_party(p)−Φ_mediator(p)| ≥ **0.15·Φ(0)**, or (b) n_core differs
between loci at some interior p < 0.5.

Null: Φ curves agree within 0.15·Φ(0) and n_core schedules match
whenever thresholds match.

**Primary verdict word.**
- H1 → `THRESHOLDS_DIFFER`
- else H2 and H3 → `SAME_THRESHOLD_DIFF_CURVE`
- else H2 and not H3 → `LOCUS_INDIFFERENT`
- else → `LOCUS_MIXED`
