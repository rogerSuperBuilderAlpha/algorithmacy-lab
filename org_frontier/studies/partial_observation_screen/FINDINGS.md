# Partial observation / estimability — findings

**Verdict: HIDDEN_COLLAPSE_INTERMITTENT_CLIFF.** On the #122/#23
strict-mediation n=3 family, mean pairwise MI under full observation
ranks the verdict at AUC **0.922**. Hiding one party collapses the
screen to **0.547** (Δ=0.375). Intermittent observation of that party
does **not** degrade smoothly: AUC stays ≥0.92 for every duty cycle
δ≥0.10, then cliffs to chance at δ=0 (max consecutive drop **0.422**).
Hiding the mediator barely moves AUC (**0.934**). Role, not mere
missingness volume, decides the damage.

In-silico; exact IIT-4.0 labels; complete-case mean MI under the
observation mask; T=2000, noise=0.08. Hypotheses fixed in
`hypotheses.md`. Pointers: `sample_complexity_screen/` (#23),
`spectral_invariant/` (#21), `ESTIMATION_ARC.md`. Construct/omit/
ladder/indeg closed.

## Curves

### Family n=3 (24 tri / 24 dya) — primary

| regime | MI AUC |
|---|---:|
| full | **0.922** |
| hidden party C | **0.547** |
| hidden party W | 0.524 |
| hidden mediator S | **0.934** |

### Intermittent party C (duty cycle δ)

| δ | MI AUC |
|---:|---:|
| 1.00 | 0.941 |
| 0.75 | 0.929 |
| 0.50 | 0.924 |
| 0.25 | 0.931 |
| 0.10 | 0.943 |
| 0.00 | **0.521** |

Intermittent mediator S stays ≥0.92 at every δ, including 0.00.

### Multifamily secondary (N=23 designed forms)

Per-family AUC often undefined (single-class families). Where both
labels exist, `single_hub` drops full→hidden 1.000→0.500 (Δ=0.500);
`chain` / `majority` hold at 1.000. Pooled oriented AUC does not
reproduce the within-family collapse (cross-topo #134 already limits
the screen). Role contrast on `family_n3` is the clean H3 witness.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 hidden party collapses (Δ≥0.20 or AUC<0.70) | **SUPPORTED** |
| H2 intermittent degrades smoothly (max drop≤0.25) | **REFUTED** (cliff at δ=0) |
| H3 topology/family mediates | **SUPPORTED** (mediator vs party \|Δ\|=0.387; family Δ spread=0.500) |

## Reading

Estimability under partial observation is **role-gated**, not a smooth
function of observation fraction. A sparse party channel (δ≥0.10) is
enough to keep the #122 MI screen alive on this family. Total absence
of a party kills it. The mediator can drop out of the log without
hurting mean-MI ranking — the cheap screen rides party–party coupling
that survives S-masking on these trajectories. Practice: treat a
missing party as a hard fail for coupling screens; intermittent logging
of that party is far less dangerous than silence. Cascade / exact Φ
remains the backstop when a role is unobserved.

## Limits

One draw per form; designed multifamily N=23 with several single-class
families (per-family AUC often nan). Oriented AUC. No field logs. No
claim about real organizations.

## Best next experiment

**#24 closes the estimation lane** with #21–#23+#25. Optional later:
**M3** overlay subset-Φ fidelity (`BEYOND_BINARY_ARC.md` /
`PR739_PACKAGE.md`), or a new agenda gap outside estimation. Do not
reopen construct/omit/ladder. Skip deep MARL unless separately scoped.

## Reproduce

```
python org_frontier/studies/partial_observation_screen/analyze_partial_obs.py
```
(~8 s)
