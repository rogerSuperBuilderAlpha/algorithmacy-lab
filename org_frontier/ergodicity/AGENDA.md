# Ergodicity × Algorithmacy — research agenda

Forty questions in ten strands. Each entry states the question, why it matters
for algorithmacy, a candidate method, and what would support or falsify it.
Questions marked **computable now** can run on existing lab code (classifier,
corpus, `studies/genuine_bistability/`, PyPhi exact IIT-4.0) without new
instrumentation. Status tags on computable questions: **run** (FINDINGS
landed), **open** (not yet run).

Source framing: Connaughton, Jeroen, and Paillusson (2026 working notes) on
ergodicity for the Phil. Trans. R. Soc. A theme issue; the lab thesis that
dyadic forms (Φ_MIP = 0) demand literacy and triadic forms (Φ_MIP > 0) demand
algorithmacy. See [`SOURCES.md`](SOURCES.md).

---

## Strand A — Text vs platform as a formal distinction

**A1.** Is loss of skew-product structure a formal criterion separating
text-like environments (literacy suffices) from platform-like environments
(algorithmacy required)?

- *Why it matters.* A text is an exogenous driver; reader-and-text is a skew
  product. A platform couples back. If that structural break is the literacy /
  algorithmacy cut, the competence claim becomes a dynamical-systems claim.
- *Method.* Formal: define a coordination environment as a skew product
  (driver independent of driven) vs a coupled product; map literacy claims to
  the skew case and algorithmacy claims to the coupled case.
- *Support / falsify.* Support: every lab dyadic (literacy) form admits a
  skew-product factorization with an exogenous driver; every triadic
  (algorithmacy) form does not. Falsify: a clear counterexample class on either
  side.

**A2.** Under what driver assumptions does Birkhoff's theorem license transferring
population reading norms to an individual reader?

- *Why it matters.* Literacy assessment assumes that transfer. Naming the
  assumptions shows when the transfer is warranted and when it is not.
- *Method.* Formal: state the invariant-measure and metric-indecomposability
  conditions under which time averages of reading observables equal ensemble
  averages (Birkhoff 1931; Connaughton et al. working notes §2).
- *Support / falsify.* Support: a short theorem list that literacy instruments
  implicitly assume. Falsify: a standard literacy observable whose time and
  ensemble averages diverge under those assumptions.

**A3.** Does restoring an exogenous, stationary driver to a platform interaction
(frozen recommender, fixed ranking) restore text-like ergodicity of user
observables?

- *Why it matters.* If freezing the mediator restores equality of averages,
  back-coupling — not mere complexity — is the non-ergodicity source.
- *Method.* Computational / empirical: compare Equality-of-Averages for the same
  user observable under live vs frozen ranking on a logged platform panel.
- *Support / falsify.* Support: live fails Equality-of-Averages; frozen passes.
  Falsify: both fail, or both pass.

**A4.** Can two environments share the same interface surface and differ only in
whether the mediating state depends on the user's past — and does that single
difference flip the literacy / algorithmacy demand?

- *Why it matters.* Isolates back-coupling as the treatment, holding UI and
  content fixed.
- *Method.* Computational: Boolean twin forms, one with S′ independent of
  (W,C) history beyond the current convey, one with S′ depending on accumulated
  state; classify Φ_MIP. **Computable now. Status: run** —
  `studies/ergodic_backcoupling_twins/` → `BACKCOUPLING_SPLITS`
  (H3 strong accum⇒triadic refuted).
- *Support / falsify.* Support: convey twin dyadic; accumulating twin triadic
  (or the reverse, if clean). Falsify: both verdicts identical across a
  designed panel.

---

## Strand B — Triadic mediation and ergodicity (Φ bridge)

**B1.** Do triadic forms (Φ_MIP > 0) show more ergodic components — attractors
and basins — than dyadic forms (Φ_MIP = 0) on matched Boolean panels?

