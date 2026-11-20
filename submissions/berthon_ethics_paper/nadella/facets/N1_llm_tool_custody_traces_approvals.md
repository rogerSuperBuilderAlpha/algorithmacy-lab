# N1 — LLM tool custody: traces, approvals, verification duties, and whom the controls answer to

*Facet N1, research round 1, 2026-10-24. Agent-drafted. The author has not reviewed it, and none of the text is the
author's. Notes for the lead, not prose for the paper.*

**What this facet covers.** How current LLM tools and agent platforms present traces, approvals and verification
duties to users and to enterprise admins, and whom their controls answer to. Microsoft first (Agent 365, Entra Agent
ID, Copilot Studio approvals, Purview audit for Copilot, Foundry agent approvals and tracing, Copilot Cowork, the
Enterprise AI Services Code of Conduct, the consumer Copilot terms, the 2026 Responsible AI Transparency Report and its
Agent Control Specification); then OpenAI, Anthropic and Google terms and product documentation; chain-of-thought
visibility in deployed products; approval mechanics and approval-rate evidence; studies of reading agent traces.

**The question the synthesis answers.** Do the tools put the reading, the record and the brake where A4 says they
sit; is the operating envelope of controls outside the model (P11–P12) declared to the deployer alone (A5); and does
anything in the setting remove the burden on people without capacity (A8)?

**Premises and outline sections served.** A4, A5, A8; moves M1, M3, M4, M5, M7, M8, M10; outline "The present case"
and its worked case (P15 → P19 → P20).

