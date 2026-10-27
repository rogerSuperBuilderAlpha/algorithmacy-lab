---
citekey: bommasani2026algorithmic
title: Algorithmic Monocultures in Hiring
authors: Bommasani, Rishi and Bana, Sarah H. and Creel, Kathleen A. and Jurafsky, Dan and Liang, Percy
year: 2026
type: article
doi: 10.1145/3805689.3812400
venue: Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26), Montreal, pp. 6351-6382
source_basis: full-text
pages_read: "pp. 1-4, 12-15 (PDF pages of arXiv 2605.27371v1, 32 pp.)"
source_url: https://arxiv.org/abs/2605.27371v1
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/v3_ledger/bommasani2026.txt
sha256: 46c3e40ba2c41dcac61fd21e4744358f0a87af50beccf202fd0c102df9d989af
manuscript_lines: [17, 135, 141, 275]
ledger_rows: [P1-004, P1-028, P4-048, P4-062, P4-063, P4-064, P4-065, P4-066, P6-002, P6-048]
verified: true
written: 2026-10-14
---

Key note: `references.bib` has no entry for this work (P6 ledger, reference-list row 9: "Not in bib").
I made the key `bommasani2026algorithmic` in the form surnameYEARfirstword.

Text note: I read the arXiv v1 PDF (`bommasani2026.pdf`, sha256 3605725f...). It carries the FAccT '26 ACM
reference format, the DOI and a CC BY 4.0 licence, and it runs 32 pages, the same length as the ACM range
6351-6382. Page numbers below are PDF pages. That PDF p. n equals ACM p. 6350+n is my inference; I did not
check it against the ACM typeset copy.

## Summary
Bommasani and colleagues ask whether "algorithmic monoculture", many employers relying on the same vendor's
screening algorithms, makes the same people and the same racial groups face rejection across employers
(p. 1). They obtained data from the vendor pymetrics covering 4,197,168 applications by 3,372,132 applicants to
1,746 positions at 156 employers; each application is scored by a pymetrics model from game play and binarized
into "recommend" or "do not recommend" (p. 2). Disaggregated by position, 10.62% of positions show adverse
impact against Black applicants under the 4/5ths rule, and 25.87% of Black applicants' applications go to such
positions (p. 2). On homogeneity, 4% of applicants who apply to ten positions are recommended for rejection from
all of them, and the systemic-rejection rate decays more slowly than independent decisions would predict; a
correspondence-study benchmark fits independence (pp. 1, 3). A counterfactual run shows every applicant would
be recommended by at least one model, but realistic applicants would need about 25 applications, against 10
under independence, to push systemic rejection below 0.1% (p. 3). The authors recommend position-level audits,
market surveillance, monoculture monitoring and mandated researcher access (pp. 13-14), and they list limits on
generalizability, applicant quality and downstream use (p. 15).

## Key facts it relies on
- Dataset: 4,197,168 applications, 3,372,132 applicants, 1,746 positions, one vendor (pymetrics); 156
  employers across 11 industries (p. 2).
- Models score game-play features and output "recommend" or "do not recommend"; a "do not recommend" applicant
  is "likely to be rejected without consideration by a human" (p. 2).
- "42 pymetrics models screen applicants at multiple companies" (p. 3); other positions use different
  pymetrics models.
- "4% of all applicants who apply to 10 positions are recommended for rejection from all positions, a rate
  higher than expected by chance" (p. 1, abstract); "Of applicants that apply to ten positions, 4% are rejected
  from all positions" (p. 3).
- "applicants would need to apply widely in order to ensure their applications are considered by a human"
  (p. 1, abstract).
- 10.62% of positions show adverse impact against Black applicants; 25.87% of Black applicants' applications
  go to such positions (pp. 1-2).
- To reach systemic rejection below 0.1%, 25 applications are needed against 10 under independence (p. 3).
- Limitations: one vendor and a game-based method; no measure of applicant quality or model validity; final
  employer use of recommendations unknown, though non-recommendation makes rejection "very likely" (p. 15).

## Critical notes from the literature
- The authors' own limits (p. 15): findings "may not generalize to all algorithmic screening"; they observe
  recommendations, not final hiring decisions.
