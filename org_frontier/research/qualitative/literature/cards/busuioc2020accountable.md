---
citekey: busuioc2020accountable
title: Accountable Artificial Intelligence: Holding Algorithms to Account
authors: Busuioc, Madalina
year: 2020
doi: 10.1111/puar.13293
arxiv: null
journal: Public Administration Review
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf
sha256: e9e6d944715d14b03c383b1e1e2f4f7aa7ffaa9bd610708bd06645f03c64e7fa
pdf_path: literature/pdfs/busuioc2020accountable.pdf
verified: true
---

## Summary

WARNING — PDF/METADATA MISMATCH. The file at `literature/pdfs/busuioc2020accountable.pdf` (sha256 e9e6d944..., matching the frontmatter) does NOT contain the Busuioc (2020) paper "Accountable Artificial Intelligence: Holding Algorithms to Account" (Public Administration Review, doi 10.1111/puar.13293). Instead, the full 15-page document is "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification" by Joy Buolamwini and Timnit Gebru, published in Proceedings of Machine Learning Research 81:1–15, 2018 (Conference on Fairness, Accountability, and Transparency). The frontmatter `source_url` field independently corroborates this: it points to `proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf`, the Gender Shades paper. Because the target paper's text is not present, I cannot author a grounded summary of Busuioc (2020) from this file without fabricating; per integrity rules I have not done so. The correct Busuioc PDF must be re-acquired before this card can be completed. The facts below are drawn from the document that is actually in the file (Gender Shades), provided only so the maintainer can confirm the mismatch.

## Key facts it relies on

- The actual PDF content is "Gender Shades" (Buolamwini & Gebru), PMLR 81:1–15, 2018, FAT* conference — not Busuioc (2020).
- Gender Shades reports that the IJB-A and Adience facial-analysis benchmarks are overwhelmingly lighter-skinned (79.6% for IJB-A and 86.2% for Adience).
- It introduces the Pilot Parliaments Benchmark (PPB) of 1,270 unique individuals, balanced by gender and skin type, labeled with the six-point Fitzpatrick skin type scale.
- Evaluating 3 commercial gender classifiers, darker-skinned females are the most misclassified group, with error rates up to 34.7%, versus a maximum error rate of 0.8% for lighter-skinned males.
- PPB draws parliamentarians from 6 countries: 3 African (Rwanda, Senegal, South Africa) and 3 European (Iceland, Finland, Sweden), selected for gender parity per the Inter-Parliamentary Union ranking.
- Benchmark subject counts cited: IJB-A 500 unique subjects (NIST, 2015); Adience 2,284 unique subjects (2014), of which 2,194 were labeled for skin type and gender.
- The frontmatter `source_url` (buolamwini18a.pdf) and the embedded text agree with each other and disagree with the declared citekey/title/doi/authors/journal.

## Critical notes from the literature

- This card cannot be verified against the intended target (Busuioc 2020). The `verified` field should remain `pending` and the PDF should be flagged for re-download from the Public Administration Review record at doi 10.1111/puar.13293.
- The mismatch appears to originate upstream in acquisition: the `source_url` in the frontmatter points to the wrong paper (Gender Shades), so the wrong file was downloaded under the Busuioc filename and its sha256 was recorded as authoritative.
- Any downstream claims attributed to "Busuioc 2020" that were generated from this file would be unsupported; do not cite this card's body for the accountability/governance arguments of the intended paper until the correct PDF is in place.

## Key topics covered

- PDF/metadata integrity mismatch (wrong paper under filename)
- (Content actually present) Algorithmic auditing; intersectional accuracy disparities; commercial gender classification; facial analysis benchmarks (IJB-A, Adience, PPB); Fitzpatrick skin type scale; fairness/accountability/transparency in AI
- (Intended but absent) AI accountability, algorithmic governance, public administration — NOT present in this file
