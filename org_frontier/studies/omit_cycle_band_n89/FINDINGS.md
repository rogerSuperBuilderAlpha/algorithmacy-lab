# Omit cycle band grammar at n=8–9 — findings

**Verdict: SCALE_BLOCKS_EXACT_PHI.** The omit/cycle **band grammar**
that stabilized at n=7 cannot be re-adjudicated by exact IIT-4.0 core-Φ
at n=8–9 under the lab stack. The indeg-lift **cycle-type catalog
expands** (10 → 14 → 21 classes; new lengths such as `(7,)`, `(8,)`,
pairs like `(3,4)`), so more cycle types do fit — the occasion for a
morph is present — but dense-state major-complex Φ at n=8 exceeds the
session budget (sparse reachable states return Φ=0). n=7
`BAND_GRAMMAR_HOLDS` stands unrebutted; hold vs morph at n=8–9 is
**not decided** by exact Φ here.

In-silico; exact binary IIT-4.0 where computed. Hypotheses fixed in
`hypotheses.md`. Answers RESEARCH_AGENDA_V4 #8. Extends V3 #8
`BAND_GRAMMAR_HOLDS` and V2 #42 `SCALE_MORPHS`.

**Scope.** Lean panel: n=7 committed designed census (control) + MC
cycle-type catalogs under indeg `(0,1,…,1,2)` at n=7/8/9 + attempted
n=8 all-1 exact micro panel. Full designed+uniformity census at n=8–9
is intractable (n=7 cells were 7–24 min; n=8 dense-state
`maximal_complex` does not finish within budget).

## Already known

| prior | result |
|---|---|
| V3 #8 omit_cycle_morph_n7 | BAND_GRAMMAR_HOLDS — Φ=12 vs 14 class-pure bands |
| V2 #42 discriminant_scale_blur | SCALE_MORPHS — singleton→band across n=5→n=6 |
| n=5 / n=6 omit bands | singleton then multi-class band |

## Results

| probe | result |
|---|---|
| n=7 control Φ bands | **{12, 14}** class-pure (10 designed classes) |
| MC classes n=7 / 8 / 9 | **10 / 14 / 21** |
| new cycle types at n=8 | `(7,)`, `(2,5)`, `(3,4)`, `(2,2,3)` |
| new cycle types at n=9 | `(8,)`, `(2,6)`, `(3,5)`, `(4,4)`, … |
| n=8 exact micro (all-1) | **not adjudicable** (budget / timeout) |
| n=8 sparse-state Φ | 0.0 (null) |

## Hypotheses

| H | result |
|---|---|
| H1 n=7 control replicates BAND_GRAMMAR_HOLDS | **SUPPORTED** |
| H2 class count grows n7 < n8 < n9 | **SUPPORTED** |
| H3 n=8 exact micro adjudicable | **REFUTED** |
| H4 band grammar holds at n=8 \| H3 | **REFUTED** (vacuous) |
| H5 n=9 consistent \| budget | **REFUTED** (not attempted) |

## Reading

Scale, not a new measured morph, is the binding constraint. More omit
cycle types fit at n=8–9 — the combinatorial precondition the agenda
named — but exact core-Φ band purity cannot be scored on the conjunctive
omit family with the current major-complex path. Practice: do not treat
n=7 band grammar as automatically exported to n=8–9 without either a
faster exact engine or an explicitly scoped approximation policy; do
treat the unrebutted n=7 grammar as the last settled omit-band claim.

## Best next (V4)

**#9** — does V3 #10’s parity-hub law Φ=2^(2−n) continue for **n>8**, or
does the closed form break when reachability / MIP sampling bites?

## Reproduce

```
python org_frontier/studies/omit_cycle_band_n89/analyze_band_n89.py
```
