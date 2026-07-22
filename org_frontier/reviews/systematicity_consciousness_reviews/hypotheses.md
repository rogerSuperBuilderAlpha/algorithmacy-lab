# Hypotheses — systematicity in consciousness-science review articles

*Committed before any corpus is coded. A direct homage to Simsek, Fox & Heavey (2023), who coded 165
management reviews for the seven systematicity practices and related practice count to citation impact.
This review applies the same instrument to a different field: review and survey articles in consciousness
science and integrated-information research. Each hypothesis names the knowledge claim it tests, its
operationalization, and the outcome that would support versus challenge it.*

The orienting question is descriptive-evaluative: how systematic are review articles in consciousness
science, measured by the seven practices, and does systematicity track time and impact? Simsek, Fox &
Heavey found that management reviews reported well under half of the practices on average. Consciousness
science is younger as an organized field, is split across neuroscience, philosophy, and clinical
medicine, and has only recently built shared infrastructure (adversarial collaborations, the ConTraSt
database). The prior is that its reviews are no more systematic than management's, and likely less.

## H1 — Fewer than half the practices, on average
- **Knowledge claim (stylized fact, imported):** review articles report a minority of the seven
  systematicity practices; explicit method is the exception, not the rule (Simsek, Fox & Heavey's
  central empirical finding in management).
- **Operationalization:** for each review, count how many of the seven practices (envisioning,
  explicating, executing, evaluating, encoding, elaborating, expositing) the title+abstract shows
  evidence of. Take the mean across the adjudicated corpus.
- **Predicts:** mean practices reported < 3.5 (fewer than half of seven).
- **Challenged if:** mean ≥ 3.5.

## H2 — Adoption rising over the last decade
- **Knowledge claim (substantive omission closing):** systematicity is diffusing into the field;
  reporting of the practices has increased over time as the field professionalized its methods.
- **Operationalization:** correlate each review's practice count with its publication year (Pearson r
  and Spearman ρ over the dated corpus).
- **Predicts:** a positive correlation between year and practice count.
- **Challenged if:** the correlation is null or negative.

## H3 — More practices, more cited
- **Knowledge claim (key assumption, imported):** systematicity is rewarded; reviews that report more
  practices accrue more citations, as Simsek, Fox & Heavey reported for management.
- **Operationalization:** Spearman ρ between practice count and citation count over the corpus (Spearman
  because citation counts are heavy-tailed).
- **Predicts:** a positive ρ between practice count and cites.
- **Challenged if:** ρ ≤ 0, or the relation is explained entirely by publication year (older = more
  cited and, if H2 holds, fewer practices — a confound stated in advance).

## Method fixed in advance
- Corpus boundary and search: `methods.md` (substantive + procedural gates; two semantic-search
  connectors over eight review-oriented queries; screen to review/survey articles).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`, coding each of the
  seven practices present/absent from title+abstract.
- Reliability reported (Fleiss' κ per practice). Any hypothesis the data contradict is reported as
  challenged. The abstract-only, agent-coder limitations are stated in `FINDINGS.md` and `paper.md`.
