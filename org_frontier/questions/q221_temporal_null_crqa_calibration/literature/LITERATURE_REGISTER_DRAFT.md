# q221 literature register (DRAFT, in progress)

This register is prospective for any future confirmatory study. No pilot code has run. The full review
(claim-to-source matrix, novelty gate) is not finished.

Raw downloads are kept outside the repo, on the box at `/workspace/q221-lit`.

**Verification levels.**
- **M:** Crossref metadata only.
- **A:** abstract checked.
- **F:** full text checked for the stated claim.

| source | DOI / id | level | claim checked |
|---|---|---|---|
| Gilpin 2025, *Recurrences Reveal Shared Causal Drivers of Complex Time Series*, PRX 15:011005 | 10.1103/PhysRevX.15.011005; arXiv:2301.13516v3 | F (arXiv HTML) | SHREC rebuilds an unobserved shared driver from shared recurrences across response series; §III.2 recovers multiplicative (higher-order) drivers that pairwise inference misses. It has no surrogate-calibration or FPR study, and its benchmarks compare reconstruction accuracy, not calibration |
| Yuan & Shou 2022, *Data-driven causal analysis of observational biological time series*, eLife 11:e72518 | 10.7554/eLife.72518 | F (PMC9391047) | **The "2022 study".** For independent autocorrelated series (their Fig 2B–C), shuffle-permutation gives p < 0.05 at "30∼92%". Phase randomisation gives 4% when its assumptions hold and 21% under nonstationarity |
| Yuan & Shou 2024, *A rigorous and versatile statistical test for correlations between stationary time series*, PLOS Biol 22:e3002758 | 10.1371/journal.pbio.3002758 (bioRxiv 10.1101/2022.01.25.477698) | F (PMC11398661) | Truncated time-shift (TTS) test. It provably controls FPR if one series is stationary, and works with any statistic. The naive time-shift test is inflated at most 2×. In their benchmark, **cyclic permutation** (with circularisation), IAAFT, stationary block bootstrap and twin surrogates all exceeded 5% in at least one stationary system. **So circular shifts are neither novel nor guaranteed valid; the plan's §3.3 "circular shift ✔" is corrected by this** |
| Romano & Tirlea 2022, *Permutation testing for dependence in time series*, JTSA 43:781–807 | 10.1111/jtsa.12638 | A | Covers **serial** dependence of one series (the null is an uncorrelated sequence). Permutation tests are not level-α for that null. Studentised fix. *It is not about cross-dependence of two series.* The blueprint's "Romano et al." is Romano & **Tirlea** |
| Phipson & Smyth 2010, SAGMB 9(1) art. 39 | 10.2202/1544-6115.1585 | F (arXiv:1603.05766) | Random permutations should give exact p-values; never report zero |
| Theiler, Eubank, Longtin, Galdrikian & Farmer 1992, Physica D 58:77 | 10.1016/0167-2789(92)90102-S | M | |
| Schreiber & Schmitz 1996, PRL 77:635 | 10.1103/PhysRevLett.77.635 | M | |
| Schreiber & Schmitz 2000, Physica D 142:346 | 10.1016/S0167-2789(00)00043-9 | F (arXiv chao-dyn/9909037, downloaded; claims still to extract) | |
| Schreiber 1998, PRL 80:2105 | 10.1103/PhysRevLett.80.2105 | M | |
| Künsch 1989, Ann. Statist. 17:1217 | 10.1214/aos/1176347265 | A | |
| Politis & Romano 1994, JASA 89:1303 | 10.1080/01621459.1994.10476870 | M | |
| Marwan, Romano, Thiel & Kurths 2007, Phys. Rep. 438:237 | 10.1016/j.physrep.2006.11.001 | M | |
| Marwan 2011, *How to avoid potential pitfalls in recurrence plot based data analysis*, IJBC 21:1003 | 10.1142/S0218127411029008 | M | |
| Wallot & Leonardi 2018, CRQA/DCRP/MdRQA tutorial in R, Front. Psychol. 9:2232 | 10.3389/fpsyg.2018.02232 | F | Suggests shuffling as a CRQA baseline. For categorical series, suggests shuffling "without 'breaking' the chunks" (a block shuffle) |
| Albantakis et al. 2023, IIT 4.0, PLoS Comput Biol 19:e1011465 | 10.1371/journal.pcbi.1011465 | M (full text downloaded; claims still to extract) | |
| Edelson & Krolik 1988, discrete correlation function, ApJ 333:646 | 10.1086/166773 | M | |
| Parzen (irregular / missing-observation spectral analysis) | **not yet identified**; OpenAlex search inconclusive | — | |
| Andrzejak et al. 2003, PRE 68:066202 | 10.1103/PhysRevE.68.066202 | M (the guessed arXiv id was wrong) | |
| Bradley 1978, BJMSP 31:144 | 10.1111/j.2044-8317.1978.tb00581.x | M | The band [0.5α, 1.5α] is **not yet verified in the text** |
| Holm 1979, Scand. J. Statist. 6:65–70 | no DOI; cited with these details in Crossref reference metadata of Romano & Tirlea 2022 | **unverified** (no primary source) | Bonferroni is the default, per Hassan |
| Williams & Beer 2010, *Nonnegative Decomposition of Multivariate Information* | arXiv:1004.2515 | F | XOR: each source alone carries no information; together they carry all of it |
| Schneidman, Still, Berry & Bialek 2003, PRL 91:238701 | 10.1103/PhysRevLett.91.238701 | A | Connected information: N-point correlation beyond the max-entropy model given all (N−1)-variable marginals |
| James & Crutchfield 2017, *Entropy* 19:531 | 10.3390/e19100531; arXiv:1609.01233 | A | Shannon measures conflate dyadic and polyadic dependency |
| Rosas, Mediano, Gastpar & Jensen 2019, PRE 100:032305 | 10.1103/PhysRevE.100.032305 | A | O-information for synergy vs redundancy |
| Battiston et al. 2020, Phys. Rep. 874:1 | 10.1016/j.physrep.2020.05.004 | M | Higher-order interactions |
| Harris 2020, *Nonsense correlations in neuroscience*, bioRxiv | 10.1101/2020.11.29.402719 | snippet only (the full-text fetch failed) | Circular shift and phase randomisation "can all produce nonsense correlations"; session permutation is valid |
