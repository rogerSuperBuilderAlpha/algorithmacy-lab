# M3 subset-Φ fidelity — findings

**Verdict: M3_FLIPS_VERDICT.**
Induced exact Φ already decides V4 items 1–3; overlay background-subset Φ moves the V4 item 1 subset-estimand key.

The published cells score clamp-at-0 induced subsystems with stock `classify_rules`. On the preregistered decision keeps that screen matches the overlay on **0/456** scores (max |Δ|=0). The all-keep induced count, every keep on every panel, is the same story: **0/840**. The reading keys stay `TRANSFER_PARTIAL_EXACT_PHI`, `PHASE_RESTORES_JOINT`, and `RETAIN_FAILS_WITH_ZERO`. The published anchors come back with them: family_n3 seed 41 alt **0.812** and zero **0.792**; multifamily alt **0.660**, zero **0.592**, retain **0.592**, omit **0.559**.

H2 asks whether background-subset Φ agrees, and it is scored on `DECISION_KEEPS` only. That grid is **41/456** (max |Δ|=1), so H2 is refuted. Forty of the 41 gaps equal 1.0. The other is `parity_hub` at n=4, zero-duty, |Δ|=**0.25**. The 41 split as **35** mediation forms and **6** parity hubs. The verdict rule reads H4 and H5. Both still hold, so the keys and `M3_FLIPS_VERDICT` stand.

The all-keep subset tally is descriptive, and it is a different denominator. Every keep on every panel gives **85/840** gaps (84 equal to 1.0; **79** mediation and **6** parity). Those extra 44 rows are keeps outside the decision grid, mostly family seed 42 pairs and family seed 41 zero-duty. They are not the H2 count.

The move in the V4 item 1 subset-estimand key is unchanged by the recount. Stock subset alt AUC is **0.736** on family_n3 (drop 0.264 from 1.000, a cliff) and **0.857** on multifamily (a hold), so the key is `FAMILY_N3_ONLY`. Overlay subset alt AUC is **0.889** and **0.916**, both holds, so the key is `EXACT_PHI_ROBUST_MI_ONLY`.

V4 items 2 and 3 keep one subset key across engines. Multifamily subset alt already holds on stock (0.857), so both engines read `NO_ALT_CLIFF` for item 2. Multifamily subset retain is **0.655** on stock and **0.681** on the overlay, both under the cliff bar, and zero-duty stays a cliff (**0.752** and **0.786**). Both engines read `RETAIN_FAILS_WITH_ZERO` for item 3.

The preregistered two-node witness `A'=B'=A XOR B` scores Φ=**1.000** on both engines, so the H3 bar (overlay ahead by ≥0.1) is missed. That witness is separate from the panel gap count. The parity triad’s proper subsets carry the inflation the caveat names: pairs {W,S} and {S,C} go from stock **0.000** to overlay **1.000**, pair {W,C} stays **0.000**, and the whole stays **0.500**.

On stock alone, the background-subset estimand already leaves the published induced keys on V4 items 1 and 2 (estimand shift item 1 YES, item 2 YES, item 3 NO). The multifamily alt cliff that carries those two cells is a property of the induced screen. The engine gap is a further move, and it lands on V4 item 1.

In-silico. Exact IIT-4.0 on the Boolean panels of V4 items 1–3, n≤4. Hypotheses fixed in `hypotheses.md` before this run. Answers RESEARCH_AGENDA_V4 item 12.

**Validation gap.** The scores are exact Φ on designed Boolean models. They are evidence about those models.

## Hypotheses

| H | result |
|---|---|
| H1 stock replay recovers V4 items 1–3 | **SUPPORTED** |
| H2 subset Φ agrees within 1e-6 on decision keeps | **REFUTED** (41/456, max \|Δ\|=1) |
| H3 XOR dyad inflates by ≥0.1 | **REFUTED** (both Φ=1.000) |
| H4 overlay-induced keys match | **SUPPORTED** |
| H5 overlay-subset keys match | **REFUTED** (V4 item 1 `FAMILY_N3_ONLY` to `EXACT_PHI_ROBUST_MI_ONLY`) |

## Subset alt and retain (the V4 item 1 move)

| panel | screen | stock AUC | overlay AUC |
|---|---|---:|---:|
| family_n3 seed 41 | phi_alt | 0.736 | 0.889 |
| multifamily | phi_alt | 0.857 | 0.916 |
| multifamily | phi_zero | 0.752 | 0.786 |
| multifamily | phi_retain | 0.655 | 0.681 |

## Best next

V4 item 11 is answered (`GRADED_HOLDS`, `studies/graded_channel_exact_phi/`).

## Reproduce

```
python org_frontier/studies/m3_subset_fidelity_v4/analyze_fidelity.py
```
