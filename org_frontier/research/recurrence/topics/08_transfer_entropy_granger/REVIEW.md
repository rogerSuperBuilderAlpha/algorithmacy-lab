# Transfer Entropy and Granger Causality
<!-- run: 2026-06-23 | sources: 14 -->
Search method: academic search via Scholar Gateway and Consensus MCP tools plus targeted web search and publisher-page verification; run date 2026-06-23.

Granger causality formalizes directed influence between time series through improvement in linear prediction: a variable Granger-causes another when its past reduces the prediction error of the target beyond the target's own past (Granger, 1969). Transfer entropy reframes the same intuition information-theoretically as the conditional mutual information between a source's past and a target's future given the target's past, requiring no linear model and capturing nonlinear and higher-order dependence (Schreiber, 2000). The two measures were long suspected to be linked, and the connection was made exact by a proof that Granger causality and transfer entropy are identical (up to a factor of two) for jointly Gaussian variables (Barnett et al., 2009). This equivalence licenses a unified reading: parametric vector-autoregressive estimation and model-free entropy estimation target the same quantity under Gaussianity, while transfer entropy generalizes the construct when distributions depart from Gaussian form.

A broader synthesis situates both inside directed information theory, where causal conditioning yields directed information that decomposes into transfer entropies plus an instantaneous-coupling term, and Granger-causality graphs emerge as hypothesis tests on these quantities (Amblard and Michel, 2011; Amblard and Michel, 2012). Extensions to the Rényi family let a tunable parameter weight tail events, and the Gaussian equivalence carries over to Rényi transfer entropy (Jizba et al., 2022). A local formulation resolves the time-averaged measure into a per-sample profile, exposing transient transfers hidden in the mean (Stramaglia et al., 2020).

Estimation remains the practical bottleneck. Model-free estimators built on the Kraskov-Stögbauer-Grassberger k-nearest-neighbor scheme avoid binning but trade bias against variance, with bias growing in embedding dimension. Effective transfer entropy subtracts a surrogate baseline to correct finite-sample bias (Vicente et al., 2011). Neural estimators using the Donsker-Varadhan representation and transformer attention extend estimation to high-dimensional and continuous settings (Luxembourg et al., 2024). For neuroscience-scale data, the multivariate vector-autoregressive toolbox computes conditional Granger causality while avoiding explicit reduced-model estimation (Barnett and Seth, 2014), and greedy multivariate transfer-entropy network inference with hierarchical surrogate testing, implemented in IDTxl, controls false positives across hundreds of nodes (Novelli et al., 2019; Wollstadt et al., 2019). Lag-specific decomposition assigns information transfer to individual delays (Faes et al., 2014). Validation against a multistable decision-network model confirms that conditional multivariate Granger causality recovers ground-truth directed connectivity when windowing is matched to the dynamics, with bivariate measures more prone to spurious links (Asadpour and Wong-Lin, 2024).

## References

- Amblard, P.-O. and Michel, O. J. J. (2011). On directed information theory and Granger causality graphs.
- Amblard, P.-O. and Michel, O. J. J. (2012). The relation between Granger causality and directed information theory: a review.
- Asadpour, A. and Wong-Lin, K. (2024). Can multivariate Granger causality detect directed connectivity of a multistable and dynamic biological decision network model?
- Barnett, L., Barrett, A. B., and Seth, A. K. (2009). Granger causality and transfer entropy are equivalent for Gaussian variables.
- Barnett, L. and Seth, A. K. (2014). The MVGC multivariate Granger causality toolbox.
- Faes, L., Marinazzo, D., Montalto, A., and Nollo, G. (2014). Lag-specific transfer entropy.
- Granger, C. W. J. (1969). Investigating causal relations by econometric models and cross-spectral methods.
- Jizba, P., Lavička, H., and Tabachová, Z. (2022). Causal inference in time series in terms of Rényi transfer entropy.
- Luxembourg, O., Tsur, D., and Permuter, H. (2024). TREET: transfer entropy estimation via transformers.
- Novelli, L. et al. (2019). Large-scale directed network inference with multivariate transfer entropy.
- Schreiber, T. (2000). Measuring information transfer.
- Stramaglia, S. et al. (2020). Local Granger causality.
- Vicente, R., Wibral, M., Lindner, M., and Pipa, G. (2011). Transfer entropy: a model-free measure of effective connectivity for the neurosciences.
- Wollstadt, P. et al. (2019). IDTxl: the Information Dynamics Toolkit xl.
