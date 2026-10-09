# M3 subset-Φ fidelity — findings

**Verdict: M3_FLIPS_VERDICT.**
Induced exact Φ already decides V4 #1–#3; overlay background-subset Φ moves the #1 subset-estimand key.

The published cells score clamp-at-0 induced subsystems with stock `classify_rules`. On that estimand the overlay matches stock on **840/840** keep-scores (max |Δ|=0). The reading keys stay `TRANSFER_PARTIAL_EXACT_PHI`, `PHASE_RESTORES_JOINT`, and `RETAIN_FAILS_WITH_ZERO`. The published anchors come back with them: family_n3 seed 41 alt **0.812** and zero **0.792**; multifamily alt **0.660**, zero **0.592**, retain **0.592**, omit **0.559**.

Background-subset Φ is the M3 object: external nodes stay at the current full-system state, and the score is the max over reachable states. There the overlay exceeds stock on **85/840** keep-scores. **84** of those gaps equal 1.0. The other is `parity_hub` at n=4, zero-duty, |Δ|=**0.25**. **79** gaps sit on mediation forms and **6** on parity hubs. Full-system Φ matches on both engines, including the faithful triad at 2.0 and the parity witness at 0.5.

That pair inflation moves cell #1 on the subset estimand. Stock subset alt AUC is **0.736** on family_n3 (drop 0.264 from 1.000, a cliff) and **0.857** on multifamily (a hold), so the key is `FAMILY_N3_ONLY`. Overlay subset alt AUC is **0.889** and **0.916**, both holds, so the key is `EXACT_PHI_ROBUST_MI_ONLY`.

Cells #2 and #3 keep one subset key across engines. Multifamily subset alt already holds on stock (0.857), so both engines read `NO_ALT_CLIFF` for #2. Multifamily subset retain is **0.655** on stock and **0.681** on the overlay, both under the cliff bar, and zero-duty stays a cliff (**0.752** and **0.786**). Both engines read `RETAIN_FAILS_WITH_ZERO` for #3.

The preregistered two-node witness `A'=B'=A XOR B` scores Φ=**1.000** on both engines, so the H3 bar (overlay ahead by ≥0.1) is missed. The parity triad’s proper subsets carry the gap the caveat names: pairs {W,S} and {S,C} go from stock **0.000** to overlay **1.000**, pair {W,C} stays **0.000**, and the whole stays **0.500**.

On stock alone, the background-subset estimand already leaves the published induced keys on #1 and #2 (estimand shift #1 YES, #2 YES, #3 NO). The multifamily alt cliff that carries those two cells is a property of the induced screen. The engine gap is a further move, and it lands on #1.

In-silico. Exact IIT-4.0 on the Boolean panels of V4 #1–#3, n≤4. Hypotheses fixed in `hypotheses.md` before this run. Answers RESEARCH_AGENDA_V4 #12.

**Validation gap.** The scores are exact Φ on designed Boolean models. They are evidence about those models.

## Hypotheses

| H | result |
|---|---|
| H1 stock replay recovers #1–#3 | **SUPPORTED** |
| H2 subset Φ agrees within 1e-6 | **REFUTED** (85/840, max \|Δ\|=1) |
| H3 XOR dyad inflates by ≥0.1 | **REFUTED** (both Φ=1.000) |
| H4 overlay-induced keys match | **SUPPORTED** |
| H5 overlay-subset keys match | **REFUTED** (#1 `FAMILY_N3_ONLY` → `EXACT_PHI_ROBUST_MI_ONLY`) |

## Subset alt and retain (the #1 move)

| panel | screen | stock AUC | overlay AUC |
|---|---|---:|---:|
| family_n3 seed 41 | phi_alt | 0.736 | 0.889 |
| multifamily | phi_alt | 0.857 | 0.916 |
| multifamily | phi_zero | 0.752 | 0.786 |
| multifamily | phi_retain | 0.655 | 0.681 |

## Best next

V4 #11, the graded party channel, is still open.

## Reproduce

```
python org_frontier/studies/m3_subset_fidelity_v4/analyze_fidelity.py
```
