# INSTRUMENT_GAP — multivalued IIT-4.0 on the lab pin

**Status: M2_GREEN (exact ternary Φ on vendored overlay).**
Stock `pyphi @ feature/iit-4.0` still rejects ternary SBS. Overlay
`third_party/pyphi_iit4_mv` constructs ternary Networks, preserves SBS
(no `int(log2)`), and computes exact IIT-4.0 system Φ (binary
regression matches stock Φ=2). Agenda #1 re-opened.

## Milestone status

| milestone | scope | status |
|---|---|---|
| **M1** | SBS-native ExplicitTPM + MultivaluedNetwork | **GREEN** |
| **M2** | Subsystem / backward TPM / sia (GID) / maximal_complex | **GREEN** |
| M3 | Broader alphabet/n docs; optional pin wiring | next polish |
| M4 | Full #2–#4 beyond-binary panels | science |

## Enable

```python
import sys
sys.path.insert(0, "<repo>/third_party")
from pyphi_iit4_mv import MultivaluedNetwork, exact_phi, maximal_complex
```

Stock binary Φ unchanged (`import pyphi`).

## Limitations

- Alphabet: any `k_i >= 2`; smoke covers ternary `k=3` and binary `k=2`.
- n ceiling: practical SBS size `∏ k_i` (smoke n≤3).
- Repertoire distance: `GENERALIZED_INTRINSIC_DIFFERENCE` only (lab default).
- CI-off `int(log2)` trap: **not used**.
- Do not install `pyphi@nonbinary` (IIT-3.0; 3.12 break).

## Φ path (M2)

`MultivaluedSubsystem` factorizes SBS → categorical node TPMs; implements
cause/effect repertoires over mixed-radix shapes; `sia` mirrors
`new_big_phi.sia` (GID, SET_UNI/BI partitions). Blocker that M1 hit
(`backward_tpm` / `probability_of_current_state`) is bypassed — not
shimmed via binary SBN.

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m2.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
```

## What this does *not* claim

- Does not replace the stock binary pin for production binary work.
- Does not use embeddings or `pyphi@nonbinary`.
- Does not claim workers were measured (in-silico only).
