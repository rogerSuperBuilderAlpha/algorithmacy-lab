# Sample complexity of the cheap screen — findings

**Verdict: FAST_WITHIN_FAMILY.** On the #122 strict-mediation n=3
family, mean pairwise MI already hits AUC **0.97 at T=125** (noise 0.08
and 0.16). The cheap screen’s sample need is tiny *within that family*.
Longer trajectories do **not** rescue MI on cross-topology panels (AUC
~0.2 at every T — #134 stands). Doubling noise does not raise T*.

In-silico; exact IIT-4.0 labels; nested prefixes of T_max=4000.
Hypotheses fixed in `hypotheses.md`. Pointer:
`structure_aware_surrogate/` NO_STRUCTURE_GAIN (#22). Construct/omit/
ladder/indeg closed.

## Curves (MI-AUC / RF-AUC)

### Family n=3 (24 tri / 24 dya) — primary #122 setting

| T | MI AUC (0.08) | RF AUC | MI AUC (0.16) |
|---:|---:|---:|---:|
| 125 | **0.972** | 0.961 | **0.965** |
| 500 | 0.964 | 0.989 | 0.967 |
| 4000 | 0.967 | 0.999 | 0.964 |

**T*_MI = 125** at both noises. T*_RF = 125.

### Within-hub size series (8 forms/n)

MI never reaches 0.90 at n∈{3,4,5} on this small designed set (parity /
majority mix). Eight-feature RF reaches AUC≥0.90 at **T=2000** for n=5
only (0.938); n=3/4 RF stay below 0.90 by T=4000.

### Cross-topo secondary (n=4,5)

| panel | MI AUC at T=4000 | RF best |
|---|---:|---:|
| cross_n4 | 0.229 | 0.829 |
| cross_n5 | 0.200 | 0.950 (T≥125) |

Longer T does not fix MI’s topology inversion.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 family n=3 T*≤1000 | **SUPPORTED** (T*=125) |
| H2 hub T* grows with n | **REFUTED** (MI T* undefined at all hub n; no 2× growth to report) |
| H3 noise raises T*≥1.5× | **REFUTED** (T*=125 at both noises) |

## Reading

Sample complexity of the #122 MI screen is a **within-family** fact: a
few hundred steps suffice on strict mediation. The binding constraint
is not T but **topology** (#134) and, for multi-feature RF, modest T
on small hub panels. Cascade practice (T=4000) is already past the
within-family MI knee; spending more trajectory length will not buy
cross-topology MI.

## Limits

One nested draw per form; designed hub/cross panels are small (N≈8–13).
No field data. Probe-131 cascade features are connectivity/dynamics,
not traj-MI — this study targets the #122 coupling screen lineage.

## Best next experiment

Done: #21 SPECTRAL_PARTIAL, #25 **AL_NO_GAIN**, lane note
[`ESTIMATION_ARC.md`](../../ESTIMATION_ARC.md). Estimation lane
**closable**. Optional later: agenda **#24**. Skip construct/omit/ladder.

## Reproduce

```
python org_frontier/studies/sample_complexity_screen/analyze_complexity.py
```
(~75 s)
