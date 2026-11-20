# R2 — Present-case concepts and claims: products and law as of 24 October 2026

*Run R2, 2026-10-24. Agent-drafted. The author has not reviewed it. None of the text is the author's. Substance only:
no comment here concerns wording or style.*

## 1. Scope

- **Ledger rows.** `../../consolidation/CONCEPT_LEDGER.md` has no I section (its sections are K, H, N, E, D, O, L, M).
  Reviewed: E01–E18 where the draft uses them (E05, E06, E08, E11, E13, E14, E15, E16 in detail) and M01–M10 for
  anything the draft carries (none of the M rows survives into `DRAFT_v1.md`; M09's venue facts are R7's).
- **Premises.** A4, A5, A8 (`../ARGUMENT_AND_OUTLINE.md` v2), with A7's "professed standard" route where §3.2 uses it.
- **Draft passages** (`../manuscript/DRAFT_v1.md`): opening ll. 25–92; §3 ll. 291–441; §4's fourth objection ll. 462–470;
  §5's worked refund case ll. 535–543 and duties ll. 519–533.
- **Sources.** Nadella's post (local capture, P1–P21); `../facets/N1_*.md`, `N4_*.md`, `AUDIT_N7b.md`, `ADJUDICATION.md`;
  every card the draft cites in §3 (headers and bodies read; quotations re-checked against today's live pages where the
  source is a web page); new primary sources listed in the search log.
- **Not re-opened** (verified by N7b on the same day and not contested here): Palod et al., Zhang and Nam, Felt et al.,
  Chiang and Yin, the Corporate Europe Observatory report, the Commission's reply to the Ombudsman, *Public.Resource.Org*,
  Microsoft's 2026 Transparency Report (except the passages I quote from the N1 copy), Shavit et al. (p. 4 read from the
  N1 copy), Moffatt.

## 2. Search log

All on 2026-10-24. Downloads: `~/iit-playground/berthon_ethics_local/pdfs/nadella/R2/<dir>/` with `SOURCE_URL.txt`.

| # | Source | Query or URL | Result | Notes |
|---|---|---|---|---|
| 1 | Local | `grep` of `CARD_INDEX.md` for Nadella, Purview, Entra, Copilot, Foundry, OpenAI, Anthropic, AI Act, GDPR, SB 53, AP2, Moffatt, Colorado, CFPB, insider, CERT, chain | 60 hits | Existing cards located; `cjeu2025dun` found in `berthon_ethics_course` (full-text, verified) |
| 2 | CELLAR | `publications.europa.eu/resource/celex/{32016R0679, 32024R1689, 32022R2065, 62022CJ0203, 32026R1744}` with `Accept: application/xhtml+xml` | HTTP 400 ×5 | "Invalid content type ... without language"; retried with `Accept-Language: en` |
| 3 | CELLAR | same five, with `Accept-Language: en` | 200 ×5 | Plain text extracted; sha256 recorded |
| 4 | CELLAR | `celex/32026D2274` (Commission Implementing Decision (EU) 2026/2274) | 200 | Read in full; carded |
| 5 | curl | Copilot consumer terms; Purview `audit-copilot`; Agent 365 overview; Copilot Studio `flows-advanced-approvals`; OpenAI reasoning guide; Anthropic `thinking`; Microsoft ACS post; Entra Agent ID page | 200 ×8 | Every string the draft quotes found on today's page (see §3 entries) |
| 6 | GitHub API | `repos/google-agentic-commerce/AP2/commits?path=docs/ap2/specification.md` | 200 | Latest commit for the file b4587ac1d0, 2026-04-28 ("Release Ap2 v0.2"): unchanged since N1 |
| 7 | GitHub raw | AP2 `specification.md` (main) | 200 | Both sentences the draft quotes present (whitespace-normalised) |
| 8 | Hugging Face | `openai/gpt-oss-120b/raw/main/README.md`; `api/models/openai/gpt-oss-120b` | 200, 200 | Model card read in part; createdAt 2025-08-04 |
| 9 | a2a-protocol.org | `/latest/specification/` | 200 | Agent Card definition read; not carded (paraphrase only) |
| 10 | eCFR API | `versioner/v1/full/2026-10-01/title-12.xml?part=1002&section=1002.9` | 406, then 200 | First call refused without compression; `--compressed` succeeded |
| 11 | leg.colorado.gov | `sites/default/files/2024a_205_signed.pdf` | 200 | SB 24-205 signed act |
| 12 | sei.cmu.edu | `insights.sei.cmu.edu/documents/5056/...SeventhEdition.pdf` (guessed) | 404 | Wrong path |
| 13 | sei.cmu.edu | `www.sei.cmu.edu/documents/5777/5692_CSG_Book_20-optimized.pdf` (dxd card URL) | 200 | CERT CSG 7th ed., 9.9 MB; definition p. 3 (PDF p. 10), stakeholders p. iv (PDF p. 6) |
| 14 | cppa.ca.gov | `regulations/pdf/ccpa_updates_cyber_risk_admt_text.pdf` (guessed) | 404 | Wrong path |
| 15 | cppa.ca.gov | `regulations/ccpa_updates.html` → `pdf/ccpa_updates_cyber_risk_admt_appr_text.pdf` | 200, 200 | Approved text, 127 pp.; carded |
| 16 | learn.microsoft.com | `azure/foundry-classic/foundry-models/tutorials/get-started-deepseek-r1` | 200 | ms.date 2026-07-28; carded |
| 17 | WebSearch | Colorado AI Act SB 24-205 effective date 2026 delay | 10 | 2025 coverage only |
| 18 | WebSearch (extended) | Colorado 2026 session SB 24-205 replaced repealed | 10 | SB 26-189 signed 14 May 2026, effective 1 Jan 2027 |
| 19 | WebSearch | "SB26-189" bill text pdf | 10 | Law-firm summaries; no official PDF link |
| 20 | WebFetch | `leg.colorado.gov/bills/sb26-189` | 200 | Found "Signed Act" link `bill_files/116489/download` |
| 21 | curl | four guessed `leg.colorado.gov/sites/default/files/...189...pdf` paths | 404 ×4 | Pattern differs from 2024 |
| 22 | curl | `leg.colorado.gov/bill_files/116489/download` | 200 | SB 26-189 signed act, 11.8 MB; carded |
| 23 | WebFetch | Finnegan article on SB 26-189 | 403 | Not circumvented |
| 24 | WebFetch | Holland & Knight, "Colorado Governor Signs SB 189" (18 May 2026) | 200 | Secondary check of the act's content; consistent with the text |
| 25 | WebSearch | CPPA ADMT regulations approved OAL effective date | 10 | Law-firm summaries: OAL approval Sept 2025; effect 1 Jan 2026; ADMT compliance 1 Jan 2027 |
| 26 | WebSearch | cppa.ca.gov final regulations text ADMT | 9 | No official link surfaced; found via row 15 |
| 27 | WebSearch | CFPB withdraws Circular 2022-03 2023-03 | 9 | 67 guidance documents withdrawn effective 12 May 2025; Federal Register notice not opened |
| 28 | WebSearch | Digital Omnibus GDPR Article 22 adopted 2026 | 10 | Still in negotiation as of the latest sources found (April 2026); Council draft reportedly dropped the Art. 22 change; not confirmed in an official text |
| 29 | WebSearch | Microsoft Responsible AI Standard 2026 re-engineered Developer/Deployer Chapter published | 9 | Only the 2026 Transparency Report describes it; no external text of the new Standard found |
| 30 | WebSearch | Azure AI Foundry DeepSeek-R1 reasoning_content | 9 | Led to row 16 |
| 31 | WebSearch | AI Act harmonised standards JTC 21 Official Journal 2026 | 9 | Conflicting; EN 18286 reported cited 14 Oct 2026 |
| 32 | WebSearch | "EN 18286" Official Journal Commission implementing decision 2026 | 10+10 | EUR-Lex ELI for Decision 2026/2274 → row 4 |
| 33 | WebSearch | California SB 53 2026 amendment | 9 | No 2026 amendment found |
| 34 | Local | N1 copy of Shavit et al. (`plain.txt`), p. 4 definition; N1 copy of Microsoft 2026 Transparency Report (`plain.txt`), PDF pp. 3–4, 11, 20 | — | Quoted below |
| 35 | Local | Nadella capture, P1–P21 | — | Word counts and principle count re-checked |
| 36 | Not attempted | openai.com (terms; "Learning to reason"); help.openai.com; digital-strategy.ec.europa.eu Art. 73 guidance; iso.org | — | Known 403/CloudFront/Cloudflare from N1/N4; not circumvented |
| 37 | Not searched | Consensus (quota exhausted until 1 Nov per N1/N4); Scholar Gateway (ACCESS_DENIED per N1/N4) | — | No scholarly-database pass this run; the concept owners here are statutes, standards bodies and vendor documents |

