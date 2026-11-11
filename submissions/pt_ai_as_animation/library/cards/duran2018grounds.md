---
key: duran2018grounds
apa: "Durán, J. M., & Formanek, N. (2018). Grounds for trust: Essential epistemic opacity and computational reliabilism. *Minds and Machines*, *28*(4), 645–666. https://doi.org/10.1007/s11023-018-9481-6"
authors: "Durán, Juan M.; Formanek, Nico"
year: 2018
title: "Grounds for Trust: Essential Epistemic Opacity and Computational Reliabilism"
venue: "Minds and Machines"
volume: "28"
issue: "4"
pages: "645–666"
doi: "10.1007/s11023-018-9481-6"
url: ""
type: article
facets: [F7]
claims: [c7, c11]
role: support
load: load-bearing
read_depth: full_text
object_read: "Publisher PDF (Springer, open access, CC BY 4.0 per the Crossref licence field; 22 pp.) and its text layer, at ~/iit-playground/pt_ai_animation_local/pdfs/duran2018grounds/duran2018grounds.pdf and duran2018grounds.txt, with crossref.json in the same folder; no copy in inbox/; read 2026-11-08; sha256 71f8340bd5fd0004f096c25ef1262835e5bfceb08f7646122307e9f125014293 (PDF, sha256.txt, recomputed with shasum -a 256, matches)"
verified: corrected
verified_against: "crossref.json; full text layer per page with pdftotext (offset 644), 11 quotations traced; sha256 recomputed"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Durán and Formanek (2018), Grounds for trust

Full text read, pp. 645-666 (the abstract, §1 to §5; the reference list was not read). Page locators give the printed page. PDF page = printed page - 644.

## What it argues

Juan Durán and Nico Formanek take up Paul Humphreys's claim that computer simulations are "epistemically opaque": a process is opaque to an agent when the agent does not know all of its epistemically relevant elements. They rebuild the definition in terms of two conditions, access and surveyability, so that a process is opaque to an agent who cannot reach and check all the steps of its justification (pp. 648-650). "Essential" epistemic opacity (EEO) is the case where, given the nature of the agent, it is impossible to know all those elements. They read "impossible" in a down-to-earth way, as human action in finite time and space with finite mental capacity, and conclude that for humans most processes in computational science are EEO (p. 651). That raises a sceptical worry: if most processes are EEO, nobody is justified in believing their results. Their answer is "computational reliabilism", a version of Goldman's process reliabilism. A researcher is justified in believing a simulation's results when the simulation is a reliable process, and reliability is shown from outside the process by four sources: verification and validation, robustness analysis, a history of successful and unsuccessful implementations, and expert knowledge (pp. 656-663). They do not remove opacity; they argue that researchers can trust the results without inspecting or surveying the process (p. 652). The article does not use the word "transparency".

## What the paper uses it for

- **c7** (necessary opacity: no frame holds the motion, no component the intelligence): Durán and Formanek supply the philosophy-of-science account of why a process can stay opaque to its users however much information they hold, and of why this does not stop them knowing. This matches the sketch's use of Humphreys's "essential epistemic opacity". Two limits matter. First, the authors place EEO "on the practical side of his in principle-in practice divide" (p. 650): the necessity comes from the nature of human agents, not from the process itself. The author's phrase "in principle black box" (SKETCH §4.2) is stronger than this, so the card does not support the "in principle" wording. Second, they write about computer simulations in science, and they say only that "much of what is said here can also be extended to other uses of computers" under conditions (p. 647). They say nothing about neural networks, LLMs, or agent harnesses. Using the article for LLM systems is the paper's extension, not theirs. The authors also say nothing of animation, so the "no frame holds the motion" sharpening is the paper's alone.
- **c11** (implementation and evaluation under the life frame): the four sources give an evaluation practice that works without opening the box, and two of them (a track record, and expert judgment) are close to evaluating a character by how it behaves over time. The use stretches the source: the authors design the four sources for the reliability of simulation results, not for the character or conduct of a system, and they warn that expert knowledge is "a rather weak source" on its own (p. 656).

## Loci

Each quotation was matched against duran2018grounds.txt. The text layer joins some hyphenated words with a non-breaking hyphen; the quotations below use a plain hyphen. Quoted passages by Humphreys appear as the authors give them.

