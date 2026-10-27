# Layman, L., & Roden, W. (2023). A controlled experiment on the impact of intrusion detection false alarm rate on analyst performance. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 67*, 220–225. https://doi.org/10.1177/21695067231192573

**Identifier:** doi:10.1177/21695067231192573 · arXiv:2307.07023 · **Read depth:** full_text (arXiv v1 preprint, 13 Jul 2023, 8 pp., not the HFES proceedings text, whose pagination is 220–225; locators below are the arXiv PDF's. All 8 pp. read, including the reference list) · **Source-tier:** preprint of a conference paper · **Evidence basis:** direct_read · **Design and sample:** between-subjects experiment; 52 volunteers recruited (computing mailing lists, a security office, two computer-security courses at one university, Fall 2019), 51 analysed (25 and 26 per group), each triaging 52 simulated intrusion-detection alarms in a web app (§2.1, §3, pp. 2–4) · **Parties modeled:** person–system (an analyst triaging a detector's alarms) · **Facets:** G · **Read:** 2026-10-13

## What it argues
Layman and Roden test the common claim that a high false-alarm rate hurts the analyst who reviews the alarms, which "have not been investigated empirically" (§1, p. 1). Participants played a junior analyst deciding whether each "impossible travel" login alarm (one user authenticating from two distant cities) should be escalated to a senior analyst. Both groups used a short "Security Playbook" and saw the same kind of alarm. One group got 25 true and 25 false alarms (50% false-alarm rate, FAR); the other 7 true and 43 false (86% FAR), plus two instruction-check alarms each (§2.3, p. 3). Participants were not told the detector's reliability and got no feedback on their answers (p. 4).

Results (Table 2, pp. 4–5; Mann–Whitney tests):

- Sensitivity (share of true alarms escalated): median 0.83 in the 50% group, 0.86 in the 86% group, U = 412.5, p = .098, not significant. Hypothesis 1 (sensitivity falls as the false-alarm rate rises) was not supported (p. 6).
- Precision (share of escalations that were right): median 0.80 against 0.33, U = 555.0, p < .001, effect size r = .708.
- Time on task: median 13.44 against 18.76 minutes, about 40% longer, p < .001. Mean time per alarm 15.6 s against 21.4 s.
- Mean confidence was 3.84 in both groups; workload scores showed no group differences (p. 4).

The abstract's "47% lower precision" is a difference of 47 percentage points (0.80 − 0.33). In relative terms the median fell by about 59%. The authors explain the precision drop partly by participants who over-escalated to be safe: "I felt like there were only a few examples that seemed like they should definitely be escalated, but [I] escalated many more than that so that a threat would not go unnoticed" (p. 6). They add that "organizations place a priority on high sensitivity to intrusions at the expense of precision" (pp. 6–7). They conclude that even 50% false alarms, "a rate unacceptable in many disciplines", gives a clear gain in analyst accuracy (p. 7).

## Relation to the argument
It is one of the few direct human studies in the alert-review literature that facet G collects for premise P12 and for the post's P15 (a person reading evidence after the event). What it shows is mixed for the strong form of P12. People kept finding true alarms at both rates. What changed was cost: more false escalations and more time, and an incentive to over-escalate. That fits the picture of review as a burden that shifts behaviour, and it does not show that people fail to detect attacks.

Facet check: Facet G quotes the abstract exactly ("47% lower precision and 40% slower time on task"). The body shows the 47 is in percentage points of median precision, so a reader who takes it as a relative drop would understate the fall (about 59% in relative terms). Facet G does not mention that the sensitivity difference was not significant at p = .098 with 7 true alarms in the high-false-alarm group, so sensitivity is estimated on few items; this is my observation from the design, not a claim in the paper.

## In conversation with
Cites no work in `../references.bib`. Its reference list leans on Axelsson (2000) on the base-rate fallacy in intrusion detection, Sawyer & Hancock (2018) on the prevalence paradox, Bliss et al. (1995) on probability matching to alarm reliability, and Sundaramurthy et al. (2015) on analyst burnout; none is in the bib. Sits beside the bib's alert-fatigue entries `ancker2017effects`, `alahmadi2022false` and `tariq2025alert`, which it does not cite.
Leads: Axelsson (2000), *ACM TISSEC* 3(3); Julisch (2003), alarm clustering; Ben-Asher & Gonzalez (2015), knowledge and attack detection; Dutt et al. (2012), base rates and detection; Roden & Layman (2020), the "Cry Wolf" dataset.

## Caution
Student and volunteer participants in a one-hour online task with a playbook that makes false alarms discernible, not working analysts; two false-alarm rates only; sensitivity is the hit rate and not d′, so it cannot separate skill from bias. The authors call for "larger sample sizes, longer duration, varied alarm triage tasks, and populations that include a variety of cybersecurity expertise" (p. 7). The HFES version may differ from this preprint, so check numbers against the proceedings paper.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The arXiv v1 PDF (2307.07023, 8 pp.) named in the card, extracted with pdftotext in both reading-order and layout modes. I checked 5 verbatim quotations with their pages, Table 2 (sensitivity medians 0.83 and 0.86, precision 0.80 and 0.33, time medians 13.44 and 18.76 minutes), the Mann-Whitney statistics (U = 412.5, p = .098; U = 555.0, r = .708), the 15.6 s and 21.4 s means, confidence 3.84, the sample (52 recruited, 1 excluded, 25 and 26 analysed, Fall 2019), the 25/25 and 7/43 alarm mixes, and the reference-list leads.

**Findings:** No issues found. The 'organizations place a priority...' quotation runs across the page 6-7 break, as the card's 'pp. 6-7' says. The abstract's '47% lower precision' is, as the card states, 0.80 against 0.33. The 'about 59%' relative figure is the card's own arithmetic (0.47/0.80 = 58.8%) and is right.
