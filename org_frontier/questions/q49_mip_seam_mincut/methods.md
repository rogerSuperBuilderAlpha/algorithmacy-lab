# Q49 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules), the measure, the controls, and the decision rule
fixed before the run. A reader reproduces every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `org_frontier/classifier/classifier.py` (`classify_rules`,
  `tpm_from_rules`, `cm_from_rules`), `org_frontier/probes/lib.py` (`verdict`).
- Family enumeration: `org_frontier/corpus/population.py` (`enumerate_family`, the 256 strict-mediation
  n=3 forms: W' = f_W(S), S' = f_S(W,C), C' = f_C(S)).
- Exact MIP and tie set: `pyphi.new_big_phi.sia`, read at the max-Φ reachable state.
- Python: the repo `venv` (PyPhi IIT-4.0 line). All forms n=3, deterministic Boolean, little-endian
  `x[0]=W, x[1]=S, x[2]=C`.

## Reading the seam (the measure used throughout)
For a form, classify it to find the max-Φ reachable state `s*` (`classify_rules(...).mip_state`). Build the
PyPhi subsystem at `s*` and take `sia = new_big_phi.sia(sub)`. The tie set `sia.ties` is the set of
partitions achieving the system Φ. Each tied partition's first repr line is a cut such as
`2 parts: {W,SC}` or `3 parts: {W,S,C}`. The **seam set** is the set of parties severed as a singleton by
some tied two-part partition: for n=3 every two-part partition is a 1+2 split, so `{W,SC}` contributes W,
`{WS,C}` contributes C, `{S,WC}` contributes S. A tie set containing only the complete partition
`{W,S,C}` gives an empty seam set. The seam-reading helper is `seam.py` (`seam_set`, `mip_ties`), reused
by every probe.

## Instrument control (run first)
The canonical strict-mediation triad, `W'=S`, `S'=W∧C`, `C'=S` (rules `[x[1], x[0]&x[2], x[1]]`, labels
`("W","S","C")`), is the established triad (#57, #26). It must reproduce `triadic` at max_phi = 2.0 with
the reported MIP `2 parts: {W,SC}` before any seam comparison is trusted. If it does not, halt.

## H1 test — the canonical seam is a tie
- **Form:** the canonical triad above.
- **Measure:** `sia.ties` at the max-Φ state; the system Φ of each tied partition; the seam set.
- **Controls:** instrument control (same form). Baseline under H0 is a singleton tie set `{W,SC}`.
- **Decision rule (fixed before run):** H1 confirmed if the tie set contains both a `{W,SC}` and a
  `{WS,C}` two-part partition at the system Φ (seam set ⊇ `{W, C}`) and not `{S,WC}`. H1 refuted if `{W,SC}`
  is the unique MIP (seam set `{W}`).
- **Script:** `probe_seam_tie.py`

## H2 test — no triadic strict-mediation form has a worker-unique seam
- **Ensemble:** all 256 strict-mediation forms from `enumerate_family()`, filtered to the triadic ones
  (expected 24, matching #33).
- **Measure:** for each triadic form, the seam set; the indicator `{W ∈ seam} == {C ∈ seam}`.
- **Controls:** instrument control. Count of triadic forms checked against the known 24 (#33).
- **Decision rule:** H2 confirmed if every triadic form has `W ∈ seam ⇔ C ∈ seam` (zero forms sever W
  alone). H2 refuted if at least one triadic form has W in the seam set and C not.
- **Script:** `probe_seam_family.py`

## H3 test — a one-sided back-channel breaks the seam tie
- **Form:** worker-side back-channel `W'=S∧C`, `S'=W∧C`, `C'=S` (rules `[x[1]&x[2], x[0]&x[2], x[1]]`).
  This adds the edge C→W to the canonical triad (#24).
- **Measure:** verdict and max_phi (must stay triadic); the seam set; the number of distinct
  singleton-severing parties in the tie set.
- **Controls:** instrument control (canonical triad, seam set `{W, C}` from H1) as the symmetric baseline.
- **Decision rule:** H3 confirmed if the form is triadic (max_phi ≥ 2.0 − 1e−9) and its seam set is a
  single party (tie broken). H3 refuted if the seam set stays `{W, C}`. If the form is dyadic the premise
  fails and the test is void (reported as such).
- **Script:** `probe_seam_break.py`

## H4 test — the broken seam follows the read direction
- **Panel (all n=3):**
  worker-side channel `W'=S∧C` → `[x[1]&x[2], x[0]&x[2], x[1]]`;
  counterpart-side channel `C'=S∧W` → `[x[1], x[0]&x[2], x[1]&x[0]]`;
  symmetric two-sided channel `W'=S∧C, C'=S∧W` → `[x[1]&x[2], x[0]&x[2], x[1]&x[0]]`.
- **Measure:** verdict; seam set for each panel form.
- **Controls:** instrument control; the canonical triad as the symmetric baseline (`{W, C}`).
- **Decision rule:** H4 confirmed if the worker-side channel gives seam `{C}`, the counterpart-side
  channel gives seam `{W}`, and the symmetric channel gives seam `{W, C}`. H4 refuted if any panel form's
  seam falls on the party that gained the incoming read, or the symmetric form does not restore the tie.
- **Script:** `probe_seam_direction.py`

## H5 test — the seam is not the connectivity min-cut
- **Ensemble:** the H4 asymmetric panel (worker-side and counterpart-side channels) plus the 8 parity
  (XOR/XNOR commit) triadic forms from the strict-mediation family.
- **Measure:** the Φ-seam set (above) and the connectivity min-cut singleton set, defined from
  `cm_from_rules`: for each party X, `cut(X) = Σ_{j≠X} cm[X,j] + cm[j,X]`; the min-cut set is
  `argmin_X cut(X)`. Compare the two on each form.
- **Controls:** instrument control. The canonical triad, where both sets are `{W, C}` (agreement), is the
  positive control for the comparison.
- **Decision rule:** H5 confirmed (H0 refuted) if the two sets disagree on at least one form: on the
  asymmetric panel the min-cut returns `{W, C}` while the Φ-seam is a single party, and on the parity
  forms the Φ-seam set is empty (complete-partition MIP) while the min-cut returns a singleton. H5 refuted
  if the Φ-seam set equals the min-cut set on every form.
- **Script:** `probe_seam_mincut.py`
