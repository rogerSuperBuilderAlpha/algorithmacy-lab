---
key: bedau2010living
apa: "Bedau, M. A., McCaskill, J. S., Packard, N. H., & Rasmussen, S. (2010). Living technology: Exploiting life's principles in technology. *Artificial Life*, *16*(1), 89–97. https://doi.org/10.1162/artl.2009.16.1.16103"
authors: "Bedau, Mark A.; McCaskill, John S.; Packard, Norman H.; Rasmussen, Steen"
year: 2010
title: "Living Technology: Exploiting Life's Principles in Technology"
venue: "Artificial Life"
volume: "16"
issue: "1"
pages: "89–97"
doi: "10.1162/artl.2009.16.1.16103"
url: ""
type: article
facets: [F1]
claims: [c4, c12]
role: support
load: load-bearing
read_depth: abstract
object_read: "Crossref record with abstract (crossref.json; MIT Press; issued 2010-01) at pt_ai_animation_local/pdfs/bedau2010living/; no work text; the zenodo copy was blocked (BROWSER_LIST.md) and inbox/ holds no copy; 2026-11-08; sha256 140a77740ded06249b35c4e9327b07046cbe335f0b9420113b699aedb04c70b2 (crossref.json, recomputed with shasum -a 256)"
verified: corrected
verified_against: "crossref.json with abstract (sha256 match); live OpenAlex API record W2130707354 for the date only"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Bedau, McCaskill, Packard & Rasmussen (2010), Living technology

## What it argues

Abstract only; I have not read the article. According to the Crossref abstract, the four authors explain "living
technology", technology based on core features of life, and illustrate it with artificial life software,
reconfigurable and evolvable hardware, self-reproducing robots, chemical protocells and hybrid
electronic-chemical systems. They split it into primary living technology (key material components and core
systems not derived from living organisms) and secondary (derived from them). They say primary living
technology is emerging and potentially powerful, link it to artificial life, synthetic biology and the
convergence of nano-, bio-, information and cognitive technologies, and end on social and ethical questions.

## What the paper uses it for

- **c4** (an organizational account of life fits the system around the LLM): possible support. The abstract
  treats life's principles as something engineers can build on, which is the sense of "life" §2 needs
  (making, not lineage). The abstract does not mention organization, autopoiesis or software systems, and it
  is not about LLMs. The use stretches the source until the text is read.
- **c12** (gap): possible support for placing the paper beside "living technology" as prior framing of
  technology through life. The abstract speaks of hardware, protocells and robots, not of AI development as
  craft, so the paper can say the idea exists in artificial life and the claim here differs. Unverified
  against the text.

## Loci

None.

## Caution

- **Abstract only.** The work is on BROWSER_LIST.md (zenodo landing page returned a 403 block; no other copy).
  FETCH_LOG.tsv records records-only.
- **Year.** The Crossref record puts print in January 2010 (volume 16, issue 1) and creation on 2009-10-26.
  DECISIONS.md reports OpenAlex as 2009; no openalex.json sits in this folder, so I did not check that. The key
  and the card take the volume year, 2010, and set no `registered_year`.
  [S6 verifier, 2026-11-08] The live OpenAlex record W2130707354 (read, not saved) gives publication_year 2009 and
  publication_date 2009-10-26, the same day as Crossref's `created`. DECISIONS.md asks only for this note, not a
  `registered_year`.
- **What the paper may not claim from it:** any argument about organization, any link to LLMs, or any
  quotation. The abstract is not a locus.

## Verification
- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 5
- verdict: corrected
- checked: frontmatter against crossref.json (four authors in order; title; Artificial Life 16(1), 89-97; DOI; journal-article; print 2010-01; created 2009-10-26); sha256 of crossref.json recomputed (match); the summary against the Crossref abstract, sentence by sentence (no claim beyond it); BROWSER_LIST.md row (zenodo 403) and FETCH_LOG.tsv (records-only); no copy in inbox/; the OpenAlex 2009 date against the live API.
- changed: Caution gains one marked note confirming OpenAlex's 2009-10-26 date. No `registered_year` added, per DECISIONS.md. The c4 and c12 uses remain tentative and say so.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 0/0 (abstract card, Loci None); the summary checked sentence by sentence against the Crossref JATS abstract; frontmatter vs crossref.json (four authors in order, Artificial Life 16(1), 89–97, print 2010-01, created 2009-10-26); sha256 recomputed, matches.
- Changed: nothing
- For the author: both uses (c4, c12) stay tentative until the article is read; status 'cited' though SOURCE.md and SKETCH.md do not name Bedau et al. (status note in part1.md).
