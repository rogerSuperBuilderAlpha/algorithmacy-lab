# Jacovi, A., Marasović, A., Miller, T., & Goldberg, Y. (2021). Formalizing trust in artificial intelligence: Prerequisites, causes and goals of human trust in AI. *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)*, 624–635.

**Identifier:** doi:10.1145/3442188.3445923 · arXiv:2010.07487v3 (20 Jan 2021) · **Read depth:** full_text (arXiv v3, the camera-ready with the ACM header; page range 624–635 confirmed against the Crossref record for the DOI on 2026-09-18) · **Source-tier:** peer-reviewed, top FAccT venue; conceptual/formal paper, no empirical study · **Evidence basis:** direct_read · **Parties modeled:** human–technology, with one worked example that names two humans (loan officer and applicant) facing the same model with different risks · **Relation last checked:** 2026-09-18

## What it argues

Trust in AI is contractual, it requires vulnerability, and it is warranted only when caused by trustworthiness. The authors borrow the sociological minimum — A trusts B if A believes B will act in A's interest and accepts vulnerability to B — and rebuild it for a model: "If H (human) perceives that M (AI model) is trustworthy to contract C, and accepts vulnerability to M's actions, then H trusts M contractually to C" (§5). The contract is whatever behaviour is to be anticipated, from correctness on a sub-population to non-discrimination, and it must be explicit; the European guidelines and the documentation genre (model cards, datasheets, factsheets) are read as catalogues of contracts (Table 1). Trust is warranted when manipulating the model's real capability would change it, which yields an evaluation protocol: measure trust, handicap or improve the model, measure again (§8.2). Warranted trust has two causes: intrinsic (the observed reasoning matches the user's priors about good reasoning) and extrinsic (behaviour on trustworthy evaluations, by proxy, deployment data, or test sets). Explanation is "uniquely positioned" as a cause of intrinsic trust for lay users (Takeaway 6), and unwarranted trust is an ethical fault to be diagnosed and avoided (Takeaway 4). The paper insists that most XAI benchmarks cannot study trust at all, because a worker labelling short sentences bears no risk (§8.1).

## Relation to the argument

RQ4 on both axes, and the one source in this cluster that writes down two humans facing one model. The credit-scoring example (§2) gives the loan officer a risk (the applicant defaults) and the applicant a different risk (denial, or a higher rate "on a loan that they deserve"), and says trust manifests for the applicant "if they believe that the AI model will work in their interest." That is the essay's structural triad stated in one paragraph — two parties, one intermediary, two contracts — and then set aside: the formalism treats each as a separate dyad, and the applicant appears only "if they have a choice as to whether to use the AI model," which in practice they do not. The paper also draws the essay's objective-axis line, with a limit. It holds that "AI as an automation does not embody intent. Formally, the intent of the AI developer manifests in the capability of the model to maintain specific contracts," and it rules trust in the developer's incentives out of the model as "interpersonal trust by proxy," to be studied elsewhere (§9.2). So the framework can express that a mediator pursues an objective neither party set — as a contract the developer wrote and the parties did not — but it deliberately declines to model the developer as a party. The contract vocabulary is nonetheless the best available scaffold for stating what a coordinating party would need to anticipate about an intermediary that also serves someone else.

## Caution

No data; a formalization with worked examples. The authors restrict "user" to an individual and "AI" to automation the user anthropomorphizes, and they treat every interaction as a clean-slate transaction. The two-human example is illustrative and gets no further development. The page range 624–635 is Crossref-confirmed. Use it for the contract/warrant vocabulary and for the explicit exclusion of the developer's intent, not as evidence that trust behaves as described.


---

## S2 adversarial verification (2026-09-18)

**Verdict:** corrected

**What I checked:** Downloaded arXiv 2010.07487v3, extracted the text, and searched for every quotation; pulled the Crossref record for the DOI.

**Findings:** All quotations are verbatim, including the contractual-trust definition, the loan-officer/applicant sentences, and the §9.2 "does not embody intent" passage. "Takeaway 4" and "Takeaway 6" correspond to items (4) and (6) of the numbered "Takeaways" paragraph, with the wording the card gives. One correction: the page range 624–635 was labelled second-hand (from Miller 2023's reference list); Crossref confirms it, so the Identifier and Caution lines now say so.
