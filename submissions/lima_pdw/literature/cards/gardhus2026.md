# Gårdhus, T., Vitsakis, N., Frederiksen, F. L., Rogers, A., & Carlsen, H. B. (2026). AInterviewer: A platform for designing and conducting AI-led qualitative interviews. In *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)* (pp. 119–127). Association for Computational Linguistics.

**Identifier:** 10.18653/v1/2026.acl-demo.12  ·  **Read depth:** abstract_only  ·  **Source read:** ACL Anthology record, verified 2026-08-18 (author list and order, pages 119–127, anthology ID 2026.acl-demo.12); abstract read from the anthology landing page
**Source-tier:** chapter
**Evidence basis:** publisher_summary
**Cluster:** qualitative-method

## What it argues

A multi-agent platform for AI-led qualitative interviews, built to fix what its authors identify as the two standing problems with existing systems: reliance on proprietary models, which compromises reproducibility and data security, and reliance on the LLM for every interview task, which surrenders control over question wording and order. Their design separates controlled question administration from generative probing and supports locally hosted models, covering guide design, pilot testing, distribution and collection monitoring.

## Relation to the argument

The most useful card in this sub-cluster for *defending the instrument's engineering* rather than its output. Their two named risks are exactly the two an IRB or a reviewer will raise about `AGENT.md`: the model is proprietary and varies by whichever assistant the participant happens to run it in, and the agent controls its own question wording. The protocol's mitigations — a versioned protocol file, `PROTOCOL_CHANGES.md`, recording the model in each response's front matter — line up with their standardisation argument and should be presented in those terms.

## Caution

A system-demonstration paper: it describes a tool, reports no interview data, and validates nothing. It is also very recent (ACL 2026) and unlikely to be known to an OS/OT reviewer. Note that this study's design does the opposite of what the platform recommends — participants run the agent in their own editor on whichever model they have — which makes the paper as much an indictment as a support. Cite it where the limitation is discussed.
