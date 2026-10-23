# Section 3: claim and citation review, literature check, and articles still needed (21 October 2026)

> **Prepared by Claude (Opus 5.5) for Roger Hunt.**
> - **What I checked:** every sentence of the Section 3 you sent, against the source texts (`debate/texts/`), my reading notes (`notes/`), and abstracts pulled today from OpenAlex, Semantic Scholar and DataCite.
> - **How I searched:** by hand — OpenAlex (8 query sets), Consensus (3 queries), DataCite and Crossref. The arXiv API returned nothing. Every search is logged in `search-log.md`, rows 59–70.
> - **New texts read today:** Anderl et al. (2024), in full, and WaitGPT (Xie et al., 2024), §§1, 3–5 and 7. Both are in `sec3/texts/`.
>
> Every bibliographic detail for the new references was checked against Crossref, DataCite or OpenAlex records.
>
> I changed no text. The corrections below are for you to accept or reject.

---

## A. Claim-by-claim verification

Status codes:
- ✅ verified against the source;
- ✏️ verified, but the wording needs a change (correction given);
- ⚠️ not verifiable from what I hold (full text needed);
- ➕ verified, with something useful the draft does not yet say.

### 3.1 Streaming and pacing

| Claim | Status | Note |
|---|---|---|
| Park & Lee (2024): N = 36, Korean expository text, four display types; bottom generation gave more fixation starts, more total fixation time and larger saccades; fixation starts clustered where new text appeared (Tables 9, 11–12); topic confounded; no comprehension measure | ✅ ➕ | Add: the 36 were split into two groups of 18 (letter by letter versus sub-sentence chunks), and most post hoc differences were Type 2 or 3 against Type 4 (Table 12). |
| "The only eye-tracking study of chatbot text movement I found" | ✅ | Still true after today's search (rows 63, 67, 69). |
| Bhat (2025): within-subjects; typing at 2–3 s per sentence; competence F = 40.89, trustworthiness F = 35.21, persuasiveness F = 76.89, all p < .0001; effectiveness F = 0.16, p = .69 | ✅ ✏️ | **"Relative to the same kind of response shown whole"** is accurate only loosely. Participants interacted live with GPT-3.5 Turbo, and Bhat notes that responses "may" have differed between modes (limitations). Suggest: "relative to responses from the same model shown whole." |
| "Simulated typing is not token streaming" | ✅ | Bhat calls it "a simulated typing delay … 2–3 seconds per sentence." |
| Liu et al. (2024): 4.8 tokens/s from a words-per-minute table at about 1.3 tokens per word; 11.2 tokens/s on a real trace | ✅ | v1 §2.1 and v2 §2.2. |
| Xiao & Yang (2025): adaptive procedure; 99th-percentile comfortable speed 21.20 / 11.97 WPS against about 45 WPS for the GPT-4o API | ✅ | §3.2 (PEST, 79 valid participants). |
| Zhu, H. et al. (2026), adaptive token pacing | ⚠️ | Still known only from its record. Read it or cut it. |
| Sharmin, Špakov & Räihä (2015): word-by-word emergence gave more rereading and regressions than letter-by-letter | ⚠️ | **I could not retrieve an abstract today** (Elsevier gives none to OpenAlex or Semantic Scholar). I can no longer confirm the direction from anything I hold. Full text needed. |
| Sharmin et al. (2016): 90.8% of regression landings on content words against a 57.1% base rate | ✅ ✏️ | Abstract confirmed today. **Two corrections:** the text emerged *letter by letter* (speech-to-text interpretation), and the authors are **Sharmin, Wiklund & Tiittula**. Add their stated cause: "a typical cause of regressions seems to be incoherence resulting from omissions." |
| Harvey et al. (2017): word-level effects preserved, sentence-level predictability benefit lost | ✅ ➕ | Abstract. Add: readers made "fewer and longer fixations … with shorter progressive and regressive saccades" with scrolling text. |
| Harvey & Walker (2018): literal comprehension held, inference suffered | ✅ ➕ | Abstract. Add a direct support: "Returning to previously encountered text is also more difficult with this format." |
| Haverkamp et al. (2023): N = 145; backtracking 2.49 vs 3.53 (fewer), but farther; paging advantage p = .066 | ✅ | Full text (notes). Reader-controlled scrolling, not auto-scroll. |

