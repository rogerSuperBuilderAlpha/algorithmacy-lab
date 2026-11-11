---
key: paleyes2023challenges
apa: "Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2023). Challenges in deploying machine learning: A survey of case studies. *ACM Computing Surveys*, 55(6), 1–29. https://doi.org/10.1145/3533378"
authors: "Paleyes, Andrei; Urma, Raoul-Gabriel; Lawrence, Neil D."
year: 2023
registered_year: 2022
title: "Challenges in Deploying Machine Learning: A Survey of Case Studies"
venue: "ACM Computing Surveys"
volume: "55"
issue: "6"
pages: "1–29"
doi: "10.1145/3533378"
url: ""
type: article
facets: [F8]
claims: [c1]
role: anchor
load: load-bearing
read_depth: partial
object_read: "arXiv v3 (arXiv:2011.09926v3 [cs.LG], 19 May 2022), typeset in the ACM CSUR template (running footer 'Vol. 1, No. 1, Article 1. Publication date: January 2022'; 29 pp.), NOT the ACM DL version of record that the triage expected; PDF and text layer paleyes2023challenges.pdf/.txt at ~/iit-playground/pt_ai_animation_local/pdfs/paleyes2023challenges/ (FETCH_LOG.tsv: route openalex_location_pdf, https://arxiv.org/pdf/2011.09926); read 2026-11-08; PARTS READ: PDF pp. 1-3 (abstract, §1, §2), 12-13 (§6.1 integration, §6.2 monitoring, start of §6.3), 20-22 (§8.2, §9, §10); NOT READ: §3-§5 (pp. 4-11), start of §6 (p. 11), §6.3 end to §8.1 (pp. 14-19), the references; sha256 d943c38c9a145e7db7455d3915e7ccf36fd81727228fd23c3d4125b58caebc68 (PDF, from sha256.txt; recomputed, matches)"
verified: corrected
verified_against: "crossref.json and openalex.json (authors, 55(6), 1-29, DOI, dates: online 2022-12-07, print 2023-07-31); sha256 recomputed; per-page pdftotext of arXiv v3, 11 quotations traced"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# A. Paleyes, R.-G. Urma and N. D. Lawrence (2023), Challenges in deploying machine learning

## What it argues

Andrei Paleyes, Raoul-Gabriel Urma and Neil Lawrence read published reports of putting machine-learning
models into production. They sort what the reports complain about by stage of a four-stage workflow (data
management, model learning, model verification, model deployment), then add cross-cutting concerns: ethics,
law, user trust, security. Their main claim is that "practitioners face challenges at each stage" of that
workflow, and they use the survey to ask academics to work on those problems. They take the workflow from
Ashmore et al. and stress that the stages overlap and feed back on one another.

For this paper the deployment stage matters most. In §6.1 the authors say that many software-engineering
ideas "are now being reinvented in the ML context". They send the reader to Sculley et al. for a "broad
selection" of ML engineering problems (glue code, pipeline jungles, configuration debt). They note that
researchers and engineers are not cleanly separated, because both end up working on the same code. In §6.2
they report that off-the-shelf monitoring tools often do not fit an ML system. In §8.2 they conclude that ML
projects differ fundamentally from ordinary software projects. The survey is about ML models in general, from
case studies "published in the last five years" before the survey (§1); it does not treat LLMs or agents.

## What the paper uses it for

- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the anchor for the deployment-gap
  half. It shows, in a peer-reviewed survey, that practitioners meet their hardest problems around the
  model: integration, monitoring, updating, data. The use stretches the source in four ways. (1) The survey
  scopes the infrastructure out ("lies out of scope of this work", §6.1), so it cannot support a claim about
  VMs or serving infrastructure. (2) Its unit is the trained model ("integration of the trained model"), so
  its vocabulary is model-first: the model is the thing deployed, the rest is what deployment needs. (3) It
  predates LLMs and harnesses. (4) The triage said this card would carry the sketch's Sculley sentence
  (that ML code is a small fraction of a real ML system). It does not. A search of the whole text layer for
  "fraction" and "small part" found nothing, and §6.1 only calls Sculley "a broad selection of engineering
  problems". Until Sculley et al. is promoted and read, the sentence stays unsupported.

## Loci

Locators: this arXiv v3 copy prints a running page number "1:N" in the ACM template; PDF page n carries
"1:n". The numbers are the preprint's, and the version of record may break pages differently. The text layer
shows ligatures (fi, fl, ff); I give them as plain letters. I matched every quotation against `pdftotext`
output for that PDF page of the held PDF (sha256 above). No quotation needed inner double quotation marks.

