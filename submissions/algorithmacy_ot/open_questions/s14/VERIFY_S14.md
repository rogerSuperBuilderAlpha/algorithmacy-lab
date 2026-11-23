[Written by Opus (claude-opus-5-5), stage S14d, 2026-11-23]

# S14d: independent verification of GAP_SEARCH.md, VERIFY_INTRO.md and CASE_SEARCH.md

I wrote none of the three files. **Method.** For quotations, I ran `pdftotext` on every PDF in `ot_open_questions_local/s14/` and split the output into pages. I used the OT `_paged.txt` layers for Schoeneborn, Stark and Hinds. A checker (Python `-I`) matched each quotation in two ways: strict (quote marks and dashes normalised, whitespace collapsed, line-break hyphens joined) and loose (letters and digits only). It then reported the page. I resolved every loose match and every miss by reading the text. Abstract-only quotations were checked against the Crossref abstract or, where Crossref has none, the OpenAlex abstract. Every DOI went to `api.crossref.org/works/<doi>`. The non-Crossref DOIs went to DataCite, doi.org and the arXiv API. I made one new fetch: the open-access accepted manuscript of Muralidhar et al. (2022), from the Aarhus Pure file path (`pure.au.dk/ws/portalfiles/portal/366985319/…Accepted_manuscript.pdf`, User-Agent `ot-oq-research/1.0`). It sits in my scratchpad, not in the store. Its printed page = PDF page − 1.

Result key: **exact** · **fixed** (correct text given) · **wrong** · **unverifiable**.

---

## 1. GAP_SEARCH.md (S14a)

### Quotations

| Item | Check | Result | Note |
|---|---|---|---|
| Row 1 Buhmann et al. 2021 | OpenAlex abstract | exact | |
| Row 2 Schüßler, Maric & Dobusch 2026, pp. 3–4 | `gap/schussler2026` PDF | exact | Runs across the page break, pp. 3–4 |
| Row 3 Fu et al. 2025 | Crossref abstract (full) | exact | |
| Row 4 Zheng & Zhu 2026 | Crossref abstract | exact | Four studies, n = 839, confirmed |
| Row 5 Ketron & Mai 2020 | OpenAlex abstract | exact | "two experimental studies" confirmed |
| Row 6 Davidson et al. 2026 | Crossref abstract | exact | |
| Row 7 Meng et al. 2026, p. 15 and p. 8 | `case/meng_2026` PDF | exact, pages correct | |
| Row 8 Curchod et al. 2020 | Crossref abstract | exact | |
| Row 9 Chan 2022 | Crossref abstract; full text now in `chrome/chan2022` | exact | Read depth is now "full text" (see §4) |
| Row 10 Wang et al. 2024 | OpenAlex abstract | exact | |
| Row 11 Rahman et al. 2024, preprint p. 52 | `gap/rahman2024` PDF (83 pp.) | exact, p. 52 | |
| Row 12 Alizadeh et al. 2024 | Crossref abstract | exact | |
| Row 13 Hirsch et al. 2026 | Crossref abstract | exact | N = 693 confirmed |
| Row 14 Scolari et al. 2026, PDF p. 21 | `gap/scolari2026` PDF | exact, p. 21 | |
| Row 15 Leonardi 2025 | OpenAlex abstract | exact | "strategic attribution processes" is in the abstract |
| Row 16 Xiao et al. 2026, p. 1 | `gap/xiao2026` PDF | exact | |
| Row 17 Eom et al. 2026, p. 16 | `gap/eom2026` PDF | exact | |
| Row 18 Beckers & Teubner 2023 | Crossref abstract | exact | Attribution is wrong (see Claims) |
| Row 19 Laapotti & Raappana 2022 | Crossref abstract | exact | |
| Row 20 Öztürkcan 2026 | OpenAlex abstract | exact | |
| Row 21 Bujold et al. 2026 | Crossref abstract; full text now in `chrome/bujold2026` | exact | |
| Row 22 Kelkar 2017 | Crossref abstract | exact | |
| Row 23 Wood et al. 2021 | Crossref abstract | exact | |
| Row 24 Vallas & Schor 2020 | Crossref abstract | exact | |
| Row 25 Stark & Pais 2021 | not in Crossref (DataCite DOI); abstract not fetched | unverifiable here | |

