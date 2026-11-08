---
key: legg2007universal
apa: "Legg, S., & Hutter, M. (2007). Universal intelligence: A definition of machine intelligence. *Minds and Machines*, *17*(4), 391–444. https://doi.org/10.1007/s11023-007-9079-x"
authors: "Legg, Shane; Hutter, Marcus"
year: 2007
title: "Universal Intelligence: A Definition of Machine Intelligence"
venue: "Minds and Machines"
volume: "17"
issue: "4"
pages: "391–444"
doi: "10.1007/s11023-007-9079-x"
url: "https://arxiv.org/abs/0712.3329"
type: article
facets: [F3]
claims: [c3, c5]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "arXiv preprint 0712.3329v1 (stamp on p. 1: 'arXiv:0712.3329v1 [cs.AI] 20 Dec 2007'), 49-page PDF and its text layer legg2007universal.txt at ~/iit-playground/pt_ai_animation_local/pdfs/legg2007universal/, fetched by S4 from https://arxiv.org/pdf/0712.3329 (FETCH_LOG.tsv); read in full 2026-11-08 (body pp. 1–43, reference list pp. 43–49 checked for [LH07], [LH05], [LH06b], [Gre98], [Ste00]); sha256 03c6a3e6ed63e4aff3aa3c868d2efcb9cc6eb7b4a837a523df872d178f650593 (PDF; recomputed with shasum -a 256, matches sha256.txt)"
verified: verified
verified_against: "crossref.json; arXiv v1 PDF sha256 recomputed; full text layer, 17 quotations traced"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Legg & Hutter (2007), Universal intelligence: A definition of machine intelligence

## What it argues

