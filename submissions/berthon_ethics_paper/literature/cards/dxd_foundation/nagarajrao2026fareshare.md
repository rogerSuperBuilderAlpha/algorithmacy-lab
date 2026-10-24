# Nagaraj Rao, V., Dalal, S., Schwartz, A., Liaqat, A., Calacci, D., & Monroy-Hernández, A. (2026). FareShare: A tool for labor organizers to estimate lost wages and contest arbitrary AI and algorithmic deactivations. *Proceedings of the ACM on Human-Computer Interaction, 10*(2).

**Identifier:** doi:10.1145/3788052; arXiv:2505.08904 · **Read depth:** full_text of the **arXiv preprint v1** (cs.CY, 13 May 2025), 30 PDF pages: body pp. 1–22, references pp. 23–25, appendices pp. 25–30. Locators are the preprint's pages, not the journal's (the bib gives pp. 1–32); the version of record may differ. I skimmed Appendix A (Reddit and prior-study summary), the evaluation protocol in Appendix E and the SUS form · **Source-tier:** peer-reviewed article (read as preprint) · **Evidence basis:** direct_read · **Design and sample:** tool build with a field deployment and no comparison group. A 75-minute formative interview with two lead organizers and one lead attorney of the Washington rideshare union "DU" (Nov 2024, p. 8); a three-month deployment, 31 Dec 2024–31 Mar 2025 (p. 16); a March 2025 office visit with 7 field representatives running intake with 10 drivers, two focus groups and a usability scale from 2 attorneys (pp. 15, 27–28); field notes coded by two researchers (p. 16) · **Parties modeled:** two parties plus a third party (driver and platform, with a union as state-designated resolution centre and a tool that computes the claim) · **Facets:** J · **Read:** 2026-10-13

## What it argues

The authors call deactivation "one of the most severe forms of algorithmic control," one that "typically occurs through arbitrary AI and algorithmic decisions with little explanation or recourse" (abstract, p. 1). Washington's HB 2076 (2022) and Seattle's 2020 ordinance give drivers notice, an appeal and back pay: average daily earnings over the preceding 12 weeks plus 12% interest, or $200 a day if the platform fails to provide earnings or to accept those the resolution centre offers as evidence (p. 7). The union still assembled earnings from screenshots and spreadsheets. FareShare extends an open-source tool, FairFare, to pull trip history through a data provider (Argyle) after the driver consents, and it generates a PDF lost-wage report (pp. 12–14).

Results. There were 122 user sign-ups linking 178 accounts; 143 synced (Uber 78, Lyft 65) and 35 did not, a 20% failure rate (pp. 16–17). Intake sign-up took 2–3 minutes where screenshots had taken 20–25; report generation took about 2 minutes against 2–3 hours (p. 17). Two attorneys rated usability 75 and 82.5 on the SUS (p. 18). The tool removed transcription errors and added new problems: Uber location-mismatch warnings frightened drivers, research-consent text added friction, and attorneys "abandoned the tool for certain cases" after repeated sync failures (pp. 18–19). One said "when Uber data doesn't sync, it puts a damper on the whole case" (p. 19). Field staff kept screenshotting: "We still collect data the same way. But it helps the legal team a lot more" (p. 17). Attorneys also used the trip data to audit platform records, checking a disputed trip by its coordinates (p. 19).

## Relation to the argument

Facet J, Q6, and ruling D8 ("where the convention bends"). The paper documents a place where it bent toward the weaker party by statute: notice, an appeal, a state-designated representative and a numeric rule for the remedy. It adds that the new right needed machinery, since platforms "restrict data access by citing privacy and trade secret protections" (p. 4). It qualifies, in part, the premise that a platform's owner does as it likes: the law binds the owner in Washington and Seattle. The paper reports no case where a platform changed its own interface or rule. The 80% overturn rate (p. 7) comes from another study of Seattle drivers (ref. 37) and covers drivers who had representation; the authors measure no arbitration outcome with FareShare.

Facet check: facet J read only the abstract and wrote "178 signups". The body separates 122 users from 178 accounts (pp. 16–17); the abstract's "178 account signups" counts accounts. Facet J's "no outcome data" holds. Its line that the rights "need worker-side tools to be used" overstates: the union had won over 1,400 reactivations and about $3.5 million before the tool (pp. 7, 10), and FareShare automates one bottleneck.

## In conversation with

- `calacci2022bargaining` (ref. 7): tools that leave data collection to individual workers (p. 4).
- `irani2013turkopticon` (ref. 21): tools for workers to aggregate experience (p. 4).
- `cameron2024making` (ref. 10): workers' isolated conditions (p. 4).
- `rosenblat2016algorithmic` (ref. 36): platforms' "soft control" and information asymmetries (pp. 3, 21).
- Not in the bib: Calacci et al. (2025), FairFare, arXiv:2502.11273; Schwartz, Weber and Brown (2023) on Seattle deactivations; Jackson, Gillespie and Payette (2014), "The policy knot"; Khovanskaya et al. (2019).

## Caution

One union in one state, a short deployment, two attorneys on the usability scale, and a partner who is also the beneficiary. The headline "over 95%" is loose: 25 to 2.5 minutes is a 90% cut on its own, the paper says the tool "could" achieve it (pp. 2, 19), and field staff still screenshot (p. 17). Intake time appears as 25 minutes in some places and 20–25 in others, and the figures mix self-report and observation (Table 3, p. 15). The bib title carries a stray "CSCW016" (flagged in AUDIT_05). Driver views are out of scope (p. 22).

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the arXiv v1 PDF (31 text pages; the title page is p. 1). Searched all 12 quotations (the three non-matches are facet-J wording) and checked the numbers and locators: HB 2076 and Seattle 2020 dates, 12 weeks / 12% / $200 a day (p. 7), 80% overturn from ref. 37, 1,400 reactivations and $3.5m (p. 7), 122 sign-ups / 178 accounts / 143 synced (78 Uber, 65 Lyft) / 35 failed = 20% (pp. 16-17), 2-3 v 20-25 minutes, 2.5 minutes v 25 and the over-95% claim (p. 19), SUS 75 and 82.5 (p. 18), the 75-minute interview in Nov 2024 (p. 8), 7 field representatives and 10 drivers (Appendix D, p. 27), and the reference numbers 7, 10, 21, 36, 37 against the reference list.

**Findings:** No issues found. The Read depth line says Appendices A and E and the SUS form were skimmed; they are about 6 pages of 30, so I left full_text.
