# Noise × composed carriers — findings

**Verdict: SAME_PSTAR_COMPOSED.** Party and mediator flip-noise still
share **p\*=0.5** on a composed **AND necklace** and a **shared-mediator
span** (shared_k2), matching the single-hub control. V2 #7’s coin-flip
threshold survives composition.

In-silico; exact binary IIT-4.0; flip-noise as in V2 #7. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V3 #12. Grows from V2 #7
`SAME_THRESHOLD_DIFF_CURVE`, V3 #4 necklace, V3 #6 shared-mediator.

## Already known

| prior | result |
|---|---|
| V2 #7 party vs mediator noise | SAME_THRESHOLD_DIFF_CURVE — p\*=0.5 both seats |
| V2 #6 commit-noise phase | SMOOTH_DECAY |
| V3 #4 AND necklace | ring landmark Φ=4 |
| V3 #6 shared-mediator k | merge Φ=2k |

## Panel (first dyadic p\*)

| carrier | n | p\*_mediator | p\*_party | max interior \|ΔΦ\| |
|---|---:|---:|---:|---:|
| hub3 (control) | 3 | **0.50** | **0.50** | 0.426 |
| shared_k2 (span) | 5 | **0.50** | **0.50** | 0.206 |
| necklace | 6 | **0.50** | **0.50** | 0.000 |

All six locus×carrier cells remain triadic through p=0.49 and flip to
dyadic at p=0.50. Necklace party and mediator Φ curves overlay on this
grid; hub and shared_k2 keep locus-shaped Φ gaps (V2 #7 DIFF_CURVE
residue on those carriers).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 hub3 control p\*=0.5 both seats | **SUPPORTED** |
| H2 composed seats share p\* | **SUPPORTED** |
| H3 composed p\* stays 0.5 | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Composition does not move the collapse threshold. Necklace and
shared-mediator span inherit the hub’s coin-flip p\* for both seats.
What composition can change is **curve shape** (necklace flattens the
party/mediator Φ gap on this grid); it does not split or shift p\*.

Validation gap: evidence about Boolean models under column flip-noise,
not about real organizations or other noise families (#5 correlated TPM).

## Best next (V3)

**#13** validation bridge (weakest Boolean render of a real coordination
log). Alternate **#15** estimation residual if the priority is
topology-aware imputation after role-gated collapse.

## Reproduce

```
python org_frontier/studies/noise_composed_carriers/analyze_noise_composed.py
```

(default loads committed sweep; `--rebuild` recomputes exact Φ, ~8 min)
