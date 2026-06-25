---
citekey: pineau2021improving
title: Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)
authors: Pineau, Joelle and Vincent-Lamarre, Philippe and Sinha, Koustuv and Lariviere, Vincent and Beygelzimer, Alina and d'Alche-Buc, Florence and Fox, Emily and Larochelle, Hugo
year: 2021
doi: null
arxiv: 2003.12206
journal: arXiv
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2003.12206
sha256: 0ea62d8ae3eede31d18faedf4246d59f9c07346df59b4ca99407ef4323d2307f
pdf_path: literature/pdfs/pineau2021improving.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a report describing the NeurIPS 2019 reproducibility program, an initiative introduced at the premier machine learning conference to improve how the community conducts, communicates, and evaluates research. The program had three components: a (voluntary) code submission policy, a community-wide reproducibility challenge, and a Machine Learning Reproducibility Checklist embedded in the paper submission process. The authors describe how each component was deployed and analyze data on author and reviewer behavior. Key findings include a rapid rise in voluntary code submission (from under 50% a year earlier to nearly 75% at camera-ready for NeurIPS 2019), thousands of reviewers engaging with submitted code, 173 papers claimed in the reproducibility challenge, and one-third of reviewers finding the checklist answers useful. The authors frame the work as a case study rather than conclusive causal evidence, noting they cannot yet show these mechanisms improve paper quality, and list open questions for further study. They argue a voluntary code-submission policy is sufficient at this stage and that the checklist could be adapted to other venues.

## Key facts it relies on
- A 2016 Nature survey (Baker, 2016) found more than 70% of researchers failed to reproduce another researcher's experiments and over 50% failed to reproduce one of their own.
- The program had three components: a code submission policy, a community-wide reproducibility challenge, and the ML Reproducibility Checklist in the submission process.
- For NeurIPS 2019: 6743 papers submitted, 21.1% acceptance rate, 40% of papers with code at submission, 74.4% with code at camera-ready (Table 1); the trend rose across NeurIPS 2018 (<50% at camera-ready), ICML 2019 (67%), to NeurIPS 2019 (74.4%).
- About 40% of authors reported providing code at initial submission, confirmed by reviewers for 71.5% of those submissions; code availability at submission was positively associated with reviewer score (p < 1e-08).
- Reviewer survey: code was provided in 5298 cases; of those, 2255 reviewers looked at the code and 1315 found it useful in guiding the review; when code was not provided, 3881 reviewers wished it had been available.
- The reproducibility challenge had 173 papers claimed (a 92% increase over ICLR 2019's 90), with participants from 73 institutions (63 universities, 10 industrial labs) and 84 reports reviewed (Table 2); selected reports were published in ReScience C.
- Checklist responses: 97% of submissions said to contain a clear description of the mathematical setting/algorithm/model; 89% reported a description of how experiments were run (consistent with ~9% of submissions listing "Theory" as primary area); 87% saw value in clearly defining metrics/statistics, yet 36% judged error bars not applicable.
- 34% of reviewers found the Reproducibility Checklist answers useful for evaluating submissions; reviewers who found it useful gave higher paper scores and were more likely to accept.
- The NeurIPS 2019 code policy was voluntary: it "expects code only for accepted papers, and only by the camera-ready deadline," and code was not used during review to decide soundness.
- Cited prior reproducibility work: Raff (2019) replicated 63.5% of results across 255 manuscripts, with 85% success when original authors assisted versus 4% when authors did not respond.

## Critical notes from the literature
- The authors explicitly state they "do not have concluding evidence" that these processes improve the quality of work or papers; the report is framed as a case study, not a causal evaluation.
- For the association between checklist "yes" answers and higher acceptance rate, the authors caution it is too early to rule out covariates (paper topic, reviewer expectations); a higher acceptance rate for "NA" responses on figure/table questions disappears when restricting to manuscripts where reviewers found the checklist useful.
- The authors note a possible selection bias in Raff (2019): authors who knew their results would reproduce may have been more likely to provide assistance, and they note it remains unclear whether ML has a reproduction problem or a reporting problem.
- The paper acknowledges legitimate objections to code submission (dataset confidentiality, proprietary software, prohibitive computation cost, and that having code does not guarantee correctness), and is not aiming for 100% compliance.
- The report lists multiple open questions it cannot answer, including the long-term value of submitted code, the accuracy of checklist answers, and the measurable effect of the checklist on paper quality and the review process.

## Key topics covered
Reproducibility; replicability; robustness; generalisability; NeurIPS 2019; code submission policy; ML Reproducibility Checklist; reproducibility challenge; ReScience C; OpenReview; open science; checklists in science (CONSORT, EQUATOR, TOP, Nature reporting checklist); double-blind review; peer review quality; reporting vs reproduction problem; reproducibility tooling (Docker, ReproZip, WholeTale); ACM artifact badges.
