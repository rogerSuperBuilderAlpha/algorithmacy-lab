# Multivalued IIT-4.0 port — findings

**Verdict: M1_GREEN.** Path A M1 landed under
`third_party/pyphi_iit4_mv`: ternary `MultivaluedNetwork` constructs;
SBS preserved without `int(log2)` collapse; CI-off unused. Exact
ternary Φ remains **blocked** at stock
`backward_tpm`/`probability_of_current_state` (M2). Agenda **#1
remains NOT_TESTABLE**.

See `INSTRUMENT_GAP.md` for locus, milestones, and next step.

## Checks

| check | result |
|---|---|
| binary control Φ=2 triad | PASS |
| stock ternary `(27,27)` Network | REJECTED |
| CI-off trap | CONFIRMED (do not use) |
| M1 MultivaluedNetwork `(9,9)`/`(27,27)` | GREEN |
| SBS preserved | GREEN |
| ternary Φ smoke | BLOCKED (M2 locus documented) |

## Next engineering step

**M2:** SBS-native `backward_tpm` + `condition_tpm` + repertoire over
`∏ k_i`, then deterministic 2-node ternary `new_big_phi` smoke.

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m1.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```
