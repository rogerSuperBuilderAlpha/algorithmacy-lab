# Q9 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `org_frontier/classifier/classifier.py` (`classify`, `classify_rules`,
  `tpm_from_rules`, `cm_from_rules`), `org_frontier/probes/lib.py` (`verdict`, `major_complex`,
  `max_phi_float`).
- Information measures: `org_frontier/probes/_info.py` (entropy, mutual_information, transfer_entropy,
  o_information).
- Exact Φ / trajectories: `proxy_audit/exact_phi.py`.
- Python: `~/iit-playground/venv-4.0/bin/python`.
- The verdict is the binary structure (`dyadic` vs `triadic`) read off `Φ_MIP` over the most-integrated
  reachable state, with `PHI_EPS = 1e-9` the zero threshold. Φ magnitude is an ordinal hint, per the
  classifier docstring. The Q9 claims rest on the verdict, on the location of its flip in `k`, and on
  major-complex membership, not on any single Φ value being a true scale.

## The corpus forms (fixed for every test)
Node 0 is `W`, node 1 is the mediator `S`, node 2 is `C`; labels `("W","S","C")`. Three triadic
conjunctive corpus forms carry the joint commit `S' = W ∧ C`, and they differ in their synchronous
attractor period:

- **`two_sided_match`** — `W' = S`, `S' = W ∧ C`, `C' = S` (rules
  `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`). Synchronous: triadic, `Φ_MIP = 2.0`, MIP
  `2 parts: {W,SC}`, attractor period **2**. The Probe 57/62 anchor and the question's primary form.
- **`ats_strict_bottleneck`** — `W' = S`, `S' = W ∧ C`, `C' = S` (same rules as `two_sided_match`).
  Triadic, `Φ_MIP = 2.0`, period **2**. The corpus duplicate of the anchor topology.
- **`gig_false_dyad`** — `W' = 1 − S`, `S' = W ∧ C`, `C' = C ∧ (1 − S)` (rules
  `[lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: x[2] & (1 - x[1])]`). Triadic, `Φ_MIP = 2.0`,
  MIP `2 parts: {W,SC}`, attractor period **1**. The differing-period form H4 needs.

Forms are loaded from `org_frontier/corpus/forms_library.py` (`FORMS_BY_KEY[key].rules`). `S_IDX = 1` is
the mediator's node index throughout.

