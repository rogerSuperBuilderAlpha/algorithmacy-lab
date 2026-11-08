---
key: zednik2021solving
apa: "Zednik, C. (2021). Solving the black box problem: A normative framework for explainable artificial intelligence. *Philosophy & Technology*, 34(2), 265–288. https://doi.org/10.1007/s13347-019-00382-7"
authors: "Zednik, Carlos"
year: 2021
registered_year: 2019
title: "Solving the Black Box Problem: A Normative Framework for Explainable Artificial Intelligence"
venue: "Philosophy & Technology"
volume: "34"
issue: "2"
pages: "265–288"
doi: "10.1007/s13347-019-00382-7"
url: ""
type: article
facets: [F12]
claims: [c7]
role: support
load: load-bearing
read_depth: partial
object_read: "Author preprint, arXiv 1903.04361 (FETCH_LOG.tsv: route arxiv_preprint, https://arxiv.org/pdf/1903.04361); 29 pp., A4, footers 'Page N'; PDF metadata: created with LibreOffice 6.0 on 4 July 2019; the file shows no arXiv stamp and no version number, so the arXiv version (v1, v2 ...) is unknown; NOT the Springer version of record; PDF and text layer zednik2021solving.pdf/.txt at ~/iit-playground/pt_ai_animation_local/pdfs/zednik2021solving/; read 2026-11-08; PARTS READ: PDF pp. 1-10 (abstract, §1, §2, §3, start of §4) and pp. 22-25 (end of §5.4, §6 conclusion); NOT READ: pp. 11-21 (§4 and §5.1-§5.3, the worked XAI techniques), the references; sha256 1beed4b6a9b1c72bb873dd5d237249f97d2a56f9caa18204f84eba02fd8dd5ae (PDF, from sha256.txt; recomputed, matches)"
verified: verified
verified_against: "crossref.json (34(2), 265-288, online 2019-12-20, print 2021-06); sha256 recomputed; per-page pdftotext of the arXiv preprint, 15 quotations traced"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# C. Zednik (2021), Solving the black box problem

## What it argues

Carlos Zednik (Magdeburg) builds a framework for judging whether an explainable-AI technique succeeds. He
starts from Paul Humphreys's analysis of opacity: a system is opaque to an agent when the agent does not
know all the "epistemically relevant elements" of it. Two consequences follow. Opacity belongs to a pair,
system and agent, not to the system alone. And the elements that matter differ with the agent's job. Zednik
takes Tomsett et al.'s six stakeholders in the machine-learning ecosystem (operators, executors,
decision-subjects, data-subjects, creators, examiners) and pairs them with David Marr's questions about
what a system does, why, how, and where. A bank teller, an applicant and a software engineer then need
different explanations of the same loan-risk model, so there are "many Black Box Problems", not one.

He points out why machine learning makes the problem sharp: its developers pick the architecture and the
learning environment but not the parameter values, so they "do not wholly determine the way in which the
problem is actually solved". The later sections (not read, see object_read) apply the framework to input
heatmapping, feature-detector identification and diagnostic classification. His verdict is mostly hopeful:
these techniques can already answer many stakeholders' questions, though they are "likely to be limited in scope
and utility", and XAI may have to move away from semantic interpretability. A footnote grants that some systems may stay opaque
after the best techniques.

## What the paper uses it for

- **c7** (necessary opacity: no frame holds the motion, no component the intelligence): the use is partial
  and the card flags where it breaks. What Zednik gives the paper: (a) a venue-native, citable analysis of
  opacity as agent-relative, which fits §4.2's point that what the viewer cannot see differs from what the
  animator cannot see; (b) the observation that ML developers do not set the values that solve the problem,
  which parallels an LLM that makes its own in-betweens; (c) the point that an explanation at one level of
  description (parameters) does not serve an agent who needs another. What does not carry: Zednik is not
  arguing that opacity is "in principle". He cites Humphreys's essential epistemic opacity only to say that
  Humphreys's "impossible" is practical, not logical, and that his own task is the systems that "can be
  rendered transparent". His conclusion is that XAI is increasingly able to answer stakeholders' questions.
  So Zednik is a counterweight as much as a support. The paper has to say why its claim, that no frame
  contains the motion, survives his view that stakeholder-relative explanation mostly works. The honest
  position is that Zednik shows opacity is relative to an agent and a question; he does not show, and does
  not claim, that any question is unanswerable. He also says nothing about animation or perception, and his
  "intelligence" is the system's behaviour, not something located in a component.

## Loci

Locators: the held preprint prints "Page N" at the foot of each page; PDF page n = printed page n. These
are the preprint's pages. The published article runs pp. 265-288 and breaks the text differently. I matched
every quotation against `pdftotext` output for that PDF page of the held PDF (sha256 above). Zednik's
footnote 5 uses straight apostrophes, as given.

