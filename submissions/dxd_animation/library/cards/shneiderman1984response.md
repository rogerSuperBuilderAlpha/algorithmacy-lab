---
key: shneiderman1984response
apa: "Shneiderman, B. (1984). Response time and display rate in human performance with computers. *ACM Computing Surveys*, 16(3), 265–285. https://doi.org/10.1145/2514.2517"
authors: "Shneiderman, Ben"
year: 1984
title: "Response time and display rate in human performance with computers"
venue: "ACM Computing Surveys"
volume: "16"
issue: "3"
pages: "265–285"
doi: "10.1145/2514.2517"
url: ""
type: article
facets: [F4]
claims: [c5]
role: anchor
load: load-bearing
read_depth: abstract
object_read: "OpenAlex abstract (W2104839312; OCR-garbled in places) and Crossref record, local folder ~/iit-playground/dxd_animation_local/pdfs/shneiderman1984response/ (crossref.json, openalex.json); original https://doi.org/10.1145/2514.2517 (FETCH_LOG.tsv: HTTP 403 on the scripted fetch); 2026-11-05; sha256 crossref.json c58a9d86e586e311b4b7037db95eb07e126f745e27017c6f64dde4cae17cff8d, openalex.json 7c7d213bb3925d3a430c22b081777cbc3419fd51963c2b606d17c90a84d0e06f"
verified: corrected
verified_against: "Crossref and OpenAlex records (crossref.json, openalex.json); FETCH_LOG.tsv, DECISIONS.md"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Abstract-only card; the article was not read. Per the OpenAlex abstract, Shneiderman says the pace of human-computer interaction matters to computer scientists and users alike, and that experiments have begun to shed light on a complex and controversial subject. He reviews theory and experimental results on display rates, response-time expectations and attitudes, user productivity and variability. Breaking the concerns and tasks apart clarifies the issues, but substantial work remains before a predictive model can emerge. In general, frequent users prefer response times under a second for most tasks, and productivity rises as response time falls. However, error rates rise when response time is too short or too long. Users pick up the pace of the system, but the profile of commands may change with its speed.

## What the paper uses it for

- c5 (animation is opaque: missing frames; the interstices are the craft): it is the human-factors baseline for timing: pace is a design variable with measurable effects on error and productivity, so the interval between request and reply is not neutral. The paper's step from "display rate" to token pacing in an LLM stream is its own; the abstract does not define display rate, and it does not mention streaming text.

## Loci

None.

## Caution

- Abstract only. The OpenAlex text is OCR-damaged ("controversml", "productwlty", "revmws"); this card paraphrases it and quotes nothing.
- DECISIONS.md planned full text (ACM bronze); the scripted fetch got 403 and no text layer exists locally.
- The abstract's findings concern frequent users of 1984-era systems and the profile of their commands; transfer to chatbot users is the paper's claim, not the abstract's.
- Neither SOURCE.md nor OUTLINE.md cites this work, so status is candidate.

## Verification

2026-11-05 · S6 verifier, batch b10 (opus; not the writer) · verdict: corrected · checked: loci 0/0 (None); metadata vs Crossref/OpenAlex (author, 1984, title, ACM Computing Surveys 16(3) 265-285, DOI); abstract summary checked against the OpenAlex abstract (Crossref has none); depth abstract confirmed; sha256 both files recomputed, match · changed: c5 bullet: removed the claim that the abstract uses 'display rate' in a 1984 sense of showing output (the abstract does not define it); Caution: replaced 'command-driven systems' with what the abstract says (frequent users, profile of commands)
