# AUDIT_N7b: adversarial audit of the N1, N4 and N5 cards and claims, and a legacy sample

*Agent-drafted (N7b) on 2026-10-24. The author has not reviewed it, and none of the text is the author's. I wrote none
of the cards or facets audited here and changed none of them. This file is the only file I wrote in the repo.*

**Date:** 2026-10-24. **Auditor:** N7b, independent.

**Scope.** (1) All 61 cards with `facet: N1`, `N4` or `N5` in `literature/cards/berthon_ethics_paper/`. (2) Sections
(c) and (d) of `N1_llm_tool_custody_traces_approvals.md`, `N4_standards_incident_disclosure_skilling.md` and
`N5_beq_frame_method_republican.md` where they bear on A1, A4–A8, and the N1, N4 and N5 rows of "Round-1 findings" in
`../COVERAGE_PREMISES.md`. (3) The seven `anthropic_authored: true` cards. (4) The 26 web and documentation cards.
(5) Legacy sample, seed 20261024: `berthon_ethics_course/balkin2016information`, `berthon_ethics_course/claassen2024wealth`,
`berthon_ethics_course/microsoft2025ai`, `berthon_ethics_course/microsoft2025responsible`, `dxd_foundation/nadella2026models`
(the `berthon_ethics_course` copy of the last is byte-identical below its provenance comment).

**Checks run.**
1. sha256 of the file at every card's `local_path`, recomputed (61 of 61, plus the five legacy cards).
2. Exact-string check of every quotation in every card (833 quoted strings of 12 characters or more), normalised for
   whitespace, line-end hyphens, soft hyphens, ligatures, curly quotes and footnote markers, against the text at
   `local_path` and its sibling extractions. Every miss was then read by hand: most were cross-references to another
   card's source, phrases from the outline or the post, or PDF extraction artefacts (`well-\nfunded`, `tech-\nnology`,
   superscript note numbers). Real misses are listed in the tables.
3. Page locators for every quotation in the 26 PDF-based cards, by `pdftotext` page and each document's own
   printed-page offset; every outlier read by hand.
4. Crossref record for all 17 DOIs (title, container, volume, issue, pages, date, authors) and
   `https://api.crossref.org/works?filter=updates:<DOI>` for each: **no update, correction or retraction notice on any
   of the 17**, nor on the legacy Claassen DOI. arXiv API records for the six preprints and the Hamilton preprint. EU
   texts: OJ headers of the CELLAR copies. SB 53: the chaptered text. M365 Roadmap 570434: Microsoft's own release API
   (the card read it through a third-party mirror).
5. Fresh fetch on 2026-10-24 of all 26 web and documentation URLs (all HTTP 200), with every card quotation re-checked
   against the fresh copy. Copies and `SHA256SUMS.txt` in `~/iit-playground/berthon_ethics_local/pdfs/nadella/N7b/web/`.
6. Independent recount of Luchs's section shares from the PDF (`N7b/luchs/`).
7. Each premise-bearing quotation read against the claim hung on it in card, facet and `COVERAGE_PREMISES.md`.
8. All 61 cards parse with `cardlib.parse_card`; every `basis` is one of the four allowed values.

No email address was sent to any service; no Unpaywall, no Chrome tools, no git. One route needs the lead's ruling:
openai.com returned HTTP 403 to me as it did to N1, and I read OpenAI's Service Terms from the Internet Archive's
public snapshot of 6 Oct 2026 instead. If the lead counts an archive snapshot of a bot-walled page as circumvention, the
OpenAI row below drops to COULD NOT CHECK.

**Result in one line.** Every file exists and every sha256 matches. The quotations are almost all exact, but four
premise-level claims outrun the text: "no vendor shows anyone raw chain of thought" is contradicted on the very page
the Anthropic card read; AP2 does not "bind both sides" and shares only part of the envelope with the counterparty;
EU harmonised standards do not "bind" implementers (the Court says compliance is not compulsory); and "all four
vendors" rested on three cards. Five cards carry a wrong statement (one misquotation, one wrong locator, three wrong
descriptions of the source).

Status key: VERIFIED verbatim / VERIFIED paraphrase / WRONG / OVERSTATED / NEEDS LIBRARY CHECK / COULD NOT CHECK.

---

## Table N1: cards and claims

Existence for N1 web and documentation cards is the vendor's own page (fresh fetch, see the web table); for preprints,
the arXiv API. "Quotes" means every quotation on the card was found in the saved copy at the locator given.