### 3.2 Automation supervision

| Claim | Status | Note |
|---|---|---|
| Parasuraman & Manzey (2010): complacency in attention allocation under multiple-task load; "looking-but-not-seeing" (p. 403) for commission errors; about half of those missing a wrong diagnosis had sampled all the information needed (p. 402) | ✅ | Notes, full core sections. |
| Lee & See (2004): appropriate reliance | ✅ ➕ | Abstract. Lamb et al. (2026, §2.4) attribute the term "boundary conditions" to Lee & See. That links your 3.2 paragraphs; use it. |
| Gegoff et al. (2025): N = 142; accuracy .89 vs .85; discrimination .93 vs .94, ηp² = .05 | ✅ ✏️ | Add two details. The accuracy effect was ηp² = .16. Discrimination was measured only in the medium and high information conditions (F(1, 94)), so on 96 participants, not 142. |
| Tatasciore et al. (2026): N = 73 and 88; high transparency chosen on 39% and 43% of trials; adaptable transparency did not improve accuracy (p. 22); across six studies, high transparency raised hit rate and sensitivity and bias toward agreeing, with no gain in correct rejections (p. 21) | ✅ | Text verified. "Six studies" = the authors' aggregated analysis of their own UV-task studies (Studies 1–6, Fig. 8). Say "across the authors' six studies." |
| Chen et al. (2026): N = 48, 192 sessions; 29 of 138 blocked; 61 of 109 failures (56%) with timing mismatch; quote | ✅ ➕ | Notes, full text. Add: the authors say oversight "should therefore trigger judgment before a consequential transition" (§6.2). That is the nearest statement to marking. |
| Lamb et al. (2026): analysts; object-detection overlay on live video; 7 of 9 stopped treating it as an "advisor" (McNemar p = .023); "boundary conditions" | ✅ | Text verified (7 shifts one way, 0 the other; p = 0.023). |
| Endsley (2017): "the more capable and reliable the automation, the less likely its supervisors are to catch its failures" | ✏️ | The abstract says that as autonomy and reliability increase, situation awareness falls and operators become "less likely … to take over manual control when needed." That is about taking over, not catching failures. Reword accordingly. |

### 3.3 LLM overreliance and friction

| Claim | Status | Note |
|---|---|---|
| Kim et al. (2025): N = 16 + 308, pre-registered, hard binary factual questions; explanations raised agreement with correct and incorrect answers; sources and inconsistencies lowered it for incorrect ones; 189 of 308 never clicked a source; quote §5.1 | ✅ | Notes, full text. |
| Steyvers et al. (2025): longer explanations raised confidence without raising accuracy | ✅ | Abstract wording: "longer explanations increased user confidence, even when the extra length did not improve answer accuracy." |
| Zhu, X. et al. (2026): post-training raised accuracy, not verifiability; rephrasing did not help; FP score 0.717 → 0.602; most raters were LLMs | ✅ ✏️ | Notes. **D16 resolved:** the authors interpret the drop, hedged ("This suggests"), as preference optimisation making justifications for wrong answers look more convincing (§7.1). You can now state it. Also usable: human raters' accuracy fell slightly *with* justifications (0.836 → 0.809, §6.1). |
| Liu, C. et al. (2026): N = 77; GPT-4 platform with injected misinformation; whole-text copy-paste, coarse navigation, acceptance despite hesitation (Table 3) | ✅ | Notes. |
| Buçinca et al. (2021): N = 199; three forcing functions including a 30-second wait; overreliance 0.48 vs 0.64, d = .36; "preferred them less and trusted the system less" | ✅ ✏️ | The abstract's wording is safer: "people assigned the least favorable subjective ratings to the designs that reduced the overreliance the most." Also add their Need-for-Cognition finding: forcing functions helped people higher in NFC more. It bears on algorithmacy levels. |
| Ghosh et al. (2026): n = 214; "Assumptions" function reduced overreliance most, without raising cognitive load | ✅ | Abstract (notes). |
| Cox et al. (2016): "a small obstacle prior to an interaction"; short time cost; user autonomy an open question | ✅ | Text verified. |
| Collins et al. (2024): selective frictions; lower click-through, little accuracy cost; spillover to other topics | ✅ | Abstract verified today (DataCite record). |
| **Arun et al. (2026)** | ✏️ | **Citation error:** two authors, so **Arun & Fischer (2026)**. Abstract now verified. Add: friction "increased trust in and perceived usefulness of the AI," and did not "increase critical evaluation." The authors call the outcome "conscious reliance." |
| Disley & Khan (2026): N = 37; ownership 6.38 / 9.16 / 11.49; "an added step, a delay" (§2.3); call for interface-level comparisons (§7.9) | ✅ | Text verified (Table 1). The suppression condition is named "Unlearning to Rest." |
| Forshaw et al. (2026): 8 managers; preferred the human coach; resisted the AI's questions; behaviours appeared after both (§6.1) | ✅ ✏️ | The abstract adds that they "welcomed the probing questions" from the human and "wanted answers" from the AI. Worth quoting, because it is the reflection penalty in their words. |

