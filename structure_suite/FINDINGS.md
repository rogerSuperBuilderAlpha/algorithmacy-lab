# Findings: scalar Φ is nearly orthogonal to the structure it summarizes

**TL;DR.** Across 372 `(network, state)` points, **scalar Φ is almost
uncorrelated with every dimension of the cause‑effect structure it is supposed
to summarize** (rank correlations ρ = 0.07–0.21). Reducible systems (Φ = 0)
nonetheless have rich structure — *all* of them have ≥1 distinction (mean 2.8),
and many have large numbers of relations. Systems with the same Φ (most starkly,
the same Φ = 0) span the full observed range of structural complexity. This is
direct, quantitative support for Barrett et al. (2026)'s proposal that a single
Φ should be replaced by a multi‑dimensional suite: **Φ is just one axis, nearly
independent of the others.**

## 1. Φ is its own axis

Rank correlation of each structural dimension with scalar Φ:

| Dimension | ρ with Φ |
|-----------|-----:|
| # distinctions | 0.21 |
| Σφ distinctions | 0.12 |
| # relations | 0.12 |
| Σφ relations | 0.07 |
| mean / max mechanism order | 0.21 |
| frac order ≥ 2 | 0.21 |

Every structural dimension is **almost orthogonal to Φ**. Meanwhile the
structural dimensions are strongly correlated *with each other* — the
mechanism‑order measures co‑move at ρ ≈ 0.99, and # distinctions ↔ # relations
at ρ ≈ 0.89 — so the suite collapses to roughly **three independent axes**:
scalar Φ, structural *size* (distinctions/relations), and *composition*
(mechanism order). Φ captures only the first. (See `suite_corr.png`.)

## 2. Φ = 0 does not mean "no structure"

Of the 372 points, 342 are reducible (Φ = 0). Among them:

- **# distinctions:** mean 2.8, max 12 — **100% have ≥1 distinction.**
- **# relations:** mean 22.6, with a heavy tail.

So a system IIT scores as *not an integrated complex* can still possess an
elaborate cause‑effect structure. The scalar collapses that to "0."

## 3. Same Φ, different structure

Structural spread within Φ bands:

| Φ band | n | # distinctions | # relations |
|--------|--:|------|------|
| Φ = 0 | 342 | 0 – 12 | 0 – (heavy tail) |
| 0 < Φ < 0.2 | 5 | 5 – 6 | 19 – 61 |
| 0.2 ≤ Φ < 0.5 | 6 | 3 – 10 | 1 – 338 |
| Φ ≥ 0.5 | 19 | 2 – 6 | 1 – 39 |

Knowing Φ pins down the structure only loosely; at fixed Φ the structure still
varies widely. (See `phi_vs_structure.png`.)

## Interpretation

The cause‑effect structure has several genuinely independent degrees of freedom
— *how much* irreducible structure (distinctions/relations), *how higher‑order*
it is (composition), and *how integrated* it is (Φ). Reporting only Φ discards
the first two. This is exactly the multi‑dimensional characterization Barrett et
al. advocate, and these data show the dimensions really are non‑redundant on
concrete systems.

## Caveats

- **Ensemble is Φ>0‑poor** (30 / 372). Random small Boolean networks rarely form
  integrated complexes (consistent with the proxy/candidate audits). The
  "Φ = 0 has structure" and "Φ⊥structure" findings rest on a large sample; the
  graded "same Φ>0, different structure" claim rests on a smaller one.
- **Distinction‑level dimensions are exact**; the **relation counts carry a
  caveat** — PyPhi emits a warning that for states with no resolved system state
  (largely the Φ = 0 cases) relations are computed before congruence resolution,
  which can inflate `n_relations` / `sum_phi_relations`. The qualitative claims
  rely on distinctions (exact) and on relations only as a secondary illustration;
  the extreme relation counts (e.g. the 4091 tail) should be read with this in
  mind.
- Small systems (`n ∈ {3,4}`), specific Boolean‑gate ensemble.

## Reproduce

`python -m structure_suite.run 1 && python -m structure_suite.analyze`
