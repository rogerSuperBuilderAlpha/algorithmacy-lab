# Section 3 outline, v2 (22 October 2026)

[CLAUDE-DRAFTED OUTLINE. Every line is mine; the sentences in the paper are yours to write. Each anchor gives its source and locator. Sources gathered today are in `~/phd1750-litreview/sec3/claudecode/`: the Claude Code docs pages, the CHANGELOG, npm release dates and Ronacher 2025.]

---

## 0. Where §3 sits in the whole paper

| § | Job in the argument | What §3 must hand it |
|---|---|---|
| 1 Introduction | States the problem: the stream as scriptio continua, and algorithmacy as the competence the stream demands. | — |
| 2 Foundations | Shows what readers need from a writing system: landing points, event boundaries, a stable object to return to. The Johnson (2000) frame is that a writing system fits a reading system. | §3 opens by applying §2's frame to a real interface. |
| **3 Current accounts** | **Shows that interfaces already offer decision points, then shows whose points they are.** One worked case (Claude Code), then four research traditions read with one question. | Hands §4 the gap: no account places marks at the user's decision spaces in a streamed natural-language response. Also hands it a contrast case for §4.11 ("what marking is not"). |
| 4 Theory | Defines decision spaces and marking, gives the propositions, and sets out the three mechanisms (4.6–4.8). | §4.5's locating rule must answer the case in §3.1: who decides where the mark goes. |
| 5 Discussion | Testing, design implications, extension to agents (5.3), counterpoints (5.4). | §5.2 can use the §3.1 case as its "before" picture. Counterpoint 2 (A11) can use the motive-versus-effect argument from §3.1. |
| 6 Conclusion | | |

**The one question §3 asks of every account:** *who places the decision point, who writes its options, and what does the user do there: select or locate?* Selecting from a menu the system has written is literacy. Locating where the stream commits you is algorithmacy.

---

## 3.0 Opening paragraph: stakes, not inventory (about 250 words)

Use the moves from 22 October, in this order:

1. **Concession.** Interfaces already stop the stream for the user. Anchor the point with the Claude Code features in 3.1 and with WaitGPT's "monitoring and steering" (Xie et al., 2024).
2. **Turn.** These decision points are placed, worded and ranked by the system. The user selects; the user does not locate.
3. **Analogy (corrected 22 Oct).** Not a Johnson distinction: he groups the smiley with word spaces and punctuation as aids a reading culture adopts when it feels strain (p. 608), and adopts slowly when it does not (p. 610). Use his mechanism, and own the contrast: the stream's reading culture adopts the aids its practice of watching needs (cues to approve), not the aids a different practice would need (spaces to locate).
4. **Stakes.** Interfaces that keep adding tone markers produce better readers of the stream (literacy), not users who can find where the stream commits them (algorithmacy). This is the literacy trap, which still needs a definition (A6).
5. **Roadmap.** One case (3.1), four traditions (3.2–3.5), one synthesis table (3.6).

Avoid every item in OPEN_ISSUES G1–G8. In particular: "I," not "we"; no "entirely ignoring"; no "psychophysical"; no "extensively."

---

## 3.1 A worked case: how Claude Code stages decisions (NEW; about 1,200–1,500 words)

**Why this case.** Claude Code publishes a dated changelog and full documentation, so I can describe every decision point, when it appeared and how its options are worded, from primary sources. Say this in the paper as the reason for choosing the case. Do **not** say Claude Code *started* the move. Earlier products did it first (3.1.5).

### 3.1.1 The reading surface

- The user watches streamed text interleaved with tool calls. The stream does not stop for the user unless the user stops it: `Esc` will "Stop the current response or tool call mid-turn so you can redirect. Claude keeps the work done so far" (Claude Code docs, *Interactive mode*, keyboard table).
- Messages the user types while Claude works are queued "instead of interrupting the turn" (*Interactive mode*, "Queue messages while Claude works"). The user's input waits for a break the system chooses.
- **§2 link:** this is the continuous scroll of §2.1 and §2.5. Interruption exists, but the user has to find the moment for it.

### 3.1.2 The decision points, with dates

| Decision point | First appears | Source |
|---|---|---|
| Task list ("helps it stay on track") | v0.2.93, 30 April 2025 | CHANGELOG; npm release date |
| Plan mode | First changelog mention v1.0.33, 23 June 2025 ("Improvements to plan mode"). A secondary blog dates its release to v1.0.16 (6 June 2025) and calls it a "stealth" launch; that claim is unverified. | CHANGELOG; npm |
| Opus used for planning, Sonnet for execution | v1.0.77, 12 August 2025 | CHANGELOG |
| Checkpoints and `/rewind` | v2.0.0, 29 September 2025 | CHANGELOG |
| "Claude will now ask you questions more often in plan mode" | v2.0.21, 16 October 2025 | CHANGELOG |
| A question **closes on its own** and Claude continues: auto-continue was on by default until v2.1.200, 3 July 2026, which "no longer auto-continue by default" | before 3 July 2026 | CHANGELOG; *Tools reference*, AskUserQuestion |
| "Yes, and switch to auto mode" added to Bash permission prompts | v2.1.247, 26 August 2026 | *Permission modes* |
| Auto mode becomes the **built-in starting mode** for every plan and provider | v2.1.283, 25 September 2026 | *Permission modes* |

