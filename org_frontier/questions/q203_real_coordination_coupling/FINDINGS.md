# Q203 findings — the lab's first real coordination, read four ways

This is the program's first contact with real data. A real two-party coordination — two people building with
LEGO, their dominant-hand movement recorded over 5799 time points (the `handmovement` dyad from the crqa
package) — is read by four behavioral coupling measures at once: cross-recurrence quantification, transfer
entropy, Granger causality, and convergent cross mapping. Each directed measure is validated on a control in
its own domain before it touches the real data.

## Instrument controls

A linear AR system with a known X→Y drive: transfer entropy and Granger causality both read X→Y (TE
difference +0.69 bits, Granger F difference +1716). A coupled chaotic logistic system with a known X→Y drive,
which is CCM's proper domain: CCM reads X→Y (Y-cross-maps-X 0.976 against X-cross-maps-Y 0.008). CONTROL PASS.
CCM was put on a deterministic control because it failed the linear one — a real result in itself: CCM's
direction logic holds for nonlinear deterministic coupling, not linear-stochastic coupling.

## The real dyad

| measure | value | direction | surrogate p |
|---|---|---|---|
| CRQA | %REC 4.96, %DET 59.8 | symmetric | — |
| transfer entropy | P1→P2 0.0248, P2→P1 0.0327 bits | P2→P1 | 0.078 |
| Granger F | P1→P2 1.15, P2→P1 3.03 | P2→P1 | 0.510 |
| CCM ρ | P1-xmap-P2 0.104, P2-xmap-P1 0.057 | P2→P1 | 0.235 |

## Verdicts

- **H1 (all three directed measures reach significance): NOT SUPPORTED.** None clears its circular-shift
  surrogate at p < .05 (0.078, 0.510, 0.235).
- **H2 (the directed measures agree on direction): SUPPORTED.** All three point P2→P1.

## What it says

CRQA reads strong recurrent structure: 59.8% of the recurrent points lie on diagonal lines, so the two
players' hand movement is genuinely coordinated, not coincidental. That structure is symmetric and says
nothing about who leads.

The three directed measures agree in sign — all three make P2 the driver — yet none is individually
significant against surrogates. The directional signal is consistent but weak. A researcher holding any one
of these measures would not confidently call the direction, even though all three, seen together, lean the
same way.

This is the real-data face of the synthetic null (q153–162). On synthetic forms the behavioral measures
failed to recover the structural verdict by disagreeing with it. On this real dyad they fail to recover a
confident directional verdict for a different reason: the signal sits below significance, while the agreement
in sign that does exist would be invisible to any single measure. Either way, behavioral coupling alone does
not deliver a coordination verdict one could stand on.

## Scope

A single real dyad, one channel (dominant-hand transfer), a worked real-data example rather than a
population. No exact Φ is computed: real time series carry no ground-truth transition function, so this is the
behavioral-recovery side of the bridge, the side that can be run on observed data. The estimator settings
(six-bin transfer entropy, AR order five, embedding dimension three, 50 surrogates) are fixed in the probe.
The data is committed at `data/handmovement.csv` and is refetchable from CRAN package `crqa`,
`data(handmovement)`. A population study across many dyads is the next step, and the
[`DATA_SOURCES.md`](../../../research/DATA_SOURCES.md) note lists larger open corpora (GaMMA, CANDOR,
hyperscanning releases) for it.
