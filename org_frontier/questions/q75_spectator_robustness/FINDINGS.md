# Q75 findings — spectator robustness of the core

All four hypotheses confirmed. The triadic core is robust: adding spectators of any non-bidirectional
coupling class leaves the maximal complex {E, M, R} at Φ=2.0.

| form | maximal complex | Φ |
|---|---|---|
| triad + 1 uncoupled spectator | {E, M, R} | 2.0 |
| triad + 2 uncoupled spectators | {E, M, R} | 2.0 |
| triad + 3 uncoupled spectators | {E, M, R} | 2.0 |
| triad + read-only spectator | {E, M, R} | 2.0 |
| triad + emit-only spectator | {E, M, R} | 2.0 |

From `probe_spectator_robustness.py`.

## What it says

The triadic core is stable under added spectators. Idle parties, observers that read the mediator without
being read, and constant sources the determination ignores all stay outside the maximal complex, which
holds at {E, M, R} with Φ=2.0 as one, two, or three are added. The verdict the lab reports on the maximal
complex does not move when the coordination is surrounded by non-participating parties. This is the
stability that makes the Q74 reporting rule trustworthy: a spectator is genuinely outside the core, and
adding more does not perturb it.

## Caveats

- **Confirmatory.** The robustness predictions held; the contribution is the demonstrated stability.
- **In-silico.** Boolean models, evidence about the models. Φ read ordinally.
- **Non-bidirectional only.** Robustness is shown for spectators that are uncoupled, read-only, or
  emit-only. A bidirectionally-coupled added party can join the core if pivotal (Finding 8), which is the
  Q74 localization case, not tested here.
