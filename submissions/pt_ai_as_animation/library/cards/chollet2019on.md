---
key: chollet2019on
apa: "Chollet, F. (2019). *On the measure of intelligence* (arXiv:1911.01547v2). arXiv. https://doi.org/10.48550/arxiv.1911.01547"
authors: "Chollet, François"
year: 2019
title: "On the Measure of Intelligence"
venue: "arXiv (cs.AI) preprint"
volume: ""
issue: ""
pages: ""
doi: "10.48550/arxiv.1911.01547"
url: "https://arxiv.org/abs/1911.01547"
type: preprint
facets: [F3]
claims: [c3, c5, c11]
role: support
load: load-bearing
read_depth: partial
object_read: "arXiv v2 PDF (64 pp. [Corrected by Fable, S7: the card said 65 pp.; pdfinfo gives 64], stamped 'arXiv:1911.01547v2 [cs.AI] 25 Nov 2019', dated 5 November 2019 on p. 1) and its text layer, at ~/iit-playground/pt_ai_animation_local/pdfs/chollet2019on/chollet2019on.pdf and chollet2019on.txt; no copy in inbox/; read 2026-11-08; sha256 773b9ecec3df33e664ab5a784f9e48818e7fd0d8e211b3243f4f4e0fdecb2fee (PDF, sha256.txt, recomputed with shasum -a 256, matches)"
verified: verified
verified_against: "csl.json (arXiv DataCite record, v2); full text layer per page with pdftotext, 13 quotations traced; sha256 recomputed"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Chollet (2019), On the measure of intelligence

Partial read. Parts read in full: abstract and contents (pp. 1-2); I.1 and I.2 (pp. 3-6); I.3.4 end and I.3.5 (pp. 16-17); II.1.1 (pp. 18-19); II.2 opening and the problem setup through the start of the training phase (pp. 27-30); II.2.3 and the start of II.3 (pp. 42-43); III.1.3 end and III.1.4 (pp. 51-52); the end of III.3 and "Taking stock" (pp. 56-57). Not read: I.3.1-I.3.4 (pp. 7-16), II.1.2-II.1.3 (pp. 20-27), the formal apparatus of II.2.1-II.2.2 (pp. 30-42), most of II.3 and III (pp. 43-51, 52-56). The PDF page number equals the printed page number throughout.

## What it argues

François Chollet argues that AI research measures the wrong thing. The field benchmarks skill at set tasks, such as board games and video games, but skill can be "bought" with built-in priors or unlimited training data, so a high score says little about intelligence (pp. 18-19). He traces the field's definitions to two old pictures of the mind: a collection of task-specific skills, and a general ability to learn (pp. 4-6). He then defines intelligence as "skill-acquisition efficiency" over a scope of tasks, relative to priors, experience and generalization difficulty (p. 27), and proposes a benchmark, the Abstraction and Reasoning Corpus (ARC), built on human-like "Core Knowledge" priors (stated in the abstract on p. 1 and summarised on p. 57; the benchmark's own sections, pp. 46-55, were read only at pp. 51-52 and 56). Along the way he separates the "intelligent system" (a program-synthesis engine) from the "skill program" it produces, and he calls the mix-up of process and artifact a basic fault in how AI is conceived (p. 42). He says openly that his definition is meant to be "actionable", not agreed (p. 27, p. 57). The paper predates ChatGPT-style systems and says nothing about LLMs or harnesses.

## What the paper uses it for

- **c3** (neither life nor intelligence has a consensus definition): Chollet states the no-consensus premise for intelligence in two places (pp. 3, 4) and adds that his own definition is not "the 'one true' definition" (p. 27). The use fits. It is a second voice beside Legg and Hutter, from inside the AI community. It stretches the source if the paper implies Chollet leaves the matter open: he offers a working definition and argues for it.
- **c5** (intelligence frame versus life frame is a stance choice): Chollet is the clearest statement of the intelligence frame the paper wants to set against the life frame. Intelligence is specified as a target, measured on a benchmark, and the engineering task is "an optimization problem" (p. 42). That is the "rigid standard" of SKETCH §2. The stretch: Chollet does not call this a stance; he argues it is the right way to do the job. The paper has to supply the word "stance" and the contrast.
- **c11** (implementation and evaluation under the life frame): Chollet gives the evaluation practice that the intelligence frame implies (skill benchmarks, then generalization benchmarks), so the paper can say what the life frame changes: believability and consistency over time instead of a score. The same pages give the paper a point of contact for c2 (model-centrism). Chollet places intelligence in the generating process and calls the produced skill program "the non-intelligent output artifact" (p. 42), and he says "the only intelligence at work here is the engineer's" for a hand-coded program (p. 19). The paper can use that as a case where a computer scientist already locates intelligence outside the artifact. It cannot say Chollet agrees that the whole surrounding system is the AI: his "intelligent system" is a learning or synthesis engine, not a harness, VM or team.

## Loci