| Facet/card and line | Claim or quotation as written | Source and locator | Status | What I found | Fix |
|---|---|---|---|---|---|
| `anthropic2025commercial` | Customer "must notify its Users"; disclaimer of warranties | Anthropic Commercial Terms, §§ D, L.2 | VERIFIED verbatim | sha256 matches; 3 own quotations exact. Two other quoted strings are the Code of Conduct (`microsoft2026microsoft`) and P3 of the post; both exact in those sources. | None |
| `anthropic2025consumer` | User "responsible for all Inputs ... and all Actions"; "You should not rely on any Outputs or Actions without independently confirming their accuracy" | Anthropic Consumer Terms §4 | VERIFIED verbatim | Exact, in §4 as cited. | None |
| `anthropic2026configure` | "in auto mode a classifier reviews actions instead of you"; managed settings "can't override" | Claude Code permissions doc | VERIFIED verbatim | Exact; fresh copy byte-identical. | None |
| `anthropic2026measuring` | auto-approve ~20% to over 40% by 750 sessions; 87% vs 67% human involvement | Anthropic research post | VERIFIED verbatim | All 13 quotations exact; fresh copy byte-identical. | None |
| `anthropic2026thinking` l. 25, l. 46 | "No display setting returns the raw chain of thought"; use: Anthropic "withholds the raw chain of thought from deployers" | Anthropic docs, *Thinking*, "Summarized thinking" | OVERSTATED | The quotation is exact. But the same section, which `pages_read` says was read, ends: "In rare cases where you need access to full thinking output, contact Anthropic sales." (also in my fresh copy). The card omits it, and its use turns "no API setting" into "withheld". | Add the sales sentence to Key facts; restate the use as "no API setting returns it; full thinking output is available to some customers by arrangement with Anthropic sales" |
| `anthropic2026usage` | "qualified person"; affected individual "must be clearly told that AI was used" | Anthropic Usage Policy, high-risk section | VERIFIED verbatim | Exact. | See Anthropic table (corroboration name) |
| `elmergawi2026introducing` | ACS answers "who defines those boundaries": "a security or compliance team" | commandline.microsoft.com post | VERIFIED paraphrase | "who defines those boundaries" is posed as a question; the answer is "There is no standard mechanism by which a security or compliance team can define, enforce, and audit policy across agents" and later "a security team gets one place to author, version, and audit controls". Fair reading of the post's aim. "sit outside the model" is the post's P11, not the blog. | None |
| `felt2012android` | "17% of participants paid attention to permissions" | Felt et al. 2012, p. 5 | VERIFIED verbatim | Crossref: SOUPS '12, pp. 1-14. Exact at p. 5. | None |
| `feng2025regulatory` | "User-specified rules override any 'self-approval' settings" (p. 3) | arXiv 2512.00742v1, p. 3 | VERIFIED verbatim | arXiv record matches; all locators match. | None |
| `google2026agentic` l. 35, l. 49 | Constraints "allow the verifier to verify that the Checkout and Payment match the User's intent"; use: envelope "approved by the user and checked by the counterparty" | AP2 spec v0.2, "Modes" | OVERSTATED | Quotations exact. The card stops one sentence short. The paragraph continues: "Only constraints relevant to the closed Mandates are shared with the verifier." The counterparty sees part of the envelope, not the envelope. The spec (v0.2) also has no "Intent Mandate"; it speaks of "open" Checkout and Payment Mandates. | Add the "Only constraints relevant" sentence; say the verifier checks the closed mandate against the constraints relevant to it |
| `google2026gemini` | developer "solely responsible for the actions and tasks performed by the service" | Gemini API Additional Terms, "Agentic Services" | VERIFIED verbatim | Exact. The "you" is the API developer, not the end user. | None |
| `microsoft2025multistage` | AI stage may approve and end a flow "as approved" | Copilot Studio multistage approvals doc | VERIFIED verbatim | Exact. | None |
| `microsoft2026audit` | Purview records resource access type, policy block, no prompt text | Purview "Audit logs for Copilot" | VERIFIED verbatim | Exact. | None |
| `microsoft2026connect` | `require_approval="always"`; "In production, implement your own approval UX and policy." | Foundry MCP doc | VERIFIED verbatim | Exact. | None |
| `microsoft2026copilot` | "you are solely responsible for those Actions and any results or consequences"; Merchant's terms | Copilot consumer terms | VERIFIED verbatim | Exact; fresh copy byte-identical. "YOU BEAR THE ENTIRE RISK" is in the Services Agreement file the card names; "always review and verify" is E14's application card, cited as such. | None |
| `microsoft2026enabling` | Roadmap 570434, "In development", GA "September CY2026" | Read via mc.merill.net | VERIFIED verbatim | Microsoft's own API (`microsoft.com/releasecommunications/api/v1/m365/570434`) returns the same title, description, status and date. | Cite the official roadmap record, not the mirror |
| `microsoft2026microsoft` | oversight "so customers can find and mitigate undesirable behaviors"; disclosure that "decisions, or actions are generated by AI" | Enterprise AI Services Code of Conduct | VERIFIED verbatim | Exact. | None |
| `microsoft2026overview` | registry and policy shown to admins and "leaders" | Agent 365 overview | VERIFIED verbatim | Exact. | None |
| `microsoft2026responsible` | Copilot file access "without those access points being recorded in Unified Audit Logs" (PDF p. 19); Cowork "attribution indicating AI assistance" (PDF p. 18) | 2026 RAI Transparency Report | VERIFIED verbatim | Exact at the PDF pages given. The card also records that Microsoft's "enhanced logging" captured the activity. | None (see C6 row) |
| `microsoft2026tracing` | tracing off by default; read through Azure monitoring roles | Foundry trace-data doc | VERIFIED verbatim | Exact. | None |
| `microsoft2026use` | "Approve All"; "Always review the details before you approve." | Cowork user guide | VERIFIED verbatim | Exact. | None |
| `openai2026agent` | Auto-review "instead of surfacing to the user"; managed requirements "take precedence" | Codex security doc | VERIFIED verbatim | Exact; fresh copy byte-identical. | None |
| `openai2026reasoning` | "we don't expose the raw reasoning tokens"; summaries may need "organization verification" | OpenAI reasoning guide | VERIFIED verbatim | Exact. `source_url` (developers.openai.com) and `SOURCE_URL.txt` (platform.openai.com) differ; the fresh fetch of the card's URL is byte-identical to the saved file, so it is the same page. | Make `SOURCE_URL.txt` and `source_url` agree |
| `palod2026evaluating` l. 27-28 | Summary: "Raw traces and pro-answer explanations raised acceptance of both correct and incorrect answers" | Palod et al., Table 3, p. 6 | WRONG | Table 3: misjudgment 54.0 (trace) against 54.2 (answer only). The trace raised acceptance of correct answers only. The card's own Critical notes say so; the Summary contradicts them. Table 3 figures otherwise exact. | "Pro-answer explanations raised acceptance of both correct and incorrect answers; raw traces raised acceptance of correct answers (75.0 vs 60.4) but not of incorrect ones (54.0 vs 54.2)" |
| `parikh2025powering` l. 27 | Intent Mandate "specifies the rules of engagement—price limits, timing, and other conditions"; "The merchant and payment providers verify purchases against it" | Google Cloud blog, 16 Sep 2025 | VERIFIED paraphrase | Quotations exact. The blog does not itself say that merchants verify against the Intent Mandate; it says the mandate is "verifiable, pre-authorized proof" that lets the agent generate a Cart Mandate. Verification by counterparties is the spec's (`google2026agentic`), and there only for "constraints relevant to the closed Mandates". | Attribute the verification sentence to the spec, with its limit |
| `park2025critical` | errors caught "at moderate-to-high rates", omissions "only 40% of the time" (p. 2) | arXiv 2511.12001v3 | VERIFIED verbatim | Text extracts as "moderate-tohigh" (line-break artefact); wording otherwise exact. | None |
| `shavit2023practices` l. 57 | "the user, not 'an authorized person' in the deployer, is the brake-holder ... in this OpenAI scheme (p. 14)" | Shavit et al. 2023, §4.7, pp. 14-15 | OVERSTATED | p. 14 is exact: deployers ensure "a user can always activate a graceful shutdown". But p. 15 adds "redundancy in the number of human parties that can turn off an AI agent instance. The two relevant parties are the system deployer and the data center operator or chip owner", and raises "in what circumstances an external party has the right or obligation to terminate a user's agent". The card is `full-text` and omits p. 15. | "The user holds the first brake (p. 14); deployer and data-centre operator hold redundant ones, and the paper leaves open a third party's right to terminate (p. 15)" |
| `zhang2026hansel` | 32.1% wrong answers accepted; 60.7% vs 67.9% | arXiv 2606.18671v1, p. 9 | VERIFIED verbatim | Exact (Greek and italic symbols aside). | None |
| `zhao2026agentgui` | 90 s vs 145 s; 93% vs 80% | arXiv 2607.26300v2, p. 4 | VERIFIED verbatim | Exact. | None |
| N1 (c) C1, l. 326-341; COVERAGE A5 | Microsoft's agent controls answer to the deploying organisation; A5 "holds for Microsoft" | `elmergawi2026introducing`, `microsoft2026overview`, `-microsoft`, `-tracing`, `-audit`, `-connect` | VERIFIED paraphrase | Every layer read names admins, leaders, owners or "a security or compliance team". The Code of Conduct gives the people acted on disclosure only. A5's sinker (envelope declared to, or binding for, the people acted on) is not met by any Microsoft card. | None |
| N1 (c) C2, l. 345-349; (d) row 3; COVERAGE A5 | A5 "refuted as a general claim by Google's AP2 Intent Mandate, which binds both sides"; "either side can produce" the audit trail | `parikh2025powering`, `google2026agentic` | OVERSTATED | (i) "binds both sides" is in no source; the user-signed open mandate constrains the agent's key, and merchants verify. (ii) "Only constraints relevant to the closed Mandates are shared with the verifier." (iii) "Intent Mandate" is the 2025 blog's term; spec v0.2 has none. (iv) "either side can produce" is right: the Checkout Mandate may come from the agent or the merchant. (v) A5 as written is about P11–P12, so AP2 refutes a general form (B3 territory), not A5 itself; the counterparty in AP2 is a merchant with commercial standing, as the facet's own C2 says. | "AP2 is a counter-instance to a general form of A5: a user-signed envelope, part of which counterparties verify, in a domain with existing liability rules" |
| N1 (c) C3, l. 361-368; COVERAGE A4 | "All four vendors put responsibility for actions on the user" | `microsoft2026copilot`, `anthropic2025consumer`, `google2026gemini`; OpenAI not read (403) | OVERSTATED | As carded, three of four, and Google's "you" is the API developer. N1's own C3 says the OpenAI terms "could not be read". My read: OpenAI Service Terms, "Updated: September 29, 2026", §14(a): "You are responsible for actions they take and content they share on your behalf." (Internet Archive snapshot 20261006184704; local `N7b/oai_terms/service_terms.html`, sha256 `567755d2…`). So the claim holds, but no card carries it. | Card OpenAI Service Terms §14 (subject to the route ruling above); write "users or developers" |
| N1 (c) C4, l. 372-376; (d) row 5; COVERAGE A4 | "No supplier read gives anyone outside it the raw chain of thought"; "no vendor shows anyone the raw chain of thought" | `openai2026reasoning`, `anthropic2026thinking`, `microsoft2026use`; Gemini thinking page (uncarded) | WRONG | Anthropic's page offers full thinking output through sales ("In rare cases where you need access to full thinking output, contact Anthropic sales"). OpenAI ("we don't expose the raw reasoning tokens") and Google ("only the summary being output from the API") hold. The facet already exempts open-weight models. | "No supplier returns the raw chain of thought through its API settings; Anthropic offers full thinking output to some customers by arrangement" |
| N1 (c) C4, l. 377-379 | Palod: misjudgment 54.0% and 51.0% against 54.2% | Palod Table 3, p. 6 | VERIFIED verbatim | Exact. | None |
| N1 (c) C5, l. 383-388; COVERAGE A4 | Approval gates thinned or handed to models; auto-approve doubling; Felt one in six | `microsoft2025multistage`, `openai2026agent`, `anthropic2026configure`, `anthropic2026measuring`, `felt2012android` | VERIFIED paraphrase | All quotations exact. Note for balance: `anthropic2026measuring` also reports interrupts rising from 5% to about 9% with experience. | Mention the interrupt rise beside the auto-approve rise |
| N1 (c) C5, l. 388-391; (d) last row | "in OpenAI's scheme the user holds the shutdown and the ledger"; "the people acted on are not given a brake anywhere I read" | `shavit2023practices`, pp. 14-15 | OVERSTATED | See the card row: p. 15 gives redundant shutdown to deployer and data-centre operator and raises an external party's right to terminate. | As in the card row |
| N1 (c) C6, l. 395-397; claim 5, l. 426 | "the 'tamper-proof' record failed in Microsoft's own product"; "P15's record as complete" contradicted | `microsoft2026responsible`, PDF p. 19 | OVERSTATED | The customer-facing Unified Audit Log missed the access. The same paragraph: "the activity was captured in our enhanced logging and data platform", which let Microsoft analyse "over 90 million security logs". The record was incomplete for the customer and complete for Microsoft; that supports M4(a) (a record kept by one side) more than an absent record. The report never calls the UAL "tamper-proof"; that is P15's word. | "The customer's audit log missed Copilot file access; Microsoft's internal logs did not" |
| N1 (c) C6, l. 397-400; COVERAGE A4, M4(b) | Enterprise traces mark commitments for enterprise readers | `microsoft2026audit`, `microsoft2026tracing`, `elmergawi2026introducing` | VERIFIED paraphrase | Purview types each resource action and policy block; Foundry traces record tool calls; ACS interception points sit at tool-call boundaries. | None |
| N1 (c) C6, l. 400-404 | HANSEL 32.1% and 60.7%; Kutasov AUC 0.65, over an hour per transcript | `zhang2026hansel` p. 9; `kutasov2025shade` (dxd) | VERIFIED verbatim | Exact; Kutasov's text gives an average of 103 minutes and AUC 0.65. | None |
| N1 (c) C7, l. 406-413 | No Microsoft evaluation of T1.3 or A5.4 in the 2026 report | `microsoft2026responsible` | VERIFIED paraphrase | My term search of the whole report ("interpret", "realistic", "user research", "comprehension") finds only the items the facet names. An absence, as the facet says. | None |

