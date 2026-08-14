# Pre-registration — cohort algorithmacy panel

Commit this file before fielding any wave. It fixes the questions before the answers, and the git
history is the evidence that it did. Nothing here is revised after Wave 1 opens; a change of plan is a
new dated entry under "Amendments," never an edit to what was registered.

## Protocol metadata

- **Study.** Three-wave longitudinal panel of algorithmacy in the Hult Cohort Program, Fall 2026.
  Registered title: "Algorithmacy: Validating a measure of communication competency in AI-mediated work."
- **Principal investigator.** Roger Hunt, Executive PhD student, Management, Bentley University.
- **IRB of record.** Bentley University Institutional Review Board (IRB#1, FWA00007335). Protocol 260511078,
  determined exempt under 45 CFR 46.102(e)(2)(ii) on May 11, 2026. Consent version fielded: `consent.md`
  v1.0. A substantial change to the consent, the study design, or the protocol requires a Research
  Progress & Review Form to the IRB before fielding.
- **Field site.** Hult Cohort Program, Fall 2026 cohort.
- **Design registered on.** `<COMMIT DATE — set by the commit that lands this file>`, before Wave 1 opens.
- **Waves.** W1 baseline (before week 1); W2 (week 4, after the first build-and-review cycle); W3 (end of
  session, week 16).
- **Population.** All enrolled participants; voluntary; not a condition of enrollment or assessment.
- **Linkage.** A one-way hash of the GitHub handle links a participant's waves without storing the handle
  beside responses.

## Constructs and where each is measured

| Construct | Source | W1 | W2 | W3 |
|---|---|:--:|:--:|:--:|
| Algorithmacy competence — counterpart inference | purpose-built | ✓ | ✓ | ✓ |
| Algorithmacy competence — signal compression | purpose-built | ✓ | ✓ | ✓ |
| Algorithmacy competence — rule-change tracking | purpose-built | ✓ | ✓ | ✓ |
| Perceived task interdependence (reciprocal) | Pearce & Gregersen 1991; Van der Vegt et al. 2001 | ✓ | ✓ | ✓ |
| Perceived system authority (commit vs. convey) | purpose-built, anchored in Lee 2018 | | ✓ | ✓ |
| Algorithmic competency, adapted (discriminant rival) | Zhou et al. 2025, items adapted to this setting | | ✓ | |
| Job autonomy (method/scheduling/criteria) | Breaugh 1985 | ✓ | ✓ | ✓ |
| Psychological ownership (built platform) | Van Dyne & Pierce 2004 | | ✓ | ✓ |
| Transactive memory system | Lewis 2003 | | ✓ | ✓ |
| Perceived substitutability | purpose-built, exploratory | ✓ | ✓ | ✓ |
| General self-efficacy | Chen, Gully & Eden 2001 | ✓ | | ✓ |
| Sense of belonging | Walton & Cohen 2007 | ✓ | ✓ | ✓ |
| Demographics & background | — | ✓ | | |
| Program experience & open response | — | | | ✓ |

Item text, response scales, reverse keys, and scoring are in [`codebook.md`](codebook.md). The fielded
forms are in [`instruments/`](instruments/).

## Hypotheses, nulls, and decision rules

Directional hypotheses are tested one-tailed at α = .05; all others two-tailed at α = .05. Each
hypothesis names the null it is tested against. The small-sample stance in
[`analysis_plan.md`](analysis_plan.md) governs which tests are confirmatory and which are exploratory;
H1 and H2 are the confirmatory core.

**RQ1 — measurement.**

- **H1a (structure).** The Algorithmacy Competence Scale items load on three correlated factors
  (counterpart inference, signal compression, rule-change tracking). *Null:* a one-factor or
  non-converging structure fits as well or better. *Rule:* at W1, exploratory factor analysis recovers
  three interpretable factors; at W2 and W3, a three-factor confirmatory model fits (CFI ≥ .90,
  RMSEA ≤ .08, SRMR ≤ .08) and beats the one-factor model by Δχ²/ΔCFI.
- **H1b (reliability).** Each facet and the total score reach McDonald's ω ≥ .70 at each wave. *Null:*
  ω < .70. *Rule:* ω with bootstrap CI reported per facet per wave.
- **H1c (invariance).** The scale holds configural, metric, and scalar invariance across waves. *Null:*
  metric or scalar invariance fails. *Rule:* nested-model comparison, ΔCFI ≤ .01 and ΔRMSEA ≤ .015 at
  each step; partial invariance reported if a step fails.

**RQ2 — development.**

- **H2 (growth).** Algorithmacy competence increases from W1 to W3. *Null:* the latent slope mean is ≤ 0.
  *Rule:* in a latent growth / multilevel model, the linear slope mean is positive and its 95% CI
  excludes 0 (one-tailed). Facet-level slopes are reported alongside the total.

**RQ3 — nomological relations.** Estimated within- and between-person; between-person estimates are
exploratory given sample size.

- **H3a.** Perceived task interdependence is positively associated with algorithmacy competence. *Null:*
  association ≤ 0.
- **H3b.** Perceived system authority (commit) is positively associated with algorithmacy competence.
  *Null:* association ≤ 0.
- **H3c.** Psychological ownership over the built platform is positively associated with algorithmacy
  competence and increases from W2 to W3. *Null:* association ≤ 0 and slope ≤ 0.
- **H3d.** Transactive memory system strength is positively associated with perceived coordination and
  with algorithmacy competence. *Null:* associations ≤ 0.
- **H3e (exploratory).** Perceived substitutability is negatively associated with psychological ownership
  and with algorithmacy competence. *Null:* associations ≥ 0.
- **Discriminant check.** Algorithmacy competence is distinguishable from general self-efficacy (latent
  correlation < .85) and explains variance in RQ3 relations beyond it.
- **H4 (discriminant vs. the published rival).** At W2, algorithmacy competence is distinguishable from
  adapted algorithmic competency (Zhou et al. 2025). *Null:* the two are empirically the same construct.
  *Rules, all fixed before fielding:* (a) a two-factor model at the second-order level fits better than a
  single-factor model by Δχ²/ΔCFI, and the latent correlation is **< .85**; (b) each scale's AVE exceeds
  their shared variance (Fornell–Larcker); (c) algorithmacy competence explains incremental variance in
  the RQ3 relations beyond ZAC. **Directional sub-predictions, registered so they cannot be claimed after
  the fact:** ZAC-Leveraging correlates most strongly with signal compression, ZAC-Understanding with
  counterpart inference, and **ZAC-Embracing correlates weakly or not at all with any algorithmacy facet**
  — it is an attitude toward the system, which algorithmacy does not claim to measure. A latent
  correlation ≥ .85, or a single factor fitting as well, falsifies the claim that algorithmacy is a new
  construct rather than a relabelling.

## What would falsify the account

Written before the data, reported in `FINDINGS.md` whether or not met.

- The three facets do not separate, or collapse to one undifferentiated factor — the construct's named
  structure is not in the data.
- The scale fails metric invariance across waves — any apparent change cannot be read as change in the
  same construct.
- The algorithmacy slope is flat or negative — sustained mediated coordination does not build the
  competence as the account predicts.
- Algorithmacy competence is empirically indistinguishable from general self-efficacy — the scale
  measures generic confidence, not the specific competence.
- Algorithmacy competence is empirically indistinguishable from adapted algorithmic competency (Zhou et
  al. 2025) — the construct is a relabelling of a measure that already exists, and the contribution is
  the setting, not the scale.
- Algorithmacy competence is unrelated to perceived task interdependence and to perceived system
  authority — the construct does not track the conditions the catalog says make a mediated arrangement
  bind.

## Stopping and inclusion rules

- **Inclusion.** A response counts if consent is recorded and at least one full scale is complete. A wave
  closes at its window's end; late responses are not accepted.
- **Attrition.** Reported per wave with a logistic check of completion on W1 variables; FIML is used under
  missing-at-random, and the assumption's sensitivity is examined.
- **No optional stopping.** Analyses run after W3 closes. No hypothesis test is run on partial data, and
  no hypothesis is added or dropped after data are seen except as a dated amendment below.

## Amendments

*Any change after Wave 1 opens is added here with a date and a reason, and the original text above is
left unchanged.*

**2026-08-13 — added the Zhou et al. (2025) discriminant block to W2 (registered, not an amendment).**
Wave 1 has not opened, so this is a change to the registered design made before any data exists, and it
is written into the sections above rather than bolted on here. It is logged for the same reason the
registration exists: the git history should show when the questions were fixed. **What changed:** twelve
adapted items (`zac_*`) added as W2 Part 8, a construct row, hypothesis **H4** with its decision rules
and directional sub-predictions, and a fifth falsification condition. **Why:** verification of the Lima
abstract's citations surfaced Zhou et al. as a validated rival scale for competency in algorithmically
mediated work, published while this instrument was being built. A construct claim that does not test
against the one published rival is not worth making. **Cost:** W2 goes from about 13 minutes to about 15.

> **⚠ IRB — this gates fielding, and it is the author's call.** Protocol 260511078 was determined exempt
> on the design as registered in May 2026. Adding a measure and lengthening the instrument may count as
> a change to the study design, which per the metadata above requires a Research Progress & Review Form
> to the Bentley IRB **before** W2 fields. It probably does not disturb the exempt determination — no new
> population, no new risk, no change to consent — but that judgment belongs to the IRB, not to this
> file. **File or confirm before W2 opens.** Consent v1.0 already describes the surveys generically; check
> whether it needs no change.

> **Note for the GauntleTT arm.** These instruments are registered for the **Hult** cohort, Fall 2026,
> W1/W2/W3 at weeks 0/4/16. The Lima PDW paper (`../../lima_pdw/`) promises a panel on **GauntleTT** in
> Trinidad and Tobago at weeks 1/4/8, under a different IRB approval. If the discriminant test is to
> appear in that paper, the same block has to be added to that instrument, under that approval, and
> fielded there. Nothing in this file covers it.
