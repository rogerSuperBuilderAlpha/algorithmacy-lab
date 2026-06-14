# Q8 — parity hub vs conjunctive hub under noise · Stage 1 review

**Question.** Under matched stochastic flip-noise injected into the commit (a probabilistic-TPM commit
that flips with probability p, the Q6/Q7 noise model), does the parity (XOR-family) hub lose its
dyadic/triadic verdict faster than the conjunctive hub at the same size n — comparing, at fixed n (n=3
and n=4), the Φ_MIP(p) decay curves and the noise level at which each form's verdict collapses, and
asking whether the parity hub's already-small clean Φ (Φ = 2^(2−n), Probe 115) makes its verdict more
fragile to noise than the conjunctive hub's (Φ = n−1, Probe 116)?

**Agenda id.** Q8 — parity vs conjunctive noise (follows Q6 probes 140–144, Q7 probes 145–149).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #115 (G3) | The XOR hub stays triadic with the full node set as its core at every size while Φ halves each step: Φ = 2^(2−n) (0.5 at n=3, 0.25 at n=4, 0.125 at n=5). | The clean-Φ baseline for the parity arm. Sets the small starting magnitude (0.5 at n=3, 0.25 at n=4) whose noise-fragility this question tests. |
| #116 (H1) | The AND-all hub holds the full core with Φ = n−1 at n=4–7; OR-all matches. | The clean-Φ baseline for the conjunctive arm. Sets the large starting magnitude (n−1) the parity curve is compared against at matched n. |
| #140–144 (Q6) | Conjunctive-chain commit noise p: Φ_MIP slides smoothly 2.0→0, dΦ/dp monotone-decreasing with max at p=0 (no interior peak), verdict flips to dyadic only in the [0.49,0.50] window — the degenerate coin-flip endpoint. | The exact noise model and method this question reuses (probabilistic-TPM flip with prob p, fine grid, classify on the {W,SC}/full-core MIP). Establishes the *conjunctive* Φ(p) curve and endpoint flip; Q8 adds the parity hub at matched n and asks if its flip comes earlier. |
| #145–149 (Q7) | Moving the same flip from the mediator to the parties reshapes Φ(p) (party noise far steeper near the corner, m_W=102 vs m_S=10) but the verdict still flips only at the degenerate p=0.5 endpoint for the conjunctive form; W and C are one symmetric seat. | Shows that for the conjunctive form the seat changes the *curve* but not the *flip point* — it stays pinned to p=0.5. Q8 changes the commit *function* (parity vs conjunctive), not the seat, and asks whether the function can move the flip point off the endpoint where seat could not. |
| #27 | Mediator reliability r: Φ falls smoothly 2.0→0.14 as r:1.0→0.5; verdict triadic until r=0.5 (random). | The coarse precursor to the conjunctive commit-noise sweep. Same smooth-decay-to-degenerate-endpoint pattern; no parity comparison. |
| #34 | Graded contestability q: Φ falls smoothly 2.0→0.19; triadic until q=1. | Another smooth-decay-verdict-robust-until-the-extreme result, on the conjunctive form. Reinforces the expectation the conjunctive verdict survives to the endpoint; says nothing about parity. |
| #56 (#47) | 8 of 24 triadic family forms are purely higher-order: whole Φ=0.5 with best proper-subset Φ=0.0 — these are the parity determinations; the 16 conjunctive forms are seeded (a pair already has Φ=2.0). | The structural reason a fragility gap is plausible. The conjunctive form has a lower-order seed Φ to fall back on; the parity form's irreducibility lives only in the whole, so noise that erodes the higher-order structure has nothing beneath it. |
| #101 (A3), #102 (A4), #113 (G1) | Φ_AR under-ranks the parity forms; every cheap CES predicate misses exactly the 8 parity forms; the blind spot is exactly the XOR-family Φ=0.5 commits. | Establishes the parity forms as the universal hard case for any magnitude-based detector. Q8 asks the dynamical analogue: is the parity verdict also the first to break under noise, not just the hardest to estimate cleanly? |
| #114 (G2) | MI[W;C] ranks parity-triadic against dyadic at AUC 0.931 — party coupling stays high even though parity Φ is tiny. | Tempers a naive fragility prediction: the parity hub's coupling is not weak, only its Φ magnitude is. Whether the *verdict* (Φ_MIP > 0) is fragile is a separate question from whether the magnitude is small — Q8 must read the binary flip, not just the curve height. |
| #120 (J3) | Φ = 2^(2−n) holds exactly at n=3..7; the law puts Φ below 1e−6 at n>21.9, so the parity hub is numerically dyadic from n=22. | Shows the parity verdict already collapses with *size* alone at a computable point, in exact (noiseless) arithmetic. Q8 asks the orthogonal axis: at fixed small n where the clean verdict is solidly triadic, how much *noise* does the same small Φ tolerate before the flip. |
| #14, #34, #38, batch-5 reading | Under stochastic perturbation Φ degrades smoothly while the verdict is robust until the extreme — the verdict is the stable object, magnitude the sensitive one. | The standing pattern across the logbook, all established on conjunctive/high-Φ forms. Q8 is the first test of whether "verdict robust until the extreme" survives when the starting Φ is 0.5 or 0.25 instead of 2.0 — i.e. whether the robustness was a property of the verdict or an artifact of a large Φ buffer. |
| #61 | A static shared exogenous source leaves the verdict unchanged; true correlated *output* noise needs a state-by-state TPM the state-by-node form cannot express. | The modeling flag Q8 must heed: the parity commit must be noised with the same probabilistic-TPM construction Q6/Q7 used, not a state-by-node approximation, or the parity Φ(p) curve will not be trustworthy. |
| #115 (G3), #132 (Q1) | The parity hub decays (Φ=2^(2−n)) while the conjunctive hub is linear (Φ=n−1); two routes bind the whole group, scaling in opposite directions. | Fixes the two forms being compared and the matched-n design. Q8 takes these two scaling laws and adds noise as a second axis at fixed n. |

