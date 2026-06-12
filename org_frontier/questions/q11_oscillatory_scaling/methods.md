# Q11 — Stage 4 methods

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
  classifier docstring. The Q11 scaling claims read the *sequence* `Φ_MIP(n)` over `n = 3,4,5,6` and the
  *law class* it traces, not any single Φ value as a true scale.
- All Φ values are exact IIT-4.0 Φ over reachable states at grain 1 (one synchronous transition), read by
  `major_complex` (which wraps `new_big_phi.maximal_complex` over `reachable_states`). Cost grows with `n`:
  the pre-registration trial timed the flip ring at ~0.2 s for `n=3`, ~46 s for `n=5`; `n=6` (2^6 = 64
  states) is a few minutes per form and is the heaviest single computation. Every test runs `n=3,4,5,6`.

## The forms (fixed for every test)
Node `i`'s rule reads the current state tuple `x` (little-endian, index 0 = first party). Labels are
`tuple(f"x{i}" for i in range(n))` throughout, matching the zoo probe `probe_scaling_zoo.py`.

**`and_ring(n)` — the zoo's capped fixed-point ring (#132).** Each node is the AND of its two ring
neighbors:
```python
def and_ring(n):
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules
```
This is the exact `ring` builder from `probe_scaling_zoo.py`. It collapses to a fixed point (synchronous
attractor period 1–2) and carries the capped law Φ=4 for `n≥4`. It is the reference family H1 separates
against.

**`rot_ring(n)` — the rotating-update ring (the genuine cycler, H1/H2/H5).** Each node copies its left
neighbor, so the global state rotates by one position each step — a traveling wave of period `n`:
```python
def rot_ring(n):
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules
```
A pure cyclic shift. Its synchronous attractor period is `n` (every state lies on an `n`-cycle or a
shorter divisor cycle; the map is a reversible permutation, so nothing collapses). This is the rotating
ring the question's winding constraint (T₂·N = nP) describes at the matched case P = n.

**`flip_ring(n)` — the rotating-flip (per-node parity) ring (H3).** Each node is the logical NOT of its
left neighbor, so a flip travels around the loop and the global pattern returns after `2n` steps:
```python
def flip_ring(n):
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(1 - x[a]))
    return rules
```
The spatial chain of XOR-like flips the review names, distributed around a ring with no shared hub.
Synchronous attractor period `2n`. This is the rotating analogue of the parity hub `parity_hub(n)` from
`probe_parity_scaling.py` (`rules[0] = XOR of all parties; rules[i>0] = x[0]`), whose decaying law is
Φ=2^(2−n).

**`commit_ring(n, p)` — the periodic-commit mediated form (H2/H4).** A mediator `S` (node 0) holds a
conjunctive commit and releases it on a fixed cadence `p`, driving members that feed back into it. The
commit phase is carried by an explicit clock built into the composed transition so the period `p` is set
*independently of member count*. Concretely, the mediated cycler is built as a composed state-by-node TPM
in which S commits `S' = AND(members)` once every `p` steps and holds its value otherwise, while each
member `i≥1` reads S; the clock phase is encoded by running `p` micro-steps per observed transition with
the commit released only on the last (the `hold_k_tpm` composition pattern from Q9's methods, with the
mediator as the held node and `k = p`). The observed transition is classified directly from the composed
`(tpm, cm)` by `classify(tpm, cm, labels)`. `p` is swept `{1, 2, 3}` at each `n`; `n` is swept `{3,4,5,6}`.

**Attractor period helper (fixed).** The synchronous attractor period `P(rules, n)` is the longest cycle
length over all `2^n` initial states under the synchronous next-state map read from `tpm_from_rules`:
```python
def period(rules, n):
    tpm = tpm_from_rules(rules)
    nxt = lambda s: sum(int(tpm[s, j]) << j for j in range(n))
    mp = 1
    for s0 in range(2 ** n):
        seen = {}; s = s0; t = 0
        while s not in seen:
            seen[s] = t; s = nxt(s); t += 1
        mp = max(mp, t - seen[s])
    return mp
```

