# Research plan: Nadella's moves against the failures of growing literacy

*Written by Claude on 2026-10-24 under the author's delegation ("Use your judgement", `README.md`, Rulings). Plan
only: no research has run. Each hypothesis is stated so the evidence can refute it.*

**The claim to test.** Each of Nadella's moves in "Models as Insider Risks" (P1–P21) takes a choice that the
institutions of growing literacy took and that the record counts as a failure by the consolidation's three internal
standards (contemporaries objected; a professed standard was broken; a promise went unmet). For each, the plan names
the historical failure, what the lab already holds, what would refute the pairing, and what must still be found.

## 1. The pairings

| # | Move | Hypothesis: the failure it repeats | In hand | Refuted if | Still needed |
|---|---|---|---|---|---|
| M1 | Authority and responsibility rest with the deploying organisation; "Orgs" set access and actions (P3, P5, P17) | **Custody of the convention by the interested party.** The page's conventions were held by ruler and church; the press by a chartered company that was also the Crown's licenser | dxd facets J, O; bec facet B (failure 1); ledger H11, N07 | The record shows conventions held by their owner that served the weaker party without outside force; or the post binds the organisation to anyone outside it | Who governs current LLM tool conventions in practice (vendor terms, enterprise admin controls) |
| M2 | Industry standards where existing ones are insufficient; learnings shared "industrywide" (P6, P20) | **Self-regulation by the guild.** The Stationers regulated the trade they monopolised; standards bodies bind no implementer | bec facet B; dxd T §10 (RFC 8890; co-determination binds through arbitration) | Industry-set standards in the literacy era protected readers without a public authority behind them | The current AI standards landscape (who writes, who is bound, who is consulted) |
| M3 | Chain-of-thought transparency "non-negotiable" but "not sufficient or dependable" (P9) | **Disclosure as the safeguard.** The second of four stages: read the text, certify the reading, do not check understanding | v4 §3, §4.3; ledger H18, H22, H24; facet G C3, C6(a) | P9's reader is shown to be able to use the chain of thought (the safety literature already says monitoring is fragile) | Who is meant to read chain of thought in deployed LLM tools, and whether any study tests that reader |
| M4 | "Observe everything": every meaningful action leaves "tamper-proof human readable evidence" (P15) | **Two failures at once.** (a) *The record over the voice*: one party keeps the record that binds the other. (b) *Scriptio continua for the auditor*: a whole-volume record with no marked points of commitment, so the reader must find the decisions, as the reader of unspaced script had to find the words | ledger H07, H22; facet G C4 row 1 (alert review, transcript audit); the Spaces essay's decision-space marking (private; cite through the author) | Evidence that people reconstruct outcomes well from complete agent logs; or that the logs mark commitments | Studies of agent-log review and audit trails in LLM tools; how current tools present traces |
| M5 | Model diversity; independent auditability; no model controls both behaviour and evidence (P14, P18) | **Checks among the owner's agents, not for the bound party.** The notary's duty ran to both parties and to the weaker; the second interpreter could be either side's | ledger H10, N07; facet G C2, C6 | Independence in the post is shown to run to the people acted on | Whether any LLM tool gives a user or counterparty an independent check |
| M6 | Controls outside the model; harness and action space separated (P11, P12) | **The correction, held by the wrong party.** The same kind of move as spacing (work moved from person to artefact), declared to the deployer only | dxd T §6; facet G C6(b), C7 ("Complication") | The envelope is declared to the people the system acts on | — (concede in the text) |
| M7 | Verifiability: continuous testing of the whole system (P16) | **Testing the system, never the person's understanding.** No equivalent of the probate registrar's check or Spain's art. 193 | ledger H23, D06; Microsoft's own Standard T1.3 asks it (E14) | The post or Microsoft's practice tests whether people can interpret outputs in realistic conditions | Microsoft's evidence, if any, against its own T1.3 and A5.4 |
| M8 | An emergency brake for "An authorized person" (P19) | **The gate held by the few.** Power over the outcome given to a designated literate class (registrar, clergy); the bound party has no refusal | ledger H01, H20, D02; facet G C4 row 2, C6(c); E15 | The brake is held by, or answers to, the people acted on | How brakes and approvals work in current tools (permission prompts; approval rates) |
| M9 | Timely disclosure "to those affected" after failure (P20) | **Notice without standing.** The Requerimiento's testimony; disclosure after the fact that proves notice was given | ledger H18, K12, O07; facet G C6(e) | Disclosure in the post carries a remedy or a voice | What incident disclosure to users means in current AI policy (AI Act art. 73) |
| M10 | "Trust the model the least" (P21) | **The burden placed on the reader.** Distrust becomes the user's duty (Copilot's "always review and verify") as reading the contract became the signer's | ledger H19, E14; v4 §4.2 | The post or the product assigns the verifying work to the operator | — |
| M11 | Silence on building anyone's capacity; skilling programmes beside the product | **The competence withheld, then oversold.** Literacy campaigns promised returns and blamed the learner; scaffolds served their sponsors | ledger H04, H13, H25, N17, E16; v4 §4.4 | Microsoft or the post builds capacity inside the system, owed and fading | Current AI-skilling claims and evidence of effect |

## 2. What would sink the thesis

The paper fails if (a) most moves pair with a correction, not a failure; (b) the pairings rest on resemblance and no
shared property (each row must name the property, as Table 1 of v3 does); or (c) the historical failures were not
failures by the internal standards. Facet G's cautions (C8–C10) are the first test of (a).

## 3. Research to run, in order

1. **Read the post's present-day setting** (M1, M4, M7, M8, M10): how current LLM tools present traces, approvals and
   verification duties to users and to enterprise admins. Start from facet G's B4 cards and Microsoft's documents (V1).
2. **The print stage at scale** (M1, M2, M11): licensing and the Stationers as censor; reading mandates and church
   examinations; mass literacy campaigns. Start from bec facet B, ledger H11–H13, and dxd facets C and O.
3. **The scribal stage, read first-hand** (M4, M6): Saenger p. 11 (the elite and the costly script), the custody of
   the page (facet O), and the work spacing moved to the page (facets A, D).
4. **Audit and log review** (M4): studies of reviewing agent transcripts and audit trails (facet G C4: Kutasov,
   Grunde-McLaughlin, CERT).
5. **Standards and self-regulation** (M2): who writes AI standards and whom they bind.

Each step ends with cards for every source relied on and a pass of `collect.py` and the arm's checks. By the author's
standing rule the drafter reads and writes the prose; agents may search and card, and every card is verified before
it enters a draft.
