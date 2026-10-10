# Ergodicity × Algorithmacy — proposed experiments

One designed experiment per agenda strand (A–J). Each entry states the
hypothesis, model or data, observable, ergodicity test, controls, expected
outcomes under the named theories in [`THEORIES.md`](THEORIES.md), compute or
data cost, and whether the cell is runnable now with lab code. Hypotheses for
computable cells are frozen in the corresponding study folder before any
analysis script runs.

Ergodicity tests use the Connaughton, Jeroen, and Paillusson (2026) operational
hierarchy: Metric Indecomposability (MI) > Equality of Distributions (EoD) >
Equality of Averages (EoA). On finite Boolean maps, MI fails whenever there
are two or more attractors; EoA is tested with a pre-registered statistic and
threshold below.

---

## Exp-A — Back-coupling twin panel (Strand A / T1)

**Hypothesis.** Holding the convey interface fixed, a twin whose mediator
update depends only on the current convey (exogenous / skew-like) is whole-
form dyadic, while the twin whose mediator accumulates path-dependent state
is whole-form triadic — or the reverse, cleanly (A4).

**Model / data.** Boolean n=3 twins: **convey** \(S' = W \land C\),
\(W'=S\), \(C'=S\) (memoryless triad) vs **accumulating**
\(S' = (W \land C) \lor S\) (sticky). Secondary twins: OR-commit vs sticky-OR;
parity hub vs sticky-parity.

**Observable.** Whole-form \(\Phi_{\mathrm{MIP}}\) verdict; presence of a
skew-product factorization (mediator update independent of retained \(S\)).

**Ergodicity test.** Structural: skew-product check on the rule table
(derived). EoA not primary here.

**Statistic / threshold.** Verdict flip across each twin pair; skew factor
present on convey twin, absent on accumulating twin.

**Controls.** Instrument gate: memoryless whole-form triadic \(\Phi=2\);
sticky whole-form dyadic \(\Phi=0\) (matches #43). Abort if either fails.

**Expected under theories.** T1 predicts the structural skew break. Note:
existing #43 sticky is dyadic, so the primary twin may **refute** a naive
"accumulating ⇒ triadic" reading and force T1 to use skew-product structure
rather than Φ alone — a useful stress test.

**Cost.** Seconds on n=3. **Runnable now:** yes
([`../studies/ergodic_backcoupling_twins/`](../studies/ergodic_backcoupling_twins/)
or as a secondary panel inside the first cell).

---

## Exp-B — Ergodic components vs \(\Phi_{\mathrm{MIP}}\) (Strand B / T2–T3)

**Hypothesis.** Triadic forms have higher mean component count (\(\delta_c
\ge 0.5\)) and higher party time–ensemble divergence rates than dyadic forms;
coexistence forms show cross-basin party gaps \(\ge 0.1\) (B1–B3; H1–H4 in
the first-cell spec).

**Model / data.** Designed n=3 panel frozen in
[`../studies/ergodic_components_vs_phi/`](../studies/ergodic_components_vs_phi/):
memoryless, sticky, xor_memory, or_commit, sticky_or, sticky_parity,
parity_hub, maj3, plus corpus dyadic/triadic landmarks as listed in the
analyze script's form table.

**Observable.** Attractor count, basin sizes, basin entropy, party occupancy
time averages on each attractor, per-attractor and whole-form
\(\Phi_{\mathrm{MIP}}\).

**Ergodicity test.** EoA at party grain: for each (form, party, attractor),
\(|\bar x_i^{(a)} - \mathbb{E}_a[x_i]|\) (primary; cycle-uniform) and vs
uniform-on-\(X\) (secondary). MI: component count \(> 1\).

**Statistic / threshold.** \(\varepsilon_{\mathrm{div}} = 0.1\) occupancy;
\(\delta_c \ge 0.5\); \(\delta_h \ge 0.1\) bits; primary verdict words as in
`hypotheses.md`.

**Controls.** Faithful memoryless triad triadic; sticky dyadic. Abort on
gate failure.

**Expected under theories.** T2 supported ⇒ `COMPONENTS_TRACK_TRIAD` or
`COUNT_ONLY` / `DIVERGENCE_ONLY`. T3 supported ⇒ `CROSS_BASIN_SPLIT`. Nulls
yield `NO_ERGODIC_SIGNATURE`.

**Cost.** ~minutes on n=3 exact Φ. **Runnable now:** yes (first cell).

---

## Exp-C — Multiplicative reach: \(\lambda\) vs \(\mu\) (Strand C / T4)

**Hypothesis.** For calibrated creator-growth noise \(z\),
\(\mu - \lambda = \log\mathbb{E}[z] - \mathbb{E}[\log z]\) exceeds a
pre-registered gap \(\delta_\lambda\), and Kelly allocation of effort beats
EV on time-average terminal wealth (C1, C3).

**Model / data.** Public creator growth series or a synthetic log-normal /
power-law \(z\) panel calibrated to published moments; Kelly vs EV policies
on a two-channel effort simplex.

**Observable.** \(\lambda\), \(\mu\), terminal wealth time averages under each
policy.

**Ergodicity test.** EoA on raw reach (expect fail) vs on \(\log\) reach
(expect pass) — Britto / Connaughton §5 transformation check.

**Statistic / threshold.** \(\mu - \lambda \ge \delta_\lambda\) (set at
calibration commit); Kelly time-average wealth \(>\) EV by a pre-registered
margin on \(\ge 80\%\) of noise draws.

**Controls.** Degenerate \(z \equiv const\) (expect \(\mu=\lambda\), Kelly=EV);
finite-sample bootstrap confidence bands.

**Expected under theories.** T4: material gap and Kelly dominance. Dashboard
ensemble means overstate typical growth (C4).

**Cost.** Simulation: CPU-minutes. Empirical fit: needs a public series.
**Runnable now:** simulation half only (no platform log in-repo); defer
empirical fit.

---

## Exp-D — Absorbing ejected mediator (Strand D / T5)

**Hypothesis.** A Boolean form with an absorbing "ejected" mediator state
hosts an ejected attractor that is dyadic or null-core and absorbing;
pre-ejection attractors remain triadic (D4).

**Model / data.** Extend ejection-order / #110 encodings: add a latch bit or
mediator rule that, once \(S=0\) under an extractive tilt, stays ejected;
compare basins and \(\Phi_{\mathrm{MIP}}\) before and after absorption.

**Observable.** Attractor list; exit rate from ejected component (=0 if
absorbing); whole-form and per-attractor verdicts; major-complex membership.

**Ergodicity test.** MI: ejected component vs pre-ejection components. EoA:
party averages inside ejected basin vs pre-ejection basins.

**Statistic / threshold.** Exit rate from ejected attractor \(= 0\);
ejected attractor dyadic/null-core; at least one pre-ejection attractor
triadic.

**Controls.** Non-absorbing #110 tilt path (known co-eject→owner); memoryless
triad gate.

**Expected under theories.** T5 Boolean clause supported on a clean encoding;
messy encodings that fail the absorbing split refute the encoding, not
necessarily the field claim.

**Cost.** Seconds–minutes. **Runnable now:** yes (encoding design +
classifier / attractor code).

---

## Exp-E — Basins as who-determines-whom (Strand E / T6)

**Hypothesis.** On multistable Boolean forms, distinct basins disagree on
major-complex membership or on party occupancy profiles (E4).

**Model / data.** Coexistence and MULTI_SAME forms from the Exp-B panel;
per-attractor maximal complex via PyPhi.

**Observable.** Core set per attractor state; party occupancy per attractor.

**Ergodicity test.** Cross-basin comparison (not EoA vs ensemble): cores
differ or max party occupancy gap \(\ge 0.1\).

**Statistic / threshold.** Fraction of multistable forms with core or
occupancy disagreement \(\ge 2/3\) of the multistable subclass.

**Controls.** Single-attractor forms (expect trivial agreement); instrument
gates as in Exp-B.

**Expected under theories.** T6 supported if coexistence/MULTI_SAME forms
split; refuted if all basins share core and occupancy.

**Cost.** Folded into Exp-B runtime. **Runnable now:** yes.

---

## Exp-F — Sticky return times (Strand F / T7)

**Hypothesis.** Sticky mediator forms show larger inactive basins and longer
mean return times to low-activity states than memoryless twins (F4).

**Model / data.** Matched sticky vs memoryless (and sticky-OR vs OR-commit)
pairs; enumerate return times under exhaustive start-state enumeration (finite
\(2^n\)).

**Observable.** Basin mass of inactive attractors (e.g. \(000\)); mean /
median return time to inactive set; activity hysteresis area (#109) as
secondary witness.

**Ergodicity test.** Not classical EoA; finite caricature of heavy-tailed
returns — compare mean return time sticky vs memoryless.

**Statistic / threshold.** Sticky mean return time to inactive set
\(\ge 1.2\times\) memoryless, or inactive basin mass strictly larger, on
every matched pair.

**Controls.** #109 hysteresis gap \(\ge 0.05\); parity_hub single-attractor
contrast.

**Expected under theories.** T7 supported on sticky pairs; MULTI_SAME sticky
without longer returns would refute the return-time clause.

**Cost.** Seconds. **Runnable now:** yes.

---

## Exp-G — EoA on synthetic logs vs \(\Phi\) (Strand G / T8)

**Hypothesis.** EoA failure on party observables from simulated trajectories
agrees with whole-form triadic verdict above a pre-registered rate (G2).

**Model / data.** Same Exp-B panel; synthetic "logs" = trajectories from every
start state (or uniform random starts), party bit as observable; ensemble =
uniform on \(X\) or basin-weighted mixture of \(\mu_a\).

**Observable.** Per-trajectory time average of party occupancy vs ensemble
mean; agreement indicator with \(\Phi\) verdict.

**Ergodicity test.** EoA: for each trajectory,
\(|\bar f_N - \mathbb{E}[f]| > \varepsilon_{\mathrm{div}}\) counts as fail.
EoD optional secondary (histogram of occupancy vs ensemble).

**Statistic / threshold.** Agreement rate
\(\mathrm{EoA\text{-}fail}\leftrightarrow\mathrm{triadic}\) (and pass ↔
dyadic) \(\ge 0.7\) across forms, or a one-sided test at \(\alpha=0.05\).

**Controls.** Single-attractor dyadic form (expect EoA pass); multi-attractor
form with known basin split (expect EoA fail from mixed starts).

**Expected under theories.** T8: agreement above threshold. Chance agreement
refutes.

**Cost.** Seconds beyond Exp-B. **Runnable now:** yes.

**Status (G2 cell).** Run — `studies/ergodic_eoa_vs_phi/`. Verdict
`EOA_AGREES_PHI` on the nine-form panel (7/9); H2/H3 supported. Misses:
sticky, maj3 (dyadic multi-attractor).

**Status (instrument stress).** Run —
`studies/ergodic_eoa_instrument/`. Reusable instrument in
`ergodicity/eoa.py`. On the pre-registered 42-form panel, agreement
**17/42 (0.405)** — H1 REFUTED; disagreements concentrate in
dyadic×multi (H2 SUPPORTED); verdict `EOA_TRACKS_MI_NOT_PHI`. Does not
rewrite the G2 cell above.

**Status (basin / stationary fix).** Run —
`studies/ergodic_eoa_basin/`. Extends `eoa.py` with `reference_mode ∈
{uniform, basin, stationary}` (uniform unchanged). On the same frozen
42-form panel, basin rescues 20/20 prior dya×multi FPs and stationary
rescues 5/5 single-attractor mismatches; both modes are all-AGREEING
(agree 25/42); binary H3 REFUTED; continuous gap AUC under basin 0.729
(H4 SUPPORTED); noise arm H5 SUPPORTED; verdict
`EOA_BASIN_INCONCLUSIVE`. Does not rewrite the G2 or instrument-stress
cells above.

**Status (settling-time residual).** Run —
`studies/ergodic_settling_time/`. Instrument in `ergodicity/settling.py`
(transient length, time-average convergence T, noisy-chain spectral
gap). On the same frozen 42-form panel, mean transient does not
separate triadic from dyadic (AUC 0.540; H1 REFUTED); Spearman with Φ
ρ=0.051 (H2 REFUTED); controlling for transient does not shrink the
basin-mode gap's association with triadic / Φ (H3 REFUTED); noisy
relaxation AUC 0.338 (H4 REFUTED); confound checks fail (H5 REFUTED);
verdict `SETTLING_NULL`. Does not rewrite the G2, instrument-stress, or
basin cells above.

**Status (gap decomposition).** Run —
`studies/ergodic_gap_decomposition/`. Extends `settling.py` with
attractor-oscillation and pre-cycle path-diversity summaries. On the
same frozen 42-form panel, the residual basin-mode gap–triadic
association is not a fluke (AUC 0.729; bootstrap 95% CI [0.560, 0.862];
permutation p 0.0075; H0 SUPPORTED). Finite-T scaling is ∼1/T (mean
log-log slope −0.976) but party-bit oscillation does not absorb the
link (β ratio 0.985; H1 REFUTED); pre-cycle diversity does not (β ratio
1.163; H2 REFUTED); party vs mediator separation holds (Δ AUC 0.232)
without oscillation mediation (H3 REFUTED); no leave-one-group-out
kills the basin H4 band (H4 REFUTED); recomputed gaps match the
committed CSV (H5 SUPPORTED); verdict `GAP_UNEXPLAINED`. Does not
rewrite the G2, instrument-stress, basin, or settling cells above.

**Status (cycle ordering).** Run —
`studies/ergodic_cycle_ordering/`. Extends `settling.py` with the
finite-T phase remainder and sequence features of party-bit flips
(co-flip synchrony, folded phase lag, lag-1 autocorrelation, Hamming
rate, clump-versus-spread index). On the same frozen 42-form panel the
gap–triadic association again clears the fluke check (AUC 0.7294;
bootstrap 95% CI [0.5600, 0.8624]; permutation p 0.0075; H0 SUPPORTED).
The on-cycle remainder does not match the basin gap (Spearman 0.242266;
H1 REFUTED) and does not track triadic status (AUC 0.5412; H2
REFUTED). Residualizing on that prediction leaves the logistic
coefficient in place (β ratio 0.997633; H3 REFUTED). At T=64 every
attractor period on the panel falls in {1, 2, 3, 4, 5}, so the
order index and order excess are constant at 0 (H4a, H4b REFUTED).
The T-independent ordering features and the amplitude controls,
including `party_osc_frac` at β ratio 0.984862, likewise fail the shrink
rule. Descriptive minimum is the all-start remainder (β ratio 0.741270),
which still misses 0.50. Verdict `ORDERING_NULL`. Does not rewrite the
G2, instrument-stress, basin, settling, or gap-decomposition cells
above.

---

## Exp-H — Ensemble vs time-average RL renderings (Strand H / T9)

**Hypothesis.** Small agents trained under ensemble reward vs time-average
reward, when their induced couplings are rendered as Boolean forms, produce
different \(\Phi_{\mathrm{MIP}}\) / major-complex distributions (H2).

**Model / data.** Minimal triadic co-adaptation loop (user, recommender,
counterpart) with two training objectives; thresholded / Booleanized
coupling matrices as lab forms.

**Observable.** Whole-form verdict rates; core membership of the recommender
bit.

**Ergodicity test.** Indirect: compare structural Φ verdicts of the two
rendered populations. Optional EoA on simulated user reward under each
policy.

**Statistic / threshold.** Triadic rate differs by \(\ge 0.2\) between
objective classes on a panel of \(\ge 20\) seeds, or cores differ in
recommender membership rate by the same margin.

**Controls.** Frozen recommender (skew-product restore, links Exp-A);
identical random seeds across objectives.

**Expected under theories.** T9: time-average objective shifts verdict or
core. Identical distributions refute.

**Cost.** Simulation + Φ classification; hours. **Runnable now:** partial —
needs a rendering convention before Φ; defer full cell, specify interface
only.

---

## Exp-I — Literacy instruments assume EoA (Strand I / T10)

**Hypothesis.** Named literacy instruments require exchangeability / EoA of
person-level observables with a population measure (I1); cross-sectional
algorithmacy scores show low concordance with within-person trajectory
metrics on the same cohort (I2).

**Model / data.** Psychometric review of common literacy instruments
(assumptions extraction); survey-arm cohort with repeated within-person
platform-task measures.

**Observable.** Documented exchangeability assumptions; concordance
(correlation / ICC) between cross-section and trajectory scores.

**Ergodicity test.** Review-level for I1; EoA on learner platform logs for I3
diagnostic.

**Statistic / threshold.** I1: \(\ge 3\) named instruments explicitly or
implicitly require EoA. I2: concordance \(< 0.4\) while trajectory predicts
platform outcomes better than cross-section by a pre-registered margin.

**Controls.** An explicitly idiographic instrument (expect no EoA
assumption); null outcome model.

**Expected under theories.** T10 education clause. High concordance refutes
I2.

**Cost.** Review: low. Empirical: survey-arm logistics. **Runnable now:**
review half only; empirical deferred to survey arm.

---

## Exp-J — Triadic teams and trajectory divergence (Strand J / T10)

**Hypothesis.** Teams rendered triadic under the lab field protocol show
larger within-team time–ensemble divergence on coordination observables than
dyadic-rendered teams (J2).

**Model / data.** Field packet → Boolean render → \(\Phi_{\mathrm{MIP}}\);
paired repeated within-team trajectory measures (commits, PRs, dispatches, or
Wageman-style repeated W).

**Observable.** Team-level EoA failure rate; association with Φ verdict.

**Ergodicity test.** EoA on named coordination observables; optional EoD.

**Statistic / threshold.** Divergence rate higher for triadic than dyadic by
a pre-registered margin (or one-sided test \(\alpha=0.05\)).

**Controls.** Text-like units (static process docs) as EoA-pass baselines;
instrument control on known forms before rendering.

**Expected under theories.** T10 organizational clause; links to T2/T8.
No association refutes.

**Cost.** Field collection + render. **Runnable now:** no — needs field
logs; packet machinery exists (`HANDOFF_PACKETS.md`) but no new panel in this
PR.

---

## Runnable-now priority

| Exp | Strand | Runnable now | Study home |
| --- | --- | --- | --- |
| Exp-B | B | **yes — first cell** | `studies/ergodic_components_vs_phi/` |
| Exp-A | A | yes | `studies/ergodic_backcoupling_twins/` |
| Exp-D | D | yes | `studies/ergodic_absorbing_ejection/` |
| Exp-E | E | yes (with B) | folded into first cell + E4 report |
| Exp-F | F | yes | `studies/ergodic_sticky_returns/` |
| Exp-G | G | yes | `studies/ergodic_eoa_vs_phi/` + `studies/ergodic_eoa_instrument/` + `studies/ergodic_eoa_basin/` + `studies/ergodic_gap_decomposition/` + `studies/ergodic_settling_time/` + `studies/ergodic_cycle_ordering/` |
| Exp-C | C | simulation only | deferred (no calibrated series in PR) |
| Exp-H | H | partial | deferred pending render convention |
| Exp-I | I | review only | deferred empirical |
| Exp-J | J | no | deferred to field arm |

Cells marked runnable now are the ones this PR implements and registers under
`ci/reproduce.json`. Deferred cells keep their design above so later PRs can
freeze hypotheses without redesigning the claim.
