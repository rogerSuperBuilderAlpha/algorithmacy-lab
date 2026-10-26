# pyphi_iit4_mv — vendored IIT-4.0 multivalued pin (M1+M2)

This overlay is the M1+M2 multivalued IIT 4.0 path for the lab's stock pin, `wmayner/pyphi` `feature/iit-4.0` at `b78d0e342d37175cbd55cf35a6d52ae035b4c50f` (`1.2.1.dev1470+gb78d0e342`, 26 December 2025). `requirements.txt` still installs `pyphi @ git+https://github.com/wmayner/pyphi@feature/iit-4.0`, and `ci/reproduce.py` still calls `pyphi.Network`, `pyphi.Subsystem`, and `pyphi.new_big_phi`. The overlay adds state-by-state TPM ingest and exact IIT-4.0 system Φ for ternary and mixed-radix alphabets, past the `int(log2(...))` collapse.

The same port is packaged on the fork branch `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339ac74aa086112545141306907ab32b4e15` and `4cdda4a1cbf73e89dd368e3991990c3933dd8b48`), open as [rogerSuperBuilderAlpha/pyphi#1](https://github.com/rogerSuperBuilderAlpha/pyphi/pull/1). That branch puts the overlay in `pyphi.multivalued` on top of `feature/iit-4.0` at `b78d0e342`. On the fork, `feature/iit-4.0` itself is at that commit. `develop` is at `f92b981d69c6c2de3887509d21b9b834ae4af906` (11 April 2026), synced with upstream. `2.0` is at `ccd247dcad5dd1c38635bdf1095af82919e3cf37` (17 May 2026).

Upstream `wmayner/pyphi#140`, `#141`, `#142`, and `#147` targeted the legacy `feature/iit-4.0` line. Will Mayner noted on `#147` that `feature/iit-4.0` is superseded by the PyPhi 2.0 release candidate on `main` (`pip install --pre pyphi`). All four pull requests closed on 25 October 2026. Upstream `main` is `134a8f31b49db512322465ed3ba5da7194d362fd` (16 October 2026; tag `v2.0.0rc4`, version line `2.0.0rc5.dev0`). That line replaces `Network` / `Subsystem` / `new_big_phi.sia` with `Substrate` / `System` / `analyze()` (`System.sia()`, `System.phi_structure()`). Mixed-radix state is native: `FactoredTPM` takes an arbitrary `num_states_per_node`.

Under `pyphi.iit4_2023()`, PyPhi 2.0 matches this overlay to machine precision on the ternary conjunctive triad (`num_states_per_node=(3,3,3)`, `S' = min(W,C)` at `(2,2,2)`, φ_s = 1.584963, which is log₂ 3) and matches `feature/iit-4.0@b78d0e342` on the binary conjunctive triad at `(1,1,1)` (φ_s = 2.0; Φ = 4.5, 4 distinctions, 10 relations). The 2.0 default, `pyphi.iit4_2026()`, applies the Mayner, Marshall, and Tononi (2026) cap φ_s = min{φ_c, φ_e, ii(s)} and lowers that ternary state to φ_s = 0.630930 and the binary triad to φ_s = 1.0. The positive triadic verdict (φ_s > 0) remains, and the Φ-structure is unchanged. The majority triad at `(1,1,1)` stays at φ_s = 1.666667 under both presets. That majority triad is the PyPhi majority gate, a separate model from the lab's three-voter rule (Φ_MIP = 0 on the pinned line).

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
| PyPhi 2.0 `iit4_2023()` parity | **match** (ternary φ_s = log₂ 3) |

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
