# Multivariate and Joint Recurrence Extensions
<!-- run: 2026-06-23 | sources: 15 -->
Search method: Consensus and Scholar Gateway academic-search tools plus WebSearch, with every DOI and arXiv ID confirmed against Crossref; run 2026-06-23.

Recurrence quantification rests on a phase-space picture in which a system revisits earlier states, and the multivariate program extends that picture to several observables and several interacting systems at once. Two distinct generalizations anchor the literature. Joint recurrence plots treat each system in its own reconstructed phase space and mark a recurrence only when both systems recur simultaneously, which makes them a test for generalized synchronization that tolerates non-phase-coherent and non-stationary data (Romano et al., 2004; Marwan et al., 2007). Multidimensional recurrence quantification analysis (MdRQA) instead stacks several observables into one common phase space and quantifies the auto-recurrence of that composite signal, providing a single coherent framework spanning individual, dyadic, and arbitrarily large group levels (Wallot et al., 2016).

The MdRQA family has expanded steadily. MdCRQA generalizes cross-recurrence to two multidimensional series and supports a diagonal cross-recurrence profile for time-lagged coupling (Wallot & Leonardi, 2018), with hands-on tutorials and the crqa 2.0 package lowering the barrier to application (Wallot et al., 2018; Coco et al., 2021). Reliable embedding for already-multidimensional signals motivated multidimensional extensions of average mutual information and false-nearest-neighbor estimators (Wallot & Mønster, 2018). Lagged MdRQA adds explicit leader-follower inference to the group-level dynamics (Tomashin et al., 2024), and a sliding-window summary-statistic scheme allows comparison of series of unequal duration, validated on Rössler and Kuramoto models (Thaikkandi & Sharika, 2023).

Mixed dimensionality poses a sharper problem, since coupled systems need not share an observable count or even a data type. Multivariate joint recurrence quantification analysis couples datasets of differing dimensionality and mixed nominal or interval scales through a joint recurrence coupling indicator, demonstrated on combined EEG and eye-tracking data (Wallot & Mønster, 2023). Joint recurrence has also been folded into time-delay-stability network analysis as a nonlinear alternative to cross-correlation (Tolston et al., 2020). Multiscale variants (MMDCRQA) probe coupling across temporal scales (He et al., 2020).

For group coordination, empirical work cautions that method choice matters: multivariate phase-space reconstruction renders cross-recurrence more sensitive to coordination manipulations than bivariate signals (Corbin et al., 2022), and group-level MdRQA links physiological synchrony to information processing in naturalistic decision-making (Sharika et al., 2024). Open questions concern principled normalization across heterogeneous channels, surrogate testing for composite phase spaces, and interpretation when component dynamics differ in dimensionality.

## References
- Coco, M. I., Mønster, D., Leonardi, G., Dale, R., & Wallot, S. (2021)
- Corbin, S., et al. (2022)
- He, Q., et al. (2020)
- Marwan, N., Romano, M. C., Thiel, M., & Kurths, J. (2007)
- Romano, M. C., Thiel, M., Kurths, J., & von Bloh, W. (2004)
- Sharika, K. M., et al. (2024)
- Thaikkandi, S., & Sharika, K. M. (2023)
- Tolston, M. T., et al. (2020)
- Tomashin, A., et al. (2024)
- Wallot, S., Roepstorff, A., & Mønster, D. (2016)
- Wallot, S., & Leonardi, G. (2018)
- Wallot, S., et al. (2018)
- Wallot, S., & Mønster, D. (2018)
- Wallot, S., & Mønster, D. (2023)