### Bibliographic records (Crossref unless stated)

| Item | Result | Note |
|---|---|---|
| Rows 2–24 DOIs | all resolve; authors, year, title and venue match | Minor: Crossref spells "Schuessler, Elke", "Ozturkcan, Selcen" and "Establés, María-José" (the file has "Estables"). Fu et al. is now *JSR* 29(1), 97–114 (online 2025, issue 2026). Ketron & Mai issue 2022 30(1), 3–21. Wood et al. issue 2023 38(2). Wang et al. issue 2026 37(5). |
| Row 1 Buhmann, 10.5465/ambpp.2021.14936abstract | fixed | The DOI **does** resolve in Crossref, so "Crossref has none" means no abstract, not no record. Crossref title: "Player or platform? How metaphors affect the attribution of actorhood to new forms of organizing", *AoM Proceedings* 2021(1), 14936. |
| Row 7 Meng et al., arXiv:2609.39311 | exact | The arXiv API returns the record. Title matches. Authors are Yibo Meng, Shuoning Shi, Bingyi Liu and Hongkai Chen. v1 is dated 30 Sep 2026. The comment reads "27 pages, to be published at ACM IMWUT". 10.48550/arXiv.2609.39311 resolves through doi.org to arXiv. Crossref has no record, as expected for a DataCite DOI. A Crossref title search found no published version. |
| Row 25 Stark & Pais, 10.6092/issn.1971-8853/12221 | fixed | Not in Crossref; DataCite has it ("Algorithmic Management in the Platform Economy", *Sociologica*), publicationYear 2021, issued 29 Jan 2021. Stark & Vanden Broeck cite it as 2020 (vol. 14(3)), and VERIFY_INTRO G4 follows them. Use one year across files. |
| Eom et al. arXiv 2604.06381; Xiao et al. arXiv 2505.20623 | exact | The arXiv API confirms both titles and the Eom authors |
| Snowball counts | not re-done | OpenAlex today gives Schoeneborn et al. 2026 `cited_by_count` 0 (Semantic Scholar 0), which confirms the claim. Stark & Vanden Broeck give 148, not 127. Counts drift and `cited_by_count` ≠ the listed works, so this is a note, not an error. |

### Substantive claims

| Item | Check | Result | Note |
|---|---|---|---|
| Row 1 / §3.2 Buhmann: "platform"/"app" lower collective-actorhood attributions | abstract | exact in substance | The abstract states the finding as anthropomorphic metaphors *raising* attributions, with "platform or app" as the contrast. It says "four empirical studies", not "four experiments". |
| Row 2 / §1.3 Schüßler et al.: platforms present as neutral intermediaries and obscure actorhood; users attribute nothing | full text | exact | Also "self-presentation as a neutral intermediary" and "positioning themselves as neutral intermediaries … their actorhood and accountability" (conclusion). The case is YouTube, from secondary data. |
| Row 3 / §4.1 Fu et al.: responsibility moves to the platform even when the provider is recognised as the cause | full Crossref abstract | exact | Moderators: high (vs. low) intermediation, severe failures, encounter (vs. core) issues. |
| Row 4 / §4.3 Zheng & Zhu: algorithm-directed framing raises the platform's responsibility | abstract | exact | Mediation in Studies 2–3; moderated by power distance. |
| Row 18: Beckers & Teubner (2023, *JOLS*) "probably the 'legal theory' Stark and Vanden Broeck mention (p. 14)" | Stark reference list | **wrong** | Stark & Vanden Broeck p. 14 cite **Beckers, A., & Teubner, G. (2021). *Three liability regimes for artificial intelligence: Algorithmic actants, hybrids, crowds*. Bloomsbury.** The 2023 article is a related but different work. |
| Row 9 Chan 2022 "abstract (download blocked)" | `chrome/chan2022` | fixed | Read depth is now full text: 50 interviews with ride-hail, delivery and TaskRabbit workers only. |
| §4.5: "Chan (2022), Curchod et al. (2020) and Meng et al. (2026) do follow decisions to both sides" | full texts | **wrong for two of three** | Chan interviewed 50 workers only, and Curchod 77 sellers only. Both report the counterpart through the worker's account. Only Meng interviewed both sides (23 users, 17 couriers). Lee et al. (2015, 21 drivers + 12 passengers) also qualifies. The point stands (the intro must stay scoped to "both conversations"), but the evidence for it needs correcting. |
| Row 21 Bujold: dyadic intermediary | full text | exact | No client or customer appears in the model. |
| Row 7 Meng | full text | exact | |

