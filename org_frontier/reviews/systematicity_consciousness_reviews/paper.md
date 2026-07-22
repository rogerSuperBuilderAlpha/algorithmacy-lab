# Systematicity in Consciousness-Science Review Articles: A Framework Replication

## Research Summary

Review articles carry a field's memory. They decide which findings count as established, which
disputes remain open, and which questions are worth a newcomer's time. Simsek, Fox and Heavey (2023)
argued that reviews earn this authority only when they are systematic — when they report the method
behind the synthesis — and they measured how often management reviews do. Their answer was sobering:
reviews report a minority of the practices that make a review reproducible.

This study applies their instrument to a different literature. Forty-three review and survey articles
in consciousness science and integrated-information research were coded, three times by independent
coders, for the seven systematicity practices. The reviews report 2.6 of the seven on average, 37% of
the instrument. Reporting has risen over the past two decades. It shows no relationship with citation
impact once the age of a review is taken into account. The rarest practices are the ones that make a
review auditable: describing the search, reporting the review's own procedure, and extracting sources
into a structured scheme. Consciousness science states its questions and builds its syntheses; it
rarely shows its work.

## Introduction

Consciousness science is a young field with an old subject. As an organized empirical enterprise it
dates to the early 1990s, and in three decades it has produced a dense theoretical landscape:
integrated information theory, the global neuronal workspace, higher-order theories, predictive
processing, recurrent processing, and more. The field has recently built shared infrastructure for
adjudicating among these theories — adversarial collaborations, open databases of experiments, formal
frameworks for inter-theory comparison. Reviews have multiplied alongside the theories, and they do
heavy work: much of what a researcher outside the field believes about consciousness science comes from
a handful of high-profile overviews.

Whether those reviews are systematic is an open question, and it is answerable. Simsek, Fox and Heavey
(2023) supplied both the framework and the method. They define systematicity as an encompassing
orientation toward explicit method in reviews, decompose it into seven reportable practices, and
measure how many of the seven a review reports. Applied to 165 management reviews across three journals,
their instrument found that the average review reports well under half the practices. Their second move
matters as much as the first: they related practice count to citation impact and reported that more
systematic reviews are more cited, which turns systematicity from a virtue into an incentive.

The same instrument can be pointed at any body of reviews. Consciousness science is a demanding target.
It is younger than management as an organized field, it splits across neuroscience, philosophy, and
clinical medicine, and its reviews range from single-author narrative essays to formal PRISMA-guided
scoping reviews. The prior expectation is that its reviews are no more systematic than management's, and
plausibly less, because narrative theory-comparison is the field's dominant review genre and narrative
reviews report few practices by construction.

Three hypotheses were fixed before any source was coded. H1: consciousness-science reviews report fewer
than half the seven practices on average. H2: practice adoption has risen over the last decade. H3:
reviews reporting more practices are more cited, replicating the impact relationship Simsek, Fox and
Heavey found in management. The hypotheses were committed to the repository before the corpus was coded;
the git history is the pre-registration.

## The Systematicity Framework

The framework is Principles, Practices, Promises. Six principles — transparency, completeness,
saturation, connectedness, universalism, coherence — describe what a systematic review aspires to. Four
promises — richness, reproducibility, trustworthiness, utility — describe what it delivers. Between them
sit the seven practices, each the reportable trace of one stage of doing a review. The practices are
what a coder can observe, so the practices are what this study measures.

- **Envisioning** is stating an explicit orienting question, objective, or review type. A review that
  names itself a scoping review, or asks whether the theories of consciousness are converging, has
  envisioned. A review that only announces a topic has not.
- **Explicating** is stating the boundary conditions: the scope, the inclusion window, which
  literatures are in and which are out. "Articles published between 2007 and 2017" is explicating.
- **Executing** is describing how the sources were found or assembled: a database search, search terms,
  screening counts, a stated corpus size. This is the practice a narrative review most often lacks.
- **Evaluating** is appraising or weighing the evidence, not only summarizing it — a quality
  criterion, a comparison rubric, a judgment about which theory predicts better.
- **Encoding** is extracting sources into a structured scheme: a grid, a taxonomy, a set of dimensions,
  a classification applied across the sources.
- **Elaborating** is building something beyond summary — a synthesis, an integration, a new framework,
  a research agenda developed from the coded material.
- **Expositing** is reporting the review's own procedure transparently enough to be reproduced: a
  PRISMA flow, a preregistration, an open dataset, a described sequence of steps.

The seven are not equally demanding. Envisioning and elaborating are close to the minimum a review must
do to be a review at all. Executing, encoding, and expositing are the practices that separate a
systematic review from a well-read essay, and they are the practices this study finds scarce.

## Method