- "However, the deployment of machine learning models in production systems can present a number of issues and concerns." — PDF p. 1 (1:1), Abstract; matched against page text of paleyes2023challenges.pdf
- "The main contribution of our paper is to show that practitioners face challenges at each stage of the machine learning deployment workflow." — PDF p. 2 (1:2), §1; matched against page text of paleyes2023challenges.pdf
- "Model deployment, which is about integration of the trained model into the software infrastructure that is necessary to run it." — PDF p. 3 (1:3), §2; matched against page text of paleyes2023challenges.pdf
- "It is perfectly normal for these stages to run in parallel to a certain degree and inform each other via feedback loops." — PDF p. 3 (1:3), §2; matched against page text of paleyes2023challenges.pdf
- "While the former is a topic that belongs almost entirely in systems engineering and therefore lies out of scope of this work" — PDF p. 12 (1:12), §6.1; matched against page text of paleyes2023challenges.pdf
- "In fact, many concepts that are routinely used in software engineering are now being reinvented in the ML context." — PDF p. 12 (1:12), §6.1; matched against page text of paleyes2023challenges.pdf
- "A broad selection of engineering problems that machine learning practitioners now face is given in Sculley et al. [71]." — PDF p. 12 (1:12), §6.1; matched against page text of paleyes2023challenges.pdf
- "Others, such as glue code or pipeline jungles, stem from the general tendency in the field to develop general-purpose software packages." — PDF p. 12 (1:12), §6.1; matched against page text of paleyes2023challenges.pdf
- "On the surface there seems to be a clear separation of responsibilities: researchers produce the model while engineers build the infrastructure to run it." — PDF p. 12 (1:12), §6.1; matched against page text of paleyes2023challenges.pdf
- "the final ML solutions are usually so sensitive to a problem’s specifics that out-of-the-box tooling does not fit their needs well." — PDF p. 13 (1:13), §6.2; matched against page text of paleyes2023challenges.pdf
- "ML projects are fundamentally different from traditional software engineering projects." — PDF p. 20 (1:20), §8.2; matched against page text of paleyes2023challenges.pdf

## Caution

- **Version.** The held file is the arXiv v3 preprint, not the ACM DL PDF named in DECISIONS (row for this
  key, "open (hybrid): ACM DL PDF"). Its footer says "Vol. 1, No. 1, Article 1 ... January 2022", while
  Crossref gives volume 55, issue 6 and pages 1-29. The S6 verifier or S8 DOI check should confirm the
  volume, issue and page range against Crossref and, if Roger can open it, against the version of record.
  Page locators above are the preprint's.
- **Year (record correction, applied).** DECISIONS says the key takes the volume year and sets
  `registered_year: 2022`. Crossref: published online 2022-12-07, print 2023-07-31. FACETS writes 2022; the
  card cites 2023 and records 2022.
- **Sculley sentence.** See the c1 bullet. The sketch's claim about the share of ML code is not in the text I
  searched. If the paper needs it, it needs Sculley et al. (2015) itself.
- **Read depth.** `partial`. I did not read the sections on data, learning, verification and the
  cross-cutting concerns (§3-§5, §7). The paper should not cite the survey for them from this card.
- **Scope.** Case studies are drawn from papers "published in the last five years" before the survey (§1, p.
  2), with a few exceptions; no LLM deployment is covered.
- **What the paper may not claim from it:** that Paleyes et al. study harnesses, VMs or efficiency work as
  parts of an AI, or that they say ML code is a small fraction of an ML system.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 3
- verdict: corrected. Frontmatter matches Crossref (year 2023 volume year, registered_year 2022); all 11 quotations verbatim on the stated preprint pages; version caveat is accurate (arXiv:2011.09926v3, 19 May 2022, footer "Vol. 1, No. 1, Article 1. Publication date: January 2022"); the Sculley "small fraction" sentence is indeed absent.
- checked: frontmatter against crossref.json and openalex.json; sha256; each quotation by per-page pdftotext; arXiv stamp and footer on p. 1; searches for "fraction", "small part", "small portion", "tiny" (no hits outside unrelated text); Ashmore attribution; "reinvented" and the researchers/engineers passage; the five-year scope sentence on p. 2.
- changed: What it argues: "case studies of roughly the five years before 2020" was not what the text says; it says papers "published in the last five years" (p. 2, §1), and the held version is from 2022. Reworded to quote the source.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 11/11 loci found in paleyes2023challenges.txt, each on the stated PDF page (1, 2, 3, 3, 12, 12, 12, 12, 12, 13, 20); frontmatter against crossref.json and openalex.json (Paleyes, Urma, Lawrence; *ACM Computing Surveys* 55(6), 1–29; online 2022-12-07, print 2023-07-31; DOI; hybrid OA); registered_year 2022 follows the DECISIONS rule; PDF sha256 recomputed, matches sha256.txt; 29 pages; the p. 1 stamp reads 'arXiv:2011.09926v3 [cs.LG] 19 May 2022'. read_depth partial lists the parts read. The c1 bullet names four stretches, including that the Sculley 'small fraction' sentence is absent (I also found no 'fraction' or 'small part' in the text layer).
- Changed: nothing.
- For the author: status 'cited' rests on DECISIONS line 87, which routes SKETCH's Sculley sentence through this card. The card shows the sentence is not in Paleyes et al. Either promote Sculley et al. (2015) and read it, or drop the sentence; as it stands the SKETCH claim has no source in the library.
