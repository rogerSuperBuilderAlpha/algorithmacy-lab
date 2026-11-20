---
citekey: microsoft2026artificial
title: Artificial intelligence (AI) shared responsibility model
authors: Microsoft
year: 2026
doi: null
source_basis: full-text
pages_read: whole page: intro, Note, "Division of responsibility", "AI layer overview" (AI platform, AI application, AI usage), "Configure before you customize", "Next steps"; the responsibility diagram is an image and was not read
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B1/ms_shared_responsibility_ai/ms_shared_responsibility_ai.txt
sha256: a1076bcfce78189fbb3623b265976d46acc641cab856b66f064b808ca1f19b2a
verified: corrected
structure_sections: 4.3; 4.4-loss; 4.2; 6-responsibilization
type: technical documentation
venue: Microsoft Learn (Azure security fundamentals), last updated 2026-08-24
source_url: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai
record_check: publisher page; saved HTML (sha256 5938ab52…) fetched by Scout B on 2026-11-18; page heading "Artificial intelligence (AI) shared responsibility model", ms.date 2026-08-24, "Last updated on 2026-08-24"
facet: B1
supersedes: none
written: 2026-11-18
---

## Summary

Read in full, except the diagram, which is an image. Microsoft's guidance divides the work of running generative AI
between Microsoft and the customer organisation by deployment type (SaaS, PaaS, IaaS) and by three layers: the AI
platform, the AI application and AI usage. A note defines "responsibility" in a governance sense (who configures,
operates and monitors each control) and disclaims any legal effect. Security responsibility generally sits with the
party that performs the task. At the usage layer the page gives "user behavior and accountability" more emphasis,
because users steer output, and tells organisations to update acceptable-use policies and educate users. It
recommends SaaS such as Copilot for initial adoption "and for all subsequent AI workloads" because it minimises the
customer's responsibility, and says only organisations with deep expertise should build custom models. It points to a separate "AI agent shared
responsibility model" for autonomous agents, which was not fetched.

## Key facts it relies on

- Purpose: "it's critical to understand the shared responsibility model and which tasks the AI platform or application provider handles and which tasks you handle". intro [quote]
- Scope pointer: "For autonomous, tool-using AI agents, see the AI agent shared responsibility model". intro [quote]
- "This article uses "responsibility" in a governance sense: who is expected to configure, operate, and monitor each control. It is illustrative guidance and is not intended to convey legal conclusions or to modify or contradict the terms of any agreement between you and Microsoft." Note [quote]
- "The security responsibilities generally reside with the party that performs the tasks, but an AI provider might choose to expose security or other controls as a configuration option to you as appropriate." AI layer overview [quote]
- The generative interface reverses the older burden: "The generative AI interface contrasts with previous interfaces that primarily force users to learn the system design and functionality and adjust to it." AI usage [quote]
- "User behavior and accountability require more emphasis because users exert more influence on the output of the systems." AI usage [quote]
- "It's critical to update acceptable use policies and educate users on the differences between standard IT applications and AI-enabled applications." AI usage [quote]
- SaaS first: Microsoft recommends Copilot-style SaaS "for their initial adoption of AI and for all subsequent AI workloads" because "This approach minimizes the level of responsibility and expertise your organization must provide to design, operate, and secure these highly complex capabilities." Configure before you customize [quote]
- "Only organizations with deep expertise in data science and the security, privacy, and ethical considerations of AI should adopt custom model building." Configure before you customize [quote]

## Critical notes

Microsoft-authored guidance with an explicit disclaimer that it changes no contract; the binding allocation sits in
the product terms (microsoft2026microsoft; microsoft2026services; microsoft2026copilot). The two parties are Microsoft
and the customer organisation; the "user" at the usage layer is the organisation's user, who is to be governed by
acceptable-use policy and educated. The page does not mention people outside the organisation; the nearest phrase is that guardrails are "critical to
protecting people, data, and business assets" (AI usage), which names no one in particular.
The page is about generative AI workloads in general; the agent-specific companion page it names is the more direct
source for the agent architecture and should be fetched. Its claim that generative interfaces adjust to the user
rather than the reverse is a design premise, stated without evidence.
Person acted on gets: record no; brake no; envelope no; standing no; loss cover no (the page allocates tasks between
Microsoft and the customer only, Note and Division of responsibility).

Corrected by the Fable read (V-B-1): the Summary and the SaaS bullet said Microsoft recommends SaaS "as the starting point"; the page recommends it for initial adoption "and for all subsequent AI workloads", and both now say so. "Restricts custom model building" softened to the page's "should". The note that outsiders "appear only as 'people' whom guardrails protect" read the generic word "people" as people outside the organisation; it now reports the phrase as it stands. The saved HTML's metadata gives updated_at 2026-10-08 beside the displayed "Last updated on 2026-08-24".
