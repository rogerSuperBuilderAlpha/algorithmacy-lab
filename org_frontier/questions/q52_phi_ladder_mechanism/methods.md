# Q52 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Reuse Q51 helpers: `org_frontier/questions/q51_implication_backchannel/backchannel_utils.py`
  (implication indices {2,4,11,13}, matched/complementary predicates, worker and symmetric back-channel
  transforms, party-read indices).
- Q52 extensions: `ladder_utils.py` (commit output at fixed (W,C), W-centric {2,13} vs C-centric
  {4,11}, rung labels, HIGH_PHI=0.830075, MID_PHI=0.415037).
- Verdict / Φ: `org_frontier/classifier/classifier.py`, `org_frontier/probes/lib.py`.
- Commit truth tables: `org_frontier/corpus/population.py` (`_two_input_tables`).
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## H1 test — W-centric party-read polarity rule
- **Ensemble:** four matched-read implication forms with s∈{2,13} and one-sided worker back-channel.
- **Measure:** S'(1,0) from commit table; party-read index iw; verdict; max_phi; predicted rung via
  `S'(1,0) != (iw==2)` → high else dyadic.
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if zero mismatches between predicted and observed rung across four
  forms. H1 refuted if ≥1 mismatch. H1 partial if rule holds for one commit index only.
- **Script:** `probe_wcentric_polarity.py`

## H2 test — C-centric mid plateau (matched)
- **Ensemble:** four matched-read implication forms with s∈{4,11} and one-sided worker back-channel.
- **Measure:** verdict; max_phi; distance from MID_PHI.
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if all four triadic and |max_phi − 0.415037| < 1e−6. H2 refuted if any
  dyadic or high-rung. H2 partial if triadic but Φ deviates.
- **Script:** `probe_ccentric_plateau.py`

## H3 test — mid rung across party-read pairing
- **Ensemble:** eight implication forms with s∈{4,11} (four matched, four complementary) under one-sided
  worker back-channel.
- **Measure:** verdict; max_phi; count at MID_PHI.
- **Controls:** instrument control.
- **Decision rule:** H3 confirmed if eight of eight triadic at 0.415037. H3 refuted if <8 at mid or any
  dyadic. H3 partial if all triadic but not all at 0.415037.
- **Script:** `probe_mid_invariant.py`

## H4 test — symmetric lift of dyadic W-centric forms
- **Ensemble:** W1_S13_C1 and W2_S2_C2 (one-sided dyadic under Q51 #156) with symmetric two-sided
  back-channel.
- **Measure:** verdict; max_phi vs HIGH_PHI.
- **Controls:** instrument control; one-sided baseline (both dyadic).
- **Decision rule:** H4 confirmed if both triadic and |max_phi − 0.830075| < 1e−6. H4 refuted if either
  dyadic or below high rung. H4 partial if triadic but below 0.830075.
- **Script:** `probe_symmetric_lift.py`

## H5 test — symmetric collapse to high-rung equilibrium
- **Ensemble:** all eight matched-read implication forms with symmetric two-sided back-channel.
- **Measure:** verdict; max_phi; range and std across panel.
- **Controls:** instrument control; one-sided spread baseline from Q51 (#156).
- **Decision rule:** H5 confirmed if eight of eight triadic and max_phi range < 1e−6 (all 0.830075). H5
  refuted if fewer than eight triadic or range ≥ 1e−6. H5 partial if uniform but not at 0.830075.
- **Script:** `probe_symmetric_collapse.py`