---

## 2. VERIFY_INTRO.md (S14b)

### Quotations (OT layers, `reads/` PDFs, `chrome/roulet2020`)

| Item | Result | Note |
|---|---|---|
| O2, O3, G1 (pp. 6, 13), G2 p. 11, G3 (p. 1, p. 14), G4 (p. 14, p. 5), G7 p. 1, G8 (all three, p. 4), X1 p. 14, X2 p. 10 (incl. "for new organizational forms, research has shown that"), X4 p. 14 (incl. "(Vesa & Tienari, 2022, p. 1137)?"), X5 p. 14, X6 p. 16, C5 p. 7, C6, C7, K7 p. 14, K3 p. 15, K5 p. 4, K6 p. 9 | exact, pages correct | In G2 and G7 the source's double quotes become single quotes inside the quotation, the normal nesting convention. |
| van Houwelingen & Stoelhorst: abstract p. 297, p. 298, p. 302 (both), p. 313 | exact, pages correct | UvA PDF page + 295 = printed page |
| "trustful stakeholder relations" (§2.3) | fixed | The phrase is not in van Houwelingen & Stoelhorst. It is Schoeneborn et al.'s ("negative implications for building trustful stakeholder relations", p. 10). Attribute it to them. |
| Karunakaran et al.: abstract, AAM p. 40, p. 27, p. 7 | exact | Locators are AAM PDF pages, as stated. |
| Curchod et al.: abstract, pp. 10, 19 (×2), 22, 38, 39 (×2) | exact | Locators are the AAM "Page n of 55" stamps, as stated. |
| Elish p. 40 (two segments) | exact | |
| Haase et al. pp. 650 (×2), 651 (×2), 668 | exact | Table 1 gives "self-portrayal" as "selfportrayal" because of a line-break hyphen. |
| Roulet & Pichler abstract (two quotes) | exact | |
| Roulet & Pichler p. 9 block quote reproduced by Schoeneborn et al. p. 11 (marked unverified in S14b) | **now verified, p. 9** | Exact except two changes Schoeneborn et al. made: the original reads "(p. 1617)", which they render "(2016, p. 1617)", and the original's single quotes become double. It does not affect the intro. |
| Vergne & Wry, Stelmaszak, Cameron, Orlikowski & Scott abstract quotes | exact (Crossref abstracts) | |

### Bibliographic records

All 13 records in the "Sources read" table match Crossref for authors, year, title, venue, volume and pages. That includes Karunakaran (2022) *Org Sci* 33(3), 1188–1211, 10.1287/orsc.2021.1469, and Vesa & Tienari, *Organization* 29(6), 1133–1145. One fix: Roulet & Pichler and Stark & Pais are covered above.

### Substantive claims

