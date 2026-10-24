# Yu, H., Liu, L., Jiang, X., Jia, Y., Wang, S., Qian, P., & Chen, Y. (2026). Habituation at the gate: Rising approval and declining scrutiny in human review of AI agent code. arXiv:2606.22721.

**Identifier:** arXiv:2606.22721 · **Read depth:** full_text (arXiv v1, 21 Jun 2026, five pages in ACM two-column format; pagination below is that PDF's, pp. 1–5) · **Source-tier:** preprint (the bib entry is typed `@misc`) · **Evidence basis:** direct_read · **Design and sample:** observational, longitudinal within-reviewer analysis of GitHub review logs from the AIDev dataset; 400 repeat reviewers (10 or more agent pull requests each) and 11,429 reviews over a seven-month window, plus a human-PR comparison of 11,415 reviews by 1,851 reviewers · **Parties modeled:** person–system (a human reviewer and an AI coding agent's output) · **Facets:** G · **Read:** 2026-10-13

## What it argues

Yu and colleagues ask whether reviewers who accumulate experience with AI-agent pull requests (PRs) approve more and inspect less. They take AIDev, which holds 16,895 reviews by 2,494 reviewers across five agents, and keep the 400 reviewers with at least 10 agent PRs (median 17 reviews; p. 2). They compare each reviewer's early and late half and also pool reviews by the reviewer's own experience decile.

The headline numbers: approval rises from 30.1% to 36.8% between the early and late halves (+6.7 points; paired Wilcoxon p < 10^-6), and across experience deciles from 27.9% to 42.4% (+14.5 points; Table 1, p. 2). The change-request rate falls from 11.2% to 5.6% in the decile table (p. 2). At the individual level 52% of reviewers become more approving, 28% less, 20% unchanged (p. 2). Median review latency rises from 3.9 to 13.5 hours (p. 2), while inline comments per review fall from 1.01 to 0.79 (−22%, p = 0.0014) and comment words from 18.6 to 13.5 (p. 3). The shift in approval correlates with the drop in commenting (Spearman ρ = −0.556; p. 3). Three checks point to experience and to the agent: a per-reviewer logistic fit gives the experience term a mean coefficient of +0.11 and calendar time −0.007 (p. 4); median PR size stays flat (p. 4); and on human-authored PRs in the same repositories approval declines (29.1% by June) while agent-PR approval rises (41.7% by July; p. 3).

The authors read the pattern as "most consistent with reflexive habituation under growing workload rather than rational trust calibration alone" (abstract, p. 1). They also say flatly: "We cannot establish causality" (p. 1), and "Crucially, we lack a direct measure of agent code quality over time; if agents genuinely improved, rising approval would be rational rather than habituative" (p. 4). All four agents received updates during 2025 (p. 1). Per-agent shifts differ: Copilot +9.1 points (n = 241), Devin +3.8 (n = 95), Codex +1.8 (n = 51) and Cursor −1.4 (n = 18; Table 2, p. 3). The proxy cross-agent control is "underpowered" (p. 3).

## Relation to the argument

**Premise P12** ("people perform sustained monitoring and whole-volume review badly"). This is the closest piece of field data on the exact task the Nadella post leaves a person: reading agent output and deciding to let it through. It is observational and compatible with the reviewers learning that the agents got better, so it supports P12 as a pattern consistent with it, not as a measured failure. The map's own wording for P12 is "mixed for the rest", and this source stays in that group. Its distinct contribution is a time trend: more approval with fewer comments as exposure grows.

**Rulings D4 and D7.** The post puts a person at the end to read evidence and halt (P11). Yu gives one reason to doubt the durability of that seat. It does not test chain-of-thought evidence, and it says nothing of pilots; the aviation literature the D7 flag calls for is not cited here.

**Premise P10.** Reviewers and agent operators are not shown to have conflicting interests here. The source cannot speak to who holds a convention.

**Facet check:** the facet's numbers (400 reviewers, 11,429 reviews, 30.1% to 36.8%, latency 3.5 times, comments −22%) match the full text. The paper itself is less internally tidy than its abstract: the early-late change-request rates (11.2% to 5.6%) repeat the first-decile and tenth-decile figures of Table 1, the text says "28% less commenting" for words but 22% for comments (pp. 3–4), and Spearman ρ = +0.02 for PR size is given a p of 0.009 and called negligible (p. 4). I could not resolve these from the text.

## In conversation with

The reference list holds eleven software-engineering items; I matched none to `references.bib`. It does not cite Bainbridge (`bainbridge1983ironies`), Parasuraman, Green (`green2022flaws`) or any automation-complacency source, though its introduction says the effect "mirrors habituation effects documented in security auditing, aviation checklists, and automated-testing interactions" (p. 1; it cites Cassee et al. 2020 and Wessel et al. 2020 for this).

- Leads, not in the bib: Li, Zhang & Hassan (2025), the AIDev dataset (arXiv:2507.15003); Wessel et al. (2020) on code-review bots; Cassee et al. (2020) on CI and review; Bacchelli & Bird (2013) on code review expectations.

## Caution

A five-page preprint by independent researchers on public, popular repositories (more than 100 stars). The data are approval flags, not defects, and no outcome quality is measured. Approval, latency and comment counts are weak proxies for "scrutiny". The reviewer pool for the human-PR comparison thins out after June 2025 (n = 207 reviews in July). Use it as suggestive evidence that review volume and exposure go with lighter review, not as a measured decline in oversight.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the arXiv v1 PDF (5 pp.) and extracted it. Checked 5 verbatim quotations (all exact, correct page), about 40 numbers (400 reviewers, 11,429 reviews, 16,895 reviews by 2,494 reviewers, approval 30.1 to 36.8 and 27.9 to 42.4, change requests 11.2 to 5.6, 52/28/20%, latency 3.9 to 13.5 h, comments 1.01 to 0.79, words 18.6 to 13.5, rho -0.556, logistic coefficients +0.11 and -0.007, the human-PR comparison 29.1% and 41.7%, per-agent shifts and n, n = 207 in July, PR-size rho +0.02 with p 0.009) and the reference list (Cassee, Wessel, Bacchelli, Li et al.; no Bainbridge or Parasuraman).

**Findings:** No issues found. The card's three internal inconsistencies in the paper (early-late versus decile change-request rates, 28% versus 22% commenting, rho = +0.02 with p = 0.009 called negligible) are real and accurately reported. The 'repeat the first-decile and tenth-decile figures' observation about change-request rates is the card's inference; the text does give 11.2 and 5.6 in the decile table.
