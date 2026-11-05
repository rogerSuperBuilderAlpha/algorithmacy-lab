---
key: magliano2011impact
apa: "Magliano, J. P., & Zacks, J. M. (2011). The impact of continuity editing in narrative film on event segmentation. *Cognitive Science*, 35(8), 1489–1517. https://doi.org/10.1111/j.1551-6709.2011.01202.x"
authors: "Magliano, Joseph P.; Zacks, Jeffrey M."
year: 2011
title: "The Impact of Continuity Editing in Narrative Film on Event Segmentation"
venue: "Cognitive Science"
volume: "35"
issue: "8"
pages: "1489–1517"
doi: "10.1111/j.1551-6709.2011.01202.x"
url: ""
type: article
facets: [F2]
claims: [c6]
role: support
load: exists
read_depth: abstract
object_read: "OpenAlex abstract (W1824005963) and Crossref record, local folder ~/iit-playground/dxd_animation_local/pdfs/magliano2011impact/ (crossref.json, openalex.json); original https://doi.org/10.1111/j.1551-6709.2011.01202.x (PMC copy https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/, which OpenAlex lists as the accepted version: the scripted fetch got HTTP 403 and a 259,657-byte non-PDF page, and no text layer was kept, FETCH_LOG.tsv rows 38 and 75); 2026-11-05; sha256 crossref.json 5f50aa46ac154674982f46f6c1f320a278b32f1eef7620d51dccdf44d8e858da, openalex.json 32efffeb0a5be7e0ce145b005051e1d72c688953a937705488aaa80610cfc6c0"
verified: corrected
verified_against: "Crossref and OpenAlex records (crossref.json, openalex.json); FETCH_LOG.tsv, DECISIONS.md"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Abstract-only card; the full text was not read. Per the OpenAlex abstract, Magliano and Zacks ask how continuity editing shapes the way viewers perceive events in a narrative film, and which brain networks process different kinds of editing boundary. Participants watched a commercially produced film, marked where they saw meaningful events begin and end, and were scanned with fMRI. The authors sort edits into three degrees of continuity: continuous in space, time and action; discontinuous in space or time but continuous in action; discontinuous in action as well. Discontinuities in action had the biggest effect on the viewers' event segmentation, and discontinuities in space and time had minor effects. Edits produced large transient increases in early visual areas, and spatial-temporal changes and action changes produced different patterns. The authors conclude that commercial film editing is shaped to support comprehension of meaningful events across breaks in low-level visual continuity.

## What the paper uses it for

- c6 (the viewer locks in; the user also animates): it gives an experimental case in which viewers bridge breaks in space and time to keep an event coherent, which fits §4.2's point that viewers supply continuity. That is the paper's reading, not the authors' claim; the abstract speaks of how editing supports event comprehension and says nothing about viewers being "locked in" or about animation or interfaces. The step to LLM interfaces is the paper's own.

## Loci

None.

## Caution

- Abstract only. Nothing about method detail, sample size or limitations is known from this read.
- DECISIONS.md planned full text from PMC 3208769; the scripted fetch got HTTP 403 and a 259,657-byte non-PDF page (FETCH_LOG.tsv), and no text layer exists locally. OpenAlex lists the PMC copy as the accepted version, not the published one. The planned depth was not reached.
- The record's film is a commercial narrative film, not animation; whether the findings carry to animation is untested here.
- Neither SOURCE.md nor OUTLINE.md cites this work, so status is candidate. It replaces Cutting (2005) in the F2 slot (DECISIONS F2 swap).

## Verification

2026-11-05 · S6 verifier, batch b10 (opus; not the writer) · verdict: corrected · checked: loci 0/0 (None); metadata vs Crossref/OpenAlex (authors, year 2011, title, Cognitive Science 35(8) 1489-1517, DOI); abstract summary checked line by line against the OpenAlex abstract; depth abstract confirmed; sha256 both files recomputed, match · changed: object_read and Caution: the PMC fetch got 403 and a 259,657-byte non-PDF page (FETCH_LOG rows 38, 75), not only a 403; added that OpenAlex lists the PMC copy as the accepted version

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (None, correct); authors, 2011 (online 2011-10-04, print 2011-11), title, Cognitive Science 35(8) 1489–1517, DOI and both sha256 values against crossref.json and openalex.json; abstract summary against the full OpenAlex abstract (its last clause, 'and even breaks in continuity of spatial and temporal location', is not summarised but nothing in the card contradicts it); FETCH_LOG rows confirm the 403 and the 259,657-byte page; DECISIONS line 53 confirms the Cutting 2005 swap; the c6 use is marked as the paper's reading.
- Changed: nothing.
- For the author: the PMC accepted version (PMC3208769) is on the browser list (row 45); the card should be upgraded from it before §4.2 cites a finding.
