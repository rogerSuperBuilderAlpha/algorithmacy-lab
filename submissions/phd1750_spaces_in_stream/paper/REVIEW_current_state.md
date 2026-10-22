# Review: does the critique address current LLM interfaces? (22 October 2026)

[CLAUDE-DRAFTED REVIEW NOTES. Nothing in your text has been changed. Sources gathered today are in `sec3/claudecode/`: the Claude Code docs, the CHANGELOG, and npm release dates.]

## 1. The diagnosis

The paper critiques three interfaces without saying they are three.

| Stage | What the user does | Where the paper critiques it | Dated anchor |
|---|---|---|---|
| **1. Chat stream** | Watches tokens arrive and proofreads them. | Abstract ("serial proofreader"), §1 ¶1–4, §2.2–2.5, Propositions 2 and 4, the eye-tracking agenda. | Park & Lee 2024; Bhat 2025; Andes (Liu et al. 2024). |
| **2. Staged agent** | Watches a log of tool calls and approves plans, commands and menus. | §2.1 counterargument (new), §2.5's new sentence on agentic halts, §3 opening (new). | Claude Code: plan mode by June 2025; "ask you questions more often in plan mode" from v2.0.21 (16 Oct 2025). |
| **3. Autonomous by default** | Does not watch. Dispatches tasks, is summoned when an agent "needs your input," and reviews the result. | **Nowhere.** | Agent view, v2.1.139 (11 May 2026): "watch their state at a glance instead of scrolling through transcripts, and step in only when one needs you." Auto mode as the built-in starting mode, v2.1.283 (25 Sep 2026). |

All Stage 3 quotations are from Claude Code's documentation (*Agent view*; *Permission modes*), and the version dates come from npm. Dates for other vendors are not verified.

**What follows from this.**
- **The intro and abstract critique Stage 1; §3 critiques Stage 2.** A reader will notice that the paper's evidence (§2) and its stimulus (the eye-tracking agenda) are Stage 1, while its sharpest critique (§3) is about Stage 2. A reviewer in late 2026 can say "you are critiquing ChatGPT in 2023."
- **There are now two definitions of the literacy trap.** §1 ¶2 has one: "packaging this computational process as an unbroken ribbon of text… cast in the role of an editor or proofreader." §3 ¶1 has another: "reducing human agency to selecting among system-curated alternatives." They describe different stages. **Recommendation:** define the trap once, as *a supervisory task handed to the user in the form of a reading task*. Then show that it **moves**: from proofreading the stream (Stage 1), to approving system-written menus (Stage 2), to reading a system-written summary after the fact (Stage 3). The constant is that the system places the decision points and the user reads. This answers A7 and turns the dating problem into the paper's argument: each generation removes more of the reading and none adds spaces.
- **Stage 3 changes the perceptual argument, so you have a scope decision to make.** In Stage 3 the stream is not watched, and what the user reads (a final summary, a diff, a "needs input" row) is *static*. Two consequences:
  - §2.5's instability argument (that text must stay put) does not apply to Stage 3.
  - §2.1's scriptio continua argument applies more strongly. The summary is a system-authored, undifferentiated text, and the decision spaces are compressed into it.

  **Decision (new A19):**
  - (a) Scope the paper to real-time supervision (Stages 1–2), and name Stage 3 in §1's scope paragraph and §5.3.
  - (b) Extend the claim to Stage 3, which means §2 needs one more strand. The relevant work is summary and review reading; I have not searched it yet.

  My recommendation is (a). The intro's scope paragraph already says "the perceptual layer of real-time interaction."

## 2. Section by section: what is dated and what to update

### Abstract
- "outputting tokens incrementally as an advancing visual stream… serial proofreader" describes Stage 1 only. Add one clause acknowledging that interfaces now also stop for approval and increasingly run unattended, and that the trap persists.
- "obscures latent algorithmic branching." Current models show some of this: extended thinking is always on for current Claude models (*Interactive mode*), and plan mode shows a plan the user can edit (Ctrl+G, *Permission modes*). The claim needs to say what remains hidden. The Ronacher (2025) source helps: the plan prompt says "Include only your recommended approach, not all alternatives." So the plan is shown, but the alternatives are not.
- "joint operation" is still open (A3/A4). "six propositions… thirteen predictions… three-condition eye-tracking" depend on A5 and A19.

