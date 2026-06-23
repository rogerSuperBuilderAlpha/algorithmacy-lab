# Recurrence research — literature review

This review was assembled by web and academic-database search (WebSearch, Frontiers, Springer, AIP, arXiv, publisher pages) on 2026-06-23, retaining only works whose DOI or arXiv identifier was confirmed against a retrieved record.

## Scope

Recurrence quantification analysis (RQA) and its bivariate extension, cross-recurrence quantification analysis (CRQA), provide a model-agnostic route to measuring coordination between two interacting systems from their time series. The method is foundational to a research program on coordination through opaque, interested third parties, where the analyst observes joint trajectories without a generative model of either party.

## Foundations

Recurrence plots originate with Eckmann, Kamphorst, and Ruelle (1987), who visualized when a dynamical system revisits earlier states in reconstructed phase space. Webber and Zbilut (1994) converted these plots into quantitative measures (recurrence rate, determinism, laminarity, diagonal-line statistics), establishing RQA for physiological signals. The canonical synthesis is Marwan, Romano, Thiel, and Kurths (2007), a Physics Reports review covering embedding, thresholding, and the full quantifier set. Marwan (2008) gives the historical lineage, and Marwan (2011) catalogs the pitfalls (embedding choices, threshold sensitivity, tangential motion) that govern reproducibility. The edited volume by Webber and Marwan (2015) consolidates best practices. Marwan and Kraemer (2023) survey the present frontier: event-like and multiscale recurrences, parameter-selection heuristics, transition and causality detection, and coupling with machine learning.

## Coordination from time series

CRQA enters the social and behavioral sciences through Shockley, Santana, and Fowler (2003), who showed that conversing dyads share more phase-space locations in postural sway than non-interacting pairs. Richardson and Dale (2005) applied cross-recurrence to speaker and listener gaze, recovering a characteristic two-second lag that predicted comprehension. Dale, Warlaumont, and Richardson (2011) generalized nominal cross-recurrence as lag-sequential analysis for categorical behavioral streams. Konvalinka et al. (2011) used nonlinear heart-rate analysis to document synchronized arousal between fire-walkers and related spectators. Fusaroli and Tylén (2016) reframed conversation as interpersonal synergy, with recurrence-based complexity matching predicting joint task performance. Angus (2019) reviews two decades of recurrence methods for communication data.

## Method tooling

Software has driven adoption. Coco and Dale (2014) released the crqa R package for categorical and continuous series; Wallot, Roepstorff, and Mønster extended RQA to multidimensional series (MdRQA), and Wallot (2019) to multidimensional cross-recurrence (MdCRQA). Wallot and Leonardi (2018) tutorialize CRQA, diagonal-cross-recurrence profiles (DCRP) for lead-lag structure, and MdRQA in R. Coco, Mønster, Leonardi, Dale, and Wallot (2021) document the consolidated crqa package, including windowed and piecewise measures. Wallot and Mønster (2023) introduce multivariate joint recurrence quantification for time series of differing dimensionality. Goldstein, Burns, Peck, Dale, and Lieberman (2025) apply CRQA to fNIRS hyperscanning during naturalistic negotiation, finding that balanced lead-lag coupling predicted outcomes where inter-subject correlation and wavelet coherence did not.

## Comparison with causal measures

Lead-lag and coupling estimates invite comparison with directed-influence measures. Schreiber (2000) defined transfer entropy, a nonparametric generalization of Granger causality that conditions out shared history. Sugihara et al. (2012) introduced convergent cross mapping (CCM), exploiting state-space reconstruction to separate causation from correlation in weakly coupled nonlinear systems. Wibral, Vicente, and Lizier (2014) consolidate transfer-entropy practice for neural data. Edinburgh, Eglen, and Ercole (2021) benchmark ten bivariate causality indices, recommending transfer entropy and nonlinear Granger causality for robustness. DCRP lag peaks describe temporal precedence and should be read as description, not causal inference; transfer entropy and CCM target the directional claim that recurrence profiles cannot license.

## References

Angus (2019); Coco and Dale (2014); Coco, Mønster, Leonardi, Dale, and Wallot (2021); Dale, Warlaumont, and Richardson (2011); Eckmann, Kamphorst, and Ruelle (1987); Edinburgh, Eglen, and Ercole (2021); Fusaroli and Tylén (2016); Goldstein, Burns, Peck, Dale, and Lieberman (2025); Konvalinka et al. (2011); Marwan (2008); Marwan (2011); Marwan and Kraemer (2023); Marwan, Romano, Thiel, and Kurths (2007); Richardson and Dale (2005); Schreiber (2000); Shockley, Santana, and Fowler (2003); Sugihara et al. (2012); Wallot (2019); Wallot and Leonardi (2018); Wallot and Mønster (2023); Webber and Marwan (2015); Webber and Zbilut (1994); Wibral, Vicente, and Lizier (2014).