The trajectory to argue: the product added decision points (2025) and is now removing them, with auto mode as the default (2026).

### 3.1.3 How the user is expected to take each decision

1. **Plan approval.** The menu's first option is "**Yes, and use auto mode**." The others are "Yes, manually approve edits" and "No, keep planning" (*Permission modes*, "Review and approve a plan"). Approving the plan by its first option removes the decision points that would have come after it.
2. **The plan arrives already narrowed.** The plan-mode prompt tells the model to "Include only your recommended approach, not all alternatives" (quoted in Ronacher, 2025, who read the prompt). The alternatives, which are the decision space, are closed off before the user sees anything.
   - **[Flag]** This is a practitioner blog quoting a prompt that may have changed since. Mark it as "as of December 2025."
3. **Questions.** The `AskUserQuestion` tool offers multiple-choice options that the model wrote. The user can type an alternative through "Other" (*Tools reference*).
   - **[Flag]** The rule that the recommended option goes first, labelled "(Recommended)," is in the tool's instructions as I see them in this session. I found no public documentation of it, so do not cite it unless a public source turns up. Describe only what the user sees.
4. **Auto mode** is described as for "reducing prompt fatigue." It "also nudges Claude to keep working without stopping for clarifying questions" (*Permission modes*). "Nudges" is the vendor's own word. A classifier model, not the user, reviews actions.
5. **What is kept.** Permission prompts, including plan approval, "never auto-resolve on idle" (*Tools reference*). This is the counter-evidence to the critique: the product does keep some decisions with the user. Say so.

### 3.1.4 Reading the case with Johnson (2000)

- **Reading as a system.** Johnson treats reading as "a sociocultural system in which the individual participates," not an individual cognitive act (p. 602; restated on p. 603). Claude Code's decision points belong to a reading system: an expert developer, alone, watching an agent work.
- **Performance script.** The bookroll was "played" like a stage performance, its reader a "reader-performer," and pause and tone were left to that reader (p. 620). The Claude Code stream is played too: the user watches a performance and is cued at moments the system chooses.
- **Tone markers versus spaces (corrected 22 Oct).** Johnson does not contrast the smiley with word spaces; he lists both as "useful aids" a reading culture adopts when it feels strain (p. 608), and slowly when it does not (p. 610). The contrast between a cue and a space is ours. Johnson's mechanism (a culture adopts the aids its practice needs) is what we cite. Claude Code's prompts, menus and status line are this kind of marker. They cue the watcher when to approve. They do not give the user a place to land and look back over a decision.
- **Closed specialist systems.** Johnson's prescription example: some reading cultures work "as closed systems" in which the script is written specialist to specialist (p. 612; the line is cropped, so check the page image before quoting). The Claude Code menus assume a developer who already knows which option is the decision. **§6 hook:** a novice cannot locate decision spaces in a menu written for experts.
- **Replay versus retrieval.** Excerpts of a roll "could be 'replayed'," but "nothing in the ancient bookroll was designed to facilitate retrieval in any other way" (p. 620). `/rewind` restores state to a point the user chooses, and its list is keyed to the user's own prompts, one entry per prompt sent (*Checkpointing*). That is replay by prompt, not retrieval by decision.
- **The claim to make (yours to word).** Claude Code gives its watcher tone and cue markers for a performance. It does not give spaces. The 2026 trajectory removes even the cues.

### 3.1.5 Precedence and the motive question

