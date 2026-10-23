# Open issues log — "Spaces in the Stream"

> **Started 21 October 2026, at Roger's request:** "document all these issues and we will come back to them at the end."
> - This is the single place to work from. Each item says where it lives, what is wrong or undecided, the source value where there is one, and the file holding the detail.
> - Nothing listed here has been changed in Roger's own text.
> - Mark items done with ✅ and the date.

**Files referred to:**
- `abstract_intro_edit.md`: your 20 October intro, with flags F1–F17.
- `DRAFT_full_v1.md`: full Claude draft with your new intro, flags D1–D28 and I1–I21, mismatches C1–C7.
- `SECTION2_redo.md`: the §2 redo, notes S0–S22.
- `SECTION3_review.md`: the §3 claim check and literature search.
- `SECTION3_full.md`: §3 draft, Notes 1–3.
- `FINAL_OUTLINE_HCI.md`: outline v4, with its decisions list.
- `../algorithmacy/COMPETENCY_MODELS.md`: the oracy, literacy and numeracy comparison.

---

## A. Decisions only you can make (theory-level)

| # | Issue | Where | Detail |
|---|---|---|---|
| A1 | **The rule for locating decision spaces**, the paper's central contribution. Confirm the four criteria (verifiable assertion ends; branching/action point; event or sub-goal shift; peak in Bayesian *surprise*, not surprisal), their order, and any rule for combining them. | §4.5 | Outline §5.1; S15/S19; Kumar et al. 2023 abstract: boundaries track Bayesian surprise "but not … surprisal" |
| A2 | **One definition of "decision spaces."** There are currently three: abstract, intro ¶4, §4.1. | Abstract, §1, §4.1 | I5 |
| A3 | **One definition of "algorithmacy."** There are currently three: abstract, intro ¶4, §4.1. | Abstract, §1, §4.1 | I14 |
| A4 | **Product (G = F × MI) or "joint operation."** The intro and abstract say "joint." §4.1, Figure 1, Proposition 5 and Table 1 P11–P13 say product. | Abstract, §1, §4 | I6, C3 |
| A5 | **The six propositions.** The intro's wording differs from §4.3, and propositions (4) and (6) carry placeholders. | §1, §4.3 | I19, C4 |
| A6 | **The intervention's name.** "Marking" collides with *visual marking* in vision science (Watson & Humphreys, 1997), which means inhibiting *old* items. Either distinguish the two in one sentence in §4.1, or rename the intervention. | §2.3, §4 onward | S12/S16; C7 |
| A7 | **"Literacy trap."** It's a keyword and is central in the intro, but undefined and absent from the body. Define it once, and search for prior uses. | Abstract, §1, body | I3, C6 |
| A8 | **"Idempotent"** (used four times) is the wrong term. Sampled generation is not idempotent. The contrast is with state-altering commitments, which would make the other side "side-effect-free" or "inconsequential." | §1 | I15 |
| A9 | **Figure 1 and Table 1:** accept, cut or redraw. P11–P13 need a measure of the model of the intermediary, or they become a research agenda. | §4.2, §4.4 | Outline decisions 3 and 10 |
| A10 | **Draft algorithmacy levels and domains:** keep, rewrite, or move to the dissertation. | §5.3 | Outline decision 11 |
| A11 | **Counterpoint 2 (the autonomous-model critique):** keep here or leave for the dissertation. | §5.4 | Outline decision 12 |
| A12 | **Form of the mark** (pause, white space, rule, label). | §4.9, §5.2 | Outline decision 6; D25 |
| A13 | **Title:** whether to keep "A Theory and Research Agenda." | Title | I1, D1 |
| A14 | **Conclusion's "puzzle."** The new intro no longer sets up a puzzle, so either restore one in §1 or change the conclusion. | §1, §6 | C5 |
| A15 | **Parkes's "grammar of legibility":** adopt only after reading chapter 3. | §2.1 | D5, S11 |
| A16 | **Your dissertation cases** for §5.3 (ranking, dispatch, screening), with sources. | §5.3 | DRAFT §5.3 [NEEDS] |
| A17 | **Prediction that marking matters more for novices:** find a source, or keep it explicitly as a hypothesis. | §4.9 | DRAFT §4.9 [NEEDS] |
| A18 | **New costs to engage.** Event boundaries "transiently disrupt" monitoring (Zacks, 2020, p. 172), and Kang & Muter (1989) found moving text kept literal comprehension. Both bear on P7, P10 and §5.4. | §4.9, §5.4 | S14; §3 review B15 |

