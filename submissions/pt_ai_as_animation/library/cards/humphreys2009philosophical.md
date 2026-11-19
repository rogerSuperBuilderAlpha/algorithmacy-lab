---
key: humphreys2009philosophical
apa: "Humphreys, P. (2009). The philosophical novelty of computer simulation methods. *Synthese*, 169(3), 615–626. https://doi.org/10.1007/s11229-008-9435-2"
authors: "Humphreys, Paul"
year: 2009
registered_year: 2008
title: "The philosophical novelty of computer simulation methods"
venue: "Synthese"
volume: "169"
issue: "3"
pages: "615–626"
doi: "10.1007/s11229-008-9435-2"
url: ""
type: article
facets: [F7]
claims: [c7]
role: anchor
load: load-bearing
read_depth: metadata
object_read: "Crossref work record (no abstract) and OpenAlex record W2055250996 (no abstract) for 10.1007/s11229-008-9435-2, at ~/iit-playground/pt_ai_animation_local/pdfs/humphreys2009philosophical/crossref.json and openalex.json; read 2026-11-08; sha256 109e61add14b073dbac1144f13c9c5684dac4fb0564f58d44488bd8b38d8e792 (crossref.json) and 936cf44cf95e7ca35678c65426ac59b413718f48c9a71296733ed91b066cc4d7 (openalex.json), computed with shasum -a 256; no sha256.txt"
verified: corrected
verified_against: "crossref.json and openalex.json (fields, dates, OA status); sha256 recomputed; BROWSER_LIST and FETCH_LOG rows; registry.tsv homonyms; triage F5-F9"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Humphreys (2009), The philosophical novelty of computer simulation methods

## What it argues

This is a metadata card; I read no text of the article. The Crossref and OpenAlex records show a
single-author article by Paul Humphreys, "The philosophical novelty of computer simulation methods", in
*Synthese* 169(3), pp. 615–626, published online 2008-11-28 (Crossref) and in print in August 2009. Neither
record carries an abstract. The title shows that Humphreys argues computer simulation methods raise
philosophically new questions. Which questions, and whether opacity is among them, the records do not say.

## What the paper uses it for

- **c7** (necessary opacity: no frame holds the motion, no component the intelligence): SKETCH §4.2 cites
  "Humphreys (2009) on essential epistemic opacity" (marked unverified) as the match for Roger's "in
  principle black box". The triage file calls the article "the source of essential epistemic opacity" and
  cites Beisbart's abstract calling it "the pioneering definition of opacity". Neither the term "epistemic
  opacity" nor any definition appears in the records this card read, so the attribution rests on the triage
  file and on Beisbart, not on Humphreys's text. The use also stretches in one direction already visible:
  the title concerns simulation methods, and c7 is about trained models and the system around them. The
  paper will need to show that Humphreys's opacity carries over from simulation to ML before leaning on it.

## Loci

None

## Caution

- **Not read.** The article is on `BROWSER_LIST.md` (full-list row: "no PDF: CiteSeerX copy 404; no open copy
  found by the tool"). OpenAlex marks it closed. FETCH_LOG.tsv records the CiteSeerX 404. A browser copy goes
  to `pt_ai_animation_local/inbox/humphreys2009philosophical.pdf`.
- **Registered year (DECISIONS record correction).** Crossref gives online 2008-11-28 and print 2009-08;
  OpenAlex gives 2008-11-27. Volume 169 is 2009. The key and `year` take the volume year;
  `registered_year: 2008` records the online year. The one-day difference between Crossref and OpenAlex does
  not change the year.
- **Homonyms.** The registry holds other Humphreys keys (`humphreys2010`, `humphreys2005`) by different
  authors on unrelated topics. `humphreys2004extending` (reserve, F7) is a book by "Humphreys, P." that the
  triage file treats as the same author's; no record for it was seen this run. DECISIONS kept it in reserve.
- **SKETCH wording.** SKETCH's "Humphreys (2009)" matches the record's volume year. The phrase "essential
  epistemic opacity" stays unchecked until the text is read; SKETCH is left unchanged.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 3
- verdict: corrected (one unsourced author identification in Caution)
- checked: Crossref: Paul Humphreys, title, Synthese 169(3), 615–626, DOI, journal-article, online 2008-11-28, print 2009-08, no abstract; OpenAlex 2008-11-27, closed, author display "Paul W. Humphreys", no abstract; registered_year 2008 matches DECISIONS; both sha256 values match; BROWSER_LIST and FETCH_LOG CiteSeerX 404; registry.tsv rows humphreys2010 (Ashlee) and humphreys2005 (M.); triage F5-F9 rows 1 and R1; SKETCH §4.2 wording; c7 stretch named.
- changed: Caution called humphreys2004extending "the same Paul Humphreys's book"; the only source seen this run is the triage row "Humphreys, P. (2004)", so the bullet now says the triage file treats it as the same author's and that no record for it was seen.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: Loci = None (metadata card, as the folder holds only crossref.json and openalex.json); frontmatter against both records (Paul Humphreys; *Synthese* 169(3), 615–626; DOI; online 2008-11-28, print 2009-08; no abstract in either); both sha256 values recomputed, match; status cited: SKETCH §4.2 names Humphreys (2009). The c7 bullet names its own two stretches (attribution of 'essential epistemic opacity' rests on triage and Beisbart, not on the text; simulation vs trained models).
- Changed: nothing.
- For the author: the article is still unread; a browser copy into inbox/ would let the 'essential epistemic opacity' phrase be checked before §4.2 leans on it.
