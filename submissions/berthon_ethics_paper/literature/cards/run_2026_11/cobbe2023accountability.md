---
citekey: cobbe2023accountability
title: Understanding accountability in algorithmic supply chains
authors: Cobbe, Jennifer; Veale, Michael; Singh, Jatinder
year: 2023
doi: 10.1145/3593013.3594073
source_basis: partial-text
pages_read: Abstract (pdf p. 1); §§4-5 whole (arXiv v2 pdf pp. 7-11 of 13, counted, since the PDF prints no page numbers); §4.3 and §5 read at the Fable read
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B4/cobbe2023accountability/cobbe.pdf
sha256: fad0d945f5c1a66f54ad04e8671e970e0ec50aac455433cebaebd1b57c48e30a
verified: corrected
structure_sections: 7-D05; 6-responsibilization; 4.4-loss
type: article
venue: 2023 ACM Conference on Fairness, Accountability, and Transparency (FAccT 2023), pp. 1186-1197
source_url: https://arxiv.org/pdf/2304.14749
record_check: crossref https://api.crossref.org/works/10.1145/3593013.3594073; the arXiv v2 preprint (22 May 2023) was read, not the ACM version of record
facet: B4
supersedes: none
written: 2026-11-18
---

## Summary

Read: Abstract and sections 4-5 of the arXiv preprint (sections 4.3 and 5 at the Fable read); sections 1-3 are unread, and the ACM version of record was behind a bot challenge and was not opened. The authors argue that algorithmic systems are increasingly produced, deployed and used within supply chains of several actors joined by data flows, so accountability for the "many hands" must be allocated across the chain. They hold that responsibility is distributed and that there is typically no one actor in overall control. They criticise the proposed EU AI Act, cited as the Commission's 2021 proposal (ref. [28]): where a user of an AI service puts it to an unintended purpose, the Act would potentially make that downstream user responsible for production-related requirements it cannot meet, while the actor who developed and controls the technology would face no obligations. They also describe an "accountability horizon", the point beyond which an actor cannot see along the chain (§4.2). Section 4.3 argues that providers use service agreements and APIs to keep control past deployment while disclaiming legal accountability. The text under review is the proposed Act, not the Regulation as adopted.

## Key facts it relies on

- Abstract: "it is the working together of an algorithmic supply chain of different actors who contribute to the production, deployment, use, and functionality that drives systems and produces particular outcomes." [quote] Abstract
- "Even when some actors are influential, there is therefore typically no one actor in overall control of a supply chain." [quote] §4.1 (pdf p. 7)
- Accountability "involves a relationship where an actor provides accounts of their activities to a forum, who imposes consequences to correct the actor if needed". [quote] §4.1 (pdf p. 7)
- Under the proposed AI Act, a user who uses an AI service for an unintended purpose becomes legally responsible for the underlying system; the authors say this does not reflect supply chain interdependencies. [paraphrase] §4.1.1 (pdf p. 8)
- "While the user would inevitably be unable to comply (due to the actual distribution of practical responsibilities in algorithmic supply chains), the actor who developed and controls that technology and is thus factually responsible for production would face no obligations." [quote] §4.1.1 (pdf p. 8)
- "Particular attention is due to systemically important actors – primarily Amazon, Microsoft, Google, and perhaps a few others." [quote] §4.1.2 (pdf p. 8)
- No actor may have enough knowledge of or control over both production and deployment to assess and mitigate impacts, so risk-management approaches are "arguably not appropriate" in this context. [paraphrase] §4.2.2 (pdf p. 9)
- "Know your customer" requirements and monitoring of misuse could help providers understand customers' purposes, but give visibility over one or two steps only. [paraphrase] §4.2.3 (pdf p. 9)
- CJEU case law gives data subjects the right to know the identities of the recipients of their personal data; where the controller does not know them, data subjects can be told only the categories of recipients, which the authors call significantly less useful. [paraphrase] §4.2.3 (pdf p. 9)
- "Providers disclaim legal accountability for things that happen through use of their services" and try to position themselves as data processors even when they use customer data for their own purposes. [quote] §4.3.1 (pdf p. 10)

## Critical notes

- Preprint of a conference paper; the version of record may differ.
- Limits: written about the proposed AI Act; the adopted Act's provider and deployer duties are not covered here and should be checked against the B5 card. The paper is about accountability among organisations. In sections 4-5 the person acted on appears once, as the data subject with a right to know who received her data (§4.2.3); her standing and redress are not discussed. The Acknowledgments (pdf p. 11) record that two authors' research group is supported by UK Research & Innovation, The Alan Turing Institute and Microsoft, via the Microsoft Cloud Computing Research Centre.
- Reads against a simple "provider makes, deployer answers" split: it warns that loading duties onto the deployer can shield the provider.
- Bearing for Q4. Person acted on gets: record partial (identities of recipients of her data, or only their categories, §4.2.3); brake no; envelope no; standing no (accountability runs to a "forum", not to her, §4.1); loss cover no. Not read: §§1-3.
- Corrected by V-B-2: pages_read widened to §§4.1-4.2.3, since the facts and Summary cite §4.2 (accountability horizon) and §4.2.2; venue pages 1186-1197 added from Crossref.
- Corrected at the Fable read (V-B-2): (1) the Summary dated the proposed AI Act to 2023; the paper cites the Commission's 2021 proposal, COM(2021) 206 (ref. [28]), and writes "would potentially make", not "would make". (2) The PDF has 13 pages, not 14, and prints no page numbers; `pages_read` now covers §§4-5, which I read whole. (3) The split quotation from §4.1.1 is one continuous sentence in the source and is now given as one. (4) "of doubtful fit" replaced by the authors' "arguably not appropriate"; its locator is §4.2.2 alone. (5) The note that the paper "does not discuss the person acted on" and the entry "record no" were too absolute, as the verifier said; both now carry the §4.2.3 passage on data subjects. (6) Three facts added (§4.1.2, §4.2.3, §4.3.1), a sentence on §4.3 added to the Summary, and the Microsoft funding line noted. Pdf page numbers added to locators. The other quotations are unchanged.
