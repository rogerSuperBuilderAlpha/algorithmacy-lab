# Ergodicity × Algorithmacy — theories

Named, falsifiable conjectures that tie the ten agenda strands to the lab's
literacy / algorithmacy cut. Each entry states the claim, a formal sketch in
the notation of Birkhoff, skew products, multiplicative growth, and the
operational hierarchy, what the claim predicts, and what would refute it.
Parts that follow as theorems on finite deterministic Boolean maps are marked
**derived**; the rest are **conjecture**.

Notation. A finite Boolean coordination form is a map \(T: X \to X\) on
\(X = \{0,1\}^n\). Attractors are the periodic orbits of \(T\); each state
flows to exactly one attractor, so the basins \(\{B_a\}\) partition \(X\).
The unique \(T\)-invariant probability supported uniformly on attractor \(a\)
is denoted \(\mu_a\). Exact binary IIT-4.0 \(\Phi_{\mathrm{MIP}}\) is evaluated
on attractor states; whole-form **triadic** means \(\Phi_{\mathrm{MIP}} >
\varepsilon\) under the lab classifier, **dyadic** means otherwise. Strand
citations point to [`AGENDA.md`](AGENDA.md) and [`SOURCES.md`](SOURCES.md).

---

## T1 — Skew-product criterion (Strand A)

**Statement (conjecture).** A coordination environment demands literacy iff
it admits a skew-product factorization \(T(x,y) = \bigl(f(x),\, g(x,y)\bigr)\)
in which the driver \(f\) is independent of the driven coordinate \(y\), and
demands algorithmacy when every natural factorization is a coupled product
(the mediating coordinate depends on party trajectories).

