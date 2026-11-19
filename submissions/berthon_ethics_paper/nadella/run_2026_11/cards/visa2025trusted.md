---
citekey: visa2025trusted
title: Trusted Agent Protocol (repository README)
authors: Visa
year: 2025
doi: null
source_basis: full-text
pages_read: README.md in full (sections "The Challenge", "The Solution", "Key Benefits", "Quick Start", "Architecture Overview"); component READMEs and code not read
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B5/visa2025trusted/README.md
sha256: 5f5fbaef32d575d1f83a0a2c8051338c37f7224cd6afd464d638b8f2863cada5
verified: pending
structure_sections: 4.4-medium; 4.4-record; 7-D03; counter
type: specification
venue: GitHub repository visa/trusted-agent-protocol, commit 16d59bd (2025-10-28); repository created 2025-10-10
source_url: https://raw.githubusercontent.com/visa/trusted-agent-protocol/16d59bdf3f8a542bc538d0962edbb80ea30a02af/README.md
record_check: GitHub API repos/visa/trusted-agent-protocol (owner visa, created 2025-10-10, last push 2025-10-28, licence not asserted); Visa press release page usa.visa.com releaseId 21716, saved as press.html with text extract press.txt beside local_path, gives the title "Visa Introduces Trusted Agent Protocol: An Ecosystem-Led Framework for AI Commerce", dated 10/14/2025
facet: B5
supersedes: none
written: 2026-11-18
---

## Summary

Read in full (the top-level README at a pinned commit; about 800 words). Visa's Trusted Agent Protocol lets an AI
agent prove to a merchant, with a cryptographic signature on each request, that it is a recognised agent, that it acts
for an authenticated user, and that it carries that user's instructions for the specific action. The signature
carries timestamps, a session identifier, a key identifier and an algorithm identifier, and is bound to the
merchant's domain and the page or operation, so the merchant can check freshness and refuse replays. Merchants can
also receive consumer and payment identifiers "as consented by the consumer". The repository ships a sample
implementation: an agent, a merchant front and back end, a CDN proxy verifying RFC 9421 signatures, and an agent
registry of public keys. The README states the merchant's problem as a choice between blocking agent commerce and
accepting risk from unverified agents.

## Key facts it relies on

- "The Challenge": "For an agent to make a purchase, merchants must answer: Is this a legitimate, trusted, and recognized AI agent? Is it acting on behalf of a specific, authenticated user? Does the agent carry valid instructions from the user to make this purchase?" [quote; list markers removed]
- "The Solution": the protocol "provides a standardized, cryptographic method for an AI agent to prove its identity and associated authorization directly to merchants. By presenting a secure digital signature with every interaction, a merchant can verify that an agent is legitimate and has the user's permission to act." [quote]
- "The Solution": the signature "includes timestamps, a unique session identifier, key identifier, and algorithm identifier, allowing you to verify that the signature is current and prevent relays or replays." [quote]
- "The Solution": "Ensure the agent is authorized for the specific action it is taking (browsing or payment) as the signature is bound to your domain and the specific operation being performed." [quote; double space in source normalised]
- "The Solution": merchants may receive "as consented by the consumer, verifiable consumer identifiers, Payment Account References (PARs) for cards on file, or other identifiers like loyalty numbers, emails and phone numbers". [quote]
- "The Solution": the proof is "a powerful new tool to reduce fraud and minimize chargebacks from unauthorized transactions." [quote]
- "Architecture Overview": an "Agent Registry manages agent public keys and metadata". Who runs the registry in production is not stated in the README. [quote; paraphrase]

## Critical notes

- Limits: a vendor README and sample code, not evidence of deployment or of effect; I found no adoption figures or independent evaluation. The press release (14 Oct 2025, saved beside the README) says the protocol was developed with Cloudflare and that its initial specifications apply to the Visa network; neither it nor the README confirms a secondary explainer's claim that Visa operates the key directory.
- Strongest use against the paper: a second deployed design, besides AP2 (`google2026agentic`), that gives the counterparty an agent acts on a verifiable record of who the agent is, whom it serves and what it is authorised to do, at the moment of the action. That is a declared envelope, bound toward the person acted on (STRUCTURE 4.4 "who holds the medium"; D03), built by a payments network, not by the model provider or deployer.
- What it leaves standing: the party protected is the merchant, a firm, and the stated purpose is fraud and chargeback reduction; the consumer appears as the source of consent and identifiers. Nothing in it reaches a customer on whom a firm's agent acts (a refund or service agent), and the counterparty gets verification only, with no brake beyond refusing the request and no standing.
- Person acted on (here the merchant) gets: record — partial (signed identity, session and authorisation per request); brake — partial (may refuse unverified agents); envelope — yes (authorisation bound to domain and operation); standing — no; loss cover — no (fraud reduction only, no allocation of loss stated).
- Corrected by V-B-1: record_check and the Limits note had said the Visa press release returned a script shell with no text; the saved press.txt holds the full release (title, 10/14/2025, Cloudflare collaboration, "initial specifications apply to the Visa network in this phase"), so both now say so.
