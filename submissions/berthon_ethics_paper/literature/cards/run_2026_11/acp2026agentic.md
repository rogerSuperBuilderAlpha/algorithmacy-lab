---
citekey: acp2026agentic
title: Agentic Commerce Protocol (ACP): README, Agentic Checkout RFC (version 2026-01-16) and Principles and Mission
authors: OpenAI; Stripe
year: 2026
doi: null
source_basis: partial-text
pages_read: docs home page (FAQ); README; RFC sections 1, 2, 4.1 to 4.5, 5 (data model, message resolution) and 7; Principles and Mission. Not read: OpenAPI and JSON Schema files, the Webhooks RFC, the Delegate Payment spec, the other RFCs
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B2/acp2026agentic/acp2026agentic_combined.txt
sha256: 8a708db5eb0304dec3f9cc778f0988416b36f6d5c3dca8d16a35cb54d2df5451
verified: corrected
structure_sections: 1.3; 4.3; 4.4-record; 4.4-stop; 4.4-loss
type: report
venue: Open standard, Apache 2.0, public GitHub repository agentic-commerce-protocol; README says maintained by OpenAI and Stripe, status beta; RFC dated version 2026-01-16
source_url: https://raw.githubusercontent.com/agentic-commerce-protocol/agentic-commerce-protocol/main/rfcs/rfc.agentic_checkout.md
record_check: the repository README names OpenAI and Stripe as maintainers; the docs home page (https://www.agenticcommerce.dev/) states that Stripe and OpenAI developed the protocol; no DOI
facet: B2
supersedes: none
written: 2026-11-18
---

## Summary

Read: the README, the docs home, the principles page and sections 1, 2, 4, 5 and 7 of the checkout RFC; the machine-readable specs and the other RFCs are not read. The Agentic Commerce Protocol is a REST contract by which an agent platform (ChatGPT first) creates, updates, completes and cancels checkout sessions on a merchant's own systems. The merchant stays system of record, and payment runs on the merchant's processor. The protocol's people are buyers, agent platforms, businesses and payment providers. The text describes how a session moves between the agent platform and the merchant. The party the agent transacts with is the merchant, which holds the record and may accept or decline a transaction; the parts read state no redress for the buyer and no record of the agent's conduct. Returns and exchanges are out of scope.

## Key facts it relies on

- The merchant keeps the record: "The merchant remains the **system of record** for all orders, payments, taxes, and compliance." [quote] (RFC, preamble)
- Returns are left out of the protocol: the RFC lists "returns/exchanges workflows" as out of scope. [quote] (RFC, section 1)
- A buyer review step exists for some cases: "Buyer must authorize before order placement (policy, regulatory, or entitlement rules)" [quote] (RFC, section 5, message `resolution` values)
- Cancellation is a call from the client: the RFC defines `POST /checkout_sessions/{checkout_session_id}/cancel`, with 200 if cancelled and 405 if already completed or cancelled. [paraphrase] (RFC, section 4.5)
- The business can refuse agents: "Businesses can then choose to accept or decline transactions on a per agent, per transaction, or custom logic basis." [quote] (docs home, FAQ)
- On logs the RFC says only what not to store: "Do not log full PAN/CVC" [quote] (RFC, section 7). It sets no record duty toward the buyer. [paraphrase] (RFC sections read)

## Critical notes

Contested by no source found. Limits: partial reading, and the RFC is marked Draft with date-based versions, so later specs may differ. The documents describe a commerce protocol, so it does not follow that the absence of redress or disclosure provisions is a design choice; the OpenAI and Stripe documentation (not read here) may carry buyer protections. OpenAI's Terms of Use returned 403 to the scout and were not read.

Bearing, read from the buyer's side (the buyer is the agent's principal; the party the agent transacts with is the merchant, which is the system of record, RFC preamble, and can accept or decline per agent or per transaction, docs home FAQ): Person acted on gets: record partial (the order has a `permalink_url` on completion, RFC section 4.4, and order webhooks go to the application's receiver, section 2.3; no record of the agent's conduct); brake partial (cancel before completion, section 4.5, issued by the agent platform; buyer review for some cases, section 5); envelope no (nothing read tells the buyer or counterparty the limits the agent runs under); standing no (returns and exchanges out of scope, section 1; the session response carries `links[]` to the merchant's own `terms_of_use`, `privacy_policy` and `return_policy` pages, sections 4.1 and 5); loss cover no (no provision read). Structure sections 4.4-stop, 4.4-loss, 4.4-record: supports, on partial reading.

Corrected by V-B-1: record_check changed; the docs-home capture does state that Stripe and OpenAI developed the protocol. Also noted: the captured RFC is the repository head, whose change log runs past 2026-01-16 (the `resolution` field quoted in section 5 was added 2026-02-04).

Corrected by the Fable read (V-B-1): the Summary's basis sentence now names the RFC sections read; the Summary sentence "gives no account of any duty to the person the agent transacts against" is replaced, because the party the agent transacts with in this protocol is the merchant, which holds the record and the refusal, and the RFC does set technical duties on the client toward the merchant's server (sections 2.1, 4.4); the bearing line now says whose side it is read from and names the policy links. The RFC header reads "Version: 2026-01-16" while the README's quick links name `spec/2026-04-17/` as the latest stable spec and the RFC's own checklist (section 10) names `API-Version: 2026-01-15`.
