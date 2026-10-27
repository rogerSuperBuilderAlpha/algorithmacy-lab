---
citekey: amershi2019guidelines
title: "Guidelines for Human-AI Interaction"
authors: "Amershi, Saleema and Weld, Dan and Vorvoreanu, Mihaela and Fourney, Adam and Nushi, Besmira and Collisson, Penny and Suh, Jina and Iqbal, Shamsi and Bennett, Paul N. and Inkpen, Kori and Teevan, Jaime and Kikin-Gil, Ruth and Horvitz, Eric"
year: 2019
type: article
doi: 10.1145/3290605.3300233
venue: Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI 2019), Glasgow, pp. 1-13
source_basis: partial-text
pages_read: "abstract (p. 1); Table 1 (p. 3)"
source_url: https://www.microsoft.com/en-us/research/uploads/prod/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/V1/ms/amershi2019.pdf
sha256: 82fff584c6b986f573608361478e93447538c6ce707e4b9b04d45d584272ea03
manuscript_lines: []
ledger_rows: []
verified: true
written: 2026-10-14
---

**Key made for this facet.** DOI and metadata checked against Crossref (title, proceedings, pp. 1–13, 13 authors). Camera-ready PDF from Microsoft Research.

## Summary
Microsoft researchers, with one University of Washington co-author, propose 18 design guidelines for human-AI interaction, "validated through multiple rounds of evaluation including a user study with 49 design practitioners who tested the guidelines against 20 popular AI-infused products" (abstract, p. 1). Table 1 (p. 3) groups the guidelines by when they apply: initially (G1–G2), during interaction (G3–G6), when wrong (G7–G11), over time (G12–G18). Some are disclosures to the user: make clear what the system can do (G1) and how well (G2), make clear why it did what it did (G11), notify users about changes (G18). Others hand the user controls: efficient invocation, dismissal and correction (G7–G9), granular feedback (G15), conveying the consequences of user actions (G16), and global controls over what the system "monitors and how it behaves" (G17). G13, "Learn from user behavior", is the system learning from the user. None of the 18 is about developing the user's own competence. Microsoft's Responsible AI Standard v2 tells teams to follow these guidelines (T1.2.1, A5.3.1). I read only the abstract and Table 1; the study's method and results are unread here.

## Key facts it relies on
- Abstract (p. 1): "We propose 18 generally applicable design guidelines for human-AI interaction"; 49 design practitioners; 20 products.
- G1, G2 (p. 3): "Make clear what the system can do"; "Make clear how well the system can do what it can do."
- G9 (p. 3): "Support efficient correction. Make it easy to edit, refine, or recover when the AI system is wrong."
- G11 (p. 3): "Make clear why the system did what it did."
- G13 (p. 3): "Learn from user behavior. Personalize the user's experience by learning from their actions over time."
- G15–G17 (p. 3): "Encourage granular feedback"; "Convey the consequences of user actions"; "Provide global controls. Allow the user to globally customize what the AI system monitors and how it behaves."

## Critical notes from the literature
- Not read here beyond Table 1; any critique in the literature is unread this round.
- Facet V1: these controls belong to the user of a product; Nadella's post (P17) gives controls to "Orgs" and uses none of them.

## Key topics covered
human-AI interaction design, disclosure of capability, explanation, correction, feedback, user control, personalisation

## Where the manuscript uses it
- v4 (not yet drafted): proposed use — Microsoft's own design canon gives users controls (correction, dismissal, feedback, global controls; G8, G9, G15–G17, p. 3), not only disclosures; the insider post uses none. Narrows the "disclosure only" charge to the post. Holds on Table 1.
- v4 (not yet drafted): proposed use — no guideline concerns the user's growth; "Learn from user behavior" (G13) is the system's learning. Holds on Table 1.

## Verifier notes
- 2026-10-14. sha256 matches. Crossref 10.1145/3290605.3300233 confirms the title, the CHI 2019 proceedings, pp. 1-13 and all 13 authors in order. Weld is the one University of Washington affiliation (p. 1).
- Exact-checked the abstract (p. 1) and the G1, G2, G9, G11, G13 and G15-G17 wording in Table 1 (p. 3). All match. Some table cells interleave in extraction, and fi-ligatures drop ("efcient"); I read those cells by eye.
- Both uses hold on Table 1. The "no guideline concerns the user's growth" verdict is the card's reading. G1's description ("Help the user understand what the AI system is capable of") is about understanding the system, not building competence.
- Bib: card `type: article` against the facet's @inproceedings. No other disagreement.
