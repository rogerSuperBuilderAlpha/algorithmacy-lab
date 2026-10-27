# Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

**Identifier:** doi:10.6028/NIST.SP.800-207 · **Read depth:** partial (final publication, August 2020, 59 pages; I cite the printed page numbers, which are the PDF page minus 9, since the front matter runs in roman numerals. I read the abstract, sections 1 to 3, section 4 (4.1-4.5), section 5 in full, 7.1 and 7.3.4-7.3.7, and Appendix B.4; I skimmed sections 6, 7.3.1-7.3.3, the rest of Appendix B and the reference list, so I cannot vouch for those) · **Source-tier:** government technical report (federal guidance, no peer review) · **Evidence basis:** direct_read · **Design and sample:** none. An architecture definition with deployment models and use cases; no experiment or measurement · **Parties modeled:** other. An enterprise (the party that defines policy), "subjects" that request resources (users, applications and other non-human entities, p. 1), and administrators who configure the policy components. Customers and the public sit outside the model (p. 7) · **Facets:** G · **Read:** 2026-10-13

## What it argues

NIST defines zero trust as "a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions in information systems and services in the face of a network viewed as compromised" (p. 4). Zero-trust models "assume that an attacker is present in the environment" and treat the enterprise's own environment as "no different—or no more trustworthy—than any nonenterprise-owned environment" (p. 1). Every request passes a policy decision point and a policy enforcement point, split in the logical architecture into a policy engine, a policy administrator and a policy enforcement point (Figs. 1-2, pp. 5, 9). A "trust algorithm" weighs the request, subject and asset records and threat intelligence; it can be criteria- or score-based, singular or contextual (pp. 17-20).

The seven tenets (pp. 6-7) include per-session access with "the least privileges needed" (tenet 3); dynamic policy that may use behavioural attributes (4); "dynamic and strictly enforced" authentication and authorization before access (6); and (7) that the enterprise "collects as much information as possible about the current state of assets, network infrastructure and communications and uses it to improve its security posture." The tenets "apply to work done within an organization or in collaboration with one or more partner organizations and not to anonymous public or consumer-facing business processes" (p. 7), and for a public-facing service "the enterprise is constrained as to what internal cybersecurity polices can be enforced" (p. 27).

Section 5 lists threats to ZTA itself. The policy engine and administrator are the key components, so a rogue administrator or a compromised policy administrator subverts everything; configuration changes "must be logged and subject to audit" (p. 28). A malicious insider or a thief holding valid credentials "may still be able to access resources for which the account has been granted access," and a contextual trust algorithm is expected to catch out-of-pattern use (p. 29; example on p. 20). Software agents that administer the system raise an "open issue" of how they authenticate; "the biggest risk" is false positives and false negatives, and an attacker may "trick the agent" (pp. 30-31). Migration is "a journey" (p. 1), and a first deployment may run in reporting-only mode (p. 40). Appendix B.4.6 admits that "there has not been a rigorous examination of how end users act" in a ZTA, and points to security fatigue as the nearest evidence (p. 49).

## Relation to the argument

NIST is the security canon behind the post's controls-outside-the-model move (the argument map's P11). The post's "assume the model is compromised" posture (its P19) matches the document's starting premise, and "observe everything" (its P15) matches tenet 7. The match is partial, as facet G records: in NIST, the information collected feeds policy decisions made by software, and a person appears only as the administrator who configures and audits the policy components (pp. 28, 30). The "human-readable evidence" the post asks for has no counterpart. NIST's enforcement is the "moves work from person to artefact" mechanism the argument map warns will not by itself separate the paper from the post.

For ruling D5 (the "enterprise, not user" reading), the scoping on pp. 7 and 27 is the clearest textual support in this batch: the tenets stop at the enterprise boundary, and people outside it are users of a public service, not parties whose protection the architecture addresses. Section 5.7 also bears on the post: NIST already treats AI software agents as non-person entities that can be induced to act for an attacker (p. 31).

Facet check: facet G's quotations of tenets 3, 6 and 7 and its description of the decision and enforcement points hold against the full text. Its note that tenet 7 feeds "policy, not a human reader" also holds, with two additions from sections it did not read: administrator audit of the policy components (p. 28), and §7.3.7's line that "the subjects and stakeholders of the resources and processes involved should also provide feedback" (p. 41), which places enterprise users in a feedback role.

## In conversation with

- `anderson1972computer` and `saltzer1975protection`: the reference-monitor and least-privilege ideas that facet G ties to the post. NIST's text and reference list name neither; it traces the term "zero trust" instead to DISA's "black core," the Jericho Forum's deperimeterization and Kindervag (p. 2).
- `parasuraman2010complacency`, `tariq2025alert`: unrelated by citation, but the fatigue gap NIST names in B.4.6 (p. 49) is the human side these two study.
- Leads, not in the bib: Kindervag's coining of "zero trust" (p. 2); NIST SP 800-63 on digital identity (cited for authentication assurance, pp. 18-20); the NIST Risk Management Framework SP 800-37 (§6.1, p. 32).

## Caution

A federal architecture guide for enterprise networks and resource access, not a study and not about AI. Its word "insider" means an authorised account misused, and it never mentions language models. Sections 6, 7.3.1-7.3.3 and most of Appendix B I only skimmed. I did not check for later NIST revisions.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the NIST PDF (60 PDF pages; printed page = PDF page minus 9, confirmed). Checked 20 quotations for exact wording and printed-page locator, the seven-tenet citations, the scope sentence on p. 7, the p. 27 and p. 31 claims, and the p. 2 provenance of the term "zero trust". Did not check the reference list or sections the card says it skimmed.

**Findings:** One fix: Read depth said "full_text" while the card itself says sections 6, 7.3.1-7.3.3 and most of Appendix B were only skimmed; changed to "partial" and kept the list of unread parts. All quotations, page locators and attributed claims match the text. No other issues found.