### §1 Introduction
- **¶1:** "scrolling downward in real time… commanding the user's visual system to track an automated cursor" is Stage 1. It is fine as the opening scene if ¶4 or ¶6 then says the scene has changed. Park & Lee (2024) remains the only eye-tracking source, and it uses a chatbot.
- **¶4:** "Users are expected to supervise… through… post-hoc proofreading." In Stage 2–3 products, users are expected to approve, and then to leave the agent to work ("Yes, and use auto mode"). Update the description of what users are now asked to do.
- **¶6 (current strategies)** lists pacing, friction and explainability. It omits the vendors' own move, staged approval (plan mode, permission prompts, clarifying questions), which §2.1 and §3 now critique. As written, "no current framework identifies… decision spaces within the generative stream" contradicts your own §2.1 counterargument and §3 opening. Add staged approval to the list, and narrow the gap sentence (B1.10/G5).
- **¶7, Proposition 2:** "continuous token generation induces… attentional capture toward the kinetic leading edge" applies to Stage 1 only. In current agent interfaces, tool calls are collapsed by default ("Called slack 3 times," *Interactive mode*), and in Stage 3 there is no leading edge being watched. Scope P2 to displays that stream to a watching user, or restate it.
- **¶7, Proposition 3** ("presenting generative supervision as an act of reading co-opts human agency") covers all three stages and is the one to build on.
- **¶8 roadmap:** §3 is still listed as the old 3.1–3.5. It now runs 3.1 (the Claude Code case) to 3.6. §5.3 ("non-textual autonomous platforms") should also cover Stage 3 coding and research agents if you choose A19(b).

### §2 Foundations
- **§2 lead, last sentence:** "an autonomously advancing, server-paced kinetic stream." A current user can scroll back, interrupt (Esc keeps "the work done so far"), queue messages, and open a transcript viewer (Ctrl+O). The pacing claim stands, but say it is about default behaviour, and that inspection is available but has to be sought out.
- **§2.1 counterargument (new):** this is the right move. It now sits in the history subsection, though, and duplicates the §3 opening. **Recommendation:** keep a two-sentence pointer in §2.1 and move the argument to §3.0/§3.1, where the Claude Code evidence is. Specific claims:
  - "Current interface stops are ornamental because they operate entirely within a dyadic fiction." "Entirely" is too strong. The plan is shown and can be edited (Ctrl+G), and plan approval "never auto-resolve[s] on idle." Concede both, then make the point.
  - "the pruning of alternative solution paths" has a source: Ronacher (2025) quoting the plan prompt. Cite it, marked "as of December 2025" (G14).
  - "the weighting of proprietary constraints" has no source. Cut it, or find one.
  - "having occurred long before the confirmation dialog appears" is supportable for the plan (the alternatives are dropped at Phase 4 of the prompt). It is not established for permission prompts.
  - "ornamental" is a new term that §3 then reuses ("ornamental dyadic structure"). Define it once, or drop it.
- **§2.1 limitation 1** ("an externally regulated process determined by server computation") is true for Stage 1. In Stage 3 the problem is not pace but absence: the user is not present while the agent works and is called in at points the system chooses. Consider adding this as limitation 3, or folding it into A19.
- **§2.4–2.5** are still the pre-cut text. The cut version (`SECTION2_4-5_cut.md`, items ⟨1⟩–⟨17⟩) is unapplied, and B2.7–B2.10 remain.
- **§2.5 new sentence:** "the preceding generative reasoning remains scrolled out of view, truncated, or buried beneath execution logs, while the prompt demands immediate forward action."
  - "Buried beneath execution logs" fits Stage 2.
  - "Demands immediate forward action" is contradicted for plan approval, which waits indefinitely.
  - It was true for questions until v2.1.200 (3 Jul 2026). Before that, an unanswered question auto-continued by default (CHANGELOG). Use that dated fact instead; it is stronger.
  - "Truncated" needs an example or a source.

