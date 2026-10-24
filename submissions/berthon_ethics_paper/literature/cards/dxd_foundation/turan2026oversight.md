# Turan, E. (2026). Oversight has a capacity: Calibrating agent guards to a subjective, fatiguing human. *arXiv preprint* arXiv:2606.08919.

**Identifier:** arXiv:2606.08919 · **Read depth:** full_text (preprint v1, 8 Jun 2026, 12 pages; locators are PDF pages. I read everything, including the reference list; I did not open the author's code or data repository) · **Source-tier:** preprint, single independent author, not peer reviewed · **Evidence basis:** direct_read · **Design and sample:** a systems and measurement study. 125 hand-labelled coding-agent actions (labels: safe 42, approval 52, blocked 31; all by the author, p. 4); a guard that scores risk with deterministic rules and an LLM (Haiku, compared once with Sonnet); three LLM "reviewer personas" standing in for human annotators; and a simulation of a reviewer whose reliability falls linearly once an escalation count passes a capacity C. No human reviewers took part · **Parties modeled:** person–system. One human reviewer and one agent guard, with an adversary who floods the reviewer · **Facets:** G · **Read:** 2026-10-13

## What it argues

Turan says the standard safety pattern for agents, a human approval gate, treats two things as given that are false: that "risky" has one correct label, and that the reviewer is "a perfect, infinitely-available oracle" (abstract, p. 1). He makes three claims.

First, the label is contestable. Three LLM personas (cautious, pragmatic, strict-compliance) labelling the 125 actions reach Fleiss' κ = 0.52; the pairwise Cohen's κ range from 0.42 to 0.71, and the pragmatic persona calls 87 actions safe against the cautious persona's 45 (p. 5). The author's own gold labels are a single judge's, "in deliberate tension" with that floor (p. 4).

Second, a guard framed as selective classification under an assumed 50:1 cost for a missed catastrophe against a false alarm cannot safely auto-decide on hard inputs. Reaching 0% missed danger needs a false-alarm rate near 100%, and the area under the risk-coverage curve is 0.374 ± 0.002 across three seeds for Haiku (pp. 5, 7).

Third, once the reviewer is modelled as fatiguing, realised danger is U-shaped in the escalation rate. The reviewer model is r(ℓ) = max(r_min, 1 − 0.02 · max(0, ℓ − C)), with r_min = 0.2 (p. 5), so fatigue is assumed to start at capacity C. Table 2 (p. 6) gives, for C = 10, 25 and 50, an optimal escalation rate of 64%, 64% and 72%, and a share of danger getting through of 56%, 42% and 22% at the optimum against 69%, 57% and 39% at full escalation. A flooding attack that buries one malicious action in k benign ones reaches an attack success of about 80% for a policy that escalates 88% of routine actions, and 40% at 50 filler actions; a "load-aware" policy escalating 26% holds at 0% until about 100 filler actions (p. 7).

Turan is plain about status: "The inverted-U and the flooding attack are modeling results that motivate a human study" (abstract, p. 1), and "the inverted-U below is a direct consequence of the assumed monotonically-fatiguing reviewer ... not an empirical finding about real people" (p. 6). He claims no new mechanism: fatigue-aware deferral, capacity-constrained deferral and reviewer-flooding attacks are "prior art" (pp. 1-2).

## Relation to the argument

Supports premise P12 in a narrow way: the reasoning that more escalation can lower safety, and the framing of attention as a budget, fit the argument that the post's P15 and P19 assign people work they perform badly. It is not evidence for P12. The fatigue curve is assumed, so the paper cannot show that people fail at it. Facet G is right to say "do not cite as human evidence," and this reading confirms it.

Two features are useful for the paper's design argument. The paper's remedy is to escalate less, so the guard keeps more of the work, which is the artefact-side direction the argument map favours (P8); it does not give the person a better reading task. And the flooding attack names a concrete way the post's "observe everything" (P15) could be turned against its reader: a long benign stream degrades the one dangerous review.

[Not from Turan, whose text and references do not cite Parasuraman and Manzey; the claim is unverified.] Against the model, Parasuraman and Manzey report that fatigued operators in one study were more careful with a decision aid than alert ones (Parasuraman and Manzey, p. 404). A monotone-decay model is one of two plausible shapes.

Facet check: facet G calls it "a model of a fatiguing reviewer." True, and the paper also reports a measured disagreement result (κ = 0.52), though from LLM personas, not people (pp. 5, 9). Facet G's other statement, that the paper calls the results modelling results, holds in the body (pp. 1, 6, 9).

## In conversation with

- `tariq2025alert`: cited as reference 15 for fatigue and flooding attacks on reviewers in security operations (pp. 1-2, 7).
- `anthropic2026how`: not cited by Turan.
- `green2022flaws`, `mitchell2026agents`, `yu2026habituation`: none cited.
- Leads, not in the bib: Zhang et al. 2026, "Fatigue-Aware Learning to Defer via Constrained Optimisation" (arXiv:2604.00904), the source of the endogenous-reviewer idea, which Turan credits "not ours" (p. 3); Alves et al. 2024, cost-sensitive learning to defer under workload constraints (TMLR; arXiv:2403.06906); Wang, Li and Tian 2026, "Reframing LLM agent security as an agent-human interaction problem" (arXiv:2605.24309); the European Data Protection Supervisor's 2025 TechDispatch on human oversight of automated decision-making (his ref. 12).

## Caution

Small, curated, single-domain (coding-agent actions) and single-author; one dataset underlies every result, which the paper itself calls "five views of one measurement instrument" (p. 8). The 50:1 cost ratio, the linear fatigue slope (0.02), the floor (0.2) and the capacities (10, 25, 50) are chosen, not fitted. The "reviewers" are LLM personas. The optimistic reviewer, who starts at perfect reliability, makes absolute danger rates lower bounds (p. 8). Do not cite the inverted-U or the flooding numbers as findings about people. Preprint v1; the repository may have moved on.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v1 PDF (12 pp.; title, author, 8 Jun 2026 match), whole text and page by page. I checked all 15 quotations and their PDF-page locators, and the numbers: 125 actions (42/52/31), Fleiss' kappa 0.52, pairwise kappa 0.42/0.47/0.71, 87 against 45, AURC 0.374 +/- 0.002 (Sonnet 0.351 against Haiku 0.373), 50:1, slope 0.02, r_min 0.2, Table 2 (64/64/72; 56/42/22; 69/57/39), the flooding figures (about 80%, 88%, 40% at 50 filler, 26%, 0% until about 100) and the FALCON/DeCCaF/ref. 15 relations.

**Findings:** Quotations, numbers and locators are right. One correction: the paragraph "Against the model, Parasuraman and Manzey report ... (p. 404)" is not from Turan; his text and reference list do not cite them. I marked it in the card as not from this source and unverified. The code and data repository was not opened, as the card says.