## 3. Entries

Locators: `P<n>` = paragraph of Nadella's post; `ll.` = `DRAFT_v1.md`; card keys are in `../../literature/cards/`.
Quotations are from copies I opened this session unless marked "per card".

### R2-01. "Insider risk" / insider threat (E13; ll. 25–34, 55–56, 455–457; title of §3)

**Draft.** Treats Nadella's borrowing as a transfer of enterprise insider-threat practice to models (l. 55: "enterprises
have learned to handle powerful insiders") and builds "the insider-risk architecture" on it.

**Owning literature.** CERT National Insider Threat Center, *Common Sense Guide*, 7th ed. (`dxd_foundation/cert2022common`,
my copy `R2/cert_csg7/csg7.pdf`), p. 3: "Insider Threat—The potential for an individual who has or had authorized access
to an organization’s critical assets to use their access, either maliciously or unintentionally, to act in a way that
could negatively affect the organization"; "Insider Risk—The impact and likelihood associated with the realization of an
insider threat". The programme's stakeholders (p. iv) are "Management, Human Resources, Legal Counsel, Physical Security,
Information Technology, Information Security" and the organisation's other internal groups. Nadella's P7 uses the concept
as CERT does: "Not because they are necessarily malicious, but because any sufficiently capable actor with access to
important systems can make mistakes or be compromised".

**Gap.** None in Nadella's use; the draft does not define the term. The definition does more for the paper than the draft
takes: in its own literature the insider frame names one victim, "the organization", and no outside party. That is the
property A4 asserts, stated by the concept's owners.

**Verdict.** Holds. Fix: A4 can cite the CERT definition as the frame's own statement of whom it protects.

### R2-02. "Trust architecture" (l. 29; P3)

**Draft.** Quotes Nadella's phrase. **Owners.** None; the nearest term of art is NIST's "zero trust architecture"
(`dxd_foundation/rose2020zero`, not reopened), which is a different thing (per-request access control). Nadella's P11
appeals to "an information security principle dating back to the 1970s that a program must not be able to bypass or
tamper with the mechanisms that enforce its permissions" (the reference-monitor idea); the draft does not use that line.
**Verdict.** Holds, as a quotation of Nadella; the paper should not gloss it with NIST's term.

### R2-03. "Agent", "agentic" (throughout §3; K02's widening)

**Owners.** Shavit et al. 2023 (`shavit2023practices`, N1 copy), p. 4: "We define the degree of agenticness in a system as
“the degree to which a system can adaptably achieve complex goals in complex environments with limited direct
supervision.”" Their parties are "model developer", "system deployer" and "user" (p. 5, per card); third parties appear
at p. 14 as those who may "demand" agent identification (per card). **Gap.** The draft's examples span the scale: a
consumer Copilot "Action", a Copilot Studio approval flow, a refund agent. Nothing in the owning definition excludes any
of them. The paper's second party is absent from the owning taxonomy, which is itself evidence for A4. **Verdict.** Holds.

