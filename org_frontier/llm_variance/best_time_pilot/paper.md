# The variance problem: how far apart are four answers to the same question?

<code + data: org_frontier/llm_variance/best_time_pilot/ ; check llm-variance-best-time-pilot in ci/reproduce.json>

## Abstract

Four students asked one language model the same question and got four answers that look different. The
answers share about a third of their wording, but their content nearly coincides and their headline verdict
is unanimous. Read across three similarity layers — lexical, structural, semantic — the effective sample
size falls from 1.98 at the surface to 1.23 in content, against four nominal responses. Most of the visible
diversity is wording. The pilot fixes a measurement model for this gap, the variance problem, and specifies
the scaled study that would estimate it with power.

## The problem

Behavioral work increasingly samples from language models: ask a model a question N times, or have N people
ask once, and treat the answers as N observations. The answers look diverse, so the sample looks rich. A
class exercise makes the trap concrete. Four students each opened a fresh, signed-out ChatGPT session, asked
"what was the best time in history?", and submitted the answer. The four texts read as four different essays.
Whether they are four observations or one is the question.

## The instrument

Each response is read at three layers, each a symmetric similarity kernel K on response pairs. The lexical
layer is token-Jaccard on the raw text, with TF-IDF cosine as a conservative complement. The structural
layer is Ward clustering of layout features — the conditional "If you value X:" framing, "For X:" headers,
named-era dating, a terminal metric→era summary. The semantic layer is Jaccard over a hand-coded
claim/era taxonomy, fixed in a codebook before coding, so content similarity is read independent of wording.
A bag-of-words semantic measure would fold the lexical signal back in; claim coding keeps them separate.

The effective sample size at layer L is n_eff(L) = N² / (1ᵀ K^L 1). It returns N when every response is
distinct and falls toward 1 as the kernel saturates, and it equals the survey design-effect
N / (1 + (N−1)ρ̄) when all pairs share one correlation. A consensus analysis reads which eras the answers
name and how concentrated those choices are. An integration reading, the lab's o-information on the
response×claim matrix, reads whether claims move together.

## Data

Four anonymized responses and one duplicate of the first, kept as an instrument control. Names, an email
address, and a phone number that arrived with the submissions were removed; the email signatures are not part
of the model's answer and were dropped. The claim taxonomy and inclusion rules are in `data/CODEBOOK.md`. The
coding is by one coder, a limit the scaled study removes.

## Results

The instrument control passes: the duplicate scores 1.000 on the lexical kernel and every distinct pair
below it (max 0.382). The four answers diverge in wording — mean token-Jaccard 0.342, cosine 0.685 (H1) —
and converge in content — mean claim-Jaccard 0.754, a gap of 0.412 (H3). The headline verdict, that the
present is best for the average person, is unanimous, and era incidence is U-shaped: three eras named by all
four, three named by exactly one (H5; Gini 0.268, shuffle-null p=0.017). Effective sample size collapses
from the surface inward, 1.98 lexical to 1.23 semantic against four (H4). The o-information over the era
columns is +1.745 bits, redundancy-dominated, the signature of template-bundled claims.

One pre-registered prediction failed. H2 expected three layout families with the two summary-list answers
paired; the clustering returns two families, {r1,r2} and {r3,r4}, silhouette 0.245 against 0.207 for three.
The dominant structural split is binary, the conditional-framing template against the rest. The convergence
H2 was testing holds more strongly than predicted — two templates over four responses — while the specific
count was wrong.

## What this is and is not

A pilot that fixes the measure on four responses. The numbers describe these four answers and carry no
inferential weight: the design-effect n_eff is degenerate at N=4 and is flagged, the o-information is
undersampled, and the single coder is unreplicated. "Best time in history" is a consensus-prone question, so
the depth of the core here is an upper estimate. The four came from one model on one date through incognito
sessions, which control the account and not the draw — the responses are samples from one conditional
distribution, which is the variance problem stated exactly.

## The scaled study

Full-class N restores within-template replication, so the design-effect n_eff and the o-information become
usable and the permutation test gains resolution. A re-run-same-prompt versus vary-the-prompt arm separates
decoding variance from prompt sensitivity. A bank of questions, some genuinely contested, tests whether the
consensus core is a property of the question or the model. A temperature sweep predicts the lexical n_eff
rising while the semantic n_eff stays near one, a per-layer dose-response curve for how much of a model's
apparent diversity is real.

## References

The lab's reproducibility and invariance precedents (q123, q197); the o-information estimator in
`org_frontier/probes/_info.py` (Rosas et al. 2019). Design effect and effective sample size after Kish.