**Extends, does not repeat.** Facet G (C2–C7) already holds the security lineage, the CoT-monitorability literature,
the alert-review studies, Chen, Yu, Grunde-McLaughlin, Mitchell, Turan, Green, Crootof, Sterz, Langer, Laux,
Bainbridge, Parasuraman and Manzey, and `anthropic2026how` (93% of prompts approved). Facet V1 holds the Responsible AI
Standard v2 (T1, T3, A5), the 2024 and 2025 Transparency Reports, the Copilot application card ("always review and
verify"), the AI Literacy Starting Guide, Elevate and the AI Act articles. I did not reopen those, except Kutasov's
human baseline (row 37) to decide on an upgrade.

---

## Legend for read status

*Read in full* = I read the whole document this session. *Read in part* = I read the sections or pages named.
*Abstract only* = an abstract from OpenAlex or Crossref. *Not accessible* = no text reached; the block is logged.

**Counts (43 sources opened or attempted):** read in full 13; read in part 23; abstract only 2; not accessible 5.
**Cards written:** 29 new, 0 upgrades (Kutasov's existing dxd card already covers the human baseline and appendix L;
see entry 37).

---

## (a) Search log

All searches ran on 2026-10-24. Downloads are under `~/iit-playground/berthon_ethics_local/pdfs/nadella/N1/<dir>/`
with `SOURCE_URL.txt` (URL and access date) in each directory.

| # | Source | Exact query or URL | Hits | Notes |
|---|---|---|---|---|
| 1 | WebSearch | `Microsoft Agent 365 overview learn.microsoft.com registry observability admin` | 10 | Located the Learn overview. |
| 2 | WebSearch | `Copilot Studio human in the loop agent flows request for information approvals learn.microsoft.com` | 9 | Located multistage approvals page and roadmap RM570434 (via mc.merill.net archive). |
| 3 | WebSearch | `Purview audit logs Copilot and AI applications CopilotInteraction learn.microsoft.com` | 9 | Located `purview/audit-copilot`. |
| 4 | WebSearch | `Azure AI Foundry agent service MCP tool require_approval human approval documentation` | 10 | Located Foundry MCP page. |
| 5 | curl | learn.microsoft.com: agent-365 overview; copilot-studio flows-advanced-approvals; purview audit-copilot; foundry MCP; entra agent-id; mc.merill.net RM570434 | 6 of 6 (HTTP 200) | Read. |
| 6 | WebSearch | `Microsoft 2026 Responsible AI Transparency Report PDF` | 9 | Located the 2026 PDF on Microsoft's CDN. |
| 7 | WebSearch | `Microsoft Enterprise AI Services Code of Conduct "human oversight" learn.microsoft.com legal` | 9 | Located the Code of Conduct. News items on a Sept 2026 draft MAI model code not followed (news only). |
| 8 | WebSearch | `Microsoft Foundry agents tracing observability view traces thread run steps learn.microsoft.com` | 9 | Located trace-data page; AZ563426 (trace replay). |
| 9 | curl | RAI Transparency Report 2026 PDF; ai-code-of-conduct; foundry trace-data; microsoft.com/servicesagreement; mc.merill.net AZ563426 | 5 of 5 (200) | AZ563426 archive page held only a title stub: **not accessible** in substance. |
| 10 | WebSearch | `"Agent Control Specification" Microsoft ACS open specification runtime governance agents GitHub` | 9 | Located the Command Line announcement. Another vendor's "Agent Control Standard" not pursued. |
| 11 | curl | commandline.microsoft.com ACS post; microsoft.com Copilot consumer terms | 2 of 2 | Read. |
| 12 | WebSearch | `Copilot Cowork application card learn.microsoft.com transparency approval actions` | 9 | No Cowork application card found (the 2026 report cites one, fn. 37). Located "Use Copilot Cowork". |
| 13 | curl | learn.microsoft.com `copilot/microsoft-365/cowork/use-cowork` | 1 | Read. |
| 14 | curl | openai.com/policies/terms-of-use/; openai.com/index/learning-to-reason-with-llms/ | **403 both** | Cloudflare challenge page. Not circumvented. |
| 15 | curl | platform.openai.com/docs/guides/reasoning (redirects to developers.openai.com/api/docs/guides/reasoning) | 200 | Read in part. |
| 16 | curl | cdn.openai.com `papers/practices-for-governing-agentic-ai-systems.pdf` | 200 | Read in full. |
| 17 | curl | platform.claude.com extended-thinking and thinking pages; code.claude.com permissions; anthropic.com legal consumer-terms, aup, commercial-terms | 6 of 6 (200) | Read in part. |
| 18 | curl | ai.google.dev gemini-api/terms and docs/thinking; policies.google.com generative-ai use-policy; ap2-protocol.org/specification/ | 3 of 4 | AP2 site returned **404**; spec taken from GitHub (row 19). |
| 19 | GitHub API + curl | `repos/google-agentic-commerce/AP2/contents/docs/ap2`; raw `specification.md`; commits for its path | 200 | v0.2 released 28 Apr 2026 (commit b4587ac1d0). |
| 20 | curl | cloud.google.com AP2 announcement blog | 200 | Read in full. |
| 21 | Consensus | three queries (agent-trajectory review accuracy; reading CoT and trust; permission-prompt habituation) | **0** | "You've used all 500 included searches this month". No retry. |
| 22 | Scholar Gateway | `How accurately do human reviewers detect errors or harmful actions when inspecting logs or traces of large language model agents?` | **ACCESS_DENIED** | Tried once, as the brief directs. |
| 23 | arXiv API | `abs:"agent" AND abs:"trajectories" AND abs:"human" AND abs:"user study"`; `abs:"reasoning traces" AND abs:"user study"`; `abs:"chain-of-thought" AND abs:"users" AND abs:"reliance"` | 12, 6, 5 | Picked 2606.18671, 2607.26300, 2605.10930, 2511.12001; abstracts of 2606.22110, 2604.18847, 2511.11187 read and set aside (row 24). |
| 24 | arXiv API | `id_list=` 2606.22110, 2607.26300, 2606.18671, 2604.18847, 2605.10930, 2511.11187, 2511.12001 | 7 of 7 | TraceView (5-researcher survey), harm recovery and ReTrace not carded: no test of verifying agent actions against outcomes. |
| 25 | curl | arxiv.org/pdf 2605.10930v2, 2511.12001v3, 2606.18671v1, 2607.26300v2, 2506.15740 | 5 of 5 | A first loop failed on shell word-splitting (404s from malformed URLs); rerun correctly. |
| 26 | WebSearch | `cdn.openai.com ChatGPT agent system card pdf confirmations watch mode user takeover` | 9 | Surfaced Feng et al. 2512.00742 and Tang et al. 2509.10723; system card PDF not surfaced. |
| 27 | WebSearch | `Anthropic "Measuring AI agent autonomy in practice" auto-approve interrupt rate Claude Code` | 10 | Located the Anthropic post. |
| 28 | WebSearch | `developers.openai.com codex approvals sandbox modes "on-request" documentation` | 9 | Located Codex "Agent approvals & security". |
| 29 | curl | anthropic.com research/measuring-agent-autonomy; developers.openai.com codex/agent-approvals-security; help.openai.com ChatGPT agent article; arxiv 2512.00742; arxiv 2509.10723 | 4 of 5 | help.openai.com **403**. Not circumvented. |
| 30 | Crossref | `/works/` 10.1080/17470214808416738; 10.1518/001872008X312152; 10.1145/3723158; 10.1145/2335356.2335360 | 4 of 4 | Mackworth QJEP 1(1):6–21 (1948); Warm et al. Human Factors 50(3):433–441 (2008); Tariq et al. ACM CSUR 57(9) (2025); Felt et al. SOUPS '12, pp. 1–14. |
| 31 | OpenAlex | `/works/doi:` same four DOIs | 4 of 4 | Mackworth: closed, no abstract. Warm: closed, abstract. Tariq: hybrid OA at ACM. Felt: abstract; author copy found at CMU CUPS. |
| 32 | curl | dl.acm.org/doi/pdf/10.1145/3723158 | **403** | ACM bot wall. Not circumvented; abstract only. |
| 33 | curl | cups.cs.cmu.edu/soups/2012/proceedings/a3_Felt.pdf | 200 | Read in part. |
| 34 | WebSearch | `Microsoft Responsible AI Standard "T1.3" OR "A5.4" evaluation results stakeholders interpret system responses oversight "realistic conditions"` | 9 | No Microsoft evaluation against T1.3 or A5.4 found; the summary points to Copilot Health clinician ratings (2026 report). |
| 35 | Local | keyword search of all 35 PDF pages of the 2026 report: T1.3, A5.4, interpret, realistic, oversight, end user, affected, recipient | — | No T1.3 or A5.4; hits recorded in `microsoft2026responsible`. |

---

## (b) Entries

Card paths are relative to the arm: `literature/cards/berthon_ethics_paper/<key>.md`. "Exists" gives how I checked the
source is what it claims to be.

### B1. Microsoft: admin control planes, approvals, audit and traces

**1. Overview of Microsoft Agent 365** (Microsoft Learn, ms.date 2026-08-19). `microsoft2026overview`; card written.
Exists: Learn page, fetched. *Read in full.* Agent 365 is the control plane through which "admins" and "leaders and AI
admins" observe a registry of agents and govern their permissions and reviews; visibility extends to "security and
business leaders" (section "Observe"); agents stay "aligned with organizational policies and business needs" (section
"Govern"). GA 1 May 2026. *Bearing:* supports A5 and M1; the page names no one outside the organisation.

