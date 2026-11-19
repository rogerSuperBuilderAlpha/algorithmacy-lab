# VERIFY — verifier_2 (rr-2026-11)

Verifier: verifier_2. Date: 2026-11-08. Cards: 30.

Method. I re-fetched every Crossref record (api.crossref.org) and every OpenAlex record on 2026-11-08 and compared them with the card frontmatter and with `literature/references.bib`. I searched for every quoted string in the saved texts under `sources/<citekey>/` with a normalised exact match (case, whitespace, punctuation and hyphenation ignored), and read the hits that failed by hand. Two-column PDFs (Metcalf `m.txt`, Yurrita, van Doorn) and dropped ligatures (Yurrita, Metcalf) needed a chunked hand check; those are marked MATCH where every chunk was found in order. Page locators were derived from form-feed counts in the pdftotext files and checked against the running heads.

For four abstract-only cards I reached the full text through Internet Archive captures of the open-access publisher or repository copies (status 200 at capture time; no challenge was bypassed). Those copies are in my scratchpad only, not in `sources/`: `/private/tmp/claude-501/-Users-ludwitt/90f3ca36-306a-4bfb-a65b-d7960158634d/scratchpad/v2/dl/` (`mw.txt` Martin and Waldman, Springer HTML capture 20240609184742; `pijls.txt` Pijls et al., ris.utwente.nl PDF capture 20240416085854; `sp23.txt` Spektor et al. 2023, ACM PDF capture 20231114160542; `sp25.txt` Spektor et al. 2025, ACM HTML capture 20250719020946). Zientara (ScienceDirect capture) held only the abstract.

No card or other file was edited.

---

## lugosi2009critical
**PASS**
- Identity: Crossref matches (SIJ 29(10), 1465-1478; three authors). No bib entry; correct for a rejected card.
- Read depth: `paper.txt` is the full pre-proof (6,865 words). Full-text honest.
- Quotes: 'is conceived of as essentially pro-business…' MATCH (section 'The development of a critical approach'); 'is broadly concerned with exploring the social, cultural, political and ethical dimensions…' MATCH (same section).
- Claims: three orientations with overlap and Figure 1 confirmed (lines 162-170); eight challenges confirmed (eight subheads under 'Questions and challenges for a critical research agenda'); the pro-business sentence cites Slattery 2002, as the card says.

## lugosi2014hospitality
**PASS**
- Identity: Crossref matches (Hospitality & Society 4(1), 75-92). No bib entry; the card flags that.
- Read depth: abstract; no source folder. Honest.
- Quotes: all four abstract quotes MATCH (OpenAlex and Crossref abstract).
- Abstract-only check: the summary and the notes stay within the abstract. "Its stakeholders are mainly organizational members" is an inference from the abstract's wording; the card hedges it.

## lynch2017mundane
**PASS-WITH-NOTES**
- Identity: Crossref, bib and card match (Annals 64, 174-184). Crossref and OpenAlex hold no abstract; confirmed.
- Read depth: metadata; honest. `verified: verified` sits oddly with a metadata-only read, but the source_basis is explicit.
- Quotes: none from the source. The v4 sentence quoted is verbatim in v4 §2.
- Claim: NOT CHECKABLE, as the card says. The bib note's earlier `readdepth=full` is unsupported in this run.

## lyons2021conceptualising
**PASS**
- Identity: Crossref matches (PACM HCI 5(CSCW1), 1-25). Crossref's title field omits the subtitle; the arXiv title page carries it. No bib entry (held card).
- Read depth: `arxiv.txt` is arXiv 2103.01774v1, same title and authors. Full text.
- Quotes: all five MATCH, and pdf p. 7, 12, 12, 12, 15 are right.
- Claims: agree. The card is right that §5.1.3 and §5.1.4 report what submissions said.

