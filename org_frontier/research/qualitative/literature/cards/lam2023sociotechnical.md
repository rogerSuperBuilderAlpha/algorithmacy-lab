---
citekey: lam2023sociotechnical
title: Sociotechnical Audits: Broadening the Algorithm Auditing Lens to Investigate Targeted Advertising
authors: Lam, Michelle S. and Pandit, Ayush and Kalicki, Colin H. and Gupta, Rachit and Sahoo, Poonam and Metaxa, Dana{\"e}
year: 2023
doi: 10.1145/3610209
arxiv: null
journal: Proceedings of the ACM on Human-Computer Interaction
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2308.15768
sha256: 83afc7acec36914b853c6d80840da89e5bdb5b536f81004725f7d4ea3a95c063
pdf_path: literature/pdfs/lam2023sociotechnical.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces the concept of a sociotechnical audit (STA), a two-part audit combining an algorithm audit (changing inputs to a system and observing outputs) with a user audit (changing inputs to the user and observing effects), arguing that algorithm audits alone miss how users and algorithms jointly influence each other. To instantiate the method, the authors build Intervenr, a browser extension plus web application that runs two-phase, longitudinal, in-browser audits with consenting, compensated participants: an observational phase that captures baseline algorithmic content and behavior, followed by an intervention phase that enacts in situ client-side modifications. As a case study, they deploy Intervenr in a two-week sociotechnical audit of targeted online advertising (N=244 completers), using an ablation-style "ad-swap" intervention that randomly pairs participants and replaces all their ads with their partner's ads to test the premise that personalized targeting performs better for users. The audit collected over 537,000 ads and measured user-oriented metrics (ad interest, feeling of representation) and advertiser-oriented metrics (recognition, views, clicks). They find personalized ads outperform swapped ads on all metrics (e.g., holistic ad interest dropped from 3.89 to 2.74, representativity from 4.10 to 2.77), but that users acclimate to a partner's ads within one week (interest in partner ads rose ~16.9%), casting doubt on the necessity of hyper-personalized, privacy-invasive targeting. Marginalized-identity participants (non-white and/or non-men) showed larger drops when targeting was broken, suggesting personalization may hold more value for users outside the social "default."

## Key facts it relies on
- An STA is defined as a two-part audit: an Algorithm Audit (change inputs to the algorithm, observe outputs) plus a User Audit (change inputs to the user, observe effects); Table 1 classifies existing methods (crowdsourced audits, RCTs, field experiments, design interventions, A/B tests) by whether they include each audit type.
- Case study: N=244 participants completed both phases over a two-week study; recruited via Prolific from 5,600 screener completers, of whom 1,310 (23.4%) signed up; 600 selected, 402 (67.0%) onboarded, 244 completed (85.6% observational-phase retention, 78.7% intervention-phase retention).
- The ablation intervention randomly pairs participants as "swap partners"; in week 2 each participant exclusively sees ads sampled from their partner's collected ad set, breaking targeting at the user level while preserving ecological validity (real ads delivered to a real user).
- Total of 537,945 ads collected; 314,762 from the final 244 participants (88,604 observational, 121,489 intervention-phase originals, 104,669 swapped-in); 21.41% of ads viewed, only 123 ads (0.04%) clicked, and 18.21% contained a person (automated detection).
- Baseline personalized ads performed only moderately: holistic ad interest M=3.89 (SD=1.87), representativity M=4.10 (SD=1.67) on a 7-point Likert; per-ad correct recognition 40.9% (SD=24.5%); 27.2% of observational-phase ads viewed; click rate M=0.057%.
- Ad-swap intervention significantly reduced metrics: holistic ad interest 3.89→2.74 (t(243)=8.73, p<0.001, Cohen's d=0.56) and representativity 4.10→2.77 (t(243)=9.79, p<0.001, d=0.63); per-ad interest for own vs. swapped ads 3.72 vs. 2.93.
- Acclimation effect: over one week, ad interest toward partner ads rose ~16.9% and representativity ~17.7%, while interest in one's own ads fell ~1.6% and representativity rose ~2.0% — a partner-ad increase corresponding to more than one Likert point.
- Demographic effects: significant effect of race on baseline ad interest (F(3,221)=3.73, p<0.05) and representativity (F(3,221)=2.97, p<0.05), with Black participants responding more positively; drops in interest when targeting broke were larger for marginalized race/gender (interaction effect F(6,221)=2.20, p<0.05).
- False recognition rose from 20.8% (observational) to 27.4% (intervention) (t(329.5)=-3.88, p<0.001, d=0.41); Intervenr ad-detection coverage validated at median 80% (15.3% false-negative rate) and person-detection at 86.3% accuracy.
- Intervenr was implemented as a Chrome extension (Manifest V2) integrating the AdNauseam ad blocker (built on uBlock Origin), a Django web app on Heroku, and a Python data pipeline on Amazon EC2; participants compensated $10 per milestone (~$40/hr) via Amazon gift cards.

## Critical notes from the literature
- The authors stress the audit captures only browser/desktop content, giving partial coverage of users' ad ecosystem; this could bias recognition (ads seen elsewhere) and weaken the intervention (users likely saw their own targeted ads on other devices), implying the acclimation effect is probably an underestimate.
- The study spanned only two weeks; the authors caution they cannot speak to longer-horizon effects (acclimation may plateau or reverse) and recommend four-week-or-longer audits of the human aspect.
- Non-compliance (using another browser, incognito, or device) could not be fully tracked; only self-reported measures were collected (low: disabling M=1.29, incognito M=1.34), and participants may have underreported.
- The system is desktop-only, missing the ~15% of American adults who are smartphone-only; the authors flag mobile data collection as a major unsolved limitation, compounded by Chrome's pending Manifest V2→V3 move that may restrict the in-browser interventions the method depends on.
- The authors explicitly do not claim the first sociotechnical audit (prior work paired algorithm audits with user interventions/experiments, e.g., Metaxa et al. 2021, Matias 2023, Mozilla Rally); they note hybrid first-/second-party access arrangements remain contentious in the auditing community over auditor impartiality.

## Key topics covered
algorithm auditing; sociotechnical audit (STA); user audit; targeted/online advertising; ablation-style intervention; ad-swap experiment; browser extension instrumentation; AdNauseam / uBlock Origin; longitudinal field study; Prolific recruitment; ad interest and representativity metrics; ad recognition / views / clicks; false recognition; repeated-exposure / familiarity effect; demographic disparities (race, gender); marginalized users; ecological validity; crowdsourced auditing; A/B testing vs. auditing; RCTs and field experiments; Mozilla Rally; Manifest V2/V3; privacy and surveillance advertising
