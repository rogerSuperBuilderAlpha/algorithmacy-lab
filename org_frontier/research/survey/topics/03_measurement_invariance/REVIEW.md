# Measurement Invariance Across Groups and Waves
<!-- run: 2026-06-23 | sources: 16 -->
Search method: parallel queries via the Consensus and Scholar Gateway academic-search tools, with every DOI verified against Crossref and publisher records; run date 2026-06-23.

Measurement invariance (MI) is the precondition for interpreting differences in a latent construct (here, worker literacy) as substantive rather than artifacts of how an instrument behaves across populations or survey waves (Meredith, 1993; Vandenberg & Lance, 2000). The standard confirmatory factor analysis (CFA) workflow tests a nested sequence: configural (same pattern), metric/weak (equal loadings), scalar/strong (equal intercepts), and residual/strict invariance, with scalar invariance being the threshold for comparing latent means across groups or occasions (Putnick & Bornstein, 2016). The same logic transfers to repeated waves, where indicators are correlated over time and autocorrelated residuals must be specified before constraints are imposed (Seddig & Leitgöb, 2018; MacKinnon et al., 2022).

Decision rules center on fit-change criteria. Because the χ² difference test is oversensitive in large worker samples, change-based thresholds in approximate fit indices are preferred, commonly ΔCFI ≤ .010 paired with ΔRMSEA ≤ .015 (Cheung & Rensvold, 2002; Chen, 2007). These fixed cutoffs have inconsistent Type I error rates, and permutation tests offer a sample-specific null distribution as an alternative to canned cutoffs (Jorgensen et al., 2018). When a constraint fails, partial invariance frees a minority of loadings or intercepts to preserve comparability, though stepwise modification-index-driven selection is fragile and capitalizes on chance (Putnick & Bornstein, 2016; Marsh et al., 2018).

Two developments address the frequent failure of exact scalar invariance with many groups or waves. Alignment optimization estimates group-specific parameters while minimizing total non-invariance, ranking which parameters and groups depart from equality without a long chain of modification decisions (Asparouhov & Muthén, 2014; Marsh et al., 2018; Luong & Flake, 2023). Approximate invariance places zero-mean, small-variance priors on cross-group or cross-wave parameter differences, tolerating minor deviations while sustaining mean comparison (Cieciuch et al., 2018; Seddig & Leitgöb, 2018). Comparative work finds these methods, alongside multilevel and mixture approaches, perform reasonably when paired with an appropriate fit criterion (Kim et al., 2017; Leitgöb et al., 2023).

Reviews of practice temper this toolkit. MI is rarely tested and poorly reported, reproductions of published tests often fail, and full scalar invariance is uncommon across cultural or worker subgroups (Maassen et al., 2025). Applied panel studies illustrate both outcomes: some scales reach strict longitudinal invariance across waves, while large cross-national surveys typically settle for approximate or aligned scalar invariance with a sizeable share of non-invariant parameters (Fong et al., 2025). For comparing literacy across worker populations and waves, the implication is to pre-register the invariance sequence, report ΔCFI/ΔRMSEA, and treat alignment or approximate methods as the realistic path to defensible mean comparison.

## References
Asparouhov, T., & Muthén, B. (2014). Multiple-group factor analysis alignment. *Structural Equation Modeling*.
Chen, F. F. (2007). Sensitivity of goodness of fit indexes to lack of measurement invariance. *Structural Equation Modeling*.
Cheung, G. W., & Rensvold, R. B. (2002). Evaluating goodness-of-fit indexes for testing measurement invariance. *Structural Equation Modeling*.
Cieciuch, J., Davidov, E., Schmidt, P., & Algesheimer, R. (2018). Testing for approximate measurement invariance of human values in the European Social Survey. *Sociological Methods & Research*.
Fong, T. C. T., et al. (2025). Longitudinal measurement invariance of EURO-D across 27 countries in SHARE. *Journal of Affective Disorders*.
Jorgensen, T. D., Kite, B. A., Chen, P.-Y., & Short, S. D. (2018). Permutation randomization methods for testing measurement equivalence. *Psychological Methods*.
Kim, E. S., et al. (2017). Measurement invariance testing with many groups: A comparison of five approaches. *Structural Equation Modeling*.
Leitgöb, H., et al. (2023). Measurement invariance in the social sciences. *Social Science Research*.
Luong, R., & Flake, J. K. (2023). Measurement invariance testing using CFA and alignment optimization. *Psychological Methods*.
MacKinnon, S. P., et al. (2022). Tutorial in longitudinal measurement invariance and cross-lagged panel models using lavaan. *Meta-Psychology*.
Maassen, E., et al. (2025). The dire disregard of measurement invariance testing in psychological science. *Psychological Methods*.
Marsh, H. W., et al. (2018). What to do when scalar invariance fails: The extended alignment method. *Psychological Methods*.
Meredith, W. (1993). Measurement invariance, factor analysis and factorial invariance. *Psychometrika*.
Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *Developmental Review*.
Seddig, D., & Leitgöb, H. (2018). Approximate measurement invariance and longitudinal CFA. *Survey Research Methods*.
Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature. *Organizational Research Methods*.
