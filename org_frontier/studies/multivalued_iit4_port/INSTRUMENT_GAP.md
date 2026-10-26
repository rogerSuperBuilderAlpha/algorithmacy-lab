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
| M3 | Fork branch, upstream PyPhi 2.0 parity, alphabet/n notes | recorded below; stock pin unchanged |
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

## M3 — fork branch and PyPhi 2.0 parity

M3 records where the overlay lives besides this tree, and how upstream PyPhi 2.0 reads the same controls. The stock pin in `requirements.txt` stays `feature/iit-4.0`.

The port is on `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339ac74aa086112545141306907ab32b4e15` and `4cdda4a1cbf73e89dd368e3991990c3933dd8b48`), pull request `rogerSuperBuilderAlpha/pyphi#1`, on top of `feature/iit-4.0` at `b78d0e342`. Upstream `wmayner/pyphi#147` closed on 25 October 2026. Will Mayner noted there that `feature/iit-4.0` is superseded by the 2.0 release candidate on `main` (`134a8f31b49db512322465ed3ba5da7194d362fd`, tag `v2.0.0rc4`, version line `2.0.0rc5.dev0`; `pip install --pre pyphi`). On the fork, `develop` is at `f92b981d` (11 April 2026) and `2.0` is at `ccd247dc` (17 May 2026).

On the benchmark controls, PyPhi 2.0 at `134a8f31` under `pyphi.iit4_2023()` matches `feature/iit-4.0@b78d0e342` and this overlay to machine precision. The binary conjunctive triad at `(1,1,1)` has φ_s = 2.0 (Φ = 4.5, 4 distinctions, 10 relations). The majority triad at `(1,1,1)` has φ_s = 1.666667. The ternary conjunctive triad (`num_states_per_node=(3,3,3)`, `S' = min(W,C)`) at `(2,2,2)` has φ_s = 1.584963 (log₂ 3).

Under `pyphi.iit4_2026()`, the default on that line, the ii(s) cap of Mayner, Marshall, and Tononi (2026) leaves the majority triad at φ_s = 1.666667, lowers the binary conjunctive triad from 2.0 to φ_s = 1.0 (Φ = 4.5, 4 distinctions, 10 relations unchanged), and lowers the ternary state `(2,2,2)` from 1.584963 to φ_s = 0.630930. Each of those three stays positive (φ_s > 0), and the Φ-structure is intact. The majority triad here is the PyPhi majority gate. The lab's three-voter rule, which scores Φ_MIP = 0 on the pinned line, is a separate model.

`pyphi.iit4_2023()` is the 2023 formalism (Albantakis et al. 2023): system integration is the uncapped directional minimum φ_s = min(φ_c, φ_e). `pyphi.iit4_2026()` caps that minimum by system-level intrinsic information, φ_s = min{φ_c, φ_e, ii(s)}, with ii(s) the minimum, over cause and effect, of the minimum of intrinsic differentiation and intrinsic specification. The 2.0 API is `Substrate`, `System`, and `analyze()` (`System.sia()`, `System.phi_structure()`), with `FactoredTPM` for mixed radix, `sia.ties` for tied MIPs, `pyphi.macro` (`MacroSubstrate`, `CoarseGraining`, `Blackbox`, `emergence`), and `pyphi.estimate` (`estimate_mip`, `purview_inclusion_probabilities`, `random_partitions`).

## What this does *not* claim

- Does not replace the stock binary pin for production binary work.
- Does not use embeddings or `pyphi@nonbinary`.
- Does not claim workers were measured (in-silico only).
