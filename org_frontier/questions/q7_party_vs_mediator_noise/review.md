# Q7 — party noise vs mediator noise · Stage 1 review

**Question.** In a triadic conjunctive mediated form (worker W, mediator/system S, counterpart C),
does injecting stochastic output-flip noise into the parties' updates (W and C, probability p) collapse
the triad at the same Φ(p) curve and the same verdict-flip point as injecting the same noise into the
mediator's commit (S) — or do the two noise sites have asymmetric effects on Φ_MIP and the
dyadic/triadic verdict?

**Agenda id.** Q7 — party vs mediator noise (follows Q6, probes 140–144).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #140–144 (Q6) | Commit noise p (S' = W∧C flips with prob p) on the conjunctive chain: Φ_MIP slides smoothly 2.0→0, dΦ/dp is monotone-decreasing with its max at the p=0 endpoint (no interior peak), and the verdict flips to dyadic only in the [0.49,0.50] window — the degenerate coin-flip endpoint. | The direct baseline. Establishes the *mediator-noise* Φ(p) curve and verdict-flip point this question compares party noise against. Q7 is the same experiment with the flip moved from S to W and C. |
| #27 | Mediator reliability r: Φ falls smoothly 2.0→1.54→1.19→0.68→0.35→0.14→0 as r:1.0→0.5; verdict triadic until r=0.5. | The original coarse mediator-commit-noise sweep Q6 refined. Same noise site (S), same smooth-decay-to-degenerate-endpoint pattern Q7 tests for the party site. |
| #38 | Asymmetric reliability r_c (system's *read* of the counterpart degrades): Φ falls smoothly 2.0→0.88→0.44→0.20→0; triadic until r_c=0. | Noise on the S←C *channel*, not on C's own output. The closest existing thing to "counterpart-side" noise, but it degrades the mediator's perception of C rather than C's commit. Q7 asks about noise injected into C's own update — a different site that #38 does not isolate. |
| #34 | Graded contestability q (worker ignores the commit with prob q): Φ falls smoothly 2.0→0.86→0.42→0.19→0; triadic until q=1. | A stochastic perturbation on the *worker's* read of S, the closest existing worker-side noise. It is a decoupling (W stops reading S), not an output flip on W's update, so it does not answer whether flipping W's own commit matches the mediator curve. |
| #81 | Criticality sweep on party tracking phase p: Φ symmetric, 2.0 at both deterministic extremes, 0 at p=0.5 — a trough, no interior peak. | The one probe that sweeps a *party*-side stochastic parameter and looks for non-monotone structure. It varies how the parties track, not an output flip, and it studies one combined party parameter, never W-vs-C-vs-S asymmetry. |
| #16 | Every triadic form has influence-asymmetry 0 (balanced); any asymmetry → dyadic. "Neither party controls" = equal influence. | Predicts the noise sites should matter symmetrically *if* noise acts like influence. Gives a reason to expect party and mediator noise to differ: the conjunctive commit reads W, C, and the S-feedback through different structural roles, so equal output noise need not act equally on Φ. |
| #26, #33 | The triadic conjunctive form's MIP cuts at {W,SC} — the worker is the most separable seam; S and C cohere more tightly. | Fixes the partition the sweep reads and predicts an asymmetry direction: noise on W sits on the weak side of the cut, noise on S sits inside the tightly-bound {S,C} block, so the two sites may load on Φ differently. |
| #55 | W↔C swap is an exact verdict automorphism (0/256 flips, 0 Φ difference). | Predicts W-noise and C-noise give identical curves to each other, so "party noise" can be reported as one curve. It says nothing about party-vs-mediator, which breaks the symmetry (S is not interchangeable with W or C). |
| #61 | A static shared exogenous source both parties read leaves the verdict unchanged; true correlated *output* noise needs a state-by-state TPM the state-by-node form cannot express. | A modeling flag Q7 must heed: injecting independent output-flip noise into W and C simultaneously is the per-party version of the output noise #61 found the state-by-node form cannot carry. Q7 needs the same probabilistic-TPM construction Q6 used, applied at the party nodes. |

## The gap

The mediator-noise side of this question is settled. Q6 (probes 140–144) traced Φ_MIP against a clean
commit-flip parameter on a fine grid, differentiated it, and pinned the verdict flip to the degenerate
p=0.5 endpoint, and #27 and #38 gave the coarse precursors. What no probe has run is the matched
experiment with the flip moved off the mediator and onto the parties. The worker-side and
counterpart-side perturbations that exist — contestability (#34) and channel reliability (#38) — are
decouplings or perception-degradations, not output flips on W's and C's own updates, so neither is the
same noise model at a different site. #81 sweeps a party parameter but a tracking phase, not an output
flip, and never separates W, C, and S. So the comparison the question asks for — same noise model, same
form, same fine grid, mediator site versus party site, read on the {W,SC} MIP — has not been made, and
the two structural predictions point in opposite directions. Role symmetry (#55) and the balanced-influence
result (#16) suggest the parties and the mediator might load on Φ identically, since the conjunctive commit
treats its inputs evenly. The MIP geometry (#26, #33) suggests the opposite: the worker sits on the weak
seam of the cut while the mediator sits inside the tight {S,C} block, so equal output noise at the two
sites need not produce the same Φ(p) curve or flip point. Whether party noise and mediator noise yield one
curve or two — and if two, whether party noise flips the verdict at an interior p below the degenerate
endpoint where mediator noise flips it — is open, and it is the live question once the state-by-node
modeling limit (#61) is handled with the same probabilistic-TPM construction Q6 used.
