---
citekey: anthropic2025safeagents
title: Our framework for developing safe and trustworthy agents
authors: Anthropic
year: 2025
doi: null
source_basis: full-text
pages_read: whole page (one web page, sections in order)
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B2/anthropic2025safeagents/anthropic2025safeagents.txt
sha256: 02841abd15d04b4b199d6b639347cc4466eaf355291876bc1c02d999dcea9353
verified: corrected
structure_sections: 1.3; 4.3; 4.4-stop; 4.4-record
type: report
venue: Anthropic website, research post, published 4 Aug 2025
source_url: https://www.anthropic.com/research/our-framework-for-developing-safe-and-trustworthy-agents
record_check: publisher page itself (title, issuer and "Published Aug 4, 2025" read in the saved text); no DOI
facet: B2
supersedes: none
written: 2026-11-18
---

## Summary

Read in full. Anthropic sets out five principles for agent development: keep humans in control, make agent behaviour transparent, align agents with human values and expectations, protect privacy across extended interactions, and secure agents' interactions. The people it names throughout are the user who gave the agent a goal and the organisation or administrator that deploys it. Its examples include a company's expense agent, a churn-analysis agent, a file-organising agent and Claude Code. The framework describes what Anthropic aims to do, with no binding commitment, and promises later revision. People other than the user and the deploying organisation's administrators appear only in passing (the facilities team a churn agent contacts; a department whose confidential decisions an agent carries to another), and the page states nothing owed to them.

## Key facts it relies on

- Control is placed with the user: "humans should retain control over how their goals are pursued, particularly before high-stakes decisions are made." [quote] (section "Keeping humans in control while enabling agent autonomy")
- Stopping is described for Claude Code: "In Claude Code, humans can stop Claude whenever they want and redirect its approach." [quote] (same section)
- Transparency serves the person directing the agent: "Humans need visibility into agents' problem-solving processes." [quote] (section "Transparency in agent behavior"). The example is a to-do checklist shown to users in real time. [paraphrase] (same section)
- Administrators set limits for their organisation: "Enterprise administrators can also set which connectors users in their organizations can connect to." [quote] (section "Protecting privacy across extended interactions")
- The post names the risk that an agent works against the interests of the person who set it going: "More concerning are cases where agents pursue goals in ways that actively work against users' interests." [quote] (section "Aligning agents with human values and expectations")
- The post offers no mechanism for contest, redress or compensation, and no sentence states anything owed to a person who is neither a user nor a deploying organisation; such people appear only in passing (the facilities team the churn agent contacts, section "Transparency in agent behavior"; the department whose confidential decisions are carried to another, section "Protecting privacy across extended interactions"). [paraphrase] (whole page, checked by reading; absence claim)

## Critical notes

Anthropic-authored; corroborate. Corroboration: the user-control and observability claims are matched in an independent firm's paper, google2025secure_agents (Principles 1 and 3, pp. 12-13), and in a public body's framework, imda2026agentic (2.2.2, p. 29; 2.3.3, p. 43). The Claude Code claims (stop at any time, read-only default, to-do checklist) carry no corroboration found; the carded Anthropic documentation cards (anthropic2026configure) are Anthropic-authored too.

Limits: a short statement of principle, with controls named only by example (Claude Code's read-only default and approval prompts, MCP connector permissions, classifiers against prompt injection), no log format and no remedy. It is written as aims ("We aim to adhere"), and Anthropic does not say these are enforced.

Bearing: Person acted on gets: record no; brake no (the brake belongs to the user and deployer); envelope no (limits are set by users and administrators; the page does not say that anyone else can see them); standing no; loss cover no. Locators: sections named above. Structure sections 1.3, 4.3, 4.4-stop, 4.4-record: supports the claim that the frame addresses the user and deployer only; not independent of Anthropic's own account.

Corrected by the Fable read (V-B-1): the Summary's last sentence and the absence bullet claimed that the page names no person acted on other than user and deployer; the page does mention the facilities team a churn agent contacts and a department exposed by carried-over information, so both now say that such people appear in passing and are owed nothing stated. "The examples are" changed to "Its examples include" (the page also has a wedding plan, a board presentation, Trellix and Block). "No controls specified" narrowed to the controls the page names by example. "The person acted on cannot see them" was an inference and now says what the page does not say.