## B. Wrong or overstated facts in your own text (flagged, not changed)

### B1. Abstract and Introduction (your 20 October version, in `DRAFT_full_v1.md`)

| # | Text | Problem and source value | Flag |
|---|---|---|---|
| B1.1 | "depletes working memory … conflates syntactic fluency with validity" | No source measured this. Bhat (2025) found perceived effectiveness unchanged (F = 0.16, p = .69), which cuts against "conflates." Anderl et al. (2024) is partial support only: discernment fell in 1 of 2 experiments. | I4, D3 |
| B1.2 | "Industry discourse routinely frames…" | No source. | I7 |
| B1.3 | "empirical investigations … fundamentally disrupts" (Park & Lee) | One study (N = 36); "fundamentally" overstates it. | I8, F3 |
| B1.4 | "verification tax … consuming working-memory buffers (Kim; Parasuraman & Manzey)" | Neither source measures working memory or a verification cost. | I9 |
| B1.5 | Scriptio continua paragraph | "devoid of word spaces, punctuation, or paragraph divisions"; "intended exclusively for oral recitation"; "broken only when seventh-century Insular scribes…". Johnson (2000, pp. 593, 608–609) says ancient silent reading was ordinary, early Roman literary texts separated words, and Greek rolls marked sentence ends. Saenger's own thesis puts common silent reading "by the fourteenth century" (p. ix). | I2, I10, I11, S3, S4 |
| B1.6 | "(Bhat, 2025; Kim et al., 2025)" for users being expected to proofread | Neither paper says this. | I12 |
| B1.7 | "ancient monks" vs "classical Greco-Roman antiquity" | Period mismatch. | I13 |
| B1.8 | "indiscriminate cognitive tax … before model access or after task completion … confirmation modals" | Collins et al. and Arun & Fischer study *selective* friction. None of the four cited works places friction after completion, and none uses modals. | I16 |
| B1.9 | "(Kim et al., 2025; Tatasciore et al., 2026)" for explainability dashboards | Tatasciore studies transparency in a UV task, shown with the recommendation, not after generation. | I17 |
| B1.10 | "no current framework identifies, models, or visually marks…" | Use the rule's form, and narrow the claim: WaitGPT (Xie et al., 2024) structures a code stream. See the §3.5 wording. | I18 |
| B1.11 | Roadmap: "ergonomic moderators (4.9–4.11)" | Only §4.9 is about moderators. | I20 |
| B1.12 | In-text "Arun et al." | Should be "Arun & Fischer." The reference list is already fixed. | I21 |

### B2. Section 2 (your rewrite)

| # | Text | Problem and source value | Flag |
|---|---|---|---|
| B2.1 | "declined by 44% to 54% for single sentences and by 58% for extended passages" | Rayner et al. (1998): 54% sentences and 44% passages (Exp. 1, p. 1132); 58% in Exp. 2 (p. 1138). | §3 Note 3.1 |
| B2.2 | "interpuncts … imperial Latin scribes intentionally abandoned word division to emulate the esteemed Greek convention" | Johnson (2000, pp. 608–609) gives word separation, then that the Romans "chose to discard word spaces." No interpuncts and no motive appear there. | Note 3.2 |
| B2.3 | "pre-attentive visual processing" (twice) | No source in the library uses the term. | Note 3.3 |
| B2.4 | "up to 20% to 25% under complex syntactic or conceptual demands" | Booth & Weger's 15–25% is a general estimate (citing Rayner & Pollatsek, 1989). | Note 3.4 |
| B2.5 | Metzner: "triggers immediate regression and a P600"; "readers without regression opportunities default to…" | Regressions were *associated* with the P600, and the comparison was trials with versus without regressions. | Note 3.5 |
| B2.6 | Wolfe: "suppressing the user's capacity…", "preventing the priority map from resetting" | Wolfe proposes this ("may get reset"); no study has tested it. His source names are "prior history" and "reward." | Note 3.6 |
| B2.7 | Kumar: "confirms that event boundaries reflect structural shifts in the underlying state space" | The paper says the results "support the hypothesis that prediction error serves as a control mechanism." | Note 3.7 |
| B2.8 | O'Regan & Noë: "readers often fixate…"; "becomes inevitable" | One informal example (p. 955). Use "can" and "more likely." | Note 3.8 |
| B2.9 | Mangen: "tactile boundaries" | Their phrase is "material placeholders." | Note 3.9 |
| B2.10 | Closing sentence of §2.5: "systematically dismantle…" | States the hypothesis as a finding. | Note 3.10 |
| B2.11 | "regions … for visual object and scene recognition" | Supported (Dehaene & Cohen, 2007, p. 393). Motor, spatial-tracking and tactile circuits are not (an earlier version). | S1 |

