# random_coupling_ensemble n=5 — hypotheses (fixed before computing)

**Question.** At n=5, do random conjunctive couplings still land only on the
discrete landmark set (as at n=4), or do new Φ values appear?

**Already known.**
- **n=4 arm (`FINDINGS.md`):** DISCRETE_LANDMARKS — 224 samples, every core Φ ∈
  {2, 4, 6, 12}; triadic rate tracks generator.
- **`interior_ring_pool` (#19):** at n=5 designed landmarks include ring **4**,
  pool **20**, mh m=2 **6**, mh m=3 incomplete **12**, chord c=2 **6**, plus
  chain-like **2** / hub-breadth **3** from related families.
- Ternary / residual-cascade noted only.

**Universe.** Same generators as the n=4 arm (ER / fixed_k / WS / BA). Exact
IIT-4.0. Target **N ≈ 90** across ensembles (~5–10 s/sample; candid total
~8–15 min). Seeded.

**Landmark set L5:** {2, 3, 4, 6, 8, 12, 20} — n=4 atoms plus n=5 designed
poles/interiors from #19 (8 = mh_m2 at n=6 scaled interest; include for
completeness of known full-core steps seen nearby). Primary claim uses this set;
report any Φ outside it as a new value.

## Ensembles (n=5)

| name | N | note |
|---|---:|---|
| ER p=0.4 | 20 | intermediate density |
| fixed_k=2 | 20 | match n=4 workhorse |
| fixed_k=3 | 16 | denser; not yet pool |
| WS p=0.3 | 20 | ring-rewire |
| BA m=2 | 16 | preferential |

## H1 — discrete landmarks hold at n=5

≥ 90% of core Φ values (all ensembles pooled) round into L5. Null: on_landmark
< 0.90.

## H2 — new Φ values appear (alternative)

At least one sample has core Φ outside L5 (rounded to 1e-6). If H2 holds and
H1 fails, discrete-landmarks is **REFUTED** at n=5. If H1 holds and off-landmark
count is 0, H2 is **REFUTED**.

## H3 — triadic rate tracks generator

ER p=0.4 triadic rate < fixed_k=2 triadic rate (gap ≥ 0.05), echoing n=4.
Null: rates within 5 points.

## H4 — between ring and pool only known atoms

Among samples with 4 < Φ < 20, every value is in {6, 8, 12} (known interior
atoms). Null: some between-band Φ not in that set.
