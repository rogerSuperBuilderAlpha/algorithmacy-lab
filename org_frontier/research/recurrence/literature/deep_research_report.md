<!-- run: 2026-06-26 | sources: 108 | verified: 108 -->
Deep-research run, 2026-06-23. 12 search angles, 24 sources, 24 verified.

## 1. Recurrence plots and RQA foundations
Recurrence plots were introduced to visualize when a trajectory revisits a neighborhood of a prior state in reconstructed phase space (Eckmann, Kamphorst, and Ruelle, 1987). Webber and Zbilut (1994) made the visualization quantitative, defining recurrence rate, determinism, laminarity, trapping time, and diagonal/vertical line statistics, and applied them to physiological signals. The comprehensive methodological reference is the Physics Reports review by Marwan, Romano, Thiel, and Kurths (2007), which formalizes embedding dimension, time delay, recurrence threshold, and the quantifier catalog. Marwan (2008) traces the historical development, and the edited volume by Webber and Marwan (2015) codifies best practices.

## 2. Parameter selection and reproducibility pitfalls
Results depend strongly on embedding parameters, threshold (epsilon), normalization, and theiler windowing. Marwan (2011) enumerates these pitfalls and how tangential motion and threshold choice distort line-based measures. Marwan and Kraemer (2023) update the field with event-like, multiscale, heterogeneous, and spatio-temporal recurrence definitions, parameter-selection heuristics, new transition/causality quantifiers, and recurrence-machine-learning hybrids.

## 3. CRQA for interpersonal coordination
Cross-recurrence quantification analysis embeds two series in a shared phase space and tallies shared locations, quantifying coupling without a generative model. Shockley, Santana, and Fowler (2003) demonstrated greater shared recurrence in postural sway for conversing dyads. This established CRQA as an objective coordination measure for joint action, behavior, and physiology.

## 4. Gaze, language, and categorical streams
Richardson and Dale (2005) applied cross-recurrence to speaker/listener eye movements, recovering a ~2 s lag that predicted discourse comprehension. Dale, Warlaumont, and Richardson (2011) generalized nominal (categorical) cross-recurrence as a lag-sequential analysis for behavioral streams, extending the method beyond continuous signals.

## 5. Physiological synchrony in groups
Konvalinka et al. (2011) used nonlinear heart-rate analysis to show synchronized arousal between fire-walkers and socially related spectators but not unrelated audience members, evidencing physiological coupling structured by social relationship.

## 6. Conversation as interpersonal synergy
Fusaroli and Tylén (2016) contrasted interactive alignment with interpersonal synergy, using recurrence-based complexity matching across prosody, lexical choice, and speech/pause structure to predict collective task performance. Angus (2019) reviews 20 years of recurrence methods for communication data, including conceptual recurrence and the Discursis toolkit.

## 7. Lead-lag, coupling, and synchrony measures
Diagonal-cross-recurrence profiles (DCRP) locate the lag of maximal cross-recurrence, indexing leader-follower structure; windowed cross-recurrence tracks coupling over time (Wallot and Leonardi, 2018). The authors and the package documentation stress that lag peaks are descriptive of temporal precedence and do not warrant causal interpretation (Coco, Mønster, Leonardi, Dale, and Wallot, 2021).

## 8. Multivariate and joint recurrence extensions
MdRQA handles multidimensional single-system series; MdCRQA quantifies co-evolution of two multivariate series (Wallot, 2019). Multivariate joint recurrence quantification detects coupling between series of different dimensionalities (Wallot and Mønster, 2023). The crqa R package consolidates auto-, cross-, multidimensional, windowed, and piecewise methods (Coco and Dale, 2014; Coco et al., 2021).

## 9. Hyperscanning application
Goldstein, Burns, Peck, Dale, and Lieberman (2025) applied CRQA to fNIRS dyads during free-flowing negotiation. Balanced (symmetric) lead-lag neural coupling predicted collaborative adjustment and positive experience, while inter-subject correlation and wavelet coherence showed no such associations, positioning CRQA as sensitive to dynamic coupling that static synchrony measures miss.

## 10. Transfer entropy and Granger causality
Schreiber (2000) defined transfer entropy, conditioning out shared history to isolate directed information flow; it is a nonparametric generalization of Granger causality and reduces to it for Gaussian variables. Wibral, Vicente, and Lizier (2014) consolidate transfer-entropy estimation for neuroscience time series.

## 11. Convergent cross mapping
Sugihara et al. (2012) introduced CCM, using time-delay state-space reconstruction (Takens embedding) to detect causation in weakly-to-moderately coupled nonlinear deterministic systems, distinguishing causality from mere correlation where Granger methods can fail.

## 12. Comparative benchmarking of causality indices
Edinburgh, Eglen, and Ercole (2021) benchmarked ten bivariate causality indices across four model systems, recommending transfer entropy and nonlinear Granger causality for robustness to noise, missing data, and rounding, with open Python code. This frames how recurrence-derived lag structure relates to, but does not substitute for, directed-causality estimates.

## Gap
The program lacks a method that unifies recurrence-based coordination quantification with formal directed-causality inference: DCRP and windowed CRQA describe temporal precedence but explicitly disclaim causal interpretation, while transfer entropy and CCM target direction yet are not natively expressed in recurrence terms. Recurrence-native causality quantifiers (recurrence measure of conditional dependence, conditional joint recurrence plots, recurrence flow) are emerging but were not consistently confirmed in peer-reviewed venues during this run and remain under-benchmarked against CRQA on real coordination data. There is no validated bridge from CRQA coupling estimates to integrated-information (Phi) quantities, no standardized significance/surrogate testing protocol shared across the coordination-CRQA literature, and no head-to-head evaluation of CRQA versus transfer entropy and CCM on the same naturalistic dyadic datasets. Coordination mediated by an opaque, interested third party (the lab's specific interest) is absent from the empirical recurrence literature, which assumes direct dyadic coupling.
