# q221 novelty assessment (gate 4), anchored on the lab's recurrence review

**Anchor.** `org_frontier/research/recurrence/REVIEW.md` on `main`. That review assembled its sources on
2026-06-23 and kept only works whose DOI or arXiv id was confirmed. Its DOIs are taken from
`org_frontier/research/recurrence/literature/references.bib`. Where this note relies on a specific *claim*
inside a source, the verification level is stated:
- **F**: full text checked;
- **A**: abstract checked;
- **S**: search snippet only;
- **R**: as summarised by the lab review.

## 1. What the lab review already establishes, and where Q221 sits relative to it

| work (DOI) | what it establishes (per REVIEW.md) | relation to Q221 |
|---|---|---|
| Marwan, Romano, Thiel & Kurths 2007, Phys. Rep. 438:237 (10.1016/j.physrep.2006.11.001) | The canonical synthesis of recurrence plots and RQA/CRQA: embedding, thresholds, quantifiers (R) | q220's statistic is a categorical, lagged cross-match profile, a special case of a diagonal-wise cross-recurrence rate. Q221 does not propose a new quantifier. |
| Marwan 2011, IJBC 21:1003 (10.1142/S0218127411029008) | Pitfalls: embedding, threshold sensitivity, tangential motion (R) | Q221's limit is not a parameter pitfall. It holds at the population level, for every lag and threshold, so it is a property of the *representation*. |
| Coco & Dale 2014, Front. Psychol. 5:510 (10.3389/fpsyg.2014.00510); Coco et al. 2021, R Journal (10.32614/RJ-2021-062) | The `crqa` toolchain for categorical and continuous CRQA, including windowed and piecewise measures (R) | These are the tools for exactly the categorical pairwise statistic whose information content Q221 bounds. |
| Wallot & Leonardi 2018, Front. Psychol. 9:2232 (10.3389/fpsyg.2018.02232) | The CRQA/DCRP tutorial. DCRP lag profiles describe lead and lag. Shuffled baselines; block shuffles for categorical data (F) | q220's profile is a DCRP-type object. The review states that DCRP peaks are *descriptive, not causal*. Q221 makes a sharper, exact point: a full set of such profiles (all pairs, all lags, plus auto-profiles) need not determine the multivariate transition law. |
| Wallot 2019, Multivariate Behav. Res. (10.1080/00273171.2018.1512846) (MdCRQA); Wallot & Mønster 2023 (10.48550/arXiv.2303.16907) (MvJRQA) | Multidimensional and joint recurrence across several series (R) | These methods recur on **joint** multichannel states, so in principle they carry more than pairwise information. Q221 did **not** test whether MdCRQA or joint recurrence separates the survivors. That is an open item. |
| Schreiber 2000, PRL 85:461 (10.1103/PhysRevLett.85.461) | Transfer entropy, which conditions on the target's own history (R) | TE is a multi-point statistic, outside the pairwise representation Q221 studies. Bivariate TE was not computed on the survivors. The transition-count baseline (gate 3), which separates them perfectly, is in TE's spirit. |
| Sugihara et al. 2012, Science 338:496 (10.1126/science.1227079) | CCM: state-space reconstruction to separate causation from correlation (R) | Not computed on the survivors. Q221 makes no claim about CCM. |
| Edinburgh, Eglen & Ercole 2021, Chaos (10.1063/5.0053519) | A benchmark of ten bivariate causality indices; recommends TE and nonlinear Granger (R) | Q221 runs no causality benchmark. Its contribution is orthogonal: an exact limit of one representation, not a ranking of indices. |

## 2. Dependence-aware testing (from `LITERATURE_REGISTER_DRAFT.md` and `independent_audit/ADVERSARIAL_GO_NO_GO.md`)

