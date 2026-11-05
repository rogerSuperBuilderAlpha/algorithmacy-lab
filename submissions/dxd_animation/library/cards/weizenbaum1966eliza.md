---
key: weizenbaum1966eliza
apa: "Weizenbaum, J. (1966). ELIZA—A computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36–45. https://doi.org/10.1145/365153.365168"
authors: "Weizenbaum, Joseph"
year: 1966
title: "ELIZA—A Computer Program For the Study of Natural Language Communication Between Man and Machine"
venue: "Communications of the ACM"
volume: "9"
issue: "1"
pages: "36–45"
doi: "10.1145/365153.365168"
url: ""
type: article
facets: [F3]
claims: [c4, c6]
role: anchor
load: load-bearing
read_depth: abstract
object_read: "Crossref abstract and OpenAlex abstract (W4236521339) of the 1966 article (not the 1983 reprint, whose DOI 10.1145/357980.357991 comes from DECISIONS.md and is unchecked), local folder ~/iit-playground/dxd_animation_local/pdfs/weizenbaum1966eliza/ (crossref.json, openalex.json); original https://doi.org/10.1145/365153.365168 (FETCH_LOG.tsv: HTTP 403 on the scripted fetch); 2026-11-05; sha256 crossref.json 216458cdcc2bd46676dad82a7724e44b11a946871ea2f0c79212d77669b83a3a, openalex.json c0ae212d0b358175926bc4fa9daace99838fe069cbc4e42f3428c409bb9706f7"
verified: corrected
verified_against: "Crossref and OpenAlex records (crossref.json, openalex.json); FETCH_LOG.tsv, DECISIONS.md, OUTLINE.md"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Abstract-only card; the article was not read. By its abstract, Weizenbaum describes ELIZA, a program running on the MAC time-sharing system at MIT that makes some kinds of natural-language conversation between person and computer possible. It analyses input sentences with decomposition rules triggered by key words, and builds responses with reassembly rules attached to the chosen decomposition rules. He names five technical problems: identifying key words, discovering minimal context, choosing transformations, responding when no key word appears, and giving ELIZA "scripts" an editing capability. The abstract ends by saying that a discussion of some psychological issues relevant to the approach, and of future developments, concludes the paper.

## What the paper uses it for

- c4 (an LLM interface is an animation): ELIZA is the early case of a conversational character produced by rules, a puppet with a script. The abstract supports only the mechanism (rules, scripts), not any animation reading; that link is the paper's own.
- c6 (the viewer locks in; the user also animates): the triage planned to look in the closing psychological discussion for Weizenbaum's own account of users reading understanding into the program, the "ELIZA effect" Stark (2024) invokes. The abstract says only that such a discussion exists. It does not show what Weizenbaum says there, so the use is unconfirmed.

## Loci

None.

## Caution

- Abstract only. The user-attribution claim the paper wants sits in the part not read.
- The "ELIZA effect" is a later label; whether this 1966 article uses the phrase, or makes the claim as the paper phrases it, is unchecked.
- Object is the 1966 article. DECISIONS.md names a 1983 reprint (10.1145/357980.357991); no record of it is in the folder, so that DOI is unchecked.
- DECISIONS.md planned full text (ACM bronze); the scripted fetch got HTTP 403 and no text layer exists. Listed for the author's browser; no bypass attempted.
- Neither SOURCE.md nor OUTLINE.md cites this work directly (it is cited only through Stark 2024), so status is candidate.

## Verification

2026-11-05 · S6 verifier, batch b10 (opus; not the writer) · verdict: corrected · checked: loci 0/0 (None); metadata vs Crossref/OpenAlex (author, 1966, title, CACM 9(1) 36-45, DOI); abstract summary checked against the Crossref abstract; depth abstract confirmed; sha256 both files recomputed, match · changed: marked the 1983 reprint DOI 10.1145/357980.357991 as taken from DECISIONS.md and unchecked (no record of it in the folder), in object_read and Caution

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (None, correct for an abstract card); the "What it argues" paraphrase follows the Crossref and OpenAlex abstracts point by point (MAC time-sharing, decomposition and reassembly rules, the five problems, the closing psychological discussion); Weizenbaum, 1966, title, CACM 9(1), 36–45, DOI match both records; sha256 of both files recomputed and match; no PDF or .txt, so abstract depth is honest; the c4 and c6 uses are correctly limited to what the abstract shows.
- Changed: nothing.
- For the author: nothing (ACM copy on BROWSER_LIST; the 1983 reprint DOI stays unchecked).