## The gap

The noise behavior of the conjunctive form is settled, and the clean (noiseless) scaling of both forms
is settled. Q6 traced the conjunctive commit-noise curve on a fine grid and pinned its verdict flip to
the degenerate p=0.5 endpoint (#140–144); Q7 showed the seat moves the curve but not that endpoint
flip (#145–149); and #115/#116/#120 give the noiseless Φ of each hub at every size, with the parity
verdict collapsing on the *size* axis near n=22. What no probe has run is the matched noise sweep on
the parity hub itself: the same probabilistic-TPM flip-with-probability-p commit, applied to the XOR-all
hub at fixed n=3 and n=4, with its Φ_MIP(p) decay curve and verdict-collapse point placed beside the
conjunctive hub's at the same n. The question this opens is whether a tiny clean Φ buys a fragile
verdict. Two predictions pull apart. The pure-higher-order structure of the parity forms (#56) says
yes — the conjunctive form has a lower-order seed Φ=2.0 to erode through before the whole factors, while
the parity form's entire irreducibility sits in the whole with nothing beneath it, so noise that thins
the higher-order structure could flip the parity verdict at an interior p well below the degenerate
endpoint where the conjunctive verdict holds. The coupling result (#114) and the standing "verdict robust
until the extreme" pattern (#14, #34, #38) say no — the parity hub's party coupling stays high even at
Φ=0.5, and every prior stochastic sweep flipped the verdict only at the degenerate endpoint regardless of
the starting magnitude, so the small Φ may be a magnitude fact that the binary verdict does not inherit.
Which holds — whether the parity verdict breaks first under noise or merely starts lower and still rides
to the same endpoint — is unanswered, and it tests whether the logbook's headline "the verdict is the
robust object, magnitude the soft one" is a real property of the verdict or an artifact of having only
ever been measured on high-Φ conjunctive forms.