**2. What is Microsoft Entra Agent ID?** (Microsoft Learn, ms.date 2026-04-14). No card (it repeats entry 1's seat).
*Read in full.* Each agent gets an identity with "adaptive access policies, real-time risk detection, lifecycle
management", and "All agent authentication and activity is logged for compliance and audit." *Bearing:* supports A5;
the identity is for the organisation's governance, not shown to counterparties.

**3. Roadmap RM570434, Copilot Studio human approval for tool calls** (published 1 Sep 2026, archived at
mc.merill.net). `microsoft2026enabling`; card written. Exists: archive reproduces Microsoft 365 Roadmap ID 570434.
*Read in full.* A per-tool toggle pauses a gated call so "a person can approve, approve for the session, or deny";
requests appear "inline in the channel where the agent is deployed". *Bearing:* narrows A5 (the agent's user gets a
confirmation step); the guardrail is "for organizations" and set by the maker.

**4. Multistage and AI approvals in agent flows (preview)** (Microsoft Learn, ms.date 2025-09-04).
`microsoft2025multistage`; card written. *Read in full.* An AI stage "produces a clear Approve or Reject decision";
in the worked example an amount under $5,000 approved by the AI stage can "bypass manager approval and automatically
end as approved"; human stages for sensitive cases are advised ("ensure that human approval stages are reached"), not
required. *Bearing:* supports M8 with a turn the post omits (the gate can be a model); supports A8.

**5. Audit logs for Copilot and AI applications** (Microsoft Learn, ms.date 2026-08-26). `microsoft2026audit`; card
written. *Read in full.* Records name the user, time, host, agent, and each resource accessed with an Action value
("read, create, modify"), a blocking policy and an XPIA flag; prompt and response appear as message IDs; access is
through the Purview portal's Audit search. *Bearing:* supports M4(a) (the tenant's record, read by its admins);
narrows M4(b) (actions are typed per resource).

**6. Connect agents to MCP server endpoints** (Microsoft Learn, ms.date 2026-09-29). `microsoft2026connect`; card
written. *Read in part* (named sections). "Microsoft has no responsibility to you or others in relation to your use of
any remote MCP servers"; the approval sample's comment says "In production, implement your own approval UX and
policy." *Bearing:* supports A5 (the approval surface and policy are the deployer's) and M10.

**7. 2026 Responsible AI Transparency Report** (Microsoft, PDF dated 28 Aug 2026). `microsoft2026responsible`; card
written. Exists: Microsoft CDN PDF, 35 pp. *Read in part* (PDF pp. 7, 10–15, 18–21, 27, plus a keyword search of all
pages). Human oversight is listed as the ability to "Configure authorization and policy settings, such as approval
gates; - Activate, block, or delete agent instances; and - Review evaluation results and logs through user interfaces"
(PDF p. 14, printed p. 26). Cowork requires user approval for actions that send or modify content, and its outputs
"include attribution indicating AI assistance, ensuring recipients know when they are interacting with AIproduced
content" (PDF p. 18). Researchers found Copilot could access files "without those access points being recorded in
Unified Audit Logs"; Microsoft fixed it (PDF p. 19, printed p. 37). The report describes a "re-engineered" Standard
with a Deployer Chapter; it reports no evaluation against v2's T1.3 or A5.4. *Bearing:* supports A5 and M7 (absence);
the audit gap complicates P15's "tamper-proof" record; recipient attribution is the one provision for people outside.

**8. Introducing Agent Control Specification** (Elmergawi et al., Command Line, 2 Jun 2026).
`elmergawi2026introducing`; card written. *Read in full.* "the question is no longer just what they can do, but what
they should be allowed to do and who defines those boundaries"; "There is no standard mechanism by which a security or
compliance team can define, enforce, and audit policy across agents"; ACS gives "a security team ... one place to
author, version, and audit controls". Eight interception points include `pre_tool_call`. *Bearing:* the strongest
primary support for A5: Microsoft names the boundary-setter as the organisation's security team. Also supports the M6
concession (enforcement moved out of the prompt into the artefact) and narrows M4(b) (tool-call boundaries are marked).

**9. Microsoft Enterprise AI Services Code of Conduct** (Microsoft Learn, ms.date 2026-05-01).
`microsoft2026microsoft`; card written. *Read in full.* Customers must "Disclose when the output, decisions, or actions
are generated by AI" and keep applications "subject to appropriate human oversight so customers can find and mitigate
undesirable behaviors"; barred: consequential decisions or actions "without appropriate human oversight". *Bearing:*
supports A5 (the envelope binds customers to Microsoft) and M9 (the people acted on get disclosure and a feedback
channel).

