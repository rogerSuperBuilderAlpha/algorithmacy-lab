# MARL emergent learn — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #41).** In multi-agent RL, does the
emergent coordination structure’s exact IIT-4.0 verdict predict whether
the agents can learn the task — a behavioral test the static ABM nulls
#98 / #107 left open?

**Already known (cited, not reopened).**
- #98: designed-form verdict ̸↔ independent Q-bandit difficulty
  (rank-AUC 0.567).
- #107: same null under fictitious-play / partner modeling (AUC 0.541).
- #37–#40 AI lane: PROTOCOL_IS_COMMIT, TOOL_LIKE_INFERENCE,
  HUMAN_COMMIT_READ, SHARP_FULL_DISPLACE — pointers only.
- Formal / stoch–temporal / estimation / construct-omit closed.

**Universe / honesty.** Controlled **tabular stateful Q-learning
proxy** (two agents; state = last commit bit; ε-greedy). **Not** deep
MARL (no MAPPO/QMIX, no continuous control). After training, embed
greedy policies into Boolean `(W,S,C)` rules and read exact Φ. Candid
N: designed commit panel × seeds.

**Definitions (fixed).**
- **Task:** binary commit `S=f(W,C)`.
- **Designed form:** `W'=S`, `S'=f(W,C)`, `C'=S` (classical skeleton).
- **Emergent form:** `W'=π_W(S)`, `S'=f(W,C)`, `C'=π_C(S)` from
  learned greedy policies.
- **Success:** mean reward in final window ≥ 0.7.
- **Difficulty:** episodes to 10-in-a-row reward=1 (cap EPISODES).
- Association only — no causal claim.

## H1 — emergent structure predicts learnability

Rank-AUC of emergent-triadic predicting success is ≥ 0.65, **or**
(when needed as a secondary cut) predicting above-median ease
(`1 − difficulty/EPISODES`) is ≥ 0.65. Null: both AUCs < 0.65.
## H2 — designed verdict still fails (#98 replicate on this panel)

Rank-AUC of difficulty predicting designed-triadic is ≥ 0.65. Null:
AUC < 0.65 (replicates #98).

## H3 — success on designed-triadic tasks yields emergent triadic

Among successful runs on designed-triadic commits, a majority are
emergent-triadic. Null: most succeed with non-triadic emergent
structure (open-loop witness expected).
