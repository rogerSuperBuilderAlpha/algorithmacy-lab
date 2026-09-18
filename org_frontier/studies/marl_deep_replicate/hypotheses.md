# MARL deep replicate — hypotheses (fixed before computing)

**Question.** Does the emergent coordination structure’s exact IIT-4.0
verdict predict learnability under a **deeper** MARL setup than the
tabular proxy in `marl_emergent_learn/` (#41 EMERGENT_NULL) — or does
the null survive?

**Already known (cited, not reopened).**
- #41 EMERGENT_NULL: tabular stateful Q-learn; AUC emerg→success 0.555;
  AND open-loop success; extends #98/#107.
- #37–#40 pointers only. AI_MULTIAGENT_ARC otherwise closed.
- Formal / stoch–temporal / estimation / construct-omit closed.

**Universe / honesty.** Smallest honest step up from tabular:
**neural / linear function-approx Q-policies** with a **larger
observation** `[S, own_last, partner_last]` (not 1-bit S alone).
NumPy MLP (hidden=8) and linear FA — **not** MAPPO/QMIX/GPU deep
MARL. Exact Φ on **binarized** greedy policy tables embedded into
`(W,S,C)`. Candid N: same commit panel × modest seeds; association
only.

**Definitions.** Same success / difficulty / emergent embed logic as
#41, with π read from the function approximator over all 8 binary
obs. AUC_THR = 0.65.

## H1 — deep MARL restores predictive association

On the primary MLP architecture, rank-AUC of emergent-triadic
predicting success **or** above-median ease is ≥ 0.65. Null: both
< 0.65.

## H2 — EMERGENT_NULL survives

H1 fails on the primary MLP, **and** designed-triadic tasks that
succeed still show majority non-triadic emergent structure (open-loop
witness class, as in #41). Null: H1 holds, or success restores
emergent triads.

## H3 — partial (architecture / curriculum)

Exactly one of {MLP, linear FA} meets the AUC ≥ 0.65 learnability
cut, or the two architectures disagree on whether success restores
emergent triadic on designed-triadic tasks. Null: both restore or
both fail alike.
