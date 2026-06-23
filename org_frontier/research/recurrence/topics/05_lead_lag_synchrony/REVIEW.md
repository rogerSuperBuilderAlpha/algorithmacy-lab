# Lead-Lag, DCRP, and Windowed Synchrony
<!-- run: 2026-06-23 | sources: 12 -->
Search method: Scholar Gateway and Consensus academic search plus targeted WebSearch/WebFetch DOI verification (Crossref, publisher pages); run 2026-06-23.

Recurrence-based estimation of leader-follower lag descends from the cross recurrence plot (CRP), whose distorted main diagonal—the line of synchronization—encodes time offsets between two embedded signals (Marwan, 2002). Building on the CRP, the diagonal cross-recurrence profile (DCRP) reads recurrence rate as a function of diagonal offset: the lag at which the profile peaks indexes who leads and by how much, while the peak height indexes coupling strength (Wallot, 2018a). Foundational tutorials formalize the DCRP alongside CRQA and multidimensional recurrence quantification, and supply the `crqa` R implementation used across the field (Wallot & Leonardi, 2018; Coco et al., 2021). The multidimensional cross-recurrence extension (MdCRQA) generalizes the DCRP to vector-valued time series, allowing lagged coupling between two multivariate streams to be summarized in a single profile (Wallot, 2018b).

Two complementary directions address the constraint that early DCRP work treats lag and coupling as stationary over a recording. First, windowing recovers time resolution: windowed multiscale synchrony decomposes signals by wavelet scale and tracks phase synchronization within sliding windows, exposing coordination that forms and dissipates within a single observation (Likens & Wiltshire, 2020). Sliding-window time-lagged cross-correlation likewise models a moving lead-lag structure and improves prediction of social-psychological outcomes from facial-expression dynamics (Hojo et al., 2023). Second, lag is built directly into the recurrence estimator: lagged multidimensional recurrence quantification analysis shifts one multivariate stream against another and quantifies joint dynamics under explicit leader-follower offsets, extending the group case beyond dyads (Tomashin et al., 2024). Inter-system recurrence networks pursue coupling direction through graph-theoretic cross-clustering, though distinguishing weak bidirectional coupling from no coupling remains difficult (Hasselman et al., 2023).

Applications validate the DCRP lag as a behavioral proxy. Dual eye-tracking studies read characteristic gaze-lag times to assign initiator and follower roles in pair programming and in sonography instruction, where teacher-led coupling toward anatomical references tracked learning (Darici et al., 2025). Speech-coordination work combines CRQA, the DCRP, and anisotropic CRQA to separate lag-zero coordination from directional leading-following, linking both to personality and conversational appraisals (Arellano-Véliz et al., 2025). Kinematic analysis of joint tower building found head and wrist motion synchronizing at distinct lags, with the leader driving longer-lag head coupling (Coco et al., 2017). Recent fNIRS hyperscanning uses CRQA to show that balanced, symmetric leading and lagging—rather than immediate alignment—predicted cooperative negotiation outcomes (Goldstein et al., 2026).

Open problems concern embedding-parameter sensitivity, window-length and resolution trade-offs, and statistical baselines that separate genuine directional coupling from shared structure under non-stationarity.

## References
- Arellano-Véliz, N. A., et al. (2025). Beyond Words: Speech Coordination Linked to Personality and Appraisals.
- Coco, M. I., et al. (2017). Multilevel Behavioral Synchronization in a Joint Tower-Building Task.
- Coco, M. I., Mønster, D., Leonardi, G., Dale, R., & Wallot, S. (2021). Unidimensional and Multidimensional Methods for Recurrence Quantification Analysis with crqa.
- Darici, D., et al. (2025). Leader-follower dynamics in medical training: A dual mobile eye-tracking analysis.
- Goldstein, B. M., et al. (2026). Cross-recurrence quantification analysis captures inter-brain coupling during naturalistic negotiation.
- Hasselman, F., et al. (2023). The geometry of synchronization: inter-system recurrence networks.
- Hojo, N., et al. (2023). Modeling Lead-Lag Structure in Facial Expression Synchrony.
- Likens, A. D., & Wiltshire, T. J. (2020). Windowed multiscale synchrony.
- Marwan, N., Thiel, M., & Nowaczyk, N. R. (2002). Cross recurrence plot based synchronization of time series.
- Tomashin, A., et al. (2024). Lagged multidimensional recurrence quantification analysis.
- Wallot, S. (2018b). Multidimensional Cross-Recurrence Quantification Analysis (MdCRQA).
- Wallot, S., & Leonardi, G. (2018). Analyzing Multivariate Dynamics Using CRQA, DCRP, and MdRQA — A Tutorial in R.
