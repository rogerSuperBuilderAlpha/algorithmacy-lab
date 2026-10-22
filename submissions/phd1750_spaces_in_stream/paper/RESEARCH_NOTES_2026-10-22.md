# Research notes for v2: "Spaces in the Stream" (22 October 2026)

Research subagents ran the searches. Tags: [FT] the agent opened the full text; [ABS] abstract only; [REC] record only. Before any source enters v2 I read its abstract or passage myself, and v2 marks every new source `[VERIFY-READ]` until you have checked it. Consensus monthly quota: about 17 searches were left at the time of writing.

## R-D. Event segmentation (bears on Criterion 4, Proposition 4, P4, P7)

**The headline finding cuts against Proposition 4 as written.**
- Zacks, Speer & Reynolds (2009) [FT]: once situation changes were controlled, film cuts *lowered* segmentation (coarse OR .70, p < .001; fine OR .85, p = .04). In their words: "cuts, by themselves, do not cause people to perceive event boundaries."
- Schwan, Garsoffky & Hesse (2000) [ABS]: "Segmentation behavior depended primarily on the occurrence of breakpoints and was largely unaffected by the occurrence of cuts." Cuts placed at breakpoints improved recall.

**Imposed cues help most when they sit on real boundaries.**
- Boltz (1992) [ABS]: commercial breaks at episode boundaries gave better memory; breaks at event middles impaired it.
- Gold, Zacks & Flores (2017) [FT]: cues at boundaries gave recall .29 against .26 with no edits (d = 0.17); cues at middles were only marginally worse (p = .09); recognition was equal for boundary and middle cues. The authors raise the possibility that the pause itself helped, regardless of placement. This bears directly on the yoked control.
- Pitts et al. (2023) [ABS]: boundary cues beat middle cues and unedited video.
- Tsoukala et al. (2025) [ABS]: line breaks that clash with clause boundaries can lead readers "down the garden path."

**Boundaries also carry costs.**
- Swallow, Zacks & Abrams (2009) [FT]: objects from the previous event were remembered worse after a boundary (accuracy −.167; RTs +340 ms), while objects at the boundary itself were remembered better.
- Speer & Zacks (2005) [ABS]: retrieval of prior information was poorer after a temporal shift.
- Zacks (2020) [FT, author manuscript]: "the presence of an event boundary transiently disrupts performance (Huff et al. 2012)." Two problems: the page number is unconfirmed, and the sentence is a secondary citation of a visual-detection study using football clips, not reading. Baldwin & Kosie (2016) report the opposite.
- Su et al. (2025) [ABS] and Crockett et al. (2025) [ABS]: segmenting a reading into separate events hurt memory for wording but helped the situation model.

**Boundary placement depends partly on the reader's task.**
- Bailey, Kurby, Sargent & Zacks (2017) [FT]: readers oriented to space segmented more at spatial shifts (.70 vs .57, d = 0.65).
- Zwaan et al. (1998) [ABS]: spatial shifts slowed reading only after readers had memorised a map.
- Newberry & Bailey (2019) [ABS]: top-down effects on segmentation are "modest at best."

**Kumar et al. (2023)** [FT]: the paper's claim is correct ("transient increases in Bayesian surprise but not … surprisal"). The fit was modest, and for one of the three stories it held at only one parameter setting.

**Zacks 2009 figures** [FT]: 92.8 ms per situation change; 108 ms per 10% of boundary probability. Both match the paper.

**Implication.** Situation-model transitions should be a *moderator* of how well a mark works (marks on real transitions work, misaligned ones cost) and the *mechanism* behind it. They should not be a *criterion* for where decision spaces lie. Proposition 4 and P4 should predict what the mark adds over the transition alone, or what a mark does where there is no transition. The evidence also gives P7 a grounded basis (Boltz; Tsoukala).

## R-C. Overreliance, fluency, and the H construct (bears on H, P3, P8, §3.3, Table 4.1)

