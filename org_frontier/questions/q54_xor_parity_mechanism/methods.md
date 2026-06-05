# Q54 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Reuse Q53: `ceiling_utils.py` (topology transforms, matched implication panel, gate ops).
- Q54 extensions: `mechanism_utils.py` (gate bijectivity, TPM permutation test, seam conditional
  entropy, XNOR topologies, commit-class labels).
- Verdict / Φ: `org_frontier/classifier/classifier.py`, `org_frontier/probes/lib.py`.
- Information measures: `org_frontier/probes/_info.py` on reachable-state trajectories.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## Gate and topology panel
- Monotone topologies: eight from Q53 `TOPOLOGY_SWEEP` (AND/OR/cross).
- Parity topologies: `worker_xor`, `counterpart_xor`, `symmetric_xor` plus Q54 `symmetric_xnor`.
- Matched implication ensemble: eight forms with s ∈ {2,4,11,13} and matched live party reads.
- Commit classes: W-centric {2,13}, C-centric {4,11}.

## H1 test — channel-gate bijectivity
- **Ensemble:** all 88 (topology, form) pairs from Q53 panel plus three XNOR topologies × eight forms.
- **Measure:** bijective-in-coupled-bit flag per channel edge; max_phi; count at Φ=2.0.
- **Controls:** instrument control; gate truth tables for AND/OR/XOR/XNOR on {0,1}².
- **Decision rule:** H1 confirmed if every Φ=2.0 pair has all channel gates bijective AND zero non-bijective
  pairs reach ceiling. H1 partial if all Φ=2.0 bijective but some bijective pairs stay below ceiling. H1
  refuted if any Φ=2.0 pair is non-bijective or any non-bijective pair hits ceiling.
- **Script:** `probe_gate_bijectivity.py`

## H2 test — TPM permutation
- **Ensemble:** Φ=2.0 pairs from XOR panel (symmetric_xor, aligned one-sided XOR) vs symmetric-AND panel
  at 0.830075 on all eight matched forms.
- **Measure:** `tpm_is_permutation(rules)` on full eight-state transition map.
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if all Φ=2.0 pairs permutation and zero symmetric-AND pairs permutation.
  H2 partial if all Φ=2.0 permutation but some symmetric-AND also permutation. H2 refuted if any Φ=2.0
  pair non-permutation.
- **Script:** `probe_tpm_permutation.py`

## H3 test — seam conditional entropy
- **Ensemble:** symmetric_xor (Φ=2.0) vs symmetric_and (0.830075) on eight matched forms.
- **Measure:** H(W,C|S) = H(W,S,C) − H(S) over uniform distribution on reachable states from trajectory
  enumeration.
- **Controls:** instrument control.
- **Decision rule:** H3 confirmed if mean H(W,C|S) for symmetric_xor strictly exceeds symmetric_and mean.
  H3 refuted if difference ≤ 0. H3 partial if XOR mean higher on majority of forms but not on mean.
- **Script:** `probe_seam_entropy.py`

## H4 test — commit-topology alignment
- **Ensemble:** eight matched forms × {worker_xor, counterpart_xor, symmetric_xor}.
- **Measure:** max_phi; alignment flag (worker_xor ↔ C-centric, counterpart_xor ↔ W-centric).
- **Controls:** instrument control; Q52 commit-class split.
- **Decision rule:** H4 confirmed if zero misaligned one-sided Φ=2.0 hits and eight of eight symmetric_xor
  at ceiling. H4 refuted if any misalignment or symmetric miss. H4 partial if alignment holds but symmetric
  below eight.
- **Script:** `probe_commit_alignment.py`

## H5 test — parity-class necessity
- **Ensemble:** eight monotone topologies × eight forms (64 pairs) plus symmetric_xnor × eight forms.
- **Measure:** count at Φ=2.0; symmetric_xnor ceiling hits vs symmetric_xor baseline.
- **Controls:** instrument control; Q53 #168 monotone sweep.
- **Decision rule:** H5 confirmed if zero monotone pairs at ceiling AND symmetric_xnor reaches Φ=2.0 on all
  eight forms. H5 refuted if any monotone hits ceiling. H5 partial if monotone zero but XNOR below eight.
- **Script:** `probe_parity_necessity.py`