**Law-class reader (fixed, from the zoo probe).** A sequence `seq = [Φ(3), Φ(4), Φ(5), Φ(6)]` is named by
`law_class` from `probe_scaling_zoo.py`: `constant` if `max−min < 1e-6`; `decay` if `seq[3] < seq[0]`;
`linear` if the second difference vanishes; else `super-linear`. The four established laws are
constant (Φ=4 capped ring; Φ=2 chain), linear (Φ=n−1 conjunctive hub), super-linear (Φ=n(n−1) pool),
decay (Φ=2^(2−n) parity hub).

## Instrument control (run first — shared by every test)
The capped AND-neighbor ring is the established reference family, and the parity hub is the decay
reference H3 names. Before any Q11 value is trusted, these must reproduce their #132 / #115 readings at
grain 1:

| form | n | required reading |
|------|---|------------------|
| `and_ring` | 4 | triadic, `max Φ_MIP = 4.0`, full core, synchronous period ≤ 2 |
| `and_ring` | 3 | triadic, `max Φ_MIP = 6.0` (the #132 n=3 ring value) |
| `parity_hub` | 5 | triadic, full core, `max Φ_MIP = 2^(2−5) = 0.125` |

Pre-registration trial (confirmed): `and_ring(4)` returns `max Φ_MIP = 4.0` with synchronous period 2;
`and_ring(3)` returns `6.0`; both triadic with the full node set in the core. If `and_ring` does not
reproduce Φ=4.0 at `n=4` and Φ=6.0 at `n=3`, halt — the instrument is mis-wired and no Q11 comparison is
trusted. The parity-hub `0.125` at `n=5` anchors the H3 floor.

## H1 test — the rotating ring is a fifth law, distinct from the capped Φ=4
- **Form / ensemble:** `rot_ring(n)` for `n = 3,4,5,6`, each classified by `major_complex(rot_ring(n),
  labels)` for `(core, Φ_MIP)` and by `verdict(rot_ring(n), labels)` for the dyadic/triadic call. In
  parallel, `and_ring(n)` at matched `n = 4,5,6` for the head-to-head against the capped family.
- **Measure:** The sequence `Φ_rot = [Φ_MIP(3), Φ_MIP(4), Φ_MIP(5), Φ_MIP(6)]` for the rotating ring, its
  `law_class`, and the per-`n` difference `Φ_rot(n) − Φ_and(n)` at `n = 4,5,6`. The synchronous period
  `P(rot_ring(n)) = n` is recorded to certify the form is a genuine cycler, not a collapser.
- **Controls:** Instrument control above (`and_ring(4) = 4.0`, `and_ring(3) = 6.0`). The `and_ring` curve
  at matched `n` is the negative control / capped-family baseline. The period read confirms `rot_ring`
  cycles (period `n`) where `and_ring` collapses (period ≤ 2), so any Φ difference is read against a
  matched topology that differs only in the update rule.
- **Decision rule (fixed before run):** H1 is **confirmed** if the rotating ring's law is separable from
  the capped Φ=4 family — either `Φ_rot(n) ≠ 4` at some `n≥4` by more than `1e-6`, or `Φ_rot(n)` differs
  from `Φ_and(n)` at some matched `n∈{4,5,6}` by more than `1e-6`, so over `n=3..6` the two trace
  distinguishable curves. H1 is **refuted** if `Φ_rot(n) = Φ_and(n)` (within `1e-6`) at every matched
  `n=4,5,6` and `Φ_rot` reproduces the capped Φ=4 (Φ=2 at n=3) constant — the rotating update changes the
  attractor type but not the law the loop carries. Pre-registration trial finding: `rot_ring` returns
  `Φ_MIP = 2.0` at `n=3` and `n=4` while `and_ring` returns `6.0` and `4.0`, so the curves already
  separate at `n=4` (2.0 vs 4.0); H1 is expected to be **confirmed**, with the rotating ring tracing a
  *flat Φ=2 constant* — a fifth family that is constant like the capped ring but pinned at a different
  value (2, not 4). The full `n=5,6` run fixes the law class before that reading is final.
- **Script:** `probe_q11_rotating_law.py`

## H2 test — the cycle period enters the law as a term
- **Form / ensemble:** Two sub-sweeps read on the same grain-1 instrument.
  (a) The **periodic-commit mediated form** `commit_ring(n, p)` with `n` held fixed at each of `3,4,5,6`
  and the commit cadence `p` swept `{1, 2, 3}` — `n` constant, `p` varying.
  (b) The **rotating ring** `rot_ring(n)` for `n = 3,4,5,6`, where the winding constraint ties period to
  size so `p = P(rot_ring(n)) = n` — `p` and `n` co-varying. Each map is classified by `classify` (the
  composed mediated map) or `major_complex` (the ring) for `Φ_MIP`.
- **Measure:** (a) Δ_p Φ = `Φ_MIP(commit_ring(n, 3)) − Φ_MIP(commit_ring(n, 1))` at each fixed `n` — the
  movement of Φ when only `p` changes. (b) The pair of curves `Φ_MIP` vs `n` and `Φ_MIP` vs
  `p = P(rot_ring(n))` for the ring, to test whether the ring's Φ is a function of `p` (here equal to `n`,
  so the two curves coincide and this sub-sweep alone cannot separate `p` from `n` — it is the corroborant,
  not the discriminator).
