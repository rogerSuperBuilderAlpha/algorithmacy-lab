# ergodic_ensemble_richness — hypotheses (fixed before computing)

**Question (Ergodicity × Algorithmacy, Strand B5).** On the complete
strict-mediation Boolean family at n=3, is whole-form Φ_MIP rank-correlated
with basin entropy, and with the number of attractors?

**Already known (cited, not reopened).**
- `studies/ergodic_components_vs_phi/` — designed panel of 9 forms.
  `NO_ERGODIC_SIGNATURE`. Mean component count triadic 2.1429 vs dyadic
  2.0000 (Δ = 0.1429 < δ_c = 0.5). Mean basin entropy was higher for the
  dyadic pair. H1, H2, and H3 refuted; H4 supported.
- `corpus/population.py` — the same 256-form family. Triadic rate 9.4% on
  the census. That rate is a structural finding about the verdict. It does
  not report basin entropy or attractor counts.
- B5 in `ergodicity/AGENDA.md` is marked computable and carries no run tag.
  The designed-panel findings name this census as the open population test.

**Definitions (fixed).**
- **Ensemble.** Every form yielded by
  `org_frontier.corpus.population.enumerate_family`: 4 × 16 × 4 = 256
  strict-mediation forms, W' = f(S), C' = f(S), S' = f(W, C), no direct
  W–C edge. The agenda's wording is a random sample. At n=3 the family is
  the population, and the lab already treats that census as the n=3 result.
  This cell therefore uses the census. A draw would be a coarser reading of
  the same question, and it is not the test below.
- **Attractor / ergodic component.** A fixed point or limit cycle of the
  synchronous map, together with its basin. Component count = number of
  attractors with basin size ≥ 1. Same definition as the B1 cell
  (`ergodicity/_boolean_ergo.find_attractors`).
- **Basin entropy.** −∑_a (b_a / 2^n) log2(b_a / 2^n), n = 3, b_a the basin
  size. Same definition as `basin_entropy` in that module.
- **Φ_MIP.** Whole-form maximum over reachable states, from
  `classify_rules`. Triadic when that maximum exceeds `PHI_EPS`; dyadic
  otherwise.
- **Rank correlation.** Spearman ρ, average ranks for ties, as implemented
  by `scipy.stats.spearmanr`.
- **Permutation null.** 2000 permutations of the Φ vector against the fixed
  structural vector. Generator: `numpy.random.default_rng(7)`. One-sided
  p for a positive association:
  (1 + count of null ρ ≥ observed ρ) / 2001.
  One-sided p for a negative association:
  (1 + count of null ρ ≤ observed ρ) / 2001.
- **Margin.** |ρ| ≥ 0.20 is the pre-registered departure from "near zero"
  in the B5 falsifier. Below 0.20 the association is near zero regardless
  of p.

**Instrument gate.** Run before any ensemble comparison. Memoryless triad
(`rules_memoryless`) whole-form triadic at Φ = 2.0. Sticky mediator
(`rules_sticky`) whole-form dyadic at Φ = 0.0. Abort the census if either
gate fails. These two forms are controls. They are not extra rows in the
256.

## H1 — basin entropy tracks Φ

Spearman ρ(Φ_MIP, basin entropy) ≥ 0.20 and the positive one-sided
permutation p < 0.05.

Null: ρ < 0.20, or p ≥ 0.05.

## H2 — attractor count tracks Φ

Spearman ρ(Φ_MIP, component count) ≥ 0.20 and the positive one-sided
permutation p < 0.05.

Null: ρ < 0.20, or p ≥ 0.05.

## H3 — mean basin entropy is higher on triadic forms

Mean basin entropy of whole-form triadic forms exceeds the dyadic mean by
δ_h ≥ 0.1 bits. The same margin as B1 H2, now on the census.

Null: the difference is below 0.1, or the dyadic mean is higher. A class
with zero forms makes the contrast undefined and refutes H3.

## H4 — mean component count is higher on triadic forms

Mean component count of triadic forms exceeds the dyadic mean by
δ_c ≥ 0.5. The same margin as B1 H1, now on the census.

Null: the difference is below 0.5, or the dyadic mean is higher. A class
with zero forms refutes H4.

## H5 — the entropy association is stable across the enumeration

Split the census in enumeration order into the first 128 forms and the
last 128. H5 is supported when ρ(Φ, basin entropy) has the same sign in
both halves and both absolute values are ≥ 0.10.

Null: the signs disagree, or either half has |ρ| < 0.10. A half with
undefined ρ (no variation) refutes H5.

**Primary verdict word.** Evaluated in this order. The first match wins.
- H1 supported and H2 supported → `RICHNESS_TRACKS_PHI`
- H1 supported → `ENTROPY_ONLY`
- H2 supported → `COUNT_ONLY`
- H1 or H2 meets the negative clause (ρ ≤ −0.20 and the negative one-sided
  p < 0.05) → `NEGATIVE_ASSOCIATION`
- else → `NO_ENSEMBLE_LINK`

H3, H4, and H5 are printed as supported or refuted. They do not change the
primary word.

**Scope.** Exact binary IIT-4.0. The 256-form strict-mediation census at
n=3. In-silico evidence about those models. No organization is measured.
No coefficient from this cell exists until the analysis script is written
after this file and then run.
