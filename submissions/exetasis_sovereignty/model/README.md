# Threshold-contagion check of the §4 claim

[Written by Claude, 26 Oct 2026, from Antonio Scala's model specification in `../PLAN_SCALA_2026-10-25.md` §5. Antonio's own `coordinative_sovereignty_sim.py` is not in this repo; this is an independent reimplementation to check whether the abstract may report the result.]

**Spec followed:** ring of K = 8 cliques of n = 10; neighbouring cliques joined by w random bridge ties; threshold rule, a node activates once the active signal from its neighbours reaches θ = 2; seed is one whole community; a competent active node emits signal 2 instead of 1; three conditions (no competence, B = 16 competent nodes at random, B = 16 at bridge endpoints); reach = fraction eventually active, mean of 200 realisations.

**Result** (`RESULTS_2026-10-26.txt`): at w = 1, reach is 0.12 with no competence, 0.14 with random competence, 1.00 with competence at bridge endpoints. Random competence only approaches that reach at B = 64 of 80 nodes (0.53). At wider bridges (w ≥ 4) random competence catches up (0.44 to 0.71) and the bridge advantage narrows.

**Reading.** The claim in the abstract holds in this model: competence compensates for thin bridges only when it sits at bridge positions. Two cautions for §4 and §7 of the paper:
1. The result is close to built in. With θ = 2 and competent weight 2, a competent node makes every tie it touches a simple-contagion tie. Bridge placement therefore works because it converts the one bridge tie and the receiving node's clique ties at once. The paper should present this as a how-possibly illustration, as Antonio's plan already says, and should not describe it as a finding about platforms.
2. At w ≥ 2 the bridge condition sits at 0.72–0.80 rather than 1.00 because the budget of 16 no longer covers every bridge endpoint and the sampled endpoints sometimes miss a crossing. A robustness check with competence placed on both endpoints of each selected bridge would tidy the curve.

Run: `python3 -I cs_sim.py` (numpy only).
