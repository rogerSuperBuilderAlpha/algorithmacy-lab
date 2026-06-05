# Q43 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

All forms are built as deterministic Boolean dynamical systems. Each party's next state is a fixed
function of the current node-state tuple `x` (little-endian: `x[0]` is the first party). Labels follow
the classifier default: `W` worker, `S` system/mediator, `C` counterpart, `C1, C2, …` further parties.
The matched triple holds the node count and the determination family fixed: every form below uses AND
of the relevant inputs (`&`), node count 3 unless a size sweep is named, and the same little-endian
encoding.

## Shared infrastructure
- Verdict / Φ / major complex: `org_frontier/classifier/classifier.py` (`classify_rules`,
  `tpm_from_rules`, `cm_from_rules`), `org_frontier/probes/lib.py` (`verdict`, `major_complex`,
  `max_phi_float`).
- Information measures: `org_frontier/probes/_info.py` (entropy, mutual_information, transfer_entropy,
  o_information).
- Exact Φ / trajectories: `proxy_audit/exact_phi.py`.
- Python: `~/iit-playground/venv-4.0/bin/python`.
- The verdict is the binary structure (`dyadic` vs `triadic`) read off `Φ_MIP` over the most-integrated
  reachable state, with `PHI_EPS = 1e-9` the zero threshold. Φ magnitude is reported as an ordinal hint
  only, per the classifier docstring.