## The two slow-commit constructions (fixed for every test)
A timescale ratio `k ≥ 1` stretches S's clock against fast parties. `k = 1` is the synchronous baseline
(#112's reporting grain). Two models of the slow commit are swept on the same `k` grid:

**(A) Deterministic hold-for-k** — the construction that stays inside the state-by-node instrument.
Inside one observed (macro) transition, `k` micro-steps run. The parties apply their rules every
micro-step; S holds its own value for the first `k−1` micro-steps and commits its conjunctive update on
the `k`-th. The observed transition is the macro-state after the full `k`-window. This is a deterministic
composed map, classified directly by `classify(tpm, cm, labels)`:

```python
def hold_k_tpm(rules, k, n=3, s_idx=1):
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]          # S holds its previous value
        return ns
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))  # commit only on the k-th micro-step
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm
```

**(B) Probabilistic 1/k commit** — the #61-flagged construction. Each step S commits its conjunctive
update with probability `1/k` and holds with probability `1 − 1/k`; the parties stay deterministic. This
lives in a stochastic state-by-node TPM: only the S column (node 1) is rescaled, mixing the clean commit
value with the held value. Φ over it is read with `max_phi_float` (which accepts a stochastic TPM and
infers the connectivity matrix). The verdict is read by thresholding that Φ at `PHI_EPS`.

```python
def prob_commit_tpm(rules, k, n=3, s_idx=1):
    base = tpm_from_rules(rules)              # deterministic synchronous next-state, state-by-node
    t = base.copy()
    for s in range(2 ** n):
        cur_S = (s >> s_idx) & 1
        commit_val = base[s, s_idx]
        t[s, s_idx] = (1.0 / k) * commit_val + (1.0 - 1.0 / k) * cur_S
    return t
```

**The grid (fixed before any run).** `k` runs over the integers `1, 2, 3, 4, 5, 6` — from the synchronous
baseline (`k=1`) through the forms' natural attractor periods (1, 2) and well beyond. The strict
**verdict-flip ratio** `k*` for a (form, construction) is the smallest grid `k` at which the verdict reads
`dyadic` (`Φ_MIP ≤ PHI_EPS`). The discrete derivative is the forward difference
`dΦ/dk|_k = Φ(k+1) − Φ(k)`. Numerical tolerance throughout is `TOL = 1e-6`.

## Instrument control (run first — shared by every test)
The synchronous (`k=1`) endpoint of each form is the established corpus verdict. Before any swept value is
trusted, the three `k=1` endpoints, under **both** constructions (which both reduce to the synchronous map
at `k=1`), must reproduce:

| form | required verdict at k=1 | required Φ_MIP (to 1e-6) | required MIP |
|------|-------------------------|--------------------------|--------------|
| `two_sided_match` | triadic | 2.0 | `2 parts: {W,SC}` |
| `ats_strict_bottleneck` | triadic | 2.0 | `2 parts: {W,SC}` |
| `gig_false_dyad` | triadic | 2.0 | `2 parts: {W,SC}` |

Confirmed in pre-registration trial: the deterministic `hold_k_tpm(rules, 1)` and the probabilistic
`prob_commit_tpm(rules, 1)` both return `Φ_MIP = 2.0`, `triadic`, MIP `{W,SC}` on `two_sided_match`. This
is the same reference value Probes 57/62 used, tying Q9's instrument to those runs. If any form's `k=1`
endpoint does not reproduce `triadic` at `Φ_MIP = 2.0`, halt and do not read that form's swept values.

## H1 test — a slow mediator flips the verdict at a finite interior k*
- **Form / ensemble:** The **deterministic hold-for-k** construction on `two_sided_match` (the
  synchronous-baseline anchor form). Build `hold_k_tpm(rules, k)` for `k = 1…6` and classify each with
  `classify(tpm, cm, labels=("W","S","C"))`. Record the verdict, `Φ_MIP`, and MIP at every `k`.
- **Measure:** The strict verdict-flip ratio `k*_det` — the smallest grid `k` where `structure` reads
  `dyadic` (`Φ_MIP ≤ PHI_EPS = 1e-9`) — and the value of `Φ_MIP` at `k*_det − 1` and `k*_det`.
- **Controls:** Instrument control above (`k=1` triadic at `Φ_MIP = 2.0`). Negative control that the
  dyadic reading is a genuine zero-crossing, not a one-point dropout: the flip must satisfy
  `Φ_MIP(k*_det) ≤ PHI_EPS` with `Φ_MIP(k*_det − 1) > PHI_EPS`, and the verdict must stay `dyadic` at every
  `k > k*_det` in the grid (no return to triadic). Contrast register for the H0 reading ("magnitude-only,
  like reliability #27 and depth #57"): record whether `Φ_MIP(k)` is strictly positive at every finite `k`
  in the grid with no `dyadic` reading until the degenerate `k→∞` limit.
- **Decision rule (fixed before run):** H1 is **confirmed** if `k*_det` is finite and interior to the grid
  (`1 < k*_det ≤ 6`), with `Φ_MIP` dropping from `> PHI_EPS` at `k*_det − 1` to `≤ PHI_EPS` at `k*_det` and
  staying dyadic above it. H1 is **refuted** if the verdict stays `triadic` (`Φ_MIP > PHI_EPS`) at every
  swept `k` — the magnitude-only H0 outcome, where `k` grades Φ down but never flips the binary verdict.
  Pre-registration trial finding (anchor form, hold-for-k): `k=1` triadic `Φ=2.0`, then `dyadic` `Φ=0` at
  `k=2,3,4,5,6`, so `k*_det = 2` and H1 is expected to be **confirmed** — timescale separation flips the
  verdict at a finite interior ratio, a fourth verdict-flipping timing axis.
- **Script:** `probe_q9_hold_verdict_flip.py`

## H2 test — slowing S ejects S from the major complex, not the parties
- **Form / ensemble:** The **deterministic hold-for-k** construction on `two_sided_match`, at `k = 1…6`.
  The major complex is read over the most-integrated reachable state. Because `major_complex` in
  `probes/lib.py` takes per-party rules, the hold-for-k composed map is fed to a rules-equivalent reader:
  the major complex is computed directly from the composed `(tpm, cm)` via PyPhi `new_big_phi.maximal_complex`
  over `reachable_states` (the same machinery `major_complex` wraps), returning `(core_label_tuple, φ)`. In
  parallel, the subsystem φ of `{W,C}` alone and of `{S}` alone are read at the same composed map and same
  state, so S's solo contribution can be compared against the W–C pair's.
- **Measure:** At each `k`: the major-complex membership `core(k)` (a subset of `{W,S,C}`); `φ_s`, the φ of
  the `{S}` singleton subsystem; and `φ_wc`, the φ of the `{W,C}` subsystem, both at the most-integrated
  reachable state. Record whether the core transitions from `{W,S,C}` (at `k=1`) to `{W,C}` (S excluded) at
  `k ≥ k*_det`, and whether an `{S}` core ever appears over the grid.
- **Controls:** Instrument control above (`k=1` core is the full `{W,S,C}` triad). The `{S}`-core watch is
  the direct discriminator against the H0 (#43 sticky-mediator) outcome, where inertia ejects the *parties*
  into a self-absorbed `{S}` core. Both `φ_s` and `φ_wc` are read at the same grain and state so the
  comparison is symmetric.
- **Decision rule (fixed before run):** H2 is **confirmed** if, at `k ≥ k*_det` (from H1), the major complex
  is `{W,C}` with S excluded, `φ_s < φ_wc` at that grain, and no `{S}` core appears at any swept `k`. H2 is
  **refuted** if the major complex contracts to `{S}` at any `k` (the parties factor out, the #43 direction),
  or if S stays in the core at every `k` while the verdict has flipped (membership does not track the flip).
  Pre-registration expectation: at `k ≥ 2` the composed map factors along `{W,SC}`→ pairwise, so the
  surviving irreducible core is `{W,C}` and S drops out; H2 is expected to be **confirmed**, distinguishing
  soft clock-inertia (ejects S) from the hard OR-stick of #43 (ejects the parties).
- **Script:** `probe_q9_hold_membership.py`

## H3 test — hold-for-k and probabilistic-1/k disagree on the verdict
- **Form / ensemble:** Both constructions on `two_sided_match`, swept on the same grid `k = 1…6`.
  Deterministic: `hold_k_tpm(rules, k)` classified by `classify`. Probabilistic: `prob_commit_tpm(rules, k)`
  read by `max_phi_float`, with the verdict assigned `dyadic` iff `Φ_MIP ≤ PHI_EPS`.
- **Measure:** The two strict flip ratios `k*_det` (deterministic, from H1) and `k*_prob` (smallest grid `k`
  with the probabilistic `Φ_MIP ≤ PHI_EPS`, or "none in grid" if the probabilistic verdict stays triadic
  through `k=6`). Also the full probabilistic `Φ_MIP(k)` profile, to characterize the soft grading.
- **Controls:** Instrument control above (both constructions reduce to the synchronous map at `k=1`,
  `Φ=2.0`, triadic — a matched starting point). `PHI_EPS = 1e-9` is applied identically to both
  constructions so the comparison is symmetric. The #61 modeling flag is recorded: the probabilistic commit
  requires the stochastic state-by-node TPM, which the deterministic hold-for-k does not.
- **Decision rule (fixed before run):** H3 is **confirmed** if the two flip ratios differ by more than one
  grid step (`|k*_prob − k*_det| > 1`), or the probabilistic verdict holds `triadic` across the whole grid
  (`k*_prob` = none) while the deterministic verdict flips (`k*_det` finite). H3 is **refuted** if the two
  cross the dyadic boundary at the same `k` within one grid step (`|k*_prob − k*_det| ≤ 1`) — the H0 reading
  that IIT reads the fast/slow ratio and not its stochastic dressing. Pre-registration trial finding: the
  deterministic flips at `k*_det = 2` (Φ to exactly 0), while the probabilistic Φ_MIP grades softly —
  `2.0, 0.271, 0.138, 0.092, 0.069, 0.055` at `k = 1…6`, never reaching PHI_EPS, so `k*_prob` = none in grid.
  H3 is expected to be **confirmed**: the slow-commit model is load-bearing.
- **Script:** `probe_q9_construction_split.py`

## H4 test — the verdict-flip ratio is tied to the form's attractor period
- **Form / ensemble:** The **deterministic hold-for-k** construction on two forms of differing synchronous
  attractor period: `gig_false_dyad` (period 1) and `two_sided_match` (period 2). The attractor period is
  computed by `attractor_period(rules)` from `probe_grain_threshold.py` (the longest cycle over all initial
  states under the synchronous map). `hold_k_tpm(rules, k)` is built for `k = 1…6` on each form.
- **Measure:** For each form: its synchronous attractor period `P` and its hold-for-k flip ratio `k*_det`
  (from the H1 definition). The contrast is whether `k*_det` increases with `P` across the two forms,
  versus sitting pinned at a period-independent constant (e.g. `k*_det = 2` for both regardless of `P`).
- **Controls:** Instrument control above (both forms triadic at `k=1`, `Φ=2.0`). The grain-collapse
  precedent #60 is the positive reference: under whole-system grain-`k` composition both forms flip at
  grain 2; the period-tracking claim is that the hold-for-k flip, applied to S only, moves with `P` where
  the whole-system grain flip did not. The two forms are matched on the AND conjunctive commit and node
  count, isolating the period as the varying input.
- **Decision rule (fixed before run):** H4 is **confirmed** if the longer-period form flips at a strictly
  larger `k*_det` — `k*_det(period-2 `two_sided_match`) > k*_det(period-1 `gig_false_dyad`)`. H4 is
  **refuted** if both forms flip at the same `k*_det` (period-independent), or if the ordering runs opposite
  to period. Honest pre-registration caveat: on a period-1 form the very first hold (`k=2`) already spans a
  full synchronous cycle, so the trial expectation is that **both** corpus forms flip at `k*_det = 2`
  regardless of `P` (the period-independent grain-2 outcome), which would **refute** H4 on this corpus pair.
  H4 stands only if the period-2 form is observed to survive to a strictly larger `k` than the period-1
  form. The decision rule is fixed before the full run and adjudicates it; the sharpest, most falsifiable Q9
  claim.
- **Script:** `probe_q9_period_lock.py`

## H5 test — clock-stretching is a different factorization from sequential update (#62)
- **Form / ensemble:** On `two_sided_match`, three composed maps at their respective collapse points:
  (a) the **deterministic hold-for-k** map `hold_k_tpm(rules, k*_det)` at its flip ratio;
  (b) the six **sequential-update** maps `sequential_tpm(rules, order)` from `probe_async.py`, one per
  permutation `order ∈ S₃` (the Probe 62 construction);
  (c) for context, the **whole-system grain-2** map `k_step(rules, 2)` from `probe_grain_threshold.py`.
  Each is classified by `classify(tpm, cm, labels=("W","S","C"))`.
- **Measure:** For each map at its dyadic collapse: the MIP partition `mip_partition`, the residual `Φ_MIP`
  at the flip (expected 0 for a clean factorization, but recorded so a near-zero residual is not assumed),
  and the set of `k` (for the hold construction) over which the dyadic verdict holds (a band `k ≥ k*_det`
  vs a single point). The hold-for-k fingerprint is the triple (MIP at `k*_det`, residual Φ, collapse band);
  the #62 fingerprint is the set of six sequential MIPs and their residual Φ.
- **Controls:** Instrument control above (`two_sided_match` at `k=1` triadic, MIP `{W,SC}`). The #62
  sequential maps and the grain-2 map are the two established alternative routes to the dyadic verdict on
  this same form, both co-computed here so the fingerprints are read on one grid. The MIP repr is taken from
  the state at which Φ is read, identically across all maps.
- **Decision rule (fixed before run):** H5 is **confirmed** if the hold-for-k collapse leaves a
  **distinguishable** fingerprint from the #62 sequential collapse on the matched form — a different MIP cut
  at `k*_det` than every sequential `order`'s MIP, a different residual `Φ_MIP` at the flip, or a collapse
  that holds over a `k` band (`k ≥ k*_det`) where #62's collapse holds at every single order rather than
  over a ratio band. H5 is **refuted** if the hold-for-k map cuts the triad at the identical MIP as the
  sequential maps with the same residual Φ, so clock-stretching is just #62 re-indexed by `k`. Honest
  pre-registration caveat: both routes are expected to deliver the same dyadic verdict with `Φ_MIP = 0`
  cleanly at the flip, so a *residual-Φ* difference is unlikely; the discriminator most likely to fire is
  the **collapse band** (hold-for-k holds dyadic over `k = 2…6`, a temporal band, where #62 collapses at
  within-step ordering with no analogous band) and any **MIP-cut** difference between the composed maps. H5
  is confirmed on either of those; the decision rule is fixed before the run.
- **Script:** `probe_q9_factorization_fingerprint.py`
