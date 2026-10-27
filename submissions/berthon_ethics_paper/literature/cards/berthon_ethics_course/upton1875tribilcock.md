---
citekey: upton1875tribilcock
title: Upton, Assignee, v. Tribilcock
authors: Hunt, Ward (Justice, for the Court; Miller J., with Waite C.J. and Bradley J., dissenting)
year: 1875
type: case
doi: null
venue: "Supreme Court of the United States, 91 U.S. 45-56 (October 1875); 23 L. Ed. 203; on error to the Circuit Court for the District of Iowa"
source_basis: full-text
pages_read: all (pp. 45-56, syllabus, opinion and dissent)
source_url: https://static.case.law/us/91/html/0045-01.html
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C2_law/cap_upton.html
sha256: c8af3883c434f1e1df17c08e5ef6b939dd063ae404dc27da116312dabf38b699
manuscript_lines: [171]
ledger_rows: [P5-025, P5-026, B02]
verified: true
written: 2026-10-14
---

The key `upton1875tribilcock` is in `review/v3/resolutions/C2_law.bib` (and, per the verifier, now also in
`literature/references.bib`), which fits the `surnameYEARfirstword` form. I read the Caselaw Access
Project scan's text (`C2_law/cap_upton.txt`, sha256 `219bbe96…`) in full. It carries star pages
`[[PAGE *46]]` to `[[PAGE *56]]`, and its OCR is noisy ("tbe" for "the"). The opinion text gives no date. The
date (decision 1875-10), the page range 45-56 and the parallel cite 23 L. Ed. 203 come from CAP's
`CasesMetadata.json` for 91 U.S., which I downloaded this session to
`pdfs/cards/upton/us91_CasesMetadata.json`.

## Summary
The assignee in bankruptcy of the Great Western Insurance Company sued Tribilcock for the 80% still unpaid on
his $10,000 stock subscription. Tribilcock pleaded that the company's agent had told him he would be liable for
only 20%, and that his certificate was stamped "non-assessable". Justice Hunt held that the capital stock is a
trust fund for creditors, which the directors cannot release (pp. 47-48). He held that the word
"non-assessable" at most bars further assessment after full payment (pp. 48-49). The agent's statements were
representations of law, not of fact. Tribilcock had held the charter and by-laws for days before he
subscribed. "That the defendant did not read the charter and by-laws, if such were, the fact, was his own
fault" (p. 50). The Court stated the duty to read in general terms: "if he will not read what he signs, he
alone is responsible for his omission" (p. 50). A mistake of law does not avoid a contract (pp. 50-51). On the
second point, a party who claims fraud must use diligence to discover it and repudiate promptly. Tribilcock had
waited from 1870 to 1873 (pp. 52-55). The judgment was reversed and a new trial ordered. Justice Miller,
joined by two others, dissented on the fraud defence (pp. 55-56).

## Key facts it relies on
- p. 45 (syllabus 2): representations about non-assessability are "no defence" where the holder "has failed to use due diligence to ascertain the truth or falsity of such representations."
- p. 47: "The capital stock of a moneyed corporation is a fund for the payment of its debts. It is a trust fund, of which the directors are the trustees."
- p. 49: "There was here no error, mistake, or misrepresentation of any fact. The defendant made the subscription he intended to make".
- p. 49: he "had received, several days before this time, a copy of the charter and by-laws of the company, and then had them in his possession."
- p. 50: "It will not do for a man to enter into a contract, and, when called upon to respond to its obligations, to say that he did not read it when he signed it, or did not know what it contained."
- p. 50: "If this were permitted, contracts would not be worth the paper on which they are written. … A contractor must stand by the words of his contract; and, if he will not read what he signs, he alone is responsible for his omission."
- p. 50: "The law is presumed to be equally within the knowledge of all parties."
- p. 55: "The judgment must be reversed, and a new trial had." Miller J. dissents, with Waite C.J. and Bradley J.

## Critical notes from the literature
- Closed ledger P5-026 and resolution C2: *Upton* shows that the duty to read is old, which justifies changing
  "modern" to "settled". *Schnabel v. Trilegiant* (2d Cir. 2012), 697 F.3d at 127, calls it the "'duty to read'
  rule" (C2 secondary; I did not open *Schnabel*).
- The case concerns a businessman who subscribed for $10,000 of stock and held the governing documents in hand.
  He was a literate, commercially sophisticated party with time to read. It says nothing about a party who
  cannot read, which is the manuscript's historical concern (compare `foster1869mackinnon`, *non est factum*).
- Facet M3 and `specht2002netscape` (p. 30): modern courts keep the rule but add an exception where "the writing
  does not appear to be a contract and the terms are not called to the attention of the recipient."

## Key topics covered
duty to read, contract formation, stock subscription, corporate trust fund doctrine, misrepresentation of law, mistake of law, fraud and rescission, diligence, bankruptcy assignee

## Where the manuscript uses it
- **L171**: "The settled rule runs the other way: 'A contract need not be read to be effective,' and 'Competent
  adults are bound by such documents, read or unread' (*Hill v. Gateway 2000, Inc.*, 1997, pp. 1148–1149; see
  *Upton v. Tribilcock*, 1875, p. 50)." The manuscript takes a nineteenth-century Supreme Court statement of the
  duty to read, to show the rule is settled and not merely modern. Source: p. 50 ("if he will not read what he
  signs, he alone is responsible for his omission"). **holds**: the passage sits after `[[PAGE *50]]` and before
  `[[PAGE *51]]`, so p. 50 is right.
- **L171, quotations**: both quoted strings are attributed to *Hill*, not to *Upton*. Exact-string check against
  *Upton*: neither string occurs in it, which is correct, because the "see" signal marks *Upton* as support, not
  as the source of the words. The *Hill* check is on `hill1997gateway`.

## Verifier notes
- 2026-10-14. sha256 of `C2_law/cap_upton.html` (c8af3883…) and `cap_upton.txt` (219bbe96…) recomputed and match. CAP `us91_CasesMetadata.json` confirms decision 1875-10, pp. 45-56, parallel 23 L. Ed. 203.
- All 8 Key-facts quotations confirmed: six run exact; the syllabus (p. 45) and the trust-fund sentence (p. 47) match once OCR noise is allowed ("due .diligence", "tbe", "wbicb"). Star pages *47, *49, *50, *55 confirmed; Miller J. dissents with Waite C.J. and Bradley J. at *55.
- Use at MANUSCRIPT_v3.md L171 (line unchanged) re-read: **holds**; the duty-to-read passage sits between [[PAGE *50]] and [[PAGE *51]]. Neither quoted string occurs in *Upton*, consistent with the "see" signal.
- Correction to the card's preamble (not a source fact): `literature/references.bib` now carries `upton1875tribilcock` (l. 261). Its note gives `pdf: D/cap_upton.html`, which does not exist (the file is `C2_law/cap_upton.html`), and "read: Part", while this card read the case in full. v3's reference (L463) "91 U.S. 45 (1875)" agrees.
