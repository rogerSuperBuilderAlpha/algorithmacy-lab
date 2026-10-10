# Methods — B5 census (fixed before the script)

Each hypothesis has one decision rule. The script that implements these
rules is written after this file is committed, and it is run after that
second commit.

## Instrument

`instrument_gates()` from `org_frontier.ergodicity._boolean_ergo`.
Pass condition: memoryless structure `triadic` and max Φ = 2.0 within
1e-6; sticky structure `dyadic` and max Φ = 0.0 within 1e-6. Any failure
exits before the census loop.

## Ensemble

`enumerate_family()` in `org_frontier.corpus.population`. 256 forms.
Labels `("W", "S", "C")`. For each form:

- whole-form verdict and max Φ from `classify_rules`
- attractors from `find_attractors(next_map(rules))`
- basin entropy from `basin_entropy` on those basin sizes at n = 3

Rows are written to `results/forms.csv` in enumeration order. The script
prints one summary block. Registered CI strings are taken from that
block after the run, not before it.

## Statistics

Spearman ρ via `scipy.stats.spearmanr` on the 256-vector of max Φ against
basin entropy (H1) and against component count (H2).

Permutation: `numpy.random.default_rng(7)`, 2000 shuffles of the Φ
vector, structural vector held fixed. p formulas are in `hypotheses.md`.

Class means for H3 and H4 use the whole-form structure label. Difference
is triadic mean minus dyadic mean.

H5 splits `forms.csv` order at row 128.

## Decision lines the script must print

The words are fixed here. The coefficients are filled by the run.

```
H1 (basin entropy tracks Φ):     SUPPORTED|REFUTED
H2 (attractor count tracks Φ):   SUPPORTED|REFUTED
H3 (entropy mean tracks triadic):SUPPORTED|REFUTED
H4 (count mean tracks triadic):  SUPPORTED|REFUTED
H5 (split-half entropy ρ):       SUPPORTED|REFUTED
verdict: RICHNESS_TRACKS_PHI|ENTROPY_ONLY|COUNT_ONLY|NEGATIVE_ASSOCIATION|NO_ENSEMBLE_LINK
```

The instrument lines match the B1 cell:

```
memoryless whole: triadic Φ=2.000000  PASS
sticky whole:     dyadic Φ=0.000000  PASS
```

## What this file does not authorize

Changing ρ = 0.20, δ_h, δ_c, the seed, the permutation count, the split
point, or the verdict order after seeing the census.
