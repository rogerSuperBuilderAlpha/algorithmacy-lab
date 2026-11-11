---
key: bongard2021living
apa: "Bongard, J., & Levin, M. (2021). Living things are not (20th century) machines: Updating mechanism metaphors in light of the modern science of machine behavior. *Frontiers in Ecology and Evolution*, *9*, Article 650726. https://doi.org/10.3389/fevo.2021.650726"
authors: "Bongard, Joshua; Levin, Michael"
year: 2021
title: "Living Things Are Not (20th Century) Machines: Updating Mechanism Metaphors in Light of the Modern Science of Machine Behavior"
venue: "Frontiers in Ecology and Evolution"
volume: "9"
issue: ""
pages: "Article 650726"
doi: "10.3389/fevo.2021.650726"
url: ""
type: article
facets: [F2]
claims: [c3, c4]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "Publisher PDF from Frontiers (15 pp., references on pp. 12-15) and its text layer bongard2021living.txt, at pt_ai_animation_local/pdfs/bongard2021living/ (FETCH_LOG.tsv: explicit_url, https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.650726/pdf); inbox/ holds no copy; pp. 1-11 read in full, with the back matter on p. 12; reference list (pp. 12-15) not read; 2026-11-08; sha256 f3906c9e407064bf6d5412576291186bcfb4e471671feedde6cc35cfc1474bf5 (PDF, from sha256.txt)"
verified: corrected
verified_against: "crossref.json; sha256 of PDF; per-page pdftotext text layer, 16 quotations traced to their pages"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Bongard & Levin (2021), Living things are not (20th century) machines

## What it argues