- "Many of the computing systems programmed using Machine Learning are opaque: it is difficult to know why they do what they do or how they work." — PDF p. 1 (Page 1), Abstract; matched against page text of zednik2021solving.pdf
- "developers in Machine Learning exert limited influence on the way in which the relevant problems are solved." — PDF p. 3 (Page 3), §2.1; matched against page text of zednik2021solving.pdf
- "ML developers do not typically decide on the particular values these parameters eventually obtain (e.g. the weights of individual network connections), and in this sense, do not wholly determine the way in which the problem is actually solved." — PDF p. 3 (Page 3), §2.1; matched against page text of zednik2021solving.pdf
- "opaque relative to a cognitive agent X at time t just in case X does not know at t all of the epistemically relevant elements of the [system]" — PDF p. 4 (Page 4), §2.2; Zednik quoting Humphreys (2009, p. 618), the bracket is Zednik's; matched against page text of zednik2021solving.pdf
- "Notably, Humphreys' notion of possibility is not logical, but practical—it depends on an agent's limited time, money, and computational power" — PDF p. 4 (Page 4), footnote 5 to §2.2; matched against page text of zednik2021solving.pdf
- "opacity is agent-relative. That is, a computing system is never opaque in and of itself, but opaque only with respect to some particular agent." — PDF p. 5 (Page 5), §2.2; matched against page text of zednik2021solving.pdf
- "all while allowing that some systems may remain opaque even after the most powerful techniques have been applied." — PDF p. 5 (Page 5), footnote 5 (continued); matched against page text of zednik2021solving.pdf
- "The primary aim of this discussion is to show how systems that can be rendered transparent should be rendered transparent." — PDF p. 5 (Page 5), footnote 5 (continued); matched against page text of zednik2021solving.pdf
- "Creators are the developers of the computing system." — PDF p. 7 (Page 7), §3.1; matched against page text of zednik2021solving.pdf
- "Perhaps surprisingly, most other agents are less likely to be concerned with the system’s variables than with the environmental features that are represented by those variables." — PDF p. 8 (Page 8), §3.2; matched against page text of zednik2021solving.pdf
- "it may in fact be more appropriate to speak of many Black Box Problems." — PDF p. 24 (Page 24), §6; matched against page text of zednik2021solving.pdf
- "Depending on who you are and how it is that you interact with an ML-programmed computer, that computer will be opaque for different reasons, and must be rendered transparent in different ways." — PDF p. 24 (Page 24), §6; matched against page text of zednik2021solving.pdf
- "For this reason, although promising, these XAI techniques are likely to be limited in scope and utility." — PDF p. 25 (Page 25), §6; matched against page text of zednik2021solving.pdf
- "it may accept that certain ML applications can only be explained by mastering the most sophisticated XAI techniques." — PDF p. 25 (Page 25), §6; matched against page text of zednik2021solving.pdf
- "although semantic interpretability may often be beneficial, it may not always be essential." — PDF p. 25 (Page 25), §6; matched against page text of zednik2021solving.pdf

## Caution

- **Version.** This is the author's preprint (arXiv 1903.04361), which DECISIONS expected. Its arXiv version
  number does not appear in the file. The published text (Springer, 34(2), 2021) may differ in wording and
  page breaks. Quotations here are from the preprint only; the S6 verifier should not match them against the
  Springer version without checking.
- **Year (record correction, applied).** Crossref: published online 2019-12-20, print 2021-06, volume 34,
  issue 2. The key takes the volume year 2021; `registered_year` is 2019, which is also the year FACETS
  wrote. If the lead prefers the online year the key becomes `zednik2019solving`.
- **Read depth.** `partial`. The worked examples of XAI techniques (pp. 11-21) were not read; the "What it
  argues" paragraph reports their purpose from the introduction and conclusion only.
- **Homonym risk.** None found. This is Carlos Zednik, Otto-von-Guericke-Universität Magdeburg at the time of
  the preprint. His affiliation in the published version is not checked.
- **The "in principle" term.** The paper's c7 quotes the author's "in principle black box". Zednik's
  Humphreys footnote says Humphreys's impossibility is practical, bounded by time, money and computing power.
  The paper should not cite Zednik as holding that opacity is in principle unavoidable.
- **What the paper may not claim from it:** that explanation is impossible in principle, that opacity lies in
  no component, or anything about animation or perception.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 3
- verdict: verified (no changes). Frontmatter matches Crossref; registered_year 2019 is right; all 15 quotations verbatim on the stated preprint pages; object_read matches pdfinfo (29 pp., LibreOffice 6.0, created 4 July 2019); the c7 counterweight reading is supported by footnote 5 (pp. 4-5) and the conclusion (pp. 24-25).
- checked: frontmatter against crossref.json; sha256; each quotation by per-page pdftotext; pdfinfo metadata; Magdeburg affiliation; Tomsett et al. stakeholders, Marr questions (what, why, how, where) and loan example; footnote 5 on essential epistemic opacity; the conclusion's "increasingly possible" passage.
- changed: nothing