## Table N4: cards and claims

| Facet/card and line | Claim or quotation as written | Source and locator | Status | What I found | Fix |
|---|---|---|---|---|---|
| `california2025transparency` | 22757.13(a), (c), (d), (f), (g); 22757.15(b) "only by the Attorney General" | SB 53, Stats. 2025 ch. 138 | VERIFIED verbatim | Exact in the chaptered text. | None |
| `chiang2022exploring` | "none of our ML literacy interventions could impact the low-performing subjects' reliance" (p. 159) | IUI '22, pp. 148-161 | VERIFIED verbatim | Crossref matches; PDF p. 12 = p. 159. | None |
| `cjeu2024publicresource` | paras 70, 74-76 | C-588/21 P, Grand Chamber, 5 March 2024 | VERIFIED verbatim | Exact at the paragraphs given. Two strings on the card belong to the Commission reply and Gornet and Maxwell, cited as such. | None (see binding row) |
| `connellpensky2026can` | abstract only; paraphrase | Computers & Education 250, 105640 | VERIFIED paraphrase | Crossref matches (Sept 2026). Basis honestly `abstract`; no quotation. | None |
| `corporateeurope2025bias` | 143 people; 54 + 24 = 78 (55 per cent); 13 civil society (9 per cent); "At least three national delegations are regularly headed by officers working for Microsoft"; 42001 "edited in SC42 by Microsoft's" representative | CEO report, Jan 2025 | VERIFIED verbatim | Exact. No access date on the card. | Add "Accessed 2026-10-24" |
| `eu2012standardisation` | Art 2(1) "with which compliance is not compulsory" | Reg 1025/2012, OJ L 316/12 | VERIFIED verbatim | Exact. | None |
| `eu2016gdpr` | Arts 34, 77-80, 82 | Reg 2016/679, OJ L 119/1 | VERIFIED verbatim | Exact. | None |
| `eu2022nis2` | Art 23(1) "Where appropriate"; "The mere act of notification shall not subject the notifying entity to increased liability" | Dir 2022/2555, OJ L 333/80 | VERIFIED verbatim | Exact. | None |
| `eu2024aiact` | Art 73 in full; Arts 85, 86; Art 99(4) | Reg 2024/1689, OJ L 12.7.2024 | VERIFIED verbatim | Exact. | None |
| `eu2024productliability` | Art 2(1): products placed on the market "after 9 December 2026" | Dir 2024/2853, OJ L 18.11.2024 | VERIFIED verbatim | Exact. | None |
| `euomnibus2026` l. 32 | new Art 75(1a): "By derogation from Article 73, providers of high-risk AI systems ..." | Reg 2026/1744, Art 1(31)(c) | WRONG | The OJ text reads "By way of derogation from Article 73". Rest of the quotation exact. | Insert "way of" |
| `europeancommission2025reply` | no affiliation data (p. 13); COI rules "would prevent industry stakeholders" (p. 16); "aware and concerned by the delay" (p. 9) | Commission reply to the Ombudsman, 2025/1974/MIK | VERIFIED verbatim | Exact at the PDF pages given. | None |
| `frontiermodelforum2026information` | "industry → authority"; FMF "funded by fees from its member firms" | FMF issue brief; FMF About page | VERIFIED verbatim | Brief quotations exact at `local_path`. Four quotations come from the About page, saved in `N4/fmf/about.txt`, which the card names nowhere and gives no sha256 for. No access date. | Name the About page's file and sha256; add access date |
| `gornet2024european` | "quasi obligatory" (p. 11); "Those impacted by the use of AI have no role to play" (p. 16) | Internet Policy Review 13(3) | VERIFIED verbatim | Crossref matches; printed = PDF − 1. The p. 16 sentence ends "(Edwards, 2022)": Gornet and Maxwell are reporting Edwards. | Keep the Edwards attribution when quoting |
| `laux2024three` | "Standardisation as a governance tool has been widely criticized as lacking legitimacy" (§1) | CLSR 53, 105957 | VERIFIED verbatim | Crossref matches; PMC copy. | None |
| `nist2024artificial` | "Formal channels do not currently exist" (p. 52); AI RMF "is intended for voluntary use" (p. 1) | NIST AI 600-1 | VERIFIED verbatim | Exact; printed = PDF − 4. | None |
| `puppart2025brief` | n = 36; over-reliance 52.1%; increased under-reliance | arXiv 2503.10556v2 | VERIFIED verbatim | arXiv record matches; text exact. | None |
| `tabassi2023artificial` | "intended to be voluntary, rights-preserving" (p. 2) | NIST AI 100-1 | VERIFIED verbatim | Exact. | None |
| `veale2021demystifying` | harmonised standards "are not as voluntary as the Commission argues" (p. 105); no right to complain to an MSA (p. 111) | CRi 22(4), 97-112 | VERIFIED verbatim | Crossref matches; the arXiv PDF carries CRi pagination (first page 97). | None |
| N4 (c) Q1, l. 114; (d) row 1 | 55 per cent corporate and consultancy, 9 per cent civil society of 143; Commission concedes no affiliation data, industry "central" | `corporateeurope2025bias`, `europeancommission2025reply` | VERIFIED verbatim | Exact. | None |
| N4 (c) Q1, l. 116; claim 1, l. 123; COVERAGE A4, M2 | EU harmonised standards "bind once cited" in the OJ (paras 70, 75) | C-588/21 P paras 70-76 | OVERSTATED | Para 70: a cited standard "forms part of EU law owing to its legal effects". Para 75: other routes "may prove difficult, or even impossible". But para 74: "compliance with harmonised standards is not compulsory"; the effect is a presumption of conformity. Para 71 (standards "may be binding on the public generally" once published) is the strongest line and is not cited. The facet's (d) wording, "binding in practice through the presumption", is right; COVERAGE's "bind" is not. The case concerned access to Directive-based toy standards. | "Once cited, a harmonised standard forms part of EU law (para 70) and is in practice hard to avoid (para 75), though compliance is not compulsory (para 74)" |
| N4 (c) Q1, l. 116; claim 1 | "It holds for ISO/IEC 42001, NIST and the FMF" | `tabassi2023artificial`, `nist2024artificial`; ISO 42001 not read | NEEDS LIBRARY CHECK | Holds for NIST on the text. ISO/IEC 42001 was not opened (iso.org challenge, paid). | ISO Online Browsing Platform, clauses 1-3 |
| N4 (c) Q2, l. 118; (d) row 5 | Art 73 reports go to market surveillance authorities; Omnibus reroutes some to the AI Office | AI Act Art 73(1)-(11); Omnibus Art 75(1a) | VERIFIED verbatim | Every paragraph of Art 73 runs provider to authority or authority to authority. Not checked: what the Art 73(8) measures under Art 19 of Reg 2019/1020 may include. | None |
| COVERAGE A4, M9, O02 | "'Notice without standing' holds for AI Act art. 73 and SB 53 only; GDPR art. 34 and the Product Liability Directive give remedies" | `eu2024aiact`, `california2025transparency`, `eu2022nis2`, `eu2016gdpr` | OVERSTATED | "Only" fails: NIS2 Art 23 is also notice without standing (self-help measures; notification adds no liability). GDPR's remedies are Arts 79 and 82; Art 34 is the notice. SB 53 lets "a member of the public" report to OES (22757.13(a)), a channel and not standing. The facet's own (c) Q2 is accurate; the COVERAGE summary compresses it wrongly. | "Holds for AI Act Art 73, SB 53 and NIS2 Art 23; GDPR pairs notice (Art 34) with remedies (Arts 79, 82); the PLD gives a remedy without notice" |
| N4 claim 6, l. 128 | Art 73 not in the Art 99(4) list; route via Arts 16 and 17(1)(i) | AI Act Art 99(4) | VERIFIED verbatim | Art 99(4)(a)-(g) lists Arts 16, 22, 23, 24, 26, 31, 33, 34, 50; not 73. | None |
| N4 (c) Q2 | PLD claim for AI software causing death, injury or data loss, from December 2026 | Dir 2024/2853 Art 2(1), recital 20 | VERIFIED paraphrase | Applies to products placed on the market after 9 Dec 2026. | None |
| N4 (c) Q3, l. 120 | Chiang and Yin helped only the competent (p. 159); Puppart and Aru shifted error (n = 36); Connell Pensky on an abstract reading | `chiang2022exploring`, `puppart2025brief`, `connellpensky2026can` | VERIFIED paraphrase | As cards. | None |
| N4 (c) Q3; (d) M11 row | "I found no Microsoft outcome evaluation and no independent one" | one web search; no card | COULD NOT CHECK | An absence after one search; the facet's (d) already says "UNSUPPORTED as 'no evaluation exists'". | Keep it as "none found in [sources]" |