Shane Legg and Marcus Hutter open with the problem that "nobody really knows what intelligence is", and
they set out to fix a definition that holds for any machine. They survey psychometric tests, animal
testing, theories of human intelligence and two sets of expert definitions (§2). From the shared features
of those definitions they distil one informal definition: "Intelligence measures an agent’s ability to
achieve goals in a wide range of environments" (p. 12). They then formalise it (§3). An agent is any
function from interaction history to action; an environment is a computable probability measure that
sends observations and rewards; the goal sits in the reward signal. They weight each environment by its
Kolmogorov complexity (Occam's razor) and sum the agent's expected reward over all computable,
reward-summable environments. The sum, Υ(π), is the agent's "universal intelligence". AIXI, Hutter's
optimal agent, sets its upper bound.

They test the measure on toy agents (random, Deep Blue, table learners, a forward planner) and claim
it orders them as intuition expects (§3.4). They grant that Υ is a definition, not a test, because
Kolmogorov complexity is not computable (§3.5). §4 surveys rival definitions and tests of machine
intelligence (the Turing test and its variants, compression tests, psychometric AI, the C-Test, Smith's
test) and scores them in Table 1. §5 sketches how a practical test might approximate Υ and answers
common objections. Their stance is "unabashedly functional": they define intelligence only by external
performance, and they set aside Block's lookup table, Searle's Chinese room and consciousness unless
these change measurable performance.

## What the paper uses it for

- **c3** (neither life nor intelligence has a consensus definition): partial support, and the use
  stretches the source. Legg and Hutter state the problem for machines ("nobody really knows what
  intelligence is", p. 1), and they quote Sternberg on there being almost as many definitions as experts
  (p. 10). But for *human* intelligence they say the opposite of c3: psychologists have reached "a fair
  degree of consensus" on definition and measurement (p. 3). Their own answer is to settle on one
  definition, not to give definitions up. The paper can cite them for the lack of consensus on
  *machine* intelligence and for the variety of expert definitions. It cannot cite them for "no
  consensus" in general. The count of definitions in the sketch ("about 70") does not appear in this
  paper; it points readers to a separate online collection [LH07] (p. 12, p. 31). That count belongs on
  `legg2007collection`.
- **c5** (intelligence frame versus life frame is a stance choice): anchor for what the intelligence
  frame looks like at its most rigorous. Legg and Hutter specify, formalise, rank agents on one scale
  and judge only external performance ("Our perspective is simply to not care whether an agent looks
  intelligent on the inside", p. 31). That matches the sketch's §2 picture of the intelligence frame
  (specify, benchmark, defer to the result). The use stretches them in one respect. They do not present
  their frame as a stance anyone may choose. They present it as "Objective", "Universal" and
  "Fundamental" (pp. 29–30), so they would resist the claim that choosing between intelligence and life
  is a matter of stance. The paper should say so and argue against it. Two details may help the paper
  elsewhere, though neither is a claim tag here. First, their agent "could be anything" that maps
  history to action (p. 17), and the definition "places no limits on the internal workings of the
  agent" (p. 24). Read strictly, the agent their measure scores would be the whole working system, harness
  included, not the model alone (bears on c1/c2; the reading is mine, not theirs). Second, the
  environment, not the agent, carries the goal ("to test an agent in any given way it is sufficient to
  fully define the environment", p. 16), and they concede that a "separate goal system" would be more
  accurate (p. 41). Whoever builds the environment sets what counts as success (bears on c9/c11; again
  my reading).

## Loci

Locators: PDF pages of the arXiv v1 copy. The preprint prints its own page numbers and they equal the
PDF pages. They are **not** the *Minds and Machines* pages (391–444); see Caution. Section numbers are
the preprint's headings. Every quotation was matched against `legg2007universal.txt`, the text layer of
the held PDF (sha256 above), after joining line-end hyphens and collapsing line breaks. No quotation
here has inner double quotation marks.

- "A fundamental problem in artificial intelligence is that nobody really knows what intelligence is." — p. 1, Abstract; matched against legg2007universal.txt
- "Although the details of the definition are debated, in broad terms a fair degree of consensus about the scientific definition of intelligence and how to measure it has been achieved [Got97a, SB86]." — p. 3, §1; matched against legg2007universal.txt
- "Ideally we would like to be able to measure the intelligence of a wide range of systems; humans, dogs, flies, robots or even disembodied systems such as chat-bots, expert systems, classification systems and prediction algorithms [Joh92, Alb91]." — p. 4, §1; matched against legg2007universal.txt
- "Viewed narrowly, there seem to be almost as many definitions of intelligence as there were experts asked to define it." (epigraph, attributed to R. J. Sternberg "quoted in [Gre98]") — p. 10, §2.6; matched against legg2007universal.txt
- "Perhaps the most elementary common feature of these definitions is that intelligence is seen as a property of an individual who is interacting with an external environment, problem or situation." — p. 11, §2.6; matched against legg2007universal.txt
- "Intelligence measures an agent’s ability to achieve goals in a wide range of environments." — p. 12, §2.6 (repeated p. 15, §3.1); matched against legg2007universal.txt
- "Thus, in the framework as we have defined it, to test an agent in any given way it is sufficient to fully define the environment." — p. 16, §3.1; matched against legg2007universal.txt
- "It should also be emphasised that this agent-environment framework says nothing about how the agent or the environment actually work; it only describes their roles." — p. 17, §3.1; matched against legg2007universal.txt
- "While Gary Kasparov would still be a formidable player if we were to change the rules of chess, IBM’s Deep Blue chess super computer would be rendered useless without significant human intervention." — p. 20, §3.2; matched against legg2007universal.txt
- "Finally, the formal definition places no limits on the internal workings of the agent." — p. 24, §3.3; matched against legg2007universal.txt
- "What we have presented is a definition of machine intelligence, it is not a practical test of machine intelligence, indeed the value of Υ is not computable due to the use of Kolmogorov complexity." — p. 27, §3.5; matched against legg2007universal.txt
- "Universal intelligence does not depend on any subjective criteria." (under the heading "Objective.") — p. 30, §3.5; matched against legg2007universal.txt
- "Universal intelligence is in no way anthropocentric." (under the heading "Universal.") — p. 30, §3.5; matched against legg2007universal.txt
- "Our perspective is simply to not care whether an agent looks intelligent on the inside. If it is able to perform well in a wide range of environments, that is all that matters." — p. 31, §4.1; matched against legg2007universal.txt
- "A more accurate framework would consist of an agent, an environment and a separate goal system that interpreted the state of the environment and rewarded the agent appropriately." — p. 41, §5.2; matched against legg2007universal.txt
- "The approach we have taken is unabashedly functional." — p. 41, §5.2; matched against legg2007universal.txt
- "Our goal is to build powerful and flexible machines and thus these somewhat vague properties are only relevant to our goal to the extent to which they have some measurable effect on performance in some well defined environment." — p. 42, §5.2; matched against legg2007universal.txt

## Caution

- **Version read.** The copy is arXiv v1, posted 20 Dec 2007 (stamp on p. 1; the title page says
  "December 2007"). The Crossref record dates the journal article online on 10 Nov 2007 and in print on
  30 Nov 2007, *Minds and Machines* 17(4), pp. 391–444. I have not seen the Springer version, so I
  cannot say whether its text matches the preprint. Every page in Loci is a preprint page. A draft that
  quotes this card must either cite "arXiv:0712.3329, p. n" or take the journal page from the Springer
  PDF. `BROWSER_LIST.md` lists this key among the works carded from preprints.
- **The preprint calls itself a "report"** (p. 28: "the core argument of this report so far"). That is
  the authors' wording in v1, not a sign of a different work.
- **SKETCH §2 attributes "about 70 definitions of intelligence" to Legg & Hutter (2007).** This paper
  gives no count. It presents "ten definitions" (§2.6) and further samples (§2.7, §4.1) and refers the
  reader to "our online collection [LH07]", the largest collection they know of (p. 12). Its reference
  list gives [LH07] as "A collection of definitions of intelligence", in Goertzel & Wang (eds.),
  *Advances in Artificial General Intelligence*, Frontiers in Artificial Intelligence and Applications
  vol. 157 (p. 47). The count, if right, comes from that work (`legg2007collection`), and its card must
  check it. SKETCH is left alone.
- **Against c3.** As noted under use, the authors claim broad consensus about the definition and
  measurement of *human* intelligence (p. 3, citing [Got97a, SB86]). A reviewer who knows this paper
  will catch an uncited "no consensus" claim.
- **Registry.** Crossref and the key agree on 2007; no `registered_year`. Crossref holds no abstract.
  The metadata in the frontmatter comes from `crossref.json` in the key folder.
- **What the paper may not claim from it:** any empirical result about real systems (the agent
  comparisons in §3.4 are thought experiments on toy agents), or that Legg and Hutter treat the
  intelligence frame as one stance among others.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 1
- verdict: verified
- checked: frontmatter against crossref.json (authors, 2007, title, Minds and Machines 17(4) 391-444, DOI, journal-article); PDF sha256 recomputed and matches sha256.txt; all 17 quotations found verbatim in legg2007universal.txt on the stated PDF pages; section locators checked against the in-text headings rather than the running headers (p. 17 quotation sits before the §3.2 heading, so §3.1 is right; p. 30 quotations sit before the §4 heading, so §3.5 is right); secondary locators checked ("ten definitions" §2.6 p. 11, [LH07] pp. 12, 31, 47, "report" p. 28, "Objective"/"Universal" p. 30, "Fundamental" p. 29, "could be anything" p. 17, AIXI upper bound p. 27, Table 1 p. 38); no count of about 70 definitions appears anywhere in the text layer; c3 and c5 stretches are named under use and Caution.
- changed: nothing