## C. Claude-drafted sections: items to settle

| # | Issue | Where |
|---|---|---|
| C1 | §2.1 still opens with your earlier Saenger and Parkes sentences, which duplicate intro ¶3. | DRAFT §2.1; superseded if `SECTION2_redo.md` or your rewrite replaces it |
| C2 | Two first authors named Zhu in 2026. In-text citations need initials: **H. Zhu** (pacing) and **X. Zhu** (verifiability). | §1, §3 |
| C3 | §3 runs to about 3,300 words against a budget of about 2,000; §2 to about 4,000 against about 2,800. Decide whether to cut. | §2, §3 |
| C4 | The experimental parameters in the outline have no source or justification: N = 42; 18 words/s, which is above Xiao & Yang's 11.97 for complex text; ≥250 Hz; 750 ms; 0.5 pt rule. | §5.1, §5.2; D26, D24, F2 |
| C5 | Table 2 (competence matrix): the oracy and numeracy cells have no source. | §4.1; D20 |
| C6 | Oberschelp (1995) is unread, so the draft says nothing about how he uses the word. | §4.1; D21 |
| C7 | Prajod et al. (2026): the finding runs the other way from the outline. The one-line label drew *more* fixation. | §4.9; D25 |
| C8 | Gould et al. (2016): the outline's millisecond values for lockouts are unverified (abstract only). | §4.9, §5.2; D24 |
| C9 | Keenan (1984) was misused for user reactance and has been dropped. | §5.4; D28 |
| C10 | Cutting & Deterding page for "severe testing": the copy I have is unpaginated at that point. | §5.1 |

## D. Sources to get in full

### D1. Section 2

| Priority | Source | Why |
|---|---|---|
| 1 | Saenger (1997), chapters 1 and 4 (pp. 1–17, 83–99) | The founding analogy rests on them; only the front matter has been read. |
| 2 | Knox (1968), *GRBS 9*(4), 421–435 (free from the GRBS archive) | Only an AI summary was supplied, and it misattributes the Ambrose argument (S5). |
| 3 | Gavrilov (1997), *Classical Quarterly 47*(1). https://doi.org/10.1093/cq/47.1.56 | The Augustine reinterpretation; eye–voice span. |
| 4 | Parkes (1992/2016), chapter 3 | Only if you use "grammar of legibility." |
| 5 | Dehaene et al. (2015); Kurby & Zacks (2008) | Cited; abstract only. |
| 6 | Huff, Papenmeier & Zacks (2012) | Cost of boundaries to monitoring; record not yet verified. |

### D2. Section 3 (cited, held only as abstract or record)

- Gnewuch et al. 2022
- Tan et al. 2026
- Kang & Muter 1989
- Harvey et al. 2017
- Harvey & Walker 2018
- Sharmin et al. 2016 (pages too)
- Goddard et al. 2012
- Lee & See 2004
- Endsley 2017
- Steyvers et al. 2025
- Zhou et al. 2024
- Lee et al. 2025
- Vasconcelos et al. 2023
- Fok & Weld 2024
- Ghosh et al. 2026 (results)
- Kim et al. 2024
- Danry et al. 2023
- Collins et al. 2024
- Arun & Fischer 2026
- Wu et al. 2025
- Cao & Huang 2022
- Glassman et al. 2024
- H. Zhu et al. 2026 (record only)

DOIs for all of these are in `SECTION3_full.md`.

### D3. Found in the search, to read before citing