## Table N5: cards and claims

| Facet/card and line | Claim or quotation as written | Source and locator | Status | What I found | Fix |
|---|---|---|---|---|---|
| `bartha2019analogy` | "Prior Association" (§3.5.2); "It pre-supposes a common set of social values" (§4.4) | SEP, rev. 25 Jan 2019 | VERIFIED verbatim | Exact, in the sections given. No access date. | Add access date |
| `celikates2023critical` | internal critique: standards "already recognized by those criticized" (§2.1) | SEP, 12 Dec 2023 | VERIFIED verbatim | Exact in §2.1. No access date. | Add access date |
| `diamantis2025danger` | "more sophisticated, well-funded, repeat player" (abstract); concessions pp. 7, 8, 19 | BEQ, online 27 Oct 2025, pp. 1-21 | VERIFIED verbatim | Crossref matches; all 11 located quotations at PDF page = printed page. | None |
| `hamilton2025digital` | "whatever kinds of domination develop" (p. 5) | arXiv 2510.00312v1 | VERIFIED verbatim | Exact at preprint p. 5. Crossref title of the published chapter is "Digital Domination"; the card says the published pagination was not seen. | None |
| `ketokivi2017reasoning` | Gentner's "system of relations" | AMR 42(4), 637-658 | VERIFIED verbatim | Crossref matches. Card renders inner double quotes as single. | None |
| `kingston2026social` l. 27 | "ceding power to third parties in formalized and accountable ways" (abstract, p. 1) | BEQ, online 14 Jan 2026, pp. 1-28 | WRONG | That exact phrase is on p. 22. The abstract (p. 1) reads "requires big buyers to collectively cede power to third parties in supply chains in formalized and accountable ways". Other locators exact (pp. 17, 19, 20). | Locator "p. 22", or quote the abstract's own words |
| `kugelberg2026practice` | first move rebuts a weak objection to their opponent (p. 6); "A powerful objection to practice-dependent theorising" (p. 10) | JBE, online 22 Jun 2026 | VERIFIED verbatim | Crossref matches; PDF page = page. | None |
| `lovett2026republicanism` | "the accidental prejudices of their day" (§4) | SEP, rev. 12 Aug 2026 | VERIFIED verbatim | Exact in §4. No access date. | Add access date |
| `luchs2026taking` l. 35 | "Introduction (untitled opening, pp. 1-3)" | ICS, online 28 Sep 2026 | WRONG | The article has an "Introduction" heading, printed p. 1 (PDF p. 2), above Fei-Fei Li's keynote. | "Introduction (pp. 1-3)" |
| `seele2022greenwashing` | map, then "where the analogy does not fit" (p. 1064); "fluid algorithms" (p. 1070) | JBE 178(4), 1063-1089 | VERIFIED verbatim | Crossref matches; printed = PDF + 1062. | None |
| `sharon2024regulating` | prose subsections, no grid | ICS 27(15), 2651-2668 | VERIFIED verbatim | Crossref matches; the PDF has no table or figure. | None |
| `vonsamson2025immanent` l. 31 | "The HU Berlin copy is the submitted version deposited by the author" | EJP 33(4), 1308-1325 | WRONG | The PDF carries Wiley's typeset pages, licence and footer; HU edoc's record gives `dc.type.version` "publishedVersion". Quotations and pages (printed = PDF + 1307) are right. The Fraser abstract quotation (l. 51) is exact against OpenAlex, but no copy of it sits at `local_path`. | "the published version (CC BY), deposited at HU edoc"; mark the Fraser line "OpenAlex abstract" |
| `walzer1988interpretation` | "it isn't universally known, not the law and not the morality behind the law" (p. 69); "a new relevance" (p. 70) | Tanner Lectures VIII | VERIFIED verbatim | Exact; PDF page = printed page (folio 69 checked). | None |
| N5 (c) Q1, l. 219-220; claim 1; COVERAGE Outline | Luchs's shares 17.6 / 41.9 / 30.3 / 10.3; body 6,591 | Luchs PDF, sections | VERIFIED paraphrase | My recount (running heads, contact and licence block, figure captions, headings, notes and references excluded): introduction 1,137; genealogy 2,684 (1,047 / 871 / 766); present case 1,960; conclusion 665; body 6,446. Shares 17.6 / 41.6 / 30.4 / 10.3. Shares agree within 0.3 points; the total differs by 145 words (2.2%), a tokenising difference. "About 6,600" is fair; "about 6,500" is closer. Abstract 249, notes 242. | Report "body about 6,450-6,600 words" |
| N5 (c) Q1, l. 221-222 | Luchs's "two slips": ChatGPT "2018" (p. 13); software crisis 1968 vs "1970s" | Luchs pp. 6, 13, 14 | OVERSTATED | ChatGPT 2018 is a real slip (p. 13). The second is not an inconsistency: a crisis "officially declared in 1968" can continue "in the 1970s". | Drop the second slip |
| N5 (c) Q1, l. 222-226; claims 2-4 | Diamantis concedes at pp. 7, 8, 19; Kugelberg's first move defends the opponent (p. 6); Sharon and Gellert have no grid | cards | VERIFIED paraphrase | As cards. | None |
| N5 (c) Q2, l. 227-234; COVERAGE A6 | A6 holds only in Bartha's stricter form | `bartha2019analogy` §3.5.2, §4.4 | VERIFIED paraphrase | Prior association and "no critical disanalogy" are exact. Bartha states them as plausibility conditions for analogical arguments; carrying a verdict across is the facet's extension through the §4.4 precedent paragraph. | Say so when citing Bartha |
| N5 (c) Q3, l. 235-246; claim 6; COVERAGE A7 | Internal critique alone does not bind a present actor; it needs the actor's own professions or non-domination | Walzer p. 69; SEP §2.1; von Samson p. 1318; Fraser abstract | VERIFIED paraphrase | Walzer p. 69 and the SEP definition carry the limit. Von Samson defends immanent critique as "methodology, not metaethics" and puts authority on independent grounds ("We might have made a promise", p. 1318); the facet uses her fairly. Fraser is abstract only. | None |
| N5 (c) Q3, l. 243-246; COVERAGE A7 | Non-domination carried across eras (Lovett §4; Hamilton p. 5) | `lovett2026republicanism`, `hamilton2025digital` | VERIFIED verbatim | Exact. | None |
| N5 claim 7; COVERAGE A7 | Conflicts with ledger N04 "describe, not condemn" | `consolidation/CONCEPT_LEDGER.md` l. 90 | VERIFIED verbatim | N04 reads "used to describe positions, not to condemn them". | None |
| N5 (c) Q4, l. 254; COVERAGE Outline | BEQ cap 12,000 words including footnotes | BEQ "Preparing your materials", saved `prep_www.html` | VERIFIED verbatim | "may not exceed 12,000 words (including the body of the text and the footnotes, but not including the abstract, tables, figures, or references)". It is a limit on the initial submission. | None |
| N5 (c) Q4, l. 255; COVERAGE Outline | "The section the outline calls 'Introduction' must carry no heading" | same | VERIFIED paraphrase | Text: "Avoid using the first level heading INTRODUCTION to start the paper." "Avoid" is guidance, not "must"; it bars that heading, not every heading. | "BEQ asks authors to avoid the heading INTRODUCTION" |
| COVERAGE Outline | Abstract ≤ 150 words | same | VERIFIED verbatim | "An abstract of not more than 150 words." | None |
| N5 (c) Q4, l. 256-257 | not "largely descriptive" case studies; AI use declared | BEQ pages | VERIFIED verbatim | "Case studies that are largely descriptive"; "you should always declare and describe your use of an AI tool if you have used it to generate text". | None |
| N5 (d) l. 284; COVERAGE v1 A1 row | A1 carried by `hamilton2025digital`, `lovett2026republicanism`, `luchs2026taking` | those cards | OVERSTATED | None of the three states A1's four design questions; Lovett and Hamilton support only "who may contest". N5 (d) says so ("no source states it"); the COVERAGE matrix lists them as A1 cards without that caveat. | Mark A1 in COVERAGE as "author's ruling; partial support for the fourth question only" |

