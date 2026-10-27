---
citekey: specht2002netscape
title: Specht v. Netscape Communications Corp.
authors: Sotomayor, Sonia (Circuit Judge, for the court; McLaughlin and Leval, Circuit Judges)
year: 2002
type: case
doi: null
venue: "United States Court of Appeals, Second Circuit; 306 F.3d 17 (Docket Nos. 01-7870, 01-7872, 01-7860), argued 14 Mar. 2002, decided 1 Oct. 2002"
source_basis: partial-text
pages_read: "pp. 20-35 (the Michigan excerpt, read through: Background, Proceedings Below, Part III); targeted passages of the full CAP text at pp. 20, 27, 30, 32, 35, 40"
source_url: https://static.case.law/f3d/306/html/0017-01.html
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/cards/specht/specht_cap.html
sha256: a1c8391bf80b7ebbeb59f3f14d8aa61d283c0e941e0f1dc6b9b0b37151af212c
manuscript_lines: [137]
ledger_rows: [P4-056]
verified: true
written: 2026-10-14
---

Key `specht2002netscape` is from `literature/references.bib`. The arm had only the University of Michigan
seven-page excerpt (`pdfs/M3/specht.txt`, sha256 `a198bafe…`, extracted from `M3/specht_umich.pdf`; note that
`M3/specht.pdf` is a saved 404 page, not the case). This session I downloaded the full opinion from the
Caselaw Access Project's static site (`static.case.law/f3d/306`; CAP metadata gives pp. 17-40, decided
2002-10-01). I extracted it to `cards/specht/specht_cap.txt` (sha256 `97226fe0…`), with star pages *20-*40.
The excerpt and the CAP text agree wherever they overlap. I did not read the CAP text in full, so the basis is
`partial-text`.

## Summary
Netscape offered its free SmartDownload plug-in on a webpage with a "Download" button. The only reference to
license terms, which included an arbitration clause, appeared on a screen below the button, and users saw it
only if they scrolled down. Users who downloaded the plug-in sued under federal privacy statutes, and Netscape
moved to compel arbitration. Applying California law, the Second Circuit (Sotomayor, J.) affirmed the denial.
A transaction becomes a contract only on a manifestation of assent. "a consumer's clicking on a download button
does not communicate assent to contractual terms if the offer did not make clear to the consumer that clicking
… would signify assent." The court accepted the general rule that a party cannot escape a contract he failed to
read. It held, however, that the rule's exception applies where "the writing does not appear to be a contract
and the terms are not called to the attention of the recipient". It distinguished *Hill v. Gateway* and
*ProCD*. "Reasonably conspicuous notice of the existence of contract terms and unambiguous manifestation of
assent to those terms by consumers are essential if electronic bargaining is to have integrity and
credibility." The court also held that Communicator's separate clickwrap did not reach SmartDownload claims, and
that the website owner Specht was not bound as a direct beneficiary.

## Key facts it relies on
- p. 20: "a reasonably prudent Internet user in circumstances such as these would not have known or learned of the existence of the license terms … and that defendants therefore did not provide reasonable notice of the license terms." Downloading "did not unambiguously manifest assent".
- pp. 22-23: Communicator required clicking "Yes" to a scrollable license. SmartDownload had "no clickwrap presentation", and its terms appeared only on "the next screen".
- p. 27: California law governs contract formation (not appealed).
- pp. 29-30: "a consumer's clicking on a download button does not communicate assent to contractual terms if the offer did not make clear to the consumer that clicking on the download button would signify assent to those terms". The court quotes *Windsor Mills*: an offeree "is not bound by inconspicuous contractual provisions of which he is unaware, contained in a document whose contractual nature is not obvious."
- p. 30: "It is true that '[a] party cannot avoid the terms of a contract on the ground that he or she failed to read it before signing.'" The exception applies "when the writing does not appear to be a contract and the terms are not called to the attention of the recipient."
- p. 32: "a reference to the existence of license terms on a submerged screen is not sufficient to place consumers on inquiry or constructive notice of those terms." Where notice is not reasonably conspicuous, "the transactional circumstances cannot be fully analogized to those in the paper world of arm's-length bargaining."
- pp. 32-33: *Hill v. Gateway 2000* and *ProCD* are distinguished. In those cases terms came with the product or were shown every time the program ran.
- p. 35: "Reasonably conspicuous notice of the existence of contract terms and unambiguous manifestation of assent to those terms by consumers are essential if electronic bargaining is to have integrity and credibility."
- p. 40: the court affirms the refusal to compel arbitration of Specht's claims, and the conclusion affirms the denial in full.

## Critical notes from the literature
- Facet M3 (l. 126-129, 248): *Specht* protects a user who never had reasonably conspicuous notice. It does
  nothing for a user who saw the terms and did not read them, and it attaches to notice and assent, not to
  inability to read. *Hill* and *Specht* sit side by side in the same body of law. M3 did not read later notice
  cases (*Nguyen v. Barnes & Noble*, 9th Cir. 2014; *Meyer v. Uber*, 2d Cir. 2017).
- AUDIT_05 (M3-8, M3-9) confirmed two *Specht* quotations exact at *32 and *30 against the Michigan excerpt. The
  CAP text gives the same pages.
- Closed ledger P4-056 is `blocked-on` the official reporter, because only an excerpt had been read. The CAP copy
  downloaded this session is the full 306 F.3d text with star pages, so it clears that block.
- The holding applies California contract law to one interface (a download button with terms below it). It
  does not address clickwrap, where assent is express.

## Key topics covered
online contract formation, browsewrap, clickwrap, reasonable notice, manifestation of assent, inquiry notice, duty to read, arbitration clauses, Federal Arbitration Act, California law, Hill v. Gateway, ProCD v. Zeidenberg

## Where the manuscript uses it
- **L137** (Table 1, "The record" row, last column): "The user has agreed to standard terms; the law treats that
  as assent where notice was reasonable (*Hill v. Gateway 2000*, 1997; *Specht v. Netscape*, 2002)." The
  manuscript takes the rule that assent to standard terms requires reasonable notice. Source: pp. 20, 30-32, 35.
  **holds**: *Specht* makes reasonably conspicuous notice a condition of assent and accepts the
  no-escape-for-not-reading rule (p. 30). Together with *Hill* it supports the manuscript's sentence. The
  manuscript gives no pin cite; p. 35 would serve.
- No quotation in the manuscript is attributed to this work.

## Verifier notes
- 2026-10-14. sha256 of `specht_cap.html` (a1c8391b…), `specht_cap.txt` (97226fe0…) and the excerpt `M3/specht.txt` (a198bafe…) all recomputed and match.
- All 12 quoted strings under Key facts run exact against `specht_cap.txt` (two only after joining a page break mid-word at *29/*30 and dropping the court's bracketed "[a]"); star pages *20, *23, *27, *29-30, *32, *35 and *40 confirmed for each. Hill and ProCD are distinguished at *32; affirmance at *40.
- Use at MANUSCRIPT_v3.md L137 (Table 1, "The record" row; line unchanged in v3) re-read: **holds** confirmed. No quotation in v3 is attributed to the case.
- Bib: v3 reference (L447) "306 F.3d 17 (2d Cir. 2002)" agrees with CAP metadata. `references.bib` still gives the Michigan excerpt URL and the note "7-page excerpt … Not the official reporter"; the card's CAP copy is the full opinion, so the bib note is now stale (not a citation error).
