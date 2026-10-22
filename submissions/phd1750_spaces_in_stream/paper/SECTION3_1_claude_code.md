# §3.1 — the Claude Code case (22 October 2026)

[DRAFTED — the whole section is Claude's draft. Every quotation was checked today against the source file in `sec3/claudecode/` or against your Johnson PDF. Each release date is the npm registry date for that version. The notes at the end list what you need to decide.]

---

### 3.1. A Worked Case: How a Commercial Coding Agent Stages Decisions

Claude Code, Anthropic's command-line coding agent, shows the platforms' move in its most developed and most fully documented form. I take it as the case for two reasons.
- **It can be dated.** Anthropic publishes the agent's documentation and a versioned changelog, and the npm registry dates every release. Each decision point described below can therefore be tied to the release that introduced or changed it.
- **It is not the first.** GitHub Next's Copilot Workspace, whose user manual dates from April 2024, made its specification and plan "fully editable and regeneratable," which "allows you to refine and steer" the system (GitHub Next, 2024). WaitGPT turned a stream of generated code into nodes that a user could inspect and interrupt (Xie et al., 2024).

So the case does not ask whether platforms offer decision points; Claude Code offers several. It asks whose intent those points are specified for.

The agent still streams. Its response arrives as text interleaved with tool calls (file reads, shell commands, edits), and the stream stops for the user only when the user stops it. Pressing Escape will "Stop the current response or tool call mid-turn so you can redirect," and "Claude keeps the work done so far" (Anthropic, 2026c). A message typed while the agent works waits its turn: Claude Code "queues the message instead of interrupting the turn" (Anthropic, 2026c). The surface is compressed as well as continuous. Tool calls collapse by default into single lines such as "Called slack 3 times," and the full record sits behind a transcript viewer that the user must open (Anthropic, 2026c). This is the digital scriptio continua of Section 1 in a working product. The record of what the agent did is on the screen, but it marks where tools were called, not where the agent chose among alternatives. Finding those points is left to the reader.

Over 2025, Anthropic added a series of stops to this stream:
- **April 2025 (v0.2.93): a task list.** The documentation describes it as "Claude's to-do checklist: items Claude created to plan multi-step work" (Anthropic, 2026c).
- **June 2025 (v1.0.33): plan mode,** whose first appearance in the changelog is in this release (Anthropic, 2026b). "Plan mode tells Claude to research and propose changes without making them," and edits stay blocked until the user approves the plan (Anthropic, 2026a).
- **September 2025 (v2.0.0): checkpoints.** Every prompt that starts a turn creates one, and a rewind menu restores code or conversation to it (Anthropic, 2026d).
- **October 2025 (v2.0.21): more questions.** The changelog announced that "Claude will now ask you questions more often in plan mode" (Anthropic, 2026b). The questions come through a tool that puts "multiple-choice questions" to the user "when it needs a decision or a clarification" (Anthropic, 2026e).

Each of these is a decision space in the ordinary sense: a point where the stream stops and the user's judgment is invited.

The way the user is expected to take these points shows the intent they were specified for.
- **Plan approval.** When the plan is ready, the agent presents three options: "Yes, and use auto mode," "Yes, manually approve edits," and "No, keep planning" (Anthropic, 2026a). The first approves the plan and also starts a mode that "lets Claude execute without routine permission prompts" (Anthropic, 2026a). One selection removes the stops that would have followed.
- **The plan arrives already narrowed.** In December 2025, Ronacher (2025) read the prompt that plan mode injects and found that it tells the model to "Include only your recommended approach, not all alternatives." The alternatives, the branching that Section 1 places at the centre of a decision space, are gone by the time the approval dialog appears.
- **Questions work the same way.** The model writes the options and the user picks one, although Claude Code does let the user "type your own text through the Other row" (Anthropic, 2026e).

For the user, the default choice is idempotent in the sense that matters here: selecting it leaves the agent's trajectory where the agent had already set it. The decision space is real, but it is specified for the platform's intent, which is to get the plan approved and the task moving.

The releases of 2026 show where that specification leads.
- **Questions closed on their own.** Until v2.1.200, released on 3 July 2026, an unanswered question auto-continued by default (Anthropic, 2026b). The dialog submitted any options already selected and told the agent the user "may be away from your keyboard, so Claude proceeds on its own judgment" (Anthropic, 2026e).
- **Shell prompts gained an exit.** In August 2026 (v2.1.247), the agent began offering "Yes, and switch to auto mode" on its shell-command prompts (Anthropic, 2026a).
- **Auto mode became the default.** In September 2026 (v2.1.283), auto mode became the "built-in starting permission mode" for interactive sessions on every plan (Anthropic, 2026a). In auto mode, "a separate classifier model reviews actions before they run," and the mode "nudges Claude to keep working without stopping for clarifying questions" (Anthropic, 2026a). Anthropic's own table of modes gives three words for what auto mode is for: "reducing prompt fatigue."
- **Agent view moved the user off the stream.** Agent view, added in May 2026 (v2.1.139), lets the user dispatch several sessions at once and "watch their state at a glance instead of scrolling through transcripts, and step in only when one needs you" (Anthropic, 2026f).

The stops have not disappeared:
- plan approval and permission prompts "never auto-resolve on idle" (Anthropic, 2026e);
- the user can open the proposed plan in a text editor and change it before approving (Anthropic, 2026a);
- Anthropic warns that auto mode "does not guarantee safety" (Anthropic, 2026a).

Still, across the releases traced here, the changes made decision points easier to pass through, and none made the points where the agent commits easier to find.

Johnson's (2000) sociology of ancient reading explains why a product would develop this way. Johnson treats reading as "a sociocultural system in which the individual participates" (p. 602), and a writing system acquires the aids that its reading culture needs.
- **The stream is a performance.** The ancient bookroll was "played" by its reader "much in the way that we play a videotape or witness a stage performance." Pause and tone were left to a reader-performer, and "nothing in the ancient bookroll was designed to facilitate retrieval in any other way" (p. 620). Claude Code's stream is played in the same sense. The user watches an agent perform, and the platform supplies cues for the audience's part: approve, choose, continue.
- **The cues are smiley faces.** These cues work like the e-mail smiley face in Johnson's example. E-mail culture adopted it within a few years because it eased a strain that readers felt (p. 608). Yet a reading culture can also go centuries without aids it does not feel it needs. Johnson's Greeks did without word spaces because, for their reading system, "habits like scriptio continua and lack of punctuation worked" (p. 608).
- **Checkpoints replay; they do not retrieve.** The rewind menu "lists the prompts you sent during the session" (Anthropic, 2026d). The user can replay the performance from any prompt but cannot retrieve it by the agent's decisions.
- **The menus are written for specialists.** Johnson also observes that some reading cultures work as closed systems between specialists, as a physician's prescription does for a pharmacist (p. 612). The agent's menus assume such a reader: a developer who already knows which option is the decision. To a novice, the same menu may offer nothing to locate.

The case supports a claim about effect. Anthropic's documentation describes the stops in terms of fatigue and of work that should keep moving, and that description is enough to show that the decision points are specified to keep the task going, not to expose where the agent binds the user's intent. The platforms have answered the problem of the stream with cues for approval rather than with spaces for inspection. The research literatures reviewed next arrive at the same place by other routes, beginning with work on how fast the stream should run (3.2).

---

### References for §3.1 (new entries; Johnson and Xie are already in your list)

Anthropic. (2026a). *Choose a permission mode* [Documentation]. Claude Code Docs. Retrieved October 22, 2026, from https://code.claude.com/docs/en/permission-modes

Anthropic. (2026b). *Changelog* [Software release notes]. Claude Code, GitHub. Retrieved October 22, 2026, from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

Anthropic. (2026c). *Interactive mode* [Documentation]. Claude Code Docs. Retrieved October 22, 2026, from https://code.claude.com/docs/en/interactive-mode

Anthropic. (2026d). *Checkpointing* [Documentation]. Claude Code Docs. Retrieved October 22, 2026, from https://code.claude.com/docs/en/checkpointing

Anthropic. (2026e). *Tools reference* [Documentation]. Claude Code Docs. Retrieved October 22, 2026, from https://code.claude.com/docs/en/tools-reference

Anthropic. (2026f). *Manage multiple agents with agent view* [Documentation]. Claude Code Docs. Retrieved October 22, 2026, from https://code.claude.com/docs/en/agent-view

GitHub Next. (2024). *Copilot Workspace: Overview* [User manual]. GitHub. Retrieved October 22, 2026, from https://github.com/githubnext/copilot-workspace-user-manual/blob/main/overview.md

Johnson, W. A. (2000). Toward a sociology of reading in classical antiquity. *American Journal of Philology, 121*(4), 593–627. https://doi.org/10.1353/ajp.2000.0053

Ronacher, A. (2025, December 17). *What actually is Claude Code's plan mode?* Armin Ronacher's Thoughts and Writings. https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/

Xie, L., Zheng, C., Xia, H., Qu, H., & Chen, Z. (2024). WaitGPT: Monitoring and steering conversational LLM agent in data analysis with on-the-fly code visualization. In *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–14). Association for Computing Machinery. https://doi.org/10.1145/3654777.3676374

