# Abstract: *ISJ*, "AI and the Future of Work"

[DRAFTED by Claude, 26 Oct 2026. For the author's read-aloud. Due 31 Jan 2027 (indexed date; verify).]

**Title:** Designing the Third Party: Provenance, Dual Address and Change Notice in Systems That Judge Two People

## Abstract
AI at work increasingly stands between two people. A booking platform ranks a hotel on its guests' reviews, a marketplace scores a seller on buyers' feedback, and an AI tool can draft the appraisal a manager gives an employee. In each case the system evaluates a relation and binds both parties to its verdict. IS design research has answered algorithmic opacity with explanation, transparency and contestability, and each answer models a single decision subject facing a system. This paper argues that systems which judge two people need different design properties. The parties' problem is not that the model is hidden; machine-learning opacity is intrinsic. Their problem is that they cannot tell whose input moved a verdict, cannot tell how a message to the other party will be scored, and cannot tell when the rule has changed. We derive three design properties from these problems. Provenance cues show which party's input moved a verdict. Dual address shows a sender what the evaluator will register and what the counterpart will see. Change notice logs rule updates and announces them to both parties. We state each property as a testable design proposition. We ground the propositions in published studies of review filters and contestation, and specify outcome measures for each: correct attribution of responsibility, shared interpretation of messages, and detection of rule change. The contribution is a design theory for the human–machine–institution interface in which the machine is a third party, not a tool or a channel.

**Keywords:** design theory; algorithmic management; contestability; accountability; future of work

## Citation check
| Claim | Source card | Depth |
|---|---|---|
| Opacity intrinsic to ML | `lima_pdw/literature/cards/burrell2016.md` | abstract |
| Disclosure is not traceability | `dxd_foundation/literature/library/kroll2021outlining.md` (p. 4) | full text |
| Contestability as a system feature | `dxd_foundation/literature/library/alfrink2023contestable.md` (p. 614) | full text |
| Users write for the filter once told of it | `dxd_foundation/literature/library/eslami2019user.md` (pp. 11–12) | full text |
| Hotel rankings; seller scores | `lima_pdw/literature/cards/orlikowskiscott2023.md` (p. 3); `lima_pdw/literature/cards/curchod2020.md` | full text |