**10. Microsoft Services Agreement** (published 30 Jul 2026, effective 30 Sep 2026). No card. *Read in part* (section
12 Warranties; "AI Services" clauses). "YOU BEAR THE ENTIRE RISK OF USING THE SERVICES" (s. 12); AI services must not
"make decisions or take actions without appropriate human oversight that may have a consequential impact" (AI
Services, ix.1). *Bearing:* supports M10; context for entry 11.

**11. Copilot - Terms of Use** (consumer; effective 18 Aug 2026). `microsoft2026copilot`; card written. *Read in
full.* "When you request that Copilot take Actions on your behalf, you are solely responsible for those Actions and any
results or consequences"; "Always verify the accuracy of information presented by Copilot before you rely on it"; for
purchases, "You are responsible for reading and complying with the Merchant’s terms". *Bearing:* supports M10 and H19
more strongly than E14; not applicable to work accounts.

**12. Use Copilot Cowork** (Microsoft Learn, ms.date 2026-09-14). `microsoft2026use`; card written. *Read in part.*
While working the user sees a "Thinking indicator: An animation" and status updates; "Some background operations, like
script execution, run without displaying individual steps." Approval options include session-wide "don't ask again"
and "Approve All"; "Always review the details before you approve." *Bearing:* supports M3 (no reasoning shown), M8 and
A8 (the product supplies ways to stop reviewing while assigning review to the user); narrows A5 for the user.

**13. Tracing and data handling** (Microsoft Foundry, ms.date 2026-06-02). `microsoft2026tracing`; card written.
*Read in full.* Traces record prompts, model inputs and outputs, tool calls and intermediate steps; "Tracing is off by
default"; data is viewable by holders of roles such as Log Analytics Reader; the customer's duty to end users is
"Informing end users about data collection". *Bearing:* supports M4(a) and A5.

**14. AZ563426, Foundry trace replay** (mc.merill.net). *Not accessible* in substance (title stub). Search summary
(row 8) described trace replay; not used.

### B2. OpenAI

**15. OpenAI Terms of Use**; **16. "Learning to reason with LLMs"**; **17. ChatGPT agent help article.** *Not
accessible* (HTTP 403, Cloudflare). Not circumvented. Logged in (e).

**18. Reasoning models** (OpenAI API docs). `openai2026reasoning`; card written. *Read in part.* "While we don’t
expose the raw reasoning tokens emitted by the model, you can view a summary"; reasoning items "remain opaque, and the
API does not return their reasoning text"; summaries on the latest models may require "organization verification".
*Bearing:* supports M3: the deployer, not just the user, gets at most a provider-written summary.

**19. Shavit et al. (2023), Practices for Governing Agentic AI Systems** (OpenAI white paper). `shavit2023practices`;
card written. Exists: OpenAI CDN PDF, 23 pp.; key reused from another arm's bib. *Read in full* (pp. 1–19). Three
parties: developer, deployer, user (p. 5). Approval is hard "when the user must approve many decisions" (p. 9); open
question "How can the effectiveness and meaningfulness of human oversight be evaluated?" (p. 10); chains of thought
"may balloon beyond a user’s ability to feasibly keep up" (p. 12); a user "can always activate a graceful shutdown"
(p. 14); third parties may "demand" agent identification (p. 14). *Bearing:* complicates M8 (brake and ledger go to the
agent's user, not a deployer's "authorized person"); supports A5 (third parties get identification at most).

**20. Agent approvals & security** (Codex docs). `openai2026agent`; card written. *Read in part.* Approvals route "to
you" by default; Auto-review sends them to a reviewer agent "instead of surfacing to the user"; the default reviewer
policy is public in the open-source repository, and "Enterprises can replace its tenant-specific section"; monitoring
pauses "can arrive after the activity that triggered it". *Bearing:* supports M8 (the human gate handed to a model);
narrows A5 slightly (a published default envelope).

### B3. Anthropic (all Anthropic-authored; corroboration named in each card)

**21. Building with extended thinking** (Claude Platform Docs). No card (pointer page). *Read in part.* Points to the
thinking overview; example prints a "Thinking summary".

**22. Thinking** (Claude Platform Docs). `anthropic2026thinking`; card written. *Read in part.* "what you see is never
the raw chain of thought"; "No display setting returns the raw chain of thought"; on current models display defaults
to "omitted"; "Summarization is processed by a different model". *Bearing:* supports M3; corroborated by entry 18 and
Palod et al. p. 2.

**23. Configure permissions** (Claude Code Docs). `anthropic2026configure`; card written. *Read in part.* "in auto
mode a classifier reviews actions instead of you"; "no other level ... can override a managed permission rule".
*Bearing:* supports A5 and M8; corroborated by entry 20.

**24. Consumer Terms of Service** (effective 8 Oct 2025). `anthropic2025consumer`; card written. *Read in part.* "You
are responsible for all Inputs you submit to our Services and all Actions"; "You should not rely on any Outputs or
Actions without independently confirming their accuracy". *Bearing:* supports M10; corroborated by entries 11 and 28.

