# B5 — The law in November 2026 and the counter-case

Agent-drafted. The author has not reviewed it and none of the text is his.

Agent B5 (opus), 18 Nov 2026. Cap 6 cards (PLAN §10 cuts 1-5). Log: `B5_law_and_counter_case.log.md`.

## 1. Counts by read status

| source_basis | Cards |
|---|---|
| full-text | 3 (`maas2023ai`, `olghamm2026urteil`, `visa2025trusted`) |
| partial-text | 3 (`kleinberg2018human`, `narayanan2025ai`, `arbel2022contracts`) |
| abstract | 0 |
| secondary | 0 |
| **Total** | **6** |

Not carded: Sunstein 2019 (closed; derivative of Kleinberg), Sunstein 1993 (library only), Ashkenazi 2025 (NOT FOUND,
Scout B), Microsoft source for counter-argument (7) (none found). Law texts: no new card (texts unchanged or already carded).

## 2. Entries

| Citekey | Record verified by | Read status | Bearing by STRUCTURE section |
|---|---|---|---|
| `maas2023ai` | Crossref 10.2139/ssrn.4612468; publisher page dates (pub. 29 Oct 2023, mod. 21 Feb 2026) | full-text (Wayback capture of law-ai.org) | 1.2, 2.3, 5: narrows (frame must say what it occludes); counter |
| `kleinberg2018human` | Crossref 10.1093/qje/qjx032 (QJE 133(1):237-293) | partial: NBER WP Feb 2017, abstract + pp. 6-8 | 6-automation: contests; 4.4-stop: silent |
| `narayanan2025ai` | Knight Institute page (15 Apr 2025); not in Crossref | partial: opening, five sub-sections of Parts I-III | 4.3, 6-automation, 6-scale: contests; 2.3: supports (history as guide) |
| `olghamm2026urteil` | NRW official database header (date, Az., ECLI, "rechtskräftig") | full-text (paras 1-87, 104, 118) | 4.2, 4.4-loss, 6-smartreader: narrows A8/the presumption-of-reading pairing; 4.4-contest: standing only via association |
| `arbel2022contracts` | Publisher PDF header (GWLR 90(1), Feb 2022, p. 83); VUW record | partial: pp. 83-84, 121, 125, 134-135, 140-141, 146 | 6-smartreader: contests; 3.4/4.4-loss: narrows, but supports "who runs the reader" |
| `visa2025trusted` | GitHub API (owner visa, created 10 Oct 2025, commit 16d59bd) | full-text (README) | 4.4-medium, 4.4-record, D03: contests A5's "AP2 alone"; counterparty is a merchant |

## 3. Part 1 — the law as of 18 November 2026 (official texts)

| Provision | Applies from (Nov 2026 status) | Protects | Bites | Procedure run by | Card / source |
|---|---|---|---|---|---|
| GDPR art. 22 | In force since 25 May 2018, **unchanged**. Commission proposal COM(2025) 837 (procedure 2025/0360(COD)) would amend it; EP Legislative Observatory, fetched 18 Nov 2026: "Awaiting committee decision" (committee draft report PE786.818, 22 Jun 2026). No adopted act | Data subject subject to a solely automated decision with legal or similarly significant effect | 22(1) prohibition in principle (before); 22(2)(a) contract exception, then 22(3) human intervention, view, contest (after) | Controller; DPA on complaint | `eu2016gdpr`; B5/gdpr_omnibus_status (OEIL page) |
| AI Act art. 4 | Applies (Chapter I from 2 Feb 2025); **text replaced** by Omnibus 2026/1744: providers and deployers "shall take measures to support" literacy of staff; "does not require ... any specific level" | Staff and persons operating AI for the provider/deployer, "considering" persons acted on | Before (training) | Provider/deployer | `euomnibus2026` |
| AI Act art. 26(11) | **2 Dec 2027** (Annex III systems): art. 26 sits in Chapter III Section 3, which Omnibus art. 113(c) defers; **not in application in Nov 2026** | Natural persons subject to Annex III high-risk decisions (to be informed) | At/before decision | Deployer | `eu2024aiact`, `euomnibus2026`; B0 aiact_official line 868 |
| AI Act art. 50 | 2 Aug 2026 (general date); art. 50(2) marking for generative systems placed on the market before 2 Aug 2026: **2 Dec 2026** (new art. 111(4)); art. 50(7) codes of practice rewritten | Natural persons interacting with an AI system (50(1)); recipients of synthetic content | At interaction | Provider (50(1)-(2)); deployer (50(3)-(4)); market surveillance | `euomnibus2026` (art. 1 points 20, 39); not separately carded |
| AI Act art. 85 | 2 Aug 2026 | Any natural or legal person (complaint) | After | Market surveillance authority; complaint is a surveillance input only | `eu2024aiact` |
| AI Act art. 86 | 2 Aug 2026 in law, but it attaches to decisions based on Annex III high-risk systems, whose obligations apply from 2 Dec 2027 | Affected person, adverse legal or similarly significant effect | After (explanation) | Deployer; residual to other Union law (86(3)) | `eu2024aiact` |
| California CCPA ADMT regs (11 CCR §§ 7200-7222) | 1 Jan 2027 for existing uses (§ 7200(b)) | Consumers, "significant decisions" (finance, housing, education, employment, health); not refunds | Pre-use notice (before); opt-out or human appeal; access to logic (after) | Business; CPPA/AG | `cppa2025text` (pending) |
| Colorado SB 26-189 | 1 Jan 2027 | Consumers, consequential decisions | Notice before (may be a public posting); explanation within 30 days and human review "to the extent commercially reasonable" (after) | Deployer; AG exclusive; no private action | `colorado2026automated` (pending) |
| Court decisions 2025-26 holding a firm to its AI's statements | OLG Hamm 12 May 2026, 4 UKl 3/25, final: chatbot statements are the operator's own commercial acts; consumer has no duty to fact-check (para 104). *Moffatt* (2024) remains the individual-claim precedent | Consumers (collectively) | After | Qualified consumer association; court injunction | `olghamm2026urteil` (new); `moffatt2024air` |