### R2-04. Copilot terms "solely responsible" as evidence about the second party (E14; ll. 50–53, 393–399; A4 "responsibility for actions placed on the user")

**Draft.** Reads the consumer Copilot terms, Anthropic's consumer terms and the enterprise application card as placing
"the burden ... where the brake is not" (l. 393) and as "*Upton*'s rule in a new medium" for "the person at the end of the
chain" (ll. 398–400).

**Source as read today.** `microsoft2026copilot`, live page fetched 2026-10-24, "Effective: August 18, 2026", unchanged:
"When you request that Copilot take Actions on your behalf, you are solely responsible for those Actions and any results
or consequences"; "Always verify the accuracy of information presented by Copilot before you rely on it"; for shopping,
"You are responsible for reading and complying with the Merchant’s terms". The "you" throughout is the account holder who
requests the Action.

**Gap.** The "you" of every term the draft cites is the agent's principal, who also holds the approval. In the paper's
own frame (A4, CA) that party is the deploying organisation or its user, not the customer, applicant or counterparty.
The terms show a chain: Anthropic's commercial terms oblige the customer to "notify its Users" (per `anthropic2025commercial`,
D.3), and Microsoft's Code of Conduct obliges customers to disclose and oversee (per `microsoft2026microsoft`). The chain
ends at the last human who requested the action; the second party of the refund case never sees these terms and is bound
by none of them. The one source in the draft that shows a firm placing the verification burden on the second party is
*Moffatt* (Air Canada's argument that the customer should "double-check", para 28, per `moffatt2024air`), which §4 uses
against the firm.

**Verdict.** Narrower. The terms carry "responsibility handed down the chain to the principal who can approve"; they do
not carry "the person acted on is told to verify". For the second party the evidence is *Moffatt* and the silence of
every document read.

### R2-05. The audit log and "whose evidence it finally is" (E13/E14; ll. 338–347; A4 "a record kept for the organisation")

**Source today.** `microsoft2026audit` (Purview), live: "which user interacted with Copilot, when the interaction took
place, and where it occurred" present verbatim. The 2026 Transparency Report passage on Unified Audit Logs was verified
by N7b; the draft's framing ("complete for the supplier and incomplete for its customer", l. 345) is the adjudicated
form (ADJUDICATION §6, A4/M4). **Verdict.** Holds.

### R2-06. Custody: Agent 365, Entra Agent ID, Agent Control Specification (ll. 299–314; A5)

**Sources today.** `microsoft2026overview`: "real-time visibility into their agentic environment", "Admins can now view
all their agents", "help leaders and AI admins stay in control" all present. `elmergawi2026introducing`: both quoted
sentences present. Entra Agent ID page (N1 entry 2; my fresh copy): the identity exists to "distinguish operations
performed by AI agents from operations performed by workforce, customer, or workload identities"; nothing on the page
addresses anyone outside the tenant. **Verdict.** Holds. A5 stands on these for Microsoft's agent controls.

### R2-07. Copilot Studio AI-stage approvals (ll. 375–378; A4 brake)

**Source today.** `microsoft2025multistage`, live, the $5,000 sentence present; the page still carries "preview" (3
occurrences). **Verdict.** Holds; the draft should state that the feature is in preview.

### R2-08. Chain-of-thought: "In the products, nobody outside the supplier receives it" (ll. 350–356, 405; A4; P9)

**Draft.** Relies on OpenAI's and Anthropic's API documentation and concedes Anthropic's sales route.

**Sources today.** `openai2026reasoning`: "we don’t expose the raw reasoning tokens emitted by the model" present.
`anthropic2026thinking` (Anthropic-authored; I am an Anthropic model): "No display setting returns the raw chain of
thought" and "In rare cases where you need access to full thinking output, contact Anthropic sales" both present.
Corroboration for the default: OpenAI's page; Google's thinking docs (N1 entry 29, uncarded). The sales route has no
corroboration and cuts the other way.

**Counter-sources.** OpenAI's open-weight model card (`openai2025gpt`, Hugging Face README): "Full chain-of-thought: Gain
complete access to the model’s reasoning process, facilitating easier debugging and increased trust in outputs. It’s not
intended to be shown to end users." Microsoft's own Foundry tutorial (`microsoft2026tutorial`, ms.date 2026-07-28): "If
the model generates reasoning, the response contains content wrapped in <think>...</think> tags followed by the final
answer"; "Some models, like DeepSeek-V4-Pro, might respond with the reasoning content. Others, like o1, output only the
completions."

**Gap.** The sentence is false for open-weight models, including those Microsoft serves to its own customers. It is true
for the hosted closed frontier APIs the draft names. The surviving and sharper claim is that where the raw reasoning is
delivered at all it goes to the deployer, and the supplier says it is "not intended to be shown to end users". That is
the second-party point in the supplier's words.

**Verdict.** Narrower. Fix: "No hosted closed frontier API returns the raw chain of thought by default (OpenAI, Anthropic,
Google); open-weight models return it to the deployer, and their suppliers address it to developers, not to the people
the outputs reach." The worked case's "available to no one outside the supplier" (l. 405) needs the same narrowing.

### R2-09. What lay readers do with traces (ll. 356–361)

Palod et al. Table 3 (54.0 against 54.2 per cent) and Zhang and Nam (60.7 per cent; 66 per cent re-execution) were
verified by N7b with one correction already in the draft. Both are preprints with lay or small samples. Not reopened.
**Verdict.** Holds, narrowly (preprints; lay users; the draft states both numbers correctly).

### R2-10. "Microsoft's own Standard asks the same" (ll. 362–368; A7 route 1; E14)

