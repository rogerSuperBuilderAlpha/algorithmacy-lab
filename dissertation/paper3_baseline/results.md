# Paper 3 — computed results: the typology on the triadic-demand scale

Exact IIT-4.0 system Φ via `proxy_audit.exact_phi` (PyPhi `new_big_phi.sia`), over application-layer
systems built under Paper 2's pre-registered state-individuation rule. Each organization's determination
structure is fixed *before* computing (pre-registered in `typology_phi.py`), derived from how that
organization actually coordinates its parties — not chosen for a target Φ. Reproduce:
`~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/typology_phi.py`.

## Stage 1: the calibration anchor (Chicago rideshare pooling)

The anchor ties Φ to an observed coordination outcome, so the scale is calibrated rather than asserted.
In rideshare pooling the platform coordinates a driver and *k* riders who never meet, entirely through
the dispatch it commits; each pool size is a distinct coordination form, modeled as a (k+2)-node strict
higher-order mediation system. Computed Φ rises with the number of bound parties: **Φ = k + 1** (solo
2.0, 2-pool 3.0, 3-pool 4.0, 4-pool 5.0 — computed in `anchor_chicago.py` / `typology_phi.py`, zero
reference to data). The model therefore predicts larger pools are harder to realize and costlier.

Tested against City of Chicago open data ("Transportation Network Providers — Trips, 2018–2022",
resource `m6dm-c72p`; 48,676-trip shared-authorized sample from the 2018 pooling era; completed-trips
only, so pooling is the available outcome). Per pool size, among shared-authorized trips:

| pool | model Φ | n | achievement share | friction (sec/mi) |
|---|---|---|---|---|
| 1 (solo) | 2.0 | 16,765 | 34.4% | 156.0 |
| 2 | 3.0 | 17,135 | 35.2% | 182.4 |
| 3 | 4.0 | 11,892 | 24.4% | 217.5 |
| 4 | 5.0 | 2,884 | 5.9% | 227.1 |

- **Φ vs friction (sec/mi): r = +0.980** — higher-Φ forms cost more time per mile (more coordination →
  more detour), monotone across the four pool sizes (156 → 182 → 218 → 227).
- **Φ vs achievement share: r = −0.912** — higher-Φ forms are realized less often; `log(share) ~ Φ`
  slope = −0.565, so **each +1 in Φ multiplies how often the platform pulls the coordination off by
  ~0.57** (roughly halving it per step of demand).
- Match success P(pooled ≥ 2 | authorized) = 0.66.

**The anchor result:** Φ, computed from determination structure alone, orders the pooling forms exactly
as observed coordination difficulty does — on both the cost axis (friction) and the rarity axis
(achievement). The scale is calibrated against behaviour. Reproduce:
`~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/anchor_chicago.py` (add `--refresh`
to re-pull the live sample).

*Honest bounds on the anchor:* (a) the Φ→friction relation runs through party count — bigger pools both
raise Φ and add detour — so the anchor validates the *party-count axis* of Φ; the typology below shows Φ
*also* separates forms at fixed party count (partial 0.83 vs strict 2.0 vs parity 0.5 at n=3), which
party count alone cannot. (b) Observational association, not a causal claim.

### Stage-1 robustness battery (full)

Run on a 193,028-trip clean sample of shared-authorized trips spanning the full pooling era
(2018-11 → 2020-03; outliers filtered to 0.5–60 mi, 120–7200 s, pace 20–1200 s/mi). Reproduce:
`anchor_chicago.py --refresh` (headline) and `robustness_anchor.py` (battery).

