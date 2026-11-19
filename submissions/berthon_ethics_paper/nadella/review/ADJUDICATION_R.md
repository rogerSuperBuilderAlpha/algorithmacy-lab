# Adjudication of the R round

*Written by Claude (the lead), 2026-10-24. Working notes for the author, not paper prose. Inputs: R1–R5 review files,
R6's audit (`AUDIT_R6.md`, 117 rows, 12 disagreements, 10%). For each ruling below, "reopened" means I opened the
local copy myself and matched the words; "on R6" means I rely on R6's match without reopening.*

## Rates

| Run | Rows audited by R6 | Disagree | Rate |
|---|---|---|---|
| R1 historical | 25 | 3 | 12% |
| R2 present case | 24 | 1 | 4% |
| R3 normative frame | 21 | 2 | 10% |
| R4 argument logic | 16 | 4 | 25% (strength of inference, not misread sources) |
| R5 novelty, counter-case | 31 | 2 | 6% |

No fabricated quotation; 35 of 35 card hashes match; 17 DOIs checked against Crossref with no update or retraction
notice. All 36 R-facet cards stay `verified: pending` until the S2 blocks are written (below, "Card work").

## Rulings that change the argument

| # | Item | Ruling | Evidence | Effect |
|---|---|---|---|---|
| 1 | **R2-16: the law gives the person more than the draft says** | Upheld in full | Reopened: GDPR art. 22(1) "the right not to be subject to a decision based solely on automated processing"; 22(3) "at least the right to obtain human intervention ... to express his or her point of view and to contest the decision"; *SCHUFA* para 52 "a prohibition in principle"; *Dun & Bradstreet* para 58 "a right to an explanation of the procedure and principles actually applied". Also noted myself: art. 22(2)(a) exempts decisions "necessary for entering into, or performance of, a contract", so a refund decision falls under the exception with 22(3)'s safeguards, not the prohibition | A8 restated. §4's "law already provides" reply rewritten as a gap: rights are enumerated, after the decision, run by the controller, and absent from the architecture. Art. 22(1) becomes the present precedent for duty 1 (structural refusal) |
| 2 | **R1-04: Saenger "unsupported"** | Overruled (R6 right) | dxd `AUDIT_01.md` lines 9, 26, 29, 31 and AUDIT_06 rows: Google Books search-inside (id `w3vZaFoaa3EC`) confirms pp. x, 83, 85, 87, the clean route BRIEF §6 names | Quotations stay. p. 100 stays "wording confirmed, page needs a library copy" |
| 3 | **R1-26 + R4 HP5 + R1-05: the two courses** | Upheld, narrowed per R6 | Reopened Foxe vol. 3 (Arundel's constitutions license *texts* examined by the universities, not readers); R1/R4 rest the rest on Johns 1998 p. 36, Johns 2002 pp. 119, 121, Parkes (on R6) | The scribes' correction and the print stage are **two recurring choices, not two stages**. Historians do not periodize literacy this way, and the draft's own Carolingian moment shows the corrected text under custody. CA is restated by beneficiary (Argument A below). "Print stage" survives only as the name for England's press regime 1557–1695, the paper's clearest case of the choice. **Author's call:** the title |
| 4 | **R1-05: Carolingian page "set from above"** | Upheld | Boretius p. 80 (on R6, card verified earlier): the capitulary concerns correcting texts corrupted by "librariorum imperitia" | Claim narrowed to custody of the corrected text |
| 5 | **R1-16b: the Requerimiento's hearers "informed after the fact"** | Upheld (wrong) | Ledger H18; R6 verified | Shared property becomes notice the hearer could neither understand nor answer, read before the attack |
| 6 | **R1-17 + R4 HP2: the literacy-test gate, position vs intent** | Narrower, not wrong (R6) | Reopened *Lassiter* 360 U.S. at 51 "some relation to standards designed to promote intelligent use of the ballot", at 53 "We do not sit in judgment on the wisdom of that policy" | The historical verdict condemns the registrars' discretion and the state-made illiteracy (*Gaston*), not literacy as a qualification. The gate pairing stays in Argument A on the 1901 convention's own objection to registrars' discretion (Alabama p. 11), a position-based objection. The gate/brake disanalogy (deciding entry vs stopping a process) must be argued, not assumed |
| 7 | **R1-06: the Stationers' charter's purpose** | Upheld (contested) | Blayney via Smyth (secondary), Clegg (abstract), Johns 2002 p. 119 (on R6) | The custodian claim holds; the Crown-control purpose is stated as disputed |
| 8 | **R1-13/14: the duty to read** | Upheld (narrower) | `L'Estrange` p. 403 "in the absence of fraud, or ... misrepresentation" (on R6) | Stated as a presumption of assent with fraud and misrepresentation defences |
| 9 | **R2-14: art. 73** | Narrower, on R6's correction | Reopened AI Act art. 113: applies from 2 Aug 2026; Omnibus recital (2026/1744) moves Chapter III ss. 1–3 to 2 Dec 2027 / 2 Aug 2028 | Art. 73 (Chapter IX) is in force but reaches only high-risk systems, and a refund agent is outside Annex III. The draft adds arts. 26(11), 50(1), 85, 86 (notice, complaint, explanation after the fact) |
| 10 | **R2-04 + R4 "second party": whose responsibility** | Upheld | Copilot terms, Anthropic D.3, application card (on R2, live pages 24 Oct) | The terms bind the account holder (the principal), not the person acted on. The second party's burden rests on *Moffatt* para 28 and on the documents' silence |
| 11 | **R2-08: chain of thought** | Upheld (narrower) | gpt-oss card; Microsoft Foundry tutorial (on R6) | Open-weight reasoning goes to the deployer. Claim restated: where reasoning is delivered, it goes to the deployer and is addressed to developers; it never reaches the person acted on |
| 12 | **R3-02: is a customer "dominated"?** | Contested; R6's correction taken | Reopened Gädeke 2020: "a structurally constituted form of power" (p. 199); "Purely interactional forms of power ... are not instances of domination" (p. 200) | **Default (author may reverse):** argue structural enablement (Gädeke's own test): terms of service, an operator-run channel, and no alternative route make the firm's power structural, not episodic. Name the Pettit–Gädeke dispute |
| 13 | **R3-05: Lazar's rival frame** | Upheld | Reopened Lazar Lecture I: "the republican ideal of non-domination to conflate an internally diverse suite of normative" (line 1195 of my text extraction; p. 20 n. 80 on R3); "Benevolent, procedurally legitimate ..." (p. 23); "unilaterally and intransparently" (p. 24) | **Default:** meet Lazar in §1 as a converging route. His legitimacy triad (ex ante limits, in-process constraint, ex post contestability) maps onto envelope, brake and record. His "who may govern" question becomes an objection in §4 (designer-adopted duties lack authority) |
| 14 | **R3-04/06: what route 2 can carry** | Upheld (narrower) | Celikates §2.1; Walzer p. 66 (on R6) | Non-domination does not "carry the old verdicts across centuries". The history classifies; the verdict today rests on route 1 (Microsoft's professed standards) and route 2 (non-domination or Lazar's legitimacy, applied now). Benchmark 1 (contemporaries objected) is evidence of recognition, not a method |
| 15 | **R3-08: Bartha licenses plausibility, not a verdict** | Upheld | Bartha SEP §2.3 (on R6) | A6 restated: the analogy establishes prima facie plausibility; each closest disanalogy is shown non-critical, not merely recorded |
| 16 | **R3-17 + R5: missing objections** | Upheld | Sparks and Jayaram via Hamilton p. 6; Scherer et al. 2023 p. 422; Fraser via von Samson p. 1308; Lazar; Arbel and Becher (abstract); Farrell et al. 2025 (on R6) | §4 adds: automation reduces domination (algorithms lack wills); paternalism; the authority objection; the LLM "smart reader" relieves the reading (answer: who runs the reader). Farrell et al. go in the opening survey |
| 17 | **R3 contribution claims** | Upheld | Ben-Shahar and Schneider; Frahm pp. 175, 200 (on R6) | The disclosure contribution narrows to *who runs the reading* (Ben-Shahar and Schneider already locate failure in the disclosee). The Frahm contribution attaches to skilling, not oversight |
| 18 | **R5 rank 1 / R5-12: grade cards** | Upheld | Reopened Ho et al. 2019 n. 1 "the same issues identified here affect that analysis" (Simon 2005); Felt et al. 2015 Table: 30.9% → 58.3% | D07's working precedent moves to Felt et al. 2015 (the SSL warning: design raised adherence). The grade card stays as a device, with the replication dispute and the independence condition (Ho 2012; Zhang 2022). `ADJUDICATION.md` A2 row gets the caveat |
| 19 | **R4 + R5: "each with a working precedent"** | Upheld | R5-07, R5-17; R4 D02/D08 | Precedents: D02 now GDPR art. 22(1) (a present precedent, partial); D03 AP2; D04 Easton 1757, Appeals Centre (with its limits); D06 teach-back at the bedside and *Jones v. Meehan* for carrying the risk (no live AI-law precedent: AI Liability Directive withdrawn); D07 Felt 2015; **D08 has none**, so it is stated as a proposal |
| 20 | **R4 HP3: who bears the duty** | Upheld | Draft lines (on R4/R6) | B2 names the deployer as the duty-bearer for D03, D04, D06, D07 and the provider for the reasoning record; Microsoft is both for its own agent products. Stated, not left to "whoever designs and runs" |
| 21 | **R4 HP4: a fifth question, who carries the loss** | Upheld | D06, the law | A1 gains a fifth question |
| 22 | **R5-04: thirteen million views** | Overruled | Reopened the capture header (12 Oct 2026): "13M views" | Keep; cite the capture |
| 23 | **R4 "scaffold"** | Narrower (R6) | Smith 2025 (Elevate) | The promise is Microsoft's Elevate pledge; Nadella's phrase is a metaphor, not a promise |
| 24 | **R5 gap search** | Accepted | 66-row log | "I found no work that ..." statements stand as R5 wrote them. Farrell et al. and Arbel and Becher are cited |

## Card work still to do (lead)

- Append S2 blocks to the 36 R-facet cards from AUDIT_R6 and set `verified`.
- Fix `gallot2026securing` (Riley: "can be held for verified human approval") and `sparks2022rule` (third reason, venue
  MPP 9(2) 201–218).
- Extend `eu2016gdpr` (arts. 13(2)(f), 15(1)(h), 22), `eu2024aiact` (arts. 26(11), 50(1), 85, 86, 113),
  `euomnibus2026` (operative dates) by upgrade cards, not edits to others' cards.
- Add the replication caveat to `simon2005impact` and to `../facets/ADJUDICATION.md` A2.

## Library list added by this round

Saenger p. 100; Blayney 2013 vol. 2 chs. 10–11; Clegg 1997; Pettit 1997/2012; Lovett 2010; Anderson 2017; Maas 2022
(gold OA behind a bot wall; open in a browser); Sparks and Jayaram 2022; Lazar's versions of record (P&PA 2025, OSPP
2024); Hussain and Moriarty 2018 (Bentley's own repository); Whelan 2012; Arbel and Becher 2022, 2025; Jin and
Leslie's reply to Ho et al. Full routes: the "Gaps and blocks" sections of R1–R5.