**Source.** `berthon_ethics_course/microsoft2022responsible`, p. 9, T1.3: evaluate "whether each stakeholder who will make
decisions or be subject to decisions based on the behavior of the system can interpret the relevant system responses
reasonably well" (per card; verified). **Counter-source.** Microsoft's 2026 Transparency Report (N1 copy): "This year, we
re-engineered our Responsible AI Standard" (PDF p. 4); "for the first time, our Standard also includes a Deployer Chapter"
whose "four objectives" are to "assess the underlying AI application, deploy trustworthy AI applications, detect and
respond to issues, and provide information to support responsible deployment" (PDF p. 20). My search (row 29) found no
published text of the re-engineered Standard. **Gap.** The draft's present tense ("asks") attributes to Microsoft today a
goal from a 2022 document that Microsoft says it has rebuilt; whether T1.3 and A5.4 survive is unknown. The route-1
bridge (A7) needs the profession to be current or to be dated. **Verdict.** Narrower. Fix: "Microsoft's 2022 Standard
asked ...; the 2026 report describes a re-engineered Standard whose text is unpublished and reports no evaluation against
either goal."

### R2-11. The brake: "held by the organization"; "The second party holds none" (ll. 371–392; A4; P19)

**Sources.** Shavit et al. p. 9 quotation verified by N7b; their p. 14–15 give the first brake to the user and redundant
ones to the deployer and the data-centre operator and ask when "an external party" may terminate (per card, corrected).
AI Act art. 14(4)(e) (my copy): the high-risk system must let "natural persons to whom human oversight is assigned ...
intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar
procedure". **Gap.** Law and industry both place the brake with the deployer's overseer; no source read gives it to the
person acted on. The Shavit p. 15 question is the nearest the literature comes to asking about her. **Verdict.** Holds,
with art. 14(4)(e) as the legal confirmation and Shavit p. 15 as the open question the paper should name.

### R2-12. Approval rates (ll. 379–381; Anthropic-authored)

`anthropic2026measuring`: "roughly 20%" to "over 40% of sessions" verified; the same post reports interrupts rising from
5 to about 9 per cent of turns, which the draft omits. Corroboration outside Anthropic is partial (Felt et al. concern
Android permission screens; `yu2026habituation` in dxd not reopened). **Verdict.** Holds, narrowly; flag as
Anthropic-authored with partial corroboration; report the interrupt rise beside the auto-approve rise.

### R2-13. AP2 as the partial counter-instance (ll. 314–321, 522–524; A5)

**Source today.** Spec at commit b4587ac1d0 (v0.2, 28 Apr 2026), unchanged: "The User sees and approves a set of
constraints over what closed Checkout and Payment would meet their intent"; "Only constraints relevant to the closed
Mandates are shared with the verifier". The draft already carries the N7b limit. **Gap.** In AP2 the signer is the
agent's principal (the shopper) and the verifier is the merchant, a counterparty with a card-network liability regime
behind it (N1 C2). Mapped onto the refund case, the analogue would be the organisation signing limits the customer can
verify; AP2 shows the mechanism exists, not that anyone has built it for a customer. **Verdict.** Holds as "partial
counter-instance"; the paper should say whose envelope it is and who verifies.

### R2-14. AI Act art. 73 in the present tense, and its reach (ll. 411–413, 406–408; A4)

**Source.** Art. 73(1) quotation verified (N4, N7b). Regulation (EU) 2026/1744 (my copy), Art. 1(40)(b), replacing
art. 113 third paragraph point (c): "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply
from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and
(ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I". Art. 73 sits in
Chapter III, Section 3. **Gap.** (i) The duty does not yet apply; the draft's "requires" is premature by fourteen months.
(ii) A refund agent is not a high-risk system under Annex III, so art. 73 would not reach the worked case even then; the
draft's "the disclosure goes, under the law that now exists, to someone else" (ll. 407–408) should read "no incident
regime now in force reaches it". **Verdict.** Narrower.

### R2-15. The AI Act's second-party provisions the draft omits (ll. 409–422, 434–435; A4 "notice to authorities, not standing for those affected")

**Sources (my copy of 2024/1689).** Art. 26(11): deployers of Annex III systems "that make decisions or assist in making
decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk
AI system." Art. 50(1): providers "shall ensure that AI systems intended to interact directly with natural persons are
designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI
system". Art. 85: "any natural or legal person having grounds to consider that there has been an infringement of the
provisions of this Regulation may submit complaints to the relevant market surveillance authority"; such complaints
"shall be taken into account for the purpose of conducting market surveillance activities". Art. 86(1): any affected
person subject to an adverse Annex III decision "shall have the right to obtain from the deployer clear and meaningful
explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken."
Art. 14(4)(c)–(d): overseers must be enabled "to correctly interpret the high-risk AI system’s output" and "to decide ...
not to use the high-risk AI system or to otherwise disregard, override or reverse the output".

**Gap.** §3.4 presents the Act as incident notice to authorities only. The Act also gives the person acted on notice that
she is acted on (26(11), 50), an explanation after the decision (86), and a complaint that is a surveillance input (85),
all for high-risk uses from December 2027; it gives her no brake and no decider outside the deployer. The paper's
`eu2024aiact` card already records arts. 85–86; the draft dropped them.

**Verdict.** Narrower. Fix for A4: "incident notice runs to authorities (art. 73); the affected person gets notice (arts.
26(11), 50(1)) and an explanation (art. 86) after the fact and a complaint that feeds surveillance (art. 85); none of
this is a brake, an independent decider or the envelope." The draft should say this in §3.4 before §4 says "the law
already provides".

### R2-16. GDPR art. 22, art. 15(1)(h) and *Dun & Bradstreet* against A8 (ll. 462–470, 519–533; A8 "the law provides remedies after the harm, not voice or brake before it"; §5 duties 1, 3, 4)