| Source | Where it would go |
|---|---|
| Si et al. 2024, NAACL. https://doi.org/10.18653/v1/2024.naacl-long.81 | §3.3 |
| Reber & Schwarz 1999. https://doi.org/10.1006/ccog.1999.0386 | §3.3, as the basic-science anchor for fluency |
| Bainbridge 1983. https://doi.org/10.1016/0005-1098(83)90046-8 | §3.2 |
| Spatharioti et al. 2025, CHI. https://doi.org/10.1145/3706598.3714082 | §3.3 |
| Magentic-UI (Mozannar et al., 2025). https://doi.org/10.48550/arXiv.2507.22358 | §5.2 |
| Inhoff et al. 2019, *Vision*; Wilcox et al. 2024, *Cognition* | §2.2 (regressions) |
| Sharmin, Špakov & Räihä 2015 | Dropped; restore only if the full text confirms the direction of the finding. |

### D4. Sections 4 and 5 (from earlier work)

- Oberschelp (1995)
- Gould et al. (2016): open-access copy at Birmingham
- Duke & Cartwright (2021): pages
- Watson & Callingham (2003): reread
- Hoover & Gough (1990), Scribner & Cole (1978): abstract only
- Najjar & Nasir (2026), Kazemitabaar et al. (2024): abstract only

## E. Reference list housekeeping

| # | Issue |
|---|---|
| E1 | Your §1 reference list lacks all 31 sources cited in §2. The verified entries are in `SECTION2_redo.md` and `DRAFT_full_v1.md`. |
| E2 | Build one merged master list for §§1–6 at the end. Every in-text citation must resolve to an entry, and every entry must be cited. |
| E3 | Entries still incomplete: Sharmin et al. 2016 (pages); Duke & Cartwright 2021 (pages unverified); Parkes (pick an edition; only the 2016 reissue has a DOI); Gibson (1979 edition has no DOI; the 2014 edition does); Knox (no DOI; add the URL). |
| E4 | Secondary citations should read "as cited in": Rayner & Pollatsek 1989, Manzey et al. 2008, Wilkinson 1965, Michael & Lupton 2016, Balogh 1927, Watson & Humphreys via Wolfe (now read directly). |
| E5 | Run `auditing-citations` on the final list before submission. |

## F. Superseded flags (for the record)

- **F1–F17** applied to your 20 October intro, now replaced. Those still live are carried above: F3 → B1.3, F16 (scriptio vs scriptura; Saenger himself writes *scriptura continua*) → pick one term, F17 → B1.5.
- **D1–D28** applied to the outline-based draft. Those still live are carried above.
- **D2** ("we" vs "I") is resolved: your new abstract uses "I."

## G. Proposed §3 opening paragraph (added 22 October 2026)

