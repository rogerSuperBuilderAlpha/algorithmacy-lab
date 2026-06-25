---
citekey: ioannidis2005published
title: Why Most Published Research Findings Are False
authors: Ioannidis, John P. A.
year: 2005
doi: 10.1371/journal.pmed.0020124
arxiv: null
journal: PLoS Medicine
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:publisher
source_url: https://journals.plos.org/plosmedicine/article/file?id=10.1371/journal.pmed.0020124&type=printable
sha256: ffc1005680cb620eec4c913437dfabbf311b535cfe16cbaeb2faec1f92afc362
pdf_path: literature/pdfs/ioannidis2005published.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This essay argues, via a probabilistic model, that under realistic conditions most claimed research findings are more likely false than true. Ioannidis defines a "research finding" as any relationship reaching formal statistical significance (typically p < 0.05) and asks for the post-study probability that such a claim is true — the positive predictive value (PPV) — using a 2x2 table comparing claimed findings against the gold standard of truly existing relationships. The key quantity is R, the ratio of true to no relationships among those tested in a field; the pre-study probability of a relationship being true is R/(R+1), and PPV depends jointly on R, statistical power (1-β), and the Type I error rate α. He shows PPV = (1-β)R/(R-βR+α), so a finding is more likely true than false only when (1-β)R > α (i.e., > 0.05 for α = 0.05). Extending the model to incorporate bias (parameter u, the proportion of non-findings reported as findings due to design/analysis/reporting flaws) and to multiple independent teams (n studies) shows both factors generally lower PPV further. Simulations across plausible study designs (Table 4) show a PPV above 50% is hard to achieve: an adequately powered RCT with 1:1 pre-study odds yields ~85%, but exploratory epidemiology and discovery-oriented massive-testing research yield PPVs of 0.20 down to ~0.001. He concludes that in many fields claimed effects may largely be accurate measures of the prevailing bias, and offers corollaries and remedies.

## Key facts it relies on
- A research finding is defined as any relationship reaching formal statistical significance, e.g. p-value less than 0.05; "negative" research is also useful but the essay targets claimed positive relationships.
- R is the ratio of "true relationships" to "no relationships" among those tested in a field; the pre-study probability of a relationship being true is R/(R + 1); power is 1 − β and the Type I error rate is α.
- From the 2x2 table (Table 1), PPV = (1 − β)R / (R − βR + α); a finding is more likely true than false if (1 − β)R > α, i.e. if (1 − β)R > 0.05 for the usual α = 0.05.
- With bias u (proportion of probed analyses not truly findings but reported as such), PPV = ([1 − β]R + uβR) / (R + α − βR + u − uα + uβR); PPV decreases with increasing u unless 1 − β ≤ α (1 − β ≤ 0.05).
- For n independent studies of equal power (Table 3), PPV = R(1 − βⁿ) / (R + 1 − [1 − α]ⁿ − Rβⁿ); PPV tends to decrease with more independent studies unless 1 − β < α.
- Box 1 example: a whole-genome study of 100,000 polymorphisms with ~10 truly associated gives R = 10/100,000 = 10⁻⁴; with 60% power at α = 0.05, a barely-significant association raises post-study probability about 12-fold but to only 12 × 10⁻⁴; with bias u = 0.10 it falls to 4.4 × 10⁻⁴, and with 10 independent teams it is only 1.5 × 10⁻⁴.
- Table 4 simulated PPVs: adequately powered RCT (1−β = 0.80, R = 1:1, u = 0.10) → 0.85; confirmatory meta-analysis of good RCTs (0.95, 2:1, 0.30) → 0.85; meta-analysis of small inconclusive studies (0.80, 1:3, 0.40) → 0.41; adequately powered exploratory epidemiology (0.20, 1:10, 0.30) → 0.20; discovery-oriented research with massive testing (0.20, 1:1,000, 0.80) → 0.0010.
- Six corollaries: findings are less likely true when (1) studies are smaller, (2) effect sizes are smaller, (3) the number of tested relationships is greater and less preselected, (4) there is greater flexibility in designs/definitions/outcomes/analyses, (5) there are greater financial/other interests and prejudice, and (6) the field is "hotter" with more competing teams.
- Example effect-size contrasts: smoking and cancer/cardiovascular disease (relative risks 3–20) vs. genetic risk factors for multigenetic diseases (relative risks 1.1–1.5); the "Proteus phenomenon" describes rapidly alternating extreme claims and opposite refutations, noted as common in molecular genetics.

## Critical notes from the literature
- The author states the model rests on simplifying assumptions: circumscribed fields with one true relationship or similar power across true relationships, and that bias u does not depend on whether a true relationship exists ("not an unreasonable assumption, since typically it is impossible to know which relationships are indeed true").
- He acknowledges "reverse bias" can annul true findings (measurement error, inefficient data use, conflicts that bury findings) but says there is no good large-scale empirical evidence on its frequency and judges it probably less common.
- The PPVs in Table 4 are derived assuming α = 0.05 for a single study; the values are simulations under chosen parameter combinations rather than empirical measurements.
- The "gold standard" of truth is acknowledged to be unattainable — "it is impossible to know with 100% certainty what the truth is in any research question" — so estimates of R remain subjective approximations.
- Proposed remedies (better-powered evidence targeted at high pre-study probability questions, considering totality of evidence rather than single teams, reducing bias via standards, upfront study registration, and explicitly considering R) are offered as partial improvements, with the author noting registration is challenging for hypothesis-generating research.

## Key topics covered
positive predictive value (PPV); pre-study odds R; statistical power (1−β); Type I error α; p < 0.05 significance; false positive report probability; bias (u); selective/distorted reporting; multiple independent teams (n studies); meta-analysis; randomized controlled trials; molecular/genetic epidemiology; microarrays / high-throughput discovery research; whole-genome association; effect size and relative risk; null fields; Proteus phenomenon; data dredging; conflicts of interest; study registration; research methodology and reproducibility
