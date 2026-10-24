# Cabrera, Á. A., Perer, A., & Hong, J. I. (2023). Improving human-AI collaboration with descriptions of AI behavior. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), Article 136.

**Identifier:** doi:10.1145/3579612 · arXiv:2301.06937 · **Read depth:** full_text (arXiv v1 PDF, typeset with the CSCW Article 136 header and 136:1–136:21 page labels, which I cite; I did not compare it with the version of record; I read the whole text and the reference list) · **Source-tier:** proceedings article (journal-proceedings, CSCW) · **Evidence basis:** direct_read · **Design and sample:** 3 × 3 between-subjects online experiment on Amazon Mechanical Turk; three tasks (hotel-review deception, satellite-image classes, bird species) × three conditions (no AI, AI, AI plus behavior descriptions); 25 recruited per cell, 225 in all; a simulated ("wizard-of-oz") AI with fixed errors (136:6–136:9) · **Parties modeled:** person–system (a worker and an AI aid); no third party · **Facets:** H · **Read:** 2026-10-13

## What it argues

The authors propose "behavior descriptions": short statements of how an AI performs on subgroups of instances, such as "the model is 20% accurate for this type of instance" (136:7). They distinguish these from explanation, which says why an output arose; a description says what pattern of outputs to expect (136:2). They design them to be actionable, simple and significant (136:5).

In each task participants labelled 30 items. Twenty came from the whole data with 95% AI accuracy. Two groups of five came from subsets where the AI was right 40% and 20% of the time; only these ten items carried a description in the third condition. Participants were told the AI was 90% accurate, but its actual accuracy was 73.33% by construction; the authors say this applies equally to all conditions (136:8).

Results (136:10–136:13). In the reviews task behavior descriptions raised accuracy over no AI (F(2,64) = 9.18, p < 0.001; pairwise p < 0.001, 95% CI [0.06, 0.22]), while "the AI by itself did not significantly improve the accuracy." In the birds task the same pairwise gap was smaller (p = 0.048, CI [0.00, 0.16]) and the team beat both human and AI alone. In the satellite task there was no difference (F(2,67) = 0.63, p = 0.534); unaided humans were already near 90%. The reviews gain came with "no human-AI complementarity" because every condition stayed below the AI's own accuracy.

The mechanism is mixed. Participants corrected failures on the described subgroups in only one case (birds, group 2). The steadier effect was that they relied more on the AI on the ordinary items when failures were fenced off into described groups (136:11, 136:13–136:14). Trust, helpfulness and willingness to reuse the AI did not differ between the AI and AI-plus-description conditions (136:12). The authors suggest that "by isolating common AI errors into well-defined, predictable subgroups, the AI appears more reliable to people" (136:14). Learning slopes rose significantly in the two tasks where descriptions helped (136:13).

## Relation to the argument

The strongest positive result in facet H for an aid the person reads, so it is the case to beat for P9. It shows that a short, concrete statement of where a system fails can raise accuracy in two of three tasks. It also shows the limits P9 predicts: no gain in the task where people were already good, no complementarity in reviews, and no change in the attitudes measured. The authors report that post-hoc explanations "have been found to have a small or even detrimental effect" (136:4), which supports the contrast the author draws between explaining an algorithm and giving behavioural guidance.

D3 ("disclosure doesn't affect our ability to navigate it") is too strong against this paper, if "navigate" means accuracy of reliance: a disclosure about behaviour changed what people did. A narrower claim survives: the disclosed object is the system's measured error pattern, not its workings, and the person still has to read it and apply it item by item. Most of the gain came from trusting the AI more where it was right, not from catching its errors.

Facet check: facet H's second pass says 225 were recruited and 209 analysed. The text removes 13 for failing an attention check and 3 for under 10% accuracy (136:7), which gives 209. The degrees of freedom of the three omnibus tests imply 67, 70 and 68 analysed (205 in all). The paper does not reconcile the two. Facet H's p = 0.048 for birds is confirmed.

## In conversation with

- `bansal2019updates` (ref. 4): cited for model updates that break users' mental models; the authors say updated descriptions could ship with a new model (136:6, 136:13).
- `bucinca2021trust` (ref. 8): cited for the claim that an overly simple or wrong mental model leads to systematic failures (136:1).
- `poursabzi2021manipulating` (ref. 48): cited for information overload that hurts error detection, which motivates the "simple" principle (136:4–136:5).
- `chen2024chatgpt`: not cited here. It measures the kind of silent model update that section 3.2 (136:6) says can break users' mental models.
- Leads: Bansal et al. 2019, "Beyond accuracy" (mental models and error boundaries); Mozannar et al. 2021, teaching humans when to defer; Lai and Tan 2019 (explanations); Zhang, Liao and Bellamy 2020 (confidence and explanation); Lee and See 2004.

## Caution

Crowdworkers with no domain expertise, a simulated AI with hand-set errors, one description type (subgroup accuracy), and binary or small-class classification; the authors list these (136:15–136:16). It tests the display of a known envelope, not whether a real system's envelope can be known or stays fixed. The stated 90% against actual 73.33% accuracy is a design choice that may inflate reliance in all arms. The effect sizes are modest and rest on one description per subgroup. This is arXiv v1 with the CSCW header; the published article may differ.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** the arXiv v1 PDF (CSCW Article 136 layout, 21 pages) from the cards folder; title, authors, version match. About 8 quotations with page labels, 20 numbers (cell sizes, 20/5/5 item split, 95%/40%/20%, 90% against 73.33%, F and p values, confidence intervals, exclusions 13 and 3, implied analysed N of 67, 70, 68), the section 5.2 mechanism claim, and the cited references (Bansal refs 3 and 4, Bucinca ref 8, Poursabzi-Sangdeh ref 48, Mozannar, Lai and Tan, Zhang et al.) in the reference list.

**Findings:** No issues found. The facet-check arithmetic (209 analysed; 205 implied by the degrees of freedom) is correct. I did not check the claim that chen2024chatgpt does not appear in the references beyond noting the reference list has no such entry in the sample I read.
