# WHO BROKE PROD? — findings

**Verdict: ACCESS_DECIDES_RELAY_DISTORTS.** In this simulator, checking cited events against the trace
is the largest single lever on attribution accuracy, and chain relaying is the largest topology cost. A
forwarding hub mediator adds a round and no accuracy. Three of six preregistered hypotheses are
supported and three are refuted.

Evidence about the model, not about a real organization. No Φ is computed in this study, and no
relationship between Φ and attribution accuracy is claimed.

Run: 2400 deterministic runs (4 scenarios × seeds 0..49 × 3 topologies × 2 incentives × 2 access);
200 paired (scenario, seed) units per cell with common random numbers. Hypotheses fixed in
`hypotheses.md` before the run. Numbers recomputed by `analyze_who_broke_prod.py` from
`results/runs.csv`.

## Cells (self-protective incentive)

All neutral-incentive cells read accuracy 1.000 (the culprit confesses with a valid citation).

| topology | access | accuracy [Wilson 95%] | false blame | abstain | mean steps |
|---|---|---|---:|---:|---:|
| flat | full | 0.775 [0.712, 0.827] | 0.225 | 0.000 | 1.48 |
| flat | claims_only | 0.130 [0.090, 0.184] | 0.760 | 0.110 | 1.00 |
| hub | full | 0.775 [0.712, 0.827] | 0.225 | 0.000 | 2.07 |
| hub | claims_only | 0.130 [0.090, 0.184] | 0.760 | 0.110 | 2.00 |
| chain | full | 0.390 [0.325, 0.459] | 0.580 | 0.030 | 1.50 |
| chain | claims_only | 0.030 [0.014, 0.064] | 0.970 | 0.000 | 1.33 |

Mean steps average only the runs that reach a stable correct attribution.

## Hypotheses

| H | result | numbers |
|---|---|---|
| H1 trace access raises accuracy (≥0.10, p<0.01) | **SUPPORTED** | 0.6467 vs 0.0967, diff 0.5500, p = 9.144e-100 |
| H2 trace access halves false blame | **SUPPORTED** | 0.3433 vs 0.8300 |
| H3 incentive matters only without access | **REFUTED** | Δ false blame 0.8300 claims-only, 0.3433 full (threshold ≤0.05) |
| H4 steps flat ≤ hub ≤ chain | **REFUTED** | flat 1.4839, hub 2.0710, chain 1.5000 |
| H5 chain costs ≥0.10 accuracy vs flat | **SUPPORTED** | 0.7750 vs 0.3900, diff 0.3850, p = 1.323e-23 |
| H6 hub gains ≥0.05 accuracy vs flat | **REFUTED** | 0.7750 vs 0.7750, diff 0.0000, p = 1.000 |

## Mechanisms

Each reading below is evidence about the model, not about a real organization.

- **H1, H2.** With access, a scapegoat claim citing the red-herring event (a change after the first
  alert) or a fabricated event id is refuted, and a witness's citation of the causal event is
  supported. Without access the investigator takes a plurality of accusations, which self-protective
  bystanders dominate.
- **H3 refuted.** Claims that cite no event cannot be refuted. Once the cited scapegoat claims are
  refuted, the investigator's fallback plurality over the remaining uncited claims still lands on an
  innocent agent when no witness exists. The incentive therefore raises false blame under full access
  too. This is a property of the investigator rule, fixed before the run.
- **H4 refuted.** Chain's mean steps (1.50) fall below the hub's (2.07) because chain successes are
  selected toward runs where a witness sits near the investigator's end of the chain and arrives early.
- **H5.** Each chain hop drops a citation with probability 0.15, and a self-protective relay that is
  itself accused rewrites the accusation and strips the citation. Distant claims also arrive late.
- **H6 refuted.** The hub mediator's single check is the same most-repeated claim the investigator
  would verify first, so the mediator adds one round of latency and no information.

## Limits

Scripted agents, four hand-built scenarios, designer-chosen parameters (witness p 0.35, fabricate p
0.5, chain drop p 0.15, budget 1 check per round, deadline 5) and a designer-chosen investigator rule.
Several effects are partly built in by design; the run tests whether the specified mechanisms produce
effects of the stated size. Association across designed conditions only. No live LLM calls. No Φ.

## Reproduce

```
python org_frontier/studies/who_broke_prod/analyze_who_broke_prod.py
```
The saved run reproduces exactly: all 12 cells match the prototype's `summary.json` (accuracy, Wilson
bounds, false blame, abstain, mean steps, mean messages) and all six decisions match.
