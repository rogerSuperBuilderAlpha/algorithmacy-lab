# Ancker, J. S., Edwards, A., Nosal, S., Hauser, D., Mauer, E., Kaushal, R., & the HITEC Investigators. (2017). Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system. *BMC Medical Informatics and Decision Making, 17*, Article 36.

**Identifier:** doi:10.1186/s12911-017-0430-8 · **Read depth:** full_text (published open-access PDF; locators are the PDF's "Page n of 9"; reference list skimmed) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** retrospective cohort from electronic health record data, Jan 2010 to Jun 2013; 112 primary-care clinicians (93 physicians, 19 nurse practitioners) in a New York network of health centres; 1,266,325 best-practice advisories (BPAs, clinical reminders) and 326,203 drug alerts, from 430,803 encounters with 99,649 patients (p. 4) · **Parties modeled:** person–system (a clinician and the alerts an electronic record fires at them) · **Facets:** G · **Read:** 2026-10-13

## What it argues

Overrides are high ("49–96% of alerts are overridden," p. 1) and usually blamed on "alert fatigue," a term the authors call poorly defined. They test two readings. In cognitive overload, acceptance falls with more work, more complex work and more uninformative alerts. In desensitization, a new alert is accepted at first and then ignored (p. 2).

For overload they build unvalidated clinician-level markers: patients and encounters per year (amount of work); alerts per encounter and a comorbidity score (complexity); and the share of alerts repeated for the same patient within a year (a proxy for low information). They report incident rate ratios (IRR) from negative binomial models. For desensitization they follow 6 newly launched BPAs, with monthly acceptance for 46 clinicians (p. 3).

Results (pp. 4–6). Clinicians accepted a median 19.4% of BPAs and a median 0.0% of drug alerts (Table 1). About a quarter of BPAs (median 26.2%) and a third of drug alerts (median 31.8%) were within-patient repeats. For BPAs, acceptance fell 30% with each additional BPA per encounter (IRR 0.70, p<.001) and 10% with each five-point rise in the repeat share (IRR 0.90, p<.001). Patients and encounters per year showed no association (IRR 1.002 per 100 patients; 0.999 per 100 encounters). Comorbidity narrowly lost significance in the full model (IRR 0.49, p=.06). Drug-alert results were similar but weaker, from floor effects. After an override of a repeated alert's first instance, later ones were overridden 87.9% of the time for BPAs and 99.9% for drug alerts (p. 6). Only one of the 6 new BPAs, a flu reminder, showed an early peak and drop, probably from seasonality.

The authors conclude there was "no evidence of an effect of workload per se, or of desensitization over time for a newly deployed alert" (p. 1) and suggest cutting repeats. They add that "we cannot conclude definitively that reducing override rates would reduce rate of inappropriate overrides," since many overrides are appropriate (p. 8).

## Relation to the argument

The source sits under premise P12 (people monitor badly), where `ARGUMENT_MAP.md` lists "alert-review studies (Ancker; Alahmadi)." It shows one robust pattern: with more alerts per encounter and more repeats, acceptance drops. It touches P9 as well, since an alert is something handed to a person to read and accept rates are low.

It supports P12 less than the map implies. The measure is acceptance, and the authors cannot say which overrides were wrong. The setting is point-of-care alerts that interrupt a clinician's own task. The map itself says the evidence "does not cover after-the-fact reconstruction by trained auditors," which is what P15 of the Nadella post names, and Ancker does not either.

Facet check: facet G summarises the study as showing alert fatigue "is therefore more about repeated and uninformative alerts than raw volume." That overstates two things. The number of BPAs per encounter was a strong predictor (IRR 0.70), so alert volume per encounter did matter; what showed no effect was overall workload, measured by patients and encounters. And "uninformative" is a proxy: the authors measured repetition, not informativeness, and say so (p. 3). The facet's quotations from the abstract are accurate.

## In conversation with

- No work in `references.bib` is cited. The treatment of repeats as false alarms rests on human-factors refs [16–18] (p. 2): Rayo & Moffatt-Bruce on alarm management, Dixon, Wickens & McCarley on automation false alarms, and Endsley & Jones. The bib's `endsley1995out` is a different work.
- Leads not in the bib: van der Sijs et al. (ref. [7], the systematic review of override rates; ref. [15], the laboratory study); Embi & Leonard (ref. [19]) on alert response over time; Baseman et al. (ref. [22]) on message volume and recall; the companion papers from the same cohort (refs [29, 30]).

## Caution

An observational study in one network with one commercial record system and interruptive alerts; the authors say this may limit generality (p. 8). Acceptance is a behaviour, not a quality outcome. The markers are new and unvalidated, and the repeat proxy is an assumption. Median drug-alert acceptance was 0.0%, so those findings sit at a floor. Not evidence on log review, auditors, or language-model agents.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the published open-access PDF (9 pp., BMC Med Inform Decis Mak 17:36); page-wise extraction. Checked 6 quotations with pages and about 30 numbers (sample sizes 112/93/19, 1,266,325 BPAs, 326,203 drug alerts, 430,803 encounters, 99,649 patients; medians 19.4%, 26.2%, 31.8%; IRRs 0.70, 0.90, 1.002, 0.999, 0.49; 87.9% and 99.9%; 6 new BPAs, 46 clinicians; flu reminder), and the named references [16], [19], [22].

**Findings:** No issues found. The card's IRR units (per 100 patients, per 100 encounters) match the Table 2 footnotes. The 'Facet check' reading of the facet G summary is about project files, not the source, so I did not test it against the source.
