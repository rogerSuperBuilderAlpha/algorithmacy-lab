# Mixed-radix mediator — findings

**Verdict: EXTRA_RESOLUTION_TO_PHI.** With binary parties and a ternary
mediator (`S'=W+C`, alphabets `(2,3,2)`), the extra mid level goes into
**Φ magnitude**, not core membership. On the `(1,S,1)` sweep both
party-read forms keep core `{W,S,C}` while Φ varies with S.

In-silico. Exact IIT-4.0 via `pyphi_iit4_mv`. N=3. Hypotheses fixed in
`hypotheses.md`. #1 / #2 pointers only.

## Binary control

AND `@ (1,1,1)`: TRIADIC Φ=2, core {W,S,C} (stock = overlay).

## Mixed-radix sweep `(1,S,1)`

| form | S=0 Φ | S=1 Φ | S=2 Φ | core |
|---|---|---|---|---|
| full (`S==2`) | 1.170 | 0.500 | 2.000 | {W,S,C} all |
| thresh (`S>=1`) | 0.585 | 0.250 | 0.585 | {W,S,C} all |

## Hypotheses

| H | result |
|---|---|
| H1 extra resolution → Φ only | **SUPPORTED** (both forms) |
| H2 extra resolution → membership | **REFUTED** |
| H3 form-dependent pattern | **REFUTED** |

## Reading

All-ternary #2 graded membership with commit level. Mixed-radix does
not: binary party alphabets pin the core; ternary S only modulates Φ.
The mid state S=1 is expressible only with the extra mediator bit and
shows up as a Φ dent, not a core change.

## Best next

**#4** higher-radix parity / balanced commit (blind spot).

## Reproduce

```
python org_frontier/studies/mixed_radix_mediator/analyze_mixed.py
```
