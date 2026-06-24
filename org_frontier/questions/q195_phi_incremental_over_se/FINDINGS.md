# q195 — findings

On the simulated cohort Φ_coord carries association with ACS-total that survives controlling for
general self-efficacy and belonging, and it tracks the algorithmacy factor more tightly than it tracks
the self-efficacy factor. The bridge measure is not a restatement of generic competence.

Self-efficacy correlates with ACS at +0.45 by construction, so the partialling in H1 is a genuine test.
After SE and belonging enter as a nuisance block, adding Φ_coord raises R² from 0.207 to 0.336
(ΔR² = +0.129), and the partial correlation r(Φ_coord, ACS | SE, BE) is +0.40 with a 95% CI that
excludes 0. Φ_coord correlates with ACS at +0.40 but with SE at only +0.10; the bootstrap CI on the
difference excludes 0.

Instrument control passed: the faithful triad `[x1, x0&x2, x1]` reads triadic with max Φ_MIP = 2.0.

| quantity                          | value   | 95% CI             |
|-----------------------------------|---------|--------------------|
| r(Φ_coord, ACS)                   | +0.4044 | —                  |
| r(Φ_coord, SE)                    | +0.1034 | —                  |
| r(SE, ACS)                        | +0.4503 | —                  |
| partial r(Φ_coord, ACS \| SE, BE) | +0.4037 | [+0.3180, +0.4828] |
| ΔR² (Φ_coord over SE + BE)        | +0.1293 | —                  |
| Δ = r(Φ,ACS) − r(Φ,SE)            | +0.3011 | [+0.2029, +0.3935] |

N = 400; 53 commit forms, 347 convey forms.

- **H1: SUPPORTED.** Partial r = +0.4037, 95% CI [+0.3180, +0.4828]: above 0.15 and the interval
  excludes 0. Φ_coord adds incremental association beyond SE and belonging (ΔR² = +0.129).
- **H2: SUPPORTED.** Δ = +0.3011, 95% CI [+0.2029, +0.3935]: the interval excludes 0. Φ_coord tracks
  the algorithmacy factor (+0.40) more tightly than the self-efficacy factor (+0.10).

Scope: the cohort is simulated. No worker is measured. The result is evidence about the Φ bridge's
discriminant validity on synthetic data, and depends on the planted structure in which algorithmacy and
coordination share a latent that self-efficacy does not reach. Whether a real cohort separates this way
is open; the validation gap is the unfielded survey.
