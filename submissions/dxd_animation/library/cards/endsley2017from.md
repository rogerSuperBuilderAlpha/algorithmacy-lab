---
key: endsley2017from
apa: "Endsley, M. R. (2017). From here to autonomy: Lessons learned from human–automation research. *Human Factors*, *59*(1), 5–27. https://doi.org/10.1177/0018720816681350"
authors: "Endsley, Mica R."
year: 2017
registered_year: 2016
title: "From Here to Autonomy: Lessons Learned From Human–Automation Research"
venue: "Human Factors"
volume: "59"
issue: "1"
pages: "5–27"
doi: "10.1177/0018720816681350"
url: ""
type: article
facets: [F8]
claims: [c3]
role: support
load: load-bearing
read_depth: full_text
object_read: "Lab-held PDF of the typeset article (Human Factors 59(1), February 2017, pp. 5–27, copyright line 2016 HFES; received 5 Apr 2016, accepted 26 Oct 2016); PDF page = journal page minus 4; local folder ~/iit-playground/dxd_animation_local/pdfs/endsley2017from/ (Endsley 2017 - From here to autonomy.pdf, endsley2017from.txt, provenance.txt); copied 2026-11-05 from the lab-held path ~/iit-playground/pyphi-experiments/spaces/notebook_sources/B_theory/ (provenance.txt; no web URL, original provenance per the spaces repo); read 2026-11-05; sha256 99a2ad6277ec1110c85956de36caae49a8d3c416b64431f9597a5a78dd683f95"
verified: corrected
verified_against: "endsley2017from.txt (text layer of the lab-held PDF, journal pp. 5–27, read for all loci and summary claims); printed title page (vol., issue, pages, DOI, copyright) and received/accepted dates on p. 27; provenance.txt; no crossref.json or openalex.json in the folder; sha256 of the PDF recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Endsley, writing in the "At the Forefront of HF/E" section of *Human Factors*, draws on about forty years of human–automation research to say what it implies for autonomous and semi-autonomous systems. Her central claim is the "automation conundrum": the more autonomy is added, and the more reliable and robust it is, the less situation awareness (SA) the human operator keeps and the less able the operator is to take over manual control when needed. She gives three causes of this out-of-the-loop (OOTL) problem: how information is presented, operator monitoring, vigilance and trust, and engagement (passive monitoring produces weaker understanding than active control).

She integrates these into the human–autonomy system oversight (HASO) model (Fig. 1). In it, system reliability and robustness, the automation interface and the "automation interaction paradigm" (level of automation, adaptive automation, and granularity of control) shape the operator's attention, SA and workload. She reviews levels-of-automation research by task stage (Table 1), finds that automation of decisions and continuous control hurts OOTL performance and SA more than automation that supports SA, lists 20 design guidelines (Table 2), and sets research needs for fully autonomous systems: validating learning software, consistency across learning systems, and transparency of learning systems. A late section adds a "concept of operations" (COO) view, where the human supervises, or the human and autonomy act as teammates (with shared SA), or the automation oversees and limits the human. She calls the COO a fourth automation paradigm that "needs substantially more research" (p. 22).

On the unit of analysis: the model's central case is a human supervisory controller overseeing one automated system. Teammates, several autonomous systems, and even several humans (pilot of a manned aircraft, car passenger) appear, but as extensions. Designers and developers appear as the people who set the paradigms and who "give scant attention" to them, not as a party with interests of their own.

## What the paper uses it for

- **c3 (support).** Triage chose Endsley (replacing Hollnagel and Woods) as the recent canonical statement of the human–automation dyad: a human operator and an autonomous system. The card supports that reading for the main model. It also gives the paper material that qualifies it. First, Endsley's teaming section adds parties, but they share a goal: shared SA "is fundamental to supporting coordinated actions across multiple parties who are involved in achieving the same goal" (p. 23). Second, one listed COO is "automation that oversees and acts as a limit on human performance" (p. 22), which puts a rule-setter in the picture without naming an interested party behind it. Third, she says designers can intentionally remove information (p. 7). That is opacity by design, but she treats it as a design fault, not as co-optation. The paper can cite her for the dyad as the standard unit and for the opacity of learning systems (pp. 21–22). It cannot cite her for the claim that HF has no multi-party model, and it should not say she shows a third party with interests.

## Loci

Quotation marks inside quotations are single, as printed. Locators are the journal pages printed in the article (pp. 5–27); the PDF page is the journal page minus 4. Each quotation was matched against endsley2017from.txt, the text layer of the lab-held PDF.