## Instrument control (run first)
The pass-through mediator chain at n=3, `W' = S`, `S' = W & C`, `C' = S` (rules
`[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`, labels `("W","S","C")`), is the established
triad (#57). It must reproduce `triadic` at `max_phi = 2.0` with MIP `2 parts: {W,SC}` before any
comparison verdict in this question is trusted. If it does not, halt and do not read the test forms.
This same form is the H1 chain and the H3 propagating-chain form, so the instrument control and those
forms share one verdict; the control fixes the reference value the other forms are compared against.

## H1 test — the naive Thompson ordering fails
- **Form / ensemble:** A matched triple, all at n=3, AND determination family.
  Pooled (independent-contribution): `[lambda x: x[1], lambda x: x[0], lambda x: x[1]]` (relay/broadcast,
  per-party channel through the shared resource, #25/#40).
  Sequential (pass-through chain): the instrument-control chain above (#57).
  Reciprocal (feedback cycle): `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` (bidirectional
  coupling closing a loop, #5/#39).
- **Measure:** `verdict(rules, labels).structure` and `.max_phi` for each of the three forms; rank the
  three Φ values.
- **Controls:** Instrument control above. Baseline expectation under H0 is the Thompson ranking
  pooled < sequential < reciprocal in Φ, with pooled dyadic and the other two triadic.
- **Decision rule (fixed before run):** H1 is confirmed if at least one of the two ordering steps fails:
  pooled is not the strict Φ-minimum (it ties or exceeds another form, or is itself triadic), or the
  sequential Φ does not fall strictly between pooled and reciprocal. H1 is refuted only if the three Φ
  values are strictly monotone in Thompson's order with pooled dyadic. Predicted: pooled dyadic
  (Φ=0), sequential triadic (Φ=2.0), reciprocal triadic (Φ=2.0); sequential ties reciprocal rather than
  sitting strictly below it, so the ordering breaks and H1 holds.
- **Script:** `probe_thompson_ordering.py`

## H2 test — "pooled" is verdict-ambiguous, and the split turns on joint determination
- **Form / ensemble:** Two pooled encodings over the same parts, same node count, AND family.
  Independent-contribution pool: `[lambda x: x[1], lambda x: x[0], lambda x: x[1]]` (per-party channels,
  no joint determination over the shared node, #25/#40).
  All-required pool: the `pool(n)` form from `org_frontier/probes/probe_group_surplus.py` —
  `S' = AND of all non-S parties`, every non-S party `= S` (#116). Run the all-required pool at n=3 and
  n=4 to check the joint-determination signature scales (Φ ≈ n−1, group surplus at n≥4).
- **Measure:** `verdict(...).structure` and `.max_phi` for both encodings; `major_complex(...)` for the
  independent-contribution pool; for the all-required pool also the whole-minus-best-proper-subset Φ
  surplus (the `best_proper_subset_phi` helper in `probe_group_surplus.py`).
- **Controls:** Instrument control above. The two encodings are matched on node count (both n=3 at the
  primary comparison) and on the AND family, isolating joint determination as the only structural
  difference.
- **Decision rule (fixed before run):** H2 is confirmed if the two encodings land on opposite verdicts
  at n=3 — independent-contribution dyadic, all-required triadic. H2 is refuted if both encodings give
  the same verdict. Predicted: independent-contribution dyadic with major complex `{W, S}` (the shared
  resource and one party); all-required triadic at Φ=2.0 (n=3) and Φ=3.0 (n=4), confirming Φ≈n−1 with a
  positive group surplus at n=4. Opposite verdicts at fixed n confirm joint determination as the switch.
- **Script:** `probe_thompson_pooled.py`

## H3 test — "sequential" is verdict-ambiguous, and the split turns on the return path
- **Form / ensemble:** Two sequential encodings at n=3, AND family.
  Propagating chain (the worker's effect is read at the far end): the instrument-control chain
  `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` (#57).
  Acyclic source→sink hand-off (each stage only sources the next, nothing returns):
  `[lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]]` (#39).
- **Measure:** `verdict(...).structure` and `.max_phi` for both encodings; `.mip_partition` for the
  propagating chain.
- **Controls:** Instrument control above. The connectivity matrices differ only in the return edge: the
  propagating chain's `S' = W & C` reads C back into the chain, the acyclic hand-off's stages carry their
  own prior state forward with no return. Both are n=3, AND family.
- **Decision rule (fixed before run):** H3 is confirmed if the two encodings split — propagating chain
  triadic, acyclic hand-off dyadic. H3 is refuted if both give the same verdict. Predicted: propagating
  chain triadic at Φ=2.0 with a balanced near-middle MIP `{W,SC}`; acyclic hand-off dyadic (Φ=0). The
  split confirms the return path as the deciding feature.
- **Script:** `probe_thompson_sequential.py`

## H4 test — reciprocal requires a feedback cycle, not bidirectional labels
- **Form / ensemble:** Two reciprocal encodings at n=3, AND family, both nominally two-way.
  Cyclic reciprocal: `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` — coupling closes a
  feedback loop through both parties (#5/#39).
  Bidirectionally-labeled but acyclic: `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]` — a
  return arrow is drawn but `C' = C` does not close a determination cycle back through the loop (#5/#39).
- **Measure:** `verdict(...).structure` and `.max_phi` for both; `major_complex(...)` and
  `.mip_partition` for the cyclic form.
- **Controls:** Instrument control above. Both forms carry arrows in both directions by label; they
  differ only in whether the return edge closes a cycle. Same node count, same AND family.
- **Decision rule (fixed before run):** H4 is confirmed if the cyclic form reads triadic and the
  acyclic-but-bidirectional form reads dyadic. H4 is refuted if both read triadic (two-way labels alone
  suffice) or both read dyadic. Predicted: cyclic triadic at Φ=2.0 with the worker on the weakest seam,
  MIP `{W,SC}` and major complex `{W,S,C}` (#16/#26/#33); bidirectional-acyclic dyadic (Φ=0).
  Irreducibility tracking the cycle and not the arrow count confirms H4.
- **Script:** `probe_thompson_reciprocal.py`

## H5 test — only reciprocal is type-robustly triadic; pooled/sequential verdicts are encoding artifacts
- **Form / ensemble:** The full matched panel from H2, H3, H4 read as a single 2×3 table — for each
  Thompson type (pooled, sequential, reciprocal) the two defensible encodings already specified:
  pooled = {independent-contribution, all-required}; sequential = {propagating chain, acyclic hand-off};
  reciprocal = {cyclic, bidirectional-acyclic}. All at n=3, AND family. The structural primitives are
  coded per form as two booleans: joint determination present (a single downstream node whose rule is an
  AND over ≥2 parties, read off `cm_from_rules` plus the rule body) and feedback cycle present (the
  connectivity matrix from `cm_from_rules` contains a directed cycle through ≥2 parties).
- **Measure:** `verdict(...).structure` for all six forms. For each form record (Thompson type, joint
  determination, feedback cycle, verdict). Then check two functional-dependence claims: (a) verdict is
  not a function of Thompson type (some type maps to both verdicts), and (b) verdict is a function of the
  primitive pair {joint determination, feedback cycle} (no two forms share a primitive pair yet differ in
  verdict).
- **Controls:** Instrument control above. The panel is matched on node count and determination family so
  the only varying inputs are the two coded primitives and the Thompson label.
- **Decision rule (fixed before run):** H5 is confirmed if both hold: pooled spans dyadic↔triadic AND
  sequential spans dyadic↔triadic (so verdict is not a function of Thompson type), while every form with
  joint determination or a feedback cycle reads triadic and every form with neither reads dyadic (so
  verdict is a function of the primitive pair). H5 is refuted if Thompson type predicts verdict cleanly
  (each type single-valued) or if the primitive pair fails to predict verdict (two forms with the same
  pair disagree). Predicted: pooled {dyadic, triadic}, sequential {dyadic, triadic}, reciprocal {triadic,
  dyadic} where the dyadic reciprocal is the cycle-broken control; the three triadic forms all carry
  joint determination or a cycle, the three dyadic forms carry neither, so the primitive pair predicts
  every verdict and the Thompson label does not.
- **Script:** `probe_thompson_primitives.py`
