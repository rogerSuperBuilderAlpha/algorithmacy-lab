# Parity radix blind spot — findings

**Verdict: BLINDSPOT_SURVIVES_RADIX.** The #113 parity blind spot is
**not** binary-specific. Balanced commits `S'=(W+C) mod k` keep a low,
flat full-system Φ band (≈0.5) at k=2,3,4, while min-commit is high.

In-silico. Exact IIT-4.0. Binary pure-HO via stock; higher radix via
`pyphi_iit4_mv` full-system Φ. N=3. Hypotheses fixed in `hypotheses.md`.
#1–#3 pointers only.

## #113 binary control (stock)

| commit | major Φ | pure-HO |
|---|---|---|
| XOR | 0.5 | **yes** |
| AND | 2.0 | no |

## Radix panel (overlay full-system)

| k | sum-mod max Φ | flat | min max Φ |
|---|---|---|---|
| 2 | 0.500 | yes | 2.000 |
| 3 | 0.528 | yes | 3.170 |
| 4 | 0.500 | yes | 4.000 |

## Hypotheses

| H | result |
|---|---|
| H1 binary-specific | **REFUTED** |
| H2 sum-mod-k recreates low-Φ band | **SUPPORTED** |
| H3 morphs | **REFUTED** (k=3 mild 0.528 drift only) |

## Caveat

Overlay proper-subset Φ is inflated on binary XOR dyads (M3 fidelity);
pure-HO at k>2 is **not** claimed from overlay subsets. The #113
signature used here is the full-system low-flat vs high-conjunctive
split, which matches stock at k=2.

## Best next

Beyond-binary science **closable**. Optional: M3 subset-Φ fidelity on
the overlay.

## Reproduce

```
python org_frontier/studies/parity_radix_blindspot/analyze_parity.py
```