- *Why it matters.* On finite deterministic maps the ergodic components are
  attractors/basins. If triadic forms are systematically more decomposable into
  components, non-ergodicity of party trajectories is a signature of active
  mediation.
- *Method.* Computational: enumerate attractors and basin sizes on a designed
  dyadic/triadic panel; compare component counts and basin entropy by verdict.
  Builds on `studies/genuine_bistability/`. First cell:
  [`../studies/ergodic_components_vs_phi/`](../studies/ergodic_components_vs_phi/).
  **Computable now. Status: run** → `NO_ERGODIC_SIGNATURE` (H1/H2 refuted;
  mean n_components tri 2.1429 vs dya 2.0000).
- *Support / falsify.* Support: triadic forms have strictly higher mean
  component count (or basin entropy) than dyadic forms on the panel, past a
  pre-registered margin. Falsify: no difference, or dyadic forms have more.

**B2.** Is party-level time-average ≠ ensemble-average a signature of an active
mediator (Φ_MIP > 0)?

- *Why it matters.* Direct operational link: the mediator makes an individual
  party's trajectory non-representative of the party ensemble.
- *Method.* Computational: for each form, compute per-party occupancy time
  averages from each basin vs the uniform (or invariant) ensemble average;
  test whether |time − ensemble| exceeds a threshold more often when
  Φ_MIP > 0. **Computable now. Status: run** (same first cell; H3 refuted —
  div_frac tri 0.9333 vs dya 1.0000).
- *Support / falsify.* Support: divergence rate higher for triadic forms.
  Falsify: divergence rate independent of verdict, or higher for dyadic forms.

**B3.** When genuine triadic/dyadic attractor coexistence holds
(`genuine_bistability` GENUINE_COEXISTENCE), does the basin a trajectory lands
in determine the literacy vs algorithmacy demand for that trajectory?

- *Why it matters.* Same coupling, different ergodic component, different
  competence demand — the sharpest version of "initial conditions select the
  component."
- *Method.* Computational: reuse the coexistence panel; report Φ_MIP by
  attractor, not by whole-form max. **Computable now. Status: run** (first
  cell H4 SUPPORTED — CROSS_BASIN_SPLIT on all 6 coexistence forms).
- *Support / falsify.* Support: at least one form has a triadic attractor and a
  dyadic attractor with nonempty basins (already the coexistence claim), and
  party time averages differ across basins. Falsify: coexistence without
  cross-basin divergence of party averages.

**B4.** Does the major-complex membership of the mediator predict the number of
ergodic components, holding party count fixed?

- *Why it matters.* Ties the lab's core-membership law to ergodic
  decomposability.
- *Method.* Computational: corpus forms stratified by whether S is in the major
  complex; compare attractor counts. **Computable now.**
- *Support / falsify.* Support: S-in-core forms have more components. Falsify:
  no association after controlling for n and indegree.

**B5.** On random Boolean ensembles at fixed n, is Φ_MIP correlated with basin
entropy (or with the number of attractors)?

- *Why it matters.* Population-level test of whether irreducibility and ergodic
  richness travel together.
- *Method.* Computational: the complete strict-mediation n=3 census
  (`corpus.population.enumerate_family`, 256 forms), rank correlation of
  Φ_MIP with basin entropy and with attractor count, permutation null.
  **Computable now. Status: run** —
  `studies/ergodic_ensemble_richness/` → `NO_ENSEMBLE_LINK`
  (ρ_entropy 0.1015, p 0.0510; ρ_count 0.1286, p 0.0185; both under
  |ρ| ≥ 0.20).
- *Support / falsify.* Support: positive rank correlation past null. Falsify:
  near-zero or negative correlation.

---

## Strand C — Multiplicative platform dynamics

**C1.** For creator reach / follower growth modeled as X_{n+1} = z_n X_n, does
the typical (time-average) growth λ = E[log z] diverge from the ensemble mean
growth μ = log E[z] under platform noise distributions?

