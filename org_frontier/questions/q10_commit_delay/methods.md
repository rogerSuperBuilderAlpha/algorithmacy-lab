# Q10 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `org_frontier/classifier/classifier.py` (`classify`, `classify_rules`,
  `tpm_from_rules`, `cm_from_rules`), `org_frontier/probes/lib.py` (`verdict`, `major_complex`,
  `max_phi_float`).
- Information measures: `org_frontier/probes/_info.py` (entropy, mutual_information, transfer_entropy,
  o_information).
- Exact Φ / trajectories / reachable states: `proxy_audit/exact_phi.py`
  (`exact_big_phi`, `reachable_states`, `simulate_trajectory`).
- Black-boxing the buffers over d steps: PyPhi `pyphi.macro` / direct composition of the micro TPM over the
  buffer window (the d-step map on the W–S–C subspace with the buffer pipeline marginalized).
- Python: `~/iit-playground/venv-4.0/bin/python`.
- The verdict is the binary structure (`dyadic` vs `triadic`) read off `Φ_MIP` over the most-integrated
  reachable state, with `PHI_EPS = 1e-9` the zero threshold. Φ magnitude is an ordinal hint, per the
  classifier docstring. The Q10 claims rest on the verdict, on its trend in `d`, and on major-complex
  membership, not on any single Φ value being a true scale.

## The corpus form (fixed for every test)
Node 0 is `W`, node 1 is the mediator `S`, node 2 is `C`; labels `("W","S","C")`. The anchor is the
triadic conjunctive form carrying the joint commit `S' = W ∧ C`:

- **`two_sided_match`** — `W' = S`, `S' = W ∧ C`, `C' = S` (rules
  `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`). Synchronous baseline (`d=0`): triadic,
  `Φ_MIP = 2.0`, MIP `2 parts: {W,SC}`, attractor period 2. Loaded from
  `org_frontier/corpus/forms_library.py` as `FORMS_BY_KEY["two_sided_match"].rules`. `S_IDX = 1` is the
  mediator's node index throughout.

A second corpus form of differing synchronous attractor period is carried for H4 and H5 to separate a
`d`-trend from an attractor effect:

- **`gig_false_dyad`** — `W' = 1 − S`, `S' = W ∧ C`, `C' = C ∧ (1 − S)` (rules
  `[lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])]`). Synchronous: triadic,
  `Φ_MIP = 2.0`, attractor period 1.