### 3.4 Gaze

| Claim | Status | Note |
|---|---|---|
| Wu et al. (2025): gaze distinguished over-, under- and appropriate reliance at run time | ✅ ✏️ | Abstract. Add the task: a time-critical drone-monitoring task with AI alarms. That matters, because it is a monitoring task like yours. |
| Cao & Huang (2022): share of gaze on the AI suggestion correlated with agreement | ✅ | Abstract: "strong positive correlation." |
| Cho & Lim (2026): N = 23; TTFF 0.96–15.65 s; gaze did not predict trust; quote §3.4; static screens | ✅ | Notes, full text. |
| Yang et al. (2027): AR shortened fixations (d = −0.80); earlier crossings; "may also indicate overreliance" (§5) | ✏️ | **Locator:** the quote is in the **abstract** ("these patterns may also indicate overreliance"), not §5. The d = −0.80 values are from one-sample tests on trial-level ΔFD (t(432), t(428)), for the HUD and crossing-path placements. Thirty took part (27 analysed per my notes). Say "fixation durations," not "fixations on approaching automated vehicles." The measure covers the vehicle and the AR interface. |
| Resulbegoviq et al. (2026): 23 studies; "no modality-independent gaze pattern emerged"; longer viewing reflected difficulty or checking | ✅ | Notes. |

### 3.5 Summary and the gap claim

| Claim | Status | Note |
|---|---|---|
| "None examines the stream's internal structure" | ✏️ **important** | **WaitGPT (Xie et al., 2024, UIST) narrows this.** While an LLM's code streams in, WaitGPT parses it into data-operation units on the fly and draws each one as a growing diagram. Users can inspect each step, interrupt "at any point," and refine individual operations. One participant: "I felt stressed viewing the code stream, but it's a pleasure to watch the diagram grow." The authors call for "automated streaming methods" that let users "control their understanding speed rather than passively following a predefined playing timeline" (§7). This is structure inside a stream, for code. It differs from your theory in four ways: it re-represents code as a diagram rather than marking points in prose, it has no pauses, it measures no gaze, and it does not test placement. The gap sentence should name it as the nearest precedent and narrow the claim to streamed natural-language responses and to placement by decision points. |
| "What this work omits is continuity" (§3.2) | ✏️ | Anderl et al. (2024) is a partial exception (see B1). |

---

## B. Literature the section is missing, ranked

### B1. Critical: a reviewer will expect these, or they bear directly on the claims

