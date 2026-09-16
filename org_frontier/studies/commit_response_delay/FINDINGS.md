# Commit→response delay — findings

**Verdict: DELAY_CORE_SHIFT.** A fixed transport delay (buffer
pipeline) keeps the conjunctive triad **triadic** at every d=0…3 —
unlike #9 hold-for-k, which factors at k*=2 into a sticky {S} core.
What moves is major-complex membership ({W,S,C} → {S,C,B1} → full
W–S–C+buffers) and Φ (non-monotone **2→1→2→2**). Not magnitude-only.
The lagged-read construction **disagrees** at d=2 (dyadic Φ=0), so the
delay model is load-bearing.

In-silico; exact IIT-4.0; candid N=1 designed form (conjunctive
anchor; buffer n=3+d≤6). Hypotheses fixed in `hypotheses.md`. Cited:
#9 FACTORS_LIKE_62 (pointer); #62; Q10 prior. Estimation / construct /
omit / ladder closed.

## Buffer pipeline (primary)

| d | Φ | structure | n_core | major complex | pass-through |
|---:|---:|---|---:|---|---|
| 0 | 2.0 | triadic | 3 | {W,S,C} | Y |
| 1 | 1.0 | triadic | 3 | {S,C,B1} | Y |
| 2 | 2.0 | triadic | 5 | {W,S,C,B1,B2} | Y |
| 3 | 2.0 | triadic | 6 | {W,S,C,B1,B2,B3} | Y |

No buffer self-edges. Never the #9 self-absorbed {S}-only core.

## Lagged read (construction check)

| d | Φ | structure | core |
|---:|---:|---|---|
| 0 | 2.0 | triadic | {W,S,C} |
| 1 | 2.0 | triadic | {W,S,C} |
| 2 | 0 | **dyadic** | {S} |
| 3 | 2.0 | triadic | {W,S,C} |

## Hypotheses (buffer)

| hypothesis | result |
|---|---|
| H1 delay flips verdict | **REFUTED** |
| H2 magnitude only (fixed core) | **REFUTED** |
| H3 core shift, no verdict flip | **SUPPORTED** |

## Reading

Transport delay and a slowed clock are different operations: delay
keeps integration while reshaping the complex; hold-for-k factors.
Within delay, buffer vs lagged-read disagree on the d=2 verdict.
Designed witness: conjunctive buffer + lag split.

## Limits

Single form (conjunctive); d≤3; parity under buffer deferred (exact-Φ
cost at n≥4). No organization measured.

## Best next experiment

Done: #11 **DIFFERENT_LAW** (`oscillatory_scaling/`). Prefer agenda
**#5** (correlated TPM) or **#13** (bistability). Do not reopen
estimation / construct / omit / ladder.

## Reproduce

```
python org_frontier/studies/commit_response_delay/analyze_delay.py
```
(~4 min)