**Formal sketch.** A skew product over an ergodic base \((X,f,\nu)\) yields,
under mild regularity, an invariant measure for which Birkhoff's theorem
equates time averages of reading observables along \(\nu\)-typical
trajectories with ensemble averages (Birkhoff 1931; Connaughton, Jeroen, and
Paillusson 2026 working notes §2). A platform mediator \(S\) with update
\(S' = h(W,S,C)\) that retains path-dependent state breaks the exogenous-
driver assumption: there is no coordinate that evolves independently of the
parties it coordinates. Literacy instruments that assume exchangeability of
readers with a population therefore presuppose the skew-product case
(Molenaar 2004).

**Derived on Boolean forms.** For a finite deterministic map, invariance of a
coordinate block \(D \subset \{1,\ldots,n\}\) under every update (the next
state of bits in \(D\) depends only on bits in \(D\)) is exactly a
skew-product factorization over that block. Checking independence of the
mediator bit's update from party bits is decidable by inspecting the Boolean
rule table. That check is derived; the competence claim that maps skew →
literacy and coupled → algorithmacy is conjecture.

**Predicts.** Every lab dyadic (literacy) form admits an exogenous-driver
factorization; every triadic (algorithmacy) form does not, on a designed
twin panel that holds the interface fixed and toggles only back-coupling
(A4).

**Refuted by.** A clean class of triadic forms that remain skew products, or
a clean class of dyadic forms that are irreducibly coupled, on that panel.

---

## T2 — Mediator-induced ergodicity breaking tracks \(\Phi_{\mathrm{MIP}} > 0\)
(Strands B1–B2)

**Statement (conjecture).** On matched Boolean panels, whole-form triadic
forms have (i) strictly higher mean ergodic-component count and (ii) higher
rates of party-level time–ensemble divergence than whole-form dyadic forms.

**Formal sketch.** On finite \(X\), every invariant probability is a convex
combination of the ergodic measures \(\{\mu_a\}\) supported on attractors.
Metric indecomposability fails whenever \(T\) has two or more attractors with
positive basin mass: time averages starting in basin \(B_a\) converge to
integrals against \(\mu_a\), not against a mixture over all attractors
(Connaughton et al. working notes §2). Party occupancy
\(\overline{x}_i^{(a)} = \frac{1}{|a|}\sum_{x \in a} x_i\) is the time average
along attractor \(a\); the ensemble contrast on \(a\) is the same for the
uniform cycle measure, and the secondary contrast is the uniform average over
\(X\). Divergence
\(\bigl|\overline{x}_i^{(a)} - \mathbb{E}_{\mathrm{ens}}[x_i]\bigr| > \varepsilon\)
is an Equality-of-Averages failure at the party grain.

**Derived.** Attractors partition the ergodic components of a finite
deterministic map; component count equals the number of attractors with
nonempty basins. Basin entropy
\(H = -\sum_a (b_a/2^n)\log(b_a/2^n)\) is a derived functional of the basin
sizes. The association of those quantities with \(\Phi_{\mathrm{MIP}}\) is
conjecture.

**Predicts.** Mean component count for triadic forms exceeds that for dyadic
forms by \(\delta_c \ge 0.5\); the fraction of (form, party, attractor) cells
with divergence \(> 0.1\) is higher for triadic forms (B1, B2;
[`../studies/ergodic_components_vs_phi/`](../studies/ergodic_components_vs_phi/)).

**Refuted by.** No difference past the pre-registered margins, or the reverse
ordering.

---

## T3 — Cross-basin competence split under coexistence (Strand B3)

**Statement (conjecture).** When a single coupling hosts both a triadic and a
dyadic attractor (the `genuine_bistability` coexistence class), the basin a
trajectory lands in selects the literacy vs algorithmacy demand for that
trajectory: party time averages differ across the two attractors.

**Formal sketch.** Coexistence means two ergodic measures \(\mu_{\mathrm{tri}}\)
and \(\mu_{\mathrm{dya}}\) with nonempty basins. Birkhoff averages of party
observables converge to \(\int x_i\,d\mu_{\mathrm{tri}}\) or
\(\int x_i\,d\mu_{\mathrm{dya}}\) according to the initial condition. If those
integrals differ by \(\ge \varepsilon_{\mathrm{div}}\), Equality of Averages
fails across components of the same form — the sharpest finite analogue of
"initial conditions select the component" (Lebowitz; Goldstein; Connaughton
et al. §2).

**Derived.** Existence of coexistence on the lab panel is already established
(`studies/genuine_bistability/`, GENUINE_COEXISTENCE). Cross-basin divergence
of party averages is an additional, testable claim.

**Predicts.** Every coexistence form on the panel shows at least one party
with cross-basin occupancy gap \(\ge 0.1\).

**Refuted by.** Coexistence without cross-basin party-average divergence.

---

## T4 — Time-average competence under multiplicative reach (Strand C)

**Statement (conjecture).** For creator state \(X_{n+1} = z_n X_n\) with i.i.d.
multiplicative noise \(z > 0\), algorithmacy is competence at optimizing the
time-average growth rate \(\lambda = \mathbb{E}[\log z]\), not the ensemble
mean growth \(\mu = \log \mathbb{E}[z]\). Platform dashboards that report
ensemble means systematically overstate the growth a typical creator should
expect whenever \(\mathrm{Var}(\log z) > 0\).

**Formal sketch.** By the LLN,
\(\frac{1}{n}\log X_n \to \lambda\) almost surely, while
\(\log \mathbb{E}[X_n]/X_0 = n\mu\). Jensen's inequality gives
\(\mu \ge \lambda\), with equality iff \(z\) is a.s. constant (Redner 1990;
Peters and Gell-Mann 2016; Peters 2019). Kelly's proportional betting rule
maximizes \(\lambda\) (Kelly 1956). The ergodicity transformation for
multiplicative wealth is the logarithm: Equality of Averages holds for
\(\log X\) under standard conditions where it fails for \(X\) (Britto 2026;
Connaughton et al. §5).

**Derived.** \(\mu - \lambda = \log\mathbb{E}[z] - \mathbb{E}[\log z] \ge 0\)
for any positive \(z\) with finite logs — a theorem, not a conjecture. That
platform noise places \(\mu - \lambda\) past a pedagogically material gap, and
that Kelly beats EV on creator time-average wealth, remain conjecture pending
calibrated \(z\)-distributions.

**Predicts.** On calibrated or public growth series, \(\mu - \lambda\) exceeds
a pre-registered gap; Kelly allocation dominates EV on time-average terminal
wealth (C1, C3, C4).

**Refuted by.** \(\mu \approx \lambda\) for the observed noise class, or EV
matching Kelly on time-average wealth for that class.

---

## T5 — Ruin-aware navigation (Strand D)

**Statement (conjecture).** Bans, demonetisation, and deplatforming act as
absorbing boundaries for creator eligibility. Near those boundaries,
time-average-optimal policies diverge from expected-utility policies that
ignore absorption, and the marginal value of algorithmacy (trajectory-aware
policy) over literacy (rule-reading) rises with proximity to ruin.

**Formal sketch.** Let eligibility \(E_t \in \{\mathrm{active},
\mathrm{removed}\}\) with \(\mathrm{removed}\) absorbing. Time-average
criteria conditioned on survival differ from unconditional expected utility
once absorption carries positive probability (Vanhoyweghen, Verbeken, and
Ginis 2026; Rodriguez Raposo and Coello Pulido 2026; Peters and Adamou
2026 on the time interpretation of expected utility). On Boolean forms, an
absorbing "ejected" mediator attractor is an ergodic component with exit
rate zero; pre-ejection attractors may remain triadic while the ejected
component is dyadic or null-core (D4).

**Derived on Boolean forms.** A fixed point (or cycle) whose basin is entered
and never left is an absorbing ergodic component by definition. Encoding an
ejected latch as such a component is a modeling choice; the Φ-pattern
prediction is conjecture.

**Predicts.** Estimated return probability from "removed" ≈ 0 on observation
windows (D1); named policy divergence under additive/multiplicative ruin
(D2); algorithmacy framing gain increases near the boundary (D3); Boolean
ejected attractors are absorbing and dyadic/null-core while pre-ejection
attractors remain triadic (D4).

**Refuted by.** Substantial restore rates; identical ruin-aware and ruin-blind
policies; flat framing gains; no clean absorbing Φ split on the Boolean panel.

---

## T6 — Bubbles as ergodic components (Strand E)

**Statement (conjecture).** Filter bubbles and lock-in are approximately
invariant sets of the user–mediator joint dynamics. Cold-start selects the
component; the recommender's policy selects which invariant measure makes a
user look typical. On Boolean mediated forms, distinct basins disagree on
major-complex membership or party occupancy — distinct "who-determines-whom"
readings of the same wiring.

**Formal sketch.** An invariant set \(I\) with negligible exit rate under the
estimated transition kernel is an approximate ergodic component. Typicality
is measure-relative: changing the invariant measure (via ranking /
exploration policy) changes which observables look typical (Lebowitz;
Goldstein; Connaughton et al. §2; E3). On finite Boolean maps, basins are
exact invariant sets; major-complex membership and party occupancy per
attractor are computable (E4).

**Derived.** Basin invariance under a deterministic map is a theorem.
Disagreement of core membership or occupancy across basins of multistable
forms is a testable claim on lab panels.

**Predicts.** Multistable Boolean forms show cross-basin disagreement on core
or party occupancy (E4); cold-start predicts component beyond chance on
logged systems (E2).

**Refuted by.** All basins sharing core and occupancy; component membership
independent of cold-start.

---

## T7 — Sticky mediation as finite infinite-ergodicity (Strand F)

**Statement (conjecture).** Sticky mediator encodings are finite-state
analogues of neutral sticky points: they enlarge inactive basins and lengthen
return times to low-activity states relative to memoryless twins, producing
a caricature of the self-averaging failure that infinite ergodicity induces
via heavy-tailed returns (Pomeau and Manneville 1980; Connaughton et al. §4;
Aaronson 1997).

**Formal sketch.** Infinite ergodic theory replaces finite invariant measures
with infinite ones; return-time tails become heavy and Hopf's ratio replaces
the LLN. A Boolean sticky latch cannot host an infinite measure, but it can
inflate the basin of an inactive fixed point and raise mean return time to
that state under a uniform or drive-perturbed sampling of trajectories —
the finite signature the lab can compute (F4; probe #109 / bistability
machinery).

**Derived.** Return times and basin sizes on a finite map are well-defined
and computable. The analogy to infinite ergodicity is interpretive;
quantitative agreement with power-law session data is a separate empirical
claim (F1–F3).

**Predicts.** Sticky forms show larger inactive basins and longer mean return
times to low-activity states than memoryless twins on a matched panel (F4).

**Refuted by.** No difference in return times or inactive-basin mass.

---

## T8 — Operational EoA calibrates to \(\Phi\) (Strand G)

**Statement (conjecture).** Equality-of-Averages (and, stronger, Equality-of-
Distributions) tests on party observables from simulated trajectories of
Boolean forms agree with the lab's \(\Phi_{\mathrm{MIP}}\) verdict above
chance: forms that fail EoA are disproportionately triadic; forms that pass
are disproportionately dyadic. The operational hierarchy Metric
Indecomposability > Equality of Distributions > Equality of Averages
(Connaughton et al. §6; Underwood and Paillusson 2026) thereby becomes a
field instrument that the exact-Φ pipeline can calibrate (G1–G2).

**Formal sketch.** For observable \(f\) and trajectory \(x_0, T(x_0),\ldots\),
EoA asks whether
\(\lim_{N\to\infty} N^{-1}\sum_{t=0}^{N-1} f(T^t x_0)\) equals the ensemble
mean under a reference measure (uniform on \(X\), or the mixture of
\(\mu_a\) weighted by basin mass). On a finite map with multiple attractors,
EoA fails for generic \(f\) whenever the initial measure is not concentrated
on one component — a **derived** fact. Agreement of that failure rate with
whole-form \(\Phi_{\mathrm{MIP}}\) across a designed panel is conjecture.

**Predicts.** Agreement rate of EoA-fail ↔ triadic (and EoA-pass ↔ dyadic)
above a pre-registered threshold on synthetic logs from corpus forms (G2).

**Refuted by.** Agreement at chance, or the reverse association.

**Computational status.** G2 (`ergodic_eoa_vs_phi`) supported agreement on
the nine-form designed panel (7/9). The instrument stress cell
(`ergodic_eoa_instrument`) refutes the ≥0.65 threshold on a 42-form
panel (17/42); disagreements concentrate in dyadic multi-attractor forms.
The per-outcome follow-on (`ergodic_eoa_basin`) clears those miss classes
under basin-restricted and attractor-stationary references (20/20 multi
and 5/5 single rescued) but collapses the binary instrument to
all-AGREEING (agree 25/42 = dyadic base rate); verdict
`EOA_BASIN_INCONCLUSIVE`. The settling-time residual cell
(`ergodic_settling_time`) tests whether the remaining continuous
basin-mode gap–Φ association is finite-T burn-in: mean transient does
not separate triadic from dyadic (AUC 0.540), and controlling for
transient does not shrink the gap association; verdict `SETTLING_NULL`.
The gap-decomposition cell (`ergodic_gap_decomposition`) tests whether
finite-T phase artifact, within-basin path diversity, party-vs-mediator
observable choice, or panel composition absorbs the residual continuous
association: the association is not a fluke (AUC 0.729; bootstrap CI
[0.560, 0.862]; permutation p 0.0075), but none of the four mechanisms
passes; verdict `GAP_UNEXPLAINED`. T8's field-instrument ambition does
not survive as a binary Φ proxy once multistability is conditioned out,
and the residual continuous signal is neither a settling-time confound
nor explained by the pre-registered gap decompositions on this panel.
The cycle-ordering cell (`ergodic_cycle_ordering`) tests whether the
ordering of party-bit flips around the attractor drives that residual.
The association again clears the fluke check (AUC 0.7294; bootstrap CI
[0.5600, 0.8624]; permutation p 0.0075). The on-cycle remainder, the
ordering features, and the amplitude controls all fail their absorption
rules; verdict `ORDERING_NULL`.

---

## T9 — Ensemble RL misaligns with time-average welfare (Strand H)

**Statement (conjecture).** Production recommenders that maximize ensemble
reward while users live time averages of experience instantiate a structural
misalignment: the platform objective is ergodic in the ensemble sense; user
welfare is a time average (Baumann et al. 2026; Verbruggen, Vanhoyweghen, and
Ginis 2026). Cooption — users adapting to the recommender while the
recommender adapts to the ensemble — is a skew-product break (H3). Rendering
ensemble-trained vs time-average-trained couplings as Boolean forms yields
different \(\Phi_{\mathrm{MIP}}\) / major-complex patterns (H2, H4).

**Formal sketch.** Let \(R(\theta) = \mathbb{E}_{x \sim \nu}[r(x;\theta)]\) be
an ensemble training objective and
\(\lambda_u(\theta) = \lim N^{-1}\sum_t r(T_\theta^t u)\) a user time average.
Non-equality of the two under non-ergodic \(T_\theta\) is the Verbruggen et
al. setting. Absence of an exogenous driver in the joint user–recommender–
counterpart map is the H3 claim (links to T1).

**Derived.** None on lab forms until couplings are rendered. The misalignment
statement is conjecture about production systems; the Boolean rendering
predictions become testable once policies are encoded.

**Predicts.** Documented ensemble objectives with diverging user proxies
(H1); different triadic rates under the two objectives once rendered (H2);
no skew-product factorization of the cooption map (H3).

**Refuted by.** Objectives already time-average at user grain; identical Φ
verdicts after rendering; a natural exogenous driver remaining.

---

## T10 — Idiographic assessment for algorithmacy; ensemble advice fails for
triadic teams (Strands I–J)

**Statement (conjecture).** Standard literacy assessment assumes ergodicity —
nomothetic norms that treat the individual as exchangeable with the ensemble
(Fisher 2026; Molenaar 2004). Algorithmacy requires idiographic,
time-average assessment. Cross-sectional findings about "the average team"
do not generalize to a given team's trajectory when the coordination form is
triadic: within-team time–ensemble divergence is larger for triadic than for
dyadic teams under the lab rendering protocol.

**Formal sketch.** Exchangeability of persons with a population measure is
EoA for person-level observables. When EoA fails, cross-sectional norms do
not license individual claims. Strand J lifts Strand B's finite signature to
fielded teams: render → \(\Phi_{\mathrm{MIP}}\); test EoA on team logs; ask
whether divergence associates with the triadic verdict (J1–J2).

**Derived.** None until field logs are paired with renders. The psychometric
claim that named literacy instruments require EoA is a reviewable conjecture
(I1).

**Predicts.** Named instruments require EoA or exchangeability (I1); low
concordance between cross-sectional algorithmacy scores and trajectory
metrics (I2); triadic-rendered teams show larger EoA failures than dyadic
ones (J2); trajectory-conditioned advice outperforms ensemble benchmarks on
a pre-registered outcome (J3).

**Refuted by.** Instruments already idiographic; high cross-section /
trajectory concordance; no association of divergence with Φ verdict;
ensemble advice matching or beating trajectory-conditioned advice.

---

## What is derived vs conjecture (summary)

| Claim | Status |
| --- | --- |
| Attractors = ergodic components on finite deterministic maps | **derived** |
| Basin entropy and party cycle averages are well-defined | **derived** |
| Skew-product factorization decidable from Boolean rule tables | **derived** |
| \(\mu - \lambda \ge 0\) for multiplicative noise | **derived** |
| Absorbing fixed points are absorbing ergodic components | **derived** |
| EoA fails across multiple attractors for generic observables | **derived** |
| Skew ↔ literacy / coupled ↔ algorithmacy | **conjecture** (T1) |
| Component count and divergence track \(\Phi_{\mathrm{MIP}}\) | **conjecture** (T2) |
| Cross-basin competence split under coexistence | **conjecture** (T3) |
| Platform noise makes \(\mu-\lambda\) material; Kelly beats EV | **conjecture** (T4) |
| Ruin raises algorithmacy's marginal value; ejected Φ split | **conjecture** (T5) |
| Bubbles = components; basins disagree on core | **conjecture** (T6) |
| Sticky forms caricature infinite-ergodic stickiness | **conjecture** (T7) |
| Operational EoA agrees with Φ on synthetic logs | **partial** (T8): G2 7/9 supported; 42-form stress **refutes** ≥0.65 — EoA tracks MI / dyadic×multi, not Φ; basin/stationary fix clears those FPs but binary EoA collapses (`EOA_BASIN_INCONCLUSIVE`); settling-time residual does not explain the remaining continuous gap (`SETTLING_NULL`); gap decomposition leaves the residual unexplained (`GAP_UNEXPLAINED`); cycle ordering of party-bit flips likewise leaves it unexplained (`ORDERING_NULL`) |
| Ensemble RL / cooption / rendered Φ differences | **conjecture** (T9) |
| Idiographic assessment; triadic team divergence | **conjecture** (T10) |

First computational tests target T2 and T3 (and the Boolean parts of T1, T5,
T6, T7, T8) under
[`../studies/ergodic_components_vs_phi/`](../studies/ergodic_components_vs_phi/)
and the companion computable cells listed in [`EXPERIMENTS.md`](EXPERIMENTS.md).
