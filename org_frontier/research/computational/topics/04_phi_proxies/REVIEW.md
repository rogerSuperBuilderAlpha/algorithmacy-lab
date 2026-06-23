# Proxies and Approximations for Phi
<!-- run: 2026-06-23 | sources: 14 -->
Search method: queries run on 2026-06-23 across Consensus and Semantic Scholar (Scholar Gateway) academic search plus targeted web verification of every DOI/arXiv identifier.

Exact integrated information (Φ) is computable only for systems of roughly a dozen elements, because both the minimum-information-partition (MIP) search and the cause-effect structure scale super-exponentially (Kitazono et al., 2018). This bottleneck has produced a literature of proxies grouped here by strategy: geometric, decoding-based, empirical/perturbational, asymptotic, and learned.

The geometric program recasts integration as a divergence between a system's distribution and a manifold on which causal influences are severed, yielding the geometric measure Φ_G and a unified taxonomy of related quantities (Oizumi et al., 2016). Tegmark (2016) classifies Φ-measures by factorization, distribution choice, and divergence, deriving approximate Gaussian formulas suited to laboratory data. Decoding offers a complementary route: Φ* uses mismatched decoding to bound integrated information from below and above and admits a closed Gaussian form for time series (Oizumi et al., 2016, PLoS Comput. Biol.). Systematic simulation comparisons show that candidate measures diverge sharply, with only a subset tracking dynamical complexity (Mediano et al., 2019), and that several approximations recover small-system Φ with correlations above 0.95 yet without large computational savings, performing best as predictors of low-Φ systems (Nilsen et al., 2019).

Empirical proxies trade theoretical fidelity for applicability. The perturbational complexity index compresses TMS-evoked EEG responses into a single integration-plus-differentiation score that discriminates conscious states (Casali et al., 2013), later accelerated to sub-second computation via state-transition counting in PCI^st (Comolatti et al., 2019). High-density EEG estimators of Φ have been combined with connectivity features to separate anesthetic states (Kim et al., 2018). These quantities correlate with, but do not equal, IIT's Φ.

Asymptotic analysis sidesteps exact computation: mean-field treatment of kinetic Ising networks shows integration diverging at criticality in the thermodynamic limit, giving a scaling account of how integration grows with size (Aguilera and Di Paolo, 2019). A scalable convex-optimization estimator of higher-order/macroscopic information now indexes criticality and consciousness in neural recordings (Liardi et al., 2025).

Recent work pursues tractability directly. Graph neural networks trained on exact 5-7-node solutions extrapolate qualitative Φ and major-complex patterns to 100-node split-brain configurations (Hosaka, 2025). GeoMIP reformulates the MIP search as hypercube-graph optimization, reporting 165-326x speedups over PyPhi with near-exact partition agreement and reach to roughly 25 variables (Díaz-Arancibia et al., 2026). The open question across these proxies is whether efficiency-driven estimators preserve the specific quantity IIT defines, or merely correlated signatures of complexity.

## References

Aguilera, M., and Di Paolo, E. A. (2019). Integrated information in the thermodynamic limit. *Neural Networks*.
Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*.
Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. *Brain Stimulation*.
Díaz-Arancibia, J., et al. (2026). GeoMIP. *Applied Sciences*.
Hosaka, T. (2025). Graph neural networks for integrated information and major complex estimation. *PLOS One*.
Kim, H., et al. (2018). Estimating the integrated information measure Phi from high-density EEG. *Frontiers in Human Neuroscience*.
Kitazono, J., Kanai, R., and Oizumi, M. (2018). Efficient algorithms for searching the minimum information partition. *Entropy*.
Liardi, A., et al. (2025). A scalable estimator of higher-order information in complex dynamical systems. arXiv.
Mediano, P. A. M., Seth, A. K., and Barrett, A. B. (2019). Measuring integrated information: comparison of candidate measures. *Entropy*.
Nilsen, A. S., Juel, B. E., and Marshall, W. (2019). Evaluating approximations and heuristic measures of integrated information. *Entropy*.
Oizumi, M., Amari, S., et al. (2016). Measuring integrated information from the decoding perspective. *PLoS Computational Biology*.
Oizumi, M., Tsuchiya, N., and Amari, S. (2016). Unified framework for information integration based on information geometry. *PNAS*.
Tegmark, M. (2016). Improved measures of integrated information. *PLoS Computational Biology*.
