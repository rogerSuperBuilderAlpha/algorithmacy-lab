# Codebook — cohort algorithmacy panel

Every variable, its items, the response scale, the reverse key, and the scoring rule. This is the
canonical source; the fielded forms in [`instruments/`](instruments/) and the platform implementation in
the program repository render exactly these items. An item marked **(R)** is reverse-scored before a
scale mean is taken. Item ids are stable across waves so the panel links cleanly.

## Response scales

- **A7** — 7-point agreement: 1 = Strongly disagree, 2 = Disagree, 3 = Somewhat disagree, 4 = Neither
  agree nor disagree, 5 = Somewhat agree, 6 = Agree, 7 = Strongly agree.
- **A5** — 5-point agreement (used for the transactive-memory items, faithful to Lewis 2003): 1 =
  Strongly disagree … 5 = Strongly agree.
- **F7** — 7-point frequency for behavioral self-report: 1 = Never, 4 = Sometimes, 7 = Always.
- **CAT** — categorical single-select (options listed with the item).
- **TEXT** — free response.

Scale scores are the mean of their items after reverse-scoring, computed when at least 75% of a scale's
items are answered. Higher means more of the named construct unless noted.

---

## Algorithmacy Competence Scale (ACS) — purpose-built · scale A7 · all waves

Twelve items, three facets of four. Score each facet and a 12-item total.

### Counterpart inference (ACS-CI) — reconstructing a hidden counterpart's wants from outcomes
- `acs_ci_1` — I can usually work out what reviewers want from the feedback they leave, even when they do not spell it out.
- `acs_ci_2` — When a tool or system gives me a result, I can reason back to what it was checking for.
- `acs_ci_3` — I form accurate expectations about what will pass review before I submit.
- `acs_ci_4` — I read past the surface of automated feedback to the rule behind it.

### Signal compression (ACS-SC) — compressing intent into the few signals the system accepts
- `acs_sc_1` — I am good at expressing what I mean in the narrow format a tool or reviewer will accept.
- `acs_sc_2` — I can reduce a complex piece of work to the few signals that decide whether it is accepted.
- `acs_sc_3` — When a system accepts only certain inputs, I can package what I intend to fit them.
- `acs_sc_4` — I know which parts of my work to make visible so the system or reviewer reads it correctly.

### Rule-change tracking (ACS-RT) — tracking rule changes the system makes without announcement
- `acs_rt_1` — I notice when the rules of a tool or process have quietly changed.
- `acs_rt_2` — I keep track of how requirements shift over time, even when no one announces it.
- `acs_rt_3` — I adjust quickly when a system starts behaving differently than before.
- `acs_rt_4` — I can tell when what worked last time will no longer work.

---

## Perceived task interdependence (TI) — reciprocal · scale A7 · all waves
Adapted from Pearce & Gregersen (1991) and Van der Vegt, Emans, & Van de Vliert (2001).
- `ti_1` — I have to work closely with other members of the cohort to get my work done.
- `ti_2` — My work depends on the work of others in the cohort, and theirs depends on mine.
- `ti_3` — Members of the cohort rely on one another for information and materials.
- `ti_4` — I cannot complete my work well without input from others in the cohort.
- `ti_5` — How I do my work directly affects others, and how they do theirs affects me.

---

## Perceived system authority — commit vs. convey (SA) · scale A7 · W2, W3
Purpose-built, anchored in Lee (2018). The "system" is the platforms and the review-and-vote gate the
cohort coordinates through. Higher = the system commits a determination (rather than conveying a signal).
- `sa_1` — The platform and review process here decide outcomes, not just pass information along.
- `sa_2` — When the system produces a result, it stands, and people act on it as settled.
- `sa_3` — The tools we coordinate through only relay what people have already decided. **(R)**
- `sa_4` — The review-and-vote process commits a decision that no individual could reach alone.
- `sa_5` — The system only carries our messages; the real decisions are made directly between people. **(R)**
- `sa_6` — What the platform determines binds everyone, whether or not they agree.

---

## Job autonomy (AU) · scale A7 · all waves
Breaugh (1985) work-autonomy scales, three facets of three.
### Method autonomy (AU-M)
- `au_m_1` — I decide how to go about getting my work done.
- `au_m_2` — I choose the procedures I use to carry out my work.
- `au_m_3` — I am free to choose the methods I use in my work.
### Scheduling autonomy (AU-S)
- `au_s_1` — I control the scheduling of my work.
- `au_s_2` — I have control over the sequencing of my work activities.
- `au_s_3` — I decide when to do particular work activities.
### Criteria autonomy (AU-C)
- `au_c_1` — I have some control over what I am supposed to accomplish.
- `au_c_2` — I am able to modify the objectives of my work.
- `au_c_3` — I am able to influence the standards by which my work is judged.

---

## Psychological ownership (PO) · scale A7 · W2, W3
Adapted from Van Dyne & Pierce (2004); target is the platform or project the participant builds.
- `po_1` — I feel a high degree of personal ownership of the work I build in this cohort.
- `po_2` — I sense that the project I build is mine.
- `po_3` — This is MY platform.
- `po_4` — I feel the work I build here is mine to look after.
- `po_5` — It is hard for me to think of the project as mine. **(R)**
- `po_6` — I invest a great deal of myself in what I build here.

---

