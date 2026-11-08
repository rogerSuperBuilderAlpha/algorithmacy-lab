---
key: froese2009enactive
apa: "Froese, T., & Ziemke, T. (2009). Enactive artificial intelligence: Investigating the systemic organization of life and mind. *Artificial Intelligence*, 173(3–4), 466–500. https://doi.org/10.1016/j.artint.2008.12.001"
authors: "Froese, Tom; Ziemke, Tom"
year: 2009
title: "Enactive artificial intelligence: Investigating the systemic organization of life and mind"
venue: "Artificial Intelligence"
volume: "173"
issue: "3–4"
pages: "466–500"
doi: "10.1016/j.artint.2008.12.001"
url: ""
type: article
facets: [F2]
claims: [c4, c12]
role: anchor
load: load-bearing
read_depth: metadata
object_read: "Crossref work record (no abstract) and OpenAlex record W1989974095 (no abstract) for 10.1016/j.artint.2008.12.001, at ~/iit-playground/pt_ai_animation_local/pdfs/froese2009enactive/crossref.json and openalex.json; read 2026-11-08; sha256 a85c0a88b72568f9e1130f6b0479bf191278ea500337d19134df0c64289d7623 (crossref.json) and b4ea13403dfbe9ea053099807c0ba75cb3ffe3d8478adf1475fe327e4073c3a7 (openalex.json), computed with shasum -a 256; no sha256.txt"
verified: verified
verified_against: "crossref.json and openalex.json (fields, dates, OA status); sha256 recomputed; BROWSER_LIST and FETCH_LOG rows; DECISIONS registered_year list"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# Froese & Ziemke (2009), Enactive artificial intelligence

## What it argues

This is a metadata card; I read no text of the article. The Crossref and OpenAlex records show an article by
Tom Froese and Tom Ziemke, "Enactive artificial intelligence: Investigating the systemic organization of life
and mind", in *Artificial Intelligence* 173(3–4), pp. 466–500, issued March 2009. Neither record carries an
abstract. The title shows that the authors bring the enactive approach to AI and that they investigate the
"systemic organization" of life and mind together. Their argument is unread.

## What the paper uses it for

- **c4** (an organizational account of life fits the system around the LLM): the title shows an
  organizational account of life already carried into AI, in AI's own flagship journal, in 2009. That makes
  the article the nearest neighbour inside F2. What it says about which systems qualify, and whether an
  engineered system can have the organization it names, is unread; the card cannot say whether Froese and
  Ziemke would accept or reject c4's application to a harness around an LLM.
- **c12** (gap: AI development as a craft of animation): the article threatens novelty more than it
  supports it. If enactive AI already reads AI through the organization of life, c12 must say what the
  animation frame adds. Checkpoint A decision 5c, as the triage file reports it, answers "the making": the
  paper is about the craft that builds the system, not about whether the system is organized like life.
  That distinction must be checked against the text before `GAP_CHECK.md` relies on it.

## Loci

None

## Caution

- **Not read.** The article is row 5 of "Open these first" on `BROWSER_LIST.md` ("enactive AI: c4 must say
  what animation adds"); the full-list row reads "blocked: ScienceDirect PDF returned 403 to the tool;
  linkinghub gives a redirect page; not bypassed". OpenAlex marks it bronze open access, so a browser should
  reach the publisher PDF.
- **Year.** Crossref gives only the issue date, March 2009, and no online date. OpenAlex gives 2008-12-26 as
  the publication date and 2008 as the year. DECISIONS lists no `registered_year` for this key, so the card
  sets none and records the OpenAlex date here, as DECISIONS does for `bedau2010living`. S8 should decide
  whether the 2008 online date needs a `registered_year`.
- **Same first name.** Both authors are "Tom" in Crossref; cite with surnames only.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 3
- verdict: verified
- checked: Crossref: authors Tom Froese and Tom Ziemke, title, Artificial Intelligence 173(3-4), 466–500, DOI, journal-article, only issue date 2009-03, no abstract; OpenAlex 2008-12-26, bronze OA, no abstract; both sha256 values match; BROWSER_LIST row 5 and full-list row; FETCH_LOG 403 and redirect; DECISIONS lists no registered_year for this key, so leaving the 2008 date to S8 in Caution is consistent with the bedau2010living handling.
- changed: nothing
