---
citekey: moravec2025algorithmic
title: Algorithmic personalization: a study of knowledge gaps and digital media literacy
authors: {Moravec
year: 2025
doi: 10.1057/s41599-025-04593-6
arxiv: null
journal: Humanities and Social Sciences Communications
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41599-025-04593-6.pdf
sha256: ad18483147e4867361d42252d39335d159c2b44ac0a023c2be3e58b5318aaa40
pdf_path: literature/pdfs/moravec2025algorithmic.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to systematically measure the knowledge that different social classes hold about algorithmically personalized online content, and how that knowledge varies across demographic groups. Its main contribution is methodological: a three-stage "information-analytical system" that combines an information model (a 19-question survey scored on three criterion groups), a fuzzy-logic aggregation method, and a fuzzy method using multidimensional (conical/pyramidal) membership functions to derive a normalized score and linguistic knowledge level per social class. The system is verified on survey data from 1213 Czech respondents (quota-sampled, aged 15+), with a worked approbation example using 124 respondents from the Jihomoravský region. Across social classes the population's knowledge of personalized content sits at an "average to above-average" level; young people (15–24) with higher education score highest, while those aged 35–44 and with professional education score lowest. The authors frame the result as evidence of social-class disparities in digital media and algorithmic literacy that justify targeted educational interventions, and present the system as an open, adaptable tool for decision-makers (NGOs, regulators, media managers).

## Key facts it relies on
- Sample: 1975 respondents contacted; 1346 completed the online (CAWI) questionnaire (68.2% return rate); after excluding 16 low-quality and 117 incomplete responses, 1213 respondents remained (604 men, 609 women).
- Quota sampling from the adMeter respondent panel, targeting the Czech population aged 15 and over with quotas on sex, age, education, and region; questionnaire design informed by Volek et al. (2023); average completion time 17 min 51 s.
- Sample composition: 81.8% of working age, 65% with education and 25.7% holding higher education degrees; questionnaire had 19 questions.
- Survey fielded 20 February 2023 to 27 February 2023 (methods text), though abstract and data-availability cite "data from 1213 participants 2024"; received 3 May 2024, accepted 19 February 2025.
- Three criterion groups: G1 = awareness of how content personalization occurs on the web (12 statements K11–K112 scored 1–10), G2 = awareness of the technical way of personalization (multiple-choice, 5 options, fuzzified 0.1–1.0 by number of answers), G3 = awareness of level of control over online content (single item scored 0–30 with an S-shaped membership function).
- Stage 2 uses four selectable fuzzy convolutions (pessimistic, careful, average, optimistic) over normalized inputs with DM-set normalized weights; the worked example used α1=9, α2=10, α3=8 giving β1=0.33, β2=0.37, β3=0.3.
- Stage 3 forms social classes by combining gender, age (7 brackets, 15–24 through 75+), and education (6 levels), then uses a conical multidimensional membership function C_KPC to map onto five linguistic terms: high (0.89,1], above average (0.77,0.89], average (0.65,0.77], low (0.54,0.65], very low [0,0.54].
- Approbation example (Jihomoravský region, 124 respondents): the social class "men, higher education, aged 35–44" yielded Δ=0.188, C_KPC=0.812 → "above average"; men/women results tabulated in Tables 4–5 (values roughly 0.66–0.82).
- Cited prior work: Zarouali et al. (2021) found algorithm misconceptions concentrated among the elderly, less educated, and women; Segijn and Van Ooijen (2020) found younger users more open to personalization techniques; Sehl and Eder (2023) found personalized political ads/news largely rejected in Germany and the UK while commercial ads/entertainment recommendations were better received.

## Critical notes from the literature
- The authors explicitly note that the system depends on a system analyst's interpretation of real data to set knowledge-level thresholds, and that outcome ambiguity is influenced by the chosen multidimensional membership-function types and characteristic functions; they assert (without independent benchmarking) that these do not compromise reliability.
- The study is essentially a single-country (Czech), single-time-point quota survey; the knowledge "score" is a constructed fuzzy index calibrated by expert/DM judgments (weights, scale cut-points) rather than validated against an external criterion of algorithmic literacy.
- The headline demographic findings (young + highly educated score highest; mid-age + professional education lowest) are derived from the 124-respondent regional approbation example, not the full 1213-respondent set, limiting how strongly the demographic gaps can be generalized.
- There is an internal date inconsistency: the methods report fielding in February 2023, while the abstract and data-availability statement label the data as "2024"; readers should treat the survey period cautiously.
- The work is framed as a methodological/tool contribution; the authors note adoption of algorithmic systems varies by country, organization type, and resources (citing Mitova et al. 2023; Caplan and Boyd 2018), which limits transfer of any single calibrated instance.

## Key topics covered
Algorithmic personalization; digital media literacy; algorithmic literacy; knowledge gaps; fuzzy logic / fuzzy set theory; multidimensional (conical/pyramidal) membership functions; information-analytical system; quota survey (CAWI); social class / demographic disparities; personalization–privacy paradox; online behavioral advertising (OBA); informational self-determination; misinformation/disinformation resilience; Czech Republic case study.
