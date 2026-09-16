# Timescale separation — findings

**Verdict: FACTORS_LIKE_62.** Deterministic hold-for-k (slow mediator,
fast parties) factors the triad at **k\*=2** on both the conjunctive
form and the parity hub — dyadic with a core drop — matching #62
sequential update (6/6 orders dyadic on the conjunctive form). The
encoding is load-bearing: probabilistic 1/k commit stays **triadic**
across k=1…6 while Φ glides down. Construction decides the verdict.

In-silico; exact IIT-4.0; N=2 designed n=3 forms × k∈{1…6} × two
constructions. Hypotheses fixed in `hypotheses.md`. Cited: #62;
#6–#8 noise pointers; Q9 prior. Estimation / construct / omit /
ladder closed.

## Hold-for-k (primary)

| form | k=1 | k=2 | k* | core @ k* |
|---|---|---|---:|---|
| conjunctive | Φ=2.0 tri n_core=3 | Φ=0 dyadic n_core=1 | **2** | **{S}** |
| parity_hub | Φ=0.5 tri n_core=3 | Φ=0 dyadic n_core=0 | **2** | (none) |

Conjunctive core collapses onto the sticky mediator {S} (#43
direction), not onto {W,C}.

## Prob 1/k (construction check)

| form | k=1…6 structure | k*_prob |
|---|---|---|
| conjunctive | all triadic (Φ 2.0→0.055) | none |
| parity_hub | all triadic (Φ 0.5→0.126) | none |

## #62 sequential control

Conjunctive form: **6/6** update orders dyadic. PASS.

## Hypotheses (hold-for-k)

| hypothesis | result |
|---|---|
| H1 factors like #62 | **SUPPORTED** |
| H2 verdict robust to k | **REFUTED** |
| H3 Φ soft without verdict flip | **REFUTED** |

## Reading

Timescale separation factors where flip-noise (#6–#8) did not — but
only under the hard hold-for-k clock. Soft probabilistic inertia keeps
the verdict while shrinking Φ. Designed witnesses: conjunctive +
parity hub; #62 sequential; construction split.

## Limits

n=3; two slow-commit models only; no continuous-time (#12). No
organization measured.

## Best next experiment

Prefer agenda **#10** (fixed commit→response delay — Round 11 found
delay keeps triadic where hold factors). Alternate **#5** (correlated
TPM). Do not reopen estimation / construct / omit / ladder.

## Reproduce

```
python org_frontier/studies/timescale_separation/analyze_timescale.py
```
(~2 s)