- p. 646, §1: "Humphreys did not offer any suggestions for a solution to epistemic opacity, but rather restricts his analysis to pointing it out as a philosophically novel issue."
- p. 647, §1: "although this article focuses efforts on computer simulations, much of what is said here can also be extended to other uses of computers provided that the right methods for grounding computational reliabilism are in place."
- p. 648, §2.1 (quoting Humphreys 2009, 618): "[A] process is epistemically opaque relative to a cognitive agent X at time t just in case X does not know at t all of the epistemically relevant elements of the process"
- p. 650, §2.3 (quoting Humphreys 2009, 618): "A process is essentially epistemically opaque to X if and only if it is impossible, given the nature of X, for X to know all of the epistemically relevant elements of the process"
- p. 650, §2.3: "For Humphreys EEO is on the practical side of his in principle—in practice divide."
- p. 651, §2.3: "And it is for humans that most processes in (computational) science are EEO"
- p. 651, §2.3: "At its core, we claim that researchers are justified in believing the results of computational processes, such as computer simulations, given certain conditions for their reliability."
- p. 651, fn. 4 (quoting Humphreys 2011, 138): "just as humans cannot in principle see atoms, neither can humans in principle be given the attributes of unbounded memory and arbitrarily fast computational speed."
- p. 652, §3: "since EEO prevents us from attributing reliability by means of inspecting the simulation models or by surveying the process of computing such models, then it must be done by appealing to procedures external to the simulation itself."
- p. 656, §4: "we identify four sources for attributing reliability to a computational process such as computer simulations."
- p. 656, §4: "expert knowledge by itself is a rather weak source for the reliability of most computer simulation."

## Caution

- **"In principle" versus "in practice."** The sketch sets Humphreys's essential opacity beside Burrell's third source as support for an "in principle" claim. Durán and Formanek read Humphreys's EEO as falling on the practical side of the in-principle/in-practice divide (p. 650), and in footnote 4 (p. 651) they quote Humphreys on why: humans cannot "in principle be given the attributes of unbounded memory and arbitrarily fast computational speed" (see Loci). The author decides whether "necessary opacity" in §4.2 means necessary for human agents of finite capacity (this source's reading) or necessary in the process itself. The Humphreys card (`humphreys2009philosophical`) should be checked on the same point.
- **Scope.** The article is about scientific computer simulations. Whether an LLM harness is a "simulation" in their sense is not argued.
- **Counter-position inside the article.** Durán and Formanek discuss Newman (2015), who holds that well-architected software is not epistemically opaque (p. 646-647). That is the same line as the practical-remedy counter in FACETS F7; the article's reply is that software engineering also produces opacity through information hiding (p. 647).
- **Trust claim.** The article argues that reliability, and with it trust in results, must be attributed "by appealing to procedures external to the simulation itself" (p. 652), not by inspecting it. "Transparency" is the card's gloss, not the authors' word. If §4.2 or §4.3 reads opacity as a reason why users cannot rely on a system they cannot inspect, this source argues the opposite, and the paper should say which it accepts.
- **Dates.** Crossref gives volume 28(4), December 2018 in print, online 2018-10-29; the key year matches the volume year.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 4
- verdict: corrected
- checked: frontmatter against crossref.json (authors Juan M. Durán and Nico Formanek, title, *Minds and Machines* 28(4), 645-666, DOI, journal-article, print 2018-12, online 2018-10-29, CC BY 4.0 licence); sha256 of the PDF recomputed, matches; 22 PDF pages = printed pp. 645-666, offset 644 confirmed; all 11 quotations found verbatim on the stated printed page (six of them break across lines with the PDF's non-breaking hyphen, which the card rejoins, as it says); prose page references checked on the page: access and surveyability (pp. 647-649), Newman (pp. 646-647), information hiding (p. 647), Goldman's reliabilism (pp. 652-655), the four sources (pp. 645, 656-663), no mention of neural networks (0 hits).
- changed: the 'trust does not need transparency' gloss in What it argues and in the Caution 'Trust claim' bullet. The word 'transparency' does not occur in the text layer; both now state the p. 652 claim in the authors' terms and mark 'transparency' as the card's word.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 11/11 loci found on the stated printed page (PDF p. = printed − 644); frontmatter vs crossref.json (Durán, Juan M.; Formanek, Nico; Minds & Machines 28(4) 645–666; online 2018-10-29, print 2018-12; DOI); PDF sha256 recomputed, matches sha256.txt; the c7 and c11 uses name their stretches.
- Changed: nothing.
- For the author: (1) status `cited` although SOURCE.md and SKETCH.md do not name Durán & Formanek. (2) The Caution's in-principle vs in-practice point stands: this source reads essential opacity as practical, which is weaker than SOURCE's "in principle black box"; you decide which §4.2 means.