## Anthropic-authored cards (scope 3)

| Card | Flag line and corroboration as written | Corroborating card | Status | What I found | Fix |
|---|---|---|---|---|---|
| `anthropic2025commercial` | "Anthropic-authored; corroborate." First line. Corroborated by the Code of Conduct's structure | `microsoft2026microsoft` | VERIFIED verbatim | Flag line first; the Code of Conduct puts oversight and disclosure on customers. | None |
| `anthropic2025consumer` | First line present. Corroborated by Copilot and Gemini terms | `microsoft2026copilot`, `google2026gemini` | VERIFIED verbatim | Both corroborate: each assigns agent actions to the user or developer. | None |
| `anthropic2026configure` | First line present. Corroborated by managed requirements "take precedence" | `openai2026agent` | VERIFIED verbatim | Exact in the OpenAI doc. | None |
| `anthropic2026measuring` | First line present. Corroborated by `yu2026habituation` and `felt2012android` | `yu2026habituation` (dxd), `felt2012android` | VERIFIED paraphrase | Felt corroborates inattention to permission screens, not AI-action approvals; Yu exists in CARD_INDEX (not reopened by me). Partial corroboration. | Say "partly corroborated" |
| `anthropic2026thinking` | First line present, with the note that the drafting model is an Anthropic model. Corroborated by OpenAI's guide and Palod p. 2 | `openai2026reasoning`, `palod2026evaluating` | VERIFIED verbatim | Both corroborate summaries-not-raw for OpenAI and, per Palod, for Anthropic and Google. Neither corroborates the omitted sales route, which cuts the other way. | See the card row |
| `anthropic2026usage` | First line present. Corroboration "microsoft2026microsoft ...; EU AI Act art. 50 and 26(11) (facet V1)" | `microsoft2026microsoft`; AI Act | VERIFIED verbatim | The Code of Conduct corroborates. "EU AI Act art. 50 and 26(11) (facet V1)" names no card. | Name `eu2024aiact` |
| `frontiermodelforum2026information` | Flag first; "no non-Anthropic corroboration found" for membership; authority-only reporting corroborated in law | `eu2024aiact` Art 73, `california2025transparency` 22757.13 | VERIFIED verbatim | Both corroborate the authority-bound direction. The flag is warranted (Anthropic is a member firm). | None |

