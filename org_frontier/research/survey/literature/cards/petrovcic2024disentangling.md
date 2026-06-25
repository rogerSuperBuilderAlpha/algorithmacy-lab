---
citekey: petrovcic2024disentangling
title: Disentangling the role of algorithm awareness and knowledge in digital inequalities: an empirical validation of an explanatory model
authors: Petrov{\v{c}}i{\v{c}
year: 2024
doi: 10.1080/1369118X.2024.2363896
arxiv: null
journal: Information, Communication \& Society
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://repozitorij.uni-lj.si/Dokument.php?id=200532&dn=
sha256: 3ae106417c1ba25e9f26c9b634aef191fce6c41ed77e67ff7b19e691571049bb
pdf_path: literature/pdfs/petrovcic2024disentangling.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how algorithm awareness and algorithm knowledge fit into the sequential pathways of digital inequalities, extending the model of compound and sequential digital exclusion (MCSDE; van Deursen et al., 2017) by positioning these two dimensions of "algorithm literacy" as digital resources mediating between internet access/skills and internet uses/outcomes. It tests an 11-hypothesis explanatory model using path analysis on a representative face-to-face survey subsample of internet users (N = 802) from the 2022 Slovenian Public Opinion Survey (response rate 54%). The model fit the data well, confirming the established sequential chain: ubiquity of internet access strongly determines internet skills and uses, which in turn drive tangible internet outcomes. For the algorithm dimensions, ubiquity of access affected only awareness (not knowledge), internet skills predicted both awareness and knowledge, awareness strongly predicted knowledge, and algorithm knowledge (but not awareness) significantly predicted breadth of internet uses. Age, education, and income moderated several paths, while gender and occupation did not. The authors conclude that algorithm awareness and knowledge are distinct facets that should be incorporated into both conceptual models of digital inequalities and digital-inclusion interventions, especially for older and low-income users.

## Key facts it relies on
- Data come from the 2022 wave of the Slovenian Public Opinion Survey, a face-to-face survey (April–August 2022) of 1001 respondents drawn via two-stage random sampling stratified by settlement type and statistical region; response rate = 54%. The analytic subsample is internet users from the past three months (N = 802; 80.1%).
- Algorithm awareness and knowledge were measured with an adapted short Algorithm Literacy Scale (ALS; Dogruel et al., 2022), 5 items each, scored as true/false test items (correct = 1; incorrect or "I don't know" = 0). After Rasch-model fitting one item was dropped per scale; the resulting 4-item scales had KR20 = .83 (awareness) and KR20 = .75 (knowledge).
- Internet skills used a short Internet Skill Scale (ISS; van Deursen et al., 2016) as a second-order factor over operational, information-navigation, social, and creative skills; CFA fit χ²(115) = 424.265, p < .001, CFI = .947, RMSEA = .068, SRMR = .057; Cronbach's α = .90, composite reliability = .79.
- Internet uses (17 items, dichotomized, formative) and internet outcomes (10 items, formative) were averaged into composite scores; both passed PCA/multicollinearity checks (max VIF < 2.2 and < 2.0 respectively). Ubiquity of access was the average number of five device types used to go online.
- The overall path model fit excellently (N = 802): χ²(4) = 8.395, p = .078, CFI = .996, RMSEA = .046, SRMR = .024.
- Confirmed standardized direct effects: ubiquity of access → internet skills β = .452, → breadth of uses β = .319, → algorithm awareness β = .136; internet skills → breadth of uses β = .409, → algorithm awareness β = .366, → algorithm knowledge β = .280; algorithm awareness → algorithm knowledge β = .482; algorithm knowledge → breadth of uses β = .115; breadth of uses → internet outcomes β = .602 (all p ≤ .001 except knowledge→uses p = .001).
- Two hypotheses were not supported: ubiquity of access → algorithm knowledge (β = .044, p = .167; H5) and algorithm awareness → breadth of uses (β = .056, p = .101; H9).
- Multi-group analysis found moderation by age, education, and income but not gender or occupation; e.g., the access→skills path was stronger for older users (18–44: 0.632; 45–64: 1.468; 65+: 2.409), for lower-education users (1.831 vs. 0.951 higher), and for below-average income (2.091 vs. 0.803 above-average).
- Estimation used full information maximum likelihood (FIML; 347 cases / 43.3% had ≥1 missing value) with the robust MLR estimator, in R using the eRm (Rasch) and lavaan packages.

## Critical notes from the literature
- The authors state the sequentiality of the model paths was derived from MCSDE assumptions but the cross-sectional research design cannot verify causal claims; post-hoc reverse and mediational models (Tables OS9/OS10) fit equally well or close to the proposed model, so longitudinal or experimental studies are needed to establish causal and bidirectional effects.
- They acknowledge they could not test the potential bidirectional relationship between algorithm awareness/knowledge and internet uses proposed by some scholars (e.g., Swart, 2021).
- Scope is limited to only two of the dimensions of algorithm literacy (awareness and knowledge), explicitly omitting others such as critical evaluation, coping tactics, and creation/design (Note 1; Dogruel, 2021).
- Generalizability is constrained: data are from Slovenia (an average-performing EU country on skills/uses per Eurostat 2022), and the authors note no comparable EU data exist for algorithm awareness and knowledge for benchmarking.

## Key topics covered
Digital inequalities (first/second/third level); model of compound and sequential digital exclusion (MCSDE); algorithm literacy; algorithm awareness vs. algorithm knowledge; Algorithm Literacy Scale (ALS); Internet Skill Scale (ISS); ubiquity of internet access; breadth of internet uses; tangible internet outcomes; path analysis; multi-group / moderation analysis; Rasch modeling; FIML / MLR estimation; Slovenian Public Opinion Survey; digital inclusion interventions.
