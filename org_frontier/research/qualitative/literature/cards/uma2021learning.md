---
citekey: uma2021learning
title: Learning from Disagreement: A Survey
authors: Uma, Alexandra N. and Fornaciari, Tommaso and Hovy, Dirk and Paun, Silviu and Plank, Barbara and Poesio, Massimo
year: 2021
doi: 10.1613/jair.1.12752
arxiv: null
journal: Journal of Artificial Intelligence Research
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://jair.org/index.php/jair/article/download/12752/26751
sha256: b1fbc1b22ade5dc8f60828b5ca843d47156630edad48a29d5ac38f4794b0590f
pdf_path: literature/pdfs/uma2021learning.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This survey challenges the standard assumption in NLP and computer vision that a single "gold" interpretation exists for each annotated item, reviewing extensive evidence that humans systematically disagree on tasks ranging from "objective" ones like part-of-speech (POS) tagging to subjective ones like sentiment. Beyond reviewing methods for learning from disagreement, the authors empirically compare four families of approaches — automatic aggregation, filtering hard items, learning directly from crowd annotations (soft labels), and combining hard and soft labels — by training each on six standardized multiply-annotated datasets (POS, information-status PDIS, medical relation extraction MRE, recognizing textual entailment RTE, and two image-classification sets IC-LabelMe and IC-CIFAR10H), and evaluating with both "hard" metrics (accuracy, F1 against gold) and "soft" metrics (e.g., cross-entropy against the crowd label distribution). The central finding is that the relative ranking of methods is critically determined by the evaluation regime: under hard evaluation, training on gold labels usually wins, but under soft evaluation the ranking largely reverses, so that methods not using gold labels (especially soft-loss training and repeated labelling) generally outperform hard-training methods on all datasets and metrics. They also report a strong dataset effect: with large, high-quality datasets giving many judgments per item, training directly with soft labels beat training from aggregated or gold labels even under hard evaluation, whereas otherwise combining gold and soft labels worked best for hard evaluation. The authors conclude that even after abandoning the gold-standard assumption, the field must still reach consensus on how to evaluate models.

## Key facts it relies on
- Six datasets are used (Table 1): POS (14,000 items, 177 workers, 12 labels, avg 16.37 annotations/item), PDIS information status (96,305 items, 2 labels, avg 11.87), MRE medical relation extraction (975 items, 2 labels, avg 15.30), RTE/PASCAL RTE-1 (800 items, 2 labels, exactly 10 annotations each), IC-LabelMe (10,000 items, 8 labels, avg 2.55), and IC-CIFAR10H (10,000 items, 10 labels, avg 51.10).
- Disagreement is pervasive: an analysis of the Phrase Detectives corpus found 64.3% of data instances contain disagreements (12.6% due to ambiguity); Poesio & Artstein (2005) found disagreement in 42% of markables in the ARRAU corpus; Pavlick & Kwiatkowski (2019) found workers disagreed on at least 20% of RTE premise/hypothesis pairs.
- Even for POS, 48.09% of items received annotations spanning more than one category, and when 10 linguistics faculty were asked to tag 10 hard items, they disagreed on the right tag in 8 of 10 cases (Plank et al. 2014b).
- Methods are grouped into four categories: (1) aggregating coder judgments (majority voting, Dawid & Skene 1979, MACE, CrowdTruth); (2) filtering/weighting hard items (e.g., Reidsma & op den Akker, GLAD); (3) learning directly from crowd annotations via soft labels (DLC, soft-loss with KL/CE/MSE, SREL repeated labelling); (4) augmenting hard labels with disagreement (PEWE, multi-task learning MTLOA/MTLSL).
- Aggregation quality varies by dataset (Table 2): majority-voting accuracy vs gold ranges from 0.75 (MRE) to 0.99 (IC-CIFAR10H); D&S and MACE generally match or beat MV (e.g., PDIS MV 0.89 vs D&S/MACE 0.98).
- Under hard (accuracy/F1) evaluation, training with gold labels (alone or with crowd info) gave best results for POS, IC-LabelMe, and MRE — sometimes by up to ~10 accuracy points (e.g., POS) — while for IC-CIFAR10H crowd information alone won and for RTE gold vs MV-silver showed no significant difference.
- Under soft (cross-entropy) evaluation, the ranking "to a large extent" reverses: methods not using gold labels generally outperform hard-training methods for all datasets and all metrics, with soft-loss training (CE/KL loss on probabilistic labels) typically best.
- The answer to RQ2a is mixed under hard evaluation but uniformly positive under soft evaluation: adding crowd information always improves over gold-only; for RQ2b, multi-task learning capturing disagreement (notably MTLSL) is usually the best way to combine gold and crowd information.

## Critical notes from the literature
- The authors stress that no single training method is a clear "winner": which method performs best depends heavily on the task, the dataset characteristics (annotation count, coder accuracy, entropy), and especially on whether hard or soft evaluation is used — their headline message is that the field still needs consensus on evaluation, not a single recommended algorithm.
- Filtering hard items — the most intuitive way to use disagreement — did not help under hard evaluation for any dataset and often hurt substantially; IC-LabelMe was the only partial exception.
- Scope limitation acknowledged by the authors: they deliberately focused on "objective" judgment tasks, so none of the six datasets cover purely subjective disagreement (e.g., sexism/offensiveness), which they note presents the most serious challenge to the gold-label idea and is included only "for completeness."
- Dataset-size and quality caveats: the RTE set has only 800 items (below their 1,000-item rule of thumb, included for comparability with prior work), and disagreement sources differ by dataset (annotator/interface error, vague annotation schemes, genuine ambiguity, item difficulty), so results may not transfer across tasks with different disagreement provenance.
- The survey positions itself against Jamison & Gurevych (2015), who compared only two approaches (hard filtering and Sheng et al.'s repeated labelling) and found soft labelling did not outperform gold/aggregated labels under hard metrics; this work argues that conclusion flips once soft evaluation and stronger neural baselines are used.

## Key topics covered
- Annotation disagreement in NLP and computer vision; the gold-label / single-truth assumption critique
- Crowdsourcing, microtask crowdsourcing, game-with-a-purpose, disagreement-aware crowdsourcing (CrowdTruth)
- Sources of disagreement: annotator error, interface problems, vague annotation schemes, genuine ambiguity, item difficulty, subjectivity
- Label aggregation: majority voting, Dawid & Skene (1979), MACE, CrowdTruth metrics (worker/media-unit/annotation quality)
- Soft labels and soft-loss training (KL, cross-entropy, MSE); repeated labelling (SREL); distillation analogy
- Filtering/weighting hard items; item-difficulty models (GLAD, Carpenter)
- Combining hard + soft labels: PEWE, multi-task learning (MTLOA, MTLSL)
- Hard vs soft evaluation metrics (accuracy, F1, CrowdTruth F1, cross-entropy against label distributions); entropy and best-distribution entropy (BDE)
- Datasets: Phrase Detectives / PDIS, Gimpel POS, CrowdTruth MRE, PASCAL RTE-1 (Snow et al.), LabelMe, CIFAR10H