| Item | Check | Result | Note |
|---|---|---|---|
| **(a) C2 Karunakaran et al. 2022: "about social media commentary, not automated systems"** | full AAM, read for algorithm/automation/deflect/front-line | **S14b's ruling stands: the author's sentence is not supported** | The study covers 911 and hotels responding to Twitter and TripAdvisor commentary. "Algorithm" occurs once in the findings: TripAdvisor's Popularity Index as a feature of the setting (AAM p. 13). "Deflecting" appears only in the prior-work list (p. 7). The study does show pressure landing on staff: managers read out reviews "that call out staff members by name or position" (AAM p. 31), call-takers act "overcautiously" (p. 27), and actors grow "unsure about what they are held accountable for" (pp. 5, 39). So "onto the people doing the work" has partial support, for *crowd commentary*, not for automated systems that deflect. Re-source or recast. Elish (2019) or Lee et al. (2015, see §4) fit the automated-system half. |
| **(b) van Houwelingen & Stoelhorst: experience, not agency** | full text | exact | Study 1, agency F(1, 123) = .04, p = .834, firms "about equally agentic" (p. 302). Experience was lower for the digital firm (p. 302). On p. 313 the authors say their antecedent, like those of two earlier studies, "only affects the attribution of experience, and not the attribution of agency". The firms are a clothing retailer (Studies 1–2) and an insurance broker (3–4), and the word "platform" does not occur. So X2 is accurate as a quote and X3 is unsupported, as S14b says. |
| Haase et al.: platforms absent from the three drivers (pp. 668–669); platform example only in Table 1 | full text | exact | |
| Roulet & Pichler §2.4 bearing: "blame moves *inside* the organization, from organization to member" | full text now | **fixed** | That describes only half the model. Blame game theory pairs scapegoating (organization → member) with whistleblowing (member → organization) (abstract, pp. 7–9). The paper does not mention platforms or algorithms. |
| C3 Curchod: "completely concealed" overstated | AAM pp. 39, abstract | exact | |
| X1 Stark p. 14 cites Curchod et al. | OT layer | exact | |

---

## 3. CASE_SEARCH.md (S14c)

### Quotations

| Item | Check | Result | Note |
|---|---|---|---|
| Muralidhar et al. §5.2.2, P11 "ever since Ola hiked the fares…" | AAM (new fetch) | exact | AAM printed p. 21 |
| Muralidhar §5.2.2, P11 "we get the blame if the fare goes up…" | AAM | exact as a quote; **gloss wrong** | Printed p. 20. "Their directions" are the *passengers'* directions, not the platform's: "They (customers) sometimes tell us to follow the directions they provide and not the map … if the route changes, then fare changes. Then, they complain to Ola. Ola people ask us why we charged extra." Do not call this "platform-routed fares". The platform's fare recalculation is the cause, and both passenger and Ola blame the driver. It is still (b), but less clean. |
| Muralidhar authors, "Any fees levied … pay." | AAM | exact | Printed p. 21; the source has a footnote marker "5" after "pay" |
| Muralidhar §2 "hostile interactions, blame game …" | AAM | exact | Printed p. 5. It is the authors' own framing. |
| Muralidhar §5.2.3, "By design, Ola does not allow…" and P13 "complained about me, citing misbehaviour" | AAM | exact | Printed p. 23. "Ola barred me from taking any rides. I had to submit a written apology." |
| "algorithmically determined by the platform" | AAM | exact | Printed p. 21. It refers to "surge pricing" and "peak hour charges". |
| Meng pp. 9, 11, 15, 8 | PDF | exact, pages correct | |
| Rosenblat & Stark p. 3772 | PDF | exact | PDF p. 15 = p. 3772 |
| Bucher OnlineFirst pp. 13, 15 (×3) | PDF | exact | "take on new clients to keep [their] scores up" is on p. 15 and also p. 10. The OnlineFirst-to-issue mapping (p. 1 = p. 44) fits the 24-page span 44–67. |
| Bucher p. 14 (pleading, over-delivering, emotions in check) | PDF | exact in substance | "Over deliver, be patient"; "plead with the client not to rate them badly" (p. 14) |
| Chan 2019 p. 186 | PDF | exact in substance, **fixed** | It is a driver's account (Noah), not an observation of passengers. Owen says passengers "don't realize" four stars can cause deactivation. Drivers move responsibility *to the platform* ("reorients the responsibility for oversight to the platform", p. 186). The rejection stands. |
| Fu, Zheng & Zhu abstract quotes | Crossref | exact | |
| Oezdemir et al. 2026 passages | not stored; Consensus text only | unverifiable here | Hybrid OA at ACM, not fetched |

