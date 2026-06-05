# Q51 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Verdict / Φ: `org_frontier/classifier/classifier.py` (`classify_rules`, `cm_from_rules`),
  `org_frontier/probes/lib.py` (`verdict`).
- Strict-mediation family: `org_frontier/corpus/population.py` (`enumerate_family`, 256 forms).
- Party-read indices: `int(label[1])` for W-index, `int(label.split("_C")[1])` for C-index; S-index
  `int(label.split("_S")[1].split("_")[0])`.
- Implication commit indices: {2, 4, 11, 13} (from Q50).
- Matched-read predicate: W-index = C-index ∈ {1, 2}. Complementary predicate: {W-index, C-index} = {1, 2}
  with W-index ≠ C-index.
- Back-channel transforms (on rules list [W', S', C']):
  - **Worker-side minimal:** W' becomes `lambda x, ow=old_W: ow(x) & x[2]` (adds C→W edge).
  - **Symmetric two-sided:** W' as above plus C' becomes `lambda x, oc=old_C: oc(x) & x[0]`.
- Edge count: sum of `cm_from_rules(rules)` (directed connectivity matrix).
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## H1 test — matched implication binds at Φ=2.0 with worker back-channel
- **Ensemble:** eight matched-read implication strict-mediation forms with worker-side back-channel.
- **Measure:** verdict; max_phi; count at Φ=2.0 (tolerance 1e-6).
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if at least one form is triadic with max_phi ≥ 2.0 − 1e−9. H1 refuted if
  zero reach the ceiling. H1 partial if some triadic but all below 2.0.
- **Script:** `probe_impl_phi2_matched.py`

## H2 test — worker back-channel enables triadic binding for most matched forms
- **Ensemble:** same eight matched-read implication forms with worker-side back-channel.
- **Measure:** verdict; count triadic (Φ>0).
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if ≥6 of 8 are triadic. H2 refuted if <6. H2 partial if 1–5 triadic.
- **Script:** `probe_impl_triadic_matched.py`

## H3 test — strict mediation control
- **Ensemble:** eight matched-read implication forms without back-channel (strict mediation).
- **Measure:** verdict; count triadic.
- **Controls:** instrument control.
- **Decision rule:** H3 confirmed if zero triadic. H3 refuted if ≥1 triadic.
- **Script:** `probe_impl_strict_control.py`

## H4 test — back-channel preserves complementary implication at Φ=2.0
- **Ensemble:** eight complementary-read implication strict-mediation forms, each with worker-side
  back-channel (baseline: all triadic at Φ=2.0 without back-channel per Q50).
- **Measure:** verdict; max_phi per form; count at Φ=2.0.
- **Controls:** instrument control; strict-mediation complementary baseline (all Φ=2.0).
- **Decision rule:** H4 confirmed if all eight stay triadic at max_phi ≥ 2.0 − 1e−9. H4 refuted if any drop
  below ceiling or become dyadic. H4 partial if all triadic but some below 2.0.
- **Script:** `probe_impl_complementary_preserve.py`

## H5 test — symmetric two-sided back-channel unifies matched binding
- **Ensemble:** eight matched-read implication forms with symmetric two-sided back-channel.
- **Measure:** verdict; max_phi; uniqueness of max_phi across triadic forms.
- **Controls:** instrument control.
- **Decision rule:** H5 confirmed if all eight triadic and all max_phi equal within 1e−6. H5 refuted if
  fewer than eight triadic or max_phi differs. H5 partial if eight triadic but Φ not uniform.
- **Script:** `probe_impl_symmetric_unify.py`
