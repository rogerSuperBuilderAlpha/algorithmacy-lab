# Beyond-binary arc — #1–#4 working picture

Short spine for the beyond-binary lane on `RESEARCH_AGENDA_50_V2`
(PR #739). Prefer exact IIT-4.0 Φ. PE / AI / formal / stoch /
estimation / construct-omit stay closed except as pointers.

## Instrument status

Lab pin: `pyphi @ feature/iit-4.0` (binary `Network` + `new_big_phi`).
Vendored overlay: `third_party/pyphi_iit4_mv` (**M1_GREEN** — SBS-native
ingest; Φ still blocked).

| attempt | result |
|---|---|
| Path (C) #1 science | **NOT_TESTABLE** — stock pin rejects ternary |
| Path (A) M1 SBS-native TPM | **M1_GREEN** — see `studies/multivalued_iit4_port/` |
| Path (A) exact ternary Φ | **blocked** at M2 (`backward_tpm`) |
| Path (B) embeddings | rejected for #1 (not party-level exact Φ) |
| `pyphi@nonbinary` | rejected (IIT-3.0; 3.12 import break; no `new_big_phi`) |

**CI-off is not a fix:** it reinterprets `k^n` SBS as corrupt binary
via `int(log2(…))`. M1 does not use it.

## #1 status

| # | study | verdict |
|---|---|---|
| 1 | `ternary_pivotality/` | **NOT_TESTABLE** |
| — | `multivalued_iit4_port/` | **M1_GREEN** (Φ still gap → M2) |

Binary two-condition control holds. Ternary science blocked on M2–M3.

## #2–#4

**Blocked** until ternary exact-Φ smoke (M3).

## Best next

**Engineering:** M2 SBS-native `backward_tpm` / `condition_tpm` +
repertoire (`INSTRUMENT_GAP.md`). Do not reopen #1–#4 science until
ternary Φ smoke is green.

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m1.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
```
