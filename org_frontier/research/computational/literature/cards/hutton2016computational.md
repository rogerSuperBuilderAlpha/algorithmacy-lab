---
citekey: hutton2016computational
title: Most computational hydrology is not reproducible, so is it really science?
authors: Hutton, Christopher and Wagener, Thorsten and Freer, Jim and Han, Dawei and Duffy, Chris and Arheimer, Berit
year: 2016
doi: 10.1002/2016wr019285
arxiv: null
journal: Water Resources Research
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://research-information.bris.ac.uk/ws/files/87904220/main_text_resubmitted.pdf
sha256: 646d7ecdeacf9f146479d04db69a3f9f588916265d8bc1cbbe608858690c3ac3
pdf_path: literature/pdfs/hutton2016computational.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is an opinion/commentary piece arguing that computational hydrology fails a foundational scientific principle: the code and data that actually produce published results are not regularly made available, which inhibits the community's ability to reproduce and verify findings. The authors situate the problem within the broader "reproducibility crisis" seen across disciplines (preclinical cancer biology, genomics, psychology), and note that some form of code underlies the vast majority of hydrology papers, from data quality analysis to figure preparation. They argue that sharing code and data alone is insufficient because it omits the implementation detail captured in a workflow. As a remedy they make four core recommendations plus a fifth for large-scale studies: (1) make code readable and re-useable; (2) build well-documented workflows that unambiguously tie code and data to results; (3) make code and metadata findable through repositories; (4) cite re-useable code and workflows with persistent identifiers (e.g., DOIs) to document provenance; and (5) develop new procedures ensuring rigour where reproducing large-scale studies is computationally too expensive. They contend reproducible, transparent computational hydrology will provide a more credible foundation for scientific advancement and policy support.

## Key facts it relies on
- The paper's framing example is order-of-magnitude differences in Darcy-Weisbach friction factors estimated from hillslope surface properties in two prior studies (Weltz et al. 1992; Abrahams et al. 1994), after which Parsons et al. (1994) found the experimental set-up was the main factor controlling the difference.
- The authors define the "research compendium" (term from Gentleman & Lang 2004) as comprising, in computational hydrology, the original data used, all analysis/modelling code, and the workflow that ties code and data together to produce the published results.
- They argue sharing data and code alone is insufficient: it does not provide the critical implementation detail contained within a workflow that is required to reproduce published results.
- Four recommendations: [1] make code readable and re-useable; [2] create well-documented workflows combining re-useable code with data; [3] make code and workflows findable via repositories and code metadata; [4] cite re-useable code/workflows with unique persistent identifiers (e.g., DOIs), with DOIs specific to the exact code version used.
- They note that exact reproducibility is impossible in open hydrological systems, but attempting to reproduce the main scientific finding within an acceptable margin of error is a core principle of scientific research (citing Popper 1959).
- They cite the joint editorial published in five hydrology journals (Blöschl et al. 2014) recognizing that model/analysis complexity makes it infeasible to report all adjustable settings (initial conditions, parameters, etc.) in publications.
- They cite Ceola et al. (2015/2014) as showing the importance of a well-documented protocol when 5 research groups attempted to reproduce the same hydrological model calibration experiment.
- Named open code examples include the hydrologic models Topmodel (Beven & Kirkby 1979), VIC (Wood et al. 1992), FUSE (Clark et al. 2008), HYPE (Lindström et al. 2010), groundwater models MODFLOW and PFLOTRAN, and optimization/uncertainty algorithms SCE (Duan et al. 1993), SCEM (Vrugt et al. 2003), and GLUE (Beven & Binley 1992).
- Named repositories/infrastructures: GitHub, Zenodo, Figshare, the EU SWITCH-ON Virtual Water-Science Laboratory, and the US CUAHSI HydroShare; OntoSoft (Gil et al. 2015) is cited as a software-metadata repository/ontology for the geoscience community.
- The study was performed within the EU FP7-funded SWITCH-ON project (grant agreement No 603587); the acknowledgement states "No data was used in producing this manuscript."

## Critical notes from the literature
- This is a commentary/opinion paper, not an empirical study: it presents no original measurements or systematic survey quantifying how many hydrology papers are non-reproducible; claims about code unavailability rest on the authors' own experience and analogy to other fields.
- The authors acknowledge incentive and cultural barriers: the current publication reward system prioritizes novel, seemingly significant results over null results and reproductions (citing Franco et al. 2014; Nosek et al. 2015), and reproducing others' work brings little reward — they explicitly pose the question "why go to the effort!?"
- They concede a key scope limitation: large-scale studies (large modelling domains, many catchments, legacy codes, large user communities) are computationally demanding and cannot currently be expected to be reproduced given the resources required, especially by reviewers; hence recommendation 5 calls for alternative formal processes (e.g., benchmark comparison tests, citing Maxwell et al. 2014) rather than full reproduction.
- They note that current funding policies fall short of mandating software sharing: US NSF and UK NERC require open data/research materials, but software sharing is only encouraged (by NSF), not required.
- The authors recognize that setting high standards for code re-use may be counter-productive to broad adoption, since most hydrology researchers are "scientists first, programmers second"; they therefore frame change as requiring gradual steps and embedded computational-science training (e.g., Software Carpentry).

## Key topics covered
Reproducibility; computational hydrology; research compendium; re-useable code; scientific workflows; code metadata and ontologies (OntoSoft); persistent identifiers / DOIs for code; code repositories (GitHub, Zenodo, Figshare, HydroShare, SWITCH-ON); reproducibility crisis across disciplines; publication reward/incentive system; open science policies of journals and funders (NSF, NERC, Science, Vadose Zone Journal); large-scale modelling and benchmark intercomparison; computational-science training and hydrology education; transparency and public-policy trust (climategate); hydrologic models and algorithms (Topmodel, VIC, FUSE, HYPE, MODFLOW, SCE, SCEM, GLUE).