### §3
- **The opening paragraph is consistent with the outline and uses Johnson correctly** (pp. 608, 610). Three items:
  - "ornamental": see above.
  - "compliant readers" is evaluative. "Readers" is enough.
  - The definition of the literacy trap here differs from §1 (see §1 of this review).
- **The 3.1 case should run on the three stages** and use the outline's dated table. The table already covers Stages 2 and 3 (plan mode → questions → auto-continue → auto mode default). Add agent view (v2.1.139, 11 May 2026) and collapsed tool calls.
- **3.2 Pacing.** Andes, Xiao & Yang, and Zhu et al. study Stage 1 reading speed. The critique writes itself: the pacing literature optimizes reading comfort for a stage the products are leaving. Note one limitation of these papers: none models extended thinking, where long silent reasoning precedes the visible answer. That claim is inferred from their abstracts, so verify it before using it.
- **3.3 Automation supervision becomes more central, not less.** Stage 3 is the classic supervisory-control situation. A classifier model reviews the agent's actions (auto mode), so the human supervises a system that supervises a system. Bainbridge's ironies are the frame for this; check his wording first (G-outline 3.3).
- **3.4 Friction.** The vendor's direction (auto mode, for "reducing prompt fatigue") runs against the cognitive-forcing literature. That is a current-state contrast worth one paragraph.
- **3.5 Gaze.** Gaze cannot index supervision in Stage 3, because no one is looking. This strengthens §4.10.

### §4–§5 (from DRAFT_full_v1; not in your paste)
- **§4.5's locating rule (A1)** must say who locates the decision spaces in each stage. The point from Kumar et al. (2023) (that boundaries are computable from text) and the critique in §3.6 together force this.
- **§5.1, the three-condition eye-tracking study.** The stimulus should be an agent transcript (Stage 2), not only a chat answer, or the study will look dated on arrival.
- **§5.2 design implications:** add the "needs input" summons of Stage 3. Where the agent calls the user in, and with what text, is a marking problem.

## 3. Items already logged that remain in this text

These are unchanged in the paste; their IDs are in `OPEN_ISSUES.md`:
- B1.1–B1.12, including:
  - B1.5: the intro's account of scriptio continua ("intended exclusively for oral recitation," "broken only when seventh-century Insular scribes") contradicts your own §2.1, which says ancient readers could read silently (Johnson; Knox);
  - B1.7: "ancient monks."
- B2.1–B2.6 (§2.1–2.3) and B2.7–B2.10 (§2.4–2.5, via the cut file).
- A2, A3, A4 and A8: "idempotent" appears three times in §1.
- B1.11: the roadmap's "ergonomic moderators (4.9–4.11)."

## 4. Sources to add for the current state

| Need | Status |
|---|---|
| Claude Code docs: *Permission modes*, *Tools reference*, *Interactive mode*, *Agent view*, *Checkpointing*; CHANGELOG with npm dates | Downloaded and read today. Cite as product documentation, with the access date. |
| Ronacher (2025), "What actually is Claude Code's plan mode?" | Read today. |
| OpenAI deep research (clarifying questions); Codex or ChatGPT agent (background tasks, approval prompts) | **Not verified.** I have only help-centre and forum results; I need primary documentation with dates. |
| GitHub Copilot Workspace (spec and plan steering) | User manual found; **launch date unverified.** |
| Literature on reading summaries and reviewing diffs (Stage 3 perception) | **Not searched.** Only needed if A19(b). |
| Any empirical study of plan approval or menu choice in coding agents | **Not searched.** This would be the nearest empirical work to §3.1. One search round is worth running before the gap sentence is final. |

## 5. New log entries

- **A19**: scope (Stages 1–2 only, or include Stage 3).
- **G18**: two definitions of the literacy trap (§1 versus §3). Merge into one definition and argue that the trap moves.
- **G19**: Proposition 2 is specific to Stage 1.
- **G20**: §1 ¶6 omits staged approval, and its gap sentence contradicts §2.1 and §3.
- **G21**: in the §2.1 counterargument, "entirely" is too strong, "proprietary constraints" has no source, and "ornamental" is undefined; the argument also duplicates §3.
- **G22**: §2.5's "demands immediate forward action" is wrong for plan approval. Replace it with the dated auto-continue fact.
- **G23**: the §5.1 stimulus should include an agent transcript.
