# Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. In *Proceedings of the 31st USENIX Security Symposium* (pp. 2783–2800). USENIX Association.

**Identifier:** https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi (no DOI; ISBN 978-1-939133-31-1 printed on the title page) · **Read depth:** full_text (published open-access proceedings PDF, 19 PDF pages: cover plus printed pages 2783–2800 including references and appendices; locators below are the printed USENIX page numbers) · **Source-tier:** proceedings (peer-reviewed conference paper) · **Evidence basis:** direct_read · **Design and sample:** online survey of 20 SOC practitioners, then 21 semi-structured interviews with practitioners from seven SOCs (five managed-service providers, two in-house), thematic Template Analysis of 105,523 transcribed words; non-random recruitment, mostly UK · **Parties modeled:** person–system (analyst and detection tool), with the customer as a third party in the managed-service SOCs · **Facets:** G · **Read:** 2026-10-13

## What it argues

Alahmadi, Axon and Martinovic ask how analysts in security operations centres (SOCs) judge alarms and why they call so many of them false positives. The survey (n = 20) was a scoping step; the authors say they "cannot claim statistical significance" (p. 2786). Of the 20 respondents, 14 agreed and 2 disagreed that their tools "frequently produce false positive results" (assertion A-1), 12 agreed and 4 disagreed that alert counts are overwhelming (A-4), and 18 agreed and 2 disagreed that a human in the loop is needed because automated systems cannot do the detection and preliminary analysis alone (A-5) (Table 3, p. 2787). Forty-five percent received under 5,000 alerts a day; two respondents used machine-learning tools (p. 2788).

The interviews carry the argument. One lead analyst said "We know 99% of the alarms we generate are false positives, but we still have to look at them" (B3, p. 2790). The authors then split "false positive" into two kinds. A false alarm fires with no security event behind it. A benign trigger is a true match on a signature that the organisation chooses to ignore for a business reason, for example outdated Java versions across a client estate (pp. 2790–2791). They conclude the 99% "is found to be mostly benign triggers and not necessarily a measurement of the performance of the technology itself" (p. 2791).

Validation stays human work. Analysts decide whether an alarm is real from their knowledge of the network, the client's business and its working hours, and they also configure the rules and tune the baselines (pp. 2788–2790). Interviewees call commercial alarms "black-box" and distrust alarms that carry no reason: "if you don't tell me the reason you fire ... I can't have really high respect on that" (C5, p. 2792). Pressure runs toward over-reporting: managed-service analysts "are afraid not to raise" alarms to the customer, and they cannot act on the network themselves (D6, B4, p. 2789). The authors derive five properties for usable alarms (Reliable, Explainable, Analytical, Contextual, Transferable; the REACT model, p. 2794), and say analysts "should not trust the system completely" but need trust "calibrated using properly designed prediction explanations" (p. 2794).

The Target breach opens the paper: the malware alarm "was picked up by Target's Security Operation Center (SOC) 1 in Bangalore", escalated to Minneapolis, "ignored", and no action followed (pp. 2783–2784). The authors add that Target's staff had disabled the tool's ability to delete the file automatically (p. 2784).

## Relation to the argument

Premise P12 (people perform sustained monitoring and whole-volume review badly) and Nadella-lineage facet G, which lists this paper with Ancker et al. as alert-fatigue evidence. The paper supports the first half of that claim and not the second.

It supports the load. Analysts who must read alarms of mostly benign origin, and who are rated on tickets closed (a point the authors take from Sundaramurthy et al., p. 2784), describe the work as tedious. That fits the paper's worry about residual human tasks in the harness around a model.

It does not measure performance. The paper reports no accuracy, miss rate or vigilance decrement. "Burnout" and "desensitization" enter through the authors' framing and a citation to a clinical alarm-fatigue review (pp. 2783–2784, reference [12]); the interviews do not test them. The respondents also rate the human role as indispensable and better than the SIEM at connecting patterns (A-5, A-6; p. 2789). A reader of this card should not cite Alahmadi for "people do this badly"; the fair claim is "people do this at great volume, with unmeasured accuracy, and say they cannot be replaced".

Two details bear on the rulings. First, D3 and D4 (disclosure and transparency as literacy-based interventions): the analysts' complaint about black-box alarms is a demand for disclosed reasons, and the authors answer with explainable-AI design plus calibrated trust (p. 2794). That is a recommendation, not a test, and it sits on the literacy side of D3. Second, P11 (the person holds the brake): the Target account shows a human-held brake that was withheld by staff because false alarms had eroded trust in automatic action (p. 2784).

Facet check: facet G's summary matches the text (20 survey, 21 interviews, the 99% quote, benign triggers, Target, the abstract's "Alarm validation is a tedious task..."). The facet's own caution that 99% is "one analyst's figure" is correct: B3's statement; the survey's ten disclosed ratios were 1 real alert in 100 and 50 in 200 for two respondents, not a measured rate (p. 2788). I found no contradiction, but the facet's placement of the paper under "approval fatigue" evidence is looser than the text, which studies alarm validation, not approval.

## In conversation with

None of the paper's 48 references is in `../references.bib`. It cites Kokulu et al. 2019 (SOC issues; the authors contradict its finding that analysts do not see false positives as a problem, pp. 2784–2785), Sundaramurthy et al. 2014–2017 (SOC ethnography, burnout), Cvach 2012 (clinical alarm fatigue), Crowley and Pescatore 2019 (SANS SOC survey) and Goodall et al. 2004 (intrusion-detection work). It was written before the bib entries on alert fatigue, so it neither cites nor answers them:

- `ancker2017effects`, `layman2023controlled`, `tariq2025alert`: later or independent work on alert fatigue in clinical and SOC settings. The relation is topical; Alahmadi does not cite any of the three.

Leads from its list, not in the bib: Kokulu et al. (CCS 2019); Sundaramurthy et al., "A human capital model for mitigating security analyst burnout" (SOUPS 2015); Cvach, "Monitor alarm fatigue: an integrative review" (2012); Goodall et al., "The work of intrusion detection" (2004).

## Caution

Self-reported views of 21 practitioners from seven SOCs, mostly UK, recruited through institutional contacts and not at random; the authors say these limits prevent "generalizable conclusions" (p. 2795). The survey is unweighted and scoping only. No outcome data on detection or error. The "99%" is a quotation, not a rate. The paper concerns people reviewing rule-based alarms from security tools, not people supervising an AI agent's actions; any carry-over to agent oversight is the project's inference. The 2022 text predates the 2023–2026 alert-review and agent-oversight studies in facet G.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the USENIX PDF (title, authors, 2022, pp. 2783-2800 match); extracted layout and reading-order text. Checked all 16 quotations and about 25 numbers (Table 3 ratios A-1 2:14, A-4 4:12, A-5 2:18; 45% under 5K alerts; 105,523 words; 21 interviewees, seven SOCs; n=10 disclosed alert ratios; REACT properties; Target/Bangalore/Minneapolis; disabled auto-delete).

**Findings:** One quotation was not verbatim: the Target sentence omitted the source's '(SOC) 1' footnote marker; restored the exact words. Everything else matches. Page locators were checked against the printed page markers where the text supplied them; the p. 2788 locator for the n=10 ratios is plausible but the page break falls close by. Two bib keys named as topical only (layman2023controlled, tariq2025alert) were not opened; the claim that Alahmadi does not cite them holds against its reference list.