Joshua Bongard (Department of Computer Science, University of Vermont) and Michael Levin (Allen Discovery Center, Tufts; Wyss Institute, Harvard) write a "Hypothesis and Theory"
paper on the old fight between mechanists, who treat cells as machines, and organicists, who say life
resists that picture. They side with the organicists on life ("We see life from the organicist
perspective", p. 2). Their move is to attack the other half of the contrast. The "machine" that
organicists reject, they argue, is a 20th-century machine: independent, predictable, human-designed,
modular, open to reductionist study, without intelligence, and with software cleanly apart from
hardware. They take these claims one at a time (pp. 2-8) and argue that modern machine learning,
evolutionary design, swarm robotics and hybrid bio-electronic systems break each of them. Their one
concession is self-similar, multi-scale organization, which still marks living systems "for now" (p. 4).
They then propose updated definitions of machine, robot, program, and software/hardware (pp. 7-8),
argue that life and machine form a continuum, not two bins (p. 9), and close by saying that cells are
"not really machines", but that every metaphor is wrong and some are more useful than others (p. 11).
The paper is conceptual and speculative. It runs no study. It was written before LLM products and
never mentions harnesses or agent scaffolds.

## What the paper uses it for

- **c4** (an organizational account of life fits the system around the LLM): contrast. Bongard and Levin
  are organicists, so they share the paper's wish to take life seriously. They would object to the
  boundary c4 needs. If c4 says an organizational account of life puts AI development on the "life"
  side and computer science on the "machine" side, they answer that the two sides blur: they call a
  "strict life/machine dualism" "highly implausible" (p. 9), and they say biology and computer science
  "are both studying the same remarkable processes, just operating in different media" (p. 9). Two
  uses fit. First, their "machines as they could be" (p. 1) mirrors Langton's "life as it could be" and
  marks the same move from a given case to the space of possible ones. Second, they describe modern
  systems as built of layers and dependencies, not as one core component: software "dependency trees"
  and a count of "intermediate machine design/optimization layers" (pp. 3, 4). That supports the idea
  that the thing a user meets is more than the model. The use stretches them in two ways. They write
  about machine learning in general and about biohybrids, not about LLMs, and "virtual machine" appears
  once, as an example of how software and machine blur (p. 3), not as part of an AI product.
- **c3** (neither life nor intelligence has a consensus definition): weak support. They say "Defining
  'life' has proven to be notoriously difficult" (p. 2) and cite other authors on changing the term.
  They do not survey definitions, and their own project is to redefine "machine", not "life", so the
  paper should cite them only for the remark.

## Loci

Locators: PDF page n is also printed page n (the Frontiers footer runs "1" to "15"). Every quotation was
matched against the held PDF's page text (sha256 above), page by page, extracted with `pdftotext -f N -l N` in reading order.
The folder's `bongard2021living.txt` is a two-column layout dump that interleaves columns, so I did not match against it. The text layer prints the "fi" ligature as one character; I give it as "fi". Where
Bongard and Levin put double quotation marks inside a quotation, I give them as single quotes.

- "Key terms such as machine, robot, program, software, evolved, designed, etc., need to be revised in light of technological and theoretical advances" — PDF p. 1, Abstract; matched against PDF page text
- "Progress in both theory and practical applications requires the establishment of a novel conception of 'machines as they could be,'" — PDF p. 1, Abstract; matched against PDF page text
- "Defining 'life' has proven to be notoriously difficult" — PDF p. 2, Introduction; matched against PDF page text
- "We see life from the organicist perspective" — PDF p. 2, Introduction; matched against PDF page text
- "Rather than reduce the conception of life to something lesser, we seek to update and elevate the understanding of 'machines,' given recent advances in artificial life, AI, cybernetics, and evolutionary computation." — PDF p. 2, Introduction; matched against PDF page text
- "We view the main aspects of a machine to refer to a device, constructed according to rational principles that enable prediction (to some threshold of accuracy) of their behavior at chosen scales." — PDF p. 2, 'What is meant by machine'; matched against PDF page text
- "Likewise, software systems have very long dependency trees: the hierarchy of support software that must be installed in order for the system in question to run." — PDF p. 3, 'Machines are independent: life is interdependent'; matched against PDF page text
- "A simple example is that of a virtual machine, which is software that simulates hardware different from that running the virtual machine software." — PDF p. 3, same section; matched against PDF page text
- "Indeed, one defensible metric of technological progress is the growing number of intermediate machine design/optimization layers sandwiched between human ingenuity and deployment of a new technology." — PDF p. 4, 'Machines are designed by humans: life is evolved'; matched against PDF page text
- "Considering the weight of a particular synaptic connection or a local neural cluster in a deep neural network provides little understanding of the machine’s behavior as a whole." — PDF p. 5, 'Machines can be studied in a reductionist framework: life cannot'; matched against PDF page text
- "modern technologies only achieve utility when they are emplaced appropriately into the technosphere; it is difficult or impossible to describe their function independently of it." — PDF p. 6, same section; matched against PDF page text
- "Any system that magnifies and partly or completely automates an agent’s ability to effect change on the world." — PDF p. 7, 'Improving definitions' (Machine); matched against PDF page text
- "Working as coherent wholes, such constructs make highly implausible a view of strict life/machine dualism" — PDF p. 9, 'An emerging field: re-drawing the boundaries'; matched against PDF page text
- "One possibility is that biology and computer science are both studying the same remarkable processes, just operating in different media." — PDF p. 9, same section; matched against PDF page text
- "Living cells and tissues are not really machines; but then again, nothing is really anything – all metaphors are wrong, but some are more useful than others." — PDF p. 11, Conclusion; matched against PDF page text
- "in this deeper, more important sense, living things are profitably studied with the deep concepts of computer science." — PDF p. 11, Conclusion; matched against PDF page text

## Caution

- **Title.** The Crossref record carries the full title with its subtitle ("Updating Mechanism Metaphors in
  Light of the Modern Science of Machine Behavior"). DECISIONS.md and the triage file give only the part
  before the colon. The card follows the record. The key stays `bongard2021living`.
- **Date.** Crossref and the PDF both give 16 March 2021 (received 7 Jan, accepted 22 Feb 2021). One
  volume, one year. No `registered_year`.
- **Direction of the contrast.** Triage F1-F4.md reads the paper as loosening the life/machine boundary
  "c4 relies on", and says it cuts both ways. The text bears that out. The authors want to raise the
  "machine" up to meet life, not to lower life to machine (p. 2). They are not an argument that AI is
  alive; the paper must not cite them for that. They are also not an argument that AI development is
  computer science, since they say computer science is not about computers (the epigraph on p. 8 is
  Dijkstra's, not theirs) and call for merged disciplines (p. 9).
- **Dated for the paper's purpose.** The work predates ChatGPT-style products. "AI" in the text means
  neural networks, evolutionary algorithms and robots (pp. 5-6, 8).
- **What the read version lacks.** I read the body (pp. 1-11) and the front and back matter on p. 12.
  I did not read the reference list (pp. 12-15) or the
  works they cite (Nicholson 2019, Rahwan et al. 2019). Claims about those works from this card are
  second-hand.
- **What the paper may not claim from it:** that organicists accept AI as living, any account of LLMs,
  or support for the paper's life-versus-intelligence frame (the authors do not use that pair).

## Verification
- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 5
- verdict: corrected
- checked: frontmatter against crossref.json (authors, title with subtitle, venue, volume 9, article number 650726, DOI, type, online date 2021-03-16; no print date, so no `registered_year`); PDF sha256 against sha256.txt and FETCH_LOG.tsv (match); all 16 quotations searched in the per-page `pdftotext -f N -l N` text, each found verbatim (ligatures, quote marks and dashes folded) on the page the card gives; the summary's page claims spot-checked ("for now" p. 4, Dijkstra epigraph p. 8, "Hypothesis and Theory" p. 1, sections "Improving definitions" p. 7, "An emerging field" p. 8, "Conclusion" p. 11).
- changed: (1) the PDF has 15 printed pages, not 12: the footer runs 1 to 15 and the references fill pp. 12-15, so object_read and the Loci locator note now say so; (2) the authors' roles "computer scientist" and "biologist" are not in the PDF, so the summary now gives their affiliations from p. 1. Quotations, locators and claim tags unchanged.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 16/16 loci found in per-page pdftotext text (three with inner double quotes given as single, matched quote-agnostically on pp. 1–2); frontmatter vs crossref.json (full title with subtitle, vol. 9, article 650726, 2021-03-16); PDF sha256 recomputed, matches; 15 pp. per pdfinfo; 'HYPOTHESIS AND THEORY' and 'We see life from the organicist perspective' present.
- Changed: nothing
- For the author: nothing.
