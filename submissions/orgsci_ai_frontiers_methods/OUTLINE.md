# Outline: proposal package (*Organization Science*, AI-Enabled Frontiers)

[DRAFTED by Claude, 26 Oct 2026. Proposal of 1,500–2,000 words plus references; technical appendix; repository.]

| Part | Words | Content | Sources |
|---|---|---|---|
| 1. The problem | 300 | "Triadic" is asserted in the literature and never tested. Two published cases are described as three-party. | `curchod2020`, `lima_pdw/literature/models/cameron2024.md`, `stark2020algorithmic` (p. 53) |
| 2. What we have done | 450 | The classifier, the 256-form census, the proxy failure, and the six-stage AI-assisted pipeline with human gates. | `org_frontier/classifier/README.md`, `org_frontier/STRUCTURAL_FINDINGS.md` (lines 18–20, 46–48), `org_frontier/protocol/RESEARCH_PROTOCOL.md` |
| 3. What we will do | 450 | Release the classifier with a model-writing guide. Build a case-to-model module in which AI drafts candidate models and humans approve them. Run it on 10–20 published platform cases. Report verdicts with sensitivity to encoding. | `org_frontier/field/README.md` (version-0 protocol, ten mocks) |
| 4. Key risks | 300 | (a) Encoding sensitivity: Φ magnitude is not a scale, so only the binary verdict is read. (b) The model-to-organization validation gap. (c) Computational cost beyond five nodes. | `org_frontier/classifier/README.md`; `org_frontier/README.md` line 19 |
| 5. If successful | 300 | Structural claims become exact and comparable. Theory can ask which arrangements demand a triadic competence. | — |
| Technical appendix | — | Definitions (Φ over the MIP versus the complete cut), validation on the lab's own controls, and runtime. | `ci/reproduce.json` checks |
| Repository | — | An anonymized fork of `org_frontier/classifier/` and `protocol/`, with no author names and no lab history. | — |
| **Total** | **1,800** | | |
