# Beyond-binary arc — #1–#4 working picture

Short spine for the beyond-binary lane on `RESEARCH_AGENDA_50_V2`
(PR #739). Prefer exact IIT-4.0 Φ. PE / AI / formal / stoch /
estimation / construct-omit stay closed except as pointers.

## Instrument status

Lab pin: `pyphi @ feature/iit-4.0` (binary `Network` + `new_big_phi`).

| attempt | result |
|---|---|
| Path (C) #1 | **NOT_TESTABLE** — pin rejects ternary |
| Path (A) port survey | **INSTRUMENT_GAP** — see `studies/multivalued_iit4_port/` |
| Path (B) embeddings | rejected for #1 (not party-level exact Φ) |
| `pyphi@nonbinary` | rejected (IIT-3.0; 3.12 import break; no `new_big_phi`) |

**CI-off is not a fix:** it reinterprets `k^n` SBS as corrupt binary
via `int(log2(…))`.

## #1 status

| # | study | verdict |
|---|---|---|
| 1 | `ternary_pivotality/` | **NOT_TESTABLE** |
| — | `multivalued_iit4_port/` | **INSTRUMENT_GAP** (path A) |

Binary two-condition control holds. Ternary science blocked.

## #2–#4

**Blocked** by the same instrument gate.

## Best next

**Engineering (not science):** vendored IIT-4.0 fork with SBS-native
mixed-radix TPM (M1 in `INSTRUMENT_GAP.md`). Do not reopen #1–#4
science until ternary Φ smoke is green.

## Reproduce

```
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
```