**Draft.** §4's fourth objection grants the GDPR "notice and a remedy for breaches of personal data" and the Product
Liability Directive a damages claim, and concludes "None of these regimes gives the person a voice or a brake before the
action" (ll. 462–469). §5 derives six duties "each with a working precedent", all historical or AP2.

**Sources (my copy of 2016/679).** Art. 22(1): "The data subject shall have the right not to be subject to a decision
based solely on automated processing, including profiling, which produces legal effects concerning him or her or
similarly significantly affects him or her." Art. 22(3): where the contract or consent exception applies, "the data
controller shall implement suitable measures to safeguard the data subject's rights and freedoms and legitimate
interests, at least the right to obtain human intervention on the part of the controller, to express his or her point
of view and to contest the decision." Art. 15(1)(h): the right of access covers "the existence of automated
decision-making, including profiling, referred to in Article 22(1) and (4) and, at least in those cases, meaningful
information about the logic involved, as well as the significance and the envisaged consequences of such processing for
the data subject" (the same words recur in arts. 13(2)(f) and 14(2)(g)). CJEU, *SCHUFA*, C-634/21 (per
`berthon_ethics_course/cjeu2023schufa`, para 52): art. 22(1) "lays down a prohibition in principle". CJEU, *Dun &
Bradstreet Austria*, C-203/22, 27 Feb 2025 (`berthon_ethics_course/cjeu2025dun`; my copy), operative part 1: the data
subject "may require the controller, as ‘meaningful information about the logic involved’, to explain, by means of
relevant information and in a concise, transparent, intelligible and easily accessible form, the procedure and
principles actually applied"; para 58: this is "to enable the data subject effectively to exercise the rights conferred
on him or her by the GDPR and, in particular, Article 22(3)"; para 59: "the mere communication of a complex
mathematical formula, such as an algorithm, or ... the detailed description of all the steps" does not satisfy it.

**Gap.** For a solely automated decision with legal or similarly significant effect on a person in the EU, the law
already gives her: a prohibition in principle, which is duty 1's structural refusal in legal form; a right to a human, to
be heard and to contest, which is voice after the decision; and a right to an explanation of "the procedure and
principles actually applied", which is a record in her hands. The paper's own ledger (E05) and library carry these
cards; `DRAFT_v1.md` dropped them. Limits that keep the paper's argument alive: the trigger ("solely"; "legal or
similarly significant") is contested at the margin and a refund denial may fall outside it; the human intervention is
the controller's own, not independent (E06); nothing operates before the decision except the prohibition itself; and
none of it is in Nadella's architecture or Microsoft's products. The 2025 Digital Omnibus proposal to soften art. 22 was
reportedly dropped from the Council's compromise text (row 28; unconfirmed in an official document).

**Verdict.** Wrong, in part. A8's "not voice or brake before it" and §4's description of the GDPR as breach notice plus
damages are contradicted by art. 22 as the CJEU reads it. Fix: restate A8 as "where law reaches the second party it does
so for enumerated decision types, after the decision, through explanation, a controller-run human review and a
complaint; it gives no brake before the action, no decider the operator does not control, and no envelope; and the
architecture adopts none of it." §5 should name art. 22(1) as the present-day precedent for duty 1 and art. 22(3) with
*Dun & Bradstreet* as a partial one for duties 3 and 4.

### R2-17. US law for the second party: Regulation B, Colorado, California (A4, A5, A8; ll. 462–470, 535–543)

**Regulation B** (`cfpb2026notifications`, eCFR as of 2026-10-01), § 1002.9(a)(2): an adverse-action notice "shall be in
writing and shall contain a statement of the action taken ... and either: (i) A statement of specific reasons for the
action taken; or (ii) A disclosure of the applicant's right to a statement of specific reasons"; § 1002.9(b)(2): the
statement "must be specific and indicate the principal reason(s)"; a failed score "on the creditor's credit scoring
system" is "insufficient". The CFPB circulars applying this to complex algorithms were withdrawn in May 2025 (row 27; not
opened); the rule stands.

**Colorado** (`colorado2024consumer`; `colorado2026automated`). SB 24-205 § 6-1-1703(4)(b) would have required, for an
adverse consequential decision, "A STATEMENT DISCLOSING THE PRINCIPAL REASON OR REASONS ... INCLUDING: (A) THE DEGREE TO
WHICH, AND MANNER IN WHICH, THE HIGH-RISK ARTIFICIAL INTELLIGENCE SYSTEM CONTRIBUTED", "AN OPPORTUNITY TO CORRECT" and
"AN OPPORTUNITY TO APPEAL ... WHICH APPEAL MUST, IF TECHNICALLY FEASIBLE, ALLOW FOR HUMAN REVIEW" (pp. 13–14). It never
took effect. SB 26-189 (signed 14 May 2026 per the bill page; applies to decisions on or after 1 January 2027) keeps a
pre-decision notice satisfiable by "A PROMINENT PUBLIC NOTICE" (§ 6-1-1704(2)), a thirty-day post-adverse-outcome
disclosure with "A PLAIN LANGUAGE DESCRIPTION OF THE CONSEQUENTIAL DECISION AND THE ROLE THE COVERED ADMT PLAYED"
(§ 6-1-1704(3)(a)), and on request "AN OPPORTUNITY FOR MEANINGFUL HUMAN REVIEW AND RECONSIDERATION OF THE CONSEQUENTIAL
DECISION, TO THE EXTENT COMMERCIALLY REASONABLE" (§ 6-1-1705(1)(a)(II)), by a reviewer who "DOES NOT DEFAULT TO THE
SYSTEM OUTPUT" (§ 6-1-1701(15)(c)); enforcement "EXCLUSIVELY BY THE ATTORNEY GENERAL" (§ 6-1-1706(1)(b)); "NOTHING IN
THIS PART 17 CREATES A NEW PRIVATE RIGHT OF ACTION" (§ 6-1-1709(1)).