- **Controls:** Instrument control above. The discriminating control is sub-sweep (a): because
  `commit_ring` sets `p` by the commit cadence *independently of member count*, holding `n` fixed and
  varying `p` isolates the period as the only changed input. `commit_ring(n, 1)` (commit every step) is the
  no-stretch baseline; it reduces to the synchronous mediated map. The conjunctive commit and node count
  are matched across the `p` sweep at each `n`.
- **Decision rule (fixed before run):** H2 is **confirmed** if Δ_p Φ ≠ 0 (by more than `1e-6`) at some
  fixed `n` — Φ moves when only the period changes, so `p` is a term in the law. H2 is **refuted** if
  Δ_p Φ = 0 (within `1e-6`) at every fixed `n=3,4,5,6` — the grain-1 reading is blind to the cycle period
  and Φ is a function of `n` and topology alone, as the static fixed-point families are. The ring sub-sweep
  (b) corroborates only if its Φ-vs-`p` curve is non-flat; with `p = n` it cannot by itself separate the
  two, and the decision rests on (a). (Note the cross-check fixed before the run: if H1's flat-Φ=2 reading
  holds for the rotating ring, the ring's Φ is *constant* in both `n` and `p`, so any period dependence H2
  finds must come from the mediated form, not the ring — the two tests are read together.)
- **Script:** `probe_q11_period_term.py`

## H3 test — distributing the parity flip around a ring breaks the decaying law
- **Form / ensemble:** `flip_ring(n)` (NOT-of-left-neighbor) for `n = 3,4,5,6`, each classified by
  `major_complex` for `(core, Φ_MIP)`. The reference is `parity_hub(n)` from `probe_parity_scaling.py` at
  matched `n`, whose law is Φ=2^(2−n).
- **Measure:** The sequence `Φ_flip = [Φ_MIP(3), Φ_MIP(4), Φ_MIP(5), Φ_MIP(6)]`, its `law_class`, and at
  each `n` the gap `Φ_flip(n) − 2^(2−n)` against the parity-hub floor. The flip ring's synchronous period
  `P(flip_ring(n)) = 2n` is recorded.
- **Controls:** Instrument control above (`parity_hub(5) = 0.125`). The `parity_hub` curve at matched `n`
  is the decay baseline. The flip ring and the parity hub are matched on the per-node flip rule and node
  count, differing only in topology (distributed ring vs shared hub), isolating the topology as the cause
  of any divergence.
- **Decision rule (fixed before run):** H3 is **confirmed** if at `n=5` and `n=6` the flip ring sits
  strictly above the parity-hub floor, `Φ_flip(n) > 2^(2−n) + 1e-6`, and its sequence does *not* halve each
  step (its `law_class` is not `decay`, or its ratio `Φ_flip(n+1)/Φ_flip(n)` stays above 0.5 + tolerance) —
  the two diverge as `n` grows. H3 is **refuted** if `Φ_flip(n)` tracks `2^(2−n)` within `1e-6` at `n=5,6`,
  halving each step toward the same floor — the flip rule sets the decaying law wherever it sits. Pre-
  registration trial finding: `flip_ring` returns `Φ_MIP = 2.0` with the full core at `n=3` (floor 0.5) and
  `n=5` (floor 0.125), period `2n`, sitting far above the floor and not halving; H3 is expected to be
  **confirmed**, with the flip ring flat at Φ=2 while the parity hub decays past it. The `n=4,6` run fixes
  the law class.
- **Script:** `probe_q11_flip_ring_decay.py`