### Bibliographic records

| Item | Result | Note |
|---|---|---|
| Muralidhar 31(3) 443–486; Bucher 28(1) 44–67 (online 2020); Chan 2019 17(1/2) 183–190; Oezdemir FAccT 2026 4470–4490; Fu; Zheng & Zhu; Acheampong 9(1) 302–314; Lee 2015 CHI 1603–1612; Raval & Dourish CSCW 97–107; Sun 12(3) 308–323; Chan 2022 9(2); Deng et al. 39(2) 1091–1115; Moon et al. 81, 239–248 | exact | |
| Meng arXiv | exact | See §1 |
| Rosenblat & Stark SSRN 10.2139/ssrn.2686227 | fixed | Crossref title: "Uber's Drivers: Information Asymmetries and Control in Dynamic Work" (2015). That is an earlier working paper with a different title, not a "version" of the *IJoC* article. Cite the *IJoC* article only. |

### Substantive claims

| Item | Check | Result | Note |
|---|---|---|---|
| **(c) Muralidhar: customers blame drivers for platform-set fees** | AAM, full | exact | Authors: fees are "determined by the platform" and "selectively hidden from the customers, leading them to wrongly assume that drivers pocket the entire amount" (p. 21); P11: "They curse us" (p. 21). 13 drivers, Bengaluru and Mysuru, June–July 2018 (p. 9). The evidence is drivers' accounts. Fix the P11 route gloss (above). |
| **(d) Fu: blame moves to the platform** | abstract | exact | |
| CASE caveat: experiments find platform-blame "when the platform's role is *made visible*" | abstract | **fixed for Fu** | That fits Zheng & Zhu (dispatch framing). Fu's conditions are high intermediation, failure severity and encounter vs. core issues, so "made visible" is S14c's gloss. Fu's consumers also *recognize* the provider as the cause, so they can tell verdict from conduct. That supports S14c's conclusion that Fu does not refute (b). Suggested caveat wording: "…when the platform intermediates heavily or its role is framed as directing the work". |
| **(f) Bucher: clients as instrument, not lost from sight** | full text | exact | The paper also states the triad: "The platform environment is marked by a triadic relationship between algorithm, client and worker" (p. 14, with Fig. 2: the platform "govern[s] access, visibility & reputation" of both worker and client). Its data come from posts in an Upwork community forum, not interviews. |
| Lee et al. 2015 "not accessible" | `chrome/lee2015` | **superseded** | See §4. It is a direct case for (b). |
| Chan 2022 "not accessible" | `chrome/chan2022` | **superseded** | See §4. It has a (b) case. |

---

## 4. The newly fetched texts (`STORE/chrome/`) and the introduction

