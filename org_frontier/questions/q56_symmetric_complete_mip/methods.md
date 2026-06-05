# Q56 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Reuse Q55: `discriminator_utils.py` (ceiling panel, below/ceiling split, rules lookup).
- Reuse Q49: `seam.py` (`mip_ties`, `seam_set`, `coupling_degree`).
- Reuse Q54: `mechanism_utils.py` (topology application, instrument control).
- Q56 extensions: `mip_geometry_utils.py` (directional symmetry, at-system-Phi partition scan,
  minimum-normalized-phi tie prediction).
- Verdict / Phi: `org_frontier/classifier/classifier.py`, `org_frontier/probes/lib.py`, PyPhi
  `new_big_phi.system_partitions` and `evaluate_partition`.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## Ceiling bijective parity panel
- Source: thirty-two ceiling pairs from Q55 (sixteen symmetric, sixteen aligned one-sided) on eight matched
  implication forms with six bijective parity topologies.
- Symmetric subset: `symmetric_xor`, `symmetric_xnor` (sixteen pairs).
- One-sided aligned subset: the sixteen ceiling pairs with `worker_xor`, `counterpart_xor`, `worker_xnor`, or
  `counterpart_xnor` that reach Phi=2.0 per Q55 #175.

## Partition-type vocabulary
- Outer-party two-part: `2 parts: {W,SC}` (W singleton seam), `2 parts: {WS,C}` (C singleton seam).
- Complete: `3 parts: {W,S,C}`.
- Official tie set: first-line partition reprs from `sia.ties` at the max-Phi reachable state (`mip_ties`).

## H1 test — complete-only tie set on symmetric pairs
- **Ensemble:** sixteen symmetric bijective ceiling pairs.
- **Measure:** official tie set from `mip_ties`; count of two-part outer-party entries.
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if all sixteen symmetric ceiling pairs have official tie set exactly
  `['3 parts: {W,S,C}']` with zero two-part outer-party entries. H1 refuted if any symmetric pair includes
  a two-part outer-party partition in ties. H1 partial if fifteen of sixteen match.
- **Script:** `probe_complete_only_tie.py`

## H2 test — one outer-party tie plus complete on one-sided pairs
- **Ensemble:** sixteen aligned one-sided bijective ceiling pairs.
- **Measure:** official tie set; count of outer-party two-part entries; presence of complete partition.
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if all sixteen one-sided ceiling pairs have official tie set of size two
  containing exactly one of `{W,SC}` or `{WS,C}` plus `{W,S,C}`. H2 refuted if any pair has zero or two
  outer-party entries or lacks complete. H2 partial if fifteen of sixteen match.
- **Script:** `probe_one_sided_outer_tie.py`

## H3 test — directional coupling symmetry
- **Ensemble:** sixteen symmetric and sixteen one-sided ceiling pairs (thirty-two total).
- **Measure:** directional symmetry flag — for each party, in-degree equals out-degree in `cm_from_rules`,
  and W out/in equals C out/in.
- **Controls:** instrument control.
- **Decision rule:** H3 confirmed if sixteen of sixteen symmetric pairs are directionally symmetric and zero
  of sixteen one-sided pairs are. H3 refuted if any symmetric pair fails or any one-sided pair passes. H3
  partial if one crossover occurs.
- **Script:** `probe_directional_symmetry.py`

## H4 test — dual outer-party at system Phi, excluded from official ties
- **Ensemble:** sixteen symmetric bijective ceiling pairs.
- **Measure:** for each partition type among `{W,SC}`, `{WS,C}`, `{S,WC}`, `{W,S,C}`, whether any cut
  achieves system Phi (`evaluate_partition` phi within 1e−6 of `sia.phi`); official tie set membership.
- **Controls:** instrument control.
- **Decision rule:** H4 confirmed if all sixteen symmetric pairs have both `{W,SC}` and `{WS,C}` at system
  Phi and zero outer-party entries in official ties. H4 refuted if any symmetric pair lacks both at-system
  outer-party types or has an outer-party entry in official ties.
- **Script:** `probe_dual_outer_excluded.py`

## H5 test — minimum normalized-phi tie-break rule
- **Ensemble:** all thirty-two ceiling bijective parity pairs.
- **Measure:** for each partition type at system Phi, the minimum `normalized_phi` from
  `evaluate_partition`; predicted tie set = types achieving the global minimum; compare to official tie set.
- **Controls:** instrument control; canonical triad as conjunctive tie-set baseline from Q49 #140.
- **Decision rule:** H5 confirmed if predicted tie set equals official tie set on all thirty-two pairs.
  H5 refuted if any pair mismatches. H5 partial if thirty-one of thirty-two match.
- **Script:** `probe_min_norm_tiebreak.py`