1. **Anderl, C., Klein, S. H., Sarigül, B., Schneider, F. M., Han, J., Fiedler, P. L., & Utz, S. (2024).** Conversational presentation mode increases credibility judgements during information search with ChatGPT. *Scientific Reports, 14*, 17127. https://doi.org/10.1038/s41598-024-67829-6 **[READ in full today; open access; record verified against Crossref]**
   - *Design:* two pre-registered experiments, 1,222 participants. Partially inaccurate information was shown as a **video of a screencast typing out the response** (dynamic text agent), as a voice agent, or as static encyclopedia text, with identical content.
   - *Results:* the dynamic and voice agents raised perceived credibility over static text. Discernment of accurate from inaccurate information was lower for dynamic text than static text in Experiment 2 (p = .029) but **not** in Experiment 1 (p = .212). The authors attribute the effect to "conversational nature," not to typing as such.
   - *Why it matters:* it is the only study I found that measures inaccuracy detection with typed-out AI text against static text. It partly supports your abstract's claim (D3, I4) and §1's puzzle, but it confounds typing with the chatbot frame and its detection effect replicated in only one of two experiments. It belongs in §3.1, and it changes the "continuity" omission in §3.2.
2. **Xie, L., Zheng, C., Xia, H., Qu, H., & Chen, Z. (2024).** WaitGPT: Monitoring and steering conversational LLM agent in data analysis with on-the-fly code visualization. In *UIST '24*. https://doi.org/10.1145/3654777.3676374 **[READ today, §§1, 3–5, 7]** The nearest precedent to marking (see 3.5 above). It belongs in §3.3 or a new short paragraph, in §4.11 ("what marking is not"), and in §5.2.
3. **Tan, F. F.-Y., Messerschmidt, M. A., Yin, W. F., & Nov, O. (2026).** The impact of response latency and task type on human–LLM interaction and perception. In *CHI '26*. https://doi.org/10.1145/3772318.3790716 **[abstract only; open access]** Time-to-first-token of 2, 9 or 20 s. Behaviour was robust to latency, but 2-second outputs were rated *less* thoughtful and useful, and delays were read as "AI deliberation." The authors conclude latency is "a tunable design variable with ethical implications." This is the newest timing study, and it supports your claim that pacing is a design choice, not a given.
4. **Glassman, E. L., Gu, Z., & Kummerfeld, J. K. (2024).** *AI-resilient interfaces* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2405.08447 **[abstract only]** Their argument is that "in order to recover from AI choices, the user must notice them first," and that an important choice can be "hiding in a wall of text." This is the closest *conceptual* neighbour to decision spaces, and §4.1 should distinguish your construct from it. WaitGPT cites it.
5. **Goddard, K., Roudsari, A., & Wyatt, J. C. (2012).** Automation bias: A systematic review of frequency, effect mediators, and mitigators. *Journal of the American Medical Informatics Association, 19*(1), 121–127. https://doi.org/10.1136/amiajnl-2011-000089 **[abstract only; open access]**
   - The standard review of automation bias, with 74 studies.
   - One mitigator they name is "the position of advice on the screen," which is direct support for the idea that *where* something appears matters.
   - Belongs in §3.2.
6. **Si, C., Goyal, N., Wu, T., Zhao, C., Feng, S., Daumé III, H., & Boyd-Graber, J. (2024).** Large language models help humans verify truthfulness — except when they are convincingly wrong. In *NAACL 2024*. https://doi.org/10.18653/v1/2024.naacl-long.81 **[record only; open access]** Directly about LLM explanations and human verification of wrong answers. Belongs in §3.3.
7. **Zhou, L., Schellaert, W., Martínez-Plumed, F., Moros-Daval, Y., Ferri, C., & Hernández-Orallo, J. (2024).** Larger and more instructable language models become less reliable. *Nature, 634*(8032), 61–68. https://doi.org/10.1038/s41586-024-07930-y **[abstract via Consensus]** Scaled-up models give "apparently sensible yet wrong" answers that "human supervisors frequently overlook." This supports §3.3's fluency point at the model level.

### B2. Important: strengthens a claim or fills a visible hole

