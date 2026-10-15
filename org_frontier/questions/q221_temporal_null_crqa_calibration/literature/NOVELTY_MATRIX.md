# q221 novelty matrix (gate F)

This matrix extends `org_frontier/research/recurrence/REVIEW.md` and `literature/NOVELTY_ASSESSMENT.md`.

**Sources of DOIs.**
- Recurrence works: `org_frontier/research/recurrence/literature/references.bib`, which the lab review verified.
- Others: `literature/LITERATURE_REGISTER_DRAFT.md`.

**Claim-check levels.**
- **F**: full text checked;
- **A**: abstract checked;
- **S**: search snippet only;
- **R**: as summarised by the lab review;
- **M**: metadata only.

| prior work | statistic / formalism | identifiability claim | assumptions | established | Q221 adds | evidence missing |
|---|---|---|---|---|---|---|
| Eckmann, Kamphorst & Ruelle 1987, EPL 4:973 (10.1209/0295-5075/4/9/004) (R) | Recurrence plot of a reconstructed trajectory | None | Deterministic dynamics; embedding | Visual recurrence analysis | — | — |
| Webber & Zbilut 1994, J. Appl. Physiol. 76:965 (10.1152/jappl.1994.76.2.965) (R) | RQA quantifiers (RR, DET, LAM) | None | Embedding; threshold | Quantitative RQA | — | — |
| Marwan, Romano, Thiel & Kurths 2007, Phys. Rep. 438:237 (10.1016/j.physrep.2006.11.001) (R) | RP / RQA / CRQA / JRP theory | Some recurrence-based invariants of dynamics (outside q221's scope) | Continuous systems, embedding | The canonical theory | Population pairwise *categorical* profiles in a finite Markov family retain exactly the Corollary data (`THEORY.md`) | Whether joint recurrence plots (JRP) separate the q221 survivors; not run |
| Coco & Dale 2014, Front. Psychol. 5:510 (10.3389/fpsyg.2014.00510) (S, PMC) | Categorical CRQA, DCRP | None; measures are "descriptive … not inferential" | Categorical series; baselines from shuffles or virtual pairs | For categorical series, a shuffle gives about the same *expected* profile as surrogate pairing | Matching the mean is not calibration. Gate E measures the type-I error | Virtual-pair (false-pair) nulls not tested |
| Wallot & Leonardi 2018, Front. Psychol. 9:2232 (10.3389/fpsyg.2018.02232) (F) | CRQA, DCRP, MdRQA tutorial | None | Baselines: false pairs (conservative), shuffles (liberal), chunk-preserving shuffles | Common practice for DCRP baselines | q220's statistic is a DCRP prominence. Gate E reports its FPR under four surrogates | False-pair baseline not tested |
| Wallot 2019, Multivariate Behav. Res. (10.1080/00273171.2018.1512846) (R/S) | MdCRQA: joint multichannel recurrence | None | Multivariate embedding | Shuffled baseline is liberal; false pairs conservative | — | Whether MdCRQA separates the survivors |
| Schreiber 2000, PRL 85:461 (10.1103/PhysRevLett.85.461) (R) | Transfer entropy | Directed influence, conditional on history | Stationarity, estimation | Multi-point and conditioned statistics capture directed dependence | Proposition 2 (one-step (|row| + 1)-point parity statistics) is a TE-like separator in the affine class | Bivariate TE on the survivors not computed |
| Sugihara et al. 2012, Science 338:496 (10.1126/science.1227079) (R) | Convergent cross mapping | Causation in weakly coupled deterministic systems | Shadow-manifold reconstruction | Separating causation from correlation | — | Not computed |
| Edinburgh, Eglen & Ercole 2021, Chaos (10.1063/5.0053519) (R) | Benchmark of 10 bivariate causality indices | Comparative performance | Simulated benchmarks | TE and nonlinear Granger are robust | — | — |
| Romano & Tirlea 2022, JTSA 43:781 (10.1111/jtsa.12638) (A) | Permutation tests for serial dependence of one series | Level-α fails without studentisation | A single series | Permutation tests misbehave under dependence | Gate E is the cross-dependence analogue, in a known DGP. Not new | — |
| Yuan & Shou 2022, eLife 11:e72518 (10.7554/eLife.72518) (F) | Correlation tests with shuffle and phase surrogates | — | Autocorrelated biological series | Shuffle FPR of 30–92% | **Nothing new.** The pilot's 34% / 67.2% are the same phenomenon | — |
| Yuan & Shou 2024, PLOS Biol 22:e3002758 (10.1371/journal.pbio.3002758) (F) | Truncated time-shift test | Valid FPR if one series is stationary | Stationarity of one series | Circular, block, IAAFT and twin surrogates can each be miscalibrated | Gate E measures these for q220's prominence statistic | TTS itself not implemented |
| Gilpin 2025, PRX 15:011005 (10.1103/PhysRevX.15.011005) (F) | Shared recurrences, SHREC driver reconstruction | Recovers multiplicative drivers that pairwise inference misses; drivers with equivalent influence are not identifiable without intervention | Common-driver setting; observational | Recurrence across *multiple* series can capture higher-order structure that pairwise methods lose | An exact, finite-state statement of what *pairwise* categorical profiles lose (Proposition 1, Corollary). Its consequence for a perturbational (IIT/q161) target | SHREC on the survivors not run |
| Williams & Beer 2010 (arXiv:1004.2515) (F); James & Crutchfield 2017, Entropy 19:531 (10.3390/e19100531) (A) | PID; dyadic vs polyadic distributions | Pairwise and Shannon measures miss synergy | Static distributions | Pairwise blindness to XOR | A dynamic, all-lag version for Boolean Markov chains with a closed form | — |
| Mayner et al. 2018, PLoS Comput. Biol. 14:e1006343 (10.1371/journal.pcbi.1006343) (M); Albantakis et al. 2023, PLoS Comput. Biol. 19:e1011465 (10.1371/journal.pcbi.1011465) (M) | PyPhi; IIT 4.0 | Φ, major complex | Perturbational TPM; IIT 4.0 axioms | The formalism q161 uses (PyPhi `feature/iit-4.0` @ `b78d0e34`) | 3 classes of pairwise-equivalent systems with the same major complex and Φ but different q161 leave-one-out targets | No claim about IIT itself |
| Barrett & Seth 2011, PLoS Comput. Biol. 7:e1001052 (10.1371/journal.pcbi.1001052) (A) | Empirical Φ from time series | Φ-like measures from observational data | Stationarity | Observational integrated-information measures exist | Different target (IIT-4.0 perturbational q161 bottleneck) | — |

**Later work (to 2026-10-15).**
- A web search found no work on the identifiability of IIT-4.0 or q161-type targets from recurrence
  summaries. The search was cursory.
- arXiv:2205.04440 (S) reports model-free higher-order interactions that distinguish Boolean dynamics which
  correlations and mutual information cannot. It is related, but static and not about recurrence.

## Strongest competing interpretation

Proposition 1 is an elementary consequence of Walsh–Fourier analysis of linear GF(2) systems. Pairwise
blindness to higher-order structure is textbook (Williams & Beer; James & Crutchfield; Gilpin). On this
reading, the only q221-specific content is:
1. that the lab's own family contains such pairs;
2. that the q161 leave-one-out target is sensitive to an out-of-complex node.

Item (2) is arguably a property of the target definition, not a discovery about recurrence. The calibration
pilot re-shows Yuan & Shou (2022). **That reading is accepted as largely correct.** Q221's defensible
contribution is narrow:
- an exact, checkable characterisation;
- an audit of the lab's own pipeline;
- the measured FPRs (gate E) for q220's actual statistic.
