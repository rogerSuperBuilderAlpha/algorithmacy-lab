# Residual phase boundary — findings (F28)

**F28 verdict: the near-boundary holistic forms sit on a Φ verdict phase boundary (H1, H2), but
that instability is shared with other classifier-uncertain forms (H3 refuted).** One-bit flips in
the truth tables flip the exact IIT-4.0 verdict for **48.2%** of neighbours of near-boundary
residual forms; every such seed has at least one flipping neighbour. Confident (far-hit) forms are
materially more stable (27.3%). Near-hit controls flip at **52.1%** — no residual-specific excess.

In-silico; exact Φ. Hypotheses fixed in `hypotheses.md` before computing. F26/F27 not reopened.

## Census table

| set | n | mean one-bit flip rate | frac with ≥1 flip |
|---|---|---|---|
| near-boundary residual (`\|p−0.5\|<0.25` RF misses) | 178 | **0.482** | **1.000** |
| near-hit control (correct, same band) | 176 | 0.521 | 1.000 |
| far-hit control (correct, `\|p−0.5\|≥0.40`) | 178 | 0.273 | 0.921 |

| hypothesis | result | detail |
|---|---|---|
| H1 mean ≥ 0.25 and ≥80% any-flip | **SUPPORTED** | 0.482; 100% any-flip |
| H2 residual − far-hit ≥ 10 pp | **SUPPORTED** | +20.9 pp |
| H3 residual − near-hit ≥ 5 pp | **REFUTED** | −3.9 pp |

## Reading

Probe 131's near-boundary residual is not a quiet island. A single bit flip in any node's table
changes the exact dyadic/triadic verdict almost half the time, and no seed in the set is locally
stable. That is a phase boundary in Boolean function space relative to typical, classifier-confident
forms (H2).

It is not a *residual-only* boundary. Forms the forest gets right while sitting in the same
`|p−0.5|<0.25` band are at least as unstable (H3). The phase structure tracks the near-boundary
region of cheap-feature probability space — where the panel is unsure — rather than the
misclassification label itself. The holistic residual lives on that unstable sheet; it does not
define a sharper one.

## Scope

- Universe: Probe-125 4096 wirings; residual via Probe-131 RF protocol.
- Perturbation: 12 Hamming-1 neighbours per seed (one bit × three 4-bit tables).
- Near-hit pool had 176 forms vs 178 residuals; the full pool was used (means compared).
- Sweep runtime ~7 minutes for 532 seeds × 12 exact-Φ evaluations; results committed under
  `results/`.

## Best next experiment

Section F is closed at n=3–4 for residual rate, affine class, and phase boundary. Natural
continuations: **F26 at n=5** (does the miss rate keep shrinking under SM sampling?), or a
**class-balanced n=4** residual panel so F26's shrink is not majority-class dominated; or move to
agenda **G** (political economy / coalition design).

## Reproduce

```
python org_frontier/studies/residual_phase_boundary/analyze_phase_boundary.py
python org_frontier/studies/residual_phase_boundary/analyze_phase_boundary.py --rebuild
```