- Ledger P6-002 (`review/v3/ledger_parts/P6.md`) first rated the 4%-of-ten figure "unsupported" at abstract
  depth; P1-028 and P4-062 to P4-066 later confirmed it on the arXiv full text. P4-065 asks for the ACM page
  numbers to be checked if a page is cited.
- `literature/facets/M4_ethical_frameworks.md:98, 201` (Creel and Hellman 2022) warns that isolated arbitrary
  decisions "are not of moral concern except when other rights make nonarbitrariness relevant", so the paper must
  say why the Bommasani cell is a wrong and not just an arbitrariness.
- P1-004 notes the manuscript's opening reaches "credit, work and civic standing"; this study supports work only.

## Key topics covered
algorithmic monoculture, outcome homogenization, systemic rejection, hiring algorithms, pymetrics, adverse impact, 4/5ths rule, researcher data access, EU AI Act, NYC Local Law 144

## Where the manuscript uses it
- v2 l. 17: "where employers share a screening vendor, 4% of applicants who apply to ten positions are
  recommended for rejection from all ten". Takes the 4%-of-ten figure. Source p. 1 (abstract), p. 3. **holds**:
  figure and wording ("recommended for rejection") match the abstract; the data are from one vendor.
- v2 l. 135 (table, gate today): "Shared screening models that reject the same applicants across employers".
  Takes the systemic-rejection finding. Source p. 3 (42 models shared across companies; homogeneity also across
  different models). **narrower**: the models "recommend" rather than reject (p. 2, p. 15), and only 42 models are
  literally shared; the homogeneity across other models is the paper's empirical finding, not shared-model
  identity.
- v2 l. 141: "study roughly three million applicants screened by a single vendor's models". Source p. 2
  (3,372,132 applicants; pymetrics). **holds**.
- v2 l. 141: "4% of those who apply to ten positions are recommended for rejection from all ten, a rate above
  chance". Source p. 1 (abstract), p. 3 ("decays more slowly than would be expected by chance"). **holds**.
- v2 l. 141, quotation: "would need to apply widely in order to ensure their applications are considered by a
  human." Exact-string check against the PDF text: **exact match** (p. 1, abstract). **holds**; the manuscript
  gives no page, and p. 1 (ACM p. 6351 by inference) would serve.
- v2 l. 141: "nothing in the study suggests a purpose to exclude". Source pp. 1-4, 12-15 as read: the paper
  attributes homogeneity to shared vendor models (p. 3) and notes pymetrics "aims to pro-actively debias each
  model" (p. 3). **holds** on the pages I read; I did not read pp. 5-11 or the appendices.
- v2 l. 141: "A single reader's judgment follows the applicant from door to door, and the applicant cannot ask
  it a question." The manuscript's own gloss. **narrower**: the "single reader" is one vendor running many
  position-specific models (p. 2), shared literally for 42 models only (p. 3). The second clause **cannot check
  (full-text)**: the pages I read say nothing about applicant queries or contestation.
- v2 l. 275 (reference list): FAccT 2026, pp. 6351-6382, DOI 10.1145/3805689.3812400. The PDF's ACM reference
  block gives the title, five authors, FAccT '26 and the DOI (p. 1). **holds**; the page range rests on the
  Crossref record cited in P4-065, which I did not re-fetch.

## Verifier notes
- 2026-10-14. sha256 of `local_path` (txt) recomputed: matches. The PDF's sha256 also matches the card's prefix (3605725f...).
- Crossref (10.1145/3805689.3812400), fetched this session: title, the five authors, FAccT 2026 proceedings, pp. 6351-6382, issued 2026-06-25. These match the card and the manuscript's reference (v2 l. 275). `references.bib` still has no entry, as the card says.
- Every key fact was string-checked against the arXiv text, with the page taken from the form-feed page breaks: dataset counts (p. 2); 156 employers and 11 industries (p. 2); "42 pymetrics models" (p. 3); 4%-of-ten (pp. 1, 3); 10.62% (p. 2) and 25.87% (pp. 1-2); 25 vs 10 applications (p. 3); "pro-actively debias" (p. 3); "may not generalize" and "very likely" (p. 15; "very likely" also on p. 8); Recommendations 1-4 (pp. 13-14). All confirmed.
- The l. 141 quotation is an exact match (p. 1). I confirm all the use verdicts, including the two narrower ones and the cannot-check on applicant contestation.
