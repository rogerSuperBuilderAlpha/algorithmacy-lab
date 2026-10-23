[DRAFTED — Claude, 22 October 2026. Change log for `DRAFT_v2_2026-10-22.md`. Doc line numbers (L###) refer to `gdoc_full_2026-10-22d.md`. "R1/R2/R3" refer to the reviews, "N#" to the problems no reviewer raised, and the remaining IDs to OPEN_ISSUES.md. Evaluation: `REVIEW_EVALUATION_2026-10-22.md`. Evidence: `RESEARCH_NOTES_2026-10-22.md`, `APPENDIX_A_changelog_verbatim.md`.]

# Change log, v2

## Decisions taken by default (yours to confirm or reverse)

| ID | Decision | Default taken in v2 | Why | Reverse by |
|---|---|---|---|---|
| D1 | Criterion 4 (situation-model transitions) | Moved out of the locating rule. It becomes an *alignment condition* on marks (§4.5), and Prop 1 is renamed "Representation Independence." | It describes the reader's comprehension, not the process; it makes P4 circular; it contaminates the Condition 2 control. Bailey et al. (2017) show segmentation depends on the reader's task. | Restoring the Doc L268 text (kept under "Cut from v2", D) and "four" in Δ109/Δ115/Δ152/Δ165/Δ175. |
| D2 | H construct | Split. **H, co-optation**, is structural: who places the stops, writes the options, sets the default; it acts upstream on alignment. **O, overreliance**, is epistemic: it gates F × MI. Formula: G = F × MI × (1 − O). Prop 3 renamed "Overreliance via Explanations and Framing"; P8 and P9 use O. | Stark & Vanden Broeck (read in full) define co-optation structurally; the H evidence is overreliance evidence. | Collapsing H and O back into one H as R3 proposes: G = F·MI·(1−H). |
| D3 | §5.3 | Coding-agent scope kept. The platform-labour material (phygital, Marks 1–4, Hirschman) is deferred to one paragraph; the original text is kept under "Cut from v2", B. | §1 brackets labour governance; "Mark" collided with interface marks; R1. | Restoring B, renaming the "Marks" (R3: "Conditions"). |
| D4 | Third party in the coding triad | No default on the theory. One drafted, marked sentence in §1 names the vendor as the third party (Simmel, 1902, p. 176). "Anticipate counterpart dynamics" kept in the definitions. | R1.5. Without it, the coding case reads as a dyad. | Deleting the drafted sentence, or redefining "counterpart". |
| D5 | Study design | Three conditions kept. The paper now states which predictions it tests (P5, P6, P9-MI, P11, P12) and which it does not (P1, P7, P8, P10, P13). RQ3 (mid-clause) removed and offered as a follow-up fourth condition. Seeded errors split into load-bearing vs local. Power recomputed: N = 40 for .85 at f = .22, recruit 50. Condition 2 also excludes situation shifts. | R1.22–1.24; R3.3; formal audit; my power recomputation (scipy noncentral F, λ = f²·N·m/(1−ρ)). | — |
| D6 | Pre-title summary | Cut; its Contributions paragraph closes §1 (Δ19). | Journals do not accept it (R1.2). | — |
| D7 | Dissertation placement (R1.1) | Flag only. | Your call. | — |
| D8 | Counterpoint 1 | Reframed on Bainbridge (1983) and Lee et al. (2025); reactance named as measurable (Brehm, 1966; Rains, 2013). Braverman not cited (no verified quotation; outside the paper's scope). | R1.28; R-H research. | — |

## Unmarked edits (listed per section, as the header of the draft says)

- **Restored symbols** (Markdown export losses, confirmed in the PDF): η² (L93), → (L220, L276, L280, L318, L326), × (L346, L430, L438, L448), α and β (L354), κ (L272; also missing in the Doc itself).
- **Headings:** §3 restructured as 3.1 case + 3.2–3.6. This makes about 25 existing cross-references resolve unchanged.
- **Paired em-dash asides recast** as parentheses or commas in §1 (L43, L45, L47), §2 (L65 ×2, L87, L95), §3 (L101, L103, L105 ×2, L109, L111 ×2, L125, L127, L133 ×2), §4 (L163, L186, L278, L312, L318, L326), §5 (L346, L383). Gloss-weld dashes kept per `writing-style.md`.
- **Citation format:** "et al." for three or more authors (Rayner, Drieghe, Schotter, Zacks, Mangen, Buçinca narrative citations); J. Liu / C. Liu; H. Zhu; Arun & Fischer.
- **Tables 3.1 and 4.1:** raw Markdown escapes removed. Table 4.1's empty header row filled (Δ79).

## Marked edits

| Δ | Where (Doc) | Original (short) | Change and reason | Source / issue |
|---|---|---|---|---|
| 1 | Abstract L31 | 286-word abstract | Compressed to 193 words, keeping your sentences where possible. Removed the scriptio continua sentence (B1.5), "fundamentally", "skeuomorphic", the "depletes working memory…" sentence (B1.1); "joint operation" → "product" (A4); "competency" → "competence"; dropped "and anticipate counterpart dynamics" from the abstract only. | HCI author instructions (200 words); R1.3 |
| 2 | §1 L37 | "fundamentally disrupts" | "fundamentally" cut | B1.3; R1, R2 |
| 3 | §1 L39 | "significant category error" | "significant" cut, to match the abstract | R1 |
| 4 | §1 L41 | "This interface pathology" | "design" | R2 (polemic) |
| 5 | §1 L41 | "shackled cognition" | "tied cognition" | R1, R3 |
| 6 | §1 L41 | "the vast cognitive architecture" | "the cognitive practices" | R3 |
| 7 | §1 L43 | "commits to verifiable claims, executes computational branching, or shifts operational goals—points where human capabilities to control internal intent and imagine counterpart intent among otherwise idempotent, conversational content become indispensable" | Rewritten to match the three criteria; the garbled clause and "idempotent" replaced | A2, A8; R1.6; style audit |
| 8 | §1 L45 | "…are bracketed" | "I bracket…" | R1 passive list |
| 9 | §1 L45 | "An essential boundary condition is established at the outset" | "I set one boundary condition at the outset" | R1 |
| 10 | §1 L45 | "idempotent" | "non-binding" | A8 |
| 11 | §1 L47 | "benign, idempotent" | "benign, non-binding" | A8 |
| 12 | §1 L47 | "These are decision spaces specified for the platform's intent." | "stops placed" (an interface does not create decision spaces: Prop 1) | Formal audit |
| 13 | §1 L47 | "Across HCI… I found no framework that…" | Replaced by a pointer to §3.6, so the gap is stated once | R1.18; G20 |
| 14 | §1 L49 | "idempotent generation" | "non-binding" | A8 |
| 15 | §1 L49 (3) | "co-opts human agency, leveraging surface syntactic fluency…" | Split into overreliance + co-optation | D2 |
| 16 | §1 L49 (4) | "[structural marks - or whatever design solution I create later]" | "interface marks" | A5; R1.4 |
| 17 | §1 L49 (5) | "the joint operation" | "the product" | A4 |
| 18 | §1 L49 (6) | "[marking, or whatever]" | "interface marking" | A5 |
| 19 | §1 (new ¶) | Contributions (pre-title L15–21) | Moved here; "four-part" → "three-part" (D1); "the first psychophysically grounded model" → "a psychophysically grounded model" (novelty) | R1.2; D6 |
| 20 | §1 L51 | "key ergonomic moderators (4.9–4.11)" | Itemised: 4.9 / 4.10 / 4.11 | B1.11 |
| 21 | §1 L51 | "explores algorithmacy across non-textual autonomous platforms (5.3)" | "sets the scope … for agentic coding environments" | D3 |
| 22 | §2 L55 | Claim in the last sentence | Claim moved to the front; a closing clause links back | R1, R3 (claim-first) |
| 23 | §2.1 L61 | "fundamental ergonomic principle … (Johnson, 2000)" | "fundamental" and the Johnson citation removed; FLAG added | N8 (Johnson p. 608 argues the opposite) |
| 24 | §2.1 L61 | "Rayner, Fischer, and Pollatsek … 44% to 54% for single sentences and by 58% for extended passages" | "54% sentences, 44% passages (Exp. 1); 58% sentences (Exp. 2)" | B2.1; Rayner et al. 1998 pp. 1132, 1138 |
| 25 | §2.1 L61 | "of all oculomotor events" | "of all fixations" (source unit: regressive fixations) | Citation audit |
| 26 | §2.1 L65 | "did add decision spaces" | "decision points" (Prop 1) | Formal audit |
| 27 | §2.1 L65 | "The default choice is idempotent in the sense that matters here" | "The leading option is a no-op…" (the docs do not say it is preselected) | A8; N10 |
| 28 | §2.1 L67 | "essential perceptual support" | "essential" cut | R1 |
| 29 | §2.2 L71 | "this essential error-recovery routine" | "essential" cut | R1 |
| 30 | §2.2 L73–75 | "…triggers immediate regression and a P600 …" + "In contrast, readers without regression opportunities default to … systematically overlooks errors (Metzner)" | Joined (orphaned citation) and rewritten to the source's wording; corrupted "In contrast" removed | B2.5; R3.7; Metzner 2017 abstract |
| 31 | §2.3 L79 | "and suppressing" | "and, on this account, suppressing" | B2.6 |
| 32 | §2.3 L81 | "fundamentally depends" | "fundamentally" cut | R1 |
| 33 | §2.3 L81 | "preventing the priority map from resetting" | "on Wolfe's proposal preventing…" | B2.6 |
| 34 | §2.4 L85 | "(Kurby & Zacks, 2012; Zacks, 2020)" for executive gating | Kurby & Zacks 2012 removed (the claim goes beyond it) | Citation audit |
| 35 | §2.4 L87 | "(t(26) = 2.97)" | "smallest t(26) = 2.97" (the minimum across narratives, coarse–fine alignment) | Zacks et al. 2009 |
| 36 | §2.4 L87 | "This result confirms that event boundaries reflect structural shifts…" | The authors' own reading (prediction error as control mechanism) | B2.7 |
| 37 | §2.4 L87 | "(Zacks, 2020)" for monitoring disruption | "(Huff et al., 2012, as cited in Zacks, 2020)" + VERIFY | R-D research |
| 38 | §2.5 L91 | "vision is conceptualized as" | "O'Regan and Noë conceptualize vision as" | Passive with hidden agent |
| 39 | §2.5 L91 | "readers often fixate"; "becomes inevitable" | "can"; "more likely" | B2.8 |
| 40 | §2.5 L93 | "material placeholders' and tactile boundaries" | "tactile boundaries" cut | B2.9 |
| 41 | §2.5 L93 | "54 empirical comparisons" | "54 studies (76 comparisons)" | Delgado et al. 2018 |
| 42 | §2.5 L93 | "argued that scrolling text imposes an extraneous cognitive burden … continually disrupting" | "suggested that scrolling may add…" | Delgado et al. 2018 wording |
| 43 | §2.5 L95 | "I found no study that tests an active streaming display." | Updated: Su et al. (2026) for code; prose untested | R-A research; N5 |
| 44 | §2.5 L95 | "an unanswered question" | "multiple-choice question" (the timeout applied only to AskUserQuestion) | tools-reference L138; G22 |
| 45 | §3 heading | "3. A Worked Case: How Claude Code Stages Decisions" | "3. A Worked Case and Prior Literature" + new 3.1 heading | R1.7; R3 |
| 46 | §3.1 L101 | queuing sentence | Dated: send-now key v2.1.275 (17 Sep 2026) | Changelog; N10 |
| 47 | §3.1 L103 | "task list" | "Todo list" (changelog wording) | Appendix A |
| 48 | §3.1 L103 | "first documented in June 2025 (v1.0.33" | "that the changelog first mentions … ('Improvements to plan mode,' v1.0.33" | G12 |
| 49 | §3.1 L103 | "By late 2025 … (v1.0.77, August 2025)" | "In August 2025 … in September 2025 it…" | Dating slip |
| 50 | §3.1 L103 | "any unanswered question … (v2.1.200; …)" | "multiple-choice"; + clause: timeout never applied to permission prompts or plan approval | R1.15; G22 |
| 51 | §3.1 L103 | "in late 2026, … in August 2026" | "in August 2026" | Dating slip |
| 52 | §3.1 L103 | "September 2026 with auto mode established as the default starting mode for enterprise and team subscription tiers (v2.1.283" | "late September 2026 … every plan and provider (v2.1.283–v2.1.284), where earlier versions had made it the default only on Pro, Max, and Team plans" | **Wrong fact corrected** (Appendix A; permission-modes.md L11, L220; changelog 2.1.283/2.1.284) |
| 53 | §3.1 L103 | "Over sixteen months" | "Over nearly seventeen months" | Appendix A (30 Apr 2025 – 25 Sep 2026) |
| 54 | §3.1 L105 | "Notably," | cut (emphasis marker) | writing-style.md |
| 55 | §3.1 L107 | "(pp. 602–603)" | "(p. 602)" | Johnson 2000 (full text) |
| 56 | §3.1 L107–109 | "…'replayed.' ¶ In contrast, 'nothing in the ancient bookroll…'; Claude Code's /rewind…" | Rejoined with "and … so" (the original "and" from `SECTION3_1_claude_code.md`) | R1.16; R3.5; G29 |
| 57 | §3.1 L111 | "evaluate the issue" | "I evaluate the issue" | R3.6 |
| 58 | §3.1 L111 | "it exercises coordinative co-optation" | "what I call coordinative co-optation, extending their platform co-optation to the interface" (the term is yours, not theirs) | Stark & Vanden Broeck 2024 (full text) |
| 59 | §3.1 L111 | "deploying automated classifier 'nudges'" | "having auto mode 'nudge' the agent" (the docs attribute it to auto mode) | permission-modes.md L335; G29 |
| 60 | §3.1 L111 | "an essential supervisory affordance" | "a supervisory affordance" | R1 |
| 61 | §3.2 L119 | "Crucially," | cut | R1, R2 |
| 62 | §3.3 L123 | "(p. 402)" | "(p. 401)" | Parasuraman & Manzey 2010 (full text) |
| 63 | §3.3 L125 | "(Tatasciore et al., 2026)—moreover," | "; across the authors' studies," (run-on fixed; scope stated) | R3.8; citation audit |
| 64 | §3.3 L125 | "fails decisively" | "fails" | G27 |
| 65 | §3.3 L125 | Chen quote, no locator | "(§6.2)" | Chen et al. 2026 (full text) |
| 66 | §3.4 L131 | "Fluent explanations consistently increase reliance … (Kim et al., 2025)" | "Explanations increase reliance … including incorrect ones (Kim et al., 2025)", + Si et al. (2024) | Kim 2025 tested explanations, not fluency; Si 2024 (abstract read) |
| 67 | §3.4 L133 | "though they often come with user dissatisfaction" | "though participants rated them as more complex" + FLAG | Buçinca 2021 (full text) |
| 68 | §3.4 L135 | governing-question opener repeated | "Against the same governing question," | R1.17 |
| 69 | §3.4 L135 | "mere 'prompt fatigue'" | "mere" cut | R1 |
| 70 | §3.5 L139 | "how radically dynamic delivery"; "almost exclusively at" | "radically" and "almost exclusively" cut | Citation audit (Park & Lee overstated) |
| 71 | §3.5 L139 | "does not predict whether users calibrate their trust" | "does not predict users' trust" (they measured trust only) | Cho & Lim 2026; G29 |
| 72 | §3.5 L139 | "More fundamentally" | "More basically" | R1 |
| 73 | §3.5 L141 | "When evaluated against the governing question … a decisive analytical limitation: it records where the fovea was directed. Still, it cannot" | "Against the same question … an analytical limitation: it records … but cannot" (corrupted "Still," repaired) | R1.17; R3.5 |
| 74 | §3.6 L147 | "Synthesizes how…" (no subject) | "The table compares how…" | Style audit |
| 75 | §3.6 L159 | Gap sentence | Narrowed to a typology of decision spaces marked for the supervisor; names HiLDe and Hippo; frames the work under Glassman et al. (2024) | R-B research; N4; B1.10 |
| 76 | §4 L163 | "While Oberschelp's (1995) earlier use of the term in informatics teaching is acknowledged, the present theory" | Drafted acknowledgment (Oberschelp p. 121; Leese & Matzner 2016) + "The present theory" | R-F research; N7; C6 |
| 77 | §4.1 L169 | "Stark and Vanden Broeck's (2024) analysis … is extended" | "I extend…" | Passive (R1) |
| 78 | §4.1 L169 | "While actors in hierarchies command, in markets contract, and in networks collaborate, platforms co-opt and enroll them through the system's structural design." | Replaced with their verbatim line (p. 5) and the "enroll … leverages rather than delegates" passage (p. 14) | Stark & Vanden Broeck 2024 (full text); R2.3 |
| 79 | §4.1 Table 4.1 | Empty header row | "Literacy / Oracy / Numeracy / Algorithmacy" | Style audit; PDF |
| 80 | §4.1 L184 | "in their formulation, comprehension is zero if either component is absent" | "the product implies that…" (the abstract says "product"; zero is the implication) | R-F research |
| 81 | §4.1 L186 | "four decisive ways" | "four ways" | R1 |
| 82 | §4.1 L186 | "(Gal et al., 2020, citing Michael & Lupton, 2016)" | First quote: (Gal et al., 2020, p. 380). Second: (Michael & Lupton, 2016, as cited in Gal et al., 2020, p. 383). | Gal et al. 2020 (full text): the first quote cites Marr & Hagston |
| 83 | §4.1 L188 | "(p. 3)" | "(p. 4)" | Ridley & Pawlick-Potts 2021 (full text) |
| 84 | §4.1 L190 | "we must establish" | "I set" | R1; G7 |
| 85 | §4.1 L190 | Street quote, no page | "(p. 77)" | Street 2003 (full text) |
| 86 | §4.1 L190 | "established" | "found" | R1.29 |
| 87 | §4.1 L190 | "no general restructuring of human cognition is posited" | "I posit no general restructuring of human cognition" | R1 |
| 88 | §4.2 L198 | H sentence | Split into co-optation (H) and overreliance (O) | D2 |
| 89 | §4.2 L200 | "joint competence formulation … multiplies with … (MI)" | "multiplicative"; formula G = F × MI × (1 − O) stated; co-optation placed upstream | D2; R1.20; R3.1 |
| 90 | §4.3 L204 | "…is formalized into six core propositions" | "Six propositions formalize…"; "ontological status" → "status" | R1 |
| 91 | §4.3 Prop 1 | "Ontological Independence" | "Representation Independence" | R1.19; D1 |
| 92 | §4.3 Prop 2 | "suppressing regressive saccades" | "suppressing long-range regressive saccades" | Harvey et al. 2017 (full text): scrolling raises regression frequency, shortens reach |
| 93 | §4.3 Prop 2 commentary | 62-word broken sentence | Split into three sentences, wording kept | R1, R3 |
| 94 | §4.3 Prop 3 | "(Co-optation via Explanations and Framing)—model-generated" | "(Overreliance via Explanations and Framing). Model-generated" | D2; R1, R3 (dash) |
| 95 | §4.3 Prop 4 | "structural marks … is predicted to induce cognitive event boundaries" | "interface marks … facilitates cognitive event boundaries where the mark coincides with a transition in the process" | N2 (Zacks et al. 2009; Schwan et al. 2000) |
| 96 | §4.3 Prop 5 | "…for oversight. Still, successful … the joint, interdependent coordination" | ", but … the multiplicative, interdependent coordination" (corrupted "Still" repaired; A4) | R3.5; A4 |
| 97 | §4.3 Prop 5 commentary | "without calibrating trust" | "without that dwell predicting trust" | Cho & Lim 2026 |
| 98 | §4.3 Prop 6 commentary | Fused last sentence | Split; alignment with situation transitions added | Style audit; D1 |
| 99 | §4.4 L232 | "Cutting and Deterding's (2022)" | "(2024)" (issue year; online 2022) | Crossref; Bib note 8 |
| 100 | Table 4.2 P1 | "reduce regressive saccades"; indicator | "reduce long-range regressive saccades"; + regression amplitude | Harvey et al. 2017 |
| 101 | Table 4.2 P4 | "will serve as external perceptual cues that induce" | "will facilitate … beyond the segmentation the text's own transitions induce"; indicator adds an unmarked-transition comparison | N2; D1 (removes circularity) |
| 102 | Table 4.2 P6 | — | Load-bearing vs local errors | R3.3 |
| 103 | Table 4.2 P8 | "Framing-Induced Co-optation \| H → G \| … independently of" | "Overreliance \| O → G \| … controlling for" | D2; formal audit (under the product form, "independently" fails) |
| 104 | Table 4.2 P9 | "under H … co-opted by fluency" | "under O … overrelies on fluent output" | D2 |
| 105 | Table 4.2 P10 | "foster" | "increase" | R1 |
| 106 | Table 4.2 P12 | — | Proviso: experts already fixate decision spaces more in unmarked streams | N1 (P12 contradicts the product without it) |
| 107 | §4.4 L257 | "cognitive co-optation" | "overreliance" | D2 |
| 108 | §4.4 L257 | P12 falsifier | Conditioned on the proviso | N1 |
| 109 | §4.5 L263 | "A decision space operational rule is defined here, comprising four structural criteria" | "I define the operational rule by three structural criteria" | D1; R1 (passive) |
| 110 | §4.5 C1 | "most supervisory failures in agent oversight result from a timing mismatch" | "56% of the failure episodes … involved a timing mismatch" | Chen et al. 2026 (full text); G27 |
| 111 | §4.5 C2 | Anchoring to lexical markers or the reasoning trace | Task-level definition (expert names more than one viable alternative); lexical markers become cues; Turpin et al. (2023) on unfaithful CoT | R3.2; Turpin 2023 (abstract read) |
| 112 | §4.5 C3 | — | "coders annotate against a stated task" (C3 is relational) | R1.19 |
| 113 | §4.5 C4 | Criterion 4 | Recast as an alignment condition (your sentences on EST and Kumar kept); drafted rationale | D1 |
| 114 | §4.5 L270 | "no commercial platform marks Criteria 2 through 4" | "Criteria 2 or 3 … Among research prototypes, HiLDe marks Criterion 2…" | D1; R-B research |
| 115 | §4.5 L272 | "these four criteria … decision spaces are annotated by independent coders … (e.g., Cohen's;" | "three … independent coders with domain expertise annotate … (e.g., Cohen's κ;" | D1; R3.2; R1 (passive); κ restored |
| 116 | §4.6, §4.9 | "Section 2.2" for Rayner et al. (1998) (four sites) | "Section 2.1" | R1.8 |
| 117 | §4.6 L276 | "Crucially for oculomotor control" | "For oculomotor control" | R1 |
| 118 | §4.6 L276 | "of eye movements" | "of fixations" | Source unit |
| 119 | §4.6 L278 | "changes fundamentally" | "changes" | R1 |
| 120 | §4.6 L278 | "the decisive material divergence" | "the material divergence" | R1 |
| 121 | §4.6 L280 | "…at the leading edge. In contrast, the mark persists, dispersing gaze…" | "…at the leading edge while the mark persists, dispersing gaze…" (the Table 4.2 P2 wording) | R3.5 (corruption) |
| 122 | §4.7 L284 | "(2009, Exp. 3) demonstrated that shifts … predict where readers place event boundaries. Each additional…" | Segmentation result = Exp. 1; reading-time figures = Exp. 3 | Zacks et al. 2009 (full text) |
| 123 | §4.7 L284 | "We interpret" | "I interpret" | G7 |
| 124 | §4.7 L286 | "Readers continued to place event boundaries above chance, demonstrating" | "Readers' coarse and fine boundaries remained aligned (smallest t(26) = 2.97), demonstrating" | Zacks et al. 2009 |
| 125 | §4.7 L288 | "This dynamic clearly departs" | "clearly" cut | Style |
| 126 | §4.7 L290 | "placing a mark at a functional decision space serves as…" | "+ that coincides with a transition in the process" | N2; D1 |
| 127 | §4.8 L294 | "(Rayner, 1998, as cited in Schotter et al., 2014)" | "(Rayner, 1998)" | R1.13 |
| 128 | §4.8 L296 | "Timkey … showed that forward fixations reflect … In contrast, regressive rereading…" | One sentence, "explains forward fixations … but not regressive rereading" (the v1 wording) | Style audit (corruption) |
| 129 | §4.8 L298 | — | "; readers of such text regress more often but over shorter distances (Harvey et al., 2017)" | Harvey et al. 2017 |
| 130 | §4.9 L308 | "However, this effect was no longer significant after multiple-comparisons correction (FDR), and statistical power was 52%" | Caveat moved to the interaction it belongs to | **Misreport corrected**: Tsoukala et al. 2025 (full text); the main effect was p < .001 |
| 131 | §4.9 L314 | "fundamentally shapes" | "shapes" | R1 |
| 132 | §4.9 L316 | "…prompts deliberate decoding. In contrast, for expert supervisors…" | "…, whereas for expert supervisors…" (the claim stays inside "The model proposes") | Style audit (corruption) |
| 133 | §4.10 L324 | "(§3.4)" for Cho & Lim | "(their §3.4)" | Formal audit (own vs cited sections) |
| 134 | §4.10 L324 | "(2010, p. 403)" | "(2010, p. 402)" | Parasuraman & Manzey 2010 |
| 135 | §4.10 L324 | "Manzey et al., 2008" | "Manzey, Reichenbach, & Onnasch, 2008, as cited in Parasuraman & Manzey, 2010" (+ reference entry) | E4; R1.31 |
| 136 | §4.10 L324 | "(§5)—an external visual mark…" | "(abstract). In other words, an external visual mark…" (the gloss separated from the quote; the quote is in the abstract) | Citation audit; style audit |
| 137 | §4.10 L326 | "persuasive co-optation"; "low-co-optation baseline" | "overreliance"; "low-overreliance" | D2 |
| 138 | §4.10 L326 | "definitively falsified" | "falsified" | Style |
| 139 | §4.11 L330 | "To delineate theoretical boundaries, interface marking should be differentiated from" | "Interface marking differs from" | R1 (passive) |
| 140 | §4.11 L332 | "(§3.2)" | "(their §3.2)" | Formal audit |
| 141 | §4.11 L332 | "decreased (0.48 vs 0.64, d = 0.36), although participants reported lower satisfaction and trust, and perceived the designs as more complex (Table 3)" | "+ on the carb-source detection task … rated the designs as more complex; differences in trust and preference were not significant (their Table 3)" | **Misreport corrected**: Buçinca et al. 2021 (full text) |
| 142 | §4.11 L332 | "The essential distinction" | "The distinction" | R1 |
| 143 | §4.11 L334 | "a small obstacle before an interaction" | "a small obstacle prior to an interaction" | **Misquotation corrected**: Cox et al. 2016 (full text) |
| 144 | §4.11 L338 | "(§2.3)", "(§7.9)" | "(their §2.3)", "(their §7.9)" | Formal audit |
| 145 | §5 L346 | "(G=FMI, before the depressive drag of co-optation H)" | "(G = F × MI × (1 − O), with co-optation acting upstream…)" | D2 |
| 146 | §5 L348 | "Technical systems do not merely deliver…" (two sentences) + "this theoretical perspective" | Two sentences cut (kept under "Cut from v2", C); "the theory" | R1, R3 (platitude-moral shape) |
| 147 | §5 L348 | "examines the theoretical scope … extending to agentic and embodied decision environments" | "sets the scope … for agentic coding environments" | D3 |
| 148 | §5.1 L352 | "(2022, §5.1)" | "(2024, §5.1)" + VERIFY page | C10 |
| 149 | §5.1 L352 | "decisive obligation" | "obligation" | R1 |
| 150 | §5.1 L354 | "(N = 42) … medium effect size f = 0.22 … N = 32 … Recruiting N = 42" | "(N = 50) … small-to-medium … N = 40 … Recruiting N = 50" | R1.24; recomputed: f = .22, N = 32 → power .763; N = 40 → .858 |
| 151 | §5.1 Condition 2 | — | Excludes situation-model transitions too | Formal audit (contamination); D1 |
| 152 | §5.1 Condition 3 | "four-part … and Situation Model Transitions" | "three-part"; C4 removed | D1 |
| 153 | §5.1 L360 | "Stimulus domains are counterbalanced … using a 3 x 3 Latin square design" | "A 3 × 3 Latin square counterbalances stimulus domains" | R1 (passive) |
| 154 | §5.1 L360 | Error-classes sentence + "To prevent Condition 3 from winning trivially … half … within designated decision spaces … half … at non-decision intervals" | Load-bearing vs local errors mapped onto your two error classes; distance-matching kept for local errors | R3.3; formal audit (contradiction with C3) |
| 155 | §5.1 L362 | "we measure" | "I measure" | G7 |
| 156 | §5.1 L364–369 | Four RQs | Three. Old RQ3 (mid-clause, exploratory) removed (now the follow-up in the D5 paragraph); RQ4 → RQ3 | R1.22; D5 |
| 157 | §5.1 RQ2 | "seeded factual and inferential errors" | "seeded load-bearing and local errors" | R3.3 |
| 158 | §5.1 L371 | "Process and outcome measures are recorded concurrently. We capture eye movements" | "I record process and outcome measures concurrently, capturing eye movements" | R1; G7 |
| 159 | §5.1 L373 | "the rate at which token delivery stays ahead of 99% of readers' comfortable reading speeds, to optimize server compute, and found thresholds" | SRAR defined as the source defines it | **Misdefinition corrected**: Xiao & Yang 2025 (full text) |
| 160 | §5.1 L373 | "we calibrate" | "I calibrate" | G7 |
| 161 | §5.1 L375 | "only two studies of conversational chatbot streaming displays…" | "few studies … Bhat; Park & Lee (chatbots); Su et al. (2026, preprint) (code)" | N5 |
| 162 | §5.1 L375 | "of the two streaming studies" | "of the two chatbot studies" | Follows Δ161 |
| 163 | §5.2 L379 | "a fundamental shift"; "a theatrical performance of thought" | "fundamental", "theatrical" cut | R1, R3 |
| 164 | §5.2 L379 | Bold sentence | Bold removed | R1.26 |
| 165 | §5.2 L381 | "the four operational criteria" | "the three … and its alignment condition" | D1 |
| 166 | §5.2 C1 | "under the guise of" | "in the name of" | R1 (polemic) |
| 167 | §5.2 C2 | "behind a facade of synthetic confidence" | "behind a single confident recommendation" | R1 |
| 168 | §5.2 C2, C3 | "An algorithmate interface"; "An algorithmic interface" | "A marked interface" (both) | R1.26 |
| 169 | §5.2 C4 | "(Criterion 4)" | "(Alignment Condition)" + one sentence: these marks aid comprehension, not decision spaces | D1; R1 (§5.2 pattern 4) |
| 170 | §5.2 L388 | "Crucially," | cut | R1, R2 |
| 171 | §5.2 L388 | "As Prajod et al. (2026) demonstrated, dense, explanatory disclosures often induce visual avoidance, whereas minimal, well-calibrated typographical cues successfully direct gaze without inflating cognitive fatigue." | Rewritten to the source's finding + "form must be tested" | **Reversed finding corrected**: Prajod et al. 2026 (full text via agent); C7 |
| 172 | §5.2 L388 | "relentless forward motion" | "forward motion" | R1 |
| 173 | §5.3 heading | "Beyond the Text Stream: Agentic and Embodied Decision Environments" | "Scope: Agentic Coding Environments" | D3 |
| 174 | §5.3 L392 | "extend far beyond"; "merely the most visible" | "far" and "merely" cut | R1 |
| 175 | §5.3 L396 | "four-part" | "three-part" | D1 |
| 176 | §5.3 bullet 4 | "It must punctuate transitions … (Criterion 4)" | "should … so that marks fall where the situation changes (Section 4.5)" | D1 |
| 177 | §5.4 L414 | "formidable" | "substantive" | R1, R3 |
| 178 | §5.4 L414 | "deserve a rigorous, dialectical defense" | "deserve an answer" | R1 |
| 179 | §5.4 L416 | "Friction Reactance and the Tyranny of Convenience" | "Reactance to Interface Friction" | R1, R2, R3 |
| 180 | §5.4 L420 | "built on the worship of velocity … design against human nature" | "built on velocity … design against what users prefer" | R1 |
| 181 | §5.4 L424 | "the decisive rebuttal" | "the rebuttal" | R1 |
| 182 | §5.4 L426 | "an exhausting cognitive double-bind" | "a double-bind" | R1 |
| 183 | §5.4 L426 | "When an interface strips away every visible seam, it does not liberate the human supervisor; it disarms them—marking restores the seam, transforming an overwhelming kinetic chase into a legible, navigable collaboration." | Replaced by the drafted Bainbridge / Lee et al. passage, which keeps "strips away every visible seam" and "restores the seam" | D8; R1.28; R2, R3 |
| 184 | §5.4 L430, L438 | "(G=FMI)" | "(G = F × MI × (1 − O))" | D2 |
| 185 | §5.4 L432 | "decisively corroborate … landmark study … proved" | "corroborate … study … found" | R1.29 |
| 186 | §5.4 L434 | "fundamentally a political struggle" | "fundamentally" cut | R1 |
| 187 | §5.4 L436 | "essential boundary conditions" | "boundary conditions" | R1 |
| 188 | §5.4 L438 | "Crucially," | cut | R1 |
| 189 | §5.4 L438 | "utterly incapable" | "incapable" | Style audit |
| 190 | §5.4 L440 | "Simmel, 1902b" | "Simmel, 1902" (only Part II is listed; Part II holds the tertius) | R1.27; Simmel 1902 (full text) |
| 191 | §5.4 L440 | "locating those choices, refusing blind compliance, and reclaiming human agency within an automated world" | "locating those choices and refusing blind compliance" | R1 (moral triplet closer) |
| 192 | §6 L446 | "In contrast, a streamed response" | "A streamed response" (the added marker broke the echo of "finished text") | Style audit (corruption, class b) |
| 193 | §6 L448 | "(G=FMI)" | "(G = F × MI × (1 − O))" | D2 |
| 194 | §6 L448 | "endorse fluent assertions regardless of factual accuracy (Kim et al., 2025)" | "accept explained answers whether or not they are correct" | Kim 2025 tested explanations |
| 195 | §6 L450 | "where decision points are presented" | "where the process binds their intent" (Prop 1) | R3.9 |
| 196 | References | Cutting & Deterding (2022) | (2024) | Crossref |
| 197 | References | Oberschelp entry | Editors added | R-F research |

## What I did not change (still yours)

- Every `[FLAG …]` sentence: 22 sites, including the scriptio continua history (B1.5, B1.7, B2.2), Metzner, Gould (L310), Prajod (L312), Buçinca (L420), "verification tax" (B1.4), and the A14 "puzzle".
- The 18 `[VERIFY…]` items: sources read only by agents or only as abstracts, pages to confirm, and the Copilot Workspace / Deep Research citations.
- Figure 4.1 needs redrawing to match D1/D2 (see the [FIGURE] note in §4.2).
- Style: emphasis markers and polemic were cut. Relation markers ("Furthermore", "Moreover", "Additionally") were kept, because your style file calls them ordinary venue usage. Your read-aloud is the last gate.
