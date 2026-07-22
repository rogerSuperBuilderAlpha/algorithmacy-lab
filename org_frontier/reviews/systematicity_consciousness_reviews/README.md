# systematicity_consciousness_reviews

**Question.** How systematic are review articles in consciousness science and integrated-information
research? A direct homage to Simsek, Fox & Heavey (2023), who coded 165 management reviews for seven
systematicity practices and related practice count to citation impact. This review runs the same
instrument on a different field.

**Design.** A screened corpus of review/survey articles (2001–2026), harvested with two academic
semantic-search connectors over eight review-oriented queries, coded three times by independent agents
for the seven practices (envisioning, explicating, executing, evaluating, encoding, elaborating,
expositing), with Fleiss' κ reported per practice.

**Hypotheses (pre-registered in `hypotheses.md`).**
- H1 — reviews report fewer than half the seven practices on average (mean < 3.5).
- H2 — practice adoption has risen over the last decade (practice count vs year, positive).
- H3 — reviews reporting more practices are more cited (practice count vs cites, Spearman positive).

**Where it stands.** See `FINDINGS.md` for verdicts, the κ table, and limitations; `paper.md` for the
write-up in the register of *Organizational Research Methods*.

**Reproduce.**
```bash
python -m org_frontier.reviews.systematicity_consciousness_reviews.build_corpus   # corpus + seeds
python -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/systematicity_consciousness_reviews/coding \
    --categorical envisioning,explicating,executing,evaluating,encoding,elaborating,expositing \
    --out org_frontier/reviews/systematicity_consciousness_reviews/results/frozen.json
python -m org_frontier.reviews.systematicity_consciousness_reviews.run              # tests + summary.json
```

**Layout.** `hypotheses.md` (pre-registered), `coding_protocol.md` (codebook), `methods.md` (boundary +
search), `literature/corpus.jsonl` (the screened corpus), `coding/coder{A,B,C}.jsonl` (independent
coders), `results/frozen.json` + `results/summary.json`, `FINDINGS.md`, `paper.md`,
`literature/references.bib`.