## Web and documentation cards (scope 4)

All 26 URLs returned HTTP 200 on 2026-10-24. In every case each card quotation present in the saved copy is also
present in the fresh copy; nothing quoted has changed since capture. "Byte-identical" means the fresh file's sha256
equals the card's; "changed bytes" means page furniture differs but every quoted string survives.

| Card | URL resolves; access date | Saved vs fresh | Status | What I found | Fix |
|---|---|---|---|---|---|
| `anthropic2025commercial` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 3/3 quotations in fresh copy | None |
| `anthropic2025consumer` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 7/7 | None |
| `anthropic2026configure` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 10/10 | None |
| `anthropic2026measuring` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 13/13 | None |
| `anthropic2026thinking` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 10/10; the sales sentence is in both copies | None |
| `anthropic2026usage` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 11/11 | None |
| `bartha2019analogy` | yes; **not recorded** | byte-identical | VERIFIED verbatim | 13/13 | Add access date |
| `celikates2023critical` | yes; **not recorded** | byte-identical | VERIFIED verbatim | 9/9 | Add access date |
| `corporateeurope2025bias` | yes; **not recorded** | changed bytes | VERIFIED verbatim | 17/17 | Add access date |
| `elmergawi2026introducing` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 13/13 own (one string is P11 of the post) | None |
| `frontiermodelforum2026information` | yes; **not recorded** | changed bytes | VERIFIED verbatim | 17/17 from the brief; 4 from the About page | Add access date; name the About file |
| `google2026agentic` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 10/10. `main` branch: the spec can change without notice | Record the commit hash |
| `google2026gemini` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 8/8 | None |
| `lovett2026republicanism` | yes; **not recorded** | byte-identical | VERIFIED verbatim | 9/9 | Add access date |
| `microsoft2025multistage` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 13/13; feature in preview | None |
| `microsoft2026audit` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 11/11 | None |
| `microsoft2026connect` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 9/9 | None |
| `microsoft2026copilot` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 13/13 | None |
| `microsoft2026enabling` | yes (mirror); 2026-10-24 | changed bytes | VERIFIED verbatim | 6/6; official API agrees | Cite official record |
| `microsoft2026microsoft` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 9/9 | None |
| `microsoft2026overview` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 11/11 | None |
| `microsoft2026tracing` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 14/14 | None |
| `microsoft2026use` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 15/15 | None |
| `openai2026agent` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 13/13 | None |
| `openai2026reasoning` | yes; 2026-10-24 | byte-identical | VERIFIED verbatim | 10/10 | Align `SOURCE_URL.txt` |
| `parikh2025powering` | yes; 2026-10-24 | changed bytes | VERIFIED verbatim | 10/10 | None |

