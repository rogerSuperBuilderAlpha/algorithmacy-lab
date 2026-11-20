---
citekey: laux2024three
title: Three pathways for standardisation and ethical disclosure by default under the European Union Artificial Intelligence Act
authors: Laux, Johann; Wachter, Sandra; Mittelstadt, Brent
year: 2024
type: article
doi: 10.1016/j.clsr.2024.105957
venue: Computer Law & Security Review 53, 105957
source_basis: full-text
pages_read: "whole author manuscript (Europe PMC PMC7618411), Abstract and sections 1-5; no page numbers in this version, locators are sections"
source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7618411/fullTextXML
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N4/laux2024/PMC7618411.xml
sha256: 6b462f133a5240268bdb0c65dee689ef540467735ff5986e6424f4f89215cdda
manuscript_lines: []
ledger_rows: [O02, D05]
premises: [A4]
facet: N4
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Crossref confirms title, venue (CLSR 53, article 105957, July 2024) and authors. I read the funder author manuscript from Europe PMC's full-text API (the PMC page served a challenge to plain HTTP; the Europe PMC REST service did not). The authors ask how European standardisation bodies (SSOs) can handle the "hard normative questions" that AI Act standards raise, such as acceptable bias thresholds. They reject two pathways: SSOs answering such questions themselves, which "would inevitably raise ... legitimacy concerns" because standardisation "tends to exclude non-expert stakeholders and the public at large" and "Industry representatives exert great influence in SSOs" (§1); and SSOs tracking existing consensus, which, on the record of ISO 26000 and SC 42, SSOs lack the "institutional design and capacity" to do reliably (§3). They propose a third: standards requiring "ethical disclosure by default", meaning minimum testing, documentation and public reporting, so that "local decision-makers", including "individuals subject to its use or otherwise affected by it" and civil society acting for them, can request the evidence (§4). The danger they name is the presumption of conformity itself: if standards leave the hard questions open, "AI providers can be considered compliant while simultaneously setting subjective ethical trade-offs and thresholds without direct external stakeholder involvement" (§4).

## Key facts it relies on
- §1: "Standardisation as a governance tool has been widely criticized as lacking legitimacy. Largely a technical discourse, it tends to exclude non-expert stakeholders and the public at large. Industry representatives exert great influence in SSOs."
- §4: "conformity with harmonised standards under the AIA will be presumed to indicate compliance with the requirements of the regulation. It follows that if SSOs fail to provide specific, implementable answers to hard normative questions in these standards, AI providers can be considered compliant while simultaneously setting subjective ethical trade-offs and thresholds without direct external stakeholder involvement."
- §4: such questions "should not be left by default to entities or procedures lacking political legitimacy."
- §4: "Ethical disclosure by default will shift setting of acceptable ethical trade-offs and thresholds away from AI providers and towards local decision-makers with the legitimacy and knowledge to make such determinations."
- §4: "Relevant local stakeholders should include organisations using AI provided by a third party, individuals subject to its use or otherwise affected by it, civil society organisations acting on behalf of such individuals, lawyers and the judiciary, as well as regulators".

## Critical notes from the literature
- Gornet and Maxwell (2024, p. 16; `gornet2024european`): "Those impacted by the use of AI have no role to play in standardisation or certification processes".

## Where the argument uses it
- A4, M2 (P6): supports. Peer-reviewed legal scholarship states that industry-weighted standardisation lacks the legitimacy to settle the questions that matter to the affected, and that the presumption lets providers settle them.
- Complicates the duties (CB, D03): their remedy is disclosure to local stakeholders, a reading task. It is close to the paper's "declared operating envelope binding toward the people acted on" but rests on the affected person's capacity to read test results, which is what the paper doubts. Note for the lead: Laux et al. are an ally on custody and a foil on disclosure.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
