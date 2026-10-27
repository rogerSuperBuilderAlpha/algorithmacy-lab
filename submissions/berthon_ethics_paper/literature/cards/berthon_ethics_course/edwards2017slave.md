---
citekey: edwards2017slave
title: "Slave to the Algorithm? Why a 'Right to an Explanation' Is Probably Not the Remedy You Are Looking For"
authors: Edwards, Lilian and Veale, Michael
year: 2017
type: article
doi: 10.2139/ssrn.2972855
venue: Duke Law & Technology Review, vol. 16, no. 1, pp. 18-84
source_basis: full-text
pages_read: "pp. 18-19 (abstract), 67 (section IV.A, transparency fallacy), 81-82 (conclusion)"
source_url: null
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/M2/edwardsveale.txt
sha256: 9569cdc0fce698d0ee3922e706ec80802a78e8a6e52bdcb200f4abf813933ac6
manuscript_lines: [13, 147]
ledger_rows: [P1-011, P1-012, P4-073]
verified: true
written: 2026-10-14
---

## Summary
Edwards and Veale argue that a "right to an explanation" under the EU General Data Protection Regulation is unlikely to be a complete remedy for algorithmic harms. They give two reasons. The law is "restrictive, unclear, or even paradoxical" about when an explanation right is triggered. And the explanations that machine-learning research produces may not supply the "meaningful information about the logic of processing" the law asks for (abstract, pp. 18-19). Even if those problems were overcome, they argue that relying on individual explanation rights risks a "transparency fallacy". Individual data subjects lack the time, resources and expertise to use the explanations they would get. Drawing on Ananny and Crawford, they add that transparency places the burden on individuals who then find themselves "disconnected from power" (p. 67). They see promise in "subject-centric" and "pedagogical" explanations. They find, however, that the GDPR's rights to erasure and portability also "rely too much on individual rights for what are too often group harms" (p. 81). They therefore look to provisions that act before deployment and on the system rather than the individual: privacy by design, Data Protection Impact Assessments, and certification or seals. The paper's thesis is that "creating better systems" beats "grimly pursuing ... a 'meaningful' version of the interior of a black box" (p. 82).

## Key facts it relies on
- Abstract (pp. 18-19): the search for a right to an explanation "may be at best distracting, and at worst nurture a new kind of 'transparency fallacy.'"
- p. 67: "Relying on individual rights to explanation as the means for users to take control of ML systems risks creating a similar 'transparency fallacy.'"
- p. 67: "Individual data subjects are not empowered to make use of the kind of algorithmic explanations they are likely to be offered even if (unlikely as it seems) the problems identified in section III are overcome. Individuals are mostly too time-poor, resource-poor, and lacking in the necessary expertise to meaningfully make use of these individual rights."
- p. 67, after Ananny and Crawford: transparency places "a tremendous burden on individuals ... only then to find out they have little power to change things anyway, being 'disconnected from power.'" Dependence on transparency "may occlude the true problems which rest in societal power relations and institutions".
- p. 81: the rights to erasure and portability, "like the 'right to an explanation,' ... rely too much on individual rights for what are too often group harms."
- p. 82: privacy by design, DPIAs and certification "might go beyond the individual to focus a priori on the creation of better algorithms". They prefer "creating better systems, with less opacity, clearer audit trails, well and holistically trained designers, and input from concerned publics".

## Critical notes from the literature
- Facet M2 calls this "the strongest pre-emption of the paper's opening move". The claim that informing the individual is the wrong remedy is already made in legal scholarship. The paper's addition is the historical mechanism and the adaptivity claim (`facets/M2_algorithm_studies.md`:22-29, :164, :181).
- Facet N5 agrees that "comprehension without leverage" is not novel as a claim. Edwards and Veale, and Schade, already argue that disclosure and explanation do not give control (`facets/N5_prior_work_gap.md`:181).
- AUDIT_05 confirmed pp. 67 and 81-82 at PDF pages 50, 64 and 65. It found that the phrase "acting for users", attributed to them in a facet, is not in the text (`audit/AUDIT_05.md`:243, :353, :366).
- Facet N2 records that the CJEU has since held, in *Dun & Bradstreet Austria* (C-203/22, 27 February 2025, para. 57), that GDPR Art. 15(1)(h) gives "a genuine right to an explanation" (`facets/N2_platform_law.md`:100-109). In my reading, that settles one of the legal doubts Edwards and Veale raised, about whether and when the right applies. It leaves their transparency-fallacy argument standing, and that argument is the one the manuscript uses.
- Copy and identifiers: the local PDF is the Duke-paginated copy. The bib note places it on Newcastle's eprint server, and the URL was not recorded, so `source_url` is null. The bib DOI resolves to the SSRN record.

## Key topics covered
GDPR, right to explanation, Article 22, Article 15(h), machine-learning explainability, transparency fallacy, individual rights versus group harms, privacy by design, DPIAs, certification, right to erasure, data portability

## Where the manuscript uses it
- l. 13: "Edwards and Veale (2017, p. 67) call reliance on individual rights to explanation a 'transparency fallacy'". p. 67. **holds**. Their wording is that such reliance "risks creating a similar 'transparency fallacy'", which is hedged where the manuscript is flat, but the attribution is fair. Exact-string check on "transparency fallacy": **exact**.
- l. 13, quotation: "Individual data subjects are not empowered to make use of the kind of algorithmic explanations they are likely to be offered." Exact-string check: **exact in the words, but the source sentence continues** ("... offered even if (unlikely as it seems) the problems identified in section III are overcome."). The manuscript closes the quotation with a period that is not in the source. p. 67. **holds**. An ellipsis would mark the cut.
- l. 147: "Edwards and Veale (2017) show that the explanation a person is offered is one she is poorly placed to use". p. 67. **holds**: "Individuals are mostly too time-poor, resource-poor, and lacking in the necessary expertise". No page is given here; p. 67 would serve.

## Verifier notes
- 2026-10-14. Recomputed sha256 of `M2/edwardsveale.txt`: matches. Running heads ("No. 1] DUKE LAW & TECHNOLOGY REVIEW", pp. 18-84) confirm volume 16, issue 1, pp. 18-84.
- Checked all six key facts: abstract p. 19 ("at best distracting", restated p. 81), p. 67 (three passages), p. 81 ("group harms"), p. 82 ("creating better systems"). All present; footnote markers 189 and 192 interrupt two strings in the raw text.
- l. 13 quotation exact in the words but cut mid-sentence, as the card says; l. 13 and l. 147 verdicts (holds) confirmed. "acting for users" is indeed absent.
- Bib disagreements: bib DOI is the SSRN record (Crossref title for it is garbled: "Why a  Right to Explanationn"); manuscript gives no DOI. Authors, title, venue, volume, issue and pages agree.