## Legacy sample (seed 20261024)

| Card | Prior status | Source and locator | Status | What I found | Fix |
|---|---|---|---|---|---|
| `berthon_ethics_course/balkin2016information` | true | UC Davis L. Rev. 49(4), 1183-1234 | VERIFIED verbatim | sha256 of `balkin_yale.txt` matches. All 16 quotations exact; each at the page cited (printed = PDF + 1182 in `balkin_yale.pdf`). No Crossref record (law review, no DOI). | None. **Agree** |
| `berthon_ethics_course/claassen2024wealth` | true | CRISPP 27(3), 317-338, doi 10.1080/13698230.2022.2113224 | VERIFIED verbatim | sha256 matches; 20/20 quotations exact; Crossref: online 18 Aug 2022, print 15 Apr 2024, 27(3) 317-338; no update notice. | None. **Agree** |
| `berthon_ethics_course/microsoft2025ai` | corrected | Microsoft AI Literacy Starting Guide, Jan 2025 | VERIFIED verbatim | sha256 matches; quotations exact at pp. 1 and 3 (the S2 correction to p. 3 holds). The Art 4 replacement by Reg 2026/1744 is right (Omnibus Art 1(5)). | None. **Agree** |
| `berthon_ethics_course/microsoft2025responsible` | true | 2025 RAI Transparency Report | VERIFIED verbatim | sha256 matches; every quotation at PDF pp. 7, 26, 28 as cited. | None. **Agree** |
| `dxd_foundation/nadella2026models` | S2 confirmed | Post, local X capture P1-P21 | VERIFIED verbatim | All 30 quoted strings found in the paragraph cited; word-occurrence claims confirmed (no "user", "customer", "employee", "people"; "human" P6 and P15; "person" P19; "authority" P5; "affected" P20). "nested black boxes" also occurs in P4. | Optional: note P4 for "nested black boxes". **Agree** |

**Legacy disagreement rate: 0 of 5 (0%; 95% Wilson interval 0–43%).** Five cards cannot estimate a rate; they show
no fault in the cards drawn.

---

## Counts

| Table | Rows | VERIFIED (verbatim + paraphrase) | WRONG | OVERSTATED | NEEDS LIBRARY CHECK | COULD NOT CHECK |
|---|---|---|---|---|---|---|
| N1 | 40 | 31 (25 + 6) | 2 | 7 | 0 | 0 |
| N4 | 28 | 23 (20 + 3) | 1 | 2 | 1 | 1 |
| N5 | 25 | 20 (15 + 5) | 3 | 2 | 0 | 0 |
| Anthropic-authored | 7 | 7 (6 + 1) | 0 | 0 | 0 | 0 |
| Web and documentation | 26 | 26 (26 + 0) | 0 | 0 | 0 | 0 |
| Legacy sample | 5 | 5 (5 + 0) | 0 | 0 | 0 | 0 |
| **All** | **131** | **112 (97 + 15)** | **6** | **11** | **1** | **1** |