**Corpus.** The unit of analysis is a review of the consciousness-science literature: a review, survey,
overview, scoping, or synthesis article whose subject is the theory, neural correlates, or measurement
of consciousness. Primary experiments, single-measure methods papers, bare adversarial-collaboration
reports, protocols, editorials, and book reviews are out of scope, because the unit is a review of a
literature rather than a contribution to it. Candidates were harvested with two academic
semantic-search connectors over eight review-oriented queries spanning theories of consciousness,
integrated information theory, neural correlates, global workspace and higher-order theories,
computational models, predictive processing, clinical markers, and machine consciousness. The returns
were merged, deduplicated by title, and screened against a decidable boundary rule; screened-out
candidates are logged. Citation counts were enriched from Semantic Scholar by DOI. The final corpus is
43 reviews spanning 2001 to 2026.

**Coding.** The codebook gives each practice a one-line operational rule for judging it from a title and
abstract, with a conservative default: a practice counts as present only when the abstract shows
positive evidence that the review performed it. Three coders applied the codebook independently and
blind to one another, each producing a full set of judgments for all 43 reviews. The coders are LLM
agents running the same fixed codebook in parallel, a design that makes the reliability figure
meaningful only among agent passes, a limitation returned to below.

**Analysis.** Intercoder reliability is Fleiss' kappa per practice, with a majority-vote adjudicated
dataset. H1 compares the mean practice count against 3.5, half the instrument. H2 correlates practice
count with publication year. H3 correlates practice count with citation count using Spearman's rho,
appropriate for heavy-tailed citation data, with the practice-count-versus-age relationship reported
alongside as a pre-registered confound. All statistics use standard-library implementations; the
pipeline reproduces end to end from three commands.

## Results

The three coders agreed substantially to almost perfectly. Fleiss' kappa was 1.00 for envisioning,
executing, and expositing, 0.93 for encoding, 0.74 for elaborating, and 0.66 for explicating and
evaluating, a mean of 0.86. The two practices with the lowest kappa are the two whose abstract-level
cues are most a matter of degree, and both sit in Landis and Koch's substantial band. The reliability
figure answers the objection that a single reader's judgment drives the result.

**H1 — supported.** The 43 reviews report 2.60 of the seven practices on average, 37% of the instrument,
below the 3.5 threshold. The distribution is concentrated at the low end: one review reports no
practice, ten report one, nine report two, and fourteen report three. Four reviews report five or more.
None report all seven. Twenty of the 43 report two practices or fewer. Consciousness-science reviews, on
this measure, are less systematic than the management reviews Simsek, Fox and Heavey coded, and the
central pattern they reported — reviews report a minority of the practices — holds in the new field.

The per-practice adoption table shows where the shortfall lives.

| practice | reviews reporting | share |
|---|---|---|
| envisioning (stated question / review type) | 42/43 | 98% |
| elaborating (synthesis, framework, agenda) | 29/43 | 67% |
| evaluating (appraisal of evidence/theories) | 18/43 | 42% |
| explicating (boundary conditions) | 13/43 | 30% |
| encoding (structured extraction scheme) | 5/43 | 12% |
| executing (described search / assembly) | 3/43 | 7% |
| expositing (transparent, reproducible method) | 2/43 | 5% |

Almost every review states a question, and two-thirds build a synthesis. Fewer than one in ten describe
how they searched for their sources, and one in twenty report their own procedure transparently enough
to reproduce. The field's reviews are strong at the practices that define a review and weak at the
practices that make one auditable. The three scarcest practices — executing, expositing, encoding — are
exactly the ones that distinguish a systematic review from a narrative overview, and the corpus is
dominated by narrative overviews.

A few reviews report the full apparatus. Sattin and colleagues' (2021) scoping review of theoretical
models states its inclusion window, its screening counts, and its thematic grid, scoring across the
demanding practices. Guerrero and colleagues' (2023) systematic review of integrated information theory
and Chis-Ciure and colleagues' (2024) measure-centrality framework likewise report encoding schemes.
These are the recent arrivals, and their timing is the subject of H2.

**H2 — supported.** Practice count rises with publication year: Pearson r = +0.30 (p = 0.05), Spearman
rho = +0.37. The systematic reviews cluster in the last several years. The field's early reviews are the
narrative theory-comparisons and framework statements that founded the modern literature; its recent
reviews increasingly adopt scoping-review and PRISMA-style machinery. Systematicity is diffusing into
consciousness science, slowly, and from a low base.

**H3 — challenged.** More practices do not bring more citations. The rank correlation between practice
count and citation count is slightly negative and indistinguishable from zero: Spearman rho = -0.12
(p = 0.46). The pre-registered confound accounts for the result. Citations accumulate with age, strongly
so in this corpus — cites correlate with year at Spearman rho = -0.75, older reviews far more cited — and
H2 established that the systematic reviews are the young ones. The most-cited reviews here are the
field-defining narrative overviews of 2001 to 2016: Dehaene and colleagues on the workspace framework,
Tononi and colleagues on integrated information theory, Baars on global workspace theory. They report
few practices and carry thousands of citations because they are old and foundational. The recent scoping
and systematic reviews report more practices and have not yet been cited. Practice count and impact are
confounded by time, and in this cross-section the reward relationship Simsek, Fox and Heavey reported for
management does not appear. The result bounds a claim without reversing one: systematicity is not
visibly rewarded in a field measured at a single moment, midway through its methodological turn.

