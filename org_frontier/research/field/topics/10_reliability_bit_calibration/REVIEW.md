# Inter-rater reliability and bit calibration
<!-- run: 2026-06-23 | sources: 11 -->
Method: searches on 2026-06-23 via Consensus, Scholar Gateway (Semantic Scholar/PubMed/Scopus/arXiv), and web search; every entry below carries a DOI or arXiv ID verified against the publisher or CrossRef.

Coded coordination data inherit two distinct quantities: how reliably human coders reproduce the labels, and how many bits those labels actually carry about the underlying coordination. The reliability literature is mature. Krippendorff's alpha is the recommended general coefficient because it accommodates any number of coders, any measurement level, and missing data, and corrects observed disagreement against chance disagreement (Hayes & Krippendorff, 2007; Krippendorff, 2011). Krippendorff (2004) clarifies recurring misconceptions, setting three conditions a statistic must meet to index data reliability and showing where percent agreement and kappa-family indices mislead. Simulation work establishes that Krippendorff's alpha and Fleiss' kappa give equivalent point estimates for complete nominal data, while alpha with bootstrap confidence intervals remains stable under missingness and is preferable for ordinal or higher data (Zapf et al., 2016).

Reporting norms remain uneven. Surveys of communication and HCI corpora find frequent reliance on percent agreement, inconsistent reporting of coefficients for every variable, and qualitative work where formal reliability appears in a minority of papers (Lombard et al., 2002; McDonald et al., 2019). Recent methodological reviews extend the same scrutiny to genre and rhetorical-move coding, comparing percent agreement, kappa, and multi-valued alpha across sample sizes and coder counts (Kim et al., 2024). Tooling has lowered the barrier: a free web calculator now computes alpha across data types without statistical-software dependencies (Marzi et al., 2024).

The calibration step connecting agreement to bits is less standardized. Empirical labels are a noisy channel observation of the latent code, so plug-in entropy and mutual-information estimates are biased downward in small samples and require correction (Paninski, 2003). Roulston (1999) derives propagable error bars on measured entropy and mutual information through standard error analysis, supplying the variance machinery for turning a coding distribution plus its agreement statistic into a calibrated bit estimate with uncertainty. The classical-test-theory analogue is disattenuation: observed associations are attenuated by unreliability and can be corrected when a reliability coefficient is available, though naive correction inflates variance and demands interval methods (Saccenti et al., 2019). A parallel machine-learning thread models each annotator's confusion matrix to recover latent labels from noisy multi-annotator data, giving an explicit channel model that maps agreement onto recoverable information (Tanno et al., 2019).

A defensible pipeline for coded coordination data therefore reports alpha with bootstrap intervals for every coded variable, treats coding as a confusion channel, applies bias-corrected entropy/MI estimation, and propagates both sampling and coding uncertainty into the final bit figure. No single work covers this full chain, so the synthesis draws the reliability, disattenuation, and information-estimation strands together.

## References
- Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures.*
- Kim, M., Qiu, X., & Wang, Y. (2024). Interrater agreement in genre analysis. *Research Methods in Applied Linguistics.*
- Krippendorff, K. (2004). Reliability in content analysis: Some common misconceptions and recommendations. *Human Communication Research.*
- Krippendorff, K. (2011). Computing Krippendorff's alpha-reliability.
- Lombard, M., Snyder-Duch, J., & Bracken, C. C. (2002). Content analysis in mass communication. *Human Communication Research.*
- Marzi, G., Balzano, M., & Marchiori, D. (2024). K-Alpha Calculator. *MethodsX.*
- McDonald, N., Schoenebeck, S., & Forte, A. (2019). Reliability and inter-rater reliability in qualitative research. *PACM HCI.*
- Paninski, L. (2003). Estimation of entropy and mutual information. *Neural Computation.*
- Roulston, M. S. (1999). Estimating the errors on measured entropy and mutual information. *Physica D.*
- Saccenti, E., et al. (2019). Corruption of the Pearson correlation coefficient by measurement error. *Scientific Reports.*
- Tanno, R., et al. (2019). Learning from noisy labels by regularized estimation of annotator confusion. *CVPR.*