**25. Commercial Terms of Service** (effective 17 Jun 2025). `anthropic2025commercial`; card written. *Read in part.*
D.3: the customer decides "where human review is appropriate" and "must notify its Users" that outputs "should not be
relied upon without independently checking their accuracy". *Bearing:* supports M10 (the duty handed down the chain);
corroborated by entry 9.

**26. Usage Policy** (effective 12 Nov 2026, posted in advance). `anthropic2026usage`; card written. *Read in part.*
High-risk recommendations need a "qualified person" who "remains responsible", and the subject "must be clearly told
that AI was used"; physical operating limits "must be enforced by the equipment or a controller independent of model
output". *Bearing:* narrows A5 (names the affected individual, but for notice); supports A8 (responsibility placed on
the reviewer, capacity untested).

**27. Measuring AI agent autonomy in practice** (18 Feb 2026). `anthropic2026measuring`; card written. *Read in full.*
Full auto-approve rises from "roughly 20%" of sessions for new users to "over 40%" by 750 sessions; interrupts from 5%
to about 9% of turns; human involvement 87% of tool calls on minimal-complexity tasks, 67% on high-complexity;
classifications by Claude, "we cannot manually inspect the underlying data"; recommends against mandating per-action
approval. *Bearing:* supports M8 and A8; corroborated outside Anthropic by `yu2026habituation` (dxd card) and entry 40.

### B4. Google

**28. Gemini API Additional Terms** (effective 23 Mar 2026). `google2026gemini`; card written. *Read in part.* For
agentic services "you are solely responsible for the actions and tasks performed by the service ... and exercising
judgment and supervision"; "You will not automatically bypass any requests for human confirmation." *Bearing:*
supports M10.

**29. Gemini thinking docs** (ai.google.dev). No card. *Read in part.* "By default, only the final output is
returned. You can enable thought summaries". *Bearing:* corroborates M3 at a third supplier.

**30. Generative AI Prohibited Use Policy** (last modified 17 Dec 2024). No card. *Read in part* (opening list). Bars
automated decisions with "a material detrimental impact on individual rights without human supervision in high-risk
domains". *Bearing:* the same oversight-without-definition pattern as entry 9.

**31. Parikh and Surapaneni (2025), Powering AI commerce with the new Agent Payments Protocol (AP2)** (Google Cloud
Blog, 16 Sep 2025). `parikh2025powering`; card written. *Read in full.* Mandates are "tamper-proof,
cryptographically-signed digital contracts that serve as verifiable proof of a user's instructions"; a delegated
Intent Mandate "specifies the rules of engagement—price limits, timing, and other conditions"; intent → cart → payment
"creates a non-repudiable audit trail". *Bearing:* **refutes A5 as a general claim** about LLM tools (see C2).

**32. Agentic Payment Protocol (v0.2), specification** (GitHub, 28 Apr 2026). `google2026agentic`; card written.
*Read in part* (the specification file in full; linked files not). "The User sees and approves a set of constraints";
verifiers check closed mandates against them; in dispute the mandates "provide a non-repudiable picture of the
transaction", obtainable from the Shopping Agent or the Merchant. *Bearing:* the refutation in normative form, with
the narrowing that dispute use is "outside the scope".

### B5. Studies of reading traces, reasoning and approvals

**33. Palod, Biswas and Kambhampati (2026)**, arXiv:2605.10930v2. `palod2026evaluating`; card written. *Read in part*
(main text pp. 1–9 in full). Lay users (25 per condition) shown raw reasoning traces or summaries accepted wrong
answers at baseline rates (misjudgment 54.0% and 51.0% against 54.2%); a pro-and-con explanation lowered it to 46.9%
(Table 3, p. 6). The abstract overstates: the raw trace raised acceptance of correct answers, not wrong ones. *Bearing:*
supports M3 narrowly; A8.

**34. Park et al. (2025)**, arXiv:2511.12001v3. `park2025critical`; card written. *Read in part* (pp. 1–2, 5). 800
participants; "users often equate trust with outcome agreement regardless of flaws in the model’s reasoning" (p. 1);
omissions caught about 40% of the time (p. 2). *Bearing:* supports M3 and M4 (omissions are what a reader of a record
misses).

**35. Zhang and Nam (2026), HANSEL**, arXiv:2606.18671v1. `zhang2026hansel`; card written. *Read in part* (pp. 1, 9).
Marking evidence in web-agent trajectories cut time and effort; accuracy did not differ significantly (p = .29); with
the full-trajectory baseline participants caught wrong agent answers 60.7% of the time, often by redoing the task (66%
of tasks); HANSEL users still accepted 32.1% of wrong answers. *Bearing:* refutation sought on M4(b) and on
reconstruction from complete logs: narrows M4(b) (marking helps effort), supports M4 (a complete log alone did not let
people check outcomes well).

**36. Zhao et al. (2026), AgentGUI**, arXiv:2607.26300v2. `zhao2026agentgui`; card written. *Read in part* (pp. 1, 4,
6). N = 8; lookup questions about traces answered 38% faster and at 93% against 80% accuracy, with guidance on where
to look. *Bearing:* refutation sought on M4: people can find stated facts in traces; it does not test judging whether
an action was right.

