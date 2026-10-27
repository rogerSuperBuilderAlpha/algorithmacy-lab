---
citekey: kolt2025governing
title: "Governing AI Agents"
authors: Kolt, Noam
year: 2026
type: article
doi: 10.2139/ssrn.4772956
venue: "Notre Dame Law Review 101(1), 335-386 (running heads dated 2026; arXiv 2501.07913 preprint 2025)"
source_basis: partial-text
pages_read: "pp. 335-336 (abstract, contents), 344-345 (n. 28), 361-364 (Part II.C, Loyalty), 385-386 (Conclusion)"
source_url: https://ndlawreview.org/wp-content/uploads/2026/08/Kolt_101.335.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C2_law/kolt_101_335.txt
sha256: aee0792cee615e5fa86c0b16102e39484f9389cf54600ae09008c4fcd5ceeb3c
manuscript_lines: [225, 331]
ledger_rows: [P6-019, P6-020, P6-021]
verified: true
written: 2026-10-14
---

## Summary
Kolt argues that AI agents, systems that "plan and execute complex tasks with only limited human involvement",
can be analysed with the economics of principal-agent problems and the common law of agency (p. 335). The
Article makes three moves (p. 335). First, it identifies the problems AI agents raise: information asymmetry,
discretionary authority, loyalty and delegation (Part II). Second, it shows that the usual fixes, incentive
design, monitoring and enforcement, may fail for agents that make uninterpretable decisions at unprecedented
speed and scale (Part III). Third, it proposes governance principles of inclusivity, visibility and liability,
backed by "new technical and legal infrastructure" (Part IV). In footnote 28 Kolt records the "apparent
consensus" that AI agents are not agents at common law, quoting the Restatement (Third) of Agency § 1.04
cmt. e. He adds that the words "at present" leave the rule open and that the Restatement cites one article
(p. 345). The loyalty section (pp. 361-364) sets out the agent's duty to act "loyally for the principal's
benefit". AI agents "can hardly be said to consistently act in the user's best interests", because they are
"developed by private for-profit corporations" and lack "single-minded loyalty ... At least not to their
users" (p. 363).

## Key facts it relies on
- The Article draws on agency law and theory to identify "information asymmetry, discretionary authority, and
  loyalty" problems (p. 335).
- Restatement (Third) of Agency § 1.04 cmt. e: "[A] computer program is not capable of acting as a principal
  or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons
  who use them." (p. 345, n. 28).
- Kolt notes the "at present" qualifier and the Restatement's reliance on a single article (Sommer 2000)
  (p. 345, n. 28).
- Agents owe a "fiduciary duty to act loyally for the principal's benefit", quoting Restatement § 8.01
  (p. 362).
- "even if AI agents do not pursue self-interest, they can hardly be said to consistently act in the user's
  best interests" (p. 363).
- "The most advanced AI agents are, after all, being developed by private for-profit corporations"; they lack
  "single-minded loyalty ... At least not to their users" (p. 363).
- An overarching duty of loyalty is "needed" to protect users and spare them costly instructions (p. 364).
- Conclusion: principles of inclusivity, visibility and liability, plus "new technical and legal
  infrastructure" (pp. 385-386).

## Critical notes from the literature
- Facet M3 (`literature/facets/M3_intermediaries_records.md:180, 284, 315`) read the arXiv version (n. 26 there)
  and treated the Restatement note as forcing the paper to say who is the legal agent behind a user's
  software.
- Facet M3 (`:260`) found no scholarship that casts the user-side agent as a third party with its own conflict
  of interest. Facet N5 (`literature/facets/N5_prior_work_gap.md:153`) adds Priyanshu et al. (2026, preprint)
  as experimental support for that claim, which otherwise rests on Kolt's legal analysis.
- Kolt's n. 28 lists scholars on both sides of whether software can be an agent (Chopra and White, Scherer
  against; Bellia, Bayern for the Restatement), so the Restatement position is contested (p. 345).
- AUDIT_05 (`literature/audit/AUDIT_05.md:377`) and DOI_CHECK flagged the year and volume: Crossref's SSRN
  record is dated 2024. The journal page (`pdfs/C2_law/nd_kolt.html`) lists the Article under Volume 101,
  Issue 1, and the PDF running heads read "2026]" and "[VOL. 101:335". The PDF header also reads "KOLT_UPDATED
  PAGE PROOF.DOCX ... 8/21/26".
- This card's citekey keeps the bib's 2025, but the published version I read is dated 2026.

## Key topics covered
AI agents, agency law, principal-agent theory, Restatement (Third) of Agency, duty of loyalty, information
asymmetry, monitoring, liability, AI governance, alignment

## Where the manuscript uses it
- **Line 225, quotation check**: "as Kolt (2025) quotes the Restatement, 'At present, computer programs are
  instrumentalities of the persons who use them'". Exact-string check: **exact** (p. 345, n. 28, published
  version; n. 26 in arXiv v2). **holds.**
- **Line 225**, "the agent carries its user's interest and no duty to anyone else". Source: p. 345 n. 28,
  p. 363. **narrower.** On the Restatement view a program holds no duties at all; it is a tool. Kolt's own
  point (p. 363) is that AI agents cannot be relied on to carry the user's interest. The manuscript's gloss
  sits closer to the Restatement than to Kolt.
- **Line 225**, the agent "is itself a new third party whose supplier has interests of its own". Source:
  p. 363 (for-profit developers; no "single-minded loyalty ... At least not to their users"). **holds** as
  Kolt's concern; the "third party" framing is the paper's.
- **Line 331, reference entry**: "Kolt, N. (2025). Governing AI agents. *Notre Dame Law Review, 101*."
  **does not hold** as printed. The published Article is 101 *Notre Dame L. Rev.* 335-386, Issue 1, dated 2026
  in its running heads (journal PDF). Author's call: cite 2026 with pages 335-386, or cite the 2025 arXiv
  preprint.

## Verifier notes
- Recomputed sha256 of `kolt_101_335.txt`: matches. Crossref has only the SSRN posting (10.2139/ssrn.4772956, posted-content, 2024). The journal PDF runs pp. 335-386 with running heads "2026]" and "[VOL. 101:335"; the saved journal page lists Volume 101, Issue 1. Bib (2025, no pages, arXiv URL, stale note) and manuscript reference (2025, no pages) disagree with the published version.
- Confirmed: abstract (three contributions; "new technical and legal infrastructure ... inclusivity, visibility, and liability", p. 335); n. 28 Restatement quotation, "at present", Sommer, and the scholars on both sides (Chopra & White and Scherer against; Bellia and Bayern for) on p. 345; Restatement § 8.01 loyalty (p. 362); "can hardly be said", "private for-profit corporations", "single-minded loyalty" (printed "singleminded") and "At least not to their users" (p. 363); overarching duty "needed" (p. 364).
- L225 quotation exact (p. 345, n. 28). Verdicts confirmed: L225 gloss **narrower**; "new third party" **holds** as Kolt's concern; L331 reference **does not hold** as printed.
- Verified 2026-10-14.
