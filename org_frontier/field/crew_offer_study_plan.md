# Crew-offer decision: proposed field study

## Status and question

This is a study plan, not a field result or a pre-registration. No Roster workflow, ranking feature, participant account, or decision log has been verified. The plan must be narrowed to an accessible site and committed as a pre-registration before evidence is collected or a model is computed.

For one crew offer on one production, does the software only carry an offer between a producer and a crew member, or does it determine which crew member can receive that offer? If it determines the offer, does that change what either person can explain or contest?

The unit is one recurring act: a producer identifies a crew member, an offer is made, and the crew member accepts or declines. The study does not treat the whole hiring process as one decision. A before/after comparison is possible only if records exist for both versions of the same act. Otherwise, compare current paths within one workflow, if both a direct offer and a software-selected offer are available.

## Separate outcomes

| Question | Evidence | Possible result |
| --- | --- | --- |
| Structure: who determines the offer? | Product rules, event logs, observed cases, and accounts from both sides | An exact-Φ verdict for each defensible Boolean encoding; no verdict about the organization without evidence for the rules |
| Understanding: can people explain the decision? | Ask each person why a named crew member did or did not receive an offer; compare the answer with the recorded decision path | Correct, partly correct, or unsupported explanation; record disagreement between the parties |
| Control: can people change the outcome or rule? | Demonstrated direct offer, correction, override, appeal, and rule-change paths; logs of attempted and completed actions | Available and effective paths, available but ineffective paths, or no path |

The structural result does not stand in for understanding or control. A triadic model may coexist with clear reasons and effective appeals. A dyadic model may coexist with opaque human choices. Both are informative outcomes.

## Evidence needed before encoding

1. Confirm that the site has a recurring crew-offer workflow and obtain permission to study it. Identify whether software ranks, filters, recommends, assigns, or only sends messages. Do not infer a feature from a product description.
2. Gather the written rules and interface states for one offer path. Use de-identified event records to trace who was eligible, who was shown, who chose, who was offered, and who accepted or declined. Record missing events.
3. Interview the producer and crew member about the same decision. Where possible, interview the person who sets or operates the software rule. Ask each person what they saw, what they believed determined the offer, and what they could change.
4. Record a direct-contact or override path if one exists. A path is effective only if it can change a real offer, not merely submit a request.

Protect participant identities and job details in any public artifact. Obtain the needed site and research permissions before collecting interviews or private logs.

## Encoding plan

The first candidate nodes are producer (P), system (S), and crew member (C). A node is active when it takes a decision-relevant action in the bounded offer. The exact binary states and next-state rules must come from field evidence; they are not specified here. In particular, a ranking shown to a producer is not a binding assignment if the producer can freely choose anyone.

Two coders independently map the same evidence to: (a) who reads whose state, (b) who can commit or block the offer, (c) whether the specific crew member is replaceable at that step, and (d) at least one plausible alternative rule for every uncertain edge. Record agreement before reconciliation, the disputed evidence, and both verdicts if defensible encodings disagree. Run the field protocol's control forms before any candidate model. Report whole-system Φ and major-complex membership, then rerun the rules on which the verdict depends.

## Predictions to fix before fieldwork

The pre-registration will state a prediction only after the actual offer path is confirmed. The working propositions are:

- If software only carries a producer-selected offer, its model may factor as a relay. The exact verdict remains to be computed.
- If software makes a binding selection using both parties' states, a triadic model is plausible. Substitution, human override, and alternative encodings may change that verdict.
- A structural change alone makes no prediction that either person's understanding or control falls. Those outcomes are measured separately.

Evidence that the producer can offer any eligible crew member directly would weaken a claim that software is necessary to this act. A result in which coders cannot agree on the rules, or plausible rules yield opposite verdicts, is reported as model uncertainty rather than resolved in favor of the preferred prediction.

## What this study could establish

The strongest possible result is a documented decision path, independently encoded rules, exact and sensitivity-tested model verdicts, and separate evidence about what the people understood and could change. It would not show that Φ measures fairness, competence, or power. A mismatch between the structural verdict and the human outcomes is a result, not a failure to report.

The next step is to confirm a site and one decision path, then turn this plan into the field protocol's pre-registration, coding scheme, interview guide, and ethics materials before data collection.