- **Earlier staged decisions.**
  - GitHub Copilot Workspace offered "two important moments where they can steer the system": edit the spec, then edit the plan (GitHub Next user manual). **[Flag]** The launch date is not verified; the search results conflicted.
  - OpenAI deep research asks clarifying questions before it starts (Fulford, OpenAI Forum session; Nielsen's first-impressions post). **[Flag]** The date of February 2025 is not verified.
  - WaitGPT (Xie et al., 2024) and Magentic-UI (Mozannar et al., 2025) come from research.
  - Ronacher (2025) reports that Amp "is removing" its plan mode, so vendors diverge.
- **Motive versus effect (G9).** Argue from effect: the system places the points, writes the options and ranks them. That is choice architecture and co-optation (Stark & Vanden Broeck). It needs no claim about engagement motive. If you want to keep the motive claim, it needs evidence the case does not supply. The vendor's own "nudges" and "prompt fatigue" support the effect claim only.
- **Disclosure, for you to decide.** The paper was drafted with Claude Code. I am Claude, so I am describing my own vendor's product. An HCI reviewer will want both facts stated, and T&F's AI-use policy will ask for the first.

---

## 3.2 Streaming and pacing (old 3.1)

- **Keep:** Tan et al. 2026 (latency); Anderl et al. 2024 (dynamic text lowered discernment in Exp. 2 only, p = .029; Exp. 1 p = .212; confounded with conversational framing); Gnewuch et al. 2022 (typing delays); Kang & Muter 1989 (counter-evidence).
- **The question applied:** these studies vary *how fast* the stream arrives. Nobody places a point in it. Pacing is the literal analogue of meter: a property of the performance.
- **Link back to 3.1:** Claude Code's stream has no pacing control either; the user's only lever is `Esc`.

## 3.3 Automation supervision (old 3.2)

- **Concede the point G4 requires:** this tradition does treat the operator as a supervisor (Parasuraman & Manzey 2010; Endsley; Bainbridge 1983).
- **The question applied:** designers fix where alarms and advice appear, in advance, in a fixed display (Goddard et al. 2012, on where advice sits on the screen). The operator responds to marks the designer placed. That is still selecting.
- **Link to 3.1:** Bainbridge's irony, in which automating the routine leaves the human the hardest monitoring, is the auto-mode default of September 2026. Check that Bainbridge's wording supports this before using it.

## 3.4 LLM overreliance and friction (old 3.3)

- **Keep:** Buçinca et al. (cognitive forcing); Kim et al. 2024 (uncertainty expressions); Fok & Weld 2024; Vasconcelos et al. 2023; Danry et al. 2023; Zhou et al. 2024; Lee et al. 2025; Spatharioti et al. 2025 (if read).
- **The question applied:** friction is placed uniformly, by the model's confidence, or by the designer. Nobody places it at the user's decision spaces.
- **Link to 3.1:** auto mode treats friction as "prompt fatigue" to be removed, which is the opposite of what this literature recommends.
- **Closest neighbours, to distinguish in §4.1:**
  - Glassman et al. 2024 (AI-resilient interfaces). An important choice can be "hiding in a wall of text." **[abstract only]**
  - WaitGPT (Xie et al. 2024), which structures a code stream. This is the nearest precedent.

## 3.5 Gaze (old 3.4)

- **The question applied:** gaze shows where the eye went. It cannot show whether the user located a decision space or only read the system's cue. This sets up §4.10 ("dissociating attention from navigation").

## 3.6 Synthesis: the missing variable (old 3.5)

**Table 3.1 (new):**

| Account | Who places the decision point | Who writes the options | What the user does | Literacy or algorithmacy |
|---|---|---|---|---|
| Claude Code (3.1) | The system (plan exit, questions); the vendor (prompt types) | The model | Selects; can type "Other" | Literacy |
| Pacing (3.2) | No one | — | Reads at the system's rate | Literacy |
| Automation supervision (3.3) | The designer, in advance | The designer | Responds | Literacy, with supervision |
| Friction (3.4) | Uniform, or by model confidence | The designer or the model | Pauses, then reads | Literacy |
| WaitGPT | The system, by parsing code | — | Inspects units; interrupts | Partly algorithmacy, for code |
| **Marking (§4)** | **The user's decision spaces, by §4.5's rule** | **None: a mark, not a menu** | **Locates** | **Algorithmacy** |

**Gap sentence, in the required form:** "I found no work that places marks in a streamed natural-language response at the reader's decision spaces rather than at points the system chooses." List where you looked: the search log rows 59–70, plus today's documentation review.

**Open problem, to settle before writing this table:** the last row depends on A1, the rule for locating decision spaces. If the rule lets the system find them, marking is also placed by the system, and the table's contrast collapses. §4.5 has to answer this.

---

## Length

Total about 4,500 words. The new 3.1 adds about 1,400. To stay near the old §3 length, trim 3.2–3.5 to one paragraph per tradition plus its "question applied" paragraph.

## New items for OPEN_ISSUES (logged as G11–G15)

- **G11.** "Claude Code started the decision space move" cannot be claimed. Copilot Workspace, deep research and WaitGPT came earlier.
- **G12.** The plan-mode launch date is not established. The first changelog mention is 23 June 2025; the 6 June 2025 date comes from a secondary source.
- **G13.** The "(Recommended)" ordering has no public source. Describe only what the user sees.
- **G14.** The plan-mode prompt is known only through Ronacher (December 2025). Mark it "as of."
- **G15.** The case relies on Claude and Claude Code, which raises a conflict of interest and needs an AI-use disclosure.
