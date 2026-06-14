# Q50 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Verdict / Φ: `org_frontier/classifier/classifier.py` (`classify_rules`, `cm_from_rules`),
  `org_frontier/probes/lib.py` (`verdict`).
- Strict-mediation family: `org_frontier/corpus/population.py` (`enumerate_family`, 256 forms).
- Party-read indices from family label: `int(label[1])` for W-index, `int(label.split("_C")[1])` for
  C-index; S-index `int(label.split("_S")[1].split("_")[0])`.
- One-input tables (little-endian): index 0 = constant 0, 1 = identity (party'=S), 2 = NOT (party'=¬S),
  3 = constant 1.
- Commit classes: AND=1, OR=7, NOR=8, NAND=14; implication indices {2, 4, 11, 13}; symmetric set
  {1, 7, 8, 14}.
- MIP tie set: PyPhi `new_big_phi.sia(sub).ties`, first line of each tie as in Q49.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## H1 test — matched non-constant reads bind OR
- **Ensemble:** all sixteen OR-commit strict-mediation forms (S-index 7).
- **Measure:** verdict; W-index and C-index; matched-read predicate (iw == ic and iw ∈ {1, 2}).
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if the triadic OR set equals exactly {W1_S7_C1, W2_S7_C2} and every
  form satisfying the matched-read predicate is triadic. H1 refuted if any mismatch.
- **Script:** `probe_or_matched.py`

## H2 test — constant reads exclude OR binding
- **Ensemble:** OR-commit forms with W-index ∈ {0, 3} or C-index ∈ {0, 3} (expect eight forms with
  constant worker, eight with constant counterpart; overlap at W0_C0 etc.).
- **Measure:** verdict; count of triadic rows.
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if zero triadic OR forms have any constant party read. H2 refuted if
  at least one triadic OR form has W-index or C-index in {0, 3}.
- **Script:** `probe_or_constant.py`

## H3 test — asymmetric reads collapse OR
- **Ensemble:** OR-commit forms with W-index ≠ C-index (expect twelve).
- **Measure:** verdict; count of triadic asymmetric forms.
- **Controls:** instrument control.
- **Decision rule:** H3 confirmed if zero asymmetric OR forms are triadic. H3 refuted if at least one
  triadic OR form has W-index ≠ C-index.
- **Script:** `probe_or_asymmetric.py`

## H4 test — binding OR forms share the canonical seam tie
- **Ensemble:** the two triadic OR forms W1_S7_C1 and W2_S7_C2.
- **Measure:** max_phi; structure; seam set from `sia.ties` (parties severed as singletons).
- **Controls:** instrument control seam set and Φ=2.0.
- **Decision rule:** H4 confirmed if both binding OR forms are triadic at Φ=2.0 and their seam sets equal
  the control's seam set (expect {W, C} parties in seam). H4 refuted if either form differs in structure,
  Φ, or seam set.
- **Script:** `probe_or_seam.py`

## H5 test — commit symmetry splits the party-read rule
- **Ensemble:** all sixteen monotone strict-mediation forms at Φ=2.0 (from Q45 H2).
- **Measure:** S-index; W-index and C-index; symmetric-commit predicate; matched vs complementary read
  predicates.
- **Controls:** instrument control (symmetric AND, matched reads).
- **Decision rule:** H5 confirmed if every symmetric-commit triadic form has iw == ic ∈ {1, 2} and every
  implication triadic form has {iw, ic} = {1, 2} with iw ≠ ic, with zero violations. H5 refuted if any
  form crosses the rule.
- **Script:** `probe_commit_symmetry.py`
