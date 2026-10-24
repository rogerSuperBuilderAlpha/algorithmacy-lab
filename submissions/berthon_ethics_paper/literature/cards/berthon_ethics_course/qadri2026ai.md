---
citekey: qadri2026ai
title: "\"AI is (not) the new..\": A Diagnostic Analogy Framework for Generative AI's Cultural Impacts"
authors: Qadri, Rida and Prabhakaran, Vinodkumar and Denton, Remi
year: 2026
type: article
doi: null
venue: "arXiv:2609.31482v1 [cs.AI], 25 Sep 2026; printed as Proceedings of the ICML 2026 workshop on Culture x AI: Evaluating AI as a Cultural Technology"
source_basis: full-text
pages_read: all (PDF pp. 1-5, including references)
source_url: https://arxiv.org/abs/2609.31482
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/N5_prior_work_gap/diagnostic2026analogy.pdf
sha256: 22cdf5b68bbfeea62bf389fd9995548c57df3624da0f2e9453072f828ea94b63
manuscript_lines: [129]
ledger_rows: [P4-N01, B26]
verified: true
written: 2026-10-14
---

Key `qadri2026ai` is from `literature/references.bib`. I read the arm's local pdftotext extraction
(`diagnostic2026analogy.txt`, sha256 `8dc33a73…`) in full this session. The bib entry's note is stale. It
says "No DOI or arXiv ID found" and calls the work a poster, but the PDF prints "arXiv:2609.31482v1 [cs.AI]
25 Sep 2026" on p. 1, and FIX_CHECK_C records the arXiv abs page (authors, date, title) as matching.

## Summary
Qadri, Prabhakaran and Denton (Google Research) argue that scholars and policymakers explain generative AI by
"gestalt analogies" to the printing press, electricity or steam power. These analogies convey magnitude but
"fail to isolate the precise technical and social properties that carry the comparison" (p. 1). Each
reading of an analogy implies a different historical lesson and governance posture, so a vague analogy yields
"governance mismatches" (p. 1). The authors propose a diagnostic framework that breaks any technological
intervention into three coordinates: the epistemic site, the governing logic and the technical mechanism
(pp. 1-2). The framework separates structural consequences, which follow from the mechanism, from contingent
ones, which stay open to design and institutional choice (p. 2). They apply it to two sites. At information
discovery, indexicality (the catalogue, the search engine) gives way to probabilistic inference, which erodes
provenance (pp. 2-3). At knowledge synthesis, editorial authority (the encyclopedia) gives way to statistical
consensus, which decouples authority from accountability (pp. 3-4). Governance of structural consequences must
act on the mechanism, not the interface (p. 4). The line between structural and contingent is itself
contestable (p. 4).

## Key facts it relies on
- Abstract, p. 1: comparisons "are typically imprecise about which property of the technology carries the comparison, and imprecise analogies produce imprecise governance by designing interventions against the wrong property of the system."
- p. 1: gestalt analogies "fail to isolate the precise technical and social properties that carry the comparison" and "can yield governance mismatches: regulatory and design interventions that apply historical solutions to entirely different technical realities."
- pp. 1-2: three coordinates, "Epistemic Site", "Governing Logic", "Technical Mechanism".
- p. 2: "Structural consequences are those produced by the mechanism itself"; contingent ones "depend on institutional conditions and human choices that remain open". The printing press's fracture of the Church is given as contingent (citing Eisenstein 1980).
- p. 3: provenance erosion is "structural", and retrofitted citation tools do not "restore indexical architecture".
- p. 4: "authority is decoupled from accountability"; "recovering something like contestability requires sustained institutional effort against a system that produces none of it on its own."
- p. 4: structural consequences "cannot be removed by interface design, transparency mandates, or post-hoc disclosure requirements that leave the mechanism intact."
- p. 4: "The line between structural and contingent, however, is itself contestable".

## Critical notes from the literature
- This is a four-page workshop paper (ICML 2026 workshop footer, p. 1) posted to arXiv. Facet N5 records no venue
  refereeing, and the bib calls the ICML listing a poster. The abstract repeats one sentence verbatim ("This paper
  offers a diagnostic framework…", p. 1), and a reference reads "INSERT_YOUTUBE_URL_HERE" (p. 5), so the text is
  an early draft.
- Facet N5 (§2; Recommendations, Must engage 1) found that the manuscript's §4.1 method sentence restates this
  paper's abstract "almost word for word", so the citation is owed. N5 also notes that the cases concern discovery
  and synthesis, not standing, literacy or third parties.
- FIX_CHECK_C: the arXiv record prints the title with three dots ("the new..."), the PDF with two ("the new..").
  Either is defensible.
- I found no published critique of the paper in the arm's record. It appeared on arXiv on 25 Sep 2026.

## Key topics covered
historical analogy, generative AI, printing press analogy, epistemic site, governing logic, technical mechanism, structural vs contingent consequences, provenance, editorial authority, statistical consensus, AI governance

## Where the manuscript uses it
- **L129**: "an analogy that does not say what carries it invites governance aimed at the wrong feature of a
  system (Qadri et al., 2026)." The manuscript takes the method of naming the property that carries an analogy,
  and the claim that vague analogy misdirects governance. Source: abstract, p. 1 ("imprecise analogies produce
  imprecise governance by designing interventions against the wrong property of the system"), and p. 1 body
  ("governance mismatches"). **holds**: a close paraphrase of the abstract, properly attributed. The manuscript
  quotes nothing from the work, so no exact-string check is needed.
- **Reference entry (v3 L425)**: lists the work as an arXiv preprint with the arXiv ID, which matches PDF p. 1.
  The entry gives no workshop venue, although p. 1 prints "Proceedings of the ICML 2026 workshop on Culture × AI".
  This is optional to add.

## Verifier notes
- 2026-10-14. sha256 of the PDF recomputed: matches; the .txt hash matches the card's `8dc33a73…`. The arXiv API record for 2609.31482 gives authors Qadri, Prabhakaran, Denton, published 25 Sep 2026, title with three dots ("the new..."); the PDF has two. PDF p. 1 footer reads "Proceedings of the ICML 2026 workshop on Culture × AI".
- Bib disagreements: `references.bib` (`qadri2026ai`) calls the work a poster, says no arXiv ID was found, and points to a Google Research page; the v3 entry (l. 425) cites the arXiv ID and gives the title as "the new .." (space, two dots), which matches neither the PDF ("new..") nor arXiv ("new..."). v3 names no workshop venue. None is an error of substance.
- Checked all eight key facts: every quotation found, on the pages given (abstract/governance mismatches p. 1; structural vs contingent and Eisenstein p. 2; indexical architecture p. 3; accountability, interface design, contestable line p. 4). The 'INSERT_YOUTUBE_URL_HERE' reference is on p. 5, and the abstract sentence 'This paper offers a diagnostic…' does occur twice.
- Use at v3 l. 129 (line unchanged): a paraphrase of the p. 1 abstract sentence, with no quotation; **holds** confirmed.
