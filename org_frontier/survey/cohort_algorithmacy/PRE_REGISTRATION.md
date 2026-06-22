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

*None. Any change after Wave 1 opens is added here with a date and a reason, and the original text above
is left unchanged.*
