# Mixed-algebra seats — findings

**Verdict: BLINDSPOT_DOMINATES.** One conjunctive seat + one parity seat on
a single mediator does **not** produce a hybrid signature. Whole-form Φ
stays in the parity blind-spot band or factors; the conjunctive seat never
restores a conjunctive landmark (Φ ∈ {2,3,4}). V2 #4’s blind-spot pattern
dominates the mixed form.

In-silico; binary exact IIT-4.0; n≤5. Hypotheses fixed in `hypotheses.md`
before computing. Grows from V3 #3 / V2 #4 / #113. Ternary / M3 noted only.

## Already known

| prior | result |
|---|---|
| #113 / V2 #4 | XOR Φ≈0.5 blind spot; survives radix |
| AND triad | Φ=2.0 |
| shared AND–AND | full-core Φ=4.0 |

## Panel

| cell | whole Φ | kind | major-complex seats |
|---|---:|---|---|
| and_triad | **2.0** | conj_landmark | full triad |
| xor_triad | **0.5** | parity_band | full triad |
| shared_AA | **4.0** | conj_landmark | full |
| shared_XX_or | **0.5** | parity_band | full |
| mix_AND | 0.0 | **factors** | parity seat only |
| mix_OR | 0.0 | **factors** | parity seat only |
| mix_XOR | 0.125 | **parity_band** | both (incomplete) |
| mix_AND_XNOR | **0.5** | **parity_band** | conj seat (local Φ=2) |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 AND Φ=2 + XOR Φ=0.5 anchors | **SUPPORTED** |
| H2 pure shared AND Φ=4 + XOR band | **SUPPORTED** |
| H3 mixed: no conjunctive whole landmark | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Mixing algebras on one mediator does not average the two templates. When a
parity seat is present, the whole-form signature is the blind-spot band (or
collapse). Even when the major complex localizes on the conjunctive seat
(mix_AND_XNOR, core Φ=2), whole-system Φ remains 0.5. No hybrid atom
appears between 0.5 and 2.

Validation gap: Boolean models, not organizations.

## Best next (V3)

Scale lane **#8** closed (`BAND_GRAMMAR_HOLDS`). Next: **#9** (interior
atoms at n=7–8) or graded×topo **#11**.

## Reproduce

```
python org_frontier/studies/mixed_algebra_seats/analyze_mixed_seats.py
```