- *Why it matters.* Algorithmacy as competence means optimizing the time-average
  growth rate (Kelly-like), not the expected value that A/B dashboards report
  (Peters 2019; Peters & Gell-Mann 2016; Redner 1990; Kelly 1956).
- *Method.* Formal / simulation: fit or posit z-distributions from public
  growth series; compare λ and μ.
- *Support / falsify.* Support: μ − λ exceeds a pre-registered gap on real or
  calibrated noise. Falsify: μ ≈ λ for the observed noise class.

**C2.** What is the ergodicity transformation for common platform success
metrics (followers, impressions, revenue)?

- *Why it matters.* Britto's volume contribution and Connaughton et al. §5:
  find the observable that restores equality of averages.
- *Method.* Formal / empirical: test log, Box–Cox, and differencing transforms
  for Equality-of-Averages on creator panels.
- *Support / falsify.* Support: a named transform passes Equality-of-Averages
  where the raw metric fails. Falsify: no transform in a pre-registered family
  restores it.

**C3.** Does Kelly-criterion allocation of effort across platform channels beat
expected-value allocation on time-average wealth for creators facing multiplicative
noise?

- *Why it matters.* Turns algorithmacy from a reading competence into a
  decision rule under non-ergodicity.
- *Method.* Simulation / empirical: compare Kelly vs EV policies on calibrated
  multiplicative walks (Kelly 1956; Peters & Adamou volume paper).
- *Support / falsify.* Support: Kelly dominates EV on time-average terminal
  wealth across a noise panel. Falsify: EV matches or beats Kelly on
  time-average for the same panel.

**C4.** When platform dashboards report ensemble-mean success, do they
systematically overstate the outcome a typical creator should expect?

- *Why it matters.* The pedagogical core of ergodicity economics applied to
  algorithmacy education.
- *Method.* Empirical: compare dashboard ensemble means to median and
  time-average growth on the same cohort.
- *Support / falsify.* Support: ensemble mean ≫ median / typical growth.
  Falsify: close agreement on the cohort's metrics.

---

## Strand D — Absorbing boundaries and ruin

**D1.** Do bans, demonetisation, shadowbans, and deplatforming behave as
absorbing boundaries for creator state, in the sense of Vanhoyweghen et al.'s
time-average decision framework?

- *Why it matters.* Algorithmacy includes decision rules that respect ruin, not
  only growth.
- *Method.* Formal / empirical: encode eligibility as a state with absorbing
  "removed" class; test whether observed exit is absorbing on logs.
- *Support / falsify.* Support: estimated return probability from "removed" ≈ 0
  on the observation window. Falsify: substantial return / appeal-restore rates
  that break absorption.

**D2.** Under absorbing platform risk, do time-average-optimal policies differ
from expected-utility policies that ignore ruin?

- *Why it matters.* Same fork Peters & Adamou draw for expected utility's time
  interpretation, now for platform actors.
- *Method.* Formal / simulation: compare policies under additive-ruin and
  multiplicative-ruin dynamics (Rodriguez Raposo & Coello Pulido; Vanhoyweghen
  et al.).
- *Support / falsify.* Support: named policy divergence on a calibrated ruin
  panel. Falsify: identical recommendations under both criteria.

**D3.** Does proximity to an absorbing eligibility boundary raise the value of
algorithmacy (trajectory-aware policy) relative to literacy (rule-reading)?

- *Why it matters.* Predicts where algorithmacy education has the highest
  marginal return — near ruin, not in the safe bulk.
- *Method.* Empirical / survey: compare decision quality under literacy vs
  algorithmacy framings as simulated distance-to-ban varies.
- *Support / falsify.* Support: algorithmacy framing gain increases near the
  boundary. Falsify: flat or reversed gain.

**D4.** Can a Boolean coordination form with an absorbing "ejected" mediator
state reproduce extractive ejection (political-economy arc) as an ergodic
absorbing component?

