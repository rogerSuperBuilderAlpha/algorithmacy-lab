---
citekey: rudin2019explaining
title: Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead
authors: Rudin, Cynthia
year: 2019
doi: 10.1038/s42256-019-0048-x
arxiv: null
journal: Nature Machine Intelligence
programs: [field]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://static-content.springer.com/esm/art%3A10.1038%2Fs42256-019-0048-x/MediaObjects/42256_2019_48_MOESM1_ESM.pdf
sha256: d0c3603982bbeeeca1dca04f28f88f2b3c3ca13ad0bd23b89f548bbeb8cbd131
pdf_path: literature/pdfs/rudin2019explaining.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This PDF is the Supplementary Materials for Rudin's Nature Machine Intelligence Perspective, which argues that for high-stakes decisions one should use inherently interpretable models rather than explaining black box models after the fact. The supplement elaborates five technical points supporting that thesis: it distinguishes two types of black box (too-complicated-to-comprehend versus proprietary); argues that for structured-covariate problems no algorithm clearly dominates, so accuracy is rarely sacrificed by choosing an interpretable model; critiques counterfactual explanations as insufficient for high-stakes recourse; shows that interpretable global models (e.g., disjunctive normal form rule sets, falling rule lists) can still yield very sparse per-individual explanations; and reframes algorithmic instability (e.g., in decision trees) as a strength tied to the Rashomon effect. The recurring argument is the "Rashomon Set": when many almost-equally-accurate models exist, an interpretable one is likely among them, and domain experts can choose it without sacrificing accuracy. The supplement is argumentative and conceptual rather than experimental, citing prior work rather than reporting new benchmark results.

## Key facts it relies on
- Two distinct types of black box are defined: type one is too complicated for a human to comprehend; type two is proprietary; some models are both. The author cites evidence that COMPAS is a proprietary-but-not-complicated model [Rudin, Wang and Coker, 2018].
- For problems with meaningful structured covariates, machine learning algorithms tend to perform similarly with no algorithm clearly dominating; variation due to a single algorithm's tuning parameters can exceed variation between algorithms.
- For complex domains such as medical records, some studies report logistic regression has identical performance to deep neural networks [Razavian et al., 2015].
- The "Rashomon Set" argument: if there is no dominating algorithm and many almost-equally-good predictive models exist, interpretable models are likely to perform well.
- Counterfactual explanations (also called inverse classification) state a feature change sufficient (but not necessary) to switch the predicted class; recourse [Ustun et al., 2019] is a special counterfactual where the user can realistically take an action to reverse a decision.
- A counterfactual should give the lowest-cost action per the user's own cost metric, but eliciting that cost is generally very difficult and the cost can change as the user acts, so counterfactual explanations alone are argued insufficient for high-stakes decisions.
- Interpretable global models can give smaller-than-global explanations: a disjunctive normal form model (an "or" of "and"s, also called decision rules, rule sets, associative classifiers) can deny a loan based on a single true conjunction (requiring perhaps only 1-2 conditions shown to the individual), even with hundreds of conjunctions in the global model [Dash et al., 2018; Goh and Rudin, 2014; Rijnbeek and Kors, 2010; Su et al., 2016; Wang et al., 2017].
- Falling rule lists [Chen and Rudin, 2018; Wang and Rudin, 2015] give shorter explanations for the most important decisions (e.g., few conditions to flag a high-risk patient, more to subdivide low-risk groups).
- Decision-tree instability (small training-data changes yield very different trees) also occurs in linear models with correlated features (even in basic least squares); the author hypothesizes this is a side-effect of the Rashomon effect and reframes it as an advantage, since domain experts can add constraints/pick the most interpretable among equally accurate models.

## Critical notes from the literature
- Scope of this artifact: the acquired PDF is the Supplementary Materials (appendices A-E) only, not the main-text Perspective; the empirical/headline claims of the paper proper (e.g., the COMPAS interpretability arguments) live in the main article and are only referenced, not reproduced, here.
- The supplement explicitly acknowledges dissent: "not all researchers working in interpretability agree with this general sentiment about the advantages of instability [Murdoch et al., 2019]."
- The author flags that publication culture in ML favors selective reporting (omitting accurate baselines, under-tuning baselines, choosing favorable datasets), which creates an "illusion of large performance differences between algorithms" — a self-acknowledged caveat about the very performance-comparison evidence used to support interpretability.
- The smaller-than-global-explanation argument is framed under an asymmetric assumption (justify loan denials but not approvals); its applicability depends on that high-stakes asymmetry holding.
- These are conceptual/argumentative claims with citations, not new experiments; the supplement reports no new benchmark numbers or datasets of its own.

## Key topics covered
Interpretable machine learning; black box models (complicated vs proprietary); high-stakes decisions; COMPAS / recidivism prediction; Rashomon set / Rashomon effect; performance comparison and ML publication culture; counterfactual explanations / inverse classification; actionable recourse; disjunctive normal form models / decision rules / rule sets / associative classifiers; falling rule lists; smaller-than-global (sparse per-instance) explanations; algorithmic stability of decision trees and linear models; regularization; credit risk and loan-denial explanation.
