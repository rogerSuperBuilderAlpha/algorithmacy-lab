# pyphi_iit4_mv — vendored IIT-4.0 multivalued pin (M1+M2)

This overlay is the M1+M2 multivalued IIT 4.0 path for the lab's stock pin, `wmayner/pyphi` `feature/iit-4.0` at `b78d0e342d37175cbd55cf35a6d52ae035b4c50f` (`1.2.1.dev1470+gb78d0e342`, 26 December 2025). `requirements.txt` still installs `pyphi @ git+https://github.com/wmayner/pyphi@feature/iit-4.0`, and `ci/reproduce.py` still calls `pyphi.Network`, `pyphi.Subsystem`, and `pyphi.new_big_phi`. The overlay adds state-by-state TPM ingest and exact IIT-4.0 system Φ for ternary and mixed-radix alphabets, past the `int(log2(...))` collapse.

The same port is packaged on the fork branch `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339ac74aa086112545141306907ab32b4e15` and `4cdda4a1cbf73e89dd368e3991990c3933dd8b48`), open as [rogerSuperBuilderAlpha/pyphi#1](https://github.com/rogerSuperBuilderAlpha/pyphi/pull/1). That branch puts the overlay in `pyphi.multivalued` on top of `feature/iit-4.0` at `b78d0e342`. On the fork, `feature/iit-4.0` itself is at that commit. `develop` is at `f92b981d69c6c2de3887509d21b9b834ae4af906` (11 April 2026), synced with upstream. `2.0` is at `ccd247dcad5dd1c38635bdf1095af82919e3cf37` (17 May 2026).

Upstream `wmayner/pyphi#140`, `#141`, `#142`, and `#147` targeted the legacy `feature/iit-4.0` line. Will Mayner noted on `#147` that `feature/iit-4.0` is superseded by the PyPhi 2.0 release candidate on `main` (`pip install --pre pyphi`). All four pull requests closed on 25 October 2026. Upstream `main` is `134a8f31b49db512322465ed3ba5da7194d362fd` (16 October 2026; tag `v2.0.0rc4`, version line `2.0.0rc5.dev0`). That line replaces `Network` / `Subsystem` / `new_big_phi.sia` with `Substrate` / `System` / `analyze()` (`System.sia()`, `System.phi_structure()`). Mixed-radix state is native: `FactoredTPM` takes an arbitrary `num_states_per_node`.

On PyPhi 2.0 at `134a8f31` (Python 3.13), a deterministic transition has one forward effect state, so under `pyphi.iit4_2026` effect differentiation is 0, ii(s) = 0, and φ_s = 0 at ε = 0. `pyphi.iit4_2023` on the binary conjunctive triad at (1, 1, 1) and p = 0 returns φ_s = 2.000000 with structure Φ = 12.000000 (4 distinctions, Σφ_d = 5.0; 8 relations, Σφ_r = 7.0), matching this pin, then 1.898808, 1.533412, 1.155438, 0.610634, 0.276923, and 0.089648 across p = 0.01, 0.05, 0.10, 0.20, 0.30, and 0.40. The 2026 preset is φ_s = 0 at p = 0 and then 0.043216, 0.215495, 0.432740, 0.610634 at p = 0.20, 0.276923, and 0.089648. The three-voter majority triad at (1, 1, 1) is φ_s = 0 under both presets (`len(sia.ties) == 4`). The ternary conjunctive triad at (2, 2, 2) is φ_s = 3.169925 = 2 log₂ 3 (structure Φ = 16.906267) under `pyphi.iit4_2023` at ε = 0. `smoke_m2.py` prints that same 3.169925 on its 2-node ternary control. Under `pyphi.iit4_2026` the (2, 2, 2) state is φ_s = 0 at ε = 0, 0.043499 at ε = 0.01 (φ_c = 2.991744, φ_e = 3.020328), and 0.222002 at ε = 0.05 (φ_c = 2.387629, φ_e = 2.481492). At (1, 1, 1) the 2023 preset returns φ_s = 0.194988 (φ_c = 0.194988, φ_e = 0.584963, `len(sia.ties) == 3`, structure Φ = 7.258146) on the full triad and 0.508798 on each dyadic pair. Under `pyphi.iit4_2026`, (1, 1, 1) is φ_s = 0 at ε = 0, 0.043499 at ε = 0.01, and φ_s = φ_c = 0.179018 at ε = 0.05.

## Enable

```python
import os, sys
ROOT = os.path.abspath("...")  # algorithmacy-lab root
sys.path.insert(0, os.path.join(ROOT, "third_party"))

from pyphi_iit4_mv import MultivaluedNetwork, exact_phi, maximal_complex
```

## Status

| capability | status |
| --- | --- |
| Ternary / mixed-radix Network | **M1 green** |
| SBS preserved (no log2 collapse) | **M1 green** |
| Exact IIT-4.0 system Φ | **M2 green** |
| Binary regression vs stock | **match** (Φ=2 triad) |
| `maximal_complex` | **M2 green** |
| PyPhi 2.0 `iit4_2023()` parity | **match** (ternary φ_s = 3.169925 = 2 log₂ 3) |

## Limitations

- Alphabet `k_i >= 2`; practical n from `∏ k_i` SBS size.
- GID repertoire distance only (lab default).
- CI-off trap never used.
- The stock binary pin stays the benchmark line. PyPhi 2.0 on upstream `main` is a separate install (`pip install --pre pyphi`) and is not what `ci/reproduce.py` runs.

## Smoke

```
python third_party/pyphi_iit4_mv/smoke_m1.py
python third_party/pyphi_iit4_mv/smoke_m2.py
```