## martinwaldman2022legitimate
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (JBE 183(3), 653-670; online 10 Feb 2022, print 2023). Citekey says 2022; bib and v4 say 2023, as the card notes.
- Read depth: abstract; `sources/` holds a client-challenge page and an error stub. Honest. **I reached the full text** (Springer CC BY HTML, Internet Archive capture of 9 Jun 2024).
- Quotes: four abstract quotes MATCH.
- Drafters' check, v4 §7: "One study compared appeal, oversight, and audit as remedies for an adverse algorithmic outcome: an appeal that reached the decision raised its perceived legitimacy, while oversight and audit lowered it." **PARTLY SUPPORTED; the framing is wrong in two places.**
  - The study compared five governance options, not three: notice, impact assessment, external audit, human in the loop, and "appeals, in which the decision can be appealed by the individual to an internal review board" (Methods, 'Governance').
  - The lowering result is real but relative, and it comes from the condition without an outcome: "offering an appeal process provides a legitimacy dividend for decisions with no outcome or arbitrary factors included (Survey 5)… (β = 4.54, p < 0.01). However, alternative governance mechanisms such as an impact assessment, including a human in the loop, and having the program audited, lower the legitimacy of the decision compared to mere notice. This was a surprise and counter to the hypothesis." (Results, 'Governance and Legitimacy'). So oversight and audit lowered legitimacy *against notice*, not against no governance, and not as "remedies for an adverse outcome".
  - The adverse-outcome result is about appeal only: "for bad outcomes, the use of an appeal process does provide a legitimacy dividend (t = −12.53; p < 0.0001)", and "the dividend did not 'make up' for the penalty of the bad outcome" (Results, 'Outcomes and Governance').
  - Discussion: "The only form of procedural governance that carries a legitimacy dividend is the most robust that we studied: a formal appeal to a human decision maker." That supports "an appeal that reached the decision".
  - A faithful wording would be close to: "of five governance mechanisms, only an appeal to a human review board raised perceived legitimacy, and it softened the penalty for a bad outcome; impact assessment, a human in the loop and audit scored below mere notice."
- The card's abstract-level verdict was correct and appropriately cautious; it should now be upgraded to full text with these loci (the HTML has no page numbers).

