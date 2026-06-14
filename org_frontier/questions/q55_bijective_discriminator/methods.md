# Q55 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Reuse Q54: `mechanism_utils.py` (parity panel, bijectivity flags, seam entropy, commit classes).
- Q55 extensions: `discriminator_utils.py` (below/ceiling split, XOR/XNOR alignment predicates, MIP first line).
- Verdict / Φ: `org_frontier/classifier/classifier.py`, `org_frontier/probes/lib.py`.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## Bijective parity panel
- Topologies: six parity topologies from Q54 (`worker_xor`, `counterpart_xor`, `symmetric_xor`,
  `worker_xnor`, `counterpart_xnor`, `symmetric_xnor`) × eight matched implication forms.
- Filter: `channel_bijective == True` (forty-eight pairs total: sixteen below, thirty-two ceiling per Q54 #170).
- Commit classes: W-centric {2,13}, C-centric {4,11}.
- Mid rung reference: 0.415037 (Q52 #161–#162).

## H1 test — misaligned one-sided partition
- **Ensemble:** forty-eight bijective parity (topology, form) pairs.
- **Measure:** below vs ceiling flag; one-sided vs symmetric; XOR/XNOR misalignment flag.
- **Controls:** instrument control; Q54 #173 alignment definition extended to XNOR inversion in H5.
- **Decision rule:** H1 confirmed if all sixteen below are misaligned one-sided and zero below are symmetric
  or aligned one-sided. H1 refuted if any below pair is symmetric or aligned. H1 partial if all below are
  one-sided misaligned but count differs from sixteen.
- **Script:** `probe_misaligned_partition.py`

## H2 test — uniform mid-rung Phi
- **Ensemble:** same forty-eight bijective parity pairs.
- **Measure:** max_phi; spread within below and ceiling subsets.
- **Controls:** instrument control; Q52 mid rung constant.
- **Decision rule:** H2 confirmed if every below pair has max_phi within 1e−6 of 0.415037 and every ceiling
  pair within 1e−6 of 2.0. H2 refuted if any below differs from 0.415037 or any ceiling below 2.0 − 1e−9.
- **Script:** `probe_mid_rung_uniform.py`

## H3 test — seam entropy split
- **Ensemble:** same forty-eight bijective parity pairs.
- **Measure:** H(W,C|S) over reachable-state trajectories; subset means for below vs ceiling.
- **Controls:** instrument control; Q54 seam entropy method.
- **Decision rule:** H3 confirmed if mean H below strictly less than mean H ceiling. H3 refuted if difference
  ≤ 0. H3 partial if direction holds pair-wise on a majority but mean gap non-positive.
- **Script:** `probe_seam_entropy_split.py`

## H4 test — MIP singleton {S,WC}
- **Ensemble:** same forty-eight bijective parity pairs.
- **Measure:** first line of MIP partition string from exact Φ verdict.
- **Controls:** instrument control.
- **Decision rule:** H4 confirmed if sixteen of sixteen below show `2 parts: {S,WC}` and zero of thirty-two
  ceiling show that partition. H4 refuted if any below differs or any ceiling matches `{S,WC}`. H4 partial
  if below uniform but one ceiling exception.
- **Script:** `probe_mip_singleton.py`

## H5 test — XNOR alignment inversion
- **Ensemble:** one-sided XNOR and XOR topologies on eight matched forms (sixteen pairs each, thirty-two
  one-sided parity pairs total).
- **Measure:** max_phi; inverted alignment flag for XNOR (worker_xnor ↔ W-centric, counterpart_xnor ↔
  C-centric); standard alignment for XOR ceiling hits.
- **Controls:** instrument control; Q54 #173 XOR alignment baseline.
- **Decision rule:** H5 confirmed if zero XNOR ceiling misalignments under inverted rule AND every aligned
  XOR one-sided pair reaches Φ=2.0. H5 refuted if any XNOR ceiling violates inverted alignment. H5 partial
  if XNOR rule holds but XOR aligned count below sixteen.
- **Script:** `probe_xnor_alignment_flip.py`