Cards alone (61 card rows): 53 VERIFIED (one of them, `parikh2025powering`, as paraphrase with a misattribution to
fix), 5 WRONG (`palod2026evaluating`, `euomnibus2026`, `kingston2026social`, `luchs2026taking`,
`vonsamson2025immanent`), 3 OVERSTATED (`anthropic2026thinking`, `google2026agentic`, `shavit2023practices`). Facet
and COVERAGE claim rows (32): 21 VERIFIED, 1 WRONG, 8 OVERSTATED, 1 NEEDS LIBRARY CHECK, 1 COULD NOT CHECK. Every
sha256 matches; every DOI resolves; no Crossref update notice.

## What sinks or narrows a premise

- **A4, "no vendor shows anyone raw chain of thought": WRONG.** Anthropic offers full thinking output by sales
  arrangement, on the page N1 carded. The defensible claim is "no API setting returns it".
- **A5 and AP2: OVERSTATED.** AP2 is a real counter-instance to a general form of A5, but it does not "bind both
  sides", the verifier sees only the relevant constraints, and the current spec has no "Intent Mandate". A5 as
  written (about P11–P12) is not touched by AP2 and holds on the Microsoft cards.
- **A4, M2, harmonised standards: OVERSTATED.** Para 74 of the judgment says compliance is not compulsory. Use "part of
  EU law and hard to avoid in practice".
- **A4, "all four vendors": OVERSTATED as carded, true on my read.** OpenAI Service Terms §14 assigns responsibility
  for agent actions to the user; it needs a card.
- **A4, M9: OVERSTATED "only".** NIS2 Art 23 also gives notice without standing.
- **A8 and the brake: OVERSTATED.** Shavit et al. p. 15 adds redundant shutdown by deployer and data-centre operator
  and asks when a third party may terminate an agent.
- **M4, P15: OVERSTATED.** Microsoft's own logs captured what the customer's audit log missed: a one-sided record, not
  a missing one.

## Recommendations

**Mark `true`** (no change needed): `anthropic2025commercial`, `anthropic2025consumer`, `anthropic2026configure`,
`chiang2022exploring`, `cjeu2024publicresource`, `california2025transparency`,
`connellpensky2026can`, `diamantis2025danger`, `elmergawi2026introducing`, `eu2012standardisation`, `eu2016gdpr`,
`eu2022nis2`, `eu2024aiact`, `eu2024productliability`, `europeancommission2025reply`, `felt2012android`,
`feng2025regulatory`, `google2026gemini`, `hamilton2025digital`, `ketokivi2017reasoning`, `kugelberg2026practice`,
`laux2024three`, `microsoft2025multistage`, `microsoft2026audit`, `microsoft2026connect`, `microsoft2026copilot`,
`microsoft2026microsoft`, `microsoft2026overview`, `microsoft2026responsible`, `microsoft2026tracing`,
`microsoft2026use`, `nist2024artificial`, `openai2026agent`, `park2025critical`, `puppart2025brief`,
`seele2022greenwashing`, `sharon2024regulating`, `tabassi2023artificial`, `veale2021demystifying`,
`walzer1988interpretation`, `zhang2026hansel`, `zhao2026agentgui`.

**Mark `corrected`, with the fix:**
- `anthropic2026thinking`: add "In rare cases where you need access to full thinking output, contact Anthropic sales";
  restate the use as "no API setting returns the raw chain of thought".
- `google2026agentic`: add "Only constraints relevant to the closed Mandates are shared with the verifier"; note that
  v0.2 has no "Intent Mandate"; record the commit hash.
- `shavit2023practices`: add p. 15 (redundant shutdown by deployer and data-centre operator; third parties' right to
  terminate) and narrow the A4/M8 use.
- `palod2026evaluating`: Summary sentence on raw traces, as in the table.
- `parikh2025powering`: attribute counterparty verification to the spec, with its limit.
- `euomnibus2026`: "By way of derogation from Article 73".
- `kingston2026social`: locator p. 22, or quote the abstract's own wording.
- `luchs2026taking`: "Introduction (pp. 1-3)", not "untitled opening"; drop the 1968/1970s "inconsistency"; body
  "about 6,450-6,600 words".
- `vonsamson2025immanent`: "published version", not "submitted version"; mark the Fraser line as an OpenAlex abstract.
- `gornet2024european`: keep "(Edwards, 2022)" when the p. 16 sentence is quoted.
- `microsoft2026enabling`: cite Microsoft's roadmap record 570434, not the mirror.
- `openai2026reasoning`: align `SOURCE_URL.txt` with `source_url`.
- `anthropic2026usage`: name `eu2024aiact` as the corroborating card.
- `anthropic2026measuring`: "partly corroborated" (Felt concerns permission screens).
- `frontiermodelforum2026information`: name `N4/fmf/about.txt` and its sha256; add the access date.
- `bartha2019analogy`, `celikates2023critical`, `lovett2026republicanism`, `corporateeurope2025bias`: add "Accessed
  2026-10-24".

**Keep `pending`:** none of the 61 for a reason found here. The COVERAGE summary rows A4, A4/M2, A4/M9, A5 and the v1
A1 listing should be restated as in the tables before the lead adjudicates, and a card for OpenAI Service Terms §14 is
needed before "all four vendors" is used.

**Legacy sample:** all five agree with their recorded status (`true`, `true`, `corrected`, `true`, `S2 confirmed`).

## Files

- Fresh web copies and hashes: `~/iit-playground/berthon_ethics_local/pdfs/nadella/N7b/web/` (`SHA256SUMS.txt`, `FETCHED_AT.txt`).
- OpenAI Service Terms (archive snapshot 20261006184704): `N7b/oai_terms/service_terms.html`, sha256 `567755d21ec3c92849da3ff58e8e4e940bdbfaad82775f307a8edf902b336d01`.
- M365 Roadmap 570434 (Microsoft API): `N7b/m365roadmap/rm.json`, sha256 `bbb91cdeb8ffce726cc692f0c46866af3a6d5d792d09ccfb69b0bc9206b087b2`.
- Luchs recount: `N7b/luchs/luchs.txt` (sha256 `d003c39a…`), cleaned body `N7b/luchs/body_clean.txt` (sha256 `0ca28987…`).