| # | Phrase in the proposed opening | Problem | What the source says / what to decide |
|---|---|---|---|
| G1 | "psychophysical evidence established in Section 2—that critical human oversight depends on…" | §2 is evidence about reading and event perception. It shows nothing about oversight, so this states the paper's hypothesis as a finding (same issue as B2.10). "Psychophysical" is also the wrong label: the studies are eye-movement, visual-search and event-cognition work. | Write "Section 2 suggests…", or say the reading evidence motivates a claim about supervision. |
| G2 | "unhurried regressive inspection" | No §2 source says "unhurried." Schotter et al. (2014) show that blocking regressions lowers comprehension; that is about whether rereading is possible, not about its pace. | Say "the chance to regress." |
| G3 | "does extensively investigate the rate of token delivery" | "Extensively" is an overclaim. The studies are few: Tan et al. 2026; Anderl et al. 2024; and Gnewuch et al. 2022, which tested typing delays, not tokens. | Cut "extensively." |
| G4 | "researchers treat the user not as a supervisor… but merely as a reader" | Wrong for automation research: Parasuraman & Manzey (2010) and Endsley treat the operator as a monitor or supervisor. Also wrong for WaitGPT (Xie et al. 2024), whose title says "monitoring and steering," and for Magentic-UI (co-planning, action guards). It also contradicts Roger's own point that interfaces already offer steerable moments. | Narrow the claim (see G5). |
| G5 | "entirely ignoring its internal architecture" | Contradicted by WaitGPT, which structures the code stream into units. The gap claim must take the form "I found no work that…", narrowed to streamed natural-language responses and to placement by decision points (§3 review item 9). | Rewrite as a novelty claim with sources. |
| G6 | "latent decision spaces where algorithmic commitments are made and human intent must intervene" | This puts decision spaces inside the model. The memory definition places them at points in the process where human judgment is required. It is a third wording of the definition. | Ties to A2: one definition, held fixed. |
| G7 | "As we will see", "We consider" | The paper is single-author and the abstract uses "I." | Change to "I." |
| G8 | "ultimately obscures" | Research does not obscure cognitive demands; at most it leaves them unexamined. | Pick a verb the evidence supports. |
| G9 | Roger's new argument: platform steering moments (Claude Code plan mode and AskUserQuestion; ChatGPT follow-up offers) are performative and engagement-driven | The claim about intent ("the goal… is to keep them engaged") has no source. The Claude Code tool rules also cut against it: ask only when blocked, avoid excessive questions. The claim about effect does not need motive: the system chooses where the choice appears, writes the options and ranks them ("(Recommended)" first). That is choice architecture and co-optation. | Decide between the motive claim (needs evidence such as engagement metrics, product statements or sycophancy research) and the effect claim (needs only a description). Cite Anthropic or OpenAI product documentation, not system prompts. |
| G10 | Meter and tone analogy (**corrected 22 Oct: Johnson does not contrast smiley and word space; see G17**) | Supported by Johnson (2000). On p. 620 the bookroll was a "performance script," read as "entertainment," with pause and tone left to the reader-performer. On p. 608 the e-mail smiley face is a tone marker added to serve an existing reading system, and the Greeks did not adopt word spaces because "habits like scriptio continua… worked." | Usable as the anchor for the stakes paragraph. The analogy should say "marking tone serves the performance-reader; spacing changes who can read." |
| G11 | "Claude Code started the decision space move" | Not supportable. Copilot Workspace (spec and plan steering), OpenAI deep research (clarifying questions), WaitGPT (2024) and Magentic-UI (2025) staged decisions too. Several came earlier. | Frame Claude Code as the best-documented case, not the origin. |
| G12 | Plan-mode launch date | First changelog mention v1.0.33, 23 June 2025. A secondary blog says v1.0.16, 6 June 2025. | Use "by June 2025" unless a primary source turns up. |
| G13 | "(Recommended)" first option in AskUserQuestion | Visible only in the tool instructions in session; no public documentation found. | Describe only what the user sees, or find a public source. |
| G14 | Plan prompt: "Include only your recommended approach, not all alternatives" | Known only via Ronacher (17 Dec 2025), who quotes the prompt. | Cite as "as of December 2025." |
| G15 | Conflict of interest | Claude drafted analysis of Claude Code; the paper was drafted with Claude Code. | Disclosure statement; T&F AI-use policy. |
| G16 | §2.4–2.5 cut version (`SECTION2_4-5_cut.md`) | Seventeen marked changes to Roger's text plus five cuts, each with its source. Three need a decision beyond accept or reject: ⟨3⟩, the claim that white space marks boundaries, has no source; ⟨7⟩, the claim that boundaries are computable from text, bears on A1; ⟨10⟩, O'Regan (2011), is unread. | Roger accepts or rejects each ⟨n⟩. |
| G17 | "Johnson's (2000, p. 608) distinction between the historical word space and the modern email emoticon" | Misreads Johnson. That framing was Claude's error, made in the 22 Oct reply and outline. On p. 608 Johnson puts the smiley and word spaces on the same side, as "obviously useful aids" that reading cultures adopt: e-mail adopted the smiley within a few years, while the Greeks did not adopt word spaces for centuries because scrolls already worked for their reading culture. As written, the line hands a reviewer the counterargument that stream readers do not need spaces either. | Cite Johnson for the mechanism; state the cue-versus-space contrast as the paper's own. |
| A19 | **Scope across interface stages.** Stage 1 is the chat stream; Stage 2 is the staged agent (plan, approve, menus); Stage 3 is autonomous by default (agent view, 11 May 2026; auto mode as default, 25 Sep 2026). Choose: (a) real-time supervision, Stages 1–2, with Stage 3 named in scope and §5.3; or (b) include Stage 3, which needs a new §2 strand. | Abstract, §1 scope, §5.3 | REVIEW_current_state.md §1 |
| G18 | Two definitions of the literacy trap: §1 ¶2 (proofreading the ribbon) and §3 ¶1 (selecting from system menus). | Define it once, as a supervisory task handed over as a reading task, and argue that it moves across the stages. Ties to A7. |
| G19 | Proposition 2 (leading-edge capture) is specific to Stage 1. Tool calls now collapse by default, and Stage 3 has no watcher. | Scope or restate. |
| G20 | §1 ¶6 omits staged approval. "No current framework…" contradicts §2.1 and §3. | Add staged approval; narrow the gap claim (B1.10). |
| G21 | §2.1 counterargument: "entirely" is too strong (the plan is shown and editable; approval waits); "proprietary constraints" has no source; "ornamental" is undefined; the argument duplicates §3. | Concede, cite Ronacher for the pruning claim, and move the argument to §3 with a pointer left in §2.1. |
| G22 | §2.5: "the prompt demands immediate forward action." | Wrong for plan approval, which never auto-resolves. Use the dated fact: questions auto-continued by default until v2.1.200 (3 Jul 2026). |
| G23 | §5.1 stimulus | Include an agent transcript (Stage 2), not only a chat answer. |
| G24 | Doc edits E1–E10 (`DOC_EDITS_2026-10-22.md`): the intent-specification critique of platform decision points. | Roger applies them in the Google Doc; the connector is read-only. Open within them: "retention" needs a source (G9); "idempotent" now has two senses (A8); Stage 3 is not added (A19, leaning to (a)). |
| G25 | §3.1 drafted (`SECTION3_1_claude_code.md`). | Open: retention is not claimed (G9); plan-mode date is v1.0.33 (G12); Ronacher is "as of Dec 2025" (G14); Johnson p. 612 is paraphrased because the scan is cropped; the novice sentence is a hypothesis (A17); disclosure (G15). Copilot Workspace's date rests on the manual repository (created 23 Apr 2024). |
| G26 | §3.2 paragraph (Roger, 22 Oct) fact check | Anderl: the authors do not attribute the between-experiment discrepancy to framing, and their design cannot separate typing-out from conversational framing. Kang & Muter measured comprehension, not "word recognition." Haverkamp tested reader-controlled scrolling, not kinetic text. "Suppresses regressions" comes from Harvey et al. 2017, not Harvey & Walker 2018. Liu (Andes) does not "throttle"; and these are systems papers, not "measurement studies." The paragraph does not yet apply the §3 question (who places the decision point). |
| G27 | §3.3 paragraph (Roger, 22 Oct) fact check | P&M: about half of the misses in one study they review, not all errors. Goddard: "identified," not "confirmed"; position of advice is listed as a mitigator, and the gloss "how critically evaluated" is not in the abstract; Goddard also lists "information versus recommendation" as a mitigator, which supports the Gegoff sentence. Gegoff: the effect is small (.94 vs .93) and was measured on 96 participants. Tatasciore: 39–43% of trials is not "infrequently," and "does not mitigate this tendency" was not tested. Chen: "decisively" is unsupported (one preprint, N = 48). Lamb/Lee & See: Lee & See supplies the term only. Bainbridge has not been read. |
| G28 | §4 opening (Roger, 22 Oct) | Decision spaces get a fourth definition, where the system commits (A2). Menus are placed "on static displays," which merges §3.1 with §3.3. §1's roadmap still says 4.9–4.11. Oberschelp's 1995 use of "algorithmacy" is unacknowledged. "Pacing adjustments" does not fit "editorial deficit." |
| G29 | §3 as it stands in the doc (`REVIEW_sec3_doc_2026-10-22.md`) | §3.1: several Anthropic citations point to the wrong page (2026c–f are missing); 19 factual or wording errors, including plan mode called interactive mode, the "uninterrupted stream" origin story, "musical scores" for Johnson's simile, "nudges" attributed to the classifier, and a broken paragraph join. §3.2: complex/easy labels unverified; typo. §3.3: P&M, Goddard, "fundamentally," "rarely." §3.4: Ghosh miscited; workload claim rests on one study. §3.5: eye–mind hypothesis uncited; Cho & Lim measured trust only; Wu and Cao counter-evidence dropped. §3.6: the table has raw Markdown; the novelty sentence needs "I found no"; heading level is inconsistent. |

