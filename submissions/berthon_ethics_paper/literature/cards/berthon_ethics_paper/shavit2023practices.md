---
citekey: shavit2023practices
title: Practices for Governing Agentic AI Systems
authors: Shavit, Yonadav; Agarwal, Sandhini; Brundage, Miles; Adler, Steven; O'Keefe, Cullen; Campbell, Rosie; Lee, Teddy; Mishkin, Pamela; Eloundou, Tyna; Hickey, Alan; Slama, Katarina; Ahmad, Lama; McMillan, Paul; Beutel, Alex; Passos, Alexandre; Robinson, David G.
year: 2023
type: report
doi: null
venue: OpenAI white paper (no date on the PDF; its references run to Nov 2023)
source_basis: full-text
pages_read: "pp. 1-19 (all body text and acknowledgements); references pp. 19-23 skimmed"
source_url: https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/oai_shavit2023/page.pdf
sha256: 22b3a8607ed781a848b82b0bfe8e638b16cd027aac90a19b2aecf236063d0e7c
manuscript_lines: []
ledger_rows: [D01, D04, E15]
premises: [A4, A5, A8]
facet: N1
anthropic_authored: false
verified: corrected
written: 2026-10-24
---

## Summary
OpenAI researchers propose seven baseline practices for agentic systems and allocate them among three "human
parties": model developer, system deployer and user. The practices are evaluating suitability, constraining the action
space and requiring approval, default behaviours, legibility of activity, automatic monitoring, attributability and
interruptibility. Third parties appear as those an agent interacts with, who might "demand" identification. The paper
names the problems the present facet is about: approvals turning into a "rubber stamp", chains of thought that
"balloon beyond a user's ability to feasibly keep up", and the question "How can the effectiveness and meaningfulness
of human oversight be evaluated?" It offers practices and open questions, not evidence.

## Key facts it relies on
- Parties: "the three primary parties that may influence an AI agent’s operations are the model developer, the system
  deployer, and the user" (p. 5).
- Accountability: "it is important that at least one human entity is accountable for every uncompensated direct harm
  caused by an agentic AI system" (p. 3; footnote marker 5 removed).
- Approval: "This raises the key challenge of how a system deployer should ensure that the user has enough context to
  sufficiently understand the implications of the action they’re approving. This is also made harder when the user
  must approve many decisions and thus must make each approval quickly" (p. 9).
- Open questions: best practices "to avoid their turning into a “rubber stamp”" and "How can the effectiveness and
  meaningfulness of human oversight be evaluated?" (p. 10).
- Legibility: chains of thought "may balloon beyond a user’s ability to feasibly keep up" (p. 12); "It may be
  particularly important that system deployers provide the user with a ledger of actions taken by the agent" (p. 12).
- Monitoring: "human users may not always have the time to go through the agent activity logs exposed by the system
  deployer at the speed or scale they desire" (p. 12).
- Third parties: in high-stakes interactions "third parties (including external tool providers) interacting with a
  user’s agent could demand such identification before starting the interaction" (p. 14).
- Interruptibility: "System deployers could be required to make sure that a user can always activate a graceful
  shutdown procedure for its agent at any time" (p. 14).
- Redundant brakes and third parties: the paper raises "in what circumstances an external party has the right or
  obligation to terminate a user’s agent", and proposes that "society could encourage redundancy in the number of
  human parties that can turn off an AI agent instance. The two relevant parties are the system deployer and the data
  center operator or chip owner on whose hardware the AI system is running" (p. 15).

## Critical notes from the literature
- Vendor-authored (OpenAI); a position paper with no data. The taxonomy is "not intended to establish a prescriptive
  framework for allocation of responsibility" (p. 5, fn. 11).
- Feng et al. (feng2025regulatory, p. 2) treat its legibility practice as the basis for regulating visible agent traces.

## Where the argument uses it
- A4 / M5 / M8: narrowed. The user holds the first brake (p. 14) and reads the ledger (p. 12); deployer and
  data-centre operator hold redundant ones, and the paper leaves open a third party's right to terminate (p. 15). That is a different seat from P19's and complicates reading the industry as uniformly
  deployer-centred; but the user here is the agent's principal, not the person acted on.
- A5: holds. The people an agent acts on enter only as parties who might demand an agent ID (p. 14); no practice
  declares the action-space constraints to them.
- A8 (capacity): supports. The paper itself asks how oversight could be shown to work and gives no answer (p. 10).

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
