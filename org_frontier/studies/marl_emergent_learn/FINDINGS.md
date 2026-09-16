# MARL emergent learn — findings

**Verdict: EMERGENT_NULL.** After tabular stateful Q-learning, the
**emergent** coordination structure’s exact verdict does **not**
predict task learnability (AUC emerg→success 0.555; emerg→easy 0.485).
The designed-form verdict still fails as a difficulty predictor
(#98-like AUC 0.456). Successful learners of designed-triadic commits
(AND/OR/NAND) systematically induce **open-loop non-triadic** policies
(`π=[1,1]/[1,1]`). Extends #98/#107; association only — not causal.
Candid: controlled tabular proxy, **not** deep MARL.

In-silico; N=110 (11 commits × 10 seeds). Hypotheses fixed in
`hypotheses.md`. Cited: #98/#107; #37–#40 pointers only. Other lanes
closed.

## Hypotheses

| H | result |
|---|---|
| H1 emergent predicts learnability | **REFUTED** |
| H2 designed verdict predicts difficulty | **REFUTED** |
| H3 success ⇒ emergent triadic on des-tri | **REFUTED** |

## Panel (selected)

| task | designed | mean diff | succ | emerg triadic |
|---|---|---:|---:|---:|
| AND / OR / NAND / NOR | triadic | 21–105 | 1.0 | **0.00** |
| XOR / XNOR | triadic | ~81 | 1.0 | 0.40–0.70 |
| W_only / C_only / implies | dyadic | 33–68 | 1.0 | 0.00 |
| const0 (unreachable) | dyadic | 300 | 0.0 | 0.00 |

## Witnesses

- **Open-loop success:** all 10 AND seeds succeed with
  `π_W=π_C=[1,1]` → emergent dyadic / empty core — hit the commit
  without a feedback triad.
- **P(emerg_tri | success ∧ designed_tri) = 0.183** — success does
  not restore the designed triad in the learned loop.
- Designed→success AUC 0.80 is a **const0 artifact** (only failure
  class); difficulty→designed stays near chance (0.456).

## Reading

The gap #98/#107 left open does not close when Φ is read on the
*learned* policy loop instead of the designed form. Selfish tabular
learners solve many joint commits by open-loop constant actions; that
behavioral success is compatible with a factored emergent structure.
Irreducibility and learnability remain different things. No claim
about deep MARL, continuous control, or field organizations.

## Limits

Tabular ε-greedy Q-learning; binary commits; state = last S bit;
exact Φ on embedded Boolean rules; no MAPPO/QMIX; no causality.

## Best next

**AI lane closable.** Synthesis: `org_frontier/AI_MULTIAGENT_ARC.md`.
Optional later gap (out of lane): deep-MARL replication only.

## Reproduce

```
python org_frontier/studies/marl_emergent_learn/analyze_marl.py
```
(~5 s)
