# Findings — consciousness-science reviews report about a third of the systematicity practices

Forty-three review and survey articles in consciousness science, coded on Simsek, Fox & Heavey's seven
systematicity practices, report 2.6 of the seven on average — 37% of the instrument. The instrument
that found management reviews well short of full systematicity finds the same shortfall, deeper, in a
younger and more fragmented field. Adoption has risen with time. It does not track citations.

## Intercoder reliability
Three independent agent coders, blind to one another, coded each review from its title and abstract.
Fleiss' kappa across the seven practices:

| practice | Fleiss' kappa | agreement | interpretation |
|---|---|---|---|
| envisioning | 1.000 | 100.0% | almost perfect |
| explicating | 0.659 | 84.5% | substantial |
| executing | 1.000 | 100.0% | almost perfect |
| evaluating | 0.658 | 82.9% | substantial |
| encoding | 0.929 | 98.4% | almost perfect |
| elaborating | 0.743 | 89.1% | substantial |
| expositing | 1.000 | 100.0% | almost perfect |

Mean kappa 0.856. The two lowest, explicating (boundary conditions) and evaluating (appraisal), are the
practices whose abstract-level cues are most a matter of degree; both remain in the substantial band.
The kappa figure is what a single-coder review cannot report, and it discharges the "one reader coded
it" objection.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | Reviews report fewer than half the seven practices (mean < 3.5) | **Supported** | mean = 2.60 of 7 (37%), N = 43 |
| H2 | Practice adoption has risen over time | **Supported** | practice count vs year: Pearson r = +0.30 (p = 0.05), Spearman rho = +0.37 |
| H3 | Reviews reporting more practices are more cited | **Challenged** | practice count vs cites: Spearman rho = -0.12 (p = 0.46) |

### Per-practice adoption
| practice | reviews reporting | share |
|---|---|---|
| envisioning (stated question / review type) | 42/43 | 98% |
| elaborating (synthesis, framework, agenda) | 29/43 | 67% |
| evaluating (appraisal of evidence/theories) | 18/43 | 42% |
| explicating (boundary conditions) | 13/43 | 30% |
| encoding (structured extraction scheme) | 5/43 | 12% |
| executing (described search / assembly) | 3/43 | 7% |
| expositing (transparent, reproducible method) | 2/43 | 5% |

Practice-count distribution across the 43 reviews: 0->1, 1->10, 2->9, 3->14, 4->5, 5->2, 6->2, 7->0.
Twenty of 43 reviews report two practices or fewer; four report five or more; none report all seven.

## What the data revise
H3 is the one the data overturn. More practices do not bring more citations in this corpus; the rank
correlation is slightly negative and not distinguishable from zero. The pre-registered confound explains
why: citations rise with age (cites vs year Spearman rho = -0.75 — older reviews are far more cited),
and H2 shows the systematic reviews are the recent ones. The most-cited reviews here are the
field-defining narrative overviews from 2001-2016 (Dehaene 2001, Tononi 2016, Baars 2005), which predate
the field's turn toward explicit method and report few practices. The recent scoping and systematic
reviews report more practices but have not yet accumulated citations. Practice count and impact are
confounded by time, and once time is in view the reward relationship Simsek, Fox & Heavey reported for
management does not appear in this cross-section. This is a finding about a young field measured at one
moment, not a verdict that systematicity is unrewarded.

The rarest practices name the field's methodological gap precisely: describing the search (executing,
7%), reporting the review's own method transparently (expositing, 5%), and extracting sources into a
structured scheme (encoding, 12%). Consciousness-science reviews overwhelmingly state a question (98%)
and build a synthesis (67%); they seldom show how they found and appraised what they synthesized.

## Limitations
- **Abstract-only coding.** Practices were coded from title and abstract, not full text. An abstract
  underreports method — a review with a full PRISMA appendix may not say so in 200 words. The practice
  counts are therefore a floor on reported systematicity, and executing/expositing are the practices
  most likely undercounted by this design. The direction of the bias is stated, not corrected.
- **Agent coders.** The three coders are LLM agents applying a fixed codebook, not trained human raters.
  Fleiss' kappa among agent passes is high (mean 0.86) but measures agreement among agents, not
  agreement with expert human coders. This is the arm's shared limitation.
- **Corpus construction.** The corpus is built from two semantic-search connectors over eight
  review-oriented queries, screened by a decidable boundary rule, not from an exhaustive database
  census. It is bounded by the connectors' coverage and by English-language indexing, and it skews
  toward theory/measure reviews over clinical ones. N = 43 supports the H1 mean and the H2 trend; the
  H3 null is reported with its confound rather than as a precise zero.
- **Not a replication of magnitude.** Simsek, Fox & Heavey coded 165 management reviews from full text.
  This is a smaller, abstract-level homage in a different field; it reproduces their central pattern
  (reviews report a minority of practices) and tests their impact claim, which it does not reproduce
  here.

## Reproduce
```bash
python -m org_frontier.reviews.systematicity_consciousness_reviews.build_corpus
python -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/systematicity_consciousness_reviews/coding \
    --categorical envisioning,explicating,executing,evaluating,encoding,elaborating,expositing \
    --out org_frontier/reviews/systematicity_consciousness_reviews/results/frozen.json
python -m org_frontier.reviews.systematicity_consciousness_reviews.run
```
Registered numbers: N = 43; mean practices = 2.60; mean kappa = 0.86; H2 r = +0.30 (p = 0.05); H3
rho = -0.12 (p = 0.46). See `results/summary.json`.
