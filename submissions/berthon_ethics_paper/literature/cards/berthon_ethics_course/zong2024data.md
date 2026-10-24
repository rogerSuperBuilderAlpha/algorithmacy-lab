---
citekey: zong2024data
title: "Data Refusal from Below: A Framework for Understanding, Evaluating, and Envisioning Refusal as Design"
authors: Zong, Jonathan and Matias, J. Nathan
year: 2024
type: article
doi: 10.1145/3630107
venue: ACM Journal on Responsible Computing 1(1), Article 10, 23 pages (March 2024); Crossref pages 1-23; CC BY 4.0
source_basis: full-text
pages_read: "10:1-10:19 (all body text: abstract, sections 1-6, acknowledgments); reference list skimmed"
source_url: https://hdl.handle.net/1721.1/152919
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C3_scholarly/zong2024matias.pdf
sha256: 3452b3409c4a1fd8bfa0ddf4fe80ce6de7baf4f9551fed6f3774b1238781e4ea
manuscript_lines: [205]
ledger_rows: [P6-004]
verified: true
written: 2026-10-14
---

**Key.** `references.bib` has no entry for this work (P6 reference check, `P6.md:147`). I made the key
`zong2024data` in the form `surnameYEARfirstword`. I read the text in the extraction
`C3_scholarly/zong2024matias.txt` (sha256 985a356b7986533fcc235cc39dce0e38a698bdfe5c4cfbd3ae6b0f25529c8580) of
the MIT Open Access copy of the final published version.

## Summary
Zong and Matias offer a framework for "data refusal from below", written "from the standpoint of people who
refuse, rather than the institutions that seek their compliance" (abstract, 10:1). They define refusal as
"saying 'no' to how data are collected or used" (10:1). Their central claim is that "refusal itself [is] a form
of design": refusers design "social artifacts" that challenge existing relations (10:5-10:6). Every act of
refusal has four facets (10:7-10:16). Autonomy can be individual or collective, time reactive or proactive,
power can foreclose or create possibility, and cost can be accepted or redistributed. Each facet is shown
through cases, including GDPR-style consent tools, IBM's Diversity in Faces dataset, facial-recognition bans,
First Nations OCAP principles, Vertesi's "digital homesteading" and CBP face scans. The authors warn that
opt-outs offered by data collectors often "placate instead of create change" (10:12-10:13). Citing Benjamin,
they hold that "it is coercive to say one has a choice, when one of those choices is automatically penalized"
(10:15). They close with lessons for designers and a call, after Benjamin, to "institutionalize refusal"
(10:17-10:19). Their focus is North American (10:2).

## Key facts it relies on
- Standpoint: "writing from the standpoint of people who refuse, rather than the institutions that seek their
  compliance" (abstract, 10:1). The authors criticize scholarship that "has largely focused on actions that
  designers and policymakers can take" (10:2).
- Refusal as design: "Because refusal involves deliberate acts to influence socio-technical systems of power, we
  see refusal itself as a form of design" (10:5).
- Designed consent: feminist HCI researchers hold that for data collectors to support autonomy, affirmative consent
  "must be voluntary, informed, revertible, specific, and unburdensome" (10:8).
- Placating offers: "data collectors often use these pathways of dissent to limit refusers' agency". Facial
  recognition opt-outs "do not provide the option of challenging or constraining companies' power" (10:12-10:13).
- Burdensome removal: IBM "can create a reasonable-sounding procedure that is nearly impossible to opt out of"
  (10:10).
- Cost: "even small costs can make people less likely to opt out of data collection" (citing Athey et al.; 10:14).
- Penalty: "it is coercive to say one has a choice, when one of those choices is automatically penalized" (quoting
  Benjamin 2016; 10:15). Their example is CBP face-scan opt-outs, which route travelers into extra screening
  (10:15).
- Institutions: collective organizing can push institutions to "actively and genuinely support the choice to refuse
  participation" (quoting Benjamin; 10:19).
