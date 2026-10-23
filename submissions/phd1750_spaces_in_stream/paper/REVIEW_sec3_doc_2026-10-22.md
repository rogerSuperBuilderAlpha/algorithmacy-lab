# Review: §4 opening and §3 as it now stands in the Google Doc (22 October 2026)

[CLAUDE REVIEW NOTES. Nothing in the doc was changed. §3 was read from the doc via Drive and saved as `gdoc_sec3_2026-10-22.md`. Each finding is checked against the source files in `sec3/claudecode/`, `sec3/texts/`, your Johnson PDF, and the verified tables in `SECTION3_review.md` and `SECTION3_full.md`.]

## §4 opening paragraph

| # | Phrase | Issue |
|---|---|---|
| 4a | "latent decision spaces where computational commitments occur" | A fourth wording of the definition (A2). The abstract defines decision spaces as points where "human intervention is functionally necessary to control intent." Here they are where the *system* commits. That is the distinction §3.6's table depends on, so choose one and hold it. |
| 4b | "restrict supervisory intervention to system-curated menus on static displays" | Two §3 findings are merged into one. The menus (§3.1) appear in a streaming agent, not on static displays. "Static displays" belongs to the automation account (§3.3). Suggest: "…or confine intervention to points the system or designer places." |
| 4c | Roadmap "(4.9)… (4.10)… (4.11)" | Correct. But §1's roadmap still says "ergonomic moderators (4.9–4.11)" (B1.11), so the two now disagree. |
| 4d | "I formulate algorithmacy theory" | Oberschelp (1995) is the one earlier use of "algorithmacy" that OpenAlex finds. It is unread. A reviewer may find it, so either cite it or add a sentence acknowledging prior uses of the term. |
| 4e | "prevailing paradigms that treat supervisory failure as an editorial deficit to be resolved through heightened vigilance, pacing adjustments, or peripheral friction" | Pacing research (§3.2) does not treat failure as an editorial deficit; it treats delivery as throughput and comfort. Drop "pacing adjustments" from this list, or change the framing. |

Everything else is accurate to the paper's own plan.

---

## §3 in the doc

### §3 opening
- "This resists, and systematically omits, the structural spaces…" is now ungrammatical. "This" has no clear referent after the edit. Suggest: "That culture resists…"
- The retention placeholder is gone, and the sentence now claims only "keeping the user moving." That is supported.

### §3.1 (the doc version differs from my draft; these are accuracy issues only)

**Citations point to the wrong document.** The doc's reference list has only Anthropic 2026a (*Permission modes*) and 2026b (*Changelog*), so several claims now cite a page that does not contain them:

| Claim in doc | Cited as | Actually in |
|---|---|---|
| Esc stops the turn | 2026a | *Interactive mode* |
| Queued messages | (none) | *Interactive mode* |
| Multiple-choice prompt with "Other" | 2026b | *Tools reference* |
| "never auto-resolve on idle" | 2026a | *Tools reference* |
| `/rewind` lists one entry per prompt | 2026b | *Checkpointing* |
| "a terminal-based programming agent" | 2026b | fine, or cite the docs home page |

Fix: add the four entries from my §3.1 file (2026c *Interactive mode*, 2026d *Checkpointing*, 2026e *Tools reference*, 2026f *Agent view*), then recite. The Copilot Workspace sentence needs GitHub Next (2024). Magentic-UI needs Mozannar et al. (2025). Stark & Vanden Broeck (2024) needs an entry too.

**Factual errors**

