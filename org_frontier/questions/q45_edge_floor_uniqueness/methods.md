# Q45 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Verdict / Φ: `org_frontier/classifier/classifier.py` (`classify_rules`, `cm_from_rules`),
  `org_frontier/probes/lib.py` (`verdict`).
- Strict-mediation family: `org_frontier/corpus/population.py` (`enumerate_family`, 256 forms).
- Structural tags: `org_frontier/corpus/forms_library.py` (`structural_tags`).
- Full n=3 wiring space: enumerate 16³ truth-table triples (same loop as `probe_ns_theorem.py`).
- Edge count: `int(cm_from_rules(rules).sum())`.
- S-function index from family label: `int(label.split("_S")[1].split("_")[0])`.
- Commit classes (two-input index, little-endian): AND = 1, XOR = 6, XNOR = 9, OR = 7.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## H1 test — triadic forms sit at the edge floor
- **Ensemble:** all 256 strict-mediation forms; filter to triadic (expect 24).
- **Measure:** edge count per triadic form.
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if every triadic form has edge count 4. H1 refuted if any triadic form
  has count ≠ 4.
- **Script:** `probe_edge_floor.py`

## H2 test — only AND reaches Φ = n−1 at the floor
- **Ensemble:** triadic strict-mediation forms with Φ = 2.0 (expect 16).
- **Measure:** S-function index; count of non-AND max-Φ forms.
- **Controls:** instrument control (AND, Φ=2.0, 4 edges).
- **Decision rule:** H2 confirmed if all max-Φ triadic forms have S-index 1. H2 refuted if any has
  Φ = 2.0 with S-index ≠ 1.
- **Script:** `probe_conjunctive_max.py`

## H3 test — parity saturates its ceiling at the floor
- **Ensemble:** triadic strict-mediation forms with S-index in {6, 9} (expect 8).
- **Measure:** edge count; Φ; deviation from 2^(2−3) = 0.5.
- **Controls:** instrument control as conjunctive baseline.
- **Decision rule:** H3 confirmed if all 8 parity triadic forms have 4 edges and |Φ − 0.5| < 1e−6. H3
  refuted if any parity triadic form misses the ceiling or edge count.
- **Script:** `probe_parity_floor.py`

## H4 test — OR does not bind in strict mediation
- **Ensemble:** all 256 strict-mediation forms with S-index 7 (expect 16).
- **Measure:** verdict; count of triadic OR forms.
- **Controls:** instrument control.
- **Decision rule:** H4 confirmed if zero OR forms are triadic. H4 refuted if at least one OR form is
  triadic.
- **Script:** `probe_or_strict.py`

## H5 test — global 4-edge max-Φ is conjunctive-only
- **Ensemble:** all 4096 n=3 wirings; filter to triadic with edge count exactly 4 and Φ = 2.0 − 1e−9.
- **Measure:** `strict_mediation` and `mediator_reads_both` tags; whether S-truth-table equals AND
  (index 1) up to party relabeling.
- **Controls:** instrument control; count of 16 conjunctive family forms as positive reference.
- **Decision rule:** H5 confirmed if every qualifying form is strict-mediation with AND commit (equivalently:
  matches the conjunctive hub up to W↔C swap). H5 refuted if any 4-edge triadic form has Φ = 2.0 without
  that pattern.
- **Script:** `probe_global_floor.py`
