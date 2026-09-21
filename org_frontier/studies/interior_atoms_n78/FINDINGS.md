# Interior atoms at n=7–8 — findings

**Verdict: SPROUTS_NEW_ATOMS.** Designed ring–pool interiors at n=7 yield a
**new** full-core Φ atom (**10**) outside the n≤6 interior landmark set
{6, 8, 9, 12}, while also recalling prior atoms 6 and 12. Discrete atoms
do not merely thicken — they **sprout**.

In-silico; binary exact IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers `RESEARCH_AGENDA_V3` #9. Lean n=8 lift deferred under night
closedown (n=7 panel alone decides); ring Φ=4 for n≥4 already established.

## Already known

| prior | result |
|---|---|
| interior_ring_pool (#19) | NO_INTERMEDIATE_LAW; n=6 steps 4→6→8→9→12→30 |
| random_coupling_ensemble (#18) | DISCRETE_LANDMARKS on those atoms |
| V3 #8 omit_cycle_morph_n7 | BAND_GRAMMAR_HOLDS (omit lane; cited only) |

**L_interior_prior** = {6, 8, 9, 12}.

## n=7 designed panel

| cell | core Φ | full | band |
|---|---:|---|---|
| ring7 | **4** | yes | pole |
| pool7 | **42** | yes | pole |
| mh2_n7 | **10** | yes | **NEW interior** |
| mh3_n7 | **12** | yes | prior |
| chord_n7_c2 | 6 | no (n_core=5) | incomplete |
| chord_n7_c3 | **6** | yes | prior |
| kreg_n7_d2 | **12** | yes | prior |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 anchors ring7=4 / pool7=42 | **SUPPORTED** |
| H2 full-core interiors exist | **SUPPORTED** |
| H3 new interior atoms sprout | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

**#9 sprout or thicken?** Sprout. Multihub m=2 at n=7 lands on Φ=**10**,
absent from L≤6 interiors. Prior landmarks 6 and 12 also recur (thicken),
so scale both **extends** the atom set and **reuses** known steps. No
continuum: values stay discrete.

**Limits.** n=7 decisive panel; lean n=8 not recomputed tonight. Conjunctive
AND; designed families only. Evidence about the model, not a real organization.

## Best next

**V3 #10** (parity law under n>6 hubs) or **V3 #11** (graded×topo).

## Reproduce

```
python org_frontier/studies/interior_atoms_n78/analyze_atoms_n78.py
```
(loads committed census; `--rebuild` recomputes exact Φ)