- **Kim et al. (2025, CHI)** [FT]: this is the paper the draft cites (in the reference list). N = 308. Explanations raised agreement on correct answers (67.2 → 78.2%) and on incorrect ones (78.2 → 82.8%). Sources cut agreement on incorrect answers to 68.2%. Quote: "the presence of explanations increases reliance on both correct and incorrect responses."
- **Steyvers et al. (2025, NMI)** [FT of arXiv v2]: longer explanations raised confidence without improving discrimination (BF = 25); human AUC was about .59–.60 against the model's .75–.78. This is the cleanest fluency-type evidence.
- **Si et al. (2024, NAACL)** [FT]: with an LLM explanation, accuracy was .87 when the explanation was correct and .35 when it was wrong. The no-evidence baseline was .49. Contrastive explanations raised the wrong-case accuracy to .56. Quote: "Humans over-rely on explanations even when they are wrong." **Not in the draft; should be.**
- **Spatharioti et al. (2025, CHI)** [FT]: on the error-inducing task, 93% chose correctly with traditional search against 47% with LLM search; highlighting low-confidence numbers raised accuracy from 26% to 58%. **Not in the draft.** Highlighting uncertain spans is a form of in-output marking (relevant to §4.11 and to novelty).
- **Gegoff et al. (2025)** and **Tatasciore et al. (2026, Human Factors 68(1), confirmed in the reference list)** are drone-management (UV) automation studies, not LLM or fluency studies. Gegoff shows that *presenting a recommendation* reduces discrimination (.93 vs .94) — a **format/structure** effect. Both belong in §3.2, not in the evidence for a fluency-based H.
- **Buçinca et al. (2021)** [FT]: overreliance .64 → .48, d = .36, confirmed. Their mechanism is heuristic ("develop general heuristics about whether and when to follow the AI").
- **Default effects (for structural co-optation):** Johnson & Goldstein (2003) [REC]; Dinner et al. (2011) [ABS], who identify effort, endorsement and reference-dependence channels; Jachimowicz et al. (2019) meta-analysis [ABS], 58 studies, d = 0.68.
- **Dark patterns:** Mathur et al. (2019) [ABS]; Gray et al. (2018) [REC].
- **Manzey et al. 2008** (cited in §4.10, absent from the reference list) most likely resolves to Manzey, Reichenbach & Onnasch (2008), HFES Proceedings 52(4) 297–301 [REC]. The "about half sampled all information" finding is reported via Parasuraman & Manzey (2010, p. 402). Cite it as "as cited in" (OPEN_ISSUES E4), or cite Manzey, Reichenbach & Onnasch (2012, JCEDM) [ABS], whose abstract names "looking-but-not-seeing."
- **Stark & Vanden Broeck (2024)**: the full text was blocked for the agent. The other agent will check it locally.
- **No study separates default/ordering effects from fluency effects in human–AI interaction** (agent's search). This is a real gap and supports the split as a testable prediction.

**Implication (supports R1's split, against R3's single H).**
- **H₁ co-optation (structural):** who places the decision point, authors the options and sets the default. Anchors: Stark & Vanden Broeck; defaults literature; Gegoff (recommendation format); the §3 plan-approval menu.
- **H₂ overreliance (epistemic/fluency):** fluent, explained output lowers scrutiny. Anchors: Kim 2025; Steyvers 2025; Si 2024; Spatharioti 2025; Buçinca 2021; Parasuraman & Manzey 2010; Reber & Schwarz 1999 [REC].
- **A falsifiable contrast:** H₁ predicts acceptance moves with option order or default placement when plan fluency is held fixed; H₂ predicts acceptance moves with fluency or length when the menu is held fixed.

## R-F. Prior uses of "algorithmacy" and literacy frameworks (bears on §4.1, §4 opening, Table 4.1)

- **Oberschelp (1995, p. 121)** [FT, read by the agent]: the term is used once, explicitly in a series with literacy and numeracy: "we have to preserve logicacy and algorithmacy by continuously training simple mental activities without artificial tools." His sense is unaided mental skill at algorithms. The paper's "in informatics teaching is acknowledged" understates how close the analogy is. The editors are D. Watson & D. Tinsley, and the volume is in the IFIP series. **Add the editors to the reference entry.**
- **Leese & Matzner (2016)** [conference programme and abstract book read]: an IAMCR 2016 pre-conference paper, Leicester: "What we call 'algorithmacy' establishes a new truth regime…" This is a second prior use, and it is unpublished.
- **Your Substack (22 Feb 2026) says the term "has never appeared in a published academic text."** That is false given Oberschelp (1995). You may want to correct it.
- OpenAlex finds the term in 1 work (Oberschelp); Crossref finds 0. Semantic Scholar and Google Books could not be searched (rate limits).
- **Ridley & Pawlick-Potts (2021)**: the quote is on **p. 4, not p. 3**. Their definition already includes "Position the individual as a co-constituent in algorithmic decision-making", and on p. 1 they compare algorithms to reading, writing and arithmetic.
- **Gal et al. (2020)**: the quote "sometimes disappears within technological systems" (p. 380) cites Marr & Hagston (2007) and Straesser (2015), **not Michael & Lupton**. Only "black boxes, even for those who produce them" (p. 383) cites Michael & Lupton (2016). **§4.1 L186 misattributes the first quote.**
- **Hoover & Gough (1990)** [ABS]: "the product of skill in decoding and linguistic comprehension"; the zero-if-either-is-absent claim is an implication of the product, not their wording.
- **The greatest threat to the algorithmacy / algorithmic-literacy distinction:** Tankelevitch et al. (2024, CHI, doi 10.1145/3613904.3642902) [REC/ABS], who argue that GenAI requires "a high degree of metacognitive monitoring and control." Also Nama (2026) on agentic literacy as a governance capability, and Apartsin & Aperstein (2026, preprint) on "Steering". All of them model a dyad, so the defence must rest on the triadic and co-optive features, not on steering. **Tankelevitch should be cited in §4.1.**
- Near neighbour to distinguish in one clause: Danaher (2016), "algocracy".

## R-A. Research on streamed LLM text (bears on §3.1, the §5.1 caveat, the gap claim)
The agent opened no paper in full; all of the following come from abstracts or summaries.
- **Su, Brasser, Reich, Jäger & Wang (2026, arXiv 2609.24616)** [ABS]: eye tracking, N = 53. The static display produced more global regressions than the streamed reveal (p < .001). Comprehension did not differ (ceiling effect). The materials were code. **This is the first direct evidence of suppressed regressions, and it falsifies the §5.1 claim that only two streaming studies exist.**
- **Pang et al. (2025, "Hippo," arXiv 2506.23678; possibly IUI 2026)** [ABS]: users interrupt and edit a reasoning tree that is segmented by topic. A reviewer is likely to name this as prior art.
- **Bigelow et al. (2025, ICLR, "Forking paths in neural text generation")** [REC]: finds the consequential "forking tokens" offline. This is support for Criterion 2, not a competitor.
- **"Not All Uncertainty Is Equal" (2026 preprint)** [REC]: token-level uncertainty markers *increased* agreement with the AI. A mark can invite deference, so this is a risk for §5.2 and P9.
- **Anderl et al. (2024)**: impaired discernment in Exp. 2 only (p = .029), not Exp. 1 (p = .212). The draft says "one experiment … but not in a preceding trial", which is consistent.
- **Kang & Muter (1989)**: moving text was *as good as* RSVP; the study had no static comparison. The draft's §3.1 wording ("comparable to RSVP") is fine.
- **Framing point:** streamed text stays on screen, so the paper must explain *why* regressions drop. Candidates are the expectation that more text is arriving, the leading-edge pull, and auto-scroll disrupting spatial memory (Weger & Inhoff 2007 [REC]).
- H. Zhu (2026, CHI EA, DOI 10.1145/3772363.3798936) and X. Zhu (2026, arXiv 2604.04418) are in your bibliography with DOIs. The agent's search missed them; that does not make them suspect.

## Citation audit (agent, full texts in ~/phd1750-litreview/texts etc.)
Corrections needed, beyond those already logged in OPEN_ISSUES:
- **Tsoukala (2025)**: the FDR non-significance and 52% power belong to the interaction, **not** the main effect. The main effect d = 0.32 / 0.41 has p < .001.
- **Buçinca (2021)**: 0.48 vs 0.64 applies to carb-source detection only (overall 0.26 vs 0.30, n.s.). Trust and preference did not differ significantly (only complexity did). "Satisfaction" and "frustrating" are not in the source. The L420 "liked and trusted … significantly less" holds only for high-NFC participants.
- **Metzner (2017)**: compared trials with vs without regressions. Medial violations read without regression still showed 87% judgement accuracy. "Systematically overlooks errors" is wrong.
- **Prajod (2026)**: L388 reverses the finding. The one-line label raised total fixation, which the authors read as an attentional cost; the detailed disclosure "did not impose additional burden."
- **Johnson (2000)**, cited at L61 for the landmark principle: Johnson argues the opposite ("habits like scriptio continua … worked", p. 608). Cite Rayner et al. (1998) or cut.
- **Rayner et al. (1998), p. 1143**: "knowing where words begin and end may have only a minor effect", which cuts against the segmentation-offloading framing. Their unit for 9.7% → 17.3% is "regressive fixations."
- **Zacks (2009)**: the segmentation finding is Exp. 1, not Exp. 3. t(26) = 2.97 is the *smallest* t for coarse–fine alignment, not "boundaries above chance."
- **Delgado (2018)**: 54 studies and 76 comparisons; the authors write that scrolling "may add" load.
- **Gould (2016)**: the title says *brief* lockouts encourage checking and *longer* ones encourage task switching. L310 says longer lockouts increased checking, which contradicts it.
- **Cox (2016)**: the quote is "a small obstacle **prior to** an interaction."
- **Parasuraman & Manzey (2010)**: the pages are 401 and 402, not 402 and 403.
- **Street (2003)**: p. 77. **Johnson (2000)**: p. 602. **Chen (2026)**: §6.2.
- **Zwaan & Radvansky (1998)**: cited at L85 with **no reference entry**.
- **J. Liu (2024) vs C. Liu (2026)**: both need initials.
- **Cutting & Deterding**: published 2024 (vol. 39, 2024).
- **Cho & Lim (2026)**: measured trust, not trust calibration.
- **Claude Code**: v2.1.275 (17 Sep 2026) added a send-now key that interrupts the turn, so "requiring the user to wait" is outdated. L111 attributes "nudges" to the classifier; the source attributes it to auto mode.

## R-G / R-H. Co-optation, Simmel, de-skilling (bears on §3.1 L111, §4.1 L169, §5.3, §5.4)
Read in full from the local PDF: `~/iit-playground/pyphi-experiments/dissertation/research/library/pdfs/stark2024.pdf`
- **Stark & Vanden Broeck (2024), p. 5** (abstract p. 1): "whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted." The p. 5 version credits Stark & Pais (2020).
  - L169's "platforms co-opt and enroll them" is **not their wording**. It joins p. 5 to p. 14 ("platform operators enroll users and providers in a system of ratings … The platform operator leverages rather than delegates") and turns their passive into an active verb.
  - **"Coordinative co-optation" is your term.** Mark it as your extension.
  - Supporting lines: p. 8 "Algorithms co-opt and organize users"; p. 9 "guiding, nudging, limiting, or expanding possibilities"; pp. 10–11 "No need for deliberation or real decision, just click"; p. 15 "organizational design is inseparable from design of the digital interface."
  - Their construct is structural; "persuasion", "fluency" and "ratify" do not occur in it. **This confirms R1's split.**
- **Simmel (1902)**: the tertius gaudens and the mediator are in **Part II** (AJS 8(2), pp. 167–182), the entry already in your reference list. The "b" suffix at L405 and L440 has no Part I ("a") to pair with, so drop it. Use "1902a/b" only if you also cite Part I (AJS 8(1), 1–46). Key quote, pp. 174–175: "he makes the reciprocal occurrences between the parties and between himself and the parties a means for his own ends."
- **Rosenblat & Stark (2016)**: the co-author is **Luke** Stark, not David Stark.
- **Bainbridge (1983)** [FT], p. 775: "the designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate"; p. 776: "The human monitor has been given an impossible task." Confirm the pages against the page images.
- **Lee et al. (2025, CHI)** [FT]: "higher confidence in GenAI is associated with less critical thinking." This paper carries Bainbridge's irony into GenAI directly, so it is the best anchor for reframing Counterpoint 1.
- **Endsley (2017)** [ABS]: the conundrum is about being "less likely … to take over manual control." It is not about detecting failures.
- **Braverman (1974)**: no verified quotation is available. Use it only through Qin & Cheon (2026, CHI) [FT], if at all. Recommendation: do not cite it in a paper about the perceptual layer.
- **Reactance**: Brehm (1966) [REC]; Rains (2013) meta-analysis [REC]; Sankaran et al. (2021) [ABS]. No HCI study has measured reactance to added friction specifically, which leaves a gap the paper can name.

## R-B. Agent oversight and checkpoint UIs (bears on §3.1, Table 3.1, the gap claim, §4.11, §5.2)
- **The broad novelty claim is falsified. A narrow version holds.** The narrow claim: no prior framework offers a *typology* of decision spaces (commitments, branch collapse, core verifiable assertions, situation shifts), marked in the live output of a coding or computer-use agent and handed to the *supervisor* as a decision, rather than used for monitoring or automatic stopping.
- **Hippo (Pang, Feng, Heer, Reinecke et al., arXiv:2506.23678)** [preprint]: streams the model's reasoning as a tree, flags points where user input would help, and stops there. Perceived control rose from 4.19 to 5.75 (p = .003, N = 16). The domain is reasoning for personal decisions, with one marker type. **This is the closest prior art and must be cited.**
- **HiLDe (Anaya González et al., arXiv:2505.22906)** [preprint]: highlights "critical decisions made by the LLM" in code completions and shows local alternatives; participants wrote 31% fewer vulnerabilities. The marking happens after each completion, not during streaming. **This is close to Criterion 2 and must be cited.**
- **Glassman, Gu & Kummerfeld (2024)**, "AI-resilient interfaces" (arXiv v1): interfaces should help users "notice and have the context to appropriately judge those AI choices." **Frame the paper as a specialisation of this work.** It also raises an objection the paper must answer: self-estimates "do not protect users when the AI is confidently wrong."
- **Streaming monitors that flag spans token by token, for machines rather than people:** Li et al. (NeurIPS 2025); Obeso et al. (arXiv:2509.03531, AUC .90).
- **Magentic-UI (Mozannar et al., 2025, arXiv:2507.22358)**: co-planning and action guards placed between steps.
- **Anthropic auto-mode posts (25 Mar 2026; 7 Aug 2026)**: users reject 39% of plans but only 3% of individual permission prompts; reviewers caught 13.6% of dangerous commands against 89% for the classifier; auto-mode users ship "about 25% more PRs"; prompts were 93% accepted (March) and 97% approved (August). **This is primary vendor evidence for the throughput thesis, and also a counterpoint (the classifier beats the humans).** Read these posts and cite them dated.
- **Counter-costs of pausing:** Wu et al. (ICML 2026): late interruptions cut reasoning accuracy by up to 60%. The Hedwig survey and Park et al. (2026): developers prefer few, early check-ins. Both belong in Counterpoint 1.
- **Corrections:**
  - The OpenAI Deep Research launch post (2 Feb 2025) does not mention clarifying questions. Cite only a dated source, or soften the claim.
  - Dhanorkar, Passi & Vorvoreanu (2026) is arXiv:2606.05391.
  - Cocoa is CHI 2026 (doi 10.1145/3772318.3791673).
  - "AskUserQuestion" first appears by name on 26 Nov 2025.

## R-I / R-J / R-E. Regressions, chain-of-thought faithfulness, friction
- **Harvey et al. (2017, JEP:HPP 43(3))** [FT accepted manuscript]: scrolling text **increased** regression probability (52.19% vs 20.64% in Exp. 1; F = 780.18, η² = .70). The regressions were **shorter** (by 6.36 characters), and long-range regressions were rarer. **This contradicts Prop 2 / P1 as written ("suppressing regressive saccades").** The defensible claim is that streaming shortens and localises look-back and reduces long-range regressions to upstream commitments.
- **Booth & Weger (2013)**: readers regress less when they know the text will be gone. A stream keeps earlier text on screen, so the evidence transfers only through the auto-scroll displacement argument.
- **Inhoff et al. (2019)** [ABS]: "college-level readers often do not regress even when this would improve sentence comprehension."
- **Timkey et al. (2026, PNAS 123(32), e2532230123)** [FT pp. 1–2]: n = 368; "syntactic disambiguation incurs a significant additional cost, reflected in an increase in rereading that is not explained by language model surprisal." **Add the full record to the references** (check the entry).
- **Metzner et al. (2017)**: the abstract does use "good-enough" ("pursue a 'good-enough' processing strategy that tolerates a deficient interpretation") and frames it as a strategic choice between trials, **not** as the effect of being denied regressions.
- **Chain-of-thought faithfulness (for Criterion 2):**
  - Turpin et al. (2023, NeurIPS; arXiv:2305.04388) [ABS]: "CoT explanations can systematically misrepresent the true reason for a model's prediction."
  - Chen et al. (2025, arXiv:2505.05410) [ABS]: "the reveal rate is often below 20%."
  - Lanham et al. (2023) [ABS].
  - Korbak et al. (2025) [ABS].
- **Friction:**
  - Arun & Fischer (2026) [ABS]: friction "did not reduce self-reported reliance on AI or increase critical evaluation" and raised trust.
  - de Jong et al. (2025, PACM HCI 9(2) CSCW048) [ABS]: partial explanations reduce overreliance.
  - Chen & Gero (2026, preprint): turn-level friction probes raised workload and time.
  - Gould et al. (2016) [ABS]: the title is "Brief Task Lockouts Encourage Checking, Longer Lockouts Encourage Task Switching." **This confirms the L310 contradiction.**
- **Rayner et al. (1998)**: the per-experiment figures were verified against the full text by the citation-audit agent (54/44% Exp. 1; 58% Exp. 2; 9.7 → 17.3% regressive fixations).