## metcalf2023courts
**PASS**
- Identity: Crossref matches (FAccT '23, 1450-1462; Metcalf, Singh, Moss, Tafesse, Watkins; given name **Emnet**). **Bib defect confirmed:** `references.bib` has "Tafesse, Elizabeth". The paper's ACM Reference Format line orders the authors Metcalf, Moss, Singh, Tafesse, Watkins; confirmed.
- Read depth: `mr.txt` (reading order) and `m.txt` are the full NSF PAR copy. pdf p. 1 = p. 1450.
- Quotes: all MATCH with correct pages: 'primary route—and the primary roadblock' p. 1450; 'forum needs its own "forum"' p. 1451; 'structures accountability… obligated to listen' p. 1453; the "Standing" definition p. 1455 (§4.2); 'fear of harm' / 'bare procedural violations' p. 1455; 'Where courts now refuse standing…' p. 1458; US-courts scope p. 1451.
- Claims: agree.

## odekerken2021service
**PASS**
- Identity: Crossref matches the bib (JOSM 33(2), 246-292; online 2021, print 2022).
- Read depth: `t2.txt` is the full QUT accepted manuscript.
- Quotes: all five MATCH at PDF p. 3, 3, 3, 3, 4.
- Claims: agree. I confirm 0 hits for "host"/"hosts" in the text; the "handed the host's role" reading is the authors'.

## okhuysenbechky2009
**PASS-WITH-NOTES**
- Drafters' check (right article?): **Yes.** `~/Downloads/EBSCO-FullText-08_20_2026-4.pdf` and `sources/okhuysenbechky2009/ebsco.pdf` have the same SHA-1 (f9319654…). The PDF is 41 pp. Page 1 carries "The Academy of Management Annals Vol. 3, No. 1, 2009, 463–502", the title "Coordination in Organizations: An Integrative Perspective", Gerardo A. Okhuysen (Utah) and Beth A. Bechky (UC Davis), and the T&F DOI 10.1080/19416520903047533 (the AOM DOI 10.5465/19416520903047533 is its re-registration). The running heads confirm pdf p. n = journal p. 462+n.
- Identity: Crossref matches the bib (3(1), 463-502). Crossref's title field carries a stray chapter prefix "10 ".
- Quotes: all twelve MATCH, and every journal page is right (483, 483, 486, 483, 486, 488, 490, 490, 490, 491, 493, 494).
- Claims: agree. p. 490 reports substitution only between predictability and common understanding ("common understandings can replace predictability and vice versa"); accountability "supports" predictability and is "seemingly additive" with common understanding. The card is right that non-compensability is the authors' inference.
- Note: the critical-notes bullet "Full text should be read before submission — … currently cites it at abstract depth" is stale now that the card is full text.

## nissenbaum1996accountability
**PASS**
- Identity: Crossref matches the card (Sci Eng Ethics 2(1), 25-42). No bib entry (held card).
- Read depth: `author_preprint.txt` is the full 18-page author copy.
- Quotes: all nine MATCH at the stated pdf pages (3, 6, 10, 10, 11, 11, 14, 15, 15).
- Claims: agree, including the "lost unless assigned" versus "stays with the institution" distinction.

## papadopoulos2021violation
**PASS**
- Identity: Crossref matches the bib (IRJ 52(4), 315-330).
- Read depth: full author version.
- Quotes: all MATCH, PDF p. 1. "Using 36 interviews…" sits in the opening paragraph headed 'Introduction', as the card says. The Discussion begins on PDF p. 10.
- Claims: agree.

## parkinson2022online
**PASS**
- Identity: Crossref matches (JSR 25(1), 108-125; online 2021).
- Read depth: abstract; no folder. Honest.
- Quotes: three MATCH (abstract).
- Abstract-only check: nothing beyond the abstract is attributed. The PARTIAL verdict stands.

## pan2025dark
**PASS-WITH-NOTES**
- Identity: Crossref matches (Tourism Management 106, 104994; Feb 2025). No abstract in Crossref or OpenAlex; confirmed.
- Read depth: metadata; honest. v4 claim NOT CHECKABLE.

## parasuraman2000types
**PASS**
- Identity: Crossref matches (IEEE SMC-A 30(3), 286-297; initials only).
- Quotes: four MATCH (OpenAlex abstract).
- Claims: agree; the citation is better as the tradition argued past.

## pijls2017measuring
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (IJHM 67, 125-133).
- Read depth: abstract; `try0.html` is the Twente record page. Honest. **I reached the full text** (published version, ris.utwente.nl PDF via Internet Archive capture of 16 Apr 2024).
- Quotes: three MATCH (abstract).
- Drafters' check, v4 §2: "It also tried two questions about agency, whether the guest had a choice and whether they felt independent, and dropped both when the scale was tested." **SUPPORTED, with one omission.**
  - Studies 1-2 produced an *autonomy* dimension with three attributes: "Having choice", "Independence", "Freedom" (Table 3, p. 129).
  - In the EFA, "Feeling independent" and "Having choice" survived, loading .76 on the comfort factor (Table 4, p. 130). They were dropped at the CFA: "To improve the fit of the model, two items with low loadings were removed one by one (the items of 'feeling independent' and 'having choice')" (§5.2, pp. 130-131).
  - The third autonomy item, "Experiencing freedom", **was kept**: "one variable of the autonomy dimension make[s] up the inviting experiential factor" (p. 130), and it is item 3 of the final scale (Table 5; Appendix: "During my visit I experience freedom").
  - So the two dropped items are right. But v4's follow-on "It tried to measure something next to it, and the questions did not survive" overstates: one autonomy item survived inside "inviting". The source's word is "autonomy", not "agency". Authors decide.

## phillips2024physical
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (SIJ 44(13-14), 919-948; online 2022).
- Read depth: full QUT manuscript.
- Quotes: all MATCH. **LOCATOR-WRONG:** "Interviews were conducted with 30 customers…" is on PDF p. 2, not p. 1 (p. 1 is the QUT cover sheet). The others are right (p. 2, 36, 36, 50).
- Claims: agree. I found no "recogni*", "negotiat*" or "exception" in the text, which supports keeping that clause off Phillips.

## riordan2024digitally
**PASS**
- Identity: Crossref matches (H&S 14(3), 277-299).
- Quotes: three MATCH (abstract).
- Abstract-only check: nothing beyond the abstract is attributed. PARTIAL stands.

## raisch2021paradox
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (AMR 46(1), 192-210).
- Read depth: `t2.txt` is the full published version. pdf p. 2 = p. 192 (pdf p. 1 is the UNIGE cover), so "p. 192" is right. The card says "full-text" while admitting the body was "skimmed, not read line by line". The source supports the label; the reading depth for the body does not quite.
- Quotes: four MATCH (p. 192, abstract).
- Claims: agree; 0 hits for hospitality or host.

## rihova2018customer
**PASS**
- Identity: Crossref matches (Tourism Management 67, 362-375). No bib entry (rejected).
- Read depth: full accepted manuscript, 14,241 words; the text begins at '1. INTRODUCTION' with line numbers.
- Quotes: both MATCH (ms p. 1; ms pp. 1-2) once the line numbers are ignored.
- Rejection rationale: agree.

## santonidesio2021gaps
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (Phil & Tech 34(4), 1057-1084).
- Read depth: `wayback_article.html` / `article.txt` hold the full article with references (13,612 words). Full text.
- Drafters' check, v4 §4 ("Duties differ in what triggers them. Care is owed because someone is in need. Fiduciary duties are owed because someone has been trusted. Governance duties exist because a system creates risk (Santoni de Sio and Mecacci 2021)"): **CONFIRMED — the paper contains no such typology.** In the full article: "fiduciary" 0 hits; "governance" 1 hit, and that one is in a reference title (Stilgoe 2017); "trigger" 1 hit, about culpability triggering "a moral duty… to explain" (an accountability point, not a need/trust/risk scheme); "trust" 2 hits, neither a duty trigger; "care" appears only as "standards of care" and "a culture of care". The v4 §4 attribution is unsupported by this source. The card locates the analogy in REVISION_PLAN §2; the same unsupported attribution is already in v4 §4 (submitted.md line 30).
- Quotes: all nine MATCH. I checked the paragraph locators against the HTML's `<h>`/`<p>` structure. Eight are right. **LOCATOR-WRONG:** "Faultless liability regimes…" is §3.2.2 ¶3 (the 7th paragraph under §3.2 overall), not §3.2 ¶9.
- Claims: agree with all four critical notes.

## shryock2012breaking
**PASS**
- Identity: Crossref matches (JRAI 18(S1); Crossref has no pages). Bib gives S20-S33, which matches the typeset PDF.
- Read depth: full typeset PDF; pdf p. 1 = S20.
- Quotes: all eleven MATCH at the stated pages (S20, S20, S20 abstract, S23, S24, S25, S28, S30 ×4).
- Claims: agree; "host authority is constituted by guest obligation" is not in the text (the card says so).

## spektor2023designing
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (DIS '23, 623-637; ten authors).
- Read depth: abstract; honest. **I reached the full text** (ACM CC BY PDF, Internet Archive capture of 14 Nov 2023; pdf p. 1 = p. 623).
- Quotes: three MATCH (abstract).
- Drafters' check, v4 §4 ("housekeeping systems lock task order and, in their most limited configurations, withhold the day's full task list…"): **SUPPORTED by the 2023 paper, near-verbatim.** "While almost none of the UpKeep configurations we discussed allowed for self-sequencing, many did allow GRAs to see their whole board. Only in the most limited configurations, GRAs were instead shown one assignment at a time – a configuration which many found stressful." (p. 629). Also: "Most of the configurations used by our participants do not allow GRA's to order their own assignment order" (p. 628). The same passage adds that many GRAs, "by working together with management", were "able to eventually phase out the one-room-at-a-time configuration" (p. 629); v4 might reflect that this was negotiated away in places.
- The card's NOT CHECKABLE verdict should be upgraded; the bib note's reading ("fixes work sequence, withholds the day's task list") is confirmed.

## shabnam2026tpsr
**PASS**
- Identity: Crossref matches the bib (JSM, early cite, pp. 1-17, no volume or issue; online 3 Jul 2026). Crossref gives "Roy, Sanjit K."; bib has "Sanjit Kumar" (fuller form, not a conflict).
- Quotes: all MATCH (abstract).
- Claims: agree, including the plural "agendas" caveat.

## slattery2002finding
**PASS**
- Identity: Crossref matches (JoHLSTE 1(1), 19-28; Crossref truncates the journal title). No bib entry; flagged in the card.
- Read depth: full publisher PDF (5,297 words); pdf p. 1 = p. 19.
- Quotes: all MATCH at the stated pages (21, 21, 22, 23, 25-26, 27). 'Hospitality managers are centrally involved…' spans the p. 25/26 break, as the card says.
- Claims: agree.

## spektor2025working
**PASS-WITH-NOTES**
- Identity: Crossref matches the bib (DIS '25, 3221-3234; nine authors).
- Read depth: abstract; honest. **I reached the full text** (ACM HTML, Internet Archive capture of 19 Jul 2025; no page numbers, so I give section numbers).
- Quotes: three MATCH (abstract).
- Drafters' check, the "withhold the day's full task list" use (v4 §4, cited "Spektor et al. 2023, 2025"): **SUPPORTED as a general description, not as a finding at the study site.** §5.1.1: "In most implementations of UpKeep, rooms are algorithmically assigned and enforced. The room list can also be programmed to reveal only one assignment at a time, prohibiting GRAs from seeing their full list of assignments in advance. However, at Hotel WCM, union representatives worked to ensure that GRAs have the ability to organize their room assignments, a right which is now also guaranteed by their union contract." §3 also describes worker-facing configurations "requiring workers to complete tasks in the order they were assigned". The card's tension is real: the 2025 site is the counter-case (self-sequencing, by union contract). The citation pair holds because 2023 carries the observation and 2025 restates the general configuration. 2025 alone would not.
- First v4 use ("more and more of their day goes to reading decisions made elsewhere and working around categories set elsewhere"): PARTLY SUPPORTED. §5.3 'The labor of documentation' reports that increased visibility "comes at a cost to workers, who must perform additional labor to update their progress and remain responsive within the app". §5.4.2 'Going around the AM to save time' reports managers working around UpKeep's credit protocols. "Reading decisions made elsewhere" is not the paper's framing.

## vandoorn2017domo
**PASS-WITH-NOTES**
- Identity: Crossref matches (JSR 20(1), 43-58); Crossref's title is the short form, as the card notes.
- Read depth: full published PDF.
- Quotes: all MATCH once the two columns are unpicked. **LOCATOR-WRONG:** "In the future, we expect more services to be collaboratively provided by human and social robot FLEs, such as in healthcare and hospitality services" is on pp. 45-46, not p. 44. The others are right (p. 43, 44, 43).
- Claims: agree. "Hospitality" appears once in the text, as the card says.

## wilsonnash2025captivity
**PASS-WITH-NOTES**
- Identity: Crossref matches the card (P&M 43(5), 974-985; online 30 Dec 2025, print May 2026). No bib entry (rejected).
- Read depth: abstract; `sources/` holds only Crossref, OpenAlex and Unpaywall JSON. Honest.
- Quotes: four MATCH (Crossref/OpenAlex abstract).
- Abstract-only check: **the Summary attributes material beyond the abstract** (the distinctions from digital exclusion and voluntary unengagement; older, disabled, low-income and unbanked customers). The card's own rr-2026-11 section flags these as unverified, but the Summary still states them as the paper's content. `verified_date: 2026-08-08` predates this run's re-read.

## xing2026algorithmic
**PASS**
- Identity: Crossref matches the bib (IJCHM 38(4), 1433-1452).
- Quotes: three MATCH (abstract). I confirm the abstract never uses "co-creator"; the support is from the title only.

## xiang2022covid
**PASS-WITH-NOTES**
- Identity: Crossref matches (Annals 93, article 103376; March 2022). No bib entry; flagged in the card.
- Read depth: PMC XML plus `paper.txt` (10,935 words), the full article.
- Quotes: all seven MATCH, and the section loci are right. The two literature-review quotes are under 'A hospitality paradigm of host-guest interactions'. The negotiation quote is under 'Integrated model of host-guest interaction rituals'. The test-report, failed-check-in and 'asked to leave' passages are under Stage II, 'Performance pathways: managing ritual violations'. The contribution quote is under 'Conclusions'. Setting, dates and ZMET count confirmed: "An upscale hotel in a city in southeastern China… between November 2020 and June 2021"; "11 interviews". The limitations sentence (high power distance, low individualism, generalisability) is in the Conclusions.
- Drafters' check, the manager-approved exception passage: **the quote and locator are right; the gloss "a negotiated exception" goes slightly beyond the text.** The source: "When conflicts arise, staff may provide compensatory measures… after checking with hotel management, the hotel was willing to cover the cost of the nucleic acid test, which was $80CNY… the hotel even arranged transportation." The testing rule was not waived. The guest still had to be tested, and management absorbed the cost. Xiang et al. call it a "compensatory measure" (and the rule was state-imposed). "A party with authority over the rule" is therefore inexact: management had authority over the hotel's response, not over the rule. The card's line that these readings are "not the authors'" is right; the paper should say "a compensation approved by management", not "an exception to the rule".

## yurrita2023disentangling
**PASS**
- Identity: Crossref matches the bib (CHI '23, 1-21).
- Read depth: full CHI PDF (ligatures dropped and two columns, as the card warns).
- Quotes: all MATCH by chunked check: abstract p. 1; §4.2.1 conditions pdf pp. 6-7; Tukey-adjusted p = 0.45 on p. 10 (§5.2); 75/267 on p. 11; "might still have thought about it as a non-human decision-maker" on p. 13.
- Claims: agree. A different human and the same system did not differ (p = 0.45), so the v4 "person" claim needs other support.

## zientara2023unpicking
**PASS**
- Identity: Crossref matches the bib (IJHM 108, 103355).
- Read depth: abstract; `try0.html` is a ScienceDirect captcha page, and my archive capture also held only the abstract. Honest.
- Quotes: three MATCH (abstract).
- Claims: agree that "often prefer to leave quietly" overstates an intention-to-quit/intention-to-unionise survey.

---

## Summary table

| Card | Verdict / item | Finding |
|---|---|---|
| — | FAILs | None |
| phillips2024physical | LOCATOR-WRONG | "Interviews were conducted with 30 customers…" is PDF p. 2, not p. 1 |
| santonidesio2021gaps | LOCATOR-WRONG | "Faultless liability regimes…" is §3.2.2 ¶3, not §3.2 ¶9 |
| vandoorn2017domo | LOCATOR-WRONG | "In the future, we expect more services…" is pp. 45-46, not p. 44 |
| santonidesio2021gaps | v4 claim refuted | No need→care / trust→fiduciary / risk→governance typology in the paper ("fiduciary" 0 hits; "governance" only in a reference title); v4 §4 attribution unsupported |
| martinwaldman2022legitimate | v4 claim partly supported | Five mechanisms, not three; audit and human-in-the-loop lowered legitimacy *against notice*, in the no-outcome condition; the appeal dividend for bad outcomes is confirmed |
| pijls2017measuring | v4 claim supported, with omission | "Feeling independent" and "having choice" dropped at the CFA (§5.2, pp. 130-131); third autonomy item "experiencing freedom" kept |
| spektor2023designing | v4 claim supported | "Only in the most limited configurations, GRAs were instead shown one assignment at a time" (p. 629) |
| spektor2025working | v4 claim supported as background | §5.1.1 describes the one-at-a-time list as a possible configuration; the study hotel itself allowed self-sequencing |
| xiang2022covid | gloss overreaches | The manager-approved step is a compensation (hotel pays for the test), not an exception to the rule |
| wilsonnash2025captivity | abstract-only overreach | The Summary states claims not in the abstract (the card flags them elsewhere) |
| metcalf2023courts | bib defect confirmed | references.bib "Tafesse, Elizabeth" should be Emnet |

All other quotes: MATCH.