| # | Doc text | Problem | Source |
|---|---|---|---|
| 1 | "In interactive ('Plan') mode, the user observes an advancing stream…" | Interactive mode is not plan mode. Plan mode is one of six *permission* modes. | *Permission modes*; *Interactive mode* |
| 2 | "By default, this stream does not pause unless the user presses Escape" | Before September 2026, the default mode (Manual) paused for permission on edits and commands. Since then, auto mode pauses rarely. Either way the stream did pause for permission prompts. | *Permission modes* |
| 3 | "requiring the user to wait for a system-determined breakpoint" | Since v2.1.275 the user can "Send queued messages now" (Ctrl+Enter). | *Interactive mode* |
| 4 | "Initially, the system introduced intermediate decision junctures, which it later removed systematically" | Not removed. Plan approval and permission prompts remain, and your own ¶3 says they "never auto-resolve." Say "made easier to pass through." | *Tools reference* |
| 5 | "By late 2025, cognitive labor was partitioned across models, with Opus responsible for plan formulation and Sonnet for code execution (v1.0.77, August 2025)" | This was an optional setting ("Opus Plan Mode: New setting in /model…"), not a default. August is not "late 2025." Cut it; it is not a decision point. | CHANGELOG |
| 6 | "unanswered user queries would automatically time out" | They were the *agent's* questions to the user, not user queries. | CHANGELOG; *Tools reference* |
| 7 | "In late 2026… in August 2026" | August is not late 2026. Say "In 2026." | — |
| 8 | "auto mode became the default starting state for all plans" | "Plans" here means subscription plans. Readers will take it to mean plan mode. Say "for every subscription plan." | *Permission modes* |
| 9 | "Over sixteen months, the interface evolved from an uninterrupted stream to a structured sequence of pauses, and ultimately to an autonomous mode designed to eliminate the interruptions it had previously introduced" | (a) April 2025 to September 2026 is 17 months. (b) It did not start as an uninterrupted stream: permission prompts existed from the start. (c) Auto mode removes *routine permission prompts*, not plan approval. | CHANGELOG; *Permission modes* |
| 10 | "The model collapses the latent decision space, including competing architectural paths, rejected libraries, and unexamined trade-offs, before rendering any text on screen" | The plan prompt governs only the plan file. The agent streams its exploration before the plan appears. "Rejected libraries" etc. is illustration, not evidence. Suggest: "before the plan reaches the user." | Ronacher 2025 |
| 11 | Classical bookrolls "formatted as unpunctuated scripts to be 'played' like musical scores" | Johnson's simile is "much in the way that we play a videotape or witness a stage performance" (p. 620). He does not mention musical scores. | Johnson p. 620 |
| 12 | "analogous to marginal accents or modern tone markers… (Johnson, 2000, p. 608)" | Johnson p. 608 discusses the e-mail smiley face. "Marginal accents" is not there. | Johnson p. 608 |
| 13 | "…just as excerpts of an ancient roll could be sequentially 'replayed.'" / "In contrast, 'nothing in…'" | A broken paragraph join: the sentence ends unfinished and the next paragraph opens mid-thought. "Sequentially" is added; Johnson's "replayed" cites the *Phaedrus*. Merge the two paragraphs. | Johnson p. 620 |
| 14 | "ancient technical texts that functioned as 'closed systems' written strictly specialist-to-specialist (p. 612)" | The legible part of p. 612 gives a *modern* example, a physician's prescription read by a pharmacist, not ancient technical texts. The page is cropped, so check the image before quoting. | Johnson p. 612 |
| 15 | "OpenAI's Deep Research" as an earlier implementation | I have no primary dated source that it came before Claude Code's task list (April 2025) or plan mode (June 2025). Drop "earlier" for it, or find OpenAI's launch post. | — |
| 16 | "WaitGPT… and Magentic-UI… have investigated on-the-fly task partitioning" | WaitGPT visualizes generated code as it streams. Magentic-UI does co-planning and action guards (abstract only). Neither is "task partitioning." | Xie et al. 2024; Mozannar et al. 2025 abstract |
| 17 | "deploying automated classifier 'nudges' to bypass clarifying pauses" | Misattributed. The docs say *auto mode* "nudges Claude to keep working without stopping for clarifying questions." The classifier reviews actions; it does not nudge. | *Permission modes* |
| 18 | "Instead, following Stark and Vanden Broeck's (2024) analysis…, evaluate the issue…" | A sentence fragment (imperative "evaluate"). Write "I evaluate." Also check that "coordinative co-optation" is their term before using it as one. | — |
| 19 | "contemporary front-ends systematically sacrifice…" | "Systematically" goes beyond one documented product. | — |

### §3.2
- Accurate after your revisions.
- **One unverified detail:** "11.97 words per second for complex text and 21.20 for easy prose." My notes record only the two values (99th-percentile comfortable speeds), not which condition each belongs to. Check Xiao & Yang's §3.2 before keeping the "complex/easy" labels.
- **Typo:** "(Haverkamp et al., 2023).023)." has stray characters at the end of the paragraph.

