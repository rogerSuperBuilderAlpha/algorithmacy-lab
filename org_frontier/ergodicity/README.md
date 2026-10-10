# Ergodicity × Algorithmacy

A research track on when ensemble statistics about coordination transfer to an
individual trajectory — and when they do not. The lab's thesis says dyadic forms
(Φ_MIP = 0) demand literacy and triadic forms (Φ_MIP > 0) demand algorithmacy.
This track asks whether that literacy/algorithmacy cut has an ergodic twin:
whether the driver a person navigates is exogenous and stationary (text-like),
or back-coupled and trajectory-dependent (platform-like).

## Thesis

Navigating a text is a skew-product problem. The reader is driven; the text is
not. Under stationarity, population norms of reading transfer to the individual,
so ensemble ≈ time average for the observables literacy cares about. Navigating a
platform is not that problem. The platform's state depends on the user's
trajectory: recommendations, visibility, reputation, and eligibility update as a
function of what the user did. The skew-product structure breaks. Stationarity
fails. Ensemble metrics — A/B tests, platform-wide averages, cohort success rates —
stop describing individual time averages. Algorithmacy is the competence that
non-ergodic, back-coupled mediation demands. Literacy is the competence that
ergodic, exogenous drivers demand.

The claim is a candidate formal criterion, not a settled theorem. Non-ergodicity
(or loss of skew-product structure) may mark when literacy suffices and when
algorithmacy is required. The agenda below develops that criterion across ten
strands, from formal distinctions through computable Φ studies to field
instruments.

## Why this belongs in the lab

The lab already computes exact IIT-4.0 Φ on finite Boolean coordination forms.
Those forms are deterministic maps on a finite state space. Their invariant
measures sit on attractors; the ergodic components are attractors and their
basins. Triadic forms (Φ_MIP > 0) and dyadic forms (Φ_MIP = 0) can therefore be
compared on basin structure, number of ergodic components, and whether
party-level time averages match ensemble averages — with existing code
(`studies/genuine_bistability/`, the classifier, the corpus). That comparison is
the first cell of the track. No result is reported here; the cell is specified so
hypotheses can be fixed before any run.

The track also reaches the lab's empirical arms. Operational Equality-of-
Distributions / Equality-of-Averages tests on platform or organizational logs are
candidate instruments for classifying an environment as text-like or
platform-like, and they sit next to the fielded Wageman work and the survey arm's
idiographic measurement problem.

## Scope

- Formal, computational (exact Φ / PyPhi / lab panels), and empirical questions.
- In-silico Φ results are evidence about models, not about real firms. Every
  computational cell states that gap.
- No invented Φ numbers or empirical findings in this track until a registered
  script produces them.
- Φ / IIT are used for causal irreducibility of coordination forms. No claim is
  made that platforms or organizations are conscious.

## Layout

| Path | What it is |
| --- | --- |
| [`AGENDA.md`](AGENDA.md) | Forty research questions in ten strands, each with method and falsifier |
| [`THEORIES.md`](THEORIES.md) | Named falsifiable conjectures (T1–T10) tying the strands |
| [`EXPERIMENTS.md`](EXPERIMENTS.md) | One designed experiment per strand; runnable-now priority |
| [`SOURCES.md`](SOURCES.md) | Verifiable bibliography (working notes + classics + volume papers) |
| [`../studies/ergodic_components_vs_phi/`](../studies/ergodic_components_vs_phi/) | First cell (B1–B3): attractor / basin structure vs Φ_MIP |
| [`../studies/ergodic_ensemble_richness/`](../studies/ergodic_ensemble_richness/) | B5: Φ_MIP vs basin entropy and attractor count on the 256-form census |
| [`../studies/ergodic_backcoupling_twins/`](../studies/ergodic_backcoupling_twins/) | A4: convey vs accumulating twins |
| [`../studies/ergodic_absorbing_ejection/`](../studies/ergodic_absorbing_ejection/) | D4: absorbing ejected mediator |
| [`../studies/ergodic_sticky_returns/`](../studies/ergodic_sticky_returns/) | F4: sticky return times / inactive basins |
| [`../studies/ergodic_eoa_vs_phi/`](../studies/ergodic_eoa_vs_phi/) | G2: operational EoA vs Φ on synthetic logs |
| [`eoa.py`](eoa.py) | Reusable EoA instrument (`run_eoa` / `run_eoa_parties`; `reference_mode ∈ {uniform,basin,stationary}`) |
| [`settling.py`](settling.py) | Settling-time measures (transient length, convergence T, noisy spectral gap) |
| [`../studies/ergodic_eoa_instrument/`](../studies/ergodic_eoa_instrument/) | G stress: instrument + wider panel vs Φ |
| [`../studies/ergodic_eoa_basin/`](../studies/ergodic_eoa_basin/) | G follow-on: basin/stationary reference fix vs Φ |
| [`../studies/ergodic_settling_time/`](../studies/ergodic_settling_time/) | G residual: settling time vs residual basin-mode EoA gap |
| [`../studies/ergodic_gap_decomposition/`](../studies/ergodic_gap_decomposition/) | G residual: decompose residual gap–Φ link (phase / path / observable / panel) |
| [`../essays/ergodicity_and_algorithmacy.md`](../essays/ergodicity_and_algorithmacy.md) | Short essay introducing the crossover |

## Relation to standing arcs

The stoch–temporal arc already showed genuine triadic/dyadic attractor
coexistence (`studies/genuine_bistability/`). This track re-reads that
multistability as ergodic-component structure and asks whether Φ_MIP tracks it.
The political-economy arc modeled rival platforms and extractive ejection; this
track asks the ergodic companion questions about ruin, multiplicative growth, and
ensemble-vs-time-average success. The survey and field arms supply the
operational measurement strand.

## Status

Theories and experiments specified. Computable cells have hypotheses frozen
before analysis scripts; results land only from registered scripts under
`ci/reproduce.json`.