**37. Kutasov et al. (2025), SHADE-Arena**, arXiv:2506.15740v2. Existing card `dxd_foundation/kutasov2025shade.md`;
no upgrade. *Read in part* (I reopened pp. 1, 7–8, 40–42 to decide). The existing partial card already reads the body
and appendix L: annotators averaged "103 minutes per transcript" (p. 7), range 20 to 356 minutes (p. 40), pooled AUC
0.65, "worse than several frontier models" (p. 42). Reading the skimmed appendices would not change the premise use, so
"full" status was not worth the time. Anthropic-authored (first author's affiliation). *Bearing:* unchanged from
facet G.

**38. Feng et al. (2025), On the Regulatory Potential of User Interfaces for AI Agent Governance**, arXiv:2512.00742v1.
`feng2025regulatory`; card written. *Read in full* (pp. 1–4, appendix figures). Six UI patterns across 22 agentic
systems, all addressed to the agent's user; "requiring user simply “watching” does not guarantee meaningful attention
or control" (p. 3); user-specified rules override agent "self-approval" (p. 3). *Bearing:* supports A4 as a survey;
narrows A5 for the principal (user-declared rules), not for third parties.

**39. Tang et al. (2025), Dark Patterns Meet GUI Agents**, arXiv:2509.10723v1. No card. *Read in part* (pp. 1–2,
11–14, 17). 22 participants supervising OpenAI Operator: oversight improved avoidance in 14 of 16 tasks but brought
"attentional tunneling", and in watch mode "participants became reactive rather than proactive" (p. 17); 70% noticed
an overt cart change (p. 12). *Bearing:* supports A8 (watching an agent narrows attention); it also shows supervision
helps somewhat. Not carded to keep within the card budget; the lead may card it.

**40. Felt et al. (2012), Android permissions**, SOUPS '12, doi:10.1145/2335356.2335360 (Crossref confirmed).
`felt2012android`; card written. *Read in part* (pp. 1–2, 5). "17% of participants paid attention to permissions
during installation, and only 3% ... could correctly answer all three permission comprehension questions" (p. 1); a
former reader: "I used to look...I just stopped doing that" (p. 5). *Bearing:* supports M8 and H24 from outside the AI
vendors.

**41. Mackworth (1948), The Breakdown of Vigilance during Prolonged Visual Search**, QJEP 1(1):6–21,
doi:10.1080/17470214808416738 (Crossref). *Not accessible* (closed; OpenAlex has no abstract). No card.

**42. Warm, Parasuraman and Matthews (2008), Vigilance Requires Hard Mental Work and Is Stressful**, Human Factors
50(3):433–441, doi:10.1518/001872008X312152 (Crossref). *Abstract only* (OpenAlex). Facet G already quotes it. No card.

**43. Tariq, Baruwal Chhetri, Nepal and Paris (2025), Alert Fatigue in Security Operations Centres**, ACM Computing
Surveys 57(9):1–38, doi:10.1145/3723158 (Crossref). *Abstract only*: OpenAlex lists it as hybrid open access, but the
ACM PDF returned 403. The abstract names "four major causes of alert fatigue in SOC" without listing them. No card.

---

## (c) Synthesis

### C1. Whom Microsoft's agent controls answer to (A5, M1, M6)

Microsoft's agent stack answers to the deploying organisation at every layer I read. Agent 365 shows the registry to
admins and leaders (`microsoft2026overview`); Entra Agent ID logs agent activity "for compliance and audit"; Purview
holds the per-action record for tenant admins (`microsoft2026audit`); Foundry traces exist only if the owner enables
them and are read through the customer's monitoring roles (`microsoft2026tracing`); MCP approvals use whatever
interface the developer builds (`microsoft2026connect`). The Agent Control Specification, the closest engineering form
of P11–P12, states the question in Microsoft's own words ("who defines those boundaries") and answers it: "a security
or compliance team" authors and audits the controls (`elmergawi2026introducing`). The Code of Conduct requires human
oversight "so customers can find and mitigate undesirable behaviors" (`microsoft2026microsoft`).

The envelope's beneficiaries outside the organisation receive notice. Cowork's outgoing content carries "attribution
indicating AI assistance" (`microsoft2026responsible`, PDF p. 18); the Code of Conduct requires disclosure that
"decisions, or actions are generated by AI". Neither declares what the agent may do to the recipient.

For A5 as written ("declares its envelope to the deployer alone"), Microsoft's documents carry the premise.

### C2. Where the envelope is declared to others (A5 refutation sought, M4(b))

The refutation the brief asked for exists, outside Microsoft. Google's AP2 builds a declared, binding envelope into
agent payments: the user signs an Intent Mandate whose constraints ("price limits, timing, and other conditions") the
merchant and payment providers verify, and the chain of mandates forms "a non-repudiable audit trail" that either side
can produce (`parikh2025powering`, `google2026agentic`). Three weaker cases point the same way, each for the agent's
principal rather than the counterparty. Feng et al. find user-declared rules that override agent self-approval in
deployed tools (`feng2025regulatory`). Copilot Studio and Cowork give the agent's user a confirmation step before a
send or payment (`microsoft2026enabling`, `microsoft2026use`). OpenAI publishes its default Auto-review policy
(`openai2026agent`).

AP2 narrows the analogy's claim in a specific way. A declared envelope appears where the counterparty has commercial
standing and a liability regime already exists (card networks, merchants, disputes); the protocol serves "Authenticity"
and "Accountability" for those parties. Where the person acted on is an email recipient, a job applicant or a customer
in a service queue, I found no declared envelope in any vendor's documents.

### C3. Who must verify (A4, M10)

Every supplier's terms put verification on the user or the deployer. Microsoft's consumer terms: "you are solely
responsible for those Actions and any results or consequences" (`microsoft2026copilot`). Anthropic: "You should not
rely on any Outputs or Actions without independently confirming their accuracy" (`anthropic2025consumer`), and
business customers "must notify its Users" of the same (`anthropic2025commercial`). Google: developers are "solely
responsible for the actions and tasks performed by the service" (`google2026gemini`). This is stronger than E14's
"always review and verify": it covers agent actions, not only outputs, and Copilot's shopping clause makes the user
"responsible for reading and complying with the Merchant’s terms", the H19 duty to read in present form. The OpenAI
terms could not be read (403).

### C4. Who can read the reasoning (M3, P9)

No supplier read gives anyone outside it the raw chain of thought. OpenAI returns summaries on opt-in, after possible
"organization verification" (`openai2026reasoning`); Anthropic says "No display setting returns the raw chain of
thought" and defaults to omitting even the summary (`anthropic2026thinking`); Gemini returns "thought summaries" on
request; Cowork shows its user an animation (`microsoft2026use`). P9's "non-negotiable" CoT transparency is therefore
not available to the enterprise that Nadella writes for when it deploys these suppliers' models; it would hold only for
open-weight models. Studies of lay readers find that traces and summaries do not improve rejection of wrong answers
(`palod2026evaluating`, misjudgment 54.0% and 51.0% against 54.2%) and that readers miss omissions most
(`park2025critical`).

### C5. Approvals and the brake (M8, A8)

The approval gate is being thinned by design and by use. Copilot Studio lets an AI stage approve and end a flow
(`microsoft2025multistage`). Codex Auto-review and Claude Code auto mode route approvals to a model "instead of
surfacing to the user" and a classifier "instead of you" (`openai2026agent`, `anthropic2026configure`). Cowork offers
"Approve All" and session-wide skips while telling the user "Always review the details" (`microsoft2026use`).
Anthropic's data show full auto-approve doubling with experience and human involvement falling as tasks grow
(`anthropic2026measuring`), and the firm argues against mandating per-action approval. Outside AI, Felt et al. found one
user in six attending to permission screens (`felt2012android`). Shavit et al. complicate the deployer-held brake: in
OpenAI's scheme the user holds the shutdown and the ledger (`shavit2023practices`, p. 14). That user is the agent's
principal; the people acted on are not given a brake anywhere I read.

### C6. Reading the record (M4, P15)

Three findings bear on the worked case's first step. First, the "tamper-proof" record failed in Microsoft's own
product: Copilot file access went unrecorded in Unified Audit Logs until outside researchers found it
(`microsoft2026responsible`, PDF p. 19). Second, the records do mark commitment points for their enterprise readers:
Purview types each resource action, Foundry traces record tool calls, delegations and enforced policies, and ACS
interception points sit at tool-call boundaries. M4(b)'s "scriptio continua for the auditor" therefore fails as stated
for enterprise traces; it holds for the person acted on, who has no trace at all. Third, marking evidence helps effort
but not accuracy in the one controlled test: with HANSEL, wrong agent answers were still accepted 32.1% of the time,
and full-log readers caught 60.7% of wrong answers, largely by redoing the task (`zhang2026hansel`). Lookup in traces is
easy (`zhao2026agentgui`); judging whether an action was right takes over an hour per transcript at AUC 0.65
(`kutasov2025shade`).

### C7. Microsoft against its own T1.3 and A5.4 (M7, A7)

I found no Microsoft evaluation of whether people "can interpret the relevant system responses reasonably well" (T1.3)
or can perform oversight "in realistic conditions" (A5.4). The 2026 report, searched page by page, has neither; the
nearest items are clinician and public ratings of Copilot Health's clarity and safety, a design aim of "designing
experiences so users interpret outputs correctly", and guidance for operators (`microsoft2026responsible`, PDF pp. 18,
21). The report also says the Standard has been "re-engineered" with developer and deployer chapters; the new text was
not found published, so whether T1.3 and A5.4 survive is unknown.

