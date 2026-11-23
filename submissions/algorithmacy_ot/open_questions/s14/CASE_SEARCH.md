[Written by Opus (claude-opus-5-5), stage S14c, 2026-11-23]

# S14c: published case for the "counterpart held to account" sentence

**Sentence under test** (`manuscript/intro_5c_2026-11-23/INTRODUCTION_5C.md`, Concern block):

> Where people cannot tell the intermediary's verdict from each other's conduct, they (a) follow the system and lose sight of the counterpart, or (b) hold the counterpart to account for what the system decided, and in either case the platform's discharge of actorhood holds.

**What counts.** For (b): a published case in which a person blames or sanctions the *other human party* for an outcome that the platform produced or co-produced, and the *source itself* says so. Hohenstein & Jung (2020) runs the other way and does not count. For (a): a case of people following the system at the counterpart's expense, with the counterpart in view.

## Verdict

**Keep the sentence, with citations.** Half (b) has two direct cases, and in both the authors themselves attribute the outcome to the platform. The stronger one is peer-reviewed: Muralidhar, Bossen & O'Neill (2022). The other is a 2026 preprint (Meng et al.). Rosenblat & Stark (2016) adds the structural reason: passengers cannot rate the system apart from the driver. Half (a) holds only in a weaker form. Bucher et al. (2021) show workers treating clients as a means of pacifying the algorithm: they avoid clients, ration their outreach, and take on new clients to keep their scores up. They do not show workers "losing sight" of the client. The client stays in view, as an instrument.