**California** (`cppa2025text`). For "significant decisions" (financial or lending services, housing, education,
employment or contracting, healthcare; § 7001(ddd)): a Pre-use Notice (§ 7220); a right to opt out of ADMT (§ 7221(a))
unless the business "provides the consumer with a method to appeal the decision to a human reviewer who has the
authority to overturn the decision" (§ 7221(b)(1)); on access, "Information about the logic of the ADMT ... which may
include the parameters that generated the output as well as the specific output with respect to the consumer"
(§ 7222(b)(2)); compliance "no later than January 1, 2027" (§ 7200(b)).

**Gap.** In the United States the second party already has a record of reasons in credit and will have, from 2027 in
two states, notice before, a reasoned record after, correction, and a human reviewer with authority to overturn (or an
opt-out), in enumerated high-stakes domains. She has standing through an attorney general only (Colorado) and no
independent decider anywhere. A refund decision is outside every one of these regimes. Colorado's 2024 rights were
narrowed before they applied, which supports the paper's claim about who writes the rules (A4, P6).

**Verdict.** Narrower, for A8 and for §5's "working precedent" framing. Fix: state the duties as generalisations of
regimes that exist for credit, housing, employment, education, health and insurance decisions, and locate the gap in
(a) the domains outside those lists, (b) the absence of any brake before the action, (c) the operator-run reviewer, and
(d) the architecture's silence.

### R2-18. The DSA's declared envelope against A5's general form (ll. 313–314; A5; E05, E06)

**Source** (`eu2022dsa`, upgrade card). Art. 14(1): terms and conditions "shall include information on any policies,
procedures, measures and tools used for the purpose of content moderation, including algorithmic decision-making and
human review"; art. 17(1): "a clear and specific statement of reasons to any affected recipients of the service";
art. 17(3)(c): "information on the use made of automated means in taking the decision". Arts. 20–21 (per the superseded
card): internal complaints and certified out-of-court bodies that "shall not have the power to impose a binding
settlement". **Gap.** The draft's "No duty in the architecture makes the envelope known or binding to the person it
constrains the agent toward" is true of the architecture. As a claim about what exists, EU law already obliges one
class of operator to declare its automated tools and procedures to the people they act on and to hand each a reasoned
record naming the automated means. The DSA case is K02's one-party case (a platform judging its own users), and the
envelope is declared as policy, not per case. **Verdict.** Narrower (for A5 read generally; A5 as written, about P11–P12,
holds). Fix: concede the DSA as the legal precedent for duty 2 and name its limits.

### R2-19. California SB 53 and the worked case (ll. 413–418, 406–408)

Quotations verified (N4, N7b); no 2026 amendment found (row 33). "Critical safety incident" is confined to weight
exfiltration, catastrophic risk, loss of control and deceptive subversion of the developer's controls (§ 22757.11(d),
per `california2025transparency`). A refund agent's wrong denial is outside it. **Verdict.** Narrower: the statute
supports "notice to government, not to the affected" for frontier developers; it says nothing about the refund case, and
the worked case should not imply that a disclosure duty is triggered.

### R2-20. Industry standards and the harmonised-standard presumption (ll. 323–335; A4, P6)

Quotations from the CEO report, the Commission's reply and *Public.Resource.Org* verified (N7b); the draft already states
para 74's "not compulsory". **New fact.** Commission Implementing Decision (EU) 2026/2274 of 12 October 2026, OJ L
14.10.2026 (`europeancommission2026commission`): "This resulted in the adoption of the new harmonised standard EN
18286:2026" (recital 3); Art. 1 publishes its reference; Annex: "EN 18286:2026 Artificial intelligence – Quality
management system for EU AI Act regulatory purposes". The draft's conditional ("Once cited in the Official Journal",
l. 332) became fact four days after Nadella's post, for the Art. 17 quality-management standard, which includes the
procedures for serious-incident reporting (art. 17(1)(i)). The composition count (55 vs the Commission's "more than
half" the other way) remains disputed, and the draft presents both. **Verdict.** Holds on the standards claim, now
stronger; contested on the composition share, which the draft already treats as contested. Fix: cite the Decision; the
`euomnibus2026` and `europeancommission2025reply` cards' "none yet cited" is superseded.

### R2-21. Skilling "reports reach, not effect" (ll. 423–430; E14; A8)

Chiang and Yin p. 159 verified (N7b); Microsoft's Elevate pages report counts (N4 entries 22–23). N4 found one
counter-study (`connellpensky2026can`, abstract only: modules built checking skill equitably in students). The draft's
sentence is confined to "those who most need it" and holds; the counter-evidence belongs in R5's objections. **Verdict.**
Holds, narrowly.

### R2-22. *Moffatt v. Air Canada* (ll. 464–469; A8)

Per `moffatt2024air` (verified by the lead): paras 27–28 quoted correctly; damages $650.88 (para 40); a small-claims
tribunal; a chatbot giving information, not an agent acting. The draft says all of this. **Verdict.** Holds. It is also
the draft's only second-party source on the verification burden (R2-04).

### R2-23. The worked refund case (ll. 402–408, 535–543)

Four claims: the organisation holds envelope, record and brake (holds, R2-05, R2-06, R2-11); "its trace is available to
no one outside the supplier" (narrower, R2-08); the customer "learns of it only as a result" (holds in the architecture;
in the EU, if the denial is solely automated and "similarly significantly affects" her, art. 22(3) and art. 15(1)(h)
give her a human, a hearing and an explanation, R2-16; whether a refund denial crosses that threshold is open); and the
disclosure "goes ... to someone else" (narrower: no incident regime in force reaches a refund agent, R2-14, R2-19).
**Verdict.** Narrower. Fix: either choose a case outside art. 22's reach by construction and say so, or add the EU
customer's art. 22 rights to the case and show what the architecture adds to them, which is nothing.

