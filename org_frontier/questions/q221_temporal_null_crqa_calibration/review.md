# Q221: Stage 1 review (DRAFT)

**Question.** Two questions:
1. Under nulls that preserve each channel's temporal dependence, are recurrence-based coupling tests
   calibrated?
2. Does the pairwise recurrence representation that q220 uses carry enough information to identify the q161
   exact-Φ bottleneck target?

**Agenda id.** This is a follow-up to q220 (PR #827, plus the corrections in #841). It has no agenda number.

## Prior work that bears on this

| source | finding | how it relates |
|---|---|---|
| q220 (`../q220_observation_process_robustness/`) | Bottleneck-pick drop under observation corruption; the shuffle null destroys within-channel dependence | Motivates both tracks |
| q161 (`../q161_noise_robust_verdict/`) | Defines the leave-one-out bottleneck target used as ground truth | This is the target whose identifiability Q221 examines |
| `org_frontier/research/recurrence/REVIEW.md` | CRQA and DCRP are descriptive; TE and CCM are for directional claims | Anchor for `literature/NOVELTY_ASSESSMENT.md` |

## The gap

Two pieces of prior work are already established:
- naive shuffles are miscalibrated under autocorrelation (Yuan & Shou 2022);
- pairwise statistics miss higher-order structure (Williams & Beer 2010; Gilpin 2025).

What had not been established is whether, inside the lab's own Boolean family, the pairwise recurrence
representation determines the transition law and the q161 target. The exploratory answer is no
(`FINDINGS.md`).
