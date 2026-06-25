---
citekey: heyselaar2023casa
title: The CASA theory no longer applies to desktop computers
authors: Heyselaar, Evelien
year: 2023
doi: 10.1038/s41598-023-46527-9
arxiv: null
journal: Scientific Reports
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41598-023-46527-9.pdf
sha256: 83ab40cd235a5385ed402ae117f19e9b950761c259a798a108dd9a07bd9eb36a
pdf_path: literature/pdfs/heyselaar2023casa.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The Computers Are Social Actors (CASA) theory holds that people unconsciously and automatically respond socially to computers as if they were human, and its originators (Reeves & Nass) claimed that time and experience should not weaken this effect. This paper asks whether that claim still holds after 30 years by conducting the first direct (non-conceptual) replication of the seminal 1994 "Are humans polite to computers?" politeness study, using a simple desktop computer with 132 participants in 2022. Participants completed a computer-run tutoring/testing/scoring session in which the computer praised its own performance, then evaluated that performance either on the same computer (Same Computer condition) or on an identical computer in another room (Different Computer condition); the original effect was that people rated the computer more positively when evaluating it on the same machine (politeness). The replication found no CASA effect: positivity was equal across conditions (Same = 5.7, Different = 5.7; t(130) = −0.2, p = 0.852, Cohen's d = −0.03), versus the large original difference (5.6 vs 4.5; t(17) = 3.5, p < 0.001, omega-squared = 0.36). The author argues the CASA effect is tied to a novelty effect and may only apply to "emergent" technology, implying current emergent social technologies (chatbots, robots, virtual agents) may cease to elicit CASA responses within a generation.

## Key facts it relies on
- The original CASA politeness study (Nass, Steuer & Tauber 1994; Nass, Moon & Carney 1999) used 30 Stanford undergraduates, 10 in each of 3 conditions; the replication dropped the paper-and-pencil condition and kept 2 computer conditions.
- Original positivity result: Raw Index/10 Same Computer = 5.6, Different Computer = 4.5, two-sample t(17) = 3.5, p < 0.001, omega-squared = 0.36.
- Replication positivity result: Raw Index/10 Same Computer = 5.7, Different Computer = 5.7, two-sample t(130) = −0.2, p = 0.852, Cohen's d = −0.03 (no effect).
- Homogeneity/"white lie" analysis: original found smaller variance in Same condition (Mean heterogeneity Same = 2.0, Different = 2.5, t(20) = 3.3, p < 0.001); replication found no difference (Same = 2.2, Different = 2.1, t(40) = 0.6, p = 0.533).
- Sample: 132 participants (75.7% female, mean age 22.7 years, SD 2.9) from the Radboud University Experiment Database; Same Computer condition n = 74, Different Computer condition n = 58. A power analysis (d = 0.5, alpha = 0.05, power 0.8, G*Power 3.1) recommended 128 total (64 per condition).
- Procedure detail: tutoring session presented 20 facts on American culture (rated 1–3 for prior knowledge), a 12-item five-alternative multiple-choice test, and a scoring session where the computer praised itself; all participants were told they answered 8 of 12 correctly and received identical evaluations.
- Outcome measure: 21 adjective items rated on a 9-point scale (1 = describes very poorly, 9 = describes very well), combined into a single factor; analyzed with two-sample t test in R (4.1.0), data normally distributed (Levene p = 0.513).
- Hardware/software: Dell Precision 3640 with a 24-inch BenQ XL2420Z screen, experiment run in Presentation (Neurobehavioral Systems, version 23.0), in single-person cubicles with an identical neighboring room for the Different Computer condition.
- Reeves & Nass explicitly framed CASA as resistant to age, knowledge, distraction, or convenience and as distinct from anthropomorphism (conscious belief), with CASA being unconscious/automatic ("it is belief, not disbelief, that is automatic").

## Critical notes from the literature
- The author acknowledges several alternative explanations she could not rule out: the exact original computer model could not be acquired, and "Internet of Things"/Cloud assumptions may have led participants to believe the Same and Different computers shared evaluation data (so they might have been polite in both conditions); follow-up studies measuring these moderators are flagged as needed.
- Scope limitation stated by the author: only the politeness phenomenon was directly replicated, whereas CASA rests on many other social phenomena, so direct replications of other CASA studies are needed before generalizing.
- The interpretation rests on a "novelty effect" account (citing diminishing robot-tutor and chatbot-friendship benefits over ~3 weeks); the author concedes the original 1990s effect may have been driven by novelty, and that the effect "may have gone much earlier" than the 30-year gap she tested, making the timing of decay uncertain.
- The original studies had very small per-condition samples (n = 10), and the paper notes prior indirect/conceptual replications have produced mixed results (some showing CASA, some not), with the distinction hinging on how novel the tested technology was at test time.

## Key topics covered
Computers Are Social Actors (CASA) theory; media equation; human-machine/human-computer interaction; direct vs conceptual replication; politeness effect; social desirability and "white lies"; novelty effect; anthropomorphism vs unconscious social response; emergent technology (chatbots, robots, virtual agents); desktop computers; Reeves & Nass; power analysis; factor analysis of adjective ratings.