- "From Here to Autonomy: Lessons Learned From Human–Automation Research" — p. 5, title page; matched against endsley2017from.txt (the full subtitle comes from here; the triage note F7-F8.md says Crossref and OpenAlex give only "From Here to Autonomy", but the local folder holds no crossref.json or openalex.json, so that is unchecked here; the PDF's own running head also reads "From Here to Autonomy").
- "An automation conundrum exists in which as more autonomy is added to a system, and its reliability and robustness increase, the lower the situation awareness of human operators and the less likely that they will be able to take over manual control when needed." — p. 5, abstract; matched against endsley2017from.txt.
- "most autonomous systems must still interact with humans who serve as supervisory controllers, responsible for directing and overseeing their performance, or as teammates who need to collaborate with them" — p. 5, introduction; matched against endsley2017from.txt.
- "These interface-related failures include cases where intentional design decisions are made to remove needed information as well as unintentional deletions." — p. 7, section "Automation Information Presentation"; matched against endsley2017from.txt.
- "Often system developers give scant attention to these design decisions" — p. 10, section "The Automation Interaction Paradigm: Autonomous but Not Alone"; matched against endsley2017from.txt.
- "GOC is a third major automation paradigm shown in the HASO model that is under the control of automation designers." — p. 17, section "GOC" (GOC = granularity of control); matched against endsley2017from.txt.
- "The actual logic and lessons ‘learned’ by neural networks and deep learning software are typically opaque not only to the human operator but also to software developers" — pp. 21–22, section "Transparency of Learning Systems" (the sentence crosses the page break; the source puts 'learned' in double quotes, converted to single); matched against endsley2017from.txt.
- "Automation that oversees and acts as a limit on human performance" — p. 22, list of potential concepts of operation (COOs); matched against endsley2017from.txt.
- "Shared SA is fundamental to supporting coordinated actions across multiple parties who are involved in achieving the same goal and who have interrelated functions" — p. 23, section "Human–Autonomy Teams"; matched against endsley2017from.txt.

## Caution

- Year: print February 2017, volume 59(1), as the title page prints it (p. 5). The online date 2016-12-15 and `registered_year: 2016` come from triage F7-F8.md and DECISIONS, not from a registry record: the local folder holds no crossref.json or openalex.json, so both are unchecked. The card takes the volume year 2017. The copyright line reads 2016; the article was received 5 April 2016 and accepted 26 October 2016.
- Not the 2017 Endsley paper on autonomous driving (`endsley-2017-autonomous-driving-preliminary-naturalistic`, dial; 10.1177/1555343417695197), a different work.
- Subtitle: the triage file took it from the PDF's file name and memory, and said the card must take it from the title page. It reads "Lessons Learned From Human–Automation Research" on p. 5, so the APA string uses it (sentence case in the APA reference, title case in the `title` field as printed).
- The abstract and the triage note call the model "human–autonomy systems oversight model" (with an s). The body names it "human–autonomy system oversight (HASO) model" (p. 8). I use the body's wording; the paper should too.
- The copy matches a publisher-typeset article (journal header, page numbers 5–27, HFES copyright, received and accepted dates). I could not check it against the version of record online; the S4 version check is for the author or the verifier.
- Endsley treats "autonomy" and "automation" as synonyms for the purposes of the article (p. 6), so a "dyad" here is operator and automated or autonomous system.
- She mentions trust definitions from Lee and See (2004); that work is not carded here.

## Verification

2026-11-05 · S6 verifier, batch b05 (opus; not the writer) · verdict: corrected · checked: loci 9/9 found in endsley2017from.txt (two-column layout; each sentence rebuilt from its column), pages confirmed against the printed page headers (PDF page = journal page minus 4) and section labels confirmed; author, title with subtitle, Human Factors 59(1), February 2017, pp. 5–27, DOI 10.1177/0018720816681350 and the 2016 HFES copyright checked against the printed title page; received 5 April 2016 and accepted 26 October 2016 confirmed on p. 27; no Crossref or OpenAlex record is in the folder, so the registry metadata could not be checked; summary claims confirmed (three OOTL mechanisms p. 6, HASO p. 8, 20 guidelines in Table 2, three COOs p. 22, synonym use p. 6); full_text depth honest; sha256 99a2ad62… recomputed and matches provenance.txt · changed: (1) "What it argues" said the teaming case needs "substantially more research"; the source says it of the COO as a fourth automation paradigm (p. 22), and the sentence now says that; (2) the online date 2016-12-15, `registered_year: 2016` and the claim that Crossref/OpenAlex give only "From Here to Autonomy" are now marked as coming from triage, unchecked against a local record. Still open: the version-of-record check (S4)