8. **Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S. A., & Vaughan, J. W. (2024).** "I'm not sure, but…": Examining the impact of large language models' uncertainty expression on user reliance. In *FAccT '24*. https://doi.org/10.1145/3630106.3658941 **[abstract]** N = 404, pre-registered. First-person uncertainty lowered agreement and raised accuracy. This is an *in-text* marker that changes reliance — a cousin of marking that a reviewer will raise.
9. **Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023).** Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), 1–38. https://doi.org/10.1145/3579605 **[abstract]** A cost–benefit account in which people choose strategically whether to engage (5 studies, N = 731). It is the main rival to the attentional account in §3.2, and §4.9 should engage it.
10. **Fok, R., & Weld, D. S. (2024).** In search of verifiability: Explanations rarely enable complementary performance in AI-advised decision making. *AI Magazine, 45*(3), 317–332. https://doi.org/10.1002/aaai.12182 **[abstract]** "Explanations are only useful to the extent that they allow a human decision maker to verify." It pairs with Zhu, X. et al. on verifiability.
11. **Spatharioti, S. E., Rothschild, D. M., Goldstein, D. G., & Hofman, J. M. (2025).** Effects of LLM-based search on decision making: Speed, accuracy, and overreliance. In *CHI '25*. https://doi.org/10.1145/3706598.3714082 **[record only; open access]**
12. **Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025).** The impact of generative AI on critical thinking. In *CHI '25* (pp. 1–22). https://doi.org/10.1145/3706598.3713778 **[abstract]** In a survey of 319 knowledge workers, higher confidence in GenAI went with less critical thinking, and GenAI shifted critical thinking "toward information verification." This supports co-optation.
13. **Danry, V., Pataranutaporn, P., Mao, Y., & Maes, P. (2023).** Don't just tell me, ask me: AI systems that intelligently frame explanations as questions improve human logical discernment accuracy over causal AI explanations. In *CHI '23*. https://doi.org/10.1145/3544548.3580672 **[abstract]** N = 204. Questions inside the AI's output improved discernment. This is a friction-*inside*-the-output precedent, and it partly qualifies the claim in §3.3 that friction never sits inside the response. Distinguish it in §4.11: it changes the content, while marking changes the presentation.
14. **Gnewuch, U., Morana, S., Adam, M. T. P., & Maedche, A. (2022).** Opposing effects of response time in human–chatbot interaction. *Business & Information Systems Engineering, 64*(6), 773–791. https://doi.org/10.1007/s12599-022-00755-x **[abstract via Consensus]** N = 202. Delayed responses had opposing effects on social presence and usage intentions, moderated by prior experience. It is the established chatbot-timing paper behind Bhat's design.
15. **Kang, T. J., & Muter, P. (1989).** Reading dynamically displayed text. *Behaviour & Information Technology, 8*(1), 33–42. https://doi.org/10.1080/01449298908914536 **[abstract]** Smooth-scrolling "Times Square" text gave comprehension "at least as high" as RSVP at 100–300 wpm. **This is counter-evidence**: moving text need not hurt literal comprehension. Cite it to pre-empt a reviewer, alongside Harvey & Walker's finding that the cost falls on inference.
16. **Mozannar, H., Bansal, G., Tan, C., Fourney, A., Dibia, V., Chen, J., Gerrits, J., Payne, T., … (2025).** *Magentic-UI: Towards human-in-the-loop agentic systems* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2507.22358 **[abstract]** Co-planning and action guards for agents. It belongs in §5.2's agent extension, beside Chen et al.

### B3. Classic anchors a human-factors reviewer will look for

