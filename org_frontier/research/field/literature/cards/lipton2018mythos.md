---
citekey: lipton2018mythos
title: The mythos of model interpretability
authors: Lipton, Zachary C.
year: 2018
doi: 10.1145/3233231
arxiv: null
journal: Communications of the ACM
programs: [field]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1606.03490
sha256: 0f20f650ff7357e3ea4a1875048b39a28bbd7110e5f569f15ba8a161cd9d9437
pdf_path: literature/pdfs/lipton2018mythos.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a position/critical-analysis paper arguing that "interpretability" in machine learning is not a monolithic concept but an ill-defined term that papers frequently invoke axiomatically without definition. Restricting scope mainly to supervised learning, Lipton surveys the literature to (1) catalog the diverse and occasionally discordant motivations (desiderata) for wanting interpretable models and (2) taxonomize the model properties and techniques claimed to confer interpretability. He identifies five desiderata — trust, causality, transferability, informativeness, and fair/ethical decision-making — arguing they arise from a mismatch between the formal objective of supervised learning (test-set predictive performance) and real-world deployment costs. He then splits interpretability methods into two competing notions: transparency (how the model works, decomposed into simulatability, decomposability, and algorithmic transparency) and post-hoc interpretability (what else the model can tell you, e.g. text explanations, visualization, local explanations, explanation by example). A central claim is that linear models are not strictly more interpretable than deep neural networks; the truth of that common assertion depends entirely on which notion of interpretability is meant. The paper concludes that claims about interpretability must be qualified to a specific definition, that transparency can conflict with broader AI objectives, and that post-hoc explanations can mislead.

## Key facts it relies on
- The paper argues interpretability "has no formal technical meaning" and that papers wield the term in a "quasi-scientific" / "quasi-mathematical" way, making claims that may not reference a single concept.
- Five desiderata of interpretability research are identified: trust (§2.1), causality (§2.2), transferability (§2.3), informativeness (§2.4), and fair and ethical decision-making (§2.5).
- The common thread across desiderata: "The demand for interpretability arises when there is a mismatch between the formal objectives of supervised learning (test set predictive performance) and the real world costs in a deployment setting."
- Transparency is decomposed into three levels: simulatability (whole model contemplated at once), decomposability (each input/parameter/calculation admits an intuitive explanation), and algorithmic transparency (understanding the learning algorithm, e.g. linear-model error surface and convergence to a unique solution).
- Post-hoc interpretability is decomposed into four approaches: text explanations (§3.2.1), visualization (§3.2.2), local explanations (§3.2.3), and explanation by example (§3.2.4).
- Concrete examples cited: Caruana et al. (2015) pneumonia model that assigned *lower* risk to asthma patients (because of more aggressive treatment), which would invalidate it if used for triage; Szegedy et al. (2013) adversarial examples on CNNs; FICO using logistic regression for credit scoring citing interpretability (Fair Isaac Corporation, 2011), with features (debt ratio, number of accounts) gameable by credit-seekers.
- Post-hoc technique examples: t-SNE visualization (Van der Maaten & Hinton, 2008); Mordvintsev et al. (2015) inceptionism; Mahendran & Vedaldi (2015) recovering images from a high-level (level 6 AlexNet) representation; saliency maps (Simonyan et al. 2013; Wang et al. 2015, Figure 2); LIME-style local sparse linear surrogate (Ribeiro et al. 2016); explanation-by-example via k-nearest neighbors in learned representation (Caruana et al. 1999); word2vec nearest neighbors (Mikolov et al. 2013).
- The paper claims neither linear models, rule-based systems, nor decision trees are *intrinsically* interpretable: high-dimensional models, unwieldy rule lists, and deep decision trees could be less transparent than "comparatively compact neural networks."
- The EU "right to explanation" (Goodman & Flaxman, 2016) is cited; the paper argues useful explanations must (i) present clear reasoning based on falsifiable propositions and (ii) offer a way to contest those propositions; little published work addresses "contestability."

## Critical notes from the literature
- Self-acknowledged scope limit: the analysis is restricted "mainly" to supervised learning and does not delve deeply into reinforcement learning, interactive learning, or Bayesian methods; the author notes RL can address some but not all interpretability objectives and still relies on a well-defined scalar objective.
- The paper cautions that post-hoc interpretations "can potentially mislead" — explanations can be (deliberately or not) optimized to be plausible but unfaithful, analogous to how human-stated rationales (e.g. "leadership," "originality") can disguise racial or gender discrimination (Mounk, 2014); the Krening et al. (2016) verbal-explanation example may "not faithfully describe the agent's decisions."
- Transparency can be at odds with broader AI goals: the short-term goal of transparent models for doctor trust may clash with the longer-term goal of improving health care, and demands for transparency may be "a concession to institutional biases against new methods."
- The paper is explicitly a conceptual/taxonomic critique rather than an empirical study; it presents no new experiments, datasets, or quantitative results, framing itself as "a first step towards providing a comprehensive taxonomy" and a call for more critical writing at ML conferences.
- The decomposability notion is fragile: linear-model weights "can be fragile with respect to feature selection and pre-processing" (e.g. flu-risk/vaccination sign flips depending on inclusion of age/immunodeficiency indicators); decomposability also requires individually interpretable inputs, disqualifying engineered/anonymous features.

## Key topics covered
Model interpretability; transparency vs. post-hoc explanation; simulatability; decomposability; algorithmic transparency; trust; causality; transferability; informativeness; fairness and ethics; right to explanation; contestability; linear models vs. deep neural networks; saliency maps; local explanations (LIME); t-SNE visualization; explanation by example; adversarial examples; problem formulation critique; deployment/real-world objective mismatch.
