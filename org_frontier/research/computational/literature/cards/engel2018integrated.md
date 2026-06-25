---
citekey: engel2018integrated
title: Integrated information as a metric for group interaction
authors: Engel, David and Malone, Thomas W.
year: 2018
doi: 10.1371/journal.pone.0205335
arxiv: null
journal: PLoS ONE
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0205335&type=printable
sha256: 82d666848c70dc55e717c754434b2434e633a40d07bbfeeeb80993ea8574bec5
pdf_path: literature/pdfs/engel2018integrated.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether "integrated information" (phi), a metric originally developed by Tononi and colleagues as a measure of consciousness in brains, can be repurposed as a metric for characterizing and predicting group interaction. Phi captures two properties in a single quantity—differentiated information and integration—that the authors argue matter in many kinds of groups, not just brains. They apply phi to three datasets: (1) 68 four-person work groups performing diverse tasks, (2) groups of Wikipedia editors, and (3) the collection of people and computers communicating over an Internet backbone. They find that 4-person groups with higher phi have higher collective intelligence (r = 0.370, p = 0.003), that Wikipedia editor groups producing higher-quality articles have higher phi, and that the phi of Internet traffic increased over a six-year period. The authors conclude that integrated information can be a useful, observational way of characterizing interactional complexity that at least sometimes predicts group performance, and propose phi as a potential metric of effective group collaboration. They are careful to note phi may be measuring "something" of interest regardless of whether it measures consciousness.

## Key facts it relies on
- Phi (integrated information) was proposed by Tononi and colleagues as a measure of consciousness; it requires a system to both generate differentiated information and have that information integrated at the level of the whole, with phi = 0 when parts are completely independent.
- Because complete models of state-transition rules are rarely available for observational data, the authors use two empirical phi estimators from Barrett and Seth: Φ_E ("empirical phi"), based on Balduzzi and Tononi's definition and assuming stationarity (Study 1), and Φ_AR ("auto-regressive phi") for larger systems (Studies 2 and 3).
- Study 1 reanalyzed data from 68 groups of four people working on diverse online tasks (generating, choosing, remembering, sensing, taking physical actions); subjects were recruited in the Boston area in 2012. Collective intelligence was the first factor from a factor analysis, explaining around 40% of variance, analogous to individual IQ.
- For face-to-face groups, average phi peaked at a time delay of around 2 seconds (Fig 1); for Internet machines, phi was maximized at a time step size of 100 ms (Fig 4), consistent with ~200 ms round-trip Internet times.
- In Study 1, phi was significantly correlated with measured collective intelligence (r = 0.370, p = 0.003), pooling face-to-face and online conditions after normalizing phi by condition.
- In Study 2, Wikipedia article quality (FA, A, GA, B, C in decreasing quality) was significantly correlated with phi when controlling for number of editors and edits per editor (F = 3.6847, p = 0.0053); pairwise Wilcoxon tests gave z = 5.6024 (p < 0.00001) between C and B and z = 3.5132 (p = 0.0004) between GA and A.
- Study 2 analyzed 999 articles (1000 from Wikipedia's Vital Articles list minus the front-page outlier); the atomic-partition phi correlated with full bipartition phi at r = 0.83 (p < 0.001) on cases with 14 or fewer editors.
- Study 3 used CAIDA Internet backbone data from San Jose (2008 onward), with the number of sending nodes ranging from about 200,000 to 1.6 million; nodes were subsampled to 100 using methods including random walk and forest fire. Phi showed a significant upward trend over six years (Fig 5 example β = 1.779, p < 0.0001; Table 1 random-walk coefficient 1.675, p < 10^-8).
- The mathematical formulation defines phi via a minimum information bipartition (MIB); Φ_E[X;τ] = I(X_{t-τ};X_t) − Σ I(M^k_{t-τ};M^k_t) and Φ_AR uses log determinants of covariance matrices of the data and of regression residuals.

## Critical notes from the literature
- The authors acknowledge considerable ongoing debate about whether phi actually measures consciousness (citing ref [22]), and that the metric they use measures "something" of interest whether or not it is consciousness.
- They note that the Barrett–Seth estimators (Φ_E, Φ_AR) are approximations with documented limitations as estimates of the original theoretical phi (refs [24,25]); Φ_AR can produce values below 0 and was sometimes numerically unstable or returned extreme values, requiring dropping the 5% lowest-variance nodes (invalid in 19.5% of Study 2 cases, repeated 2.27 times on average; 67.14% initially in Study 3, repeated 2.12 times on average).
- Because enumerating all bipartitions to find the MIB is computationally infeasible for large systems, the authors used "atomic" partitions (each node its own partition) rather than the true MIB in Studies 2 and 3.
- The authors assume, but do not test for, stationarity of the time series in all three studies, and acknowledge results could be caused partly by non-stationarity; they flag examining alternative explanatory factors as important future work.
- The authors concede other metrics may have predictive power similar to phi and be simpler to compute, and that comparing phi's predictive power against components and other variables (participation, effort/ability, network topology) is needed.

## Key topics covered
Integrated information (phi); integrated information theory (Tononi); differentiation and integration; collective intelligence; group performance prediction; minimum information bipartition (MIB); empirical phi (Φ_E) and auto-regressive phi (Φ_AR); Barrett–Seth estimators; mutual information and entropy; Wikipedia article quality; Internet backbone traffic (CAIDA); graph subsampling (random walk, forest fire, breadth first, random nodes); time-delay and time-step selection; hybrid human-computer systems; collaboration metrics.
