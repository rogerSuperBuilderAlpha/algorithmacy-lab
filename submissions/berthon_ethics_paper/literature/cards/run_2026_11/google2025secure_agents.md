---
citekey: google2025secure_agents
title: Google's Approach for Secure AI Agents: An Introduction
authors: Díaz, Santiago; Kern, Christoph; Olive, Kara
year: 2025
doi: null
source_basis: full-text
pages_read: pp. 1-18 of the PDF (cover to acknowledgements)
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B2/google2025secure_agents/google2025secure_agents.txt
sha256: b126d83d7c90d415cfbb1f0ee4f3cc943d4c23651f6066bb50718fccb500718a
verified: corrected
structure_sections: 1.3; 4.3; 4.4-record; 4.4-stop
type: report
venue: Google white paper, May 2025 (PDF page numbers; the saved text splits pages at form feeds)
source_url: https://services.google.com/fh/files/misc/googles_approach_for_secure_ai_agents.pdf
record_check: the PDF's own cover (title, three authors, May 2025), 18 pages by pdfinfo; no DOI
facet: B2
supersedes: none
written: 2026-11-18
---

## Summary

Read in full. The white paper is a security paper. It names rogue actions and sensitive data disclosure as the two main risks and states three principles: agents must have well-defined human controllers, agent powers must be limited, and agent actions and planning must be observable. It proposes a hybrid defence of deterministic controls and reasoning-based defences. "Users" throughout are the people who control the agent. The paper uses the word "accountability" for the link from agent to controlling human, and it names no person outside that link as a party owed a control, a record or a remedy. Third parties appear only incidentally: the wrong recipient of a mis-sent e-mail and "physical safety risks" among the impacts of rogue actions (PDF p. 10), and another user of a shared agent (PDF p. 12).

## Key facts it relies on

- Principle 1 ties each agent to a controlling human: "Every agent must have a well-defined set of controlling human user(s)." [quote] (PDF p. 12)
- Critical or irreversible actions need confirmation from that user. [paraphrase] (PDF p. 12, "explicit human confirmation")
- Users are the party that can revoke: "Users must also retain the ability to inspect and revoke any authority delegated to an agent." [quote] (PDF p. 12, Principle 2)
- Observability is for security, debugging and the user's own understanding: "agent actions, and where feasible, their planning processes, must be observable and auditable." [quote] (PDF p. 13, Principle 3). Logs capture inputs, tools invoked, parameters, outputs and ideally intermediate reasoning. [paraphrase] (PDF p. 13)
- Another person's interests appear as a harm to avoid: the paper wants controls that prevent "one user inadvertently triggering actions impacting another" [quote] (PDF p. 12). The case is two users of the same agent. Elsewhere third parties are incidental to a harm described from the user's side: an agent that picks "the wrong contact, inadvertently sharing sensitive information" [quote], and impacts that run to "physical safety risks" [quote] (PDF p. 10, Risk 1).
- Memory: "Users also need transparency and control over agent memory." [quote] (PDF p. 7)

## Critical notes

Contested by no source found in this run; it is a company white paper that announces a "forthcoming, comprehensive whitepaper" (PDF p. 4). Limits: it covers security properties and says nothing on disclosure to third parties, contest or loss cover. It is Google-authored; the other cards in this facet (imda2026agentic) give an independent public-body view of the same logging and oversight controls.

Bearing: Person acted on gets: record no (logs serve the controller and security reviewers, p. 13); brake no (revocation and confirmation belong to the controlling user, p. 12); envelope partial at most (the limits are defined for the controller's risk tolerance, p. 12; the paper does not say they are shown to anyone else); standing no; loss cover no. Structure sections 1.3, 4.3, 4.4-record, 4.4-stop: supports the claim that the controls are built for the controller; the one cross-user line is a design concern with no remedy.

Corrected by the Fable read (V-B-1), settling the verifier's OVERSTATED: the Summary said the paper "names no person outside that link" and that others appear "only" as victims of cross-user contamination; Risk 1 (PDF p. 10) names a wrongly chosen e-mail contact and "physical safety risks", so the Summary and the cross-user bullet are narrowed to say that no such person is owed a control, a record or a remedy. The basis sentence said "the rest skimmed"; all 18 pages were read at this read, so it now says "Read in full". "A point of departure for Google's later work" rested on no passage and is replaced by the paper's own announcement of a later white paper. Locators are PDF pages; the printed folio is the PDF page plus one (PDF p. 12 carries "13").
