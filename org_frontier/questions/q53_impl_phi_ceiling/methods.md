# Q53 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Reuse Q51 helpers: `org_frontier/questions/q51_implication_backchannel/backchannel_utils.py`
  (implication indices {2,4,11,13}, matched predicate, party-read indices, instrument control).
- Q53 extensions: `ceiling_utils.py` (topology transforms, gate functions AND/OR/XOR, panel enumeration).
- Verdict / Φ: `org_frontier/classifier/classifier.py`, `org_frontier/probes/lib.py`.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Back-channel topologies (deterministic n=3 Boolean gates)
On rules list [W', S', C'] with old party functions preserved on the non-channel side:
- **worker_and:** W' = old_W & C (Q51 worker_backchannel).
- **counterpart_and:** C' = old_C & W.
- **symmetric_and:** both AND gates (Q51 symmetric_backchannel).
- **worker_or:** W' = old_W | C.
- **counterpart_or:** C' = old_C | W.
- **symmetric_or:** both OR gates.
- **cross_wor_cand:** W' = old_W | C, C' = old_C & W.
- **cross_wand_cor:** W' = old_W & C, C' = old_C | W.
- **worker_xor / counterpart_xor / symmetric_xor:** same pattern with XOR (^) gate.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## H1 test — counterpart-side AND ceiling
- **Ensemble:** eight matched-read implication strict-mediation forms with counterpart_and transform.
- **Measure:** verdict; max_phi; count at Φ=2.0 (tolerance 1e−6).
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if ≥1 at ceiling. H1 refuted if zero at ceiling. H1 partial if some
  triadic but all below 2.0.
- **Script:** `probe_counterpart_and_ceiling.py`

## H2 test — OR-graded worker-side ceiling
- **Ensemble:** eight matched-read implication forms with worker_or transform.
- **Measure:** verdict; max_phi; count at Φ=2.0.
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if ≥1 at ceiling. H2 refuted if zero. H2 partial if triadic but below 2.0.
- **Script:** `probe_worker_or_ceiling.py`

## H3 test — XOR gates vs 0.830075
- **Ensemble:** eight matched-read implication forms × three XOR topologies (worker, counterpart, symmetric).
- **Measure:** max_phi per pair; count exceeding SYMMETRIC_EQ=0.830075.
- **Controls:** instrument control; symmetric-AND baseline from Q51 #159.
- **Decision rule:** H3 confirmed if ≥1 pair exceeds 0.830075 + 1e−6. H3 refuted if none exceed. H3 partial
  if any triadic but none above equilibrium.
- **Script:** `probe_xor_exceed_equilibrium.py`

## H4 test — full topology sweep for Φ=2.0
- **Ensemble:** eight matched forms × eight topologies {worker_and, counterpart_and, symmetric_and,
  worker_or, counterpart_or, symmetric_or, cross_wor_cand, cross_wand_cor} = 64 pairs.
- **Measure:** count at Φ=2.0; list any hits.
- **Controls:** instrument control.
- **Decision rule:** H4 confirmed if zero at ceiling across 64 pairs. H4 refuted if ≥1 at ceiling. H4
  partial if near-ceiling (≥1.9) but none at 2.0.
- **Script:** `probe_topology_sweep_phi2.py`

## H5 test — supremum characterization
- **Ensemble:** same 64 pairs as H4 plus three XOR topologies × eight forms = 24 additional pairs (88 total).
- **Measure:** global max_phi; argmax topology and label; symmetric-AND panel spread.
- **Controls:** instrument control; Q52 SYMMETRIC_EQ=0.830075.
- **Decision rule:** H5 confirmed if global max within 1e−6 of 0.830075 AND symmetric-AND has eight of eight
  at 0.830075 with spread < 1e−6. H5 refuted if any pair exceeds 0.830075 + 1e−6. H5 partial if max equals
  0.830075 but symmetric-AND panel not uniform.
- **Script:** `probe_supremum_characterization.py`