Not found: any 2025-26 merits decision holding a firm liable for what an autonomous agent *did* (as opposed to said).
LG München I's 28 May 2026 interim injunction on Google AI Overviews was seen only in secondary reports and not opened.

## 4. Part 2 — the counter-case, one entry per argument

| # | Counter-argument | Best source carded | Strongest form | Strikes | What the paper would have to concede |
|---|---|---|---|---|---|
| 1 | Deployed designs already give the person acted on a record, envelope or brake | `visa2025trusted` (with `google2026agentic`, AP2) | Two payment networks/platforms ship per-request, signed, operation-bound authorisation the counterparty verifies before acting; the envelope is declared toward the person acted on, by a third party, not by the deployer | 4.4 rows 1-3; A5 ("AP2 shows the alternative"); D03 | That D03 is not a single exception but a pattern in agentic payments; the paper's claim must be restricted to non-payment agents acting on consumers (refund, service, hiring), where I found no such design. Both protect merchants against fraud, not consumers |
| 2 | Automated decisions are less arbitrary than the human ones they replace | `kleinberg2018human` | At equal release rates an algorithm cut crime ~25%, or jailed ~42% fewer at equal crime, while reducing racial disparities; judges' deviations are noise (pp. 6-7) | 6-automation; 3.2 gate pairing | That the gate held by an agent may be fairer than the gate held by an official; the paper's complaint must be about who holds the record, brake and standing, not about the quality of the decision. Limits: one narrow prediction task; WP copy only |
| 3 | AI is normal technology; existing institutions absorb its risks | `narayanan2025ai` | High-consequence uses diffuse slowly under regulation; new uses "can and must" be regulated as they arise; operator controls (audits, circuit breakers, reversibility) and market discipline keep humans in control | 4.3 (treats Nadella's controls as adequate); "transition" framing in Intro and 1.1; 6-scale | That operator-side controls are the mainstream answer and that the case for new duties rests on the person acted on being outside them. The essay itself lists concentration of power and organisations pursuing their interests as the main normal-AI risks, and reasons from the Industrial Revolution |
| 4 | Arguing from historical analogy misleads AI governance | `maas2023ai` | Every analogy foregrounds some features and occludes others; unreflexive analogies entrenched in law cause "governance misspecification"; the aim is not the "correct" metaphor | 1.2, 2.3, 5 | That the literacy frame must state what it occludes (speed, adaptation, multi-agent interaction) and be one lens among others. Maas does not argue against analogy and does not discuss literacy; it narrows, it does not refute. Sunstein 1993 not read |
| 5 | The "smart reader" relieves the reading | `arbel2022contracts` (and `arbel2025how`, abstract) | Lack of reading "may be a technological challenge that is increasingly solved" (p. 134); regulation might shift to raising adoption (p. 135) | 6-smartreader; 3.4 and 4.4 "who carries the loss" | That the burden of reading can move to a machine. The source's own risks support the paper's answer: firms can attack readers (p. 121), platforms may supply the score (p. 121), unequal access makes a stronger duty to read regressive (p. 141). Ashkenazi 2025 NOT FOUND |
| 6 | Replies to Nadella's post since 24 Oct 2026 | none | — | — | I found no reply, defence or critique dated after 24 Oct 2026 in WebSearch (two queries); coverage found is all 10-12 Oct (Pillitteri, cryptobriefing, digit.in, androidheadlines, windows-faq.de). Scholarly indexes not re-run |
| 7 | Microsoft gives the affected person something the paper says it does not | none | — | — | I found no Microsoft document giving the person acted on a record, brake or standing; one search returned only admin controls (block agents) and a community playbook. B1's facet is the place to check |
| — | The law already holds firms to their AI's words | `olghamm2026urteil` | A second legal order attributes chatbot statements to the operator despite autonomy and the black box (paras 70-73) and rejects a consumer duty to fact-check (para 104) | 4.2; 4.4-loss; O02 | That the "presumption of reading" pairing fails for misstatements in two jurisdictions. What stands: the misled person received nothing; standing ran to an association; the remedy was forward-looking |

## 5. What each STRUCTURE section in scope can rest on (this facet's cards)

- **1.2 / 2.3 (why literacy; analogy method):** `maas2023ai` (full) narrows; `narayanan2025ai` (partial) supports reasoning from past technological revolutions.
- **4.2 (remedies on offer):** law table above; `olghamm2026urteil` (full) adds a consumer-protection route.
- **4.3 (what Nadella gets right):** `narayanan2025ai` (partial) treats operator controls as the right model.
- **4.4-medium / D03:** `visa2025trusted` (full README) plus AP2: envelope toward the counterparty exists in payments.
- **4.4-record:** `visa2025trusted` partial record for the merchant; nothing for consumers.
- **4.4-stop:** UNSUPPORTED by this facet: no source gives the person acted on a brake.
- **4.4-contest:** `olghamm2026urteil`: standing only via a listed association.
- **4.4-loss:** `olghamm2026urteil`, `arbel2022contracts` (partial).
- **6-automation:** `kleinberg2018human` (partial, WP), `narayanan2025ai` (partial).
- **6-smartreader:** `arbel2022contracts` (partial), `olghamm2026urteil` para 104.
- **6-scale:** `narayanan2025ai` (human-in-the-loop "rubber stamp").

## 6. Claims in STRUCTURE.md, ARGUMENT_AND_OUTLINE.md or the ledger that the sources contradict

1. **STRUCTURE 4.2 and ARGUMENT A8** list AI Act art. 26(11) among the person's present rights. Art. 26 is in Chapter III Section 3; Omnibus 2026/1744 art. 1 point (40)(b) moves that section to 2 Dec 2027 (Annex III). In November 2026 art. 26(11) does not apply. Art. 86 attaches to Annex III high-risk systems and is affected in practice for the same reason. Ruling 9 records the deferral for Chapter III but A8 was not updated.
2. **ARGUMENT A5** ("AP2's mandate ... shows the alternative can be built") reads as a single exception. `visa2025trusted` is a second (Oct 2025). A5's "one move" claim stays; the "only AP2" implication does not.
3. **ARGUMENT A8 / N6 Q4 ("Moffatt adds a consumer case")**: no longer the only case. `olghamm2026urteil` paras 70-73, 104 reach the same result in Germany under unfair-competition law.
4. **ARGUMENT A8 "Arbel and Becher (abstract)"** and ruling 16: the 2022 article is now read in part (`arbel2022contracts`); its pp. 121 and 141 support the paper's "who runs the reader" answer.
5. **Scout B, row `ashkenazi2025nore`**: says DOI 10.1017/9781009279079.019 is Elvy and Kim's. Crossref (18 Nov 2026) lists Arbel and Becher, matching the existing card `arbel2025how`. Scout row `arbel2022smart` MISMATCH: the lead (2022) was right; the article is 90 Geo. Wash. L. Rev. 83 (2022).
6. **Internal inconsistency in Kleinberg WP**: abstract 24.8%/42.0% vs p. 6 24.7%/41.8%. Cite the QJE version's figures only after opening it.

## 7. Gaps and blocks

| Item | Block | Where a library user would find it |
|---|---|---|
| Kleinberg et al. 2018, QJE version of record | Not tried (WP read instead) | Oxford Academic / JSTOR |
| Sunstein 2019, Social Research 86(2):499-511 | Closed (MUSE); no repository copy (OpenAlex, DASH) | Project MUSE; SSRN 3300171 in a browser; author's OBLB blog version (Jan 2019) is open |
| Sunstein 1993, "On Analogical Reasoning", 106 Harv. L. Rev. 741 | Not attempted (budget) | JSTOR; HeinOnline |
| Maas 2023, PDF version | law-ai.org Cloudflare; SSRN 403 | law-ai.org in a browser (wp-content PDF); read via Wayback HTML instead |
| Ashkenazi 2025 | NOT FOUND (Scout B: Crossref, OpenAlex, WebSearch) | — |
| Visa TAP press release (usa.visa.com releaseId 21716) | Script shell, no text | Browser |
| OLG Hamm press release 16/26 | HTTP 410 | Court site archive |
| LG München I, 28 May 2026 (Google AI Overviews) | Not opened (secondary only) | Bavarian court database (gesetze-bayern.de) |
| Replies to Nadella after 24 Oct 2026 | Two WebSearch queries only; scholarly indexes and X not searched | Google Scholar, X |
| Narayanan and Kapoor Part IV (policy) | Not read (page budget) | Same local HTML |
