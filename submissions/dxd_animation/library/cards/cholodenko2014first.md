---
key: cholodenko2014first
apa: "Cholodenko, A. (2014). \"First principles\" of animation. In *Animating film theory* (pp. 98–110). Duke University Press. https://doi.org/10.1215/9780822376811-007"
authors: "Cholodenko, Alan"
year: 2014
title: "“First Principles” of Animation"
venue: "Animating Film Theory (Duke University Press)"
volume: ""
issue: ""
pages: "98–110"
doi: "10.1215/9780822376811-007"
url: "https://read.dukeupress.edu/books/book/chapter-pdf/592072/9780822376811-007.pdf"
type: chapter
facets: [F1]
claims: [c5, c7]
role: support
load: exists
read_depth: abstract
object_read: "Registry records only, no PDF: OpenAlex W3082465199 (its 'abstract' is the chapter's opening text, ending in a running head), at ~/iit-playground/dxd_animation_local/pdfs/cholodenko2014first/openalex.json (sha256 182fea5deccff2bc8dc99c632ee6d220670616a89b9aa12bd7aca4ccead60712), and the Crossref record for 10.1215/9780822376811-007 (no abstract), crossref.json (sha256 bcdf3e52367997abe8c0103e6e33ab085f0dc177f1eeb2a3913c85d4601283ec); the scripted fetch of https://doi.org/10.1215/9780822376811-007 returned HTTP 403 (FETCH_LOG.tsv, status closed); read 2026-11-05"
verified: corrected
verified_against: "Crossref crossref.json (sha256 bcdf3e52 recomputed) and OpenAlex openalex.json (sha256 182fea5d recomputed; abstract rebuilt from inverted index): author, title, pages 98-110, publisher, year, DOI, pdf URL, counts; FETCH_LOG 403; CHECK F11"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

# Cholodenko (2014), "First principles" of animation

## What it argues

This card rests on registry text only. OpenAlex holds no true abstract: its abstract field carries the
chapter's opening page, cut off mid-argument. I read no other part of the chapter.

In that opening, Cholodenko says his publications of "the last twenty-three years are dedicated to animating
film theory". He means two things: "addressing what animation adds to the theorizing of film" and "doing
that adding", while redressing "the marginalization of animation by film studies, film history, and film
theory", for "animation has been their blind spot". His project applies "especially to the theorization of
live action film through animation" and answers late-1960s French Marxist film theory and the Anglo-American
theory derived from it. He names the anthologies he edited, *The Illusion of Life: Essays on Animation*
(1991) and *The Illusion of Life 2* (2007), and offers the chapter as "my key results to date, my 'first
principles' of animation" (single quotes mine; the record has double). The first principle reverses the
usual order: "not only is animation a form of film but all film, film 'as such,' is a form of animation"
(single quotes mine). From this he infers that "live action is a form of animation". He says he made the
claim "ten years before Lev Manovich's similar assertion". The excerpt stops there.

## What the paper uses it for

- **c5** (animation is opaque; the interstices are the craft): DECISIONS wants an open text of animation
  theory for §4.1. The excerpt says nothing about frames or interstices, so it does not yet support c5.
- **c7** (animation is triadic): the excerpt names no viewer, character or animator, so it does not yet
  support c7.
- **c4** (not tagged, but nearest): the first principle, that all film is animation, could support the
  paper's widening of "animation" to the LLM interface. That is the paper's extension, not Cholodenko's
  claim. Neither SOURCE.md nor OUTLINE.md cites the chapter yet.

## Loci

None

## Caution

- Read depth: DECISIONS approved this as "full_text, open (bronze)", but the fetch returned HTTP 403 and no
  PDF or text layer is held. The card stays abstract-depth until a copy arrives. The De Gruyter reissue
  (10.1515/9781478091950-008, per the triage file) is the fallback route; I did not see its record.
- Editor: the triage APA names K. Beckman as the volume's editor. Neither local record names an editor, so
  the APA entry here omits one until the title page is seen.
- The OpenAlex text is a scrape of the chapter's first page, not an author-written abstract. It ends in the
  running head "6 : : 'First Principles' of Animation" (single quotes mine), which suggests a chapter number
  of 6. Any quotation from it needs a page check against the chapter before it enters the paper.
- Counts: Crossref 21 citing works; OpenAlex 35.
- Homonym: CHECK F11 recommends Thomas and Johnston (1981), *The Illusion of Life*, and notes the phrase
  appears in Silvio (2010, p. 428). Cholodenko's 1991 anthology *The Illusion of Life* shares the phrase but is
  a different work from Thomas and Johnston's book and from this chapter.

## Verification

2026-11-05 · S6 verifier, batch b08 (opus; not the writer) · verdict: corrected · checked: loci 0/0; every quotation in What it argues found verbatim in the OpenAlex text; metadata vs crossref/openalex; depth abstract honest · changed: Caution: the Illusion of Life bullet misdescribed CHECK F11 (F11 recommends Thomas and Johnston 1981 and cites Silvio 2010 p. 428; it does not concern Cholodenko); rewritten as a homonym note

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (None, correct); every quotation in "What it argues" is in the OpenAlex text rebuilt from the inverted index, which does end in the running head "6 : : 'First Principles' of Animation"; frontmatter vs crossref.json and openalex.json (Cholodenko, 2014, Animating Film Theory, Duke, 98–110, DOI, chapter-pdf URL; no editor in either record; counts 21 and 35); sha256 of both files matches; claim uses: c5 and c7 are stated as not yet supported, which is honest for the excerpt.
- Changed: nothing.
- For the author: DECISIONS approved this as full text (bronze) but the fetch got 403 (BROWSER_LIST row 40); the editor (K. Beckman, per triage) stays out of the APA string until the title page is seen.
