# Q90 literature — does a small-system law survive scale?

## The law under test

The lab's probe loop established a two-condition account of which parties join the irreducible core of a
coordination form: bidirectional constraining coupling is necessary, and among coupled parties the
probability of major-complex membership rises monotonically with pivotality — the Boolean sensitivity of
the determination to the party. The account reached rank-AUC 0.89 over the 256 three-node determinations
(`probes/probe_family_validation.py`, Finding 8 in `STRUCTURAL_FINDINGS.md`). It was found and validated
on three-node systems.

## Why scale is the open question

A regularity established on the smallest systems need not hold as systems grow. Integrated information
theory is explicit that higher-order mechanisms appear only with more elements (Albantakis et al. 2023):
at n = 4 and n = 5 a node can enter the major complex through joint constraints that have no three-node
analogue, so a predictor built on pairwise out-influence could lose accuracy. The lab's own Finding 6
shows that one size-dependent quantity, the random triadic rate, falls sharply with n (9.4% → 2.3% → 0%),
which is a warning that small-n intuitions can fail at scale. Q81 just showed that a *learned* surrogate
for the verdict does not generalize past the size it trained on. Whether the *structural* membership law
generalizes is the matching question, and it is unanswered.

## The exact ceiling

The major complex requires the full complex search, which is heavier than the whole-system Φ the verdict
uses. At n = 5 one wiring is about 27 seconds; at n = 6 it is about 9 minutes. The law can be checked at
n = 4 with a good sample and at n = 5 with a small one, and not at n = 6. That the test itself runs into
the size ceiling (Mayner et al. 2018) is part of the finding.

## Method context

The sampling and the sensitivity-based influence measure follow probe #12 directly, lifted to n-node
truth tables. Rank-AUC is the same rank statistic the probe loop used throughout.