**Suggested wording** (marked as Claude's draft, for Roger to accept or reject):

> [C: Where people cannot tell the intermediary's verdict from each other's conduct, they work the counterpart to satisfy the system (Bucher et al., 2021), or they hold the counterpart to account for what the system decided: passengers curse auto-rickshaw drivers for fares the platform raised and hid (Muralidhar et al., 2022), and customers read a stalled tracking dot as a courier's negligence (Meng et al., 2026). In either case the platform's discharge of actorhood holds.]

**Caveat the author should see.** Controlled experiments in service marketing find the opposite tendency when the platform's role is *made visible*. There, consumers shift responsibility onto the platform: Fu, Bai & Gu (2025) call this the "locus-responsibility shift", and in Zheng & Zhu (2026), framing dispatch as algorithm-directed raises the platform's share of blame for a worker's failure. Both were read at abstract level only. They do not refute (b), because the sentence's condition is that people *cannot tell* the verdict from the conduct. They do mean the sentence should keep that condition, and should not read as a general law of blame.

## Candidates

### 1. Muralidhar, Bossen & O'Neill (2022): DIRECT evidence for (b)

- **Record:** Muralidhar, S. H., Bossen, C., & O'Neill, J. (2022). Between a rock and a hard place: Negotiating dependencies and precarity in the on-demand economy. *Computer Supported Cooperative Work (CSCW)*, 31(3), 443–486. https://doi.org/10.1007/s10606-022-09434-7 (volume, issue and pages confirmed against Crossref).
- **Read depth:** full text through §5.2.4. I read 79k of 137k characters of the author accepted manuscript via Consensus `get_full_text`. The manuscript has no VoR page numbers, so the locators below are section numbers. §6 onward was not read. The Springer PDF was blocked to curl.
- **Passages (§5.2.2, "How platform mediation impacts driver-passenger interaction"):**
  - Driver P11: "ever since Ola hiked the fares, customers behave very differently […] they think that whatever they are paying is pocketed by me. […] They curse us, saying we are all the same."
  - Driver P11 on platform-routed fares: "we get the blame if the fare goes up (from the initial estimate), because we followed their directions [...] Then, they complain to Ola."
  - Authors: "Any fees levied or deductions made are not only determined by the platform, but they are also selectively hidden from the customers, leading them to wrongly assume that drivers pocket the entire amount they pay."
  - §2, authors' framing: platform design causes "hostile interactions, blame game, and risk/cost-transference whilst the platform remains unscathed itself."
  - §5.2.3 shows a sanction, not only blame. A dispute arises over a payment mode that the platform locks at booking ("By design, Ola does not allow the customer to change the mode of payment"). The customer "complained about me, citing misbehaviour", and Ola barred the driver until he gave a written apology (driver P13).
- **Does the source attribute the outcome to the platform?** Yes, in the authors' own words: fares and fees are "algorithmically determined by the platform" and hidden from customers.
- **Limits:** 13 auto-rickshaw drivers in Bengaluru and Mysuru. The evidence is the drivers' accounts of customer behaviour, not observation of customers.
- **Strength:** direct evidence. This is the citation the [NEEDS] asks for.

### 2. Meng, Shi, Liu & Chen (2026): DIRECT evidence for (b), but a PREPRINT

- **Record:** Meng, Y., Shi, S., Liu, B., & Chen, H. (2026). When data becomes judgment: Misaligned interpretations and accountability in food delivery platforms. arXiv:2609.39311 [cs.HC], v1, 30 Sep 2026. https://doi.org/10.48550/arxiv.2609.39311. The PDF's running head names *Proc. ACM IMWUT* 10(4), December 2026, but its DOI is a placeholder (`10.1145/nnnnnnn.nnnnnnn`), and a Crossref title search on 23 Nov found no published version. Cite it as a preprint.
- **Read depth:** full text (PDF at `ot_open_questions_local/s14/case/meng_2026/`). The pages below are the preprint's own page numbers.
- **Passages:**
  - p. 9, §4.1.4: "even when structural bottlenecks originate from restaurant backlogs or platform dispatching delays, couriers inevitably absorb the fallout".
  - p. 11, §4.3.2, courier F6: "as soon as users see that, they will have complaints—this is actually a system problem, but in the end I am the one who bears it."
  - p. 15, §5: "When a delivery is delayed by faulty dispatching or kitchen bottlenecks, the infrastructure remains invisible and thus unaccountable; the user perceives only the visible failure of the courier."
  - p. 8, §4.1.2: customers read the algorithm's ETAs as the courier's promise and "immediately attribute the discrepancy to courier negligence".
- **Does the source attribute the outcome to the platform?** Yes. The authors name dispatch logic, ETAs and batching as the cause, and they interviewed both sides: 23 users and 17 couriers.
- **Strength:** direct evidence, the closest fit to the sentence. It is unrefereed, so it can serve as a second citation but not as the only one.

### 3. Rosenblat & Stark (2016): SUPPORTING evidence for (b), structural

- **Record:** Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study of Uber's drivers. *International Journal of Communication*, 10, 3758–3784. No DOI. The OA journal PDF is at ijoc.org (article 4892); an SSRN version exists as 10.2139/ssrn.2686227.
- **Read depth:** full text (PDF and text layer at `ot_open_questions_local/s14/case/rosenblat_stark_2016/`).
- **Passage (p. 3772):** "systematic accountability for the whole interactive process (Leidner, 1999, p. 83) is downloaded onto individual drivers because passengers do not have the option to rate the Uber system in-app separately from their drivers."
- **Does the source attribute it to the platform?** Yes, to the rating system's design. It does not report a passenger blaming a driver for a specific platform decision.
- **Strength:** suggestive. It explains why (b) happens, which suits a "because" clause, but on its own it is not a case.

### 4. Bucher, Schou & Waldkirch (2021): evidence for (a), partial. The pairing needs rewording.

- **Record:** Bucher, E. L., Schou, P. K., & Waldkirch, M. (2021). Pacifying the algorithm: Anticipatory compliance in the face of algorithmic management in the gig economy. *Organization*, 28(1), 44–67. https://doi.org/10.1177/1350508420961531. OpenAlex dates it 2020 (OnlineFirst, 27 Nov 2020).
- **Read depth:** full text of the published OnlineFirst version (pp. 1–24) from the BI/NVA repository (`ot_open_questions_local/s14/case/bucher_2021/`). The page numbers below are OnlineFirst pages. The issue pages, if OnlineFirst p. 1 = issue p. 44, would be about 13→56, 14→57 and 15→58. That mapping is my inference and has not been checked against the issue PDF.
- **What it says about clients:**
  - p. 13: workers curtail outreach and avoid clients: "Avoid clients who have a history of leaving negative feedback if your score is fragile."
  - p. 15: workers "need to focus primarily on receiving positive feedback and ratings from clients, which in turn translate into a positive evaluation by the algorithm"; "While the goals of algorithms and clients might be largely aligned, they are not entirely congruent", since workers "take on new clients to keep [their] scores up" while clients may want long-term relationships.
  - p. 15: workers address the algorithm "both directly and indirectly (via the client)".
- **Does it fit (a)?** Only in part. Workers follow the system, and the client becomes the route to the algorithm. The paper documents a worker who keeps the client fully in view, pleading, overdelivering and holding emotions in check (p. 14). It does not document a worker losing sight of the client. "Lose sight of the counterpart" overstates it. "Work the counterpart to satisfy the system" is what the text supports.
- **Strength:** suggestive for (a) as drafted, and direct for the reworded version.

### 5. Oezdemir, Alizadeh, Benlian & Wiener (2026): SUGGESTIVE, workplace (b)

- **Record:** Oezdemir, F., Alizadeh, A., Benlian, A., & Wiener, M. J. (2026). Caught in the loop: How algorithmic management disempowers frontline supervisors. *Proceedings of ACM FAccT 2026*, 4470–4490. https://doi.org/10.1145/3805689.3812344 (CC BY). Pages are from OpenAlex.
- **Read depth:** full text, first 40k of 53.5k characters, via Consensus. That text has no page numbers. The ACM PDF was blocked to curl.
- **Passage ("The Displaced Decision-Maker", "Responses to Algorithmic Opacity"):** the scheduling system kept rostering an employee who was on approved leave. "We could not figure out why." The authors write that the supervisor "functioned merely as a buffer for employee frustration, unable to offer any rational explanation."
- **Does the source attribute it to the system?** Yes, the error is the scheduling system's. But the employees' blaming of the supervisor appears in the authors' gloss, not in a quotation, and the supervisor is a hierarchical superior rather than a peer counterpart.
- **Strength:** suggestive. Useful only if the paper later extends the claim to workplaces.

### 6. Counter-direction (abstract only): platforms blamed, not counterparts

- Fu, X., Bai, L., & Gu, F. F. (2025). Why platforms become scapegoats: Extending attribution theory in multi-actor service contexts. *Journal of Service Research*. https://doi.org/10.1177/10946705251324611. Abstract: consumers "transfer responsibility for service failures to a platform, even after recognizing the individual provider as the source of the problem" (24,183 complaints plus 4 experiments).
- Zheng, L., & Zhu, Y. (2026). Who is to blame? How order dispatch information shapes consumer responses to worker-caused service failures. *Asia Pacific Journal of Marketing and Logistics*. https://doi.org/10.1108/apjml-09-2025-1986. Abstract: consumers respond more negatively to the platform when dispatch is framed as algorithm-directed, an effect mediated by attribution of responsibility to the platform.
- **Bearing:** neither is a case of (b). Both show that the direction of blame depends on whether the platform's role is visible, which is the sentence's own condition. Read at abstract level only.

### Checked and rejected

- Chan, N. K. (2019). The rating game: The discipline of Uber's user-generated ratings. *Surveillance & Society*, 17(1/2), 183–190. https://doi.org/10.24908/ss.v17i1/2.12911. Full text read. At p. 186, passengers give "average" three or four stars without knowing that 4.6 is the platform's deactivation threshold. The sanction is the platform converting the passenger's judgment. The passenger does not blame the driver for a platform outcome. **No.**
- Acheampong (2021, 10.1016/j.cstp.2021.01.008), Ghana ride-hailing. Abstract and Consensus excerpts mention passenger–driver "clashes" over "intransparent" fare pricing, but the excerpts point to drivers charging extra cash, so the platform's role is unclear. **No** at this read depth.

## Not accessible (not bypassed)

| Item | DOI | Why it mattered | Status |
|---|---|---|---|
| Lee, Kusbit, Metsky & Dabbish (2015), "Working with machines", CHI, 1603–1612 | 10.1145/2702123.2702548 | Uber/Lyft drivers and passengers under algorithmic assignment | Closed (S2); ACM PDF blocked to curl |
| Raval & Dourish (2016), "Standing out from the crowd", CSCW, 97–107 | 10.1145/2818048.2820026 | Driver ratings and passenger expectations | Closed (S2); ACM PDF blocked to curl |
| Sun (2019), "Your order, their labor", *Chinese Journal of Communication* 12(3), 308–323 | 10.1080/17544750.2019.1583676 | Chinese couriers, algorithmic time limits and customers | Paywalled |
| Chan (2022), "Algorithmic precarity and metric power", *Big Data & Society* 9(2) | 10.1177/20539517221133779 | Workers, customers and metrics across three platform types | Gold OA, but SAGE returned HTML to curl, and Consensus has no OA copy. Retry by browser. |
| Deng, Tang & Lai (2025), *Information Technology & People* 39(2), 1091–1115 | 10.1108/itp-12-2023-1201 | Couriers preventing negative reviews; abstract calls for evaluation that accounts for "uncontrollable factors" | Paywalled |
| Moon, Wei & Miao (2019), *International Journal of Hospitality Management* 81, 239–248 | 10.1016/j.ijhm.2019.04.026 | Airbnb host–guest complaints, attribution | Paywalled |
| Muralidhar et al. (2022), VoR PDF | 10.1007/s10606-022-09434-7 | VoR page numbers for candidate 1 | Springer blocked to curl; AAM read via Consensus |

**Store note.** Several failed downloads left HTML stubs named `*.pdf` in `ot_open_questions_local/s14/case/`: chan_2022, huang_2022, wood_lehdonvirta_2022, oezdemir_2026, lee_2015, raval_dourish_2016, muralidhar_2022. My delete command was refused, so they are still there. They are not papers.

## Query log

| # | Tool | Query | Useful hits |
|---|---|---|---|
| 1 | Scholar Gateway `semanticSearch` | Do customers blame gig workers … for outcomes caused by the platform algorithm … | ACCESS_DENIED |
| 2 | Consensus | customers blame gig workers for algorithmic platform decisions ratings misattribution (30) | Chan 2022; Fu et al. 2025; Zheng & Zhu 2026; Rosenblat et al. 2017 |
| 3 | Consensus | Pacifying the algorithm anticipatory compliance online labor platforms (5) | Bucher et al. record |
| 4 | Consensus | Uber passengers rate drivers low for surge pricing or app navigation route errors beyond driver control (20) | none direct |
| 5 | Consensus | food delivery customers blame courier for late delivery caused by platform dispatch algorithm (20) | **Meng et al. 2026**; Sun 2019 |
| 6 | Consensus | attribution of blame to service provider versus platform in sharing economy service failure (20) | Fu et al. 2025; Zheng & Zhu 2026; Kim et al. 2021 (counter-direction) |
| 7 | OpenAlex `/works?search=` | eight title searches (Rosenblat & Stark; Raval & Dourish; Lee et al.; Sun; Chan 2022; Bucher; Rosenblat et al. 2017; Meng) | records and OA links |
| 8 | OpenAlex `/works/doi:` | locations for Bucher, Chan 2022, Huang 2022 | Bucher repository handle 11250/2721045 |
| 9 | NVA API `search/resources` and `filelink` | "Pacifying the algorithm" | Bucher published-version PDF |
| 10 | Consensus | gig workers receive negative ratings from customers for problems caused by the app or platform, unfair ratings (20) | Chan 2019; Deng et al. 2025; Liu et al. 2025 |
| 11 | Consensus | workers blame coworkers or managers blame employees for outcomes of algorithmic scheduling … (20) | **Oezdemir et al. 2026** |
| 12 | Consensus | Airbnb hosts guests conflict over platform policies reviews misattributed responsibility (15) | Moon et al. 2019; Farmaki & Kaniadakis 2020 (not case-level) |
| 13 | OpenAlex `/works/doi:` | seven DOIs (Chan 2019, Oezdemir, Lee, Raval, Sun, Deng, Moon) | OA status |
| 14 | Semantic Scholar `/paper/DOI:` | five DOIs | Lee and Raval closed; Oezdemir and Chan 2022 OA |
| 15 | Consensus `get_full_text` | Chan 2022; Oezdemir 2026 | Chan blocked; Oezdemir read (40k chars) |
| 16 | Consensus | ride-hailing drivers say passengers blame them for fares, routes or cancellations set by the app (15) | **Muralidhar et al. 2022**; Acheampong 2021 |
| 17 | Consensus | workers absorb customer anger for algorithmic decisions they did not make … (15) | no new candidates |
| 18 | Consensus `get_full_text` | Muralidhar et al. 2022 (two parts) | §§1–5.2.4 read |
| 19 | Crossref | Meng title search; Muralidhar DOI | Meng not published; Muralidhar 31(3) 443–486 confirmed |

Every reference above comes from a record or text retrieved in this session. Nothing was cited from memory.
