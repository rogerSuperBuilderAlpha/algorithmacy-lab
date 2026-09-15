# Interior topology between ring and pool — findings

**Verdict: NO_INTERMEDIATE_LAW.** Full-core topologies **between** the ring
(Φ = 4) and the pool (Φ = n(n−1)) **exist**, but none in this designed census
follows a **log or √n law in n**. Φ rises in **discrete steps** set by hub
count, chord count, or ring degree. Partial pools **collapse**. Not a pure
jump between poles, and not the log/√n intermediate the agenda asked for.

In-silico; binary exact IIT-4.0; n ∈ {4,5,6}. Hypotheses fixed in
`hypotheses.md`. Extends #132 / q143 / pool ceilings; cites
`small_world_vs_hierarchy` PICK_ONE and q146/q150. Ternary / residual-cascade
noted only.

## Already known

| prior | result |
|---|---|
| ring (#132 / q143) | Φ = 4.0 size-independent for n ≥ 4 |
| pool | Φ = n(n−1) (12, 20, 30 at n=4,5,6) |
| small-world #17 | PICK_ONE; ring→hub interiors collapse |
| q150 one chord | Φ stays 4.0 |
| #119 multihub | Φ rises with m toward pool |

## Census (selected)

| cell | n | core Φ | full | band |
|---|---:|---:|---|---|
| ring | 4–6 | **4** | yes | lower pole |
| pool | 4–6 | **12 / 20 / 30** | yes | upper pole |
| mh m=2 | 5, 6 | **6, 8** | yes | **interior** |
| mh m=3 | 5, 6 | 12 | no | incomplete |
| chord c=2 | 5, 6 | **6, 6** | yes | **interior** |
| chord c=3 | 6 | **9** | yes | **interior** |
| k-reg d=2 | 5 | 20 | yes | = pool |
| k-reg d=2 | 6 | **12** | yes | **interior** |
| lattice strip | 6 | **6** | yes | **interior** |
| partial pool m<5 | 5 | 2–12 | no | **collapse** |

At n=6, full-core Φ steps: **4 → 6 → 8 → 9 → 12 → 30**.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 ring cap + pool n(n−1) | **SUPPORTED** |
| H2 fixed-n interiors exist | **SUPPORTED** |
| H3 no log/√n intermediate law | **SUPPORTED** |
| H4 partial pools collapse | **SUPPORTED** |
| H5 discrete steps at n=6 | **SUPPORTED** |

## Reading

**Log / √n law?** No. `mh_m2` goes 6→8 (not proportional to log n or √n);
`chord_c2` is flat at 6; `kreg_d2` is pool at n=5 then 12 at n=6 (non-monotone
in the log/√n sense). No series keeps Φ/log(n) or Φ/√n within 10%.

**Only poles / collapse?** No. Seven full-core interiors sit strictly between
ring and pool. Coupling richness (extra hubs, chords, next-nearest neighbors,
strip width) buys **stepwise** Φ, not a continuous intermediate scaling in n.

**vs small-world PICK_ONE.** Rewiring *from* a ring toward hubs collapses.
Building *designed* interiors (symmetric multi-hub, chordal, k-regular) can
occupy the gap — different question, different answer.

## Limits

Exact Φ through n=6; n=6 trimmed (no redundant ring aliases). Conjunctive AND
only. No organization measured.

## Best next experiment

**Done next:** `random_coupling_ensemble/` (agenda #18) — DISCRETE_LANDMARKS;
random AND couplings hit #19 atoms only; triadic rate tracks generator.
Follow-on: larger n=5 ensemble, or scale blur of discriminants (#42).

## Reproduce

```
python org_frontier/studies/interior_ring_pool/analyze_interior.py
```
(~7 min; n=6 cells dominate)
