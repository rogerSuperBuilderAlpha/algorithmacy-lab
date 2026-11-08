---
key: sullivan2022understanding
apa: "Sullivan, E. (2022). Understanding from machine learning models. *The British Journal for the Philosophy of Science*, *73*(1), 109–133. https://doi.org/10.1093/bjps/axz035"
authors: "Sullivan, Emily"
year: 2022
registered_year: 2019
title: "Understanding from Machine Learning Models"
venue: "The British Journal for the Philosophy of Science"
volume: "73"
issue: "1"
pages: "109–133"
doi: "10.1093/bjps/axz035"
url: ""
type: article
facets: [F7]
claims: [c7]
role: contrast
load: load-bearing
read_depth: abstract
object_read: "OpenAlex record with abstract (openalex.json; publication date 2019-08-02) and Crossref record without abstract (crossref.json; University of Chicago Press; issued 2022-03-01) at pt_ai_animation_local/pdfs/sullivan2022understanding/; no work text; philsci-archive served a bot challenge (BROWSER_LIST.md) and inbox/ holds no copy; 2026-11-08; sha256 d82234f97a0e5286982693814d1c64737168b3d9770ac22c65efdcf97b71374a (openalex.json), 34dc65e6534a1701c71daabe6c0b5b451692b16d79bcb2e9284ac8e83c6be37d (crossref.json), recomputed with shasum -a 256"
verified: verified
verified_against: "openalex.json abstract and crossref.json (sha256 match)"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Sullivan (2022), Understanding from machine learning models

## What it argues

Abstract only; I have not read the article. Emily Sullivan starts from a puzzle: simple idealized models seem
to give more understanding than opaque, complex ones, yet scientists increasingly use opaque machine learning
models. Do they trade understanding for another good, or are the assumptions behind minimal models' power to
explain misguided? Using deep neural networks as her case, she argues that it is not a model's complexity or
black-box nature that limits understanding. A lack of scientific and empirical evidence linking the model to
the target phenomenon is what primarily prohibits it.

## What the paper uses it for

- **c7** (necessary opacity): contrast. Sullivan would object if the paper lets opacity carry the whole
  weight, as in "no component holds the intelligence, so we cannot understand it". By her abstract, opacity is
  not what blocks understanding; the missing evidence that ties the model to what it models is. For
  the paper, that moves the question from "where is the intelligence" to "what supports the link between this
  system and the behaviour users meet". It may also bear on c11 (evaluation), but the card tags c7 only. The
  abstract is about scientific models of phenomena, not about products built around an LLM, so any use for
  the paper's argument stretches the source.

## Loci

None.

## Caution

- **Abstract only.** On BROWSER_LIST.md (philsci-archive 16276, bot challenge; no other copy; FETCH_LOG.tsv
  "no candidates"). The Crossref record has no abstract; the text above is OpenAlex's.
- **Record correction (DECISIONS.md).** The key and `year` take the volume year, 2022 (Crossref: issued
  2022-03-01, vol. 73, no. 1). `registered_year: 2019` marks the online date, 2019-08-02, seen in OpenAlex's
  `publication_date` and Crossref's `created`. The sketch and any cite-by-DOI list will show 2019.
- **Homonym.** Reserve `sullivan2022inductive` is a different Sullivan paper, not carded here.
- **What the paper may not claim from it:** her argument beyond the abstract, or that opacity does no harm.

## Verification
- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 5
- verdict: verified
- checked: frontmatter against crossref.json (Sullivan, Emily; title; The British Journal for the Philosophy of Science 73(1), 109-133; DOI; journal-article; University of Chicago Press; issued 2022-03-01; created 2019-08-02) and openalex.json (publication_date 2019-08-02), so `year: 2022` and `registered_year: 2019` follow the volume-year rule and DECISIONS.md; both sha256 values recomputed (match); the summary against the OpenAlex abstract, sentence by sentence (no claim beyond it); the named stretch on c7 (scientific models, not LLM products) is present; BROWSER_LIST.md and FETCH_LOG.tsv agree; reserve `sullivan2022inductive` exists in triage F5-F9.md (R4).
- changed: nothing.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: Loci = None (abstract card); the summary matches the OpenAlex abstract sentence by sentence; both record sha256 values recomputed, match; crossref.json 73(1), 109–133, issued 2022-03-01, created 2019-08-02, so year 2022 and registered_year 2019 hold; the c7 stretch (scientific models, not LLM products) is named.
- Changed: nothing
- For the author: abstract only; status `cited` though SKETCH does not name Sullivan (see part4 header)
