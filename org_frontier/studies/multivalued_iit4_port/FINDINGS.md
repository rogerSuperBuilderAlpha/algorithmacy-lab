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

Beyond-binary **#2–#4** already ran on the overlay. M3, below, records the fork branch and the PyPhi 2.0 parity check. The stock pin stays the benchmark line.

## M3 — fork branch and PyPhi 2.0 parity

The port is on `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339a` and `4cdda4a1`), pull request `rogerSuperBuilderAlpha/pyphi#1`, on top of `feature/iit-4.0` at `b78d0e342`. Upstream `wmayner/pyphi#147` closed on 25 October 2026 after Will Mayner noted that `feature/iit-4.0` is superseded by the 2.0 release candidate on `main` (`134a8f31`, tag `v2.0.0rc4`, version line `2.0.0rc5.dev0`).

On PyPhi 2.0 at `134a8f31` (Python 3.13), a deterministic gate has ii(s) = 0, so `pyphi.iit4_2026` returns φ_s = 0 at ε = 0. The binary conjunctive triad at (1, 1, 1) under `pyphi.iit4_2023` is φ_s = 2.000000 with structure Φ = 12.000000 (4 distinctions, Σφ_d = 5.0; 8 relations, Σφ_r = 7.0), matching the stock pin, and the ternary conjunctive triad at (2, 2, 2) is φ_s = 3.169925 = 2 log₂ 3 (structure Φ = 16.906267). `smoke_m2.py` prints 3.169925 on its 2-node ternary control. Under `pyphi.iit4_2026` both of those deterministic states are φ_s = 0; with noise the binary triad rises to 0.043216, 0.215495, 0.432740, and a peak of 0.610634 at p = 0.20, and the ternary state at (2, 2, 2) is 0.043499 at ε = 0.01 and 0.222002 at ε = 0.05. The three-voter majority triad at (1, 1, 1) is φ_s = 0 under both presets (`len(sia.ties) == 4`). At ternary (1, 1, 1), `pyphi.iit4_2023` returns φ_s = 0.194988 on {W, S, C} and 0.508798 on each dyad, and `pyphi.iit4_2026` returns 0 at ε = 0, 0.043499 at ε = 0.01, and 0.179018 at ε = 0.05. Detail is in [`INSTRUMENT_GAP.md`](INSTRUMENT_GAP.md).

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m2.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```