### Claims the sources contradict

1. **A5 as a claim about LLM tools in general.** AP2 declares a user-signed envelope to counterparties
   (`parikh2025powering`, `google2026agentic`). A5 holds for Nadella's post and Microsoft's agent controls.
2. **M4(b) as stated ("no marked points of commitment").** Enterprise traces and audit records mark tool calls and
   actions (`microsoft2026audit`, `microsoft2026responsible`, `elmergawi2026introducing`); AP2 mandates are marked
   commitments. The claim survives only for the person acted on.
3. **"No end-user confirmation step" (if the paper implies it).** Cowork, Copilot Studio, Codex and Claude Code all
   offer the agent's user a pre-action approval; Shavit et al. give the user the brake.
4. **E14 as the whole of the verification story.** The terms now assign actions, not only outputs, to the user
   (`microsoft2026copilot`, `anthropic2025consumer`, `google2026gemini`); E14 understates.
5. **P15's record as complete.** Microsoft reports a gap in its own audit logs (`microsoft2026responsible`).
6. **Using T1.3 and A5.4 as Microsoft's current standard.** The 2026 report describes a replacement Standard; the paper
   should cite v2 (2022) as the standard Microsoft professed then and note the re-engineering.
7. **Palod et al.'s abstract ("persuasive but not informative") for raw traces.** Their Table 3 shows no rise in
   accepting wrong answers for raw traces; cite the table, not the abstract.

