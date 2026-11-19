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

These controls were run on PyPhi 2.0 at `134a8f31` under Python 3.13. Under `pyphi.iit4_2026`, φ_s(s, P) = min{φ_c(s, P), φ_e(s, P), ii(s)}. A strictly deterministic transition has one forward effect state, so effect differentiation is 0, ii(s) = 0, and φ_s = 0 unless the run uses positive transition noise or `pyphi.iit4_2023`.

On the binary conjunctive triad at (1, 1, 1), `pyphi.iit4_2023` at p = 0 returns φ_s = 2.000000 (structure Φ = 12.000000, 4 distinctions with Σφ_d = 5.0, 8 relations with Σφ_r = 7.0), matching `feature/iit-4.0@b78d0e342`, then 1.898808 (Φ = 11.559196) at p = 0.01, 1.533412 (Φ = 9.937348) at p = 0.05, 1.155438 at p = 0.10, 0.610634 at p = 0.20, 0.276923 at p = 0.30, and 0.089648 at p = 0.40. `pyphi.iit4_2026` returns φ_s = 0 at p = 0, with φ_c = φ_e = 2 and structure Φ = 12 still in place, then 0.043216, 0.215495, 0.432740, a peak of φ_s = φ_e = 0.610634 at p = 0.20 (ii(s) = 0.894818), 0.276923, and 0.089648. The three-voter majority triad at (1, 1, 1) scores φ_s = 0 under both presets, with `len(sia.ties) == 4` and `d.cause.purview_ties = [((0, 1), 0.5), ((1, 2), 0.5), ((0, 2), 0.5)]` on voter A's first-order distinction.

The ternary conjunctive triad (k = 3, S' = min(W, C)) at (2, 2, 2) returns φ_s = 3.169925 = 2 log₂ 3 under `pyphi.iit4_2023` at ε = 0 (structure Φ = 16.906267). `smoke_m2.py` prints 3.169925 on its 2-node ternary control. Under `pyphi.iit4_2026` that state is φ_s = 0 at ε = 0, 0.043499 at ε = 0.01 (φ_c = 2.991744, φ_e = 3.020328), and 0.222002 at ε = 0.05 (φ_c = 2.387629, φ_e = 2.481492). At (1, 1, 1), `pyphi.iit4_2023` returns φ_s = 0.194988 on {W, S, C} (`len(sia.ties) == 3`, structure Φ = 7.258146) and φ_s = 0.508798 on each of {W, S} and {S, C}. Under `pyphi.iit4_2026`, (1, 1, 1) is φ_s = 0 at ε = 0, 0.043499 at ε = 0.01, and φ_s = φ_c = 0.179018 at ε = 0.05.

`pyphi.iit4_2023()` is the 2023 formalism (Albantakis et al. 2023): system integration is the uncapped directional minimum φ_s = min(φ_c, φ_e). The 2.0 API is `Substrate`, `System`, and `analyze()` (`System.sia()`, `System.phi_structure()`), with `FactoredTPM` for mixed radix, `sia.ties` for tied MIPs, `pyphi.macro` (`MacroSubstrate`, `CoarseGraining`, `Blackbox`, `emergence`), and `pyphi.estimate` (`estimate_mip`, `purview_inclusion_probabilities`, `random_partitions`).

## What this does *not* claim

- Does not replace the stock binary pin for production binary work.
- Does not use embeddings or `pyphi@nonbinary`.
- Does not claim workers were measured (in-silico only).