### R2-24. Facts about the post (ll. 25–34, 455)

Re-checked on the capture: "user", "customer", "employee", "people" do not occur in P1–P21; "those affected" occurs once
(P20); P14–P20 are seven principles; the capture of 12 October shows 13M views. P3's "we" is a reading: it can be
Microsoft as provider-and-deployer or "we" the industry, and P17's "Orgs" is the one place the subject is named.
**Verdict.** Holds; the "we" reading should be flagged as the paper's and anchored on P17.

## 4. Gaps and blocks

| Item | Status | Where a Bentley library user would find it |
|---|---|---|
| Microsoft's re-engineered Responsible AI Standard (2026; Developer and Deployer Chapters) | Described in the 2026 Transparency Report; no text found published | Microsoft's responsible-AI site; ask Microsoft whether an external release exists. Until then, cite v2 (2022) as the standard professed then |
| CFPB, Withdrawal of Guidance Documents (effective 12 May 2025) listing Circulars 2022-03 and 2023-03 | Not opened; web search only | Federal Register (govinfo.gov), May 2025; HeinOnline |
| Colorado SB 26-189: the Attorney General's implementing rules (due by 1 Jan 2027 under §§ 6-1-1704(4), 6-1-1705(3)) | Not yet issued as far as searched | coag.gov rulemaking page; Colorado Register |
| Finnegan, "Colorado Replaces Landmark AI Act" | WebFetch 403 | Browser; Lexis/Westlaw practitioner insights. Holland & Knight's summary used instead |
| California CPPA: OAL approval record and effective-date notice for the ADMT regulations | Not opened; law-firm summaries only | cppa.ca.gov rulemaking page ("Notice of Approval"); OAL file |
| GDPR Digital Omnibus (Nov 2025 proposal) and its treatment of Art. 22 | Status unconfirmed in any official text (row 28) | European Parliament Legislative Observatory; Council press releases |
| EU AI Act harmonised standards for Arts. 9–15 (risk management, transparency, human oversight) | No OJ citation found by 24 Oct 2026 beyond EN 18286 | Official Journal L series; Commission "standardisation" page for the AI Act |
| OpenAI Service Terms §14 (agent actions) | Not re-attempted (openai.com 403 to N1 and N7b; archive route awaits the author's ruling, ADJUDICATION §5) | Browser; Internet Archive |
| Commission draft guidance and template on Art. 73 serious incidents | Not re-attempted (CloudFront 403 to N4) | digital-strategy.ec.europa.eu in a browser |
| A2A protocol: whether any Agent Card field declares limits (not capabilities) to a counterparty | Read in part; the Agent Card describes "identity, capabilities, skills, service endpoint, and authentication requirements"; no limits field found; not carded | a2a-protocol.org specification, §5 and §12.7 |
| Visa Intelligent Commerce / Mastercard Agent Pay (agentic tokens, merchant verification) | Not searched this run | Vendor developer documentation; would extend R2-13 beyond Google |
| Consensus and Scholar Gateway | Quota exhausted / access denied (per N1, N4; not retried) | Rerun after 1 Nov for scholarship on art. 22 and AI Act art. 86 (e.g. Kaminski; Wachter, Mittelstadt and Floridi) |

**Cards the lead should extend (same citekey already in this folder, so no R2 upgrade card was written):**
`eu2016gdpr` (add arts. 13(2)(f), 15(1)(h), 22; my copy `R2/gdpr/32016R0679.txt`, sha256
8e5d737c8081e86bc0e661d9675f3923aa2a588fe44c87031c573d7cdff82343); `eu2024aiact` (add arts. 14(4), 26(7), 26(11), 50(1),
113 as amended; `R2/aiact/32024R1689.txt`, sha256 d3713fb660aadae637c1f3f5cfbd28fab7780a94af42078545ed11da96325944);
`euomnibus2026` (add Art. 1(40) operative dates; `R2/omnibus/32026R1744.txt`, sha256
4d591eb90a3768c817df90e692e8c20441a84d24e38a335f5c2e3f195b666d06). Legacy cards cited without a new card: `cert2022common`
(dxd; my copy `R2/cert_csg7/csg7.pdf`, sha256 c2640e3c8bfd028b3e35e2d02108816d36e219e9ecc6f2fcbf2ea2670cd5355e),
`cjeu2025dun`, `cjeu2023schufa`, `microsoft2022responsible` (bec).

**Anthropic-authored sources in scope** (`anthropic2026thinking`, `anthropic2026measuring`, `anthropic2025consumer`): each
flagged above with its corroboration; the reviewer is an Anthropic model.

## 5. Verdict table

| ID | Concept / claim | Draft lines | Verdict | Evidence (card + locator) | Fix to the argument |
|---|---|---|---|---|---|
| R2-01 | "Insider risk" used as CERT uses it | 25–34, 55–56 | holds | `cert2022common` p. 3 (definition names "the organization" as the harmed party), p. iv (stakeholders); P7 | Cite the owners' definition as the frame's own statement of whom it protects |
| R2-02 | "Trust architecture" | 29 | holds | P3; `rose2020zero` is a different term | Keep as Nadella's phrase; do not gloss with NIST |
| R2-03 | "Agent"/"agentic" | §3 passim | holds | `shavit2023practices` p. 4 (definition), p. 5 (three parties) | Note that the owning taxonomy has no second party |
| R2-04 | Copilot/Anthropic terms place the burden on the second party | 50–53, 393–400 | narrower | `microsoft2026copilot` (live, eff. 18 Aug 2026); `anthropic2025consumer` §4; `anthropic2025commercial` D.3; `moffatt2024air` para 28 | A4: "responsibility handed down the chain to the principal who holds the approval"; second-party evidence is *Moffatt* and the documents' silence |
| R2-05 | Audit log kept for the organisation; one-sided record | 338–347 | holds | `microsoft2026audit` (live); `microsoft2026responsible` PDF p. 19 | None |
| R2-06 | Custody of the envelope: Agent 365, Entra Agent ID, ACS | 299–314 | holds | `microsoft2026overview`, `elmergawi2026introducing` (live); Entra page (N1 entry 2) | None |
| R2-07 | AI-stage approvals bypass managers | 375–378 | holds | `microsoft2025multistage` (live; "preview") | State preview status |
| R2-08 | "Nobody outside the supplier receives" the chain of thought | 350–356, 405 | narrower | `openai2026reasoning`; `anthropic2026thinking` (Anthropic; sales route); `openai2025gpt` README Highlights; `microsoft2026tutorial` "Reasoning content" | "No hosted closed API returns it by default; open-weight models return it to the deployer and their suppliers say it is not for end users" |
| R2-09 | Lay readers do not reject wrong outputs better with traces | 356–361 | holds | `palod2026evaluating` Table 3 p. 6; `zhang2026hansel` p. 9 (per N7b) | Keep "preprints; lay or small samples" |
| R2-10 | "Microsoft's own Standard asks" T1.3/A5.4 | 362–368 | narrower | `microsoft2022responsible` p. 9, p. 8; `microsoft2026responsible` PDF pp. 4, 20 (re-engineered; Deployer Chapter) | Date the profession to 2022; say the 2026 Standard is unpublished and reports no evaluation |
| R2-11 | Brake held by the organisation; none for the second party | 371–392 | holds | `shavit2023practices` pp. 9, 14–15; AI Act art. 14(4)(e) (R2 copy) | Add art. 14(4)(e) and Shavit's open question about "an external party" |
| R2-12 | Auto-approve rising 20%→40% | 379–381 | holds | `anthropic2026measuring` (Anthropic; partly corroborated by `felt2012android` p. 1) | Report the interrupt rise (5%→9%) beside it; flag authorship |
| R2-13 | AP2 as partial counter-instance | 314–321, 522–524 | holds | `google2026agentic` "Modes" (live, commit b4587ac1d0); `parikh2025powering` | Say the signer is the principal and the verifier a merchant with a liability regime |
| R2-14 | AI Act art. 73 "requires" incident reports; reaches the refund case | 406–413 | narrower | `eu2024aiact` art. 73(1); `euomnibus2026` Art. 1(40)(b) (applies 2 Dec 2027 / 2 Aug 2028) | "Will require from Dec 2027, for high-risk systems; a refund agent is outside Annex III; no regime in force reaches it" |
| R2-15 | "Notice to authorities, not standing for those affected" (AI Act) | 409–422, 434–435 | narrower | AI Act arts. 26(11), 50(1), 85, 86(1) (R2 copy; `eu2024aiact` card has 85–86) | A4: affected person gets notice and explanation after, and a complaint; no brake, no independent decider, no envelope |
| R2-16 | A8: "the law provides remedies after the harm, not voice or brake before it"; §4's GDPR account | 462–470, 519–533 | wrong (in part) | GDPR arts. 22(1), 22(3), 15(1)(h) (R2 copy); `cjeu2023schufa` para 52; `cjeu2025dun` operative part 1, paras 58–59 | Restate A8 (enumerated decisions; after the fact; controller-run; no envelope; not in the architecture); cite art. 22(1) as duty 1's present precedent and art. 22(3)/*Dun & Bradstreet* for duties 3–4 |
| R2-17 | US law gives the second party nothing before the harm | 462–470, 535–543 | narrower | `cfpb2026notifications` § 1002.9(a)(2), (b)(2); `colorado2024consumer` § 6-1-1703(4)(b); `colorado2026automated` §§ 6-1-1701(15), 1704(1)–(3), 1705(1), 1706(1)(b), 1709(1); `cppa2025text` §§ 7001(ddd), 7200(b), 7220–7222 | Duties 1, 3, 4 have legislated precedents for enumerated decisions from 2027; gap is domain, timing, operator-run review, AG-only standing, and the architecture's silence |
| R2-18 | A5 general form: no declared envelope to the person acted on | 313–314 | narrower | `eu2022dsa` arts. 14(1), 17(1), 17(3)(c), 17(3)(f); arts. 20–21 (superseded card) | A5 holds for P11–P12 and Microsoft; concede the DSA as duty 2's legal precedent (policy-level; one-party case) |
| R2-19 | SB 53 and the worked case | 406–408, 413–418 | narrower | `california2025transparency` §§ 22757.11(d), 22757.13(c), (f), (g)(1), 22757.15(b) | Statute supports notice-to-government for frontier developers; it does not reach a refund agent |
| R2-20 | Industry-written standards bind through the presumption; composition count | 323–335 | holds (standards) / contested (share) | `europeancommission2026commission` recital 3, Art. 1, Annex (EN 18286 cited 14 Oct 2026); `cjeu2024publicresource` paras 70, 74–75; `corporateeurope2025bias` vs `europeancommission2025reply` p. 13 | Cite the Decision; supersede "none yet cited"; keep both counts |
| R2-21 | Skilling reports reach, not effect | 423–430 | holds | `chiang2022exploring` p. 159; N4 entries 22–23; `connellpensky2026can` (abstract) as counter | Keep confined to "those who most need it" |
| R2-22 | *Moffatt* | 464–469 | holds | `moffatt2024air` paras 27–28, 40 | Use it also in §3.3 as the second-party verification source |
| R2-23 | Worked refund case | 402–408, 535–543 | narrower | R2-08, R2-14, R2-16, R2-19 | Pick a case outside art. 22 by construction, or add the EU customer's art. 22 rights and show the architecture adds nothing |
| R2-24 | Word counts, seven principles, 13M views, the "we" | 25–34, 455 | holds | Nadella capture P1–P21 (N7b word check) | Anchor "we" on P17's "Orgs" and mark the reading as the paper's |