- *Why it matters.* Bridges ruin language to the lab's exact-Φ ejection studies.
- *Method.* Computational: extend ejection-order encodings with an absorbing
  ejected attractor; classify basins and Φ_MIP. **Computable now. Status:
  run** — `studies/ergodic_absorbing_ejection/` → `ABSORBING_EJECTION`.
- *Support / falsify.* Support: ejected attractor is dyadic or null-core and
  absorbing; pre-ejection attractors remain triadic. Falsify: no clean absorbing
  split, or Φ verdict unrelated to ejection.

---

## Strand E — Ergodic components as bubbles

**E1.** Are filter bubbles and lock-in formally invariant sets of the
user-and-user joint dynamics?

- *Why it matters.* Recasts a media-studies object as an ergodic component:
  once entered, the trajectory stays.
- *Method.* Formal / empirical: test approximate invariance of content-cluster
  sets under estimated transition kernels from logs.
- *Support / falsify.* Support: estimated exit rates below a pre-registered
  threshold inside named clusters. Falsify: clusters mix freely on the
  timescale of interest.

**E2.** Do cold-start / initial conditions select which ergodic component a
user enters, holding the recommender fixed?

- *Why it matters.* Typicality and initial-measure choice (Lebowitz; Goldstein;
  Connaughton et al. §2) become the mechanism of path dependence.
- *Method.* Empirical / simulation: randomize or stratify cold-start; measure
  component membership at a fixed horizon.
- *Support / falsify.* Support: initial condition predicts component beyond
  chance. Falsify: component membership independent of cold-start.

**E3.** Does the recommender's choice of invariant measure (the ranking /
  exploration policy) determine which user observables look "typical"?

- *Why it matters.* Platforms do not merely sample an invariant measure; they
  select one. Algorithmacy includes reading that selection.
- *Method.* Formal / computational: compare time averages under two policies
  that preserve different measures on the same state space.
- *Support / falsify.* Support: named observables change typical value across
  policies. Falsify: observables invariant to policy in the tested class.

**E4.** On Boolean mediated forms, do distinct basins correspond to distinct
"who-determines-whom" readings of the same wiring?

- *Why it matters.* Connects bubbles to the lab's determination / major-complex
  vocabulary.
- *Method.* Computational: for multistable forms, report major-complex and
  party time averages per   attractor. **Computable now. Status: run** (first cell E4 SUPPORTED —
  8/8 multistable forms disagree on core or occupancy).
- *Support / falsify.* Support: basins disagree on core membership or on party
  occupancy. Falsify: all basins share the same core and occupancy profile.

---

## Strand F — Infinite ergodicity and engagement traps

**F1.** Do infinite-scroll / continuous-feed interfaces induce sticky neutral
fixed points in engagement dynamics, in the sense of Pomeau–Manneville
intermittency?

- *Why it matters.* Sticky points trap trajectories; return times become
  heavy-tailed; self-averaging fails (Connaughton et al. §4; Pomeau &
  Manneville 1980).
- *Method.* Formal / empirical: fit return-time distributions to session-gap
  and re-engagement data; test power-law vs exponential.
- *Support / falsify.* Support: return times consistent with infinite-mean
  power law on a pre-registered test. Falsify: exponential or finite-mean fits
  dominate.

**F2.** Does cumulative engagement scale sub-linearly with persistent randomness
(Hopf ratio phenomenon) for heavy-tailed platform sessions?

- *Why it matters.* Loss of self-averaging means longer observation does not
  buy a stable individual mean — literacy's "practice average" fails.
- *Method.* Empirical: Hopf-ratio / aging statistics on session aggregates.
- *Support / falsify.* Support: aging and sub-linear growth of cumulative
  sums. Falsify: ordinary LLN-like convergence.

**F3.** Is virality an infinite-ergodicity phenomenon — rare trajectories
dominating ensemble reach while typical trajectories stay local?

