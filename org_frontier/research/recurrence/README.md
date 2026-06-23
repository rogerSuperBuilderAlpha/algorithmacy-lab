# Recurrence research — coordination read off behavior

The literature watch for the recurrence arm: cross-recurrence quantification analysis and recurrence plots,
coordination and interpersonal dynamics read from time series, the lead-lag, coupling, and synchrony measures
that read who leads, and how these compare with Granger causality, transfer entropy, and convergent cross
mapping. This is the reading behind pairing exact Φ with the behavioral instrument.

## Topics

| # | topic | scope |
|---|---|---|
| 01 | [Recurrence Plot Foundations and RQA Measures](topics/01_recurrence_plot_foundations/REVIEW.md) | The origin of recurrence plots and the definition and interpretation of the core RQA quantifiers (recurrence rate, determinism, laminarity, line statistics). |
| 02 | [CRQA Method and Parameter Selection](topics/02_crqa_method_parameters/REVIEW.md) | How cross-recurrence quantification is constructed and the embedding, delay, threshold, and normalization choices that govern reproducibility and pitfalls. |
| 03 | [Interpersonal Coordination via CRQA](topics/03_interpersonal_coordination_crqa/REVIEW.md) | Empirical CRQA studies of postural, gestural, and behavioral coordination between interacting people in joint-action and conversational settings. |
| 04 | [Gaze and Linguistic Coupling](topics/04_gaze_language_coupling/REVIEW.md) | Cross-recurrence analyses of speaker-listener eye movements, categorical behavioral streams, and lexical/prosodic alignment in dialogue. |
| 05 | [Lead-Lag, DCRP, and Windowed Synchrony](topics/05_lead_lag_synchrony/REVIEW.md) | Diagonal-cross-recurrence profiles and windowed cross-recurrence for estimating leader-follower lag and time-varying coupling strength. |
| 06 | [Multivariate and Joint Recurrence Extensions](topics/06_multivariate_joint_recurrence/REVIEW.md) | MdRQA, MdCRQA, and joint recurrence methods for multidimensional and mixed-dimensionality time series and group-level coordination. |
| 07 | [Physiological and Inter-Brain Synchrony](topics/07_physiological_synchrony/REVIEW.md) | Recurrence-based quantification of coupled physiological signals and inter-brain coupling in hyperscanning (EEG/fNIRS) during social interaction. |
| 08 | [Transfer Entropy and Granger Causality](topics/08_transfer_entropy_granger/REVIEW.md) | Information-theoretic directed-influence measures, their relationship to Granger causality, and estimation practice for coupled time series. |
| 09 | [Convergent Cross Mapping and State-Space Causality](topics/09_convergent_cross_mapping/REVIEW.md) | Takens-embedding-based causality detection in nonlinear deterministic systems and its contrast with correlation-based and Granger methods. |
| 10 | [Causality Method Benchmarks and Software](topics/10_causality_method_benchmarks/REVIEW.md) | Comparative benchmarking of recurrence, transfer entropy, Granger, and cross-mapping indices, plus the R and Python tooling that implements them. |

## Files

- [`REVIEW.md`](REVIEW.md) — the curated synthesis of the program's literature.
- [`literature/deep_research_report.md`](literature/deep_research_report.md) — the cited survey and the gap statement.
- [`literature/references.bib`](literature/references.bib) — the program bibliography.
- [`topics/`](topics/) — the ten topics, each with its own review and bibliography.