- Limits they state: a North American focus (10:2), cases "not meant to be an exhaustive representation" (10:7),
  and generative power that "falls short of the ideal" (10:16).

## Critical notes from the literature
- Facet N5 (`literature/facets/N5_prior_work_gap.md:185`): a human alternative is not new. The OSTP Blueprint's
  "human alternatives, consideration, and fallback" (via Burrell 2024) and Bhargava and Assadi (2024) on hiring
  already state it. N5 found no work that states the alternative as a duty with a no-penalty condition. Zong and
  Matias come close through Benjamin's quotation (10:15), but they describe it rather than derive it as an
  operator's duty.
- Ledger P6-004 (`review/v3/ledger_parts/P6.md:14, 155`) rated the manuscript's sentence "unsupported" at abstract
  depth and asked whether the paper says anything about penalties for refusing. It does (10:14-10:15).
- The paper's scope is refusing data collection and data use. It does not address refusing an automated decision
  at a gate such as hiring or credit, which is the manuscript's case.
- I opened no published critique of this article. The arm's record has none.

## Key topics covered
data refusal, refusal from below, feminist standpoint theory, refusal as design, autonomy (individual, collective, relational), reactive vs proactive refusal, power, cost of refusal, opt-out and consent design, data cooperatives and trusts, Indigenous data sovereignty (OCAP), facial recognition, institutionalized refusal

## Where the manuscript uses it
- Line 205: "Zong and Matias (2024) treat refusal as something a system can be designed to honor". The manuscript
  takes from the paper an antecedent for structural refusal, a route that the system itself keeps open. **narrower**.
  The paper's thesis runs the other way: refusers are the designers, and the paper is written "from below", against
  work centered on what designers do (10:2, 10:5). It does discuss consent and opt-out mechanisms that data
  collectors can design (10:8), and it calls for institutions that "actively and genuinely support the choice to
  refuse participation" (10:19). But it warns that collector-designed opt-outs often placate (10:12-10:13). A
  closer paraphrase would be "treat refusal as design, and warn that opt-outs designed by data collectors can
  placate rather than protect".
- Line 205, the no-penalty element of structural refusal ("attach no penalty to taking it"). The sentence does not
  cite the paper for this, but the paper supports it: "it is coercive to say one has a choice, when one of those
  choices is automatically penalized" (Benjamin 2016, quoted at 10:15). It also notes that small costs deter
  opt-outs (10:14). **holds** as available support that is not used. Cite Benjamin (2016) as the source of the
  words, via Zong and Matias.
- Reference entry (line 411): authors, title, journal, volume, issue and DOI match Crossref and the article. ACM
  gives the article number (Article 10, 23 pages) rather than page numbers, and its pages print as 10:1-10:23.
  The entry's "1-23" follows Crossref. **holds**, but APA style for ACM journals would give "Article 10".

## Verifier notes
- Opened `zong2024matias.pdf` (sha256 of the extraction also matches); PDF p. n = 10:(n-1) confirmed from running folios. Crossref: Zong and Matias, *ACM J. Responsible Computing* 1(1), pages 1-23, online 2024-03-20; CC BY 4.0 on the PDF.
- Key facts exact at the locators given: 10:1 standpoint and "saying “no” to how data are collected or used"; 10:2 designers-and-policymakers critique and North American focus; 10:5 refusal as design; 10:8 consent criteria; 10:10 IBM; 10:12-10:13 placating offers; 10:14 small costs; 10:15 Benjamin's "coercive" sentence; 10:19 "actively and genuinely support".
- Verdicts confirmed: line 205 narrower (the paper writes from below and warns that collector-designed opt-outs placate); the no-penalty support at 10:15 exists but is not cited.
- Bib: `references.bib` has no entry for this work. Manuscript entry agrees with Crossref; ACM numbers the article as 10. Date 2026-10-14.
