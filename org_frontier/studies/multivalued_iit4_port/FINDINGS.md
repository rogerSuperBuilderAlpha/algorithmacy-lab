# Multivalued IIT-4.0 port — findings

**Verdict: M2_GREEN.** Exact ternary IIT-4.0 Φ runs on
`third_party/pyphi_iit4_mv`. Binary regression matches stock pin Φ=2.
CI-off unused. Agenda **#1** re-opened →
`TWO_CONDITION_STATE_DEPENDENT` (see `ternary_pivotality/`).

## Checks

| check | result |
|---|---|
| binary control / regression Φ=2 | PASS (match stock) |
| stock ternary `(27,27)` | REJECTED |
| M1 SBS ingest | GREEN |
| M2 exact ternary Φ (2-node) | GREEN (Φ=log₂9) |
| maximal_complex | GREEN |
| independent sticky Φ≈0 | PASS |
| CI-off trap | unused |

## Next

M3 polish (broader alphabets / n ceiling docs); beyond-binary **#2–#4**
on the overlay.

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m2.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```
