---
citekey: citron2008technological
title: Technological Due Process
authors: Citron, Danielle Keats
year: 2008
type: article
doi: null
venue: Washington University Law Review 85(6), 1249-1313
source_basis: partial-text
pages_read: "pp. 1249-1250, 1253, 1276 (passage), 1305-1306, 1313"
source_url: https://journals.library.wustl.edu/lawreview/article/id/6697/
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/M3/citron.txt
sha256: 5aa8f9fc15b1f31510ae0af6d2666e39e1963edbdbf6ebb5c36800b1e2a84537
manuscript_lines: [223, 283]
ledger_rows: [P6-017]
verified: corrected
written: 2026-10-14
---

Text note: the local PDF (`citron.pdf`, sha256 165fe727..., 65 pages) is the journal's own PDF; the same text
sits at `pdfs/N2_platform_law/scholarship/citron2008.txt` (byte-identical). Its 65 pages run from p. 1249 to
p. 1313, which confirms the end page 1313 that the bib note had from a search result only.

## Summary
Citron argues that automated decision systems in government break both procedural regimes of twentieth-century
administrative law. Due process requires notice and a hearing in adjudication; rulemaking requires public
participation. "This century's automated decision making systems combine individual adjudications with
rulemaking while adhering to the procedural safeguards of neither" (p. 1249). Hearings lose value through poor
notice and through "the hearing officer's tendency to presume a computer system's infallibility"; programmers
alter rules when coding them, "in ways the public, elected officials, and the courts cannot review" (p. 1249).
Her cases are state benefits and child-support systems built by private vendors, where some systems "lack
recordkeeping audit trails, making review of the law and facts supporting a system's decisions impossible"
(p. 1253). She proposes "technological due process": an "inquisitorial model of quality control" plus
mechanisms for transparency, accountability and accuracy (p. 1250). For individual rights, "At a minimum,
automated systems should generate audit trails that record the facts and rules supporting their decisions"
(p. 1305), so that agencies can give reasons and hearing officers can test the machine's findings (pp. 1305-1306).
The conclusion restates the aim: "fair, accountable, and transparent adjudications and rulemaking without
forgoing the benefits offered by computerized decision systems" (p. 1313).

## Key facts it relies on
- Automated systems "combine individual adjudications with rulemaking while adhering to the procedural
  safeguards of neither" (p. 1249, abstract).
- "Code, not rules, determines the outcomes of adjudications" (p. 1249).
- "Some systems adjudicate in secret, while others lack recordkeeping audit trails" (p. 1253).
- "Automated systems often fail to maintain audit trails of their decisions" (p. 1276, in the section on the
  failures of "Government 2.0").
- "At a minimum, automated systems should generate audit trails that record the facts and rules supporting
  their decisions" (p. 1305).
- Audit trails should record "a comprehensive history of decisions made in a case" and "the actual rules applied
  in every mini-decision" (p. 1305).
- A per se requirement would bind "no matter the identity of the private vendor that built the system" (p. 1305).
- Agencies set the trails' contours and courts apply the Mullane notice standard (p. 1306).

## Critical notes from the literature
- `literature/facets/M3_intermediaries_records.md:184-188` and ledger P6-017: Citron's setting is government
  adjudication under constitutional due process (benefits systems), not private platforms; using her for
  platform operators is an extension the paper must make or defend.
- `AUDIT_05.md:417` (M3-27) confirmed the p. 1305 audit-trail quotation.
- I read no published critique of the article this session; the arm's record holds none beyond the scope point.

## Key topics covered
due process, administrative law, automated decision systems, audit trails, notice and hearing, rulemaking, automation bias, government benefits systems, private vendors, Mathews v. Eldridge

## Where the manuscript uses it
- v2 l. 223: "Citron (2008) argued that automated decision systems owe their subjects audit trails." Takes the
  audit-trail proposal. Source p. 1305 ("At a minimum, automated systems should generate audit trails that record
  the facts and rules supporting their decisions"); p. 1253. **narrower**: Citron's duty runs from government
  agencies to individuals under due process, and her systems are public benefits and enforcement systems; the
  sentence sits in a paragraph about gig workers and platforms, so it reads wider than her claim.
- v2 l. 283 (reference list): WULR 85(6), 1249-1313. The PDF's running heads give vol. 85 and pp. 1249-1313
  (65 pages). **holds**.

## Verifier notes
- 2026-10-14. Recomputed sha256 of `M3/citron.txt` (matches) and of `citron.pdf` (165fe727..., matches the text note). Publisher page meta tags (journals.library.wustl.edu, article 6697) give WULR vol. 85, issue 6; running heads give pp. 1249-1313. Crossref holds no DOI for the article, so `doi: null` stands. Manuscript l. 283 and references.bib agree with the card: no bibliographic disagreement.
- Ran every quotation on the card as an exact-string check against the text: all match ("mini-decision" carries a real hyphen across the line break).
- Corrected one page: "Some systems adjudicate in secret, while others lack recordkeeping audit trails, making review of the law and facts supporting a system's decisions impossible" sits under the p. 1253 running head, not p. 1251 (text lines 219-236; the facet `M3_intermediaries_records.md:185` also gives p. 1253). Changed in Summary, Key facts, the l. 223 use bullet and `pages_read`.
- Checked the other page locators (1249, 1250, 1276, 1305, 1306, 1313) against the running heads: all correct.
- Use at l. 223: re-read; the **narrower** verdict stands (government due-process setting, cited in a platform paragraph).