---

## (d) What the argument can rest on

| Claim (premise) | Cards and read status | Verdict |
|---|---|---|
| Microsoft's agent controls (P11–P12 analogues) are authored, declared and audited for the deploying organisation (A5, M1, M6) | `elmergawi2026introducing` (full); `microsoft2026overview` (full); `microsoft2026microsoft` (full); `microsoft2026tracing` (full) | Carried |
| The people acted on get notice, not the envelope (A5, M9) | `microsoft2026responsible` (part, PDF p. 18); `microsoft2026microsoft` (full); `anthropic2026usage` (part) | Carried |
| No LLM tool declares a binding envelope to counterparties (A5, general form) | — | **Contradicted** by `parikh2025powering` (full), `google2026agentic` (part) |
| Suppliers assign verification of outputs and actions to users and deployers (A4, M10) | `microsoft2026copilot` (full); `anthropic2025consumer` (part); `anthropic2025commercial` (part); `google2026gemini` (part) | Carried |
| No one outside the supplier reads raw chain of thought in deployed products (M3, P9) | `openai2026reasoning` (part); `anthropic2026thinking` (part, Anthropic); `microsoft2026use` (part) | Carried |
| Readers of reasoning traces do not reject wrong outputs better (M3, A8) | `palod2026evaluating` (part; main text full); `park2025critical` (part) | Carried narrowly (lay users; preprints) |
| Approval gates are thinned or automated (M8, A8) | `microsoft2025multistage` (full); `openai2026agent` (part); `anthropic2026configure` (part); `anthropic2026measuring` (full, Anthropic); `felt2012android` (part) | Carried |
| The record kept by one side (M4(a)) | `microsoft2026audit` (full); `microsoft2026tracing` (full) | Carried |
| Records do not mark commitments (M4(b)) | — | **Contradicted** for enterprise readers (see C6); holds only for the person acted on |
| A complete log does not let people check outcomes well (M4) | `zhang2026hansel` (part); `kutasov2025shade` (dxd, part); `zhao2026agentgui` (part, complicates) | Carried narrowly (small studies) |
| Microsoft has not evaluated T1.3 / A5.4 (M7, A7) | `microsoft2026responsible` (part, all pages searched) | Carried as absence; the replacement Standard is unread |
| The industry's brake is held by the deployer's "authorized person" (M8) | `shavit2023practices` (full) | Complicated: OpenAI's scheme gives it to the user |

---

## (e) Gaps and blocks

| Item | Status | Where a Bentley library user would find it |
|---|---|---|
| OpenAI Terms of Use (openai.com/policies/terms-of-use/) | 403 (Cloudflare) | Open in a normal browser; or the Internet Archive capture of the page |
| OpenAI, "Learning to reason with LLMs" (Sept 2024) | 403 | Browser, openai.com/index/learning-to-reason-with-llms/ |
| OpenAI help article "ChatGPT agent" (11752874) | 403 | Browser, help.openai.com |
| ChatGPT agent system card; Operator system card (cdn.openai.com) | Not attempted (URLs only in Feng et al. refs 40–41) | cdn.openai.com PDFs, as cited in `feng2025regulatory` p. 7 |
| Microsoft re-engineered Responsible AI Standard (2026), Developer and Deployer Chapters | Not found published | Microsoft responsible-AI site; ask whether an external release exists |
| Copilot Cowork application card (2026 report fn. 37) | Not located by search | Microsoft Learn transparency / application cards index |
| Microsoft 365 Roadmap ID 570434 on microsoft.com | Read via third-party archive only | microsoft.com/microsoft-365/roadmap |
| Tariq et al. (2025), ACM CSUR 57(9), doi:10.1145/3723158 | Abstract only; ACM 403 | ACM Digital Library (Bentley subscription) |
| Mackworth (1948), QJEP 1(1):6–21, doi:10.1080/17470214808416738 | Not accessible | Taylor & Francis Online via Bentley; or a print run of QJEP |
| Warm, Parasuraman and Matthews (2008), Human Factors 50(3):433–441 | Abstract only | SAGE Journals via Bentley |
| AP2 linked files (checkout_mandate.md, payment_mandate.md, flows.md) | Not read | github.com/google-agentic-commerce/AP2/docs/ap2 (open) |
| Park et al. (2025) method and appendices; Tang et al. (2025) full | Read in part | arXiv (open) |
| Consensus (quota exhausted until 1 Nov) and Scholar Gateway (access denied) | Blocked | Rerun the three Consensus queries in row 21 after 1 Nov |
| Microsoft Copilot Studio "human in the loop" request-for-information action | Not located on Learn | Microsoft Learn, Copilot Studio agent flows |
</content>
</invoke>
