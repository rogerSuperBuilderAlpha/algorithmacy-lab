[DRAFTED — Claude, 2026-10-22. Proposed online appendix. Every quotation is copied verbatim from the local copies in `~/phd1750-litreview/sec3/claudecode/` (CHANGELOG.md, npm.json, permission-modes.md, tools-reference.md, checkpointing.md, interactive-mode.md, ronacher.html), retrieved 22 October 2026. Publication dates are npm registry `time` stamps (UTC).]

## Appendix A. Primary-source record for the Claude Code case (Section 3.1)

| Version | npm publish date (UTC) | Changelog entry, verbatim (Anthropic, 2026b) | Paper's claim | Status |
|---|---|---|---|---|
| 0.2.93 | 30 Apr 2025 | "Claude now has access to a Todo list that helps it stay on track and be more organized" | "An explicit task list designed to help the agent 'stay on track' was introduced in April 2025" | Verified. The entry says *Todo list*, not task list. |
| 1.0.33 | 23 Jun 2025 | "Improvements to plan mode" | "a dedicated 'plan mode' first documented in June 2025 (v1.0.33)" | Partly. This is the first *changelog* mention, but the entry improves an existing mode. Write "by June 2025" (OPEN_ISSUES G12). |
| 1.0.77 | 12 Aug 2025 | "Opus Plan Mode: New setting in `/model` to run Opus only in plan mode, Sonnet otherwise" | "optional configuration… Opus for planning and Sonnet for execution (v1.0.77, August 2025)" | Verified. |
| 2.0.0 | 29 Sep 2025 | "/rewind a conversation to undo code changes" | "/rewind command (v2.0.0, September 2025)" | Verified. |
| 2.0.21 | 16 Oct 2025 | "Added an interactive question tool" / "Claude will now ask you questions more often in plan mode" | "more frequent solicitation of clarifying input during planning (v2.0.21, October 2025)" | Verified. |
| 2.1.200 | 3 Jul 2026 | "Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt into an idle timeout via `/config`" | "Until July 2026, any unanswered question… would automatically time out" | Verified for AskUserQuestion questions only. It does not apply to permission prompts (see tools-reference below). |
| 2.1.247 | 26 Aug 2026 | "Added a tip on Bash permission prompts pointing to auto mode, with a one-keystroke 'Yes, and switch to auto mode' option" | "in August 2026, permission prompts for Bash execution included a 'Yes, and switch to auto mode' option" | Verified. |
| 2.1.283 | 25 Sep 2026 | "Changed interactive sessions on third-party providers or with telemetry off to start in auto mode when no permission mode is configured; `permissions.defaultMode` still overrides it" | "auto mode established as the default starting mode for enterprise and team subscription tiers (v2.1.283; Anthropic, 2026a, 2026b)" | **Wrong.** This version extends the auto default to third-party providers and to sessions with telemetry off. Before it, the default applied on Pro, Max and Team plans (2026a). |
| 2.1.284 | 28 Sep 2026 | "Changed interactive terminal and VS Code sessions to start in auto mode when no permission mode is configured, on every plan and provider; `permissions.defaultMode` still overrides it" | (not cited) | This is the changelog line that makes auto mode the default "on every plan and provider." The documentation (2026a) dates the same state to "v2.1.283 or later." Write "by late September 2026 (v2.1.283–v2.1.284), on every plan and provider." |
| 2.1.275 | 17 Sep 2026 | "Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn and sends all queued messages at once…" | §3.1: typed input is queued, "requiring the user to wait for a system-determined breakpoint" | **Outdated as of v2.1.275.** Queued input can now interrupt the turn. Date the claim ("until September 2026") or add the send-now key. |

**Span.** From 30 Apr 2025 to 25 Sep 2026 is 16 months and 26 days, covering 17 calendar months. "Nearly seventeen months" is accurate. The sentence opens the arc at "basic operational permission prompts", which date from the first release (npm package created 24 Feb 2025). Measured from that point, the span is about 19 months.

**Other dating slips in §3.1 (L103).** "By late 2025" introduces v1.0.77 (August 2025). "In late 2026" introduces v2.1.247 (August 2026). L111 attributes "nudges" to the classifier, but the documentation attributes it to auto mode. L65 calls the first plan-approval option "the default choice", but the documentation does not say that option is preselected.

### Documentation passages (Anthropic, 2026a, *Choose a permission mode*)

- Mode table, `auto` row: "Everything, with background safety checks | Long tasks, reducing prompt fatigue"
- "With Claude Code v2.1.283 or later, auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions on every plan and provider. On earlier versions, it's the built-in starting permission mode only on Pro, Max, and Team plans."
- "The built-in `auto` default requires Claude Code v2.1.228 or later on macOS, Linux, and WSL, and v2.1.233 or later on native Windows. On earlier versions, the built-in default is Manual."
- Plan approval options, in this order: "**Yes, and use auto mode**: approve and start in auto mode." / "**Yes, manually approve edits**: approve and review each edit individually." / "**No, keep planning**: stay in plan mode and tell Claude what to change."
- "Press `Ctrl+G` to open the proposed plan in your default text editor and edit it directly before Claude proceeds."
- "Auto mode also nudges Claude to keep working without stopping for clarifying questions, though Claude still asks when your prompt or a skill explicitly relies on it."
- "A separate classifier model reviews actions before they run…"

### Documentation passages (Anthropic, 2026d, *Tools reference*)

- "Answer by picking an option, or type your own text through the `Other` row or the notes field."
- "Questions stay open until you answer them. If you want a question you leave unanswered to eventually close and let Claude continue without you, set the `askUserQuestionTimeout` setting…"
- "The timeout applies only to `AskUserQuestion`'s multiple-choice questions; permission prompts, including plan approval, never auto-resolve on idle."

These passages reconcile §2.5/§3.1 ("until July 2026 … closed on its own") with §3.1 ("never auto-resolve on idle"). The timeout governed questions, while permission prompts and plan approval never auto-resolved. The current documentation describes the post-v2.1.200 state, in which the timeout is opt-in.

### Documentation passages (Anthropic, 2026e, *Checkpointing*; 2026c, *Interactive mode*)

- "checkpointing automatically captures the state of your code before each prompt you send that starts a turn."
- `Esc`: "Stop the current response or tool call mid-turn so you can redirect. Claude keeps the work done so far."
- "Queue messages while Claude works" (section heading). The paper's claim that typed input is queued rather than interrupting the turn is consistent with this.

### Third-party source (Ronacher, 2025, 17 Dec 2025)

- Quoted plan-mode instruction: "Include only your recommended approach, not all alternatives". This is known only through Ronacher. Cite it as "as of December 2025" (OPEN_ISSUES G14).
