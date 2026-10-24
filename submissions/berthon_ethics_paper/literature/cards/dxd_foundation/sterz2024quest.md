# Sterz, S., Baum, K., Biewer, S., Hermanns, H., Lauber-Rönsberg, A., Meinel, P., & Langer, M. (2024). On the quest for effectiveness in human oversight: Interdisciplinary perspectives. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (FAccT '24). https://doi.org/10.1145/3630106.3659051

**Identifier:** doi:10.1145/3630106.3659051 · arXiv:2404.04059 · **Read depth:** full_text (arXiv v2, 7 May 2024, 13 pages in the ACM layout; locators are PDF pages, because the arXiv copy carries no proceedings page numbers. I read the whole text including the reference list's first pages; I skimmed the rest of the references. This is the arXiv version of the FAccT paper, not the proceedings PDF) · **Source-tier:** proceedings paper (peer-reviewed conference), conceptual · **Evidence basis:** direct_read · **Design and sample:** none. A conceptual synthesis by a psychologist, lawyers, philosophers and computer scientists, with a table of facilitators and inhibitors and a reading of Article 14 of the EU AI Act · **Parties modeled:** person–system, with the deployer and provider as parties who enable the "oversight person"; users and stakeholders appear only inside the definition of fitting intentions (p. 5) · **Facets:** G · **Read:** 2026-10-13

## What it argues

The authors ask when human oversight is effective, taking "the central objective of oversight is risk mitigation" as the standard (p. 2). Oversight is effective, they propose, if and only if the oversight person has four things: causal power over the system and its effects, epistemic access to the relevant situation, self-control, and fitting intentions for the role. Their short form is "Effectiveness = Moral Responsibility + Fitting Intentions" (p. 2), since the first three conditions together amount to moral responsibility.

The definitions carry detail. Causal power fails if the person is "a mere observer" or has only "pseudo-options" such as a stop button that does not work (p. 4). Epistemic access needs enough knowledge of "what the system is doing, in which state it is," the risks, and what interventions would do; explainability measures can raise it (pp. 4-5). Self-control means being able to choose a path and follow through, which needs attention: if overseeing "a fleet of autonomous vehicles is so uneventful and dull that a normal person cannot help but let their mind wander off," oversight fails (p. 5). Fitting intentions means the person is moved by a role-appropriate aim: "they intend to mitigate any risks while taking other relevant factors, such as the interests of the system's users and other stakeholders, into consideration in a suitable way" (p. 5).

Table 1 sorts facilitators and inhibitors into technical design (for example intervention options and preselection of outputs to review), individual factors (training, exhaustion, motivation, automation bias) and environment (job design, role conflicts, accountability, time pressure) (p. 7). On automation bias they cite Parasuraman and Manzey for "learned carelessness" (p. 7). One environmental factor stands out: if the overseer is also the decision-maker, "a conflict arises" when mitigating risk costs the decision-maker something (p. 8).

Section 5 compares the definition to Article 14(4) of the EU AI Act. Requirements (d) and (e), override and a stop button, supply causal power; (a) and (c) supply epistemic access; "the criterion of fitting intentions ... has little direct equivalent in the legal text" (p. 9). They find the article's items of "strongly varying levels of abstraction" (p. 9) and point out it never mentions the system's inputs (p. 10). The authors name three limits: the definition is abstract, the mapping from factors to conditions needs empirical work, and it says whether oversight is effective, not whether something is oversight (p. 10).

## Relation to the argument

The four conditions give the project a checklist for the post's two human roles. The post's P19 holder of the brake has causal power by design; P15's reader of "human readable evidence" is meant to have epistemic access; the sources the project reads in facet G are about whether epistemic access and self-control hold. Sterz also says what is missing from the post: nothing in the post secures fitting intentions or deals with role conflict.

Two points matter for the rulings. First, D5 (the "enterprise, not user" reading) and the argument map's P10. Sterz's role-conflict case (the overseer who is also the beneficiary of approvals, p. 8) and "other conflicting interests" (p. 5) are the person-level version of the owner-versus-user conflict P10 assumes. The paper does not extend that to a platform owner. Second, the affected enter only inside "fitting intentions": the overseer should weigh the interests of users and stakeholders, but they have no role as parties. Sterz does not argue that the people the system acts on should hold any control.

Facet check: facet G says P19 supplies (a) and P15 is meant to supply (b), and that the literature is about whether (b) and (c) hold. That matches the paper. The facet does not mention (d), fitting intentions, or role conflict (p. 8), which bear most directly on D5.

## In conversation with

- `green2022flaws`: the paper's main source for criticism of oversight, from its survey of 41 policies and its call for institutional oversight (pp. 2-3).
- `bucinca2021trust`: cited for forcing people to think before seeing the system's output (p. 8; reference 11).
- `parasuraman2010complacency`: cited for automation bias and "learned carelessness" (p. 7).
- `eu2024regulation`: Article 14, the legal test case in Section 5 (pp. 8-10).
- `laux2024institutionalised`: cited (their ref. 49) for the idea that oversight should not be an end in itself and for conceptual work on what oversight is (pp. 2, 4). I did not check each use.
- `langer2024effective`: shares an author (Markus Langer) with the paper; I found no citation of it by title in the text or reference list.
- `santonidesio2018meaningful`: not cited; both lean on Fischer and Ravizza (Sterz fn. 4, p. 4).
- Leads, not in the bib: Fischer and Ravizza 1998 for guidance control; Enqvist 2023 on human oversight in the AI Act (their ref. 19); Mosier, Skitka, Burdick and Heers (1996) for the definition of automation bias, quoted on pp. 2 and 7 (their p. 205); Biewer et al. 2024 on "software doping analysis for human oversight."

## Caution

A conceptual proposal, in its authors' words "one among potentially numerous conceptualizations" (p. 4). It tests nothing on real overseers, and it predates the final adopted text of the AI Act (it uses the version approved by Parliament, with the Council still to adopt, fn. 9, p. 8). The arXiv v2 is not the proceedings page layout.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened arXiv v2 PDF (13 pages; locators are PDF pages as the card says); title, authors and venue match. Checked 14 quotations for exact wording and page (non-layout extraction), the Article 14(4) mapping, Table 1 factors, the 41-policy count for Green, Bucinca's forced-thinking suggestion (p. 8), fn. 9 (Council), and the reference-list leads (Enqvist, Biewer, Fischer and Ravizza, Mosier).

**Findings:** Two small fixes. (1) The guidance-control footnote (Fischer and Ravizza, ref. 26) is fn. 4 on p. 4, not p. 5. (2) The card called the automation-bias source 'Mosier and Skitka (1996)'; the reference is Mosier, Skitka, Burdick and Heers (1996), quoted from p. 205. All quotations match.