## H4 test — the limit-cycle family stays triadic across n
- **Form / ensemble:** Both constructed cyclers at every `n = 3,4,5,6`: the rotating ring `rot_ring(n)` and
  the periodic-commit mediated form `commit_ring(n, 2)` (commit cadence 2, a non-trivial cycle). Each is
  read with `verdict(...)` (or `classify` on the composed mediated map) for the dyadic/triadic call and with
  `major_complex(...)` for the core membership over the most-integrated reachable state.
- **Measure:** At each `n`, for each form: the binary verdict (`triadic` iff `Φ_MIP > PHI_EPS`) and the
  major-complex membership — specifically whether the core is the full `n`-node set or sheds nodes (a
  center-periphery drop, #128). Record the MIP partition repr at the max-Φ state to check it is balanced
  rather than shearing a periphery.
- **Controls:** Instrument control above. The #130 result (no attractor predicate separates the verdict) is
  the standing caveat: this test does *not* claim cycling implies triadicity in general, only that these two
  built-to-integrate cyclers land triadic. `major_complex`'s full-set return is checked against the node
  count `n` at each size; a shed node is a refutation, not a tolerance.
- **Decision rule (fixed before run):** H4 is **confirmed** if both forms read `triadic` at every
  `n=3,4,5,6` and `major_complex` returns the full `n`-node set for both at every `n`. H4 is **refuted** if
  either form reads `dyadic` at any `n`, or its core sheds at least one node at any `n` (membership drops
  below the full set). Pre-registration trial finding: `rot_ring` and `flip_ring` both return `triadic` with
  the full core at `n=3,5`; the rotating ring at `n=3,4` and the flip ring at `n=3,5` all hold the complete
  node set; H4 is expected to be **confirmed** for these constructions, with the mediated form's `n=3..6`
  run fixing it. The full-core check at `n=6` is the most expensive single value and the decisive one.
- **Script:** `probe_q11_triadic_persistence.py`

## H5 test — the detectable band widens with period: grain flips the verdict only at grain ≳ p
- **Form / ensemble:** `rot_ring(n)` for `n = 3,4,5,6`, read under a sweep of the temporal observation
  grain `g`. The grain-`g` map is the `g`-step whole-system composition of the synchronous next-state map
  (the `k_step` / coarse-grain composition used by the grain probes #32/#60): compose the synchronous
  transition `g` times into one observed transition, then classify the composed `(tpm, cm)` with
  `classify(tpm, cm, labels)`. Sweep `g = 1, 2, 3, …, n+1` at each `n` (covering the full cycle period `p =
  n` and one step past).
- **Measure:** At each `n`, the **grain-flip threshold** `g*(n)` — the smallest grain `g` at which the
  composed map reads `dyadic` (`Φ_MIP ≤ PHI_EPS`), or "none in grid" if it stays triadic through `g = n+1`.
  The pairing tested is `g*(n)` against the attractor period `p = P(rot_ring(n)) = n`.
- **Controls:** Instrument control above. The positive reference is the corpus grain result (#32/#60): the
  short-period (1–2) corpus forms flip at grain `g = 2`. The rotating ring's longer period `p = n` is the
  varied input against that fixed corpus benchmark. `g = 1` is the grain-1 baseline at which the ring is
  triadic (from H1); the sweep starts from that confirmed reading so the flip is a genuine crossing.
- **Decision rule (fixed before run):** H5 is **confirmed** if the grain-flip threshold scales with the
  period — `g*(n)` is non-decreasing in `n` and `g*(6) > g*(3)` (a wider band for the longer-period ring),
  with the flip located near `g ≈ p = n` rather than pinned at `g = 2`. H5 is **refuted** if `g*(n)` is
  fixed near 2 for every `n` (period-independent, the corpus outcome), or if the ring never flips through
  `g = n+1` at any `n` (no band to scale). Honest pre-registration caveat fixed before the run: the
  rotating ring is a reversible permutation, so its `g`-step composition is again a pure rotation by `g`
  positions and may never wash out within one period — if `rot_ring` reads triadic at every `g ≤ n+1` for
  all `n`, that is the "never flips in grid" refutation branch, and H5 is then read as refuted on this form
  even though the period is long. The decision rule adjudicates both branches; H5 stands only if a flip is
  observed and its location grows with `n`.
- **Script:** `probe_q11_grain_band.py`