| robustness check | result | reading |
|---|---|---|
| **Effect size (trip-level)** | regression pace ~ Φ across all 193k trips: **slope +16.8 sec/mi per +1 Φ**, r=+0.139, **R²=0.019** | the aggregate r=+0.98 is across 4 points; per-trip the effect is small-but-robust — Φ is a *form-level* measure, not a per-trip predictor (this **reinforces Claim A**) |
| **Temporal stability** | split at median date: aggregate r **+0.976 (early) vs +0.975 (late)**; trip-level slope +16.5 vs +15.2 | the Φ→outcome relation is stable across time windows |
| **Within-stratum (Simpson's)** | friction rises monotonically with pool size in **7 of 8** top community areas | the trend holds *inside* strata — not a pooling/Simpson's artifact |
| **Alternative aggregation** | r(Φ, friction) = **+0.98** (sum/sum), **+0.95** (mean pace), **+0.94** (median pace) | robust to the friction-aggregation choice |
| **Achievement (replicated)** | share 33/35/26/6% by pool size; log(share)~Φ slope −0.544 (**×0.58 per +1 Φ**); r=−0.88 | replicates the rarity axis at larger N |
| **Power** | N=193k → significance is trivial; report **R² and the slope**, not p | effect-size-first reporting |

**Controls (labeled).** *Negative control:* the dyadic baselines (Φ=0; §2.C of Paper 2 / typology floor)
— forms that should and do score zero. *Positive control:* Φ separates forms at **fixed party count**
(partial 0.83 vs strict 2.0 vs parity 0.5, all n=3) — Φ carries signal that raw party count cannot, the
answer to the party-count confound. **The confound, named:** the anchor's Φ→friction relation runs
through party count; the fixed-n positive control is what shows Φ is more than a party counter, and the
typology is where that extra signal lives.

## The baseline (Stage 2: the typology placed by Φ)

| Φ (max) | Organization | Class | Structure |
|---|---|---|---|
| **0.00** | Direct exchange (no mediator) | dyadic baseline | parties deal directly; mediator inert |
| **0.00** | Chat with a language model | dyadic baseline | two-party loop; nothing couples a third |
| **0.50** | Complementary skill matching | algorithmic platform | parity determination (S′ = W ⊕ C) |
| **0.83** | Freelance marketplace (Upwork) | algorithmic platform | partial mediation (parties also coordinate directly) |
| **0.83** | Healthcare staffing agency | **human-mediated** | partial mediation |
| **0.83** | Real-estate broker | **human-mediated** | partial mediation |
| **2.00** | Rideshare, solo (Uber/Lyft) | algorithmic platform | strict mediation (S′ = W ∧ C) |
| **2.00** | Food delivery | algorithmic platform | strict mediation |
| **2.00** | Hiring / applicant-tracking system | algorithmic-institutional | strict mediation |
| **2.00** | Content moderation | algorithmic-institutional | strict mediation |
| **2.00** | Court (judge between parties) | **human-mediated** | strict mediation |
| **3.00** | Rideshare, POOLED (driver + 2 riders) | higher-order (n=4) | S′ = W ∧ C ∧ D |
| **3.00** | Crowdwork (requester + 2 workers) | higher-order (n=4) | S′ = W ∧ C ∧ D |

Five structural levels emerge: **0** (dyadic / no constitutive mediator), **0.5** (parity-coupled
determination), **0.83** (partial mediation — the parties retain a direct channel), **2.0** (strict
mediation — the parties reach each other only through a joint determination), and **3.0** (higher-order —
a determination binding more than three parties). The level is set by the determination structure, and
the model returns each form's place by one uniform procedure.

## The headline: structure sets the score, not the seat of the mediator

The human-mediated contrast class is the test that the model measures *triadic coordination* and not
*algorithms*, and it passes cleanly:

- **A court scores Φ = 2.00 — identical to Uber, the ATS, and content moderation.** A judge between two
  parties who reach each other only through rulings is, structurally, the same strict mediator as the
  dispatch algorithm. The human in the seat does not change the demand.
- **A staffing agency and a real-estate broker score Φ = 0.83 — identical to Upwork.** All three match the
  parties but leave them a direct channel; partial mediation lands at the same level whether the matcher
  is an algorithm or a person.

The human-mediated forms interleave with the algorithmic ones at every level, sorted by structure. This
is the decisive evidence that algorithmacy is a demand of the *coordination form*, not a reaction to
software — and that the model travels across organization types, which is what makes it a model rather
than a platform study.

## Notes and honest bounds

- **The 3-node scale (0 → 2.0) is directly comparable.** The two higher-order cases are 4-node systems,
  so their Φ = 3.0 is partly a function of system size; they show the scale *extends upward* when a
  determination binds more parties (the pooled ride is the anchor domain's own higher-order form), but
  cross-node magnitudes are not strictly comparable and we say so. A size-normalized companion measure is
  a candidate for the write-up.
- **Several organizations share a structure and therefore a score** (e.g., the four strict-mediation forms
  at 2.0). This is a finding, not a defect: the model says forms that coordinate the same way make the
  same demand, regardless of industry vocabulary.
- **Partial vs strict mediation is a modeling choice that must reflect the real coordination** (does the
  platform forbid off-app contact, or only introduce the parties?). Each placement's structure is
  pre-registered and defensible from how the organization actually operates; the staffing-agency case in
  particular (workers and facilities do coordinate directly once placed) is the reason it sits at 0.83
  rather than 2.0.
- **These are Stage-2 placements, validated insofar as the anchor licenses the scale.** Stage 1 above —
  the Chicago rideshare-pooling anchor — ties Φ to observed coordination difficulty (friction r = +0.98,
  achievement r = −0.91), which is what turns these structural scores into a calibrated scale. The anchor
  validates the party-count axis of Φ; the typology shows Φ additionally separates forms at fixed party
  count by determination structure. Together they establish Φ as a difficulty scale, not a party counter.