## Transactive memory system (TMS) · scale A5 · W2, W3
Lewis (2003), three subscales of five, kept at the original 5-point anchors.
### Specialization (TMS-S)
- `tms_s_1` — Each cohort member has specialized knowledge of some aspect of our work.
- `tms_s_2` — I have knowledge about an aspect of the work that no other member has.
- `tms_s_3` — Different members are responsible for expertise in different areas.
- `tms_s_4` — The specialized knowledge of several different members is needed to finish our projects.
- `tms_s_5` — I know which members have expertise in specific areas.
### Credibility (TMS-C)
- `tms_c_1` — I am comfortable accepting procedural suggestions from other members.
- `tms_c_2` — I trust that other members' knowledge about the work is credible.
- `tms_c_3` — I am confident relying on the information other members bring.
- `tms_c_4` — When other members give information, I want to double-check it. **(R)**
- `tms_c_5` — I do not have much faith in other members' expertise. **(R)**
### Coordination (TMS-Co)
- `tms_co_1` — Our cohort works together in a well-coordinated way.
- `tms_co_2` — Our cohort has few misunderstandings about what to do.
- `tms_co_3` — Our cohort has to backtrack and start over a lot. **(R)**
- `tms_co_4` — We accomplish tasks smoothly and efficiently.
- `tms_co_5` — There is much confusion about how we will accomplish tasks. **(R)**

---

## Perceived substitutability (SU) · scale A7 · all waves
Purpose-built, exploratory; written to the catalog's substitutability prior. Higher = more substitutable
(less pivotal).
- `su_1` — If I dropped out, the cohort's work would carry on largely unchanged.
- `su_2` — Someone else could easily do the part I play here.
- `su_3` — My specific contribution would be hard to replace. **(R)**
- `su_4` — The coordination here does not really depend on me in particular.

---

## General self-efficacy (SE) · scale A7 · W1, W3
New General Self-Efficacy Scale (Chen, Gully, & Eden, 2001). Discriminant covariate.
- `se_1` — I will be able to achieve most of the goals I set for myself.
- `se_2` — When facing difficult tasks, I am certain I will accomplish them.
- `se_3` — In general, I think I can obtain outcomes that are important to me.
- `se_4` — I believe I can succeed at most any endeavor I set my mind to.
- `se_5` — I will be able to overcome many challenges successfully.
- `se_6` — I am confident I can perform effectively on many different tasks.
- `se_7` — Compared with other people, I can do most tasks very well.
- `se_8` — Even when things are tough, I can perform quite well.

---

## Sense of belonging (BE) · scale A7 · all waves
Adapted from Walton & Cohen (2007). Covariate.
- `be_1` — I feel like I belong in this cohort.
- `be_2` — I feel like an outsider in this cohort. **(R)**
- `be_3` — I fit in well with the people in this cohort.
- `be_4` — People in this cohort accept me.

---

## Demographics and background (DEM) · W1 only
All optional, each with "Prefer not to say."
- `dem_age` — Age range. **CAT**: 18–24 / 25–34 / 35–44 / 45+ / Prefer not to say.
- `dem_gender` — Gender. **CAT**: Woman / Man / Non-binary / Self-describe (TEXT) / Prefer not to say.
- `dem_education` — Highest level of education completed. **CAT**: Secondary / Some college / Bachelor's /
  Master's / Doctoral / Other.
- `dem_coding_years` — Years of programming experience. **CAT**: <1 / 1–2 / 3–5 / 6–10 / >10.
- `dem_platform_work` — Have you worked through an online platform or gig app (e.g., rideshare, delivery,
  freelance marketplace)? **CAT**: Yes / No / Prefer not to say.
- `dem_platform_kind` — If yes, which kind(s)? **TEXT** (shown only if `dem_platform_work` = Yes).
- `dem_region` — Region of residence. **CAT** (continental list) + Prefer not to say.

---

## Program experience and open response (EXP) · W3 only
### Perceived learning (EXP-L) · scale A7
- `exp_l_1` — I learned a great deal in this program.
- `exp_l_2` — My ability to coordinate through tools and systems improved over the program.
- `exp_l_3` — I am better at reading what a system or reviewer wants than I was at the start.
### Open response (TEXT)
- `exp_open_1` — Describe a time you worked out what a system or reviewer wanted without being told directly.
- `exp_open_2` — How did the way you read the cohort's tools and review process change over the program?
- `exp_open_3` — Anything else about coordinating through the platforms you want to add?

---

## Derived variables
- `ACS_CI`, `ACS_SC`, `ACS_RT` — facet means (A7); `ACS_TOTAL` — 12-item mean.
- `TI`, `SA`, `PO`, `SU`, `SE`, `BE`, `EXP_L` — scale means.
- `AU_M`, `AU_S`, `AU_C`, `AU_TOTAL` — autonomy facet and total means.
- `TMS_S`, `TMS_C`, `TMS_Co`, `TMS_TOTAL` — TMS subscale and total means (A5).
- `wave` ∈ {1, 2, 3}; `pid` — one-way hash linking a participant's waves.
- `consent_version`, `completed_at` — per response.

## Notes on deviations
- TMS keeps Lewis's 5-point anchors; all other multi-item scales use 7-point agreement. The mixed anchors
  are recorded here so a re-analysis treats TMS on its own metric.
- The autonomy criteria facet (`AU-C`) is expected to run low in this setting, since program objectives
  and assessment standards are largely fixed. That is substantive, not a measurement fault, and is read
  as such.