- *Why it matters.* Ensemble virality metrics mislead the typical creator the
  same way ensemble wealth misleads the typical gambler.
- *Method.* Empirical: compare ensemble-mean reach to median and to
  time-average reach on share cascades (Redner-style multiplicative view).
- *Support / falsify.* Support: ensemble mean dominated by a thin upper tail;
  typical trajectory far below. Falsify: thin tails and close mean/median.

**F4.** Can a Boolean "sticky mediator" (lab sticky encodings) be read as a
finite-state analogue of a neutral sticky point, and does its basin structure
predict engagement hysteresis?

- *Why it matters.* Reuses probe #109 / bistability machinery as a finite
  caricature of infinite-ergodic stickiness.
- *Method.* Computational: sticky vs memoryless panel; compare return times to
  low-activity states and basin sizes. **Computable now. Status: run** —
  `studies/ergodic_sticky_returns/` → `HYSTERESIS_ONLY` (H1 return/mass
  clause refuted; #109 gap remains).
- *Support / falsify.* Support: sticky forms show longer return times /
  larger inactive basins than memoryless. Falsify: no difference.

---

## Strand G — Operational measurement

**G1.** Can an Equality-of-Distributions / Equality-of-Averages test on platform
or organizational logs classify an environment as text-like vs platform-like?

- *Why it matters.* Turns the Connaughton et al. §6 hierarchy
  (Metric Indecomposability > Equality of Distributions > Equality of Averages)
  into a lab instrument.
- *Method.* Empirical: pre-register observables and tests; apply to paired
  text-like (static FAQ, fixed syllabus) and platform-like (live feed, live
  dispatch) logs.
- *Support / falsify.* Support: text-like passes EoA/EoD; platform-like fails,
  at pre-registered α. Falsify: classification accuracy at chance.

**G2.** Does the operational ergodicity verdict agree with the lab's Φ verdict
on designed Boolean forms instrumented with synthetic "logs"?

- *Why it matters.* Calibration bridge between operational tests and exact Φ.
- *Method.* Computational: simulate trajectories from corpus forms; run EoA on
  party observables; compare to Φ_MIP. **Computable now. Status: run** —
  `studies/ergodic_eoa_vs_phi/` → `EOA_AGREES_PHI` (7/9; sticky FAIL×dyadic
  witness).
- *Support / falsify.* Support: agreement above a pre-registered rate.
  Falsify: agreement at chance.

**G3.** Can fielded team instruments (Wageman-style W, survey algorithmacy
scales) be paired with Equality-of-Averages tests on team trajectories to
separate cross-sectional from idiographic coordination findings?

- *Why it matters.* Organizational surveys are ensemble instruments;
  algorithmacy may be a time-average competence (Fisher volume paper; Molenaar
  2004).
- *Method.* Empirical: joint administration of W / algorithmacy scale and
  repeated within-team trajectory measures; test EoA.
- *Support / falsify.* Support: teams that fail EoA show scale–trajectory
  divergence. Falsify: scale predicts trajectory even when EoA fails.

**G4.** Where on the operational hierarchy (indecomposability / distributions /
averages) do real platform logs typically break?

- *Why it matters.* Tells practitioners which weaker notion still licenses
  their claims.
- *Method.* Empirical: apply the hierarchy in order on a public log corpus
  (Underwood & Paillusson spectroscopic framing as inspiration).
- *Support / falsify.* Support: a stable break-level across datasets of one
  class. Falsify: no consistent break-level.

---

## Strand H — Recommender RL as a non-ergodic optimiser

**H1.** Do production recommenders optimize ensemble reward while users live
time averages of experience?

- *Why it matters.* Structural misalignment: the platform's objective is
  ergodic in the ensemble sense; the user's welfare is a time average
  (Baumann et al.; Verbruggen et al. volume papers).
- *Method.* Formal / empirical: document the training objective; compare to
  user-level time-average welfare proxies.
- *Support / falsify.* Support: objective is ensemble; user proxy diverges.
  Falsify: objective already time-average at user grain, or proxies agree.

**H2.** In a triadic co-adaptation loop (user, recommender, counterpart), does
non-ergodic RL produce Φ_MIP > 0 encodings that expected-reward RL does not?

- *Why it matters.* Connects RL-under-non-ergodicity to the lab's triadic
  claim.
- *Method.* Computational / simulation: train small agents under ensemble vs
  time-average objectives; render resulting couplings as Boolean forms;
  classify Φ. Partially **computable now** once couplings are rendered.
- *Support / falsify.* Support: time-average objective yields higher triadic
  rate (or the reverse, cleanly). Falsify: identical verdict distributions.

**H3.** Is "cooption" by the platform — users adapting to the recommender while
the recommender adapts to the ensemble — a skew-product break?

- *Why it matters.* Names the political-economy interest of the mediator as a
  dynamical-systems fact.
- *Method.* Formal: write the joint map; show absence of a driver that evolves
  independently of the users.
- *Support / falsify.* Support: no skew-product factorization exists under
  stated coupling assumptions. Falsify: a natural exogenous driver remains.

**H4.** Do model-agnostic corrections for non-ergodic RL (Verbruggen et al.)
change major-complex membership when rendered as coordination forms?

- *Why it matters.* Tests whether the volume's RL fixes move the lab's
  structural verdict, not only reward curves.
- *Method.* Computational: render corrected vs uncorrected policies as forms;
  compare Φ_MIP and core. **Computable now** after rendering.
- *Support / falsify.* Support: correction flips verdict or core membership on
  a designed panel. Falsify: identical verdicts.

---

## Strand I — Education and assessment

**I1.** Does standard literacy assessment assume ergodicity — nomothetic norms
that treat the individual as exchangeable with the ensemble?

- *Why it matters.* If yes, literacy tests are mis-applied wherever the
  environment is platform-like (Fisher; Molenaar 2004).
- *Method.* Formal / psychometric review: extract the exchangeability /
  ergodicity assumptions in common literacy instruments.
- *Support / falsify.* Support: named instruments require EoA or
  exchangeability. Falsify: instruments already idiographic / time-average.

**I2.** Does algorithmacy education require idiographic, time-average assessment
rather than cross-sectional norms?

- *Why it matters.* Positive design claim: how to assess the competence this
  lab names.
- *Method.* Empirical: compare cross-sectional algorithmacy scores to
  within-person trajectory metrics on the same cohort (survey arm).
- *Support / falsify.* Support: low concordance between cross-section and
  trajectory; trajectory predicts platform outcomes better. Falsify: high
  concordance and equal predictive power.

**I3.** Can an Equality-of-Averages failure on a learner's platform log be used
as a diagnostic that the learner needs algorithmacy instruction, not more
literacy drills?

- *Why it matters.* Operational placement test for the competence.
- *Method.* Empirical: pre-register a diagnostic rule; validate against expert
  judgment and against outcome.
- *Support / falsify.* Support: diagnostic accuracy above chance and above a
  literacy-score baseline. Falsify: no incremental accuracy.

**I4.** Do cognitive speed–accuracy findings under non-ergodic reward dynamics
(Fleming et al. volume paper) transfer to platform decision tasks that demand
algorithmacy?

- *Why it matters.* Imports a volume result into the lab's competence framing.
- *Method.* Experimental: replicate the speed–accuracy / reward-dynamics
  manipulation on a platform-like task.
- *Support / falsify.* Support: same qualitative dependence of optimal response
  time on reward dynamics. Falsify: no transfer.

---

## Strand J — Organizational coordination

**J1.** When do cross-sectional organizational findings about coordination forms
generalize to a given team's trajectory?

- *Why it matters.* Org surveys are ensembles; teams live time averages. The
  ergodicity question is the generalizability question (Fisher).
- *Method.* Empirical: paired cross-section and repeated within-team measures
  on coordination observables; test EoA / EoD.
- *Support / falsify.* Support: named observables fail EoA while still showing
  cross-sectional effects. Falsify: EoA holds wherever cross-sectional effects
  do.

**J2.** Do triadic (algorithmacy-demanding) teams show larger
within-team time-vs-ensemble divergence than dyadic teams, when both are
rendered and classified by the lab protocol?

- *Why it matters.* Field bridge from Strand B to real teams.
- *Method.* Field / computational: field protocol → Boolean render → Φ_MIP;
  trajectory EoA on team logs. Uses existing field packet machinery.
- *Support / falsify.* Support: divergence associates with triadic verdict.
  Falsify: no association.

**J3.** Is "the average team" a misleading unit for advising a specific team
whose coordination form is triadic?

- *Why it matters.* Practitioner stake of the whole track.
- *Method.* Empirical / case: compare advice from ensemble benchmarks vs
  trajectory-conditioned advice; pre-register an outcome.
- *Support / falsify.* Support: trajectory-conditioned advice outperforms on
  the outcome. Falsify: ensemble advice matches or wins.

**J4.** Can operational ergodicity tests on collaboration logs (commits, PRs,
dispatches) classify a repo or dispatch unit as text-like (process docs suffice)
vs platform-like (algorithmacy required)?

- *Why it matters.* Extends G1 into the recurrence / OSS settings the lab
  already reads.
- *Method.* Empirical: EoA on recurrence-arm event series; compare to
  governance / gate labels from v8–v10.
- *Support / falsify.* Support: classification aligns with named gate /
  mediation labels above chance. Falsify: no alignment.

---

## Count by strand

| Strand | Theme | Questions | Computable now |
| --- | --- | ---: | ---: |
| A | Text vs platform | 4 | A4 |
| B | Triadic mediation × Φ | 5 | B1–B5 |
| C | Multiplicative dynamics | 4 | — |
| D | Absorbing boundaries | 4 | D4 |
| E | Bubbles as components | 4 | E4 |
| F | Infinite ergodicity / traps | 4 | F4 |
| G | Operational measurement | 4 | G2 |
| H | Recommender RL | 4 | H2*, H4* |
| I | Education / assessment | 4 | — |
| J | Organizational coordination | 4 | — |
| **Total** | | **41** | **12 (+2 partial)** |

\*Partial: computable once couplings / policies are rendered as Boolean forms.

## First cell

Strand B attractor / component questions on existing infrastructure:
[`../studies/ergodic_components_vs_phi/`](../studies/ergodic_components_vs_phi/).
**Status: run.** Verdict `NO_ERGODIC_SIGNATURE` with secondary
`CROSS_BASIN_SPLIT` | `BASIN_DETERMINATION_SPLIT`. Companion computable
cells A4/D4/F4/G2 also run (see study FINDINGS). G-strand stress follow-on
`studies/ergodic_eoa_instrument/` packages the EoA instrument and refutes
T8's ≥0.65 agreement on a 42-form panel (`EOA_TRACKS_MI_NOT_PHI`). The
per-outcome follow-on `studies/ergodic_eoa_basin/` clears those miss
classes under basin/stationary references but collapses binary EoA to
all-AGREEING (`EOA_BASIN_INCONCLUSIVE`). Settling-time residual
`studies/ergodic_settling_time/` does not explain the remaining
continuous gap (`SETTLING_NULL`). Gap decomposition
`studies/ergodic_gap_decomposition/` finds the association is not a
fluke but is unexplained by phase / path / observable / panel
mechanisms (`GAP_UNEXPLAINED`). Theories
and experiment designs: [`THEORIES.md`](THEORIES.md),
[`EXPERIMENTS.md`](EXPERIMENTS.md). Deferred: C (needs calibrated series),
H (needs RL render), I empirical, J field.
