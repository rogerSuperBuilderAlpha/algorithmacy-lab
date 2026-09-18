# MARL deep replicate — findings

**Verdict: NULL_SURVIVES.** A deeper MARL proxy — NumPy MLP and
linear FA Q-policies with observation `[S, own_last, partner_last]` —
**does not** restore a link between the emergent exact-Φ verdict and
learnability. EMERGENT_NULL from #41 survives (and is sharper:
emergent-triadic rate ≈ 0 on successful designed-triadic tasks).
Association only. Candid: still not MAPPO/QMIX/GPU deep MARL.

In-silico; N=176 (11 commits × 8 seeds × 2 archs). Hypotheses fixed
in `hypotheses.md`. Cited: #41; #98/#107; #37–#40 pointers. Other
lanes closed.

## Hypotheses

| H | result |
|---|---|
| H1 MLP restores predictive association | **REFUTED** |
| H2 EMERGENT_NULL survives | **SUPPORTED** |
| H3 partial (arch disagree) | **REFUTED** |

## Primary (MLP)

| metric | value | #41 tabular ref |
|---|---:|---:|
| AUC emerg→success | 0.500 | ≈0.555 |
| AUC emerg→easy | 0.500 | ≈0.485 |
| P(emerg_tri \| succ ∧ des_tri) | **0.000** | 0.183 |
| AND open-loop success | **8/8** | 10/10 |

Linear FA agrees (AUC emerg→success 0.450; AND open-loop 8/8;
predicts=no).

## Witnesses

- Successful AND/OR/XOR under MLP still collapse to **open-loop**
  constant policies; emergent structure stays non-triadic.
- Larger obs and neural approx do not force the classical `W'=S,C'=S`
  feedback triad when open-loop hits the commit.
- Architectures do **not** disagree on the learnability cut → H3
  refuted.

## Reading

The optional deep-MARL gap named in `AI_MULTIAGENT_ARC.md` is filled
at the smallest honest step up from tabular. Structure ≠ learnability
holds for function-approx independent learners with partner-aware
observations. No claim about centralized training, value
factorization, or continuous control.

## Limits

NumPy MLP (h=8) / linear FA; binary commits; binarized greedy tables
for exact Φ; modest seeds; not production deep MARL; no causality.

## Lane status

**AI lane remains closable** — deep gap filled with NULL_SURVIVES.
Further deep-MARL (MAPPO/QMIX) is optional curiosity, not a lane
blocker.

## Reproduce

```
python org_frontier/studies/marl_deep_replicate/analyze_deep.py
```
(~6 s)
