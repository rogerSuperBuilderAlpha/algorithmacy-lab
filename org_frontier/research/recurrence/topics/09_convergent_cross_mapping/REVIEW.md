# Convergent Cross Mapping and State-Space Causality
<!-- run: 2026-06-23 | sources: 15 -->
Search method: Consensus and Scholar Gateway academic search plus targeted WebSearch/WebFetch, with every DOI verified through Crossref; run 2026-06-23.

Convergent cross mapping (CCM) detects causation in nonlinear deterministic systems by exploiting state-space reconstruction. Takens' delay-embedding theorem establishes that a time-delayed embedding of a single observable is diffeomorphic to the original system's attractor (Takens, 1981). CCM uses this to test whether the historical record of an effect variable Y can estimate the states of a putative cause X: if X drives Y, information about X is encoded in Y's reconstructed manifold, so cross-map skill rises and converges toward unity as library length grows (Sugihara et al., 2012). This logic separates the method from correlation, which is symmetric and undirected, and from Granger causality, which presumes separability of causal information and degrades under the "mirage correlations" of coupled deterministic systems (Sugihara et al., 2012; Munch et al., 2023).

The original formulation has been extended along several axes. Time-lagged cross mapping distinguishes direction, separates synchrony-induced coupling from genuine bidirectional forcing, and resolves transitive chains (Ye et al., 2015). Spatial CCM substitutes ensembles of short series for long temporal records (Clark et al., 2015), and a geographical variant performs causal inference on cross-sectional spatial data lacking time series (Gao et al., 2023). Partial cross mapping removes indirect links by combining phase-space reconstruction with partial correlation (Leng et al., 2020), and conditional cross-map techniques extend pairwise tests toward full network reconstruction (Yang et al., 2023). Causalized CCM restricts prediction to past values, restoring temporal precedence, and shows approximate equivalence with directed information under Gaussian processes (Deng et al., 2023; Sun et al., 2024).

The relationship to Granger methods is more nuanced than an outright replacement. Benchmarks on predator-prey, competition, and multi-species networks find linear Granger causality and CCM uncovering interactions with comparable accuracy, with method choice depending on data and aims (Cobey & Baskerville, 2021). Frequency-domain cross-mapping coherence further bridges the two traditions (Benkő et al., 2024).

Critiques temper CCM's reach. Cross-map skill does not always track intuitive notions of driving, and pairwise asymmetric inference can mislabel direction (McCracken & Weigel, 2014). Strong coupling and generalized synchrony produce spurious or collapsed causal estimates (Butler et al., 2023), and related manifold methods such as convergent cross sorting fail under synchrony in both simulated and empirical data (Krakovská & Hanzely, 2023). Butler et al. (2023) supply Gaussian-process diagnostics to flag data unsuitable for cross mapping. The active 2023-2026 literature thus refines embedding choices, conditioning, and equivalence results while mapping the conditions under which state-space causality is trustworthy.

## References
- Benkő, Z., Varga, B., Stippinger, M., & Somogyvári, Z. (2024). Detecting Causality in the Frequency Domain with Cross-Mapping Coherence.
- Butler, K., Feng, G., & Djurić, P. M. (2023). On Causal Discovery With Convergent Cross Mapping.
- Clark, A. T., Ye, H., Isbell, F., Deyle, E. R., Cowles, J., Tilman, G. D., & Sugihara, G. (2015). Spatial convergent cross mapping to detect causal relationships from short time series.
- Cobey, S., & Baskerville, E. B. (2021). Inferring species interactions using Granger causality and convergent cross mapping.
- Deng, J., et al. (2023). Causalized convergent cross-mapping and its approximate equivalence with directed information in causality analysis.
- Gao, B., et al. (2023). Causal inference from cross-sectional earth system data with geographical convergent cross mapping.
- Krakovská, A., & Hanzely, M. (2023). Usefulness and limitations of convergent cross sorting and continuity scaling methods.
- Leng, S., et al. (2020). Partial cross mapping eliminates indirect causal influences.
- McCracken, J. M., & Weigel, R. S. (2014). Convergent cross-mapping and pairwise asymmetric inference.
- Munch, S. B., et al. (2023). Recent developments in empirical dynamic modelling.
- Sugihara, G., et al. (2012). Detecting Causality in Complex Ecosystems.
- Sun, B., et al. (2024). Causalized Convergent Cross Mapping and Its Implementation in Causality Analysis.
- Takens, F. (1981). Detecting strange attractors in turbulence.
- Yang, L., et al. (2023). Conditional cross-map-based technique: From pairwise dynamical causality to causal network reconstruction.
- Ye, H., et al. (2015). Distinguishing time-delayed causal interactions using convergent cross mapping.