These works are prior art for the calibration track:
- Theiler et al. 1992 (10.1016/0167-2789(92)90102-S);
- Schreiber & Schmitz 1996/2000;
- Künsch 1989 and Politis & Romano 1994;
- Phipson & Smyth 2010 (F);
- Yuan & Shou 2022, eLife (10.7554/eLife.72518; F): shuffle FPR of 30–92% for independent autocorrelated series;
- Yuan & Shou 2024, PLOS Biol (10.1371/journal.pbio.3002758; F): circular shift, IAAFT, block bootstrap and
  twin surrogates can each exceed 5%;
- Romano & Tirlea 2022 (10.1111/jtsa.12638; A): serial dependence of a single series.

**Q221's pilot adds nothing new here.** It is Hassan's zero-lag Pearson pilot on independent binary Markov
channels. It re-shows a known result and is kept only as a methods check. No calibration claim for CRQA or for
the q220 decoder is made.

## 3. Higher-order and integrated-information prior art (outside the lab review)

- Williams & Beer 2010 (arXiv:1004.2515; F): XOR as pure synergy.
- James & Crutchfield 2017, Entropy 19:531 (10.3390/e19100531; A): dyadic vs polyadic distributions that are
  indistinguishable in Shannon terms.
- arXiv:2205.04440 (authors not verified; S): model-free higher-order interactions distinguish Boolean dynamics that
  correlations and mutual information cannot.
- Gilpin 2025, PRX 15:011005 (F): shared recurrences recover multiplicative drivers that pairwise inference
  misses. The paper also notes that drivers with equivalent influence are not identifiable without
  intervention.

**So "pairwise statistics miss higher-order structure" is classical.**

On integrated information, Barrett & Seth 2011, PLoS Comput. Biol. 7:e1001052 (10.1371/journal.pcbi.1001052; A)
define empirical, time-series Φ measures, so Φ-like quantities *from observational data* exist. Q221's target
is different: the lab's q161 leave-one-out bottleneck set under IIT 4.0 (Albantakis et al. 2023), computed
perturbationally on the deterministic TPM.

A targeted web search (2026-10-15) found **no** prior work on whether IIT-4.0 major-complex or
leave-one-out bottleneck targets are identifiable from recurrence summaries. That search was cursory, and the
absence of a hit is not proof that no such work exists.

## 4. What Q221 adds, stated precisely

**Beyond the lab review and dependence-aware testing, Q221 adds two things.** Both are exploratory and not
yet validated.

1. **An exact representation limit inside the lab's own generator family.**
   - The family is q220's deterministic rule plus 8% flip, with three nodes, `nsi` and GF(2)-affine forms.
   - It contains non-isomorphic systems (3 classes up to node permutation × value relabelling) whose
     marginals, self-recurrence profiles and cross-recurrence profiles are equal *in population* at every lag.
     Equality is proved by exact rational arithmetic plus a linear-recurrence argument.
   - Their transition laws are different, and finite data separate them at once by transition counts
     (gate 3: accuracy 1.000).
   - **Consequence:** pairwise population recurrence summaries, which is the representation behind the
     DCRP-style profiles in the review's toolchain, may not identify the full multivariate transition law.
2. **A consequence for the lab's structural target.** In the lead pair, the q161 leave-one-out bottleneck set
   differs ({X,H} vs {H}). Major complex, Φ and per-state φ are identical, and the difference enters through
   a node *outside* the major complex. So any method restricted to that representation cannot recover this
   target uniformly across the family.

**Not added:**
- a new recurrence quantifier;
- a new surrogate or null;
- a calibration result for CRQA or q220;
- a finite-sample indistinguishability result;
- evidence that q220 fails on its own corpus;
- an IIT theorem.

## 5. Open items for this gate

- Test MdCRQA / joint recurrence, bivariate TE and CCM on the 3 survivors. Joint-state recurrence is the most
  likely competitor that would already resolve them.
- Run a proper database search (Crossref, OpenAlex, Semantic Scholar) for identifiability of IIT or
  perturbational targets from observational statistics.
- Upgrade the claims checked only at levels M, S or R to full-text verification.