---

## H. Added 22 October 2026 (evaluation of reviews R1–R3; v2 draft)

> Sources: `REVIEW_EVALUATION_2026-10-22.md`, `RESEARCH_NOTES_2026-10-22.md`, `APPENDIX_A_changelog_verbatim.md`. "v2" means `DRAFT_v2_2026-10-22.md`.
> Items marked **(v2 default)** have a default already applied in v2 that you can reverse. "✅ v2" means fixed in v2 but not yet in the Doc.

### H1. Theory-level decisions (new)

| # | Issue | v2 default |
|---|---|---|
| A20 | **Third party in the coding triad.** §5.3 names worker / platform / consumer, but the coding case has no named counterpart (R1). | Drafted sentence naming the vendor (Simmel, 1902, p. 176), marked [DECISION D4]. |
| A21 | **H conflates two mechanisms.** Structural co-optation (Stark & Vanden Broeck: "leverages rather than delegates", p. 14) is not the same as overreliance on fluent or explained output (Kim 2025; Steyvers 2025). | **(v2 default)** Split into H (co-optation, which acts on where stops are placed) and O (overreliance). G = F × MI × (1 − O). |
| A22 | **Criterion 4** fails the definition, makes P4 circular, and contaminates the Condition 2 control. Bailey et al. (2017): segmentation depends on the reader's task. | **(v2 default)** Moved to an alignment condition; three criteria remain. Prop 1 renamed "Representation Independence". |
| A23 | **§5.3 platform labour.** "Mark" means two things; the section contradicts §1's bracketing. | **(v2 default)** Deferred to one paragraph; original text kept under "Cut from v2". |
| A24 | **Study design.** Condition 2 does not test P7; RQ3 was a hidden fourth condition; the seeded "non-decision" errors contradicted C3; P1, P8, P10 and P13 are untested. | **(v2 default)** Three conditions; tested and untested predictions now stated; load-bearing vs local errors; mid-clause pauses offered as a follow-up. |
| A25 | **P12 contradicts the product formula.** Equal ΔF gives a larger ΔG for high-MI users, so the gap widens (formal audit; no reviewer caught this). | Proviso added: experts already fixate decision spaces unaided. It is an assumption and needs evidence or an explicit "hypothesis" label. |
| A26 | **Marks alone may not create event boundaries.** Zacks et al. (2009): film cuts *lowered* segmentation once situation changes were controlled; Schwan et al. (2000). | Prop 4 / P4 made conditional on alignment. Read Schwan (2000) before keeping it. |
| A27 | **Prop 2 / P1: "suppressing regressions."** Harvey et al. (2017, full text): scrolling text *raised* regression frequency (52% vs 21%) but shortened its reach. | Restated as "long-range regressions". Decide whether Prop 2 should rest on reach rather than frequency. |
| A28 | **Novelty claim.** Closest prior art: Hippo (Pang et al., 2025), HiLDe (Anaya González et al., 2025), Glassman et al. (2024). Spatharioti et al. (2025) highlight uncertain numbers. | Gap narrowed to a typology plus marking for the supervisor (§3.6). Read the three preprints. |
| A29 | **Algorithmacy / algorithmic-literacy distinction.** Tankelevitch et al. (2024, CHI) already place "metacognitive monitoring and control" at the centre. | Drafted paragraph: the distinction rests on the triad, not on steering. |
| A30 | **Prior uses of "algorithmacy".** Oberschelp (1995, p. 121) uses it beside literacy and numeracy; Leese & Matzner (2016) is unpublished. **Your Substack (22 Feb 2026) says it "never appeared in a published academic text," which is wrong.** | Drafted acknowledgment in §4. Your Substack is yours to correct. |
| A31 | **Mark form may invite deference.** A 2026 preprint ("Not All Uncertainty Is Equal", record only) found that token-level uncertainty markers *increased* agreement. | One drafted sentence in §5.2 tied to P9. Find and read the source. |

