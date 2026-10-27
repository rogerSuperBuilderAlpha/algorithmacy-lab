# Anthropic. (2026, March 25). How we built Claude Code auto mode: a safer way to skip permissions. *Engineering at Anthropic*. https://www.anthropic.com/engineering/claude-code-auto-mode

**Identifier:** URL above · **Read depth:** full_text (saved web page; no pagination, locators are section headings and Table 1; author given as John Hughes) · **Source-tier:** vendor engineering report (not peer reviewed) · **Evidence basis:** direct_read · **Design and sample:** classifier evaluation on three datasets: real internal traffic (n = 10,000 tool calls from Anthropic employees), real overeager actions (n = 52) and synthetic exfiltration tasks (n = 1,000) · **Parties modeled:** user, agent and a classifier acting as approver · **Facets:** G · **Read:** 2026-10-13

## What it argues
"Claude Code users approve 93% of permission prompts" (opening). The post names "approval fatigue, where people stop paying close attention to what they're approving". Auto mode replaces the human approver with a model: a transcript classifier "acting as a substitute for a human approver" (section "How it works") on Sonnet 4.6, plus a server-side prompt-injection probe on tool outputs. The classifier sees only user messages and tool calls, "reasoning-blind by design" (so the agent cannot talk it round; section "Why we strip assistant text"). Its threat model has four causes: overeager behaviour, honest mistakes, prompt injection and a misaligned model, the last one the authors say they do not currently see in practice. Actions go through three tiers; only those with "real downside potential" reach the classifier.

Table 1: on real traffic (n = 10,000) stage 1 has an 8.5% false-positive rate and the full two-stage pipeline 0.4%. On real overeager actions (n = 52) the false-negative rate is 6.6% at stage 1 and 17% for the full pipeline. On synthetic exfiltration (n = 1,000) it is 1.8% and 5.7%. The authors call 17% "the honest number": misses mostly find the danger but misjudge "whether a real consent signal in the session actually covers this action". They say auto mode is "not a drop-in replacement for careful human review on high-stakes infrastructure", and that it beats skipping permissions but is "arguably a regression" for someone who approves each action carefully. After 3 consecutive or 20 total denials the system stops the model and "escalate[s] to the human". Action-level blocking is "orthogonal to chain-of-thought monitoring" and the two "are complementary" (section "Why we strip assistant text").

## Relation to the argument
Premise P12, ruling D4. It is the nearest direct datum on a person overseeing an agent that acts, and the vendor's remedy removes the person from the approval step instead of improving the reading. That fits the paper's principle (move the work to an artefact) and its problem: the artefact is a second model, the "nested" check P10 of the post warns about. The standard of authorisation is the user's stated intent, "everything the agent chooses on its own is unauthorized until the user says otherwise", not the deployer's. The one party that holds authority is the individual user.

## In conversation with
Cites the Claude Opus 4.6 system card (§6.2.1, §6.2.3.3), not in the bib. Companion to `nadella2026models` (P9, P10, P19). The oversight-fatigue studies in the bib (`ancker2017effects`, `alahmadi2022false`, `yu2026habituation`) concern the same effect; the post cites none.

## Caution
Facet check: the bib note said "read in part (opening paragraphs)"; the full page was read here. Vendor report on its own product; the 52 real overeager actions come from employee denials and post-hoc flags, a small sample that depends on what was caught. The 93% is a rate of approvals, not a measure of inattention, and the post gives no behavioural measure of fatigue. The bib's note that "the drafting model is an Anthropic model" is not a statement the page makes.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the saved HTML page (published 25 Mar 2026; byline 'Written by John Hughes'); stripped markup and searched. Checked 17 quotations and every number in Table 1 and the dataset sizes (n=10,000; n=52; n=1,000; 8.5%, 0.4%, 6.6%, 17%, 1.8%, 5.7%), the 93% opening, '3 consecutive denials or 20 total', Sonnet 4.6, the Opus 4.6 system card sections 6.2.1 and 6.2.3.3.

**Findings:** No issues found. Locators are section headings, as the card says (the saved page has no pagination). I did not test the card's claims that the post cites none of the bib's oversight-fatigue studies beyond reading the page text, which names none of them.
