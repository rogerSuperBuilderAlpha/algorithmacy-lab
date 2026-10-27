<!-- Copied 2026-10-14 from the sister arm's verified library card (wt-dxd-foundation/submissions/dxd_foundation/literature/library/elish2019moral.md). Format is that library's, not this arm's card format. -->
# Elish, M. C. (2019). Moral crumple zones: Cautionary tales in human-robot interaction. *Engaging Science, Technology, and Society, 5*, 40–60.

**Identifier:** doi:10.17351/ests2019.260 · **Read depth:** full_text (published open-access PDF from the journal; the pagination is the journal's, pp. 40–60, and the PDF's page N is journal page N + 39; reference list scanned for the works named below) · **Source-tier:** peer-reviewed article (STS case analysis) · **Evidence basis:** direct_read · **Design and sample:** qualitative analysis of four cases (Three Mile Island 1979, Air France 447 in 2009, the 2018 Uber self-driving fatality, Google and Tesla driverless-car episodes), using official reports and press coverage, with the Therac-25 radiation accidents as a counter-case · **Parties modeled:** person–system, with the institution that designs and deploys the system as an unnamed third party · **Facets:** G · **Read:** 2026-10-13

## What it argues
Elish names the moral crumple zone: responsibility "may be misattributed to a human actor who had limited control over the behavior of an automated or autonomous system". The human "bears the brunt" in the way a car's crumple zone absorbs impact, but "the moral crumple zone protects the integrity of the technological system, at the expense of the nearest human operator" (abstract, p. 40). Operators become "liability sponges" (p. 41). She says her aim "is not to provide new insight into the causes or circumstances" of the accidents (p. 41).

- **Three Mile Island** (pp. 42–46). Press and the Kemeny report stressed operator error. Elish points to the control room, where physical conditions "were not adequately represented in the control interface" (p. 44); there was no direct indicator of the cooling-water level, and "the operators made incorrect decisions because they had incorrect information" (p. 44).
- **Air France 447** (pp. 46–50). After frozen airspeed sensors forced the plane into a mode where the pilots held primary control, they failed to recover from a stall. US coverage stressed the pilots' loss of "cognitive control", although the report also cited the controls, feedback and training (p. 48). She argues that pilots are in the crumple zone because law and certification put the burden on them: "While control has been effectively distributed, responsibility has not scaled accordingly" (p. 49). She says that casting humans as last-minute emergency responders "is something humans do not do well" (p. 50, citing Roscoe and Wiener), that automation does not free people for higher judgment (Bainbridge; Parasuraman and Riley), and that "the only possible malfunction, systemically" is the human, because the autopilot is certified as software and no certification covers the interaction (p. 50).
- **Therac-25** as counter-case (pp. 50–51): no crumple zone formed where the fault was proven as software and the manufacturer blamed first. Elish lists conditions: a highly publicised event, and an operator placed so as to lack the information (Therac-25: "no way of knowing") or the authority (TMI: "not ... sufficient information or authority"; AF447: "systemically disempowered") to correct (pp. 50-51).
- **Driverless cars** (pp. 52–54): the Uber safety driver faced possible charges although the vehicle's own braking was disabled in autonomous mode (p. 53); Google dropped supervised automation because it could not solve the handoff problem (p. 54).

The conclusion asks that "human in the loop" claims be tested against practice, and asks whether certification can cover "an unbounded system" (p. 55). Her remedies are a call to rethink certification and liability, not a design method.

## Relation to the argument
**P12 and P11.** Elish gives the strongest account in the project of where the person in the post's architecture ends up. The post gives a person authority to read evidence and halt (P15, P19). On Elish's cases, that person is the one blamed when the system fails, whatever the evidence says. The parallel is structural and by analogy; she did not study LLM agents.

**P5 (re-representation).** The TMI passage is an unplanned support for the paper's human-factors premise: a representation that omitted what the operator needed produced the wrong decisions, and the blame went to the operator (p. 44). It reads as evidence that interface design decides who can act, not as evidence about writing.

**D4.** Nadella's controls sit outside the model, but the person sits in the loop; Elish says that seat is where responsibility pools. This is a reason to ask who answers when a halt fails, a question the post is silent on.

**P10/D8.** Elish does not discuss conventions or their holders. Her point that certification bounds the technology and leaves interaction uncovered (p. 50) is about the regulator, not the owner.

**Facet check:** the facet (abstract and introduction only) states the definition correctly. Nothing contradicts it. The full text adds the TMI interface point and the certification argument, which the facet does not use.

## In conversation with
- `bainbridge1983ironies`: cited, with Parasuraman and Riley, for automation not relieving humans of hard tasks (p. 50).
- `parasuraman2000types`: the levels-of-automation framework used to define automation (n. 3, p. 41).
- `perrow1999normal`: Elish cites the 1984 edition of Perrow's *Normal Accidents* on TMI (pp. 42, 45); the bib holds a later edition.
- `green2022flaws` cites Elish for the pattern of operators blamed for system breakdowns (its p. 10).
- Leads not in the bib: Nissenbaum (1996) on accountability in a computerised society; Elish and Hwang (2015) on the history of autopilot litigation; Mindell (2015) on automation myths; Parasuraman and Riley (1997).

## Caution
A case-study essay on media and official reports, American context, with legal liability explicitly excluded (p. 52). Elish says moral crumple zones are not a property of every automated system. The cases are physical systems; the extension to AI agents is argued, not shown.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The journal PDF (Engaging STS 5, pp. 40-60), pdftotext; 13 quotations (all verbatim) with page locators checked page by page (PDF page + 39 = journal page: all matched); the case facts (TMI, AF447 pitot tubes, Therac-25, Uber, Google handoff) and the cited works (Bainbridge, Parasuraman and Riley, Parasuraman-Sheridan-Wickens 2000, Perrow 1984, Nissenbaum, Mindell, Elish and Hwang all appear). Not checked: the card's remark that green2022flaws cites Elish on its p. 10 (source outside this batch).

**Findings:** (1) The Therac-25 comparison conditions were conflated: Elish says the Therac-25 operator had no way of knowing of the malfunction, while TMI operators knew but lacked information or authority and AF447 pilots had information but were "systemically disempowered"; the card now says so and the locator is pp. 50-51. Otherwise no issues; the Caution's "not a property of every automated system" is supported (p. 51-52, "moral crumple zones are not a property of every complex and automated system").
