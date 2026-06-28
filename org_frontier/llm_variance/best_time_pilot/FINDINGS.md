# best_time_pilot — findings

Four students each asked a fresh ChatGPT session "what was the best time in history?" and submitted the
answer. The four answers are read across three similarity layers, with a per-layer effective sample size and
a consensus analysis over a hand-coded claim taxonomy. N=4, exact descriptive statistics.

| hypothesis | verdict | key numbers |
|---|---|---|
| Gate instrument control | passed | duplicate pair sim=1.000; max distinct lexical sim=0.382 |
| H1 surface divergence | confirmed | token-Jaccard mean 0.342, TF-IDF cosine mean 0.685 |
| H2 template convergence (K=3, {r3,r4}) | refuted | best K=2, grouping {r1,r2} \| {r3,r4} |
| H3 semantic beats lexical | confirmed | claim-Jaccard 0.754 − token-Jaccard 0.342 = 0.412 |
| H4 effective-N collapse | confirmed | n_eff: lexical 1.98, semantic 1.23 (nominal 4) |
| H5 consensus core over thin tail | confirmed | verdict unanimity 1.000; head 3 eras, tail 3 singletons, Gini 0.268 |

## The variance is a surface, the content one answer

The four answers share almost no wording. Mean token-Jaccard is 0.342 and no two distinct answers overlap
above 0.382, so two-thirds of each answer's vocabulary is unique to it. Read for content, the same four
answers nearly coincide. Mean claim-set Jaccard is 0.754, and the headline verdict — the present is the best
time for the average person's quality of life — is unanimous. The gap between the two readings, 0.412, is
the variance problem in one number: most of the visible diversity is wording.

The effective sample size makes the gap a count. Using n_eff = N² / (1ᵀ K 1), the lexical layer carries
n_eff = 1.98 and the semantic layer n_eff = 1.23, against a nominal four responses. Four answers to this
prompt are worth about one and a quarter independent answers in content. Treating them as four independent
observations — "three of four name the Renaissance," "75% cite Classical Athens" — counts the same answer
several times.

## The template prediction was wrong; the convergence is stronger

H2 predicted three layout families with the two "If you value X:" answers grouped. The structural clustering
returns two families instead: {r1, r2} and {r3, r4}, with a silhouette of 0.245 for K=2 against 0.207 for
K=3. The strongest structural divide is binary — the conditional "If you value X:" template with a terminal
metric→era summary (r3, r4) against everything else (r1's "For X:" headers and r2's named-era contenders).
The specific count was mis-predicted. The phenomenon H2 was testing, that the answers collapse into fewer
templates than responses, holds more strongly than predicted: K=2 < 4, and the structural n_eff is 2.30.

## A consensus core over a thin tail

Era incidence is U-shaped. Three eras are named by all four answers — the present, the post-war boom, the
Renaissance — and three are named by exactly one each: the Pax Romana (r2), the Age of Discovery (r3), the
late 1990s (r2). The Gini of era incidence is 0.268 and the normalized entropy 0.932, a distribution
concentrated at the ends. The divergent, "interesting" eras are exactly the single-mention tail, the part
that would not reproduce on a re-run. A margin-conditioned shuffle of the incidence matrix puts the observed
mean semantic Jaccard above 98% of nulls (p=0.017), so the agreement is not an artifact of each claim's
marginal rate.

The integration reading agrees. Claims travel in bundles: the o-information over the era columns is +1.745
bits, redundancy-dominated, the signature of claims that move together by template rather than independently.
This is reported as a pairwise descriptor only; over four rows the joint estimate is undersampled and is a
scaled-study instrument, not a result here.

## A formal model of the variance problem

The pilot fixes a model that scales. A response ensemble is read at three layers, each a similarity kernel
K^L on response pairs: lexical (token-Jaccard), structural (Ward clustering of layout features), semantic
(claim-set Jaccard). The effective sample size at layer L is

```
n_eff(L) = N² / (1ᵀ K^L 1),
```

which equals N when the responses are distinct and falls toward 1 as the kernel saturates. It equals the
survey design-effect n_eff = N / (1 + (N−1)ρ̄) in the equicorrelated limit, so it inherits the design-effect
reading without needing within-cluster replication, which N=4 cannot supply. The variance problem is the
ordered collapse n_eff(lexical) > n_eff(structural) > n_eff(semantic): apparent diversity high, effective
diversity near one. The consensus-core analysis names what survives the collapse — a head of unanimous
claims — and the integration reading names why — claims bundle redundantly by template.

## Caveats

N=4 gives no inferential power. The textbook ICC / design-effect estimate of n_eff is degenerate here
(within-template df = 1, and the design effect is capped near 1.33), so it is printed but flagged, and the
similarity-based n_eff is the headline. One prompt, one model, one date confound prompt-, model-, and
snapshot-effects, and "best time in history" is an unusually consensus-prone question. The claim coding is by
one coder against the codebook; a second coder and inter-rater agreement belong to the scaled study.
Incognito sessions control the account, not independence: the four answers are draws from one conditional
distribution, which is why n_eff refers to this model, this prompt, this date. The o-information is
undersampled at four rows. None of this measures an organization or a population; it measures four answers.

## The scaled study

Full-class N (30–100) restores within-template replication, so the ICC/design-effect n_eff and the
o-information become usable and the permutation test gains resolution. A re-run-same-prompt versus
vary-the-prompt contrast separates decoding variance from prompt sensitivity. Several questions, including
genuinely contested ones, test whether the consensus core is a property of this question or of the model. A
temperature sweep predicts n_eff(lexical) rising while n_eff(semantic) stays low — a per-layer dose-response
curve for the variance problem.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/llm_variance/best_time_pilot/analyze_variance.py`