Inner quotation marks in the source are changed to single quotes. Each quotation was matched against chollet2019on.txt (the text layer of the PDF read).

- p. 3, §I.1: "It is a testimony to the immaturity of our field that the question of what we mean when we talk about intelligence still doesn’t have a satisfying answer."
- p. 3, §I.1: "These would not be merely definitions and measures meant to describe or characterize intelligence, but precise, explanatory definitions meant to serve as a North Star, an objective function showing the way towards a clear target"
- p. 4, §I.2: "Many formal and informal definitions of intelligence have been proposed over the past few decades, although there is no existing scientific consensus around any single definition."
- p. 4, §I.2: "Legg and Hutter [53] summarized in 2007 no fewer than 70 definitions from the literature into a single statement"
- p. 19, §II.1.1: "the only intelligence at work here is the engineer’s."
- p. 19, §II.1.1: "it is no more intelligent than the ink and paper used to write down the proof of a theorem."
- p. 19, §II.1.1: "Hard-coding prior knowledge into an AI is not the only way to artificially 'buy' performance on the target task without inducing any generalization power."
- p. 27, §II.2.1: "The intelligence of a system is a measure of its skill-acquisition efficiency over a scope of tasks, with respect to priors, experience, and generalization difficulty."
- p. 27, §II.2.1: "we do not purport that the definition above and the formalism below represent the 'one true' definition."
- p. 42, §II.2.3 (a): "the process of creating an intelligent system can be approached as an optimization problem, where the objective function would be a computable approximation of our quantitative intelligence formula."
- p. 42, §II.2.3 (a): "we stop thinking of 'agents' as monolithic black boxes that take in sensory input and produce behavior"
- p. 42, §II.2.3 (a): "we believe that this confusion between process and artifact has been an ongoing fundamental issue in the conceptualization of AI."
- p. 57, "Taking stock": "were developed to be actionable, explanatory, and quantifiable, rather than being descriptive, exhaustive, or consensual."

## Caution

- **Partial read.** The paper's uses sit in the framing sections, which I read. The formal definition (pp. 30-42) and ARC details (pp. 46-56) were not read in full, so the card does not describe their mechanics.
- **Version.** This is the arXiv preprint v2, not a peer-reviewed article. No later version of record was checked for this card. csl.json in the folder gives version "2", 2019.
- **Attribution inside Chollet.** On p. 3 Chollet quotes Legg and Hutter [53], "to the best of our knowledge, no general survey of tests and definitions has been published". His reference [53] is "A collection of definitions of intelligence. 2007." I searched the arXiv v1 text of that work (card `legg2007collection`) and did not find the sentence. Do not cite it to the Collection through Chollet.
- **"No fewer than 70" (p. 4)** is Chollet's wording for the Collection's "70 odd" definitions.
- **No registry record.** The folder holds csl.json (arXiv/DataCite style) only; no Crossref or OpenAlex file. The DOI is the arXiv DOI, taken from csl.json.
- **Overlap with the other card.** Chollet and `legg2007collection` serve the same facet; the paper should cite Legg and Hutter for the count and Chollet for the benchmark frame.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 4
- verdict: verified (no changes)
- checked: frontmatter against csl.json (author, 2019, title, DOI 10.48550/arxiv.1911.01547, version 2; `type: preprint` for a record typed 'article' is right for an arXiv preprint); the PDF's p. 1 stamp 'arXiv:1911.01547v2 [cs.AI] 25 Nov 2019' and date 'November 5, 2019'; sha256 of the PDF recomputed, matches sha256.txt and the card; all 13 quotations in Loci searched page by page with pdftotext -f N -l N, all verbatim (inner quotes changed to single, as the card says) and all on the stated page; prose claims spot-checked on the page: the Legg and Hutter quotation on p. 3, 'the non-intelligent output artifact' on p. 42, 'buy' and board and video games on pp. 1 and 18-19; the Caution that 'no general survey of tests and definitions has been published' is absent from the Legg v1 text layer is confirmed (no hit).
- changed: nothing. Note for Fable: DECISIONS tags this work c5, c11; the card adds c3 and supports it with the pp. 3, 4 and 27 quotations. The c2 contact point in the c11 bullet is labelled as a contact point, not a tag.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index after fix** (fixed here).
- Checked: 13/13 loci found in the per-page text layer on the stated pages (3, 4, 19, 27, 42, 57); frontmatter vs csl.json (arXiv DOI, version 2, 2019); PDF sha256 recomputed, matches; the v2 stamp and 'non-intelligent output artifact' present; partial depth lists the parts read.
- Changed: object_read said '65 pp.'; pdfinfo and per-page extraction give 64. Corrected and marked.
- For the author: the card tags c3 beyond DECISIONS's c5, c11, with pp. 3, 4, 27 quotations behind it; accept or drop the tag. Status 'cited' though SOURCE.md and SKETCH.md do not name Chollet (status note in part1.md).
