# Q6 — Φ phase transition vs smooth decay under commit noise · Stage 1 review

**Question.** For a triadic conjunctive mediated form whose commit flips with probability p (a
probabilistic TPM, S' = W∧C realized only with reliability 1−p), how do Φ_MIP and the dyadic/triadic
verdict move as p rises — and is the verdict transition sharp (a threshold or a kink in Φ or its
derivative) or gradual (the smooth monotone decay the reliability sweeps already showed)?

**Agenda id.** #6 (program task; tracked as Q6 — noise phase transition, probes 140–144).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #27 | Mediator reliability r: Φ falls smoothly 2.0→1.54→1.19→0.68→0.35→0.14→0 as r goes 1.0→0.5; verdict holds triadic until r=0.5 (random), where Φ=0. | The closest existing answer. Same commit (S'=W∧C) and the same output-noise model this question names (commit flips with prob 1−r). The curve looks smooth and the verdict flips only at the random endpoint — but it was sampled at 7 coarse points, never differentiated, never tested for a kink. |
| #38 | Asymmetric reliability r_c (system's read of the counterpart): Φ falls smoothly 2.0→0.88→0.71→0.44→0.20→0; triadic until r_c=0 (counterpart fully invisible). | A second smooth monotone decay on a related noise axis. The drop from r_c=1.0 to 0.9 is large (2.0→0.88), hinting the curve may not be smooth near the clean limit — a non-smoothness this question would catch with a fine sweep. |
| #34 | Graded contestability q: Φ falls smoothly 2.0→0.86→0.62→0.42→0.19→0; triadic until q=1 (full autonomy). | Same qualitative shape — smooth Φ decay, verdict robust until the extreme — on a different stochastic parameter. Establishes the "magnitude sensitive, verdict robust to the endpoint" pattern the question asks whether commit noise also follows. |
| #81 | Criticality sweep (tracking phase p): Φ is symmetric, 2.0 at both deterministic extremes and 0 at p=0.5 (random) — a trough, not an interior peak. No critical Φ maximum found. | The one probe that explicitly looked for non-monotone / critical-point structure on a noise-like axis and found none. It sweeps party tracking, not the commit flip, so it does not settle whether the commit-noise axis itself has a threshold or kink. |
| #14, #34, #27, #38 | Recurring result: under stochastic perturbation Φ degrades smoothly while the verdict is the robust binary object, flipping only at the extreme. | The standing generalization this question stress-tests at fine resolution for the commit-flip parameter specifically. |
| #26, #33 | The triadic conjunctive form's MIP cuts at {W,SC}, the worker the most separable seam. | Fixes the partition whose Φ the sweep reads; lets the question report not just Φ_MIP but whether the MIP itself moves as noise rises. |
| #79 | An adapting mediator walks Φ 2.0→0.71→0.44→0.20→0 across epochs and crosses to dyadic at the final epoch — a dynamic version of the reliability decay. | Shows the verdict crossing happens at the degenerate endpoint here too, not at an interior threshold. |

## The gap

The reliability sweeps already trace Φ against commit noise for exactly this form, and they show a
smooth monotone fall with the verdict holding triadic until the noise reaches its degenerate maximum
(Probe 27: r=0.5, the random commit; Probe 38: r_c=0). So the headline answer the question expects —
decay, not a phase transition — is strongly suggested. Three things keep the question open. The
reliability curves were sampled at six or seven coarse points and never differentiated, so a kink or a
threshold in Φ or dΦ/dp between sample points would have been missed; whether the decay is analytically
smooth or has a critical point is not actually established, only sketched. The verdict flip in every
prior sweep sits at the degenerate endpoint (the commit becomes a coin flip, or a party becomes
invisible), which is a trivial collapse rather than an interior phase transition — but no probe has
asked whether a finite, interior critical p exists below which the triad survives and above which it
factors, the way an order parameter crosses zero at a critical temperature. And no probe has reported
Φ_MIP as a continuous function of a single clean commit-flip parameter p on a fine grid, checked the
MIP location for movement, or framed the result against organization/coordination theory's distinction
between graceful degradation and a coordination regime change. Probe 27 nearly answers this; it does not
close it, because its coarse, undifferentiated curve cannot distinguish a smooth decay from a hidden
threshold, and it never poses the interior-critical-point question that "phase transition" actually
asks. The pieces strongly imply smooth decay with no interior transition; the fine-grained sweep,
the derivative check, and the explicit phase-transition framing have not been run.