---

## Notes (your decision on each)

1. **Retention.** The section claims effect, which the documentation supports in Anthropic's own words: "reducing prompt fatigue," "nudges Claude to keep working." I did not write "retention." No source I have read shows that the stops are designed to bring users back, and your §3 opening still carries [NEEDS: source for retention]. If you find a source, add one sentence after "…binds the user's intent."
2. **Plan-mode date.** "June 2025 (v1.0.33)" is the plan mode's first changelog mention. A secondary blog says it shipped quietly in v1.0.16 (6 June 2025), so either way it was June 2025.
3. **Ronacher** quotes a prompt that may have changed since. The text dates it to December 2025.
4. **Johnson p. 612** is cropped in your PDF, so I paraphrased the prescription example rather than quoting it. Check the page image before submission.
5. **The novice sentence** ("To a novice, the same menu may offer nothing to locate") is a hypothesis. It belongs with A17. Keep it hedged, or cut it.
6. **Conflict of interest (G15).** This section is Claude's description of Claude Code, written for a paper drafted with Claude Code. The paper needs a disclosure statement, and T&F's AI-use policy applies.
7. **Copilot Workspace's date.** The GitHub repository holding the manual was created on 23 April 2024, and `overview.md` was first committed on 28 April 2024 (GitHub API). "Dates from April 2024" rests on those dates, not on a launch announcement.
8. **Length:** about 1,250 words.
