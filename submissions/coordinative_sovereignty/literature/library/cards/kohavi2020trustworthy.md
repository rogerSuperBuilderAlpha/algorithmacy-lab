---
id: kohavi2020trustworthy
type: book
authors: [ "Kohavi, R.", "Tang, D.", "Xu, Y." ]
year: 2020
title: "Trustworthy online controlled experiments: A practical guide to A/B testing"
container: ""
volume: ""  issue: ""  pages: ""  publisher: "Cambridge University Press"
doi: "10.1017/9781108653985"
url: ""
origin: [audit]
priority: optional
role: optional
chapter_sections: ["§3", "§3.2"]
tags: [algorithmic_management_literacy, platform_power_economics]
verified: abstract
verified_on: 2026-08-23
verified_how: "Cambridge University Press frontmatter PDF (9781108724265) opened; authors, year, ISBN, DOI 10.1017/9781108653985 and the book description read. DOI added from the publisher frontmatter (sources.json had none)."
apa: "Kohavi, R., Tang, D., & Xu, Y. (2020). Trustworthy online controlled experiments: A practical guide to A/B testing. Cambridge University Press. https://doi.org/10.1017/9781108653985"
corrections: "DOI resolved: none → 10.1017/9781108653985 (audit asked to verify before use); subtitle confirmed"
anonymization_risk: none
---

## Summary
This is a practitioner's handbook on online controlled experiments, written by the leaders of the experimentation platforms at Google, LinkedIn and Microsoft. Its premise is that getting numbers is easy and getting numbers you can trust is hard. The book explains how large technology companies accelerate product change through A/B tests, drawing on experience at firms that each run more than 20,000 controlled experiments a year, and it walks through the pitfalls that make such experiments untrustworthy: sample ratio mismatch, novelty effects, interference between variants, metric design and the organizational decisions that follow. It is not an academic study of platforms but a description of practice from inside them, and its value for the chapter is evidential: it documents that ranking, matching and interface configurations on large platforms are under continuous experimental revision, which is the practice behind the chapter's claim that the mediator is reconfigured continuously. It does not quantify how often production ranking systems change.

## Use in the chapter
Not cited. Audit U1 marks the §3 and §3.2 claims that the mediator is "adaptive, reconfigured continuously and without notice" and that "a ranking system is retuned continuously" as load-bearing and unsourced, and proposes Koo and Eesley 2021 and Rahman 2021, "optionally Kohavi, Tang & Xu 2020 on continuous experimentation". Gap G2 notes that no peer-reviewed source quantifies retuning frequency; this book documents experimentation practice, so "continuously" remains an inference and should be worded as such. Role: optional support for the continuous-reconfiguration claim.

## Key quotations
"Getting numbers is easy; getting numbers you can trust is hard." (publisher description, frontmatter)
"Based on practical experiences at companies that each runs more than 20,000 controlled experiments a year" (publisher description, frontmatter)

## Related cards
koo2021platform, rahman2021invisible, eu2019p2b, christin2020ethnographer, ziewitz2019rethinking, oreilly2024algorithmic
