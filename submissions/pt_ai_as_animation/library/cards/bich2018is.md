---
key: bich2018is
apa: "Bich, L., & Green, S. (2018). Is defining life pointless? Operational definitions at the frontiers of biology. *Synthese*, 195(9), 3919–3946. https://doi.org/10.1007/s11229-017-1397-9"
authors: "Bich, Leonardo; Green, Sara"
year: 2018
registered_year: 2017
title: "Is defining life pointless? Operational definitions at the frontiers of biology"
venue: "Synthese"
volume: "195"
issue: "9"
pages: "3919–3946"
doi: "10.1007/s11229-017-1397-9"
url: ""
type: article
facets: [F1]
claims: [c3, c4]
role: contrast
load: load-bearing
read_depth: metadata
object_read: "Crossref work record (no abstract) and OpenAlex record W2602557110 (no abstract) for 10.1007/s11229-017-1397-9, at ~/iit-playground/pt_ai_animation_local/pdfs/bich2018is/crossref.json and openalex.json; read 2026-11-08; sha256 202c3888ddfb1d3d61590de8959740c2c33f908d58e691776faf9378cac3b646 (crossref.json) and eee100a7501fd05ba3ce890f97086c467e0a31fed58e4f39c878171902a95086 (openalex.json), computed with shasum -a 256; no sha256.txt"
verified: corrected
verified_against: "crossref.json and openalex.json (fields, dates, locations, no abstract); sha256 recomputed; BROWSER_LIST and FETCH_LOG rows; triage F1-F4 note"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# Bich & Green (2018), Is defining life pointless?

## What it argues

This is a metadata card; I read no text of the article. The Crossref and OpenAlex records show an article by
Leonardo Bich and Sara Green, "Is defining life pointless? Operational definitions at the frontiers of
biology", in *Synthese* 195(9), pp. 3919–3946, published online 2017-04-18 and in print in September 2018.
Neither record carries an abstract. The title asks whether defining life is pointless (the triage files, not the records, pair it
with Machery) and points to an answer in "operational definitions" used "at the frontiers of biology". What those definitions are, and
whether the authors answer no, is unread.

## What the paper uses it for

- **c3** (no consensus definition; defend a theory): the triage files pair this article with
  `machery2012why` as its counter. The role `contrast` is relative to Machery, not to the paper's thesis.
  On the title alone, Bich and Green could object to c3 only in one place: c3 asks for a general,
  defended theory of life, while their subtitle points to operational definitions that work locally, at
  particular frontiers of research. If that is their view, they would say the paper needs a working
  definition fitted to its own frontier (engineered systems around an LLM), not a universal theory. This is
  inference from the title and must be checked against the text.
- **c4** (an organizational account of life fits the system around the LLM): the triage note says Bich also
  writes the organizational account F2 rests on, so this card could link §2's two halves. Nothing in the
  records shows that this article discusses organization; the c4 use is unsupported until the text is read.

## Loci

None

## Caution

- **Not read.** The work is on `BROWSER_LIST.md` (full-list row: "blocked: the KU PDF link returned 403
  Forbidden"). FETCH_LOG.tsv also records a 404 from a second repository handle (hdl.handle.net/10810/74972).
  OpenAlex marks the Copenhagen deposit (researchprofiles.ku.dk, 3a84eb91-2e8e-4b1f-a3f6-f7d30320ac2a) as
  green open access and "publishedVersion"; a browser may reach it where the tool could not. No paywall or
  block was bypassed.
- **Other open routes (added by the S6 verifier).** OpenAlex W2602557110 also lists two philsci-archive
  PDFs typed "acceptedVersion" (eprints 12895 and 12988, each with a direct pdf_url) and a PhilPapers PDF
  (BICIDL, "submittedVersion"). FETCH_LOG.tsv records no attempt on them, and BROWSER_LIST says only "the
  OA candidates returned 403/404". S4 or Roger should try the philsci-archive accepted version before
  promoting `knuuttila2017what`.
- **Registered year (DECISIONS record correction).** Crossref and OpenAlex give 2017-04-18 (online); volume
  195 is 2018. The key and `year` take the volume year; `registered_year: 2017` records the online year.
- **Key.** "Is" is the first title word and not an article, so the key rule gives `bich2018is` (triage
  F1-F4 key note).
- If this article cannot be read, DECISIONS names `knuuttila2017what` (open) as the reserve to promote.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 3
- verdict: corrected (one overreach in What it argues; one omission in Caution)
- checked: Crossref and OpenAlex records: authors, title, Synthese 195(9), 3919–3946, DOI, journal-article, online 2017-04-18, print 2018-09, no abstract on either; registered_year 2017 matches DECISIONS; both sha256 values match; BROWSER_LIST and FETCH_LOG rows; triage F1-F4 row 5 note on Bich and F2; key note.
- changed: What it argues said the title "poses Machery's question"; the records do not link the two, so the sentence now says the triage files make the pairing. Caution gains a bullet: OpenAlex lists philsci-archive accepted-version PDFs (12895, 12988) and a PhilPapers PDF that FETCH_LOG shows were never tried. Nothing fetched.
