# Bansal, G., Nushi, B., Kamar, E., Weld, D. S., Lasecki, W. S., & Horvitz, E. (2019). Updates in human-AI teams: Understanding and addressing the performance/compatibility tradeoff. *Proceedings of the AAAI Conference on Artificial Intelligence, 33*(1), 2429–2437. https://doi.org/10.1609/aaai.v33i01.33012429

**Identifier:** doi:10.1609/aaai.v33i01.33012429 · **Read depth:** full_text (the AAAI-19 proceedings PDF from the publisher's site, 9 pages, proceedings pagination 2429–2437; I read the whole text and saw the figures only as extracted text, so Figures 3–5 are known to me through their captions and the prose) · **Source-tier:** proceedings (peer-reviewed conference paper) · **Evidence basis:** direct_read · **Design and sample:** (1) a crowd experiment on an abstract game ("CAJA"): 25 Mechanical Turk workers per condition, 100 objects per run in the mental-model studies and 150 cycles in the update study; (2) classifier simulations on three real high-stakes datasets (recidivism, in-hospital mortality, credit risk), with no human participants in that part · **Parties modeled:** person–system (one person and one AI recommender, with the AI changing over time) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Bansal and colleagues study "AI-advised human decision making": the AI recommends, the person decides, and over repeated tasks the person learns when to trust it. Their claim in the abstract is that "updates that increase AI performance may actually hurt team performance" (p. 2429), because an update can introduce errors in places where the person had learned to trust the system. They define a local compatibility condition (an update keeps the AI right wherever the person trusts it and it was right before), a global one, and a score: the share of cases the old model got right that the new model still gets right (pp. 2431–2432).

The people-facing experiment uses CAJA, a game in which workers label boxes as defective. The AI ("Marvin") starts 80% accurate. The payoff is $0.04 for accepting a right recommendation and −$0.16 for accepting a wrong one; a "compute" option costs the same as perfect solving, so only learning where Marvin errs beats a fixed strategy (Table 1, p. 2433). Labels are random, so no one can become a task expert; workers can only learn the AI's error pattern (p. 2432). The reported findings are:

- Team performance falls as the number of human-visible features rises and as errors become more stochastic; workers whose self-reported mental model of Marvin's errors was correct scored highest, then partial, with wrong and unsure lowest (Figure 3, p. 2434).
- In the update study the AI becomes 5 points more accurate (80% to 85%) at cycle 75. Where the update leaves the error boundary unchanged or adds only compatible changes, performance holds or rises. Where it introduces new errors, team performance drops below the no-update line, "despite improvements in AI accuracy" (Figure 4 and its caption, p. 2434). The text gives no numeric scores and does not state the group sizes for this study; the finding is read from the figure.
- Standard retraining is not compatible. A model trained on 200 examples and then on 5,000 improves its area under the ROC curve, yet compatibility can be low: for logistic regression on the mortality task the score is 0.40, "60% of the instances where h1 was correct are now violated" (Table 2, p. 2434; the sentence quoted is on p. 2435).
- A retraining loss that adds a penalty for new errors ("dissonance") gives a tunable performance/compatibility tradeoff on all three datasets (Figure 5, p. 2435).

The authors admit that the importance of mental modelling "may vary" with how easily a person can check a recommendation, and that "an important future direction is to develop computational models of how people create and update mental models" (pp. 2435–2436).

## Relation to the argument

**Premise P7 and the map's second exposure.** The map says external-representation research assumes a regularity that holds and a designer who knows the constraints, and that "an adaptive, interested mediator offers neither." Bansal shows what happens when the regularity breaks: the person's learned model of when to trust the system becomes wrong exactly where the system changed. The cost is the person's work of re-learning the mediator, which is the work P7 says no convention yet carries. The paper also turns the problem into a design obligation on the mediator's side, to keep updates compatible, which is a rule that sits in the mediator and not an aid the person reads. That fits the author's lean toward rules that remove work from the person (P8) over aids that add to it (P9).

**Ruling D7.** Part 1 of the DXD series (line 66) says an adaptive intermediary disrupts the rapid, unequivocal feedback that learning by acting needs. This is the controlled source for that statement, in a dyad and in an abstract game: the experiment has the feedback loop (reward after every decision) and shows that changing the system breaks the learning.

**What it cuts.** The AI is neutral and its accuracy is set by the experimenters. No party has an interest at odds with the user, and there is no counterpart. So it says nothing about a mediator whose owner can change the rule to its own advantage; there the update might be the point.

**Facet check:** the facet's quotations are correct but it reads the three high-stakes tasks as "crowd participants" ("simulated high-stakes tasks with crowd participants"). The crowd participants played only the abstract CAJA game; the recidivism, mortality and credit-risk work used classifiers alone, with no people. The facet's "participant numbers not in the abstract" is now answered: 25 workers per condition in the mental-model studies (with the bottom quartile of scorers removed as likely spammers, p. 2433); the group sizes for the update study are not stated.

## In conversation with

- No work in `references.bib` is cited by this paper (I checked the reference list against the bib by surname and year). Its mental-model frame comes from Norman (1988) and Kulesza et al. (2012).
- Later work in the bib that studies a person's picture of the AI's errors: `cabrera2023improving`, where a short description of the AI's behaviour is the intervention; I did not read it this session beyond what the facet reports.
- Not in the bib, as leads: Norman (1988), *The Psychology of Everyday Things*; Kulesza et al. (2012) on mental models of intelligent agents; Hoff & Bashir (2015) on trust in automation; Wang et al. (2016) on combining physicians and expert systems.

## Caution

Abstract game with randomised labels so that no one can learn the task, MTurk workers, one 5-point update, and group sizes unreported for the key figure. The "high-stakes" part is classifier simulation with no human test. The compatibility score is defined on the old model's correct cases only, so it does not capture new correct answers or the person's confidence. The result is on AI-advised decisions, not on any system whose owner updates it for its own ends.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the AAAI-19 proceedings PDF (9 pp., pdf page 1 = p. 2429); extracted text page by page. Checked 8 quotations (abstract; Figure 4 caption; 60% sentence; 'may vary'; future-direction sentence) and about 25 numbers (25 MTurk workers per condition, bottom-quartile filter, 100 objects, 150 cycles with update at cycle 75, 80% to 85%, $0.04 and -$0.16, 200 vs 5,000 examples, mortality logistic-regression score 0.40), and Norman 1988, Kulesza et al. 2012, Hoff and Bashir 2015, Wang et al. 2016 in the reference list.

**Findings:** One locator error: the '60% of the instances where h1 was correct are now violated' sentence is on p. 2435, not p. 2434 (Table 2 itself is on p. 2434). Corrected. All other quotations, numbers and the facet-check point (crowd participants only played CAJA; the high-stakes datasets used classifiers only) are accurate.
