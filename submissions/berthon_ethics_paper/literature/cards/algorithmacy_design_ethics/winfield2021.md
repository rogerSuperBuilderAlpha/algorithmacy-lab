# Winfield, A. F. T., Booth, S., Dennis, L. A., Egawa, T., Hastie, H., Jacobs, N., Muttram, R. I., Olszewska, J. I., Rajabiyazdi, F., Theodorou, A., Underwood, M. A., Wortham, R. H., & Watson, E. (2021). IEEE P7001: A proposed standard on transparency. *Frontiers in Robotics and AI*, 8, 665729.

**Identifier:** doi:10.3389/frobt.2021.665729 · **Read depth:** full_text (open-access HTML, Frontiers; sections cited by number) · **Source-tier:** peer-reviewed journal (Frontiers in Robotics and AI); an account of a draft standard by its working-group members · **Evidence basis:** direct_read · **Parties modeled:** human–technology, with five stakeholder groups · **Relation last checked:** 2026-09-18

## What it argues

P7001 (published as IEEE 7001-2021, which is paywalled and not opened for this card) sets out "measurable, testable levels of transparency, so that autonomous systems can be objectively assessed and levels of compliance determined" (§3). Transparency is "the transfer of information from an autonomous system or its designers to a stakeholder, which is honest, contains information relevant to the causes of some action, decision or behavior and is presented at a level of abstraction and in a form meaningful to the stakeholder"; explainability is the subset "accessible to non-expert stakeholders" (§3.1). Five stakeholder groups get separate 0–5 scales — end users, the wider public and bystanders, safety certifiers, incident investigators, lawyers and expert witnesses — and "stakeholders are beneficiaries of the standard, as distinct from users of the standard: designers, developers, builders and operators" (§3.2). The end-user levels (Table 1) run from a user manual (1) and an interactive visualisation (2) to a "why did you just do that?" function (3) and a "what would you do if ... ?" function (4); the investigator levels run from a recorder to logs of high-level decisions "and the reasons" (4) with visualisation tools (5). A system is compliant at level 1 in any one group, so a bare compliance claim "would be misleading" (§3.4); the useful outputs are a System Transparency Assessment and a System Transparency Specification, illustrated on a fictional robot teddy and a hospital vacuum robot. The limitations section is candid: deep networks challenge explainability "at least"; there was disagreement over whether contextualised explanation is desirable "since it necessarily creates a system-generated interpretation of what is happening, which could introduce biases"; and, citing Kaur et al. (2020), "the provision of explainability mechanisms led to over-confidence in a model," which "may also contribute to automation bias" (§5.2). Transparency is noted as being "in tension with ... security ... and privacy."

## Relation to the argument

This is the standards route into the four affordances, and two of them appear as compliance levels: level 4's "what would you do if" is Counterfactual/Branching Exploration made normative, and level 3's "why did you just do that" is a per-decision seam. That gives the affordances an external, testable anchor. Two things cut the other way. The over-confidence caveat cuts against any assumption that disclosure calibrates reliance, which is the assumption Cognitive Forcing Functions exist to correct, so the standard and that affordance need each other. And the stakeholder taxonomy shows what standards inherit from VSD: users and bystanders are the human categories, the operator is a user of the standard rather than a party owed anything, and nothing in the levels requires disclosure of the system's objective — transparency here is about causes of behaviour, not about whom the behaviour serves. The counterpart in a two-sided mediation has no group of her own; she would be a bystander, which is the inversion RQ5 asks about, produced by a standard rather than by VSD. The OECD gloss the authors quote — transparency "as the means of understanding and challenging the outcomes" — is the only mention of contest, and P7001 does not build on it.

## Caution

The paper describes a draft; the authors are the working group, the worked examples are fictional, and no system has been assessed. Several higher levels "require techniques that have not yet been developed," so the scale is partly aspirational. The volume-8 article number is Frontiers' identifier, not a page range. IEEE 7001-2021 itself, and the related IEEE 7000-2021 process standard, were not accessed; this card covers the standard only as its authors present it.

---

## S2 adversarial verification (2026-09-18)

**Verdict:** confirmed

**What I checked:** Re-fetched the Frontiers HTML and searched all 18 quoted strings.

**Findings:** All verbatim, including the transparency definition, the stakeholder/user distinction and the Kaur et al. over-confidence caveat. No issues found.