### §3.3
- "operators often follow faulty automated advice even after reviewing all necessary external information." **Still overstated** (G27 #1). In one study they review, about half of the participants who missed a wrong diagnosis had sampled all the information.
- Goddard: "the provision of raw data instead of canned recommendations as primary design mitigators." The abstract says "the provision of information versus recommendation." "Raw data," "canned" and "primary" are not in it.
- "Presenting system output as an explicit recommendation **fundamentally** changes user scrutiny." This contradicts your next sentence ("slightly reduce"). The effect was .94 to .93.
- "they **rarely** select high transparency." It was chosen on 39% and 43% of trials, which is less than half, not rare.
- "(Lamb et al., 2026; Lee & See, 2004)." Lee & See supply only the term. Lamb is the finding.
- "Whether through alert placement (Goddard et al., 2012)." Goddard's factor is the position of *advice*, not alerts.
- Bainbridge has been removed, so the unverified claim is gone. Good.

### §3.4 (new material; checked against my verified notes)
- Kim et al. (2025), Steyvers et al. (2025), Zhou et al. (2024), X. Zhu et al. (2026), Kim et al. (2024), Danry et al. (2023), Disley & Khan (2026) and Forshaw et al. (2026) are accurate.
- **Ghosh et al. (2026)** is cited for "at the expense of user satisfaction." Ghosh found the Assumptions function reduced overreliance *without raising cognitive load*. That is closer to counter-evidence than support. Cite Buçinca alone for the satisfaction cost.
- **"Peripheral obstacles… frequently increase perceived workload without reliably improving critical evaluation (Collins; Arun & Fischer; Cox)."** Only Arun & Fischer measured workload (mental demand rose, and critical evaluation did not). Collins found less click-through with little effect on accuracy and did not measure workload. Cox (2016) is a design proposal with no outcome data. "Frequently" rests on one study.
- **"users often resort to coarse scanning and indiscriminate copying because interfaces rarely support efficient verification (Fok & Weld; Liu et al., 2026)."** Liu et al. found these behaviours *associated with* high overreliance. The causal "because interfaces rarely support…" is not their finding. Fok & Weld say that explanations rarely enable verification.
- **"cognitive forcing is necessary to maintain critical scrutiny."** The studies show it *reduces* overreliance, not that it is necessary.

### §3.5
- **"the strong eye–mind hypothesis"** is uncited. It is Just & Carpenter's (1980) assumption, so cite it or drop the label.
- **"focuses initial fixations almost exclusively on the leading edge (Park & Lee, 2024)."** "Almost exclusively" is stronger than "clustered" (cf. B1.3).
- **Cho & Lim (2026):** "does not predict whether users calibrate their trust or critically evaluate model claims." They measured trust, not calibration or critical evaluation: "gaze measures did not predict trust." Their screens were static and their sources unclickable; that caveat matters here.
- **"as sensorimotor psychophysics has established, visual gaze reflects low-level alerting and stimulus-driven capture as much as active deliberation."** "Has established" and "as much as" have no source.
- **Counter-evidence is missing.** Wu et al. (2025) and Cao & Huang (2022) found that gaze *does* track reliance. Leaving them out makes the section look one-sided to a reviewer. My draft had them in its first paragraph.

### §3.6
- **The table has formatting problems.** Its cells show literal "\*\*" and "\*" characters (Markdown that did not convert), and the header row is a blank row followed by the labels. Bold them in Docs instead.
- **"reveals no work that places marks…"** should take the required form: "I found no work that places marks…" Also confirm that log rows 59–70 actually covered "artificial intelligence safety"; if not, drop it from the list of fields searched.
- **"an invariant spatial mark"** in the table commits to a form of mark that A12 has not decided.
- **The §3.6 heading is Heading 3, while 3.1–3.5 are Heading 4.**

### References
The doc carries only three new references at the end. Everything §3 cites must eventually be in the merged list (E2). The new names introduced in the doc version are GitHub Next (2024), Mozannar et al. (2025), Stark & Vanden Broeck (2024) and Anthropic 2026c–f.