## The two transport-delay constructions (fixed for every test)
A transport delay `d ≥ 0` carries S's already-committed value forward `d` steps before the parties read it.
`d = 0` is the synchronous baseline (#112's reporting grain); both constructions reduce to the synchronous
W–S–C map at `d = 0`.

**(A) Buffer pipeline** — `d` pass-through buffer nodes `B_1 … B_d` are inserted on the path from S's
commit to the parties' read of S. The system has `n = 3 + d` nodes: `W`(0), `S`(1), `C`(2),
`B_1`(3) … `B_d`(3+d−1). S commits its conjunctive update from the current party states; the buffer head
`B_1` copies S, each `B_{i+1}` copies `B_i`, so `B_d` carries S's value from `d` steps ago. The parties read
the pipeline tail `B_d` in place of S (at `d = 0` they read S directly). Each buffer is pure pass-through:
`b'_i = (previous node on the line)`, **no self-OR** (`b'_i` does not depend on `b_i`), verified by
`cm_from_rules` showing no `B_i → B_i` self-edge — this is the transport-vs-inertia check the hypotheses
require (a self-OR buffer would be a #43 stickiness cell, not a transport line).

```python
def buffer_pipeline_rules(rules, d, s_idx=1):
    # nodes: 0..2 = W,S,C ; 3..3+d-1 = B_1..B_d (B_1 = head copies S, B_d = tail read by parties)
    n = 3 + d
    head = 3            # index of B_1
    tail = 3 + d - 1    # index of B_d  (== s_idx when d == 0: parties read S directly)
    read = tail if d > 0 else s_idx
    def lift(rule):     # party rule that reads S now reads the pipeline tail B_d
        return lambda x: rule(tuple(x[read] if i == s_idx else x[i] for i in range(3)))
    party = [lift(rules[0]), rules[1], lift(rules[2])]     # S keeps its own conjunctive commit on x[0..2]
    party[s_idx] = lambda x, r=rules[1]: r((x[0], x[1], x[2]))
    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)          # B_1 copies S; B_{i+1} copies B_i
        buf.append((lambda x, s=src: x[s]))
    return party + buf                                     # length n list of n-ary rules
```

(The party rules `W' = read`, `C' = read`, `S' = W ∧ C` are written as `n`-ary functions of the full
`(W,S,C,B_1…B_d)` state; only the indices they touch matter.) The form is classified by
`classify(tpm_from_rules(rules), cm_from_rules(rules), labels=("W","S","C","B1",…))`. The verdict object is
recovered on the W–S–C core; the **black-boxed** reading composes the micro map over the `d` buffer steps
and reads Φ on the 3-node W–S–C subspace.

**(B) Lagged read** — the same `d`-step transport with **no buffer nodes**. The parties read S as it was `d`
synchronous steps earlier. On the 3-node W–S–C state space this is a composed/strided map: S advances under
its own rule each step, and the parties at the observed transition apply their rules to S's value `d` steps
back. Built as the `d`-fold composition of the synchronous map with the party read delayed by `d`:

```python
def lagged_read_tpm(rules, d, n=3, s_idx=1):
    base = tpm_from_rules(rules)                  # synchronous state-by-node, 3 nodes
    if d == 0:
        return base
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        # advance S (and the system) d-1 free steps; parties commit reading S from d steps back
        hist = [state[:]]
        cur = state[:]
        for _ in range(d):
            nxt = [int(rules[j](tuple(cur))) for j in range(n)]
            hist.append(nxt); cur = nxt
        lagged_S = hist[0][s_idx]                 # S as it was d steps before the read
        read_state = list(cur)
        read_state[s_idx] = lagged_S
        for j in range(n):
            tpm[s, j] = float(rules[j](tuple(read_state))) if j != s_idx else float(cur[s_idx])
    return tpm
```

Φ over the lagged-read map is read by `classify(tpm, cm, …)` where `cm` is inferred by `cm_from_rules`-style
flip-test on the composed TPM (the `max_phi_float` connectivity inference is used when the map is fed as a
bare TPM). Whether this map is expressible as a single composed/strided 3-node TPM (it is, by construction)
is recorded — that is the H3 representational claim.

**The grid (fixed before any run).** `d` runs over the integers `0, 1, 2, 3` — the synchronous baseline
(`d=0`) through three steps of transport, spanning the forms' attractor periods (1, 2) and the sibling Q9
flip point (`k=2`). The discrete derivative is the forward difference `dΦ/dd|_d = Φ(d+1) − Φ(d)`. A
**verdict flip** for a (form, construction) is the smallest grid `d` at which the verdict reads `dyadic`
(`Φ_MIP ≤ PHI_EPS`). Numerical tolerance throughout is `TOL = 1e-6`.

## Instrument control (run first — shared by every test)
The synchronous (`d=0`) endpoint of each form is the established corpus verdict, and both constructions
reduce to it at `d=0`. Before any swept value is trusted, the `d=0` endpoints must reproduce:

| form | required verdict at d=0 | required Φ_MIP (to 1e-6) | required MIP |
|------|-------------------------|--------------------------|--------------|
| `two_sided_match` | triadic | 2.0 | `2 parts: {W,SC}` |
| `gig_false_dyad` | triadic | 2.0 | `2 parts: {W,SC}` |

This is the same reference value Probes 57/62 used, tying Q10's instrument to those runs. A second
instrument check fixes the buffer construction itself: `buffer_pipeline_rules(rules, 0)` must equal the bare
3-node synchronous form (no buffer nodes added at `d=0`), and for `d ≥ 1`, `cm_from_rules` on the pipeline
must show **no `B_i → B_i` self-edge** (pass-through verified, not a stickiness cell). If any form's `d=0`
endpoint does not reproduce `triadic` at `Φ_MIP = 2.0` with MIP `{W,SC}`, or any buffer carries a self-edge,
halt and do not read that form's swept values.

## H1 test — transport delay grades Φ down but does not flip the verdict
- **Form / ensemble:** The **buffer-pipeline** construction on `two_sided_match`. Build
  `buffer_pipeline_rules(rules, d)` for `d = 0,1,2,3` and classify each with
  `classify(tpm_from_rules(r), cm_from_rules(r), labels)`. Read the verdict on the W–S–C core (the whole-
  system verdict, then confirmed against the black-boxed 3-node map). Record verdict, `Φ_MIP`, MIP, and the
  `Φ_MIP(d)` trend at every `d`.
- **Measure:** The verdict (`dyadic`/`triadic`) at each `d`; the `Φ_MIP(d)` profile and its forward
  differences `dΦ/dd`. The verdict is "stable triadic across the grid" iff `structure == "triadic"` at every
  `d = 0,1,2,3`.
- **Controls:** Instrument control above (`d=0` triadic at `Φ_MIP = 2.0`, MIP `{W,SC}`). Negative control:
  the pass-through verification (no `B_i → B_i` self-edge) confirms the added structure is transport, not
  inertia, so any Φ change is attributable to depth and not to a stickiness cell. Trend register for the H0
  reading: record whether any `d` in `1..3` reads `dyadic` (the W–C pair factoring), which would match the
  timing-axis collapse of #32/#62.
- **Decision rule (fixed before run):** H1 is **confirmed** if the verdict reads `triadic` at every
  `d = 0,1,2,3` (no flip in the grid) while `Φ_MIP(d)` either falls monotonically with `d` (`dΦ/dd ≤ 0`
  across the grid) or holds at the #57 chain value of 2.0 — magnitude-soft, verdict-robust. H1 is **refuted**
  if the buffer-pipeline verdict reads `dyadic` at any `d` in `1..3` (transport delay flips the verdict like
  the other timing axes), or if `Φ_MIP(d)` rises with `d`. The directional prediction (Marshall 2018:
  regrade, do not abolish) is the confirmed branch.
- **Script:** `probe_q10_buffer_verdict.py`

## H2 test — the buffer nodes sit outside the major complex at the micro grain
- **Form / ensemble:** The **buffer-pipeline** construction on `two_sided_match` at `d = 1,2,3` (the cases
  with at least one buffer). At each `d` the major complex is read at the micro grain over the most-
  integrated reachable state, via `new_big_phi.maximal_complex(net, state)` over `reachable_states` (the
  machinery `major_complex` in `probes/lib.py` wraps), returning `(core_label_tuple, φ)`. In parallel, the
  individual φ of each interior buffer singleton `{B_i}` is read at the same map and state (the report's
  open-question-4 "measure it, do not assume zero" flag), and the φ of the `{W,S,C}` core subsystem. The
  same complex is then re-read after **black-boxing** the buffers over `d` steps to record whether the
  higher grain absorbs them (Marshall 2018).
- **Measure:** At each `d`: the micro-grain major-complex membership `core(d)` (a subset of
  `{W,S,C,B_1…B_d}`); whether `{W,S,C}` ⊆ `core(d)`; whether each interior buffer `B_i` (`i < d`) is
  excluded; `φ_{B_i}` for each buffer singleton; and the black-boxed core membership and Φ.
- **Controls:** Instrument control above. The buffer φ is **measured, not assumed** — `φ_{B_i}` is read
  explicitly so the feed-forward Φ=0 claim (Oizumi 2014; Tononi 2015; Hanson 2019) is tested, not asserted
  (refuted-claim flag). The pass-through verification (no self-edge) is the structural prior that the
  interior buffers are feed-forward. The black-boxed re-read is the positive contrast for the absorption
  branch.
- **Decision rule (fixed before run):** H2 is **confirmed** if, at every `d = 1,2,3`, the micro-grain major
  complex contains the full `{W,S,C}` core (with at most the S-adjacent buffer `B_1` as a weakly-integrated
  appendix) and **excludes** every interior buffer `B_i` (`i ≥ 2`), with `φ_{B_i} ≈ 0` (`< PHI_EPS`) for each
  excluded buffer. H2 is **refuted** if any interior buffer sits inside the major complex (the #57 chain-
  intermediary reading) with `φ_{B_i} > PHI_EPS`, or if the `{W,S,C}` core is not recovered at the micro
  grain. The black-boxed absorption (buffers entering the core at higher Φ) is recorded as the Marshall-2018
  grain-dependent branch and does not by itself refute the micro-grain claim.
- **Script:** `probe_q10_buffer_membership.py`

## H3 test — the buffer pipeline and the lagged read disagree
- **Form / ensemble:** Both constructions on `two_sided_match`, swept on the same grid `d = 0,1,2,3`.
  Buffer pipeline: `buffer_pipeline_rules(rules, d)` classified by `classify`, verdict read on the W–S–C
  core. Lagged read: `lagged_read_tpm(rules, d)` classified by `classify` with the connectivity inferred by
  flip-test on the composed TPM (`max_phi_float` when fed as a bare TPM).
- **Measure:** At each `d`: the buffer-pipeline verdict `v_buf(d)` and the lagged-read verdict `v_lag(d)`,
  each `Φ_MIP`, and each major-complex core. Also whether the lagged-read map is expressible as a single
  composed/strided 3-node TPM (it is, by construction) while the buffer pipeline is not (it adds nodes). The
  pair **disagrees** at `d` iff `v_buf(d) ≠ v_lag(d)` or the two return different major complexes (after
  mapping the buffer core onto its W–S–C projection).
- **Controls:** Instrument control above (both reduce to the synchronous map at `d=0`, `Φ=2.0`, triadic — a
  matched starting point). `PHI_EPS = 1e-9` is applied identically to both constructions. The
  representational fact (lagged read = composed/strided TPM; buffer pipeline = added depth) is recorded as
  the load-bearing difference.
- **Decision rule (fixed before run):** H3 is **confirmed** if at some `d` in `1..3` the verdicts disagree —
  `v_lag(d)` reads `dyadic` while `v_buf(d)` reads `triadic` at the same `d` — or the two return different
  major complexes at the same `d`, with the lagged-read map expressible as a composed/strided TPM the buffer
  pipeline is not. H3 is **refuted** if the two constructions return the same verdict at every `d` in the
  grid and the same W–S–C major-complex membership (IIT reads the lag, not its representation). The
  implementation-is-load-bearing claim is the confirmed branch.
- **Script:** `probe_q10_construction_split.py`

## H4 test — no d=2 threshold under transport delay
- **Form / ensemble:** The **buffer-pipeline** construction on `two_sided_match` (period 2) and
  `gig_false_dyad` (period 1), each at `d = 0,1,2,3`. The synchronous attractor period `P` is computed by
  `attractor_period(rules)` (longest cycle over all initial states under the synchronous map). For each form
  build `buffer_pipeline_rules(rules, d)`, classify, and read `Φ_MIP(d)` and the verdict.
- **Measure:** For each form: the `Φ_MIP(d)` profile and its forward differences `dΦ/dd` at `d = 0→1`,
  `1→2`, `2→3`; whether a verdict change occurs uniquely at `d=2`; and whether the `d=2` reading lies on the
  same smooth trend (within `TOL`) as the line through its `d=1` and `d=3` neighbours. A **d=2 kink** is a
  forward-difference discontinuity (`|dΦ/dd|_{d=2} − dΦ/dd|_{d=1}| > TOL` and likewise vs `d=2→3`) or a
  verdict change appearing only at `d=2`.
- **Controls:** Instrument control above (both forms triadic at `d=0`, `Φ=2.0`). The sibling Q9 `k=2` flip
  and the grain-2 collapse (#32, #60) are the positive references for what a genuine `d=2` threshold looks
  like; the claim is that the transport-delay trend shows none. The two forms of differing `P` are the
  control for tying any threshold (if it appears in the lagged-read arm, H3) to the form's attractor period
  rather than to a fixed `d=2`.
- **Decision rule (fixed before run):** H4 is **confirmed** if `Φ_MIP(d)` on the buffer pipeline shows **no**
  kink, jump, or verdict change uniquely at `d=2` for either form — the `d=2` reading lies on the smooth
  trend through `d=1` and `d=3` within `TOL`, and any verdict change (if H1's null held) is not pinned to
  `d=2`. H4 is **refuted** if a forward-difference discontinuity or a verdict change appears uniquely at
  `d=2` on the buffer pipeline, reproducing the Q9 `k=2` / grain-2 threshold. Any threshold observed in the
  lagged-read arm is checked against `P` (period-tied) rather than fixed at 2.
- **Script:** `probe_q10_no_d2_threshold.py`

## H5 test — transport delay and the slowed clock leave distinguishable fingerprints
- **Form / ensemble:** On `two_sided_match`, three composed maps read at matched grain:
  (a) the **buffer-pipeline** map `buffer_pipeline_rules(rules, d)` at each `d = 1,2,3` (this probe);
  (b) the Q9 **hold-for-k** map `hold_k_tpm(rules, k)` at its flip ratio `k*_det = 2` (the slowed clock,
  from `org_frontier/questions/q9_timescale_separation/methods.md`);
  (c) for context, the #62 **sequential-update** maps `sequential_tpm(rules, order)` over `order ∈ S₃`.
  Each is classified by `classify(tpm, cm, labels)`; the buffer map's complex is projected onto W–S–C.
- **Measure:** For each map: the major-complex membership; the MIP partition `mip_partition`; and the
  residual `Φ_MIP`. The transport-delay fingerprint is the triple (W–S–C core with buffers excluded, MIP
  cut, residual Φ) across `d`; the slowed-clock fingerprint is the Q9 hold-for-k result at `k*_det` (its
  `{S}`-ejection or `{W,C}`-core membership and MIP, from Q9 H2). The discriminator is whether the transport
  delay ever produces the self-absorbed `{S}` core the hold-for-k produced (#156), and whether its MIP cut
  matches the hold's. The pass-through check (no `B_i → B_i` self-edge) is read to confirm no stickiness
  (#43) arises.
- **Controls:** Instrument control above (`two_sided_match` at `d=0` triadic, MIP `{W,SC}`). The Q9 hold-
  for-k result and the #62 sequential maps are the two established alternative timing-axis fingerprints on
  this same form, co-read here on one grid. The `{S}`-core watch is the direct discriminator against the H0
  (the delay-as-memory-cell reading). MIP reprs are taken at the state where Φ is read, identically across
  maps.
- **Decision rule (fixed before run):** H5 is **confirmed** if, where transport delay touches the verdict, it
  leaves a major complex on `{W,S,C}` or `{W,C}` with the buffers excluded and **never** the self-absorbed
  `{S}` core the hold-for-k produced, and its MIP cut differs from the hold's at the matched grain, with the
  pass-through buffers verified to carry no self-OR (no #43 stickiness). H5 is **refuted** if the transport
  delay reproduces the hold's `{S}`-core collapse with the identical MIP cut (the delay-is-a-memory-cell
  reading), so transport delay is the slowed clock re-parameterized. The distinct-fingerprints claim
  (a fourth, verdict-stable timing axis extending the #112 catalogue) is the confirmed branch.
- **Script:** `probe_q10_factorization_fingerprint.py`
