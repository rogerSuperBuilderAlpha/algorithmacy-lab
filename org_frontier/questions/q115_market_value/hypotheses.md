# Q115 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on how a required market's value distributes as it scales. Q113 found an all-required market
at N=2 splits its value equally between the two unique outer parties and the two agents. This scales the
market to N = 3 and N = 4 and asks who captures the gains: the unique parties or the agents. The agents are
all required, so none is substitutable; the question is whether being required is enough to share in the
growth, or whether scale commoditizes the agents regardless. Written and committed before the run; the
instrument was validated.

## H1 — The market distributes its full value at every N

- **Claim:** At N = 2, 3, 4 the parties' Shapley values sum to the market's Φ (efficiency).
- **H0:** The sum departs from Φ.
- **Predicted outcome:** Σ = Φ at every N. H0 refuted. The Shapley value is exact and the market is fully
  distributed at every scale.

## H2 — The unique outer parties out-earn each agent once N ≥ 3

- **Claim:** At N = 3 and N = 4, each unique outer party's Shapley value exceeds an agent's.
- **H0:** The agents earn at least as much as the outer parties.
- **Predicted outcome:** outer > agent. H0 refuted. Uniqueness, not requiredness, commands the larger share
  once the market grows.

## H3 — The outer parties' value grows with N

- **Claim:** Each unique outer party's Shapley value increases monotonically from N = 2 to 3 to 4.
- **H0:** It does not increase.
- **Predicted outcome:** it grows. H0 refuted. The unique parties capture the value the larger market
  creates. This is the study's genuinely uncertain claim — the gains could equally accrue to the agents who
  do the added work.

## H4 — Each agent's value does not grow with N

- **Claim:** An agent's Shapley value at N = 4 does not exceed its value at N = 2.
- **H0:** Agents' value grows with the market.
- **Predicted outcome:** it does not grow. H0 refuted. The agents are commoditized: adding required agents
  does not raise any agent's share, even though every one is required.
