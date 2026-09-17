# Multivalued IIT-4.0 port — findings

**Verdict: INSTRUMENT_GAP.** Path A surveyed and probed. The lab pin
rejects ternary SBS at `ExplicitTPM`/`convert` (binary `2^n`).
CI-off is a corrupt shim (`int(log2(9))=3`). `pyphi@nonbinary` is
IIT-3.0, fails on Python 3.12, and has no `new_big_phi`. A trustworthy
multivalued IIT-4.0 port is **multi-week**, not a study-turn patch.
Agenda **#1 remains NOT_TESTABLE**.

See `INSTRUMENT_GAP.md` for locus, inventory, effort, and next step.

## Checks

| check | result |
|---|---|
| binary control Φ=2 triad | PASS |
| ternary (27,27) Network | REJECTED |
| `num_states_per_node` on pin | absent |
| CI-off trap | CONFIRMED (do not use) |
| nonbinary branch usable | REFUTED |
| ternary Φ smoke | BLOCKED |

## Next engineering step

Vendor `feature/iit-4.0` fork → M1 SBS-native mixed-radix
`ExplicitTPM` → M2 repertoire/`Subsystem` → M3 `new_big_phi` smoke on
2-node ternary → then reopen #1.

## Reproduce

```
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```