### H2. Wrong or overstated facts found 22 October (flagged inline in v2 unless marked ✅)

| # | Where | Problem → source value |
|---|---|---|
| B3.1 | §3.1 L103 | ✅ v2. v2.1.283 "default … for enterprise and team tiers" is wrong. The default reached every plan and provider in v2.1.283–2.1.284; earlier it applied on Pro, Max and Team only (permission-modes.md L11, L220; changelog). |
| B3.2 | §3.1 L103 | ✅ v2. "Sixteen months" → nearly seventeen; "task list" → "Todo list"; "By late 2025" and "in late 2026" introduce August dates. |
| B3.3 | §3.1 L101 | ✅ v2. Queued messages could interrupt the turn from v2.1.275 (17 Sep 2026; send-now key). |
| B3.4 | §3.1 L111 | ✅ v2. "Classifier 'nudges'": the docs attribute nudging to auto mode (permission-modes.md L335). |
| B3.5 | §4.1 L169 | ✅ v2. "Platforms co-opt and enroll them" is not Stark & Vanden Broeck's wording; their line is passive ("on platforms they are co-opted", p. 5). "Coordinative co-optation" is your term. |
| B3.6 | §4.1 L186 | ✅ v2. Gal et al.'s "disappears within technological systems" (p. 380) cites Marr & Hagston (2007) and Straesser (2015), not Michael & Lupton (2016). |
| B3.7 | §4.1 L188 | ✅ v2. Ridley & Pawlick-Potts quote is on p. 4, not p. 3. |
| B3.8 | §4.9 L308 | ✅ v2. Tsoukala: the FDR / 52%-power caveat belongs to the interaction; the main effect was p < .001. |
| B3.9 | §4.11 L332, §3.4 L133 | ✅ v2 (L332); flagged (L420). Buçinca: 0.48 vs 0.64 is carb-source detection only; trust and preference differences were not significant; "frustrating" is not in the paper. |
| B3.10 | §5.2 L388 | ✅ v2. Prajod: the finding was reversed. The one-line label raised total fixation (an attentional cost); detailed disclosures "did not impose additional burden." |
| B3.11 | §4.9 L310 | Flagged. Gould: the paper's own title says *brief* lockouts encourage checking and *longer* ones task switching. |
| B3.12 | §2.1 L61 | Flagged; citation removed in v2. Johnson (2000) is cited for a landmark principle he argues against (p. 608). |
| B3.13 | §4.11 L334 | ✅ v2. Cox quote: "prior to an interaction". |
| B3.14 | §3.3 L123, §4.10 L324 | ✅ v2. Parasuraman & Manzey pages: 401 and 402. |
| B3.15 | §4.7 L284, L286 | ✅ v2. Zacks 2009: segmentation is Exp. 1, reading times Exp. 3; t(26) = 2.97 is the smallest t for coarse–fine alignment. |
| B3.16 | §5.1 L354 | ✅ v2. Power: f = .22 is not "medium"; N = 32 gives power .763; N = 40 is needed for .85; a 20% buffer means recruiting 50 (recomputed). |
| B3.17 | §5.1 L373 | ✅ v2 (definition); tokens vs words flagged. SRAR is the share of users whose comfortable speed ≤ the stream speed (Xiao & Yang). |
| B3.18 | References | ✅ v2. Zwaan & Radvansky (1998) and Manzey et al. (2008) were cited with no entry. Cutting & Deterding is 2024. Simmel "1902b" → "1902". |
| B3.19 | §2.5 L95; §5.1 L375 | ✅ v2. "No study tests an active streaming display" / "only two streaming studies": Su et al. (2026, preprint; code, N = 53) now exists. |

### H3. Status of earlier items in v2

- ✅ v2: A5 (placeholders); A8 (idempotent); B1.11 (roadmap); B1.12 (Arun & Fischer); B2.1 (Rayner figures); B2.9 (tactile boundaries); C2 (Zhu initials); E4 (Manzey "as cited in"); G7 (I/we); G12 (plan-mode date); G22 (timeout vs plan approval); G29 items (corrupted joins, nudges, raw Markdown in tables).
- Changed in v2 but still yours to approve: A2/A3 (one definition each; the abstract now reads "competence"), A4 (product), A6 (one drafted sentence distinguishing visual marking), A13 (title kept).
- Still open: A1, A7, A9 (Figure 4.1 must be redrawn for D1/D2), A10–A12, A14 (puzzle), A15–A19, every B1/B2 item flagged inline, C3 (length; v2 body is about 23.7k words including tables), C5, C10, D-list reading.
