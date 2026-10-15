# q221 feasibility plan: temporal-null calibration of CRQA (design only)

**Status.** Design document. No experiment has been run for q221, no code has been written, no branch, commit or PR
exists, and nothing on GitHub was changed. The file sits untracked in the local clone `/workspace/algorithmacy-827`
(checked out on `q220-post-merge-corrections` at `cdfea22d`). It is not part of PR #841 and must not be added to it.
q220, q161 and every branch are untouched.

**Proposed id.** `q221` is free (checked 2026-10-15, 12:13 ET): there is no `q221*` directory on `upstream/main`
(`c9818b03`, Roger's repo) or `upstream/contrib` (`44f9b491`). Roger's repo has only those two branch heads plus PR
refs, and no branch name matches `q22[1-9]`. The only open PR is #841 (q220 corrections). No file on `upstream/main`
mentions "q221". The highest probe row in `org_frontier/probes/PROBES.md` is 463 (q220) on both `main` and
`contrib`, so the study's probes would start at **464**. Suggested slug: `q221_temporal_null_crqa_calibration`.

**Provisional title.** Temporal-null calibration of CRQA.

**Research question (Hassan).** If the null keeps each channel's temporal autocorrelation, does CRQA still pick the
correct structural bottleneck more often than a matched chance baseline? The primary objective is
*calibration*. Rescuing q220's S2-H1 is out of scope.

---

## 0. How this fits the lab's protocol

Repo conventions (read from the files cited):

- **Numbering and folder.** Each question gets its own directory, `org_frontier/questions/q<NN>_<slug>/`
  (`org_frontier/AGENTS.md:13`, `org_frontier/protocol/RESEARCH_PROTOCOL.md:21`). The scaffold is
  `python -m org_frontier.protocol.new_question --id 221 --slug temporal_null_crqa_calibration --question "…"`.
  It copies `org_frontier/protocol/template/` and fills in the next probe number from `PROBES.md`
  (`org_frontier/protocol/new_question.py:1-17`).
- **Templates.** The scaffold provides `review.md`, `hypotheses.md` (H1–H5, each with its H0 and a predicted outcome),
  `methods.md` (form/ensemble, measure, controls and a decision rule per hypothesis, plus an instrument control that
  runs first), `paper.md`, `FINDINGS.md` and `probe_template.py`. q220 stage 2 added a standalone
  `PREREGISTRATION.md` (`…/q220_observation_process_robustness/stage2/PREREGISTRATION.md`). q221 should follow that
  model, because the decision rules carry the credibility (`RESEARCH_PROTOCOL.md:58-62`).
- **Literature first.** Stage 2 (deep research) must finish before Stage 3 (hypotheses), and the hypotheses must be
  committed before any computation (`RESEARCH_PROTOCOL.md:14-17, 32-38, 40-44`). The literature gate asks for about
  15–30 real sources with DOIs and open-access status, plus an explicit statement of the gap
  (`RESEARCH_PROTOCOL.md:35-38`). q220 broke this order, and #841 states that openly (LITERATURE_NOVELTY L3). q221
  must not repeat it.
- **Indexing and registration.** The new question is indexed with `python tools/build_index.py` and gets a row in
  the generated `README.md` directory, as q220 has at `README.md:645`. Probe rows go into
  `org_frontier/probes/PROBES.md` with global numbering. Every reported number is registered in
  `ci/reproduce.json`, and all three `--check`s must pass (`AGENTS.md:77-92, 108-109, 125-136`).
- **Instrument control first.** A known control must pass before any comparison is made (`RESEARCH_PROTOCOL.md:69-71`).
  The `RESEARCH_PROTOCOL.md:70` text names `~/iit-playground/venv-4.0/bin/python`; q220 used the repo venv on
  Python 3.12.

Proposed order for q221. Each step is gated on the previous one:

1. Stage 1 `review.md`: the lab's prior work (§1 and §2.4).
2. Stage 2 `literature/deep_research_report.md` + `references.bib`, done **prospectively**. §2 gives a verified seed
   list.
3. **Feasibility pilot (§4)** on development forms and seeds only. Its go/no-go rules (§4.6) are committed before it
   runs. *This step is not in the protocol, which has no pilot stage. Section 8 lists it as an open decision for the
   maintainers.*
4. Stage 3/4: `hypotheses.md`, `methods.md` and `PREREGISTRATION.md` (skeleton in §5), committed and pushed before
   the confirmatory run.
5. Stage 5: the confirmatory run on held-out forms and seeds. Stage 6: `paper.md` and `FINDINGS.md`.

---

## 1. Verified motivating facts

Line references for code and results files hold both at local HEAD `cdfea22d` and on `upstream/main`
(`c9818b03`): the files are byte-identical in both places (checked with `git diff --quiet`). Line references for
`FINDINGS.md`, `paper.md` and `PREREGISTRATION.md` are at `cdfea22d` (PR #841's branch), because #841 edits those
files. `Q = org_frontier/questions/q220_observation_process_robustness`.

| # | Hassan's statement | verified fact | source |
|---|---|---|---|
| F1 | S2-H1's +0.204 is concentrated in 4 of 12 curated forms | **Verified.** S2-H1 (B − A, MAR 0.3) = +0.204 [+0.015, +0.417], with forms +4/−1, sign p = 0.375, dz = 0.57. Per-form values: `substitutable_counterparts` +0.850, `deep_pool_all` +0.800, `deep_substitutable` +0.600, `one_counterpart_constitutive` +0.400, `gig_false_dyad` −0.200, seven forms at 0.000. (2.45/12 = 0.204.) These are four of the five forms that dropped in stage 1. | `Q/stage2/results/stage2_stdout.txt:147`; `Q/stage2/results/stage2_per_form.txt:1-13`; `Q/FINDINGS.md:186-190`; `Q/paper.md:62-63` |
| F2 | about −0.007 on 30 independent random forms | **Verified, with a caveat.** S2-H6a (B − A, R2, MAR 0.3) = −0.007 [−0.082, +0.078], INCONCLUSIVE; forms +9/−12. Caveat: this is the gap-closing contrast, not the bottleneck-vs-chance contrast. On R2 the clean decoder itself is not clearly above chance: S2-H6b (CLEAN − \|B\|/n) = +0.136 [−0.001, +0.272]. R2 is therefore a weak test of anything that depends on bottleneck signal. | `stage2_stdout.txt:152-153`; `stage2_per_form.txt:66-96`; `Q/FINDINGS.md:15, 215-220`; `Q/paper.md:65` |
| F3 | the shuffle null destroys autocorrelation | **Verified by construction.** `shuffle_null` permutes each channel's time order independently, which removes all serial dependence in expectation and keeps only the marginal distribution. It is used once per run as NULL-CLEAN (`default_rng(20_000+seed)`). **Its measured impact depends on the form** (see F3b). | `Q/corruptions.py:48-53`; `Q/stage2/probe_stage2.py:125-128`; `Q/stage2/PREREGISTRATION.md:97-100`; `Q/FINDINGS.md:273-277`; `Q/paper.md:315-316`; review `CODE_AUDIT.md:21` |
| F3b | (refinement) | The review's diagnostic (`.verify/autocorr.txt`, lag-1 self-match, mean over channels, seeds 1000–1004) mixes marginal imbalance with dependence. For a binary channel, P(x_t = x_{t+1}) = p² + q² + 2·Cov(x_t, x_{t+1}), and shuffling keeps p² + q². So (raw − shuffled)/2 estimates the channel-mean lag-1 autocovariance. Arithmetic on the review's committed numbers: chat_dyad +0.051, ats_feedback_factors +0.054, decoupled_control +0.059, gig_false_dyad +0.039; **the four S2-H1 forms: substitutable_counterparts −0.005, deep_pool_all −0.001, deep_substitutable −0.005, one_counterpart_constitutive +0.007.** The shuffle removes the *least* lag-1 dependence on exactly the forms that carry S2-H1. Two of them are slightly anti-persistent on average. Limits: this is a channel average at lag 1 only, and opposite-sign channels can cancel. No new computation was run. | `/workspace/algorithmacy-827-claude-review/.verify/autocorr.txt:1-12` (not in the repo) |
| F4 | the effect disappears at MAX_LAG = 5, but the clean signal also degrades | **Verified.** At `max_lag=5`, B − A = −0.019 [−0.119, +0.108] and CLEAN = 0.585 [0.385, 0.783], against chance \|B\|/n = 0.556 (main run: CLEAN 0.785). A preregistered descriptive sensitivity check; `MAX_LAG` was never varied in a confirmatory test. | `stage2_stdout.txt:55, 57, 250`; `Q/stage2/probe_stage2.py:43, 51`; `Q/stage2/PREREGISTRATION.md:169-171`; `Q/FINDINGS.md:13, 200-201` |
| F5 | (relevant) the shuffle null rarely gives the decoder any evidence | NULL-CLEAN is flagged no-evidence (no pair prominence above `PROM_FLOOR = 0.05`) in 74.2% of R1 runs and 78.8% of R2 runs. Its BN score then equals \|B\|/n by construction, so S2-H7b largely restates S2-H7a. | `stage2_stdout.txt:201, 223`; `Q/stage2/observe.py:209-217`; review `STATS_AUDIT.md:27` |
| F6 | (relevant) on random forms the shuffle null is *above* uniform chance | R2 NULL-CLEAN gain over \|B\|/n = +0.017 [+0.002, +0.031]. Marginal structure alone (shuffling keeps each channel's marginal) moves the decoder off uniform chance. The q221 design must separate marginal-driven agreement from coupling-driven agreement. | `stage2_stdout.txt:104`; review `STATS_AUDIT.md:28` |
| F7 | (relevant) chance baselines depend on decoder tie-breaking | In stage 1, the shuffled null "0.703" was a tie-break artefact (argmax → node 0 in 283/320 shuffled runs). The tie-aware score fixes this. q221 keeps the tie-aware score. | `Q/FINDINGS.md:81-85`; `Q/stage2/observe.py:209-217` |
| F8 | (relevant) the decoder is a thresholded statistic, not a test | Prominence = profile peak minus its median over usable lags. Centrality sums prominences above a fixed floor of 0.05. The BN pick is the argmax set. No p-value or surrogate distribution is involved. The prominence statistic **ignores where the peak sits in lag**, which matters for periodic processes (§3). | `Q/stage2/observe.py:151-160, 194-217`; `org_frontier/recurrence/crqa.py:125-166` |
| F9 | (relevant) the generating process | Synchronous Boolean network with independent per-node flip noise (default 0.08 in q220) and 20 warm-up steps: a finite ergodic Markov chain on the joint state. Each channel is a *projection* of that chain, so it is generally not a finite-order Markov chain itself. `random_wiring` forms have no self-inputs (each node reads only the others). | `org_frontier/recurrence/crqa.py:32-51`; `org_frontier/questions/q162_feature_ablation_minimal/probe_feature_ablation_minimal.py:177-185` |
| F10 | (relevant) the inference used | Two-stage form-then-seed percentile bootstrap, 2,000 resamples. No multiplicity adjustment. The 95% lower bound of S2-H1 is positive under percentile, BCa and form-only intervals and negative under basic and t (post-hoc). | `Q/stage2/stats.py:22-35`; `Q/stage2/PREREGISTRATION.md:128-130`; review `STATS_AUDIT.md:21, 66-86` |

**What the facts imply for q221.**
- (a) The temporal-null question is real for the decoder in general: F3, F5, F6 and F8.
- (b) The temporal-null question is **unlikely to bear on S2-H1**. The shuffle changed lag-1 dependence least on the
  four forms that carry S2-H1 (F3b).
- (c) Random-form bottleneck signal is weak (F2), so the power and bottleneck-identification outcomes are at risk
  from the start.

---

## 2. Literature-first step (prospective)

The protocol's Stage 2 must be written and committed **before any pilot code runs**. The list below is the verified
seed bibliography for that report.

**Verification method.**
- Each DOI was resolved with WebFetch against the Crossref API, `api.crossref.org/works/<doi>` or
  `…/works?filter=doi:…`. That confirmed title, authors, venue, year, volume and pages.
- Content claims were checked against abstracts where one could be retrieved: Crossref, Europe PMC REST and the
  Semantic Scholar API. The Coco & Dale and Wallot content comes from publisher-page excerpts returned by a web
  search.
- Where only metadata was verified, a content claim is marked "(metadata only)" and must be checked against the full
  text in Stage 2.

### 2.1 Surrogate-data foundations

| ref | DOI | verified | relevance |
|---|---|---|---|
| Theiler, Eubank, Longtin, Galdrikian & Farmer (1992). Testing for nonlinearity in time series: the method of surrogate data. *Physica D* 58:77–94 | 10.1016/0167-2789(92)90102-S | Crossref ✔ (metadata only) | Origin of the surrogate-data method: a null hypothesis is defined by which properties the surrogates keep |
| Schreiber & Schmitz (1996). Improved surrogate data for nonlinearity tests. *PRL* 77:635–638 | 10.1103/PhysRevLett.77.635 | Crossref ✔ (metadata only) | IAAFT: keeps the value distribution exactly and the spectrum approximately |
| Schreiber & Schmitz (2000). Surrogate time series. *Physica D* 142:346–382 | 10.1016/S0167-2789(00)00043-9 | Crossref ✔ (metadata only) | Review: constrained realisations, end-point and periodicity issues, multivariate surrogates |
| Theiler & Prichard (1996). Constrained-realization Monte-Carlo method for hypothesis testing. *Physica D* 94:221–235 | 10.1016/0167-2789(96)00050-4 | Crossref ✔ (metadata only) | Constrained vs typical realisations; pivotal statistics |
| Schreiber (1998). Constrained randomization of time series data. *PRL* 80:2105–2108 | 10.1103/PhysRevLett.80.2105 | Crossref ✔ (metadata only) | General constrained randomisation (annealing), applicable to arbitrary constraints such as binary ACFs |
| Kugiumtzis (1999). Test your surrogate data before you test for nonlinearity. *PRE* 60:2808–2816 | 10.1103/PhysRevE.60.2808 | Crossref ✔ (metadata only) | Basis for the surrogate-fidelity checks in §4.3 |
| Prichard & Theiler (1994). Generating surrogate data for time series with several simultaneously measured variables. *PRL* 73:951–954 | 10.1103/PhysRevLett.73.951 | Crossref ✔ (metadata only) | Multivariate surrogates that *keep* cross-correlation. This is the wrong null for a coupling test and is excluded |
| Small, Yu & Harrison (2001). Surrogate test for pseudoperiodic time series data. *PRL* 87:188101 | 10.1103/PhysRevLett.87.188101 | Crossref ✔ (metadata only) | Surrogates for (pseudo)periodic data, relevant to the oscillatory classes |
| Lancaster, Iatsenko, Pidde, Ticcinelli & Stefanovska (2018). Surrogate data for hypothesis testing of physical systems. *Physics Reports* 748:1–60 (CC-BY) | 10.1016/j.physrep.2018.06.001 | Crossref ✔; abstract ✔ (Semantic Scholar) | Review. Per the abstract, it compares surrogate types for nonlinearity, synchronisation, coherence, coupling strength and the nature of coupling |

### 2.2 Block and model-based resampling for dependent data

| ref | DOI | verified | relevance |
|---|---|---|---|
| Künsch (1989). The jackknife and the bootstrap for general stationary observations. *Ann. Statist.* 17:1217–1241 | 10.1214/aos/1176347265 | Crossref ✔; abstract ✔ | Moving-block bootstrap. Consistency needs block length l → ∞ with l/n → 0 (abstract) |
| Politis & Romano (1994). The stationary bootstrap. *JASA* 89:1303–1313 | 10.1080/01621459.1994.10476870 | Crossref ✔ (metadata only) | Random (geometric) block lengths; the resampled series is stationary |
| Politis & White (2004). Automatic block-length selection for the dependent bootstrap. *Econometric Reviews* 23:53–70 | 10.1081/ETC-120028836 | Crossref ✔ (metadata only) | Data-driven block length, tuned for the sample mean and not for lag-profile maxima |
| Patton, Politis & White (2009). Correction to "Automatic block-length selection…". *Econometric Reviews* 28:372–375 | 10.1080/07474930802459016 | Crossref ✔ | Must be cited together with Politis & White (2004) |
| Lahiri (2003). *Resampling Methods for Dependent Data*. Springer | 10.1007/978-1-4757-3803-2 | Crossref ✔ (metadata only) | Textbook reference for block methods |

### 2.3 Autocorrelation and cross-correlation significance

| ref | DOI | verified | relevance |
|---|---|---|---|
| Bartlett (1935). Some aspects of the time-correlation problem in regard to tests of significance. *JRSS* 98:536 | 10.2307/2342284 | Crossref ✔ (metadata only) | Classical result: autocorrelation inflates the variance of correlation estimates |
| Haugh (1976). Checking the independence of two covariance-stationary time series: a univariate residual cross-correlation approach. *JASA* 71:378–385 | 10.1080/01621459.1976.10480353 | Crossref ✔ (metadata only) | Prewhitening as an alternative to surrogates |
| Ebisuzaki (1997). A method to estimate the statistical significance of a correlation when the data are serially correlated. *J. Climate* 10:2147–2153 | 10.1175/1520-0442(1997)010<2147:AMTETS>2.0.CO;2 | Crossref ✔ (metadata only) | Phase-randomisation test for correlation under serial dependence |
| Pyper & Peterman (1998). Comparison of methods to account for autocorrelation in correlation analyses of fish data. *CJFAS* 55:2127–2140 | 10.1139/f98-104 | Crossref ✔ (metadata only) | A direct precedent for comparing the false-positive rates of autocorrelation corrections |
| Dean & Dunsmuir (2016). Dangers and uses of cross-correlation in analyzing time series in perception, performance, movement, and neuroscience. *Behav. Res. Methods* 48:783–802 | 10.3758/s13428-015-0611-2 | Crossref ✔; abstract ✔ (Europe PMC) | The abstract says cross-correlations of autocorrelated series "can indicate spurious relationships" and that aggregating pairs does not fix this |

### 2.4 Coupling and synchrony tests, recurrence-based surrogates, CRQA practice

| ref | DOI | verified | relevance |
|---|---|---|---|
| Andrzejak, Kraskov, Stögbauer, Mormann & Kreuz (2003). Bivariate surrogate techniques: necessity, strengths, and caveats. *PRE* 68:066202 | 10.1103/PhysRevE.68.066202 | Crossref ✔; abstract ✔ (Europe PMC) | Compares surrogate types for interdependence across eight stochastic and deterministic models and reports pitfalls. Closest methodological precedent |
| Thiel, Romano, Kurths, Rolfs & Kliegl (2006). Twin surrogates to test for complex synchronisation. *EPL* 75:535–541 | 10.1209/epl/i2006-10147-0 | Crossref ✔ (abstract withheld by publisher) | Recurrence-based surrogates that keep each system's dynamics |
| Thiel, Romano, Kurths, Rolfs & Kliegl (2008). Generating surrogates from recurrences. *Phil. Trans. R. Soc. A* 366:545–557 | 10.1098/rsta.2007.2109 | Crossref ✔ (metadata only) | Twin-surrogate construction |
| Romano, Thiel, Kurths, Mergenthaler & Engbert (2009). Hypothesis test for synchronization: twin surrogates revisited. *Chaos* 19:015108 | 10.1063/1.3072784 | Crossref ✔; abstract ✔ | Gives twin-surrogate parameter choice and compares twin surrogates with "natural" surrogates from independent trials (abstract). That is the oracle null in §3 |
| Hurtado, Rubchinsky & Sigvardt (2004). Statistical method for detection of phase-locking episodes in neural oscillations. *J. Neurophysiol.* 91:1883–1898 | 10.1152/jn.00853.2003 | Crossref ✔ (metadata only) | Phase-locking significance for oscillators. Whether it uses shift surrogates must be checked in the full text |
| Moulder, Boker, Ramseyer & Tschacher (2018). Determining synchrony between behavioral time series: an application of surrogate data generation for establishing falsifiable null-hypotheses. *Psychol. Methods* 23:757–773 | 10.1037/met0000172 | Crossref ✔; abstract ✔ (Europe PMC; open copy PMC6163103) | Reviews four surrogate methods for windowed cross-correlation synchrony. The abstract notes that common methods "will show some level of observed synchrony even when research participants have not interacted" |
| Boker, Rotondo, Xu & King (2002). Windowed cross-correlation and peak picking… *Psychol. Methods* 7:338–355 | 10.1037/1082-989X.7.3.338 | Crossref ✔ (metadata only) | Peak-picking on lag profiles, the analogue of the prominence peak |
| Bernieri, Reznick & Rosenthal (1988). Synchrony, pseudosynchrony, and dissynchrony. *JPSP* 54:243–253 | 10.1037/0022-3514.54.2.243 | Crossref ✔ (metadata only) | Pseudo-pair ("pseudosynchrony") baseline |
| Richardson & Dale (2005). Looking to understand… *Cognitive Science* 29:1045–1060 (q220 key `richardson2005looking`) | 10.1207/s15516709cog0000_29 | Crossref ✔ | Per Coco & Dale (2014), it used virtual pairs and shuffling as CRQA baselines |
| Coco & Dale (2014). Cross-recurrence quantification analysis of categorical and continuous time series: an R package. *Front. Psychol.* 5:510 (q220 key `coco2014cross`) | 10.3389/fpsyg.2014.00510 | Crossref ✔; content ✔ (publisher-page excerpt) | Says that for *categorical* series shuffling gives "approximately the same expected mean" as surrogate pairing. It calls the measures descriptive and suggests growth-curve modelling. q221 tests tails, not means |
| Wallot (2019; online 2018). Multidimensional cross-recurrence quantification analysis (MdCRQA). *Multivariate Behav. Res.* 54:173–191 (q220 key `wallot2018mdcrqa`) | 10.1080/00273171.2018.1512846 | Crossref ✔; content ✔ (publisher-page excerpt) | Calls shuffling a "liberal criterion" and false pairs "more conservative" for testing diagonal-profile values |
| Marwan, Romano, Thiel & Kurths (2007). Recurrence plots for the analysis of complex systems. *Physics Reports* 438:237–329 (q220 key `marwan2007recurrence`) | 10.1016/j.physrep.2006.11.001 | Crossref ✔ | Recurrence background |
| Runge et al. (2019) (q220 key `runge2019inferring`) | already verified in q220's bib (#841) | — | Common drivers and causal discovery from time series |
| **Lab precedent:** q203 / probe 307 uses circular-shift surrogates (50 shifts, minimum shift 50 samples, +1 correction) for TE/Granger/CCM | — | read in repo (`upstream/main:org_frontier/questions/q203_real_coordination_coupling/methods.md:24-25`; `probe_real_coordination_coupling.py:127-129`) | Reuse the pattern; Stage 1 must cite it |

### 2.5 Simulation-study design, calibration criteria, multiplicity

| ref | DOI | verified | relevance |
|---|---|---|---|
| Morris, White & Crowther (2019). Using simulation studies to evaluate statistical methods. *Stat. Med.* 38:2074–2102 | 10.1002/sim.8086 | Crossref ✔ (metadata only) | Simulation-study planning (aims, data-generating mechanisms, estimands, methods, performance measures) and Monte Carlo SE reporting |
| Bradley (1978). Robustness? *BJMSP* 31:144–152 | 10.1111/j.2044-8317.1978.tb00581.x | Crossref ✔ (metadata only) | Source usually cited for the "liberal" robustness band [0.5α, 1.5α]. Confirm the exact band in the full text |
| Phipson & Smyth (2010). Permutation p-values should never be zero. *SAGMB* 9(1) | 10.2202/1544-6115.1585 | Crossref ✔ (metadata only) | The (b+1)/(m+1) p-value for randomly drawn surrogates |
| Berger (1982). Multiparameter hypothesis testing and acceptance sampling. *Technometrics* 24:295–300 | 10.1080/00401706.1982.10487790 | Crossref ✔ (metadata only). *An earlier guessed DOI (…10487759) resolved to a different paper and was discarded.* | Intersection–union tests: "calibrated in every class" at level α without adjustment |
| Benjamini & Hochberg (1995). Controlling the false discovery rate. *JRSS-B* 57:289–300 | 10.1111/j.2517-6161.1995.tb02031.x | Crossref ✔ | Optional FDR for the descriptive per-cell tables |
| Cameron, Gelbach & Miller (2008). Bootstrap-based improvements for inference with clustered errors. *REStat* 90:414–427 (q220 key `cameron2008bootstrap`) | 10.1162/rest.90.3.414 | Crossref ✔ | Few-cluster inference, which q220's S2-H1 made concrete |

### 2.6 Not verified (do not cite until verified)

- **Holm (1979).** A simple sequentially rejective multiple test procedure. *Scand. J. Statist.* 6:65–70. It has no DOI. The JSTOR page (stable 4615733) returned 403 to WebFetch, and a Crossref bibliographic query did not return it. Plain Bonferroni needs no citation and can serve as a fallback.
- **Kulperger & Prakasa Rao (1989)**, finite-state Markov chain bootstrap. Not looked up. It would support the
  Markov-surrogate method; verify it or drop it.
- **Dale et al. (2011a)**, cited by Coco & Dale for "shuffling ≈ surrogate pairing for categorical series". Not looked
  up.
- **Shift-surrogate content** of Hurtado et al. (2004) and Lancaster et al. (2018) (time-shift surrogates for
  coupling). Only the metadata and abstract are verified.
- **Content claims about IAAFT, block-length conditions, twin-surrogate construction and Bradley's band** come from
  general knowledge and the titles. Stage 2 must confirm them against the full texts.

### 2.7 What the literature already settles (prospective statement of the gap)

**Settled.**
- Autocorrelation inflates cross-correlation significance (Bartlett 1935; Dean & Dunsmuir 2016).
- Surrogates that keep each channel's dynamics are the standard remedy: phase or IAAFT, block, shift, twin, and
  natural/virtual pairs (Theiler 1992; Schreiber & Schmitz 2000; Andrzejak 2003; Romano 2009; Lancaster 2018;
  Moulder 2018).
- For CRQA, shuffling is a liberal baseline (Wallot 2019).

**Apparently open** (to be confirmed or closed by Stage 2):
1. Calibration of *categorical* diagonal-profile tests whose statistic is a lag-invariant peak-minus-median.
2. Calibration of the *decoder pipeline* (floor → centrality → argmax bottleneck) against an exact-Φ structural
   ground truth.
3. Whether the q220 corpus-level "beats chance" inference stays calibrated when the only signal is marginal
   dynamics.

**Gate G-lit.** The study is not worth running as planned if Stage 2 finds item 1 already done for comparable
categorical recurrence statistics. In that case it should narrow to item 3, the pipeline-level calibration (H4 below).

---

## 3. Which nulls are valid for which generating process

### 3.1 Setup

**Hypotheses.** For a channel pair (a, b) the surrogate null is **H0: a and b are independent processes, each
stationary with its own dynamics.** All candidate nulls below are *univariate*: each channel is resampled separately,
which destroys cross-dependence. They differ in which within-channel properties they keep.

**Statistics.**
- *Pair statistic:* the q220 prominence of the clean profile, `observe.coupling(..., "timestamp")` on full series.
  This equals `crqa.dcrp` (`Q/stage2/observe.py:18-21`).
- *Form statistic:* the maximum prominence over pairs. A max statistic controls family-wise error within a form.
- *Decoder statistic:* the tie-aware BN score.

**A useful derivation (to be checked in Stage 2 and the pilot).**
- Write a_t = 2x_t − 1 and b_t = 2y_t − 1. The lag-k match indicator is m_t = (1 + a_t b_{t+k})/2.
- Under independence, Cov(m_t, m_s) = ¼[E(a_t a_s)·E(b_{t+k} b_{s+k'}) − E(a)²E(b)²]. This depends only on each
  channel's mean and autocovariance.
- So the null mean and covariance of the whole lag profile are **second-order** quantities. To a CLT approximation,
  the null law of prominence is fixed by the channels' marginal means and autocovariance functions.

**Consequences.**
- Any surrogate that matches each channel's mean and ACF over the relevant lags (≤ 2·MAX_LAG plus the correlation
  time) should be approximately valid for this statistic, even when its formal null model (a Gaussian process for
  IAAFT) is wrong.
- The shuffle matches the mean but sets the ACF to zero. It is invalid whenever any channel is autocorrelated.
- The approximation is weakest for short series, strong persistence, or near-deterministic cycles. The pilot
  measures this directly.

### 3.2 Generating-process classes (all Boolean networks with flip noise, so the existing `crqa.trajectory` applies)

| class | construction | structural truth |
|---|---|---|
| **N0 iid** | any rules with flip = 0.5 → iid fair coins | no coupling |
| **N1 persistent** | x_i' = x_i, flip ε ∈ {0.02, 0.08} → binary symmetric Markov chain, ρ(k) = (1−2ε)^k (correlation time ≈ 24 / 6 steps) | no coupling |
| **N2 oscillatory** | x_i' = ¬x_i, flip ε ∈ {0.02, 0.08} → ρ(k) = (−(1−2ε))^k, noisy period 2 | no coupling |
| **N3 heterogeneous** | mixed N0/N1/N2 nodes in one system | no coupling; the adversarial decoy for BN |
| **N4 replicate composite** | take a coupled dev or held-out form f and build a null system whose channel j comes from an *independent* run r_j of f | no coupling, but each channel has **exactly** f's marginal dynamics; decoy B = f's true Φ bottleneck |
| **C1 common driver** | D' ∈ {D, ¬D}; X' = D, Y' = D (optionally X, Y with their own noise) | X–Y dependent, with no direct X–Y edge |
| **P1 known coupled** | chains or the q161 control triad (W–S–C, mediator S) at several flip levels | known edges; Φ bottleneck from `bottleneck_set` |
| **P2 periodic coupled** | X' = ¬X, Y' = X at ε ∈ {0.02, 0.08} | coupled, with near-periodic channels |
| **R-dev / R-hold** | `random_wiring` forms from new RNG streams, selected blind to CRQA with q220's R2 rules | Φ bottleneck |

### 3.3 Validity table

Key: ✔ valid; ≈ approximately valid if the stated condition holds; ✗ invalid (anti-conservative). Power notes are
for the coupled classes.

| null | what it keeps | N0 | N1 | N2 | N3 | N4 | C1 | power notes (P1/P2/R) | reason |
|---|---|---|---|---|---|---|---|---|---|
| **Shuffle** (q220) | marginal only | ✔ | ✗ | ✗ | ✗ | ✗ to the degree channels are autocorrelated | rejects (correct for H0, but not evidence of a direct edge) | inflated "power" | Exchangeability holds only for iid channels. With ρ ≠ 0 the profile variance is inflated by Σρ_aρ_b, and N2 adds lag-alternating structure that shuffling removes |
| **Circular shift** (each channel by an independent offset s ∈ [w, T−w], w ≥ MAX_LAG + correlation time; q203 used w = 50) | everything within each channel except one wrap junction | ✔ | ✔ | ✔ | ✔ | ≈ (stationarity) | rejects | **P2 at small ε: power ≈ 0.** | Under H0 it is exact up to the junction and stationarity. Under periodic coupling with coherence time ≳ T and period ≤ 2·MAX_LAG+1, a shifted pair keeps a prominent peak at a shifted lag. Prominence ignores peak location, so the surrogate looks as coupled as the data. This is the "circular shifts can preserve periodic coupling" concern, made precise: it is a **power** failure, not a false-positive failure. It goes away when phase diffusion (≈ 1/(2ε) steps) is much shorter than w |
| **Block bootstrap** (stationary or circular, mean block L, per channel) | dependence within blocks | ✔ | ≈ if L ≫ correlation time and L ≫ MAX_LAG | ≈ same, and junctions also reset phase | ≈ | ≈ | rejects | power falls as L grows (fewer distinct surrogates) | Each junction removes dependence at lags that cross it. With L comparable to the correlation time the surrogate ACF shrinks, so the test is **anti-conservative**. Block length is a design factor: L ∈ {5, 20, 50, 100}. Politis–White automatic L targets the sample mean, so it is reported but not trusted |
| **Markov order-p** (fit per-channel context counts, p ≤ 6 by BIC, simulate independently) | ACF and higher-order dependence up to order p | ✔ | ✔ (correct model) | ✔ | ✔ | ≈ (a channel is a hidden-Markov projection, so finite order is only an approximation) | rejects | as circular for P2 | Exact for N0–N3 and approximate for network nodes. Plug-in parameters make it slightly anti-conservative at T = 600. Fidelity check: ACF to lag 20 and run-length distribution |
| **IAAFT** (per channel, binary values remapped by rank) | exact counts, approximate spectrum | ✔ | ≈ | ≈ (end-point and periodicity issues) | ≈ | ≈ | rejects | — | Its formal null (Gaussian linear process through a monotone transform) does not hold for binary Markov channels. By §3.1 it may still be valid for this second-order statistic, *if* the spectrum is matched. Two-valued data make IAAFT converge coarsely, so it is kept only if it passes the fidelity check |
| **Twin surrogates** (embedding m) | recurrence structure | ≈ | ≈ | ≈ | ≈ | ≈ | rejects | — | For exact-match categorical recurrence with embedding m, twins are time points with identical m-histories. The surrogate is then close to an order-m empirical Markov resample. *Analytic observation, to be checked against Thiel et al. 2006/2008 in Stage 2.* If it holds, twins are folded into the Markov method rather than run separately |
| **Oracle: independent-run composite** (simulation only) | each channel's exact marginal law, including non-stationary transients | ✔ (exact) | ✔ | ✔ | ✔ | ✔ | rejects | reference power | This is the natural or virtual-pair surrogate (Romano 2009; Bernieri 1988). An analyst with one recording cannot use it, but in simulation it is exact and defines the **matched chance baseline** for BN |

**Common driver (C1).** Every null above tests independence, and X and Y are dependent, so rejection is the correct
answer to H0. A rejection is still not evidence of a direct X–Y edge. C1 therefore reports an "indirect-dependence
rejection rate" and is excluded from the false-positive rate. A conditional surrogate (resampling given D) would be
needed for a direct-edge null. It is out of scope; Runge et al. 2019 is the reference.

**Mapping to Hassan's null candidates.**
- Circular shifts are valid for false positives in every null class. Their power fails only for coherent periodic
  coupling.
- Block surrogates are valid only above a class-specific L. The pilot estimates that L.
- Model-based (Markov) surrogates are exact for N0–N3 and approximate for network channels.
- IAAFT is conditional on spectral fidelity with binary values.
- AR in the continuous sense does not apply to binary series. Its binary analogue is the Markov-p method.

---

## 4. Minimal feasibility pilot (design only; not run)

### 4.1 Purpose

The pilot answers six questions before anything is preregistered:
1. Is the shuffle null measurably anti-conservative for the q220 statistic?
2. Is at least one temporal null calibrated in every null class?
3. Is there usable power?
4. How large are the variance components?
5. What does the full study cost?
6. Which methods and classes can be dropped?

The pilot uses **development forms and seeds only**. Its data are never reused in confirmatory analyses.

### 4.2 Design

**Classes.**
- Null: N0; N1 at ε 0.02 and 0.08; N2 at ε 0.02 and 0.08; N3; N4 built from R-dev forms.
- Coupled: P1 at three flip levels; P2 at two ε; C1.
- R-dev random forms, n = 3–4.
- **The q161 curated forms (q220's R1) are excluded from the pilot.** They generated q220's hypotheses. Using them
  again invites a de facto S2-H1 rescue (see §8).

**Size.** 15 forms per class × 10 seeds (n = 3–5 nodes, T = 600, warm-up 20, as in q220).

**Methods.**
- oracle composite
- shuffle (reference)
- circular shift (w = 50)
- stationary bootstrap at L ∈ {5, 20, 50}
- Markov-p (BIC, p ≤ 6)
- IAAFT-binary

That is 8 methods. Twin surrogates are covered analytically (§3.3).

**Surrogates per run.** 99, giving p = (b+1)/(99+1) (Phipson & Smyth 2010).

**Lag windows.** One ±20 profile per series. The windows MAX_LAG ∈ {5, 10, 20} are read from that one profile, so
the three windows cost one computation.

**Outcomes.**
- (i) Rejection rate of the form max-prominence test at α = 0.05 per class × method × window, which is the
  false-positive rate on N0–N4.
- (ii) The legacy `PROM_FLOOR = 0.05` "any evidence" rate, as a reference.
- (iii) Pair-level detection rate on true edges in P1, P2 and R-dev.
- (iv) Tie-aware BN gain over each matched baseline, where baseline = mean BN score over that method's surrogates
  (on N4 with decoy B, and on R-dev).
- (v) Surrogate fidelity: maximum absolute ACF error over lags 1–20, marginal mean, and run-length distribution.

### 4.3 Steps

**Step 0, instrument.**
- `q161.control()` must pass (the faithful W–S–C triad: Φ = 2.0, mediator picked; q161 probe
  `control()`).
- A q221 harness must reproduce exactly the committed q220 CLEAN and NULL-CLEAN `bn_score` rows for two R1 seeds,
  using q220's own functions with the same seeds. This is a read-only equivalence check against
  `Q/stage2/results/stage2_runs.csv.gz`, in the spirit of q220's S0 check.
- Per-call timing of `observe.coupling` is measured.
- If a vectorised clean-profile function is written for speed, it must match `observe.coupling` exactly before use.

**Step 1, fidelity.** No CRQA is involved. Every method is applied to every null and coupled class and the fidelity
metrics are reported. A method whose mean ACF error exceeds 0.05 at lags ≤ 2·MAX_LAG in a class is flagged
"unfaithful" there.

**Step 2, calibration** on N0–N4.

**Step 3, power and BN** on P1, P2, C1 and R-dev.

**Step 4, variance and compute.** ICC of the per-form rejection rates, measured cost per run, and the projected full
size.

### 4.4 Reuse of q220 and lab code (read-only imports; nothing edited)

- `org_frontier.recurrence.crqa.trajectory` for all classes. N0–N3, P1, P2 and C1 are rule lists, so no new
  generator is needed except where per-node flip rates are wanted. That would be a new `generators.py` in q221.
- `q220 …stage2.observe`: `coupling`, `peak_prominence`, `centrality`, `bottleneck_scores`.
- `q220 …stage2.stats`: `cluster_boot`, `sign_test`, `icc_share`.
- `q220 …stage2.decision`: the three-way rules as a pattern. q221 would add calibration rules in its own
  `decision.py`.
- `q220 …corruptions.shuffle_null`, used as the reference null.
- `q161 …`: `bottleneck_set`, `core_indices`, `control`.
- `q162 …random_wiring`, plus q220's `forms_r2.select_r2` selection *pattern* (copied with new seeds; the original is
  not modified).
- The q203 circular-shift pattern (`_surrogate_p`).
- **New code in q221 only:** `surrogates.py` (circular, block, Markov-p, IAAFT-binary, oracle composite) with unit
  tests: each surrogate keeps what it claims; under the oracle the p-values are uniform on N0.
- **Seeds disjoint from q220.** q220 used 0–19, 1000–1019, 2000–2019, 9000+, 10 000+, 20 000+, 30 000+ and rng
  220. Proposal for q221:
  - pilot trajectories 40 000+;
  - confirmatory trajectories 50 000+;
  - surrogate streams 60 000+;
  - form-selection streams `default_rng(22101)` (dev) and `default_rng(22102)` (held-out).
- **Per-form seed streams** (seed = hash(form id, replicate)) avoid q220's crossed seed design (review S11).

### 4.5 Compute estimate on this box (8 cores, 15 GiB RAM; shared via `box-run`)

**Cost per coupling call.** q220 stage 2 did 55,680 coupling evaluations in 120.7 s wall with 4 workers, including
form selection, trajectories and analysis (`postmerge-logs/06_reproduce_q220.log`; `stage2_stdout.txt:4`). That
bounds the cost at **≈ 8.7 CPU-ms per call** (n ≤ 5, ±10 lags). For ±20 lags assume ≈ 17 ms. *Step 0 replaces this
estimate with a measured value.*

**Pilot.**
- Runs: 12 class cells × 15 forms × 10 seeds ≈ 1,800 runs.
- Calls: 1,800 × 8 methods × 100 profiles ≈ 1.44 M calls.
- Time: ≈ 6.8 CPU-h at 17 ms, ≈ 1.7 h wall on 4 workers. A vectorised clean profile would probably cut this
  several-fold; it is untested.
- Exact Φ for R-dev and P1 bottlenecks: n ≤ 4 is seconds per form (q220's 30-form R2 selection fit inside its
  2-minute run); n = 5 is unmeasured.
- Memory: under 1 GB per worker.
- Run it as `box-run --class test --mem 3000 --timeout 14400 -- python -m …probe_pilot`, the same queue used for
  #841's reproduce run.

**Full study (projected, pilot-dependent).**
- Runs: 9 classes × 70 forms × 20 seeds ≈ 12,600 runs.
- Calls: 12,600 × 6 surviving methods × 200 profiles ≈ 15 M calls.
- Time: ≈ 71 CPU-h with the current code (≈ 18 h wall on 4 workers), or a few hours with a verified vectorised
  profile.
- The pipeline-level H4 simulation adds 200 replicate corpora × 12 forms × 20 seeds × (1 clean + 6 single-draw
  baselines) ≈ 0.34 M calls ≈ 1.6 CPU-h.
- **Feasible on this box only if the vectorised profile passes Step 0**, or if the methods are cut to 3–4 after the
  pilot.

### 4.6 Go/no-go criteria (to be committed before the pilot runs)

| gate | GO if | otherwise |
|---|---|---|
| G0 instrument | q161 control passes; exact reproduction of the committed q220 rows; any fast path equals `observe.coupling` exactly | stop and fix; no numbers reported |
| G-lit (before the pilot) | Stage 2 finds the item-1 gap in §2.7 still open | narrow to H4 (pipeline calibration) or stop |
| G1 the problem exists | shuffle FPR point ≥ 0.10 in at least one of N1, N2 or N4 at MAX_LAG = 10 | **NO-GO.** The shuffle is not materially miscalibrated for this statistic. Write a short pilot note that closes q220's "anti-conservative?" open item (`Q/FINDINGS.md:293-294`) |
| G2 a valid null exists | ≥ 1 temporal method has point FPR in [0.025, 0.075] in **every** null class N0–N4 at MAX_LAG = 10 and passes fidelity | NO-GO, or redesign the statistic, e.g. a lag-location-aware statistic |
| G3 usable power | that method reaches ≥ 0.5 pair-level detection on P1 at the middle flip level. BN gain point estimate ≥ 0.05 on R-dev is needed to keep BN identification confirmatory | if pair-level power is fine but BN gain < 0.05, GO with BN identification **demoted to descriptive** in the prereg. If pair-level power < 0.5, NO-GO for power claims and report calibration only |
| G4 feasibility | the projected full study is ≤ 24 h wall under `box-run`, ≤ 4 workers, ≤ 3 GB, and the ICC-based size is ≤ 100 forms per class | cut methods or classes before preregistering |
| G5 information value | the temporal nulls are **not** all equivalent to the oracle and to one another in every class, *or* H4 shows a gap between the uniform/shuffle baselines and the calibrated ones | if everything except the shuffle is calibrated and equivalent, and the baselines agree, the pilot note is the deliverable; no full study |

---

## 5. Draft preregistration skeleton (for `PREREGISTRATION.md`; to be finalised after the pilot)

**Units.**
- The unit is the **independently generated form**, meaning a generating system.
- (form, seed) runs are replicates within the unit.
- Confirmatory forms come from `default_rng(22102)`, selected blind to CRQA.
- Truth tables are de-duplicated against the q161 corpus, q220's R2 and the q221 dev forms.
- The q161 curated forms are excluded from every confirmatory test.

**Held-out structure.**
- Dev forms and seeds (pilot) are never used in confirmatory analysis.
- Held-out forms are split per class into a *confirmatory* set and a *replication* set, about 50/50, by a
  preregistered hash.
- Every confirmatory verdict must hold on the confirmatory set. The replication set is reported separately; it
  either replicates or is flagged.

**Fixed decoder.** The q220 decoders are unchanged: `PROM_FLOOR = 0.05`, tie-aware score, timestamp-mode clean
profile. MAX_LAG ∈ {5, 10, 20}, with 10 primary.

**Surrogates.** 199 per run (999 for the primary cells if compute allows). p = (b+1)/(B+1). α = 0.05.

### Hypotheses (five, per protocol; each with its H0 and a predicted outcome)

**H1, shuffle miscalibration (primary).**
- Claim: on N1, N2 and N4 the shuffle-null max-prominence test has FPR > 0.075.
- H0: FPR within [0.025, 0.075].
- Predicted: ANTI-CONSERVATIVE on N1 and N2 at both ε, and on N4 for the R-hold forms with autocorrelated channels.

**H2, temporal-null calibration (primary).**
- Claim: method M has FPR ≤ 0.075 in every null class (N0–N4) × MAX_LAG cell.
- Methods: oracle, circular, Markov-p, and those of block-L and IAAFT that pass the pilot.
- H0: FPR > 0.075 in at least one cell.
- Predicted: circular, Markov-p and oracle are CALIBRATED. Block bootstrap is calibrated only for L ≥ L* (pilot
  value). IAAFT depends on fidelity.

**H3, power (secondary).**
- Claim (a): for each method calibrated under H2, pair-level detection of true edges on P1 at the reference flip is
  ≥ 0.8.
- Claim (b): on P2 at ε = 0.02, every calibrated method has power ≤ 0.2. This is the identifiability limit of the
  lag-invariant prominence statistic, predicted in advance and reported as a limit.
- H0 for (a): power < 0.8.

**H4, pipeline calibration (secondary, key).**
- Construction: 200 replicate corpora of 12 N4 composite forms (decoy B = the true Φ bottleneck of the source form),
  20 seeds each.
- Procedure: the q220 inference is applied as preregistered there: per-run CLEAN − baseline, two-stage percentile
  bootstrap with 2,000 resamples, `decision.positive`.
- Claim: with the oracle or an H2-calibrated baseline, the false-CONFIRMED rate is ≤ 0.05 (upper 95% bound ≤ 0.075).
- Recorded alongside: the rate with the uniform \|B\|/n and shuffle baselines.
- H0: rate > 0.075.
- Predicted: calibrated for oracle, circular and Markov-p. Uniform and shuffle above nominal *if* the marginal-driven
  pull in F6 generalises; otherwise also calibrated.
- Either outcome is informative about q220's S2-H7a/H7b, but q221 does **not** re-score q220.

**H5, bottleneck identification beyond a matched temporal null (secondary).**
- Claim: on held-out R forms, tie-aware BN score − matched calibrated-null baseline > 0 (lower bound > 0).
- H0: gain ≤ 0.
- Predicted: INCONCLUSIVE or a small positive gain, given R2's +0.136 [−0.001, +0.272] against uniform chance (F2).
- This hypothesis is demoted to descriptive if pilot gate G3 says so.

### Calibration and power criteria

**Rejection-rate estimand.** The mean over forms of each form's rejection rate across seeds.

**Intervals.**
- (i) The two-stage form-then-seed percentile bootstrap (`stats.cluster_boot`, 20,000 resamples).
- (ii) A t interval on form means.
- **A verdict is issued only if both intervals agree.** This is the lesson from q220's S2-H1 (review S2).
- The Monte Carlo SE of each rate is reported (Morris et al. 2019).

**Three-way verdict per cell** (in the style of `decision.py`):
- CALIBRATED if the upper bound ≤ 0.075.
- ANTI-CONSERVATIVE if the lower bound > 0.075.
- CONSERVATIVE flag if the upper bound < 0.025 (still valid, but costs power).
- Otherwise INCONCLUSIVE.

**Power verdict.** ADEQUATE if the lower bound ≥ 0.8; INADEQUATE if the upper bound < 0.8.

**Precision target.** The upper bound must fall within 0.025 of the point estimate at the Holm-adjusted level. With
FPR ≈ 0.05 and z ≈ 2.6 that needs n_eff ≈ 500 runs per cell. With deff = 1 + 19·ICC, the number of forms per class is
set from the pilot ICC (e.g. ICC 0.05 → deff 1.95 → 1,000 runs → 50 forms × 20 seeds).

### Multiplicity

**Primary family {H1, H2}.**
- Within a method, H2 is an intersection–union test across classes × windows (Berger 1982). Every cell must pass at
  level α, so no within-method adjustment is needed.
- Across methods, and between H1 and H2, Holm at FWER 0.05. *Holm's citation is unverified (§2.6); if it stays
  unverified, use Bonferroni.*

**Secondary family {H3, H4, H5}.**
- Gatekept: tested only for methods declared CALIBRATED in the primary family.
- Holm within the family.
- The descriptive per-cell tables (all ε, L and window values) carry no verdicts. Optionally they get
  Benjamini–Hochberg q-values.

### Exclusions, deviations and outputs

- As in q220: no run-level exclusions. Failures are recorded.
- One confirmatory run. Bugs go into `DEVIATIONS.md` with both sets of numbers kept.
- Outputs: per-run CSV (gzip, SHA-256 printed), per-cell summary and per-form tables, all registered in
  `ci/reproduce.json`.
- PROBES rows start at 464.

### Stage-1 review content (for `review.md`)

**Prior work to cite.**
- q161: robust bottleneck pick under model noise.
- q162: random-wiring forms and whole-system recurrence.
- q203 / probe 307: circular-shift surrogates on real dyads.
- q220 / probe 463: per-channel shuffle null; F1–F10.
- The recurrence arm (`org_frontier/recurrence/`).

**Gap sentence.** No lab study has tested whether the CRQA→Φ decoder's chance baselines are calibrated when the
null keeps temporal dependence.

---

## 6. Risks, and what would make the study not worth running

**Risks.**
1. **The statistic, not the null, is the limit.** Prominence ignores the lag location, so coherent periodic coupling
   cannot be identified with *any* dynamics-preserving null (§3.3, P2). This is a known limit to report, not a
   failure to fix.
2. **A predictable answer.** The second-order argument (§3.1) predicts that every ACF-matching null behaves alike. If
   the pilot confirms that, the full study adds little beyond the pilot (gate G5).
3. **Weak bottleneck signal on random forms** (F2). H5 and the BN part of H3 may be underpowered whatever the null.
   Gate G3 demotes them instead of running them underpowered.
4. **Ground truth depends on a definition.** The Φ bottleneck uses clamp-to-0 leave-one-out (review `STATS_AUDIT.md:96-98`). H4 and H5 inherit that choice.
5. **Few-cluster and Monte Carlo fragility** (q220 S2, S12). Mitigations: many forms, two interval methods,
   20,000+ resamples, and reported Monte Carlo SE.
6. **Non-stationarity.** Slow-mixing forms may still carry transients after 20 warm-up steps. That affects circular
   shifts (wrap junction) and Markov fits. Mitigation: a warm-up-200 sensitivity check and the oracle composite as the
   reference.
7. **Combinatorial scope.** 8 methods × 12 cells × 3 windows invites forking paths. The pilot must prune before the
   prereg, and descriptive cells carry no verdicts.
8. **Compute.** The current per-pair index code is slow (§4.5). A vectorised path must be proven identical first.
9. **Scope creep toward q220.** Using the R1 curated forms, or reporting "S2-H7 survives a temporal null" as a
   q221 result, would turn calibration into a rescue. Mitigations: R1 is excluded, and q220 is linked only in
   Discussion.
10. **Protocol deviation.** A pilot before Stage 3 is not in `RESEARCH_PROTOCOL.md`. It needs maintainer approval,
    or it must be relabelled as a Stage-4 methods check on dev data.
11. **External validity.** The setting is binary synchronous Boolean networks only. The validation gap must be stated
    (`RESEARCH_PROTOCOL.md:85-88`).

**Not worth running (any one suffices):**
- (a) Stage 2 shows that categorical lag-profile tests have already been calibrated against dynamics-preserving
  nulls in a comparable setting, and H4 alone does not interest the maintainers.
- (b) G1 fails: the shuffle is not anti-conservative for this statistic. A short note closes the q220 open item.
- (c) G5 fails: all temporal nulls are equivalent and calibrated, and the H4 baselines agree. A note suffices.
- (d) G2 fails and no statistic redesign is wanted.
- (e) The maintainers deprioritise the CRQA→Φ decoder. q220 already shows that the clean decoder is near chance on
  random forms.
- (f) G4 fails even after pruning.

---

## 7. Honest novelty assessment

- **The methods are established.** Shuffle, phase/IAAFT, block bootstrap, circular shift, twin and natural/virtual-pair
  surrogates all come from the literature. So do the results that autocorrelation inflates cross-correlation
  significance and that shuffling is a liberal CRQA baseline (§2.1–2.4; Wallot 2019 says so explicitly). q221
  invents no surrogate and should claim none.
- **Shuffle anti-conservativeness is not a finding.** H1 confirming it would be a *replication* of known behaviour
  in a new setting.
- **Where a genuine contribution could lie** (all modest, and to be confirmed as open by Stage 2):
  1. *Tail calibration for categorical CRQA.* Coco & Dale (2014) note that shuffling and pairing agree in
     *expected mean* for categorical series. q221 would measure whether they agree in the *tails* that a test uses,
     for the peak-minus-median statistic, with exact ground truth. This is a small, citable methods point for CRQA
     users.
  2. *Pipeline-level calibration against exact Φ* (H4). This asks whether a corpus-level "the decoder beats chance"
     inference stays calibrated when only marginal dynamics carry signal. The replicate-composite construction
     isolates marginal-driven agreement (F6) from coupling-driven agreement. The design is standard Monte Carlo
     practice. The application to an exact-Φ structural target appears new *within the lab's framing*, and its main
     value is internal: it decides whether the lab's CRQA→structure baselines (q161, q220 S2-H7, the recurrence arm)
     are trustworthy.
  3. *A stated identifiability limit.* Lag-invariant prominence cannot detect coherent periodic coupling against any
     dynamics-preserving null. This is probably known in the synchronisation literature (phase-locking statistics
     exist for this reason) and must be checked before any claim is made.
- **Expected publishable weight: low outside the lab.** Inside the lab the value is real: a calibrated threshold or
  p-value could replace the fixed `PROM_FLOOR`, and the chance baselines used in CRQA→Φ claims would get a valid
  reference. The honest framing is "a calibration study of the lab's own instrument". It is not a new method. It is
  not a test of q220's S2-H1, which F3b suggests it would barely touch anyway.

---

## 8. Open questions for Hassan

1. **Pilot before hypotheses.** Is a dev-data pilot before Stage 3 acceptable to Roger, or should it be framed as a
   Stage-4 methods check? (Protocol deviation, §0 and §6.10.)
2. **R1 curated forms.** Exclude them entirely (recommended), or allow a labelled descriptive appendix *after* the
   confirmatory run?
3. **Scope of BN identification (H5).** Keep it confirmatory only if G3 passes (recommended), or make it
   descriptive from the start given F2?
4. **Primary statistic.** Max-over-pairs prominence (form level, recommended) or per-pair tests with within-form
   multiplicity? Should a lag-location-aware statistic be considered if G2 fails?
5. **Calibration band.** Bradley's liberal [0.025, 0.075] at α = 0.05 (recommended), or a stricter
   non-inferiority margin such as 0.065?
6. **Common driver.** Is "indirect-dependence rejection rate" acceptable as the C1 outcome, or should a hidden-driver
   variant be added? Its Φ ground truth under marginalisation is not defined by q161's method.
7. **Compute.** Approve writing a vectorised clean-profile function (must equal `observe.coupling` exactly), or keep
   the q220 code path and accept roughly 18 h of wall time for the full study?
8. **Multiplicity citation.** Use Holm, which needs a verified source (§2.6), or Bonferroni?