## Discussion

The headline is a shortfall with a shape. Consciousness-science reviews report about a third of the
systematicity practices, and the third they report is predictable: they state questions and synthesize,
they do not describe searches or expose their method. This is the signature of a field whose review
genre is the authored theory-comparison — the essay that surveys integrated information theory, global
workspace, and their rivals and argues for a reading of the landscape. That genre is valuable. It is
also, by construction, low on the practices that make a review reproducible, and a field that leans on
it inherits a reproducibility gap in its secondary literature.

The trend is the encouraging part. Adoption is rising, and the mechanism is visible in the corpus: the
scoping reviews and systematic reviews that report the demanding practices are recent, and the tools
they use — PRISMA reporting, open experiment databases, formal comparison frameworks — arrived with the
field's turn toward theory-adjudication. The instrument registers a field in transition. A replication
in five years would test whether the mean practice count continues to climb.

The impact null is the finding that most resists a tidy reading, and its confound is the point rather
than a nuisance. In management, systematicity and citation rose together; in consciousness science,
measured now, they do not, because the systematic reviews have not had time to be cited and the
foundational overviews were never systematic. Whether systematicity pays in consciousness science cannot
be settled from a single cross-section dominated by age effects. The honest statement is that the reward
is not yet visible, and that a longitudinal design controlling for age is what would reveal it.

For a field building shared infrastructure for theory-adjudication, the scarce practices are the ones
worth cultivating. A review that describes its search, extracts theories into a structured scheme, and
reports its own procedure is a review the field can build on rather than re-litigate. The instrument
does not merely grade; it names the three practices — executing, encoding, expositing — whose adoption
would raise the field's mean the fastest.

## Limitations

Four limitations bound the result. First, coding was from titles and abstracts, not full text. An
abstract underreports method, so the practice counts are a floor on reported systematicity, and the two
scarcest practices, executing and expositing, are the ones this design most likely undercounts; the
direction of the bias is stated rather than corrected. Second, the coders are LLM agents applying a
fixed codebook, not trained human raters. Agreement among agent passes is high — mean kappa 0.86 — but
agreement among agents is not agreement with expert human coders, and the reliability figure should be
read as internal consistency of the instrument, not external validity. Third, the corpus comes from two
semantic-search connectors over eight queries, screened by a boundary rule, not an exhaustive
database census; it is bounded by the connectors' coverage and by English-language indexing, and it
skews toward theory and measure reviews over clinical ones. Fourth, this is a homage rather than a
full-scale replication: Simsek, Fox and Heavey coded 165 management reviews from full text, and this
study coded 43 consciousness-science reviews from abstracts. It reproduces their central pattern and
challenges their impact claim in a young field, and it makes no claim to their sample size or their
full-text depth.

## References

Baars, B. J. (2005). Global workspace theory of consciousness: toward a cognitive neuroscience of human
experience. *Progress in Brain Research*, 150, 45-53.

Chis-Ciure, R., et al. (2024). A Measure Centrality Index for Systematic Empirical Comparison of
Consciousness Theories. *Neuroscience and Biobehavioral Reviews*, 161, 105670.

Dehaene, S., & Naccache, L. (2001). Towards a cognitive neuroscience of consciousness: basic evidence
and a workspace framework. *Cognition*, 79(1-2), 1-37.

Guerrero, L. E., et al. (2023). A systematic review of integrated information theory: a perspective from
artificial intelligence and the cognitive sciences. *Neural Computing and Applications*, 35, 7575-7607.

Sarasso, S., et al. (2021). Consciousness and complexity: a consilience of evidence. *Neuroscience of
Consciousness*, 2021(2), niab023.

Sattin, D., et al. (2021). Theoretical Models of Consciousness: A Scoping Review. *Brain Sciences*,
11(5), 535.

Seth, A. K., & Bayne, T. (2021). Theories of consciousness. *Nature Reviews Neuroscience*, 23, 439-452.

Signorelli, C. M., et al. (2021). Explanatory profiles of models of consciousness — towards a systematic
classification. *Neuroscience of Consciousness*, 2021(2), niab021.

Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in Organizational Research Literature
Reviews: A Framework and Assessment. *Organizational Research Methods*, 26(2), 292-321.
doi:10.1177/10944281211008652

Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling Questions in Research: Seeing What
Everybody Has Seen and Thinking What Nobody Has Thought. *Journal of Management*, 48(6).
doi:10.1177/01492063211073068

Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). Integrated information theory: from consciousness
to its physical substrate. *Nature Reviews Neuroscience*, 17(7), 450-461.

*Full corpus (43 reviews) with DOIs and harvested citation counts: `literature/references.bib` and
`literature/corpus.jsonl`.*
