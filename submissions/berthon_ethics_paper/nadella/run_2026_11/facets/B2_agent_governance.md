# B2 Agent governance beyond Microsoft

Agent-drafted. The author has not reviewed it and none of the text is his.

Budget cut in force (PLAN 10 cuts 1-5): cap 4 cards; scope OpenAI, Anthropic, Google and one public body.

## Counts by read status

| source_basis | cards |
|---|---|
| full-text | 2 (anthropic2025safeagents, google2025secure_agents) |
| partial-text | 2 (imda2026agentic, acp2026agentic) |
| abstract | 0 |
| secondary | 0 |

## Entries

| citekey | record verified by | read status | bearing (STRUCTURE section) |
|---|---|---|---|
| anthropic2025safeagents | Anthropic's own page, date read in the saved text | full-text (one page) | 1.3, 4.3, 4.4-stop, 4.4-record: supports |
| google2025secure_agents | the PDF's own cover (title, authors, May 2025), 18 pp | full-text; pp. 7, 12-13 closely | 1.3, 4.3, 4.4-record, 4.4-stop: supports |
| imda2026agentic | IMDA press-release page (publisher) plus PDF cover, v1.5 of 20 May 2026 | partial-text (about 20 of 53 pp. read; whole text searched) | 4.3, 4.4-stop, 4.4-contest: narrows; 4.4-record, 4.4-loss: supports; counter |
| acp2026agentic | repository README names OpenAI and Stripe as maintainers; docs home does not confirm | partial-text (README, checkout RFC, principles, docs home) | 4.4-stop, 4.4-loss, 4.4-record: supports on partial reading |

## Comparison: what the person an agent acts on gets (yes / no / partial)

Items: (a) record of what the agent did to her; (b) a way to stop or refuse it; (c) sight of the limits; (d) standing to contest; (e) cover for loss. Cards listed as "carded" were not re-carded in this facet; their answers are not stated here because their cards were not reopened.

| Framework | Addresses | (a) record | (b) stop/refuse | (c) limits | (d) standing | (e) loss cover |
|---|---|---|---|---|---|---|
| Anthropic framework, card anthropic2025safeagents | user, deployer/administrator | no | no (user's stop only, "Keeping humans in control") | no | no | no |
| Google secure agents, card google2025secure_agents | controlling user, security reviewers | no (p. 13) | no (p. 12) | partial at most (p. 12) | no | no |
| IMDA framework v1.5, card imda2026agentic | deployers; end users incl. those who interact with agents | no (pp. 43-44) | partial (human contact, p. 47) | partial (p. 47) | partial (contact where "dissatisfied with a decision", p. 47) | no (p. 29; p. 28 firm-to-firm contracts) |
| Agentic Commerce Protocol, card acp2026agentic (partial reading) | buyers, agent platforms, merchants, payment providers | partial (order permalink, s. 4.4; webhooks to merchant, s. 2.3) | partial (cancel call, s. 4.5; buyer review, s. 5) | no | no (returns out of scope, s. 1) | no |
| Shavit et al. 2023; Chan et al. 2023, 2024, 2025; Kolt 2025; Agent Payment Protocol (`google2026agentic`); Agent Control Specification (`elmergawi2026introducing`); OpenAI and Anthropic documentation cards | already carded | not restated | not restated | not restated | not restated | not restated |

## What each STRUCTURE section in scope can rest on

- 1.3 and 4.3 (the frame addresses the user and deployer): anthropic2025safeagents (full text), google2025secure_agents (full text). Both name no non-user. Corroboration of Anthropic's claims: google2025secure_agents and imda2026agentic.
- 4.4-record: google2025secure_agents p. 13 (logs for controllers and security); imda2026agentic pp. 43-44 (deployer's audit trails); acp2026agentic (merchant is system of record, partial).
- 4.4-stop: anthropic2025safeagents (user's stop); google2025secure_agents p. 12 (revocation by the controlling user); imda2026agentic p. 43 (deployer halts); acp2026agentic s. 4.5 (cancel by the platform).
- 4.4-contest: imda2026agentic p. 47 only (human contact for the dissatisfied user). All other cards: UNSUPPORTED as a provision; nothing found.
- 4.4-loss: imda2026agentic p. 29 mentions liability only as an approval trigger; no card shows a loss-cover provision.
- Counter-case (`counter`): imda2026agentic pp. 46-47. A public body does ask deployers to declare the agent, state its range of action and give a human contact to people who interact with agents. It is voluntary and its examples are mostly staff and customers of the deployer.
- 6-scale, 6-cost, 7-D02 to 7-D08, 5, 6-*: not touched by these four sources.

## Claims in STRUCTURE.md, ARGUMENT_AND_OUTLINE.md or the ledger that these sources contradict

- None contradicted outright. One narrowing: a claim that no framework gives the person any disclosure or route to a human is contradicted by imda2026agentic p. 47 (voluntary, to "end users" who interact with agents). The lead should check how STRUCTURE 4.4 words "none".

## Gaps and blocks

| Source | Status | Where a library user would find it |
|---|---|---|
| OpenAI Terms of Use; ChatGPT agent help page | scout BLOCKED (403); not retried here; no card | the publisher's site in a browser; the terms are on the open web |
| OWASP Agentic AI threats, AWS scoping matrix, WEF AI Agents in Action | SKIPPED, outside the cut scope and cap (OWASP and AWS saved locally by the scout; WEF 403) | publishers' own sites |
| Gabriel et al. 2024; Kasirzadeh and Gabriel 2025; South et al. 2025; Riedl and Desai 2025; Priyanshu et al. 2026; Feng et al. 2025 | SKIPPED, outside the cut scope and cap (saved locally) | arXiv |
| Ayres and Balkin 2024 | scout BLOCKED (SSRN 403); not retried | SSRN 4862025, or the author's institutional repository |
| "Empowering Consumers with Personal AI Agents" | scout NOT FOUND | no record located |
| IMDA framework | scout said NOT FOUND; found here by the publisher's PDF URL; pp. 5-24, 31-42, 50-53 not read | imda.gov.sg |
| ACP | OpenAPI and JSON Schema, Webhooks RFC, Delegate Payment spec, OpenAI and Stripe documentation pages: not read (two pages saved, unread) | the repository and the vendors' documentation |
| Anthropic page | no paragraph numbers; locators are section headings | |