| Text | Claims the S14 files make | Bears on INTRODUCTION_5C? |
|---|---|---|
| **Lee, Kusbit, Metsky & Dabbish (2015)**, CHI, 10.1145/2702123.2702548 | CASE: Uber/Lyft drivers and passengers. Correct: 21 drivers, 12 passengers (pp. 1603–1605). | **Yes, directly: the strongest peer-reviewed case for the Concern sentence's half (b).** "drivers noticed that passengers misattributed system faults and negative experiences that drivers could not control to drivers themselves, which in turn resulted in lower ratings (e.g., surge pricing, traffic jams, GPS errors etc.)" (p. 1608). Also: "these numeric systems that made drivers accountable for all interactions" (p. 1608). It reports drivers' perceptions, though passengers were interviewed too. It also fits A7 ("ride-hailing") and could re-source part of C2. |
| **Chan (2022)**, *Big Data & Society* 9(2) | GAP row 9 and §4.5; CASE (not accessible) | **Yes, a second (b) case.** Driver Clayton: "you consistently get rated lower on UberPool than you do on UberX, because it's a bad product, not because you're a bad driver … If you miss your airplane because you took UberPool, you're going to one-star your driver, even though it's not the driver's fault" (p. 8). Chan also writes that "customers might misattribute the responsibility of restaurants to workers through their ratings" (p. 7), but the third party there is a restaurant, not the platform. Workers' accounts only. |
| **Roulet & Pichler (2020)**, *OT* 1(4) | S14b §2.4 | Indirect, but one usable concept: "attributional ambiguity … that is, there are multiple ways of attributing responsibility for misconduct to actors" (p. 7). It sits near the Concern sentence's condition ("cannot tell the intermediary's verdict from each other's conduct"), but in a misconduct-accusation setting. Optional. |
| **Bujold, Gaudet & Parent-Rocheleau (2026)**, *OPR* | GAP row 21 | Marginal. "Workers tend to anthropomorphize AM systems due to their managerial functions, attributing intentionality and motivation to them" (p. 13, citing Sherman et al., 2025). This bears on the `[NEEDS]` apex decision (algorithm as an "other-than-human" address) and stands in mild tension with X2's "digitalization can impede anthropomorphization", but it is a secondary citation and concerns the system, not the collective. |
| Fu et al. (2025), abstract only | GAP, CASE | Already handled. It bears on C1 ("lands on the people"), as S14a says. |

---

## 5. Corrections the lead must carry

1. **GAP row 18**: the "legal theory" in Stark & Vanden Broeck p. 14 is Beckers & Teubner (2021), *Three liability regimes for artificial intelligence*, Bloomsbury, not the 2023 *JOLS* article. Remove "probably … not checked".
2. **GAP §4.5**: Chan (2022) and Curchod et al. (2020) interview one side only. Only Meng et al. (2026), and Lee et al. (2015), cover both sides. Restate the evidence. The conclusion (keep the sentence scoped) stands.
3. **GAP row 1**: the Buhmann DOI resolves in Crossref, so change "Crossref has none" to "no abstract in Crossref".
4. **Stark & Pais**: 2020 (as Stark cites, *Sociologica* 14(3)) vs 2021 (DataCite issue date). Use one year across the run.
5. **VERIFY_INTRO §2.3**: "trustful stakeholder relations" is Schoeneborn et al.'s phrase (p. 10), not van Houwelingen & Stoelhorst's.
6. **VERIFY_INTRO §2.4**: Roulet & Pichler is now read. The p. 9 block quote is verified. Blame runs both ways in their model (scapegoating and whistleblowing), not only from the organization to the member. Remove Roulet & Pichler from the "not accessible" table.
7. **CASE, Muralidhar**: the P11 route quotation concerns passengers' directions, not "platform-routed fares". Fix the gloss. AAM printed pages are now available (pp. 5, 20, 21, 23). Read depth is now the full AAM via Aarhus Pure.
8. **CASE caveat**: "made visible" fits Zheng & Zhu, not Fu et al. (intermediation, severity, encounter issues).
9. **CASE, Rosenblat & Stark**: the SSRN DOI belongs to a 2015 working paper with a different title. Drop it, or label it as the earlier paper.
10. **CASE, Lee et al. (2015) and Chan (2022)** are no longer inaccessible. Lee et al. (p. 1608) is a direct, peer-reviewed case for half (b), stronger than the Meng preprint. Chan (p. 8) is a second. The lead should offer both to the author for the `[NEEDS]` slot. Wording stays the author's.
11. **C2 (Karunakaran et al.)**: the S14b ruling is confirmed. The study is about social media commentary, not automated systems. It does show staff named and chastised through reviews (AAM p. 31), so the author can recast to that, or re-source to Elish (2019) or Lee et al. (2015).
12. Spelling and records: Establés (Scolari et al.). Fu et al. is now *JSR* 29(1), 97–114.

Unverifiable here: Oezdemir et al. (2026) passages (Consensus text only); Stark & Pais abstract; Vergne & Wry full text; Stelmaszak full text; Cameron full text.
