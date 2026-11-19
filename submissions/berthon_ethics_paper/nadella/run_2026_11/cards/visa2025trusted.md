---
citekey: visa2025trusted
title: Trusted Agent Protocol (repository README)
authors: Visa
year: 2025
doi: null
source_basis: full-text
pages_read: README.md in full (sections "The Challenge", "The Solution", "Key Benefits", "Quick Start", "Architecture Overview"; the flow diagram under "Example Agent Verification for Payments" is an image and was not read); the press release saved beside it (press.txt) in full; component READMEs and code not read
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B5/visa2025trusted/README.md
sha256: 5f5fbaef32d575d1f83a0a2c8051338c37f7224cd6afd464d638b8f2863cada5
verified: corrected
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

Read in full (the top-level README at a pinned commit; about 800 words; its flow diagram is an image and was not
read). The README poses three questions a merchant must answer before an agent buys: whether the agent is legitimate
and recognised, whether it acts for a specific authenticated user, and whether it carries that user's valid
instructions for the purchase. Visa's Trusted Agent Protocol answers with a cryptographic signature on every
interaction, by which the agent proves "its identity and associated authorization" and the merchant verifies that the
agent "is legitimate and has the user's permission to act". The signature carries timestamps, a session identifier, a
key identifier and an algorithm identifier, and is bound to the merchant's domain and the page or operation, so the
merchant can check freshness and refuse replays. Merchants can also receive consumer and payment identifiers "as
consented by the consumer". The repository ships a sample implementation: an agent, a merchant front and back end, a
CDN proxy verifying RFC 9421 signatures, and an agent registry of public keys. The README states the merchant's
problem as a choice between blocking agent commerce and accepting risk from unverified agents.

## Key facts it relies on

- "The Challenge": "For an agent to make a purchase, merchants must answer: Is this a legitimate, trusted, and recognized AI agent? Is it acting on behalf of a specific, authenticated user? Does the agent carry valid instructions from the user to make this purchase?" [quote; list markers removed]
- "The Challenge": "Without a standard, merchants face an impossible choice:" either "Block potentially valuable agent-driven commerce" or "Accept significant operational and security risks from unverified agents". [quote; list and bold markers removed]
- "The Solution": the protocol "provides a standardized, cryptographic method for an AI agent to prove its identity and associated authorization directly to merchants. By presenting a secure digital signature with every interaction, a merchant can verify that an agent is legitimate and has the user's permission to act." [quote]
- "The Solution": the signature "includes timestamps, a unique session identifier, key identifier, and algorithm identifier, allowing you to verify that the signature is current and prevent relays or replays." [quote]
- "The Solution": "Ensure the agent is authorized for the specific action it is taking (browsing or payment) as the signature is bound to your domain and the specific operation being performed." [quote; double space in source normalised]
- "The Solution": merchants may receive "as consented by the consumer, verifiable consumer identifiers, Payment Account References (PARs) for cards on file, or other identifiers like loyalty numbers, emails and phone numbers". [quote]
- "The Solution": the proof is "a powerful new tool to reduce fraud and minimize chargebacks from unauthorized transactions." [quote]
- "Key Benefits": "Every request from a trusted agent is cryptographically locked to a merchant's specific website and the exact page with which the agent is interacting"; "Each signature includes unique, time-sensitive elements that ensure every request is fresh and valid only for a single use." [quote]
- "Key Benefits": the protocol lets a merchant "distinguish legitimate, authorized AI agents from other automated traffic" and "confidently welcome agent-driven commerce while protecting your site from harmful bots." [quote]
- "Architecture Overview": an "Agent Registry manages agent public keys and metadata". Who runs the registry in production is not stated in the README. [quote; bold markers removed; paraphrase]
- The README states no spending limit, no content of the user's instruction, and no rule on disputes, refunds or liability (README searched for limit, amount, dispute, refund, liab, revok, record, receipt: none; "chargebacks" once, in "The Solution"). [paraphrase]

## Critical notes

- Limits: a vendor README and sample code, not evidence of deployment or of effect; I found no adoption figures or independent evaluation. The press release (14 Oct 2025, saved beside the README) says the protocol was developed with Cloudflare, that it "is available today in the Visa Developer Center and GitHub", and that its initial specifications apply to the Visa network; neither it nor the README confirms a secondary explainer's claim that Visa operates the key directory. The release speaks of "approved agents" without saying who approves them, and lists Microsoft among "early partners" that gave feedback.
- Record: the GitHub API (checked 19 Nov 2026, generic client) shows no push to the repository since 28 Oct 2025 and no change to README.md since 13 Oct 2025; the pinned commit 16d59bd changed one file of the sample proxy.
- Strongest use against the paper (the card's inference): a second published design, besides AP2 (`google2026agentic`), with sample code, that gives the counterparty an agent acts on a verifiable attestation of who the agent is, whom it serves and that it is authorised for this action, at the moment of the action. The attestation is bound toward the person acted on (STRUCTURE 4.4 "who holds the medium"; D03) and comes from a payments network, not from the model provider or deployer. It is less than a declared envelope: the README describes no statement to the merchant of the limits the user set.
- What it leaves standing: the party protected is the merchant, a firm, and the stated purpose is fraud and chargeback reduction; the consumer appears as the source of consent and identifiers, and the release names "visibility into the consumer behind the agent" as a merchant need. Nothing in it reaches a customer on whom a firm's agent acts (a refund or service agent), and the counterparty gets verification only, with no brake beyond turning the request away and no standing.
- Person acted on (here the merchant) gets: record — partial (signed identity, session and authorisation with each request, "The Solution"; no log, receipt or retained record is described); brake — partial (the README implies the merchant may turn away traffic it cannot verify, "Key Benefits"; it describes no stop once a verified agent acts); envelope — partial (authorisation for "browsing or payment" bound to domain and operation, "The Solution"; no limit set by the user is disclosed); standing — no; loss cover — no (fraud reduction only, no allocation of loss stated).
- Corrected by V-B-1: record_check and the Limits note had said the Visa press release returned a script shell with no text; the saved press.txt holds the full release (title, 10/14/2025, Cloudflare collaboration, "initial specifications apply to the Visa network in this phase"), so both now say so.
- Corrected by the Fable read (V-B-1), settling the verifier's OVERSTATED: "a second deployed design" is now "a second published design ... with sample code", the verifier's wording, since the release says only that the protocol is "available". Summary: the sentence that had the agent prove three things now gives the README's three questions as questions and its answer in its own words; the README does not say the signature carries the user's instructions. Key facts: four facts added from "The Challenge" and "Key Benefits", which the Summary and the bearing line rely on, and one on what the README does not state; the registry quotation marked as having bold markers removed. Critical notes: "a verifiable record" changed to "a verifiable attestation" and "a declared envelope" narrowed, with the envelope value changed from yes to partial, because the README discloses a per-request authorisation and no limits; the record and brake values now say what the README does and does not describe; three points added from the press release (availability, "approved agents", Microsoft among early partners) and a record note from the GitHub API. `pages_read` now names the press release and the unread image.
