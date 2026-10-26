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

Under `pyphi.iit4_2023()`, PyPhi 2.0 at `134a8f31` matches this overlay and the pinned line to machine precision: binary conjunctive triad `(1,1,1)` φ_s = 2.0 (Φ = 4.5, 4 distinctions, 10 relations); majority triad `(1,1,1)` φ_s = 1.666667; ternary conjunctive triad (`num_states_per_node=(3,3,3)`, `S' = min(W,C)`) at `(2,2,2)` φ_s = 1.584963 (log₂ 3). Under `pyphi.iit4_2026()`, the ii(s) cap of Mayner, Marshall, and Tononi (2026) leaves the majority triad at 1.666667, lowers the binary triad to φ_s = 1.0 with that Φ-structure unchanged, and lowers the ternary state to φ_s = 0.630930. All three stay positive (φ_s > 0). The majority triad in this check is the PyPhi majority gate, separate from the lab's three-voter rule (Φ_MIP = 0 on the pinned line). Detail is in [`INSTRUMENT_GAP.md`](INSTRUMENT_GAP.md).

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m2.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```