17. **Bainbridge, L. (1983).** Ironies of automation. *Automatica, 19*(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8 It is the origin of the monitoring paradox that Endsley's conundrum restates.
18. **Reber, R., & Schwarz, N. (1999).** Effects of perceptual fluency on judgments of truth. *Consciousness and Cognition, 8*(3), 338–342. https://doi.org/10.1006/ccog.1999.0386 Your "fluency co-opts" claim has no basic-science anchor in the library. This is the standard one.

### Reviewed and not recommended for §3

These are off target, or are system papers without human evaluation:
- Koscelny et al. (2025);
- Yu et al. (2026);
- Taş et al. (2026);
- AI Chains (Wu et al., 2022): relevant to decomposition, but already covered by Kazemitabaar et al.;
- the LLM self-correction surveys.

Inhoff et al. (2019, *Vision*) and Wilcox et al. (2024, *Cognition*) on regressions belong to §2, not §3. Inhoff et al. note that "college-level readers often do not regress even when this would improve sentence comprehension," which qualifies §2.2.

---

## C. Full articles you still need for complete vetting

**Cited in §3 but held only as abstract or record. The current text depends on these:**
1. Sharmin, Špakov & Räihä (2015), *IJHCS, 78*. https://doi.org/10.1016/j.ijhcs.2015.01.010. I can no longer confirm the direction of the claim.
2. Sharmin, Wiklund & Tiittula (2016), *SKY Journal of Linguistics, 29*. https://journal.fi/finjol/article/view/153025 (open access).
3. Harvey et al. (2017), *JEP:HPP, 43*(3). https://doi.org/10.1037/xhp0000329
4. Harvey & Walker (2018), *QJEP, 71*(9). https://doi.org/10.1080/17470218.2017.1363258
5. Zhu, H. et al. (2026), CHI EA. https://doi.org/10.1145/3772363.3798936. Known only from its record.
6. Collins et al. (2024), arXiv (open access). https://doi.org/10.48550/arXiv.2407.12804
7. Arun & Fischer (2026). https://doi.org/10.1145/3808045.3808049
8. Wu et al. (2025), *PACM HCI, 9*(3). https://doi.org/10.1145/3725841
9. Cao & Huang (2022), *PACM HCI, 6*(CSCW2). https://doi.org/10.1145/3555572
10. Steyvers et al. (2025), *Nature Machine Intelligence, 7*. https://doi.org/10.1038/s42256-024-00976-7
11. Lee & See (2004), *Human Factors, 46*(1). https://doi.org/10.1518/hfes.46.1.50_30392
12. Endsley (2017), *Human Factors, 59*(1). https://doi.org/10.1177/0018720816681350
13. Ghosh et al. (2026), arXiv (open access; results section unread). https://doi.org/10.48550/arXiv.2601.18033

**New, needed before citing (B1 and B2):**
- Tan et al. (2026) and Si et al. (2024) are open access. I can fetch them myself if you approve.
- Goddard et al. (2012) and AI-Resilient Interfaces (2024) are also open access.
- Zhou et al. (2024), *Nature*.
- Kim et al. (2024), FAccT.
- Vasconcelos et al. (2023).
- Fok & Weld (2024).
- Spatharioti et al. (2025), open access.
- Lee et al. (2025).
- Danry et al. (2023).
- Gnewuch et al. (2022).
- Kang & Muter (1989).
- Magentic-UI (2025), open access.

**Already sufficient:** Park & Lee, Bhat, Liu J. (Andes, relevant sections), Xiao & Yang, Haverkamp, Parasuraman & Manzey, Gegoff, Tatasciore, Chen, Lamb, Kim (2025), Zhu X., Liu C., Buçinca, Cox, Disley & Khan, Forshaw, Cho & Lim, Yang, Resulbegoviq, Anderl, WaitGPT.

---

## D. Corrections to make in the text (summary)

1. Arun et al. → **Arun & Fischer** (two authors).
2. Sharmin et al. (2016): the text emerged **letter by letter**; the authors are Sharmin, Wiklund & Tiittula.
3. Endsley: reword to "less likely to be able to take over manual control when needed."
4. Yang et al.: give the quote's locator as the **abstract**, and the measure as fixation durations on the vehicle and AR cues (trial-level d).
5. Gegoff et al.: discrimination was measured on the 96 participants in the medium and high conditions.
6. Bhat: "responses from the same model," not "the same kind of response."
7. Buçinca: use the abstract's wording on subjective ratings.
8. Zhu, X. et al.: D16 resolved. State the authors' hedged interpretation.
9. §3.5 and the gap sentence: name WaitGPT as the nearest precedent and narrow the claim to streamed natural-language responses and to placement by decision points.
10. §3.3's "None of it sits inside the generated response": qualify with Danry et al. (2023), questions inside the output, and Kim et al. (2024), uncertainty phrases inside the output. Both change *content*; marking changes *presentation*.
11. §3.1: add Anderl et al. (2024) after Bhat. It is the one study measuring inaccuracy detection with typed-out text.
12. §3.2: add Goddard et al. (2012), position of advice on the screen, and Bainbridge (1983).
