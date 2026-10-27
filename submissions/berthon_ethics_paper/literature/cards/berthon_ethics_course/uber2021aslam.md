---
citekey: uber2021aslam
title: Uber BV and others v Aslam and others
authors: Leggatt, George (Lord Leggatt, with whom Lord Reed, Lord Hodge, Lady Arden, Lord Sales and Lord Hamblen agree)
year: 2021
type: case
doi: null
venue: "UK Supreme Court, [2021] UKSC 5, judgment given 19 February 2021 (on appeal from [2018] EWCA Civ 2748)"
source_basis: partial-text
pages_read: "header; paras 1, 10-14, 43-45, 51-53, 71-72, 76, 93-102, 120-121, 130, 139-140"
source_url: https://caselaw.nationalarchives.gov.uk/uksc/2021/5
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C2_law/aslam.html
sha256: 5470d528278cfdac2942036dfff9fb57cc74803e43362c23eff34fa694f90e14
manuscript_lines: [31]
ledger_rows: [P2-004, P2-005, P2-006, B27]
verified: true
written: 2026-10-14
---

The key `uber2021aslam` is in `review/v3/resolutions/C2_law.bib` (and, per the verifier, now also in
`literature/references.bib`), which fits the `surnameYEARfirstword` form. The local copy is the full
judgment from the National Archives' Find Case Law service. I read its text extraction
`C2_law/aslam.txt` (sha256 `07b7f88a…`), which is one unbroken line, by paragraph number. The judgment is long,
and I read only the paragraphs listed above.

## Summary
The Supreme Court unanimously dismissed Uber's appeal and upheld the employment tribunal's finding that
London Uber drivers are "workers" entitled to the national minimum wage and paid leave (paras 1, 139). Uber's
written terms cast Uber BV as a technology-services provider and payment-collection agent, and Uber London as a
booking agent, with the transport contract running between driver and passenger (para 43). Lord Leggatt held
that the terms of a written contract are not the starting point. To start there "would reinstate the mischief
which the legislation was enacted to prevent", because the employer can dictate the terms (para 76). Five
findings justified worker status. Uber fixes the fare (para 94). Uber dictates the contract terms (para 95).
Uber constrains acceptance of rides by controlling information, for example withholding the destination, and by
monitoring acceptance rates (paras 96-97). Uber controls how drivers deliver the service, including through
the ratings system (paras 98-99). Uber restricts driver-passenger contact (para 100). Each week Uber BV pays
drivers the fares less a "service fee", which was 20% for the two lead claimants (para 11). The only written
agreements to which drivers were parties were with Uber BV (para 52). The court held that drivers who log on
in London contract with Uber London (para 130).

## Key facts it relies on
- Para 1: the question is whether drivers "work for Uber under workers' contracts" or, "as Uber contends", work for themselves as independent contractors.
- Para 11: "Uber BV makes a weekly payment to the driver of sums paid by passengers for trips driven by the driver less a 'service fee' retained by Uber BV. In the cases of Mr Aslam and Mr Farrar, the service fee was 20% of the fares."
- Para 43: Uber relies on terms stating "that the only role of Uber BV is to provide technology services and to act as a payment collection agent for the driver".
- Para 52: "The only written agreements to which drivers were parties were agreements with Uber BV, the Dutch parent company. No other Uber company was a party to those agreements."
- Para 76: treating the written terms as the starting point "would reinstate the mischief which the legislation was enacted to prevent", because the employer "is often in a position to dictate such contract terms".
- Paras 94-95: the fare "is fixed by Uber and the drivers have no say in it"; "the contractual terms on which drivers perform their services are dictated by Uber."
- Para 96: Uber controls "the information provided to the driver"; "the driver is not informed of the passenger's destination until the passenger is picked up".
- Para 99: the ratings system is "A further potent method of control"; failure to keep a set average rating leads to warnings and "ultimately … termination".
- Para 130: the tribunal was entitled to find that a driver logging on in London enters "a contract with Uber London".

## Critical notes from the literature
- Closed ledger P2-004 to P2-006 and resolution C2: "neutral" is the manuscript's gloss. Uber's own case was that
  it acts as the drivers' agent and technology provider (para 43), not that it is a neutral matcher.
- Closed ledger P2-005: Uber's US service-fee page says Uber takes no fee on some trips, so "each match" was
  changed to "its matches". *Aslam* para 11 gives 20% for the two lead claimants only.
- Resolution C2 (l. 185) and closed ledger P2-006: this is UK law on UK facts. If the sentence should rest on US
  terms, the author must supply Uber's US driver agreement (the Platform Access Agreement party clause). The
  10-K shows that the contracting entity varies by market.
- The judgment identifies two counterparties. The written agreements are with Uber BV (para 52), and the court
  found the worker's contract to be with Uber London (para 130).

## Key topics covered
employment status, worker status, gig economy, ride-hailing, Uber, written terms vs reality, unequal bargaining power, algorithmic control, ratings systems, information asymmetry, service fee, agency

## Where the manuscript uses it
- **L31**: "the ride-hail firm … earns a commission on its matches, and is also the driver's contractual
  counterparty (*Uber BV v Aslam*, 2021, [52])." The manuscript takes the claim that the firm is the driver's
  contracting party. Source: para 52 ("The only written agreements to which drivers were parties were agreements
  with Uber BV"). **holds**. The court's further finding that the worker's contract is with Uber London (para 130)
  strengthens the point that an Uber entity, not the passenger, is the counterparty.
- **L31, uncited clause**: "earns a commission on its matches". v3 gives no citation for this clause. *Aslam*
  para 11 supports it (a 20% "service fee" retained by Uber BV). The closed ledger's P2-005 fix proposed citing
  "[11]", but v3 does not carry it. **holds** if [11] is added.
- **L31, "presents itself as the neutral matcher"**: v3 cites Rosenblat & Stark (2016, p. 3761) here, not this
  case. Para 43 records Uber's own self-description as technology provider and payment-collection agent, which
  the closed ledger noted as the source for P2-004. **narrower** if this case were cited for it: Uber claimed
  agency, not neutrality.
- No quotation in the manuscript is attributed to this case.

## Verifier notes
- 2026-10-14. sha256 of `C2_law/aslam.html` (5470d528…) and `aslam.txt` (07b7f88a…) recomputed and match.
- All quoted strings under Key facts run exact against `aslam.txt`, each inside the paragraph the card gives (1, 11, 43, 52, 76, 94, 95, 96, 99, 130). Para 11 has curly double quotes around "service fee"; the card renders them as single quotes, a nesting convention only. Header confirms judgment given 19 February 2021; para 139 "I would dismiss this appeal".
- Uses at MANUSCRIPT_v3.md L31 (line unchanged) re-read: **holds** (para 52), **holds if [11] is added** (v3 still carries no cite for "earns a commission on its matches"), and **narrower** for "neutral matcher" (v3 cites Rosenblat & Stark there). All confirmed.
- Correction to the card's preamble (not a source fact): `literature/references.bib` now does carry `uber2021aslam` (l. 253), identical to `C2_law.bib`. Its note gives `pdf: D/aslam.html`, a path that does not exist; the file is at `C2_law/aslam.html`. Its note also says "read: Full", while this card reads selected paragraphs. v3's reference (L453) "*Uber BV v Aslam* [2021] UKSC 5 (UK Supreme Court)" agrees with the judgment.
