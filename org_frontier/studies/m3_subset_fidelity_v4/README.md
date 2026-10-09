# M3 subset-Φ fidelity vs V4 items 1–3 (agenda V4 item 12)

Does subset-Φ from `third_party/pyphi_iit4_mv` move any of the V4
items 1–3 reading keys, or does exact binary Φ already decide them?

## Run

```
python org_frontier/studies/m3_subset_fidelity_v4/analyze_fidelity.py
```

## Result in one line

**M3_FLIPS_VERDICT** — H2 on the decision keeps is 41/456 and still
refuted. Induced decision keeps match (0/456) and the three published
keys stand. The all-keep descriptive subset count is 85/840.
Background-subset Φ moves the V4 item 1 key (`FAMILY_N3_ONLY` to
`EXACT_PHI_ROBUST_MI_ONLY`).

## Hypotheses

Fixed before computing in [`hypotheses.md`](hypotheses.md).

## Priors

V4 item 1 `TRANSFER_PARTIAL_EXACT_PHI`; item 2 `PHASE_RESTORES_JOINT`;
item 3 `RETAIN_FAILS_WITH_ZERO`. Overlay M1+M2 green; subset-Φ caveat in
`BEYOND_BINARY_ARC.md` and `PR739_PACKAGE.md`. Exact binary IIT-4.0;
in-silico.
