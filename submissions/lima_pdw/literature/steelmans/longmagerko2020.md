# Steelman — Long & Magerko (2020)

Read 2026-08-19 from the **camera-ready full text**, sixteen pages, CHI '20 Paper 598,
doi:10.1145/3313831.3376727. ACM refused every route; the authors' own copy at
`aiunplugged.lmc.gatech.edu` no longer resolves, and the Internet Archive holds it
(`web.archive.org/web/20250618030030/…/CHI-2020-AI-Literacy-Paper-Camera-Ready.pdf`). A camera-ready
is textually the published paper; **page anchors still need the ACM version**, and the competencies
are numbered rather than paginated, which is how to cite them.

An earlier version of this memo was written from the card and two secondaries and flagged three things
as unverified. All three are now settled, and the section below says how.

## Their claim, in their words

> We define AI literacy as a set of competencies that enables individuals to critically evaluate AI
> technologies; communicate and collaborate effectively with AI; and use AI as a tool online, at home,
> and in the workplace.

The framework is a literature review sorted into **five overarching themes, which they frame as
questions about AI**: *What is AI?*, *What can AI do?*, *How does AI work?*, *How should AI be used?*,
and *How do people perceive AI?* Seventeen competencies fall under them — **4 / 2 / 9 / 1 / 1** — with
fifteen design considerations for teaching them. Their own selection rule for what entered the list:
does it reflect the definition, is it supported by numerous sources, is it a useful guideline for
designers and educators.

All seventeen, verbatim, with the theme each sits under:

**What Is AI?**
1. *Recognizing AI* — "Distinguish between technological artifacts that use and do not use AI."
2. *Understanding Intelligence* — "Critically analyze and discuss features that make an entity
   'intelligent', including discussing differences between human, animal, and machine intelligence."
3. *Interdisciplinarity* — "Recognize that there are many ways to think about and develop 'intelligent'
   machines. Identify a variety of technologies that use AI, including technology spanning cognitive
   systems, robotics, and ML."
4. *General vs. Narrow* — "Distinguish between general and narrow AI."

**What Can AI Do?**
5. *AI's Strengths & Weaknesses* — "Identify problem types that AI excels at and problems that are more
   challenging for AI. Use this information to determine when it is appropriate to use AI and when to
   leverage human skills."
6. *Imagine Future AI* — "Imagine possible future applications of AI and consider the effects of such
   applications on the world."

**How Does AI Work?**
7. *Representations* — "Understand what a knowledge representation is and describe some examples of
   knowledge representations."
8. *Decision-Making* — "Recognize and describe examples of how computers reason and make decisions."
9. *ML Steps* — "Understand the steps involved in machine learning and the practices and challenges
   that each step entails."
10. *Human Role in AI* — "Recognize that humans play an important role in programming, choosing models,
    and fine-tuning AI systems."
11. *Data Literacy* — "Understand basic data literacy concepts such as those outlined in [107]."
12. *Learning from Data* — "Recognize that computers often learn from data (including one's own data)."
13. *Critically Interpreting Data* — "Understand that data cannot be taken at face-value and requires
    interpretation. Describe how the training examples provided in an initial dataset can affect the
    results of an algorithm."
14. *Action & Reaction* — "Understand that some AI systems have the ability to physically act on the
    world. This action can be directed by higher-level reasoning (e.g. walking along a planned path) or
    it can be reactive (e.g. jumping backwards to avoid a sensed obstacle)."
15. *Sensors* — "Understand what sensors are, recognize that computers perceive the world using sensors,
    and identify sensors on a variety of devices. Recognize that different sensors support different
    types of representation and reasoning about the world."

**How Should AI Be Used?**
16. *Ethics* — "Identify and describe different perspectives on the key ethical issues surrounding AI
    (i.e. privacy, employment, misinformation, the singularity, ethical decision making, diversity,
    bias, transparency, accountability)."

**How Do People Perceive AI?**
17. *Programmability* — "Understand that agents are programmable."

## Best version

Two clauses a reviewer will press, and the full text strengthens both.

**The definition names collaboration.** "Communicate and collaborate effectively with AI" is one of
three clauses. A paper whose contribution is a communication competency cannot wave past a framework
that already claims communication as a competency, and §3 has to answer in their wording rather than by
characterisation. Their own framing helps: they place AI literacy in the literacy family exactly as our
paper does — literacy as "the ability to express ourselves and communicate using written language,"
then digital, computational, scientific and data literacies by analogy. **We are running the same
move on the same shelf.** Saying so is better than letting a reviewer notice it.

**They also anticipate the interpretive problem.** Their *How do people perceive AI?* section opens on
folk theories — "informal theories…to perceive and explain how a system works" — and observes that these
theories "whether accurate or not, shape the nature of user interaction and experience." Their
"Interpreting AI Systems" passage argues that theory of mind, our way of explaining "other people's
behavior by attributing to them independent mental states," is not a reliable guide to AI. That is a
real hearing of interpretation under opacity, and it belongs in §3 rather than a bare "object of
knowledge" label.

## What they make the algorithm

An **object of knowledge**, and the seventeen bear it out. Recognise it, say what makes it intelligent,
know what it is good at, understand its representations, its decisions, its training steps, its data,
its sensors, its ethics, its programmability.

## Hunt for the counterpart

The full text settles this, and it settles it in our favour once the claim is stated correctly.

**The earlier absolute form was falsifiable and is now replaced by a checkable one.** Competency 10 is
titled *Human Role in AI*, and a reviewer with the table finds the title in seconds. Its text is the
answer: "Recognize that humans play an important role in **programming, choosing models, and
fine-tuning AI systems**." Humans enter the framework as the system's makers. Competency 5 names
"human skills" as the alternative to using AI. Neither gives another person a position in an
interaction the learner is conducting.

**Every "collaborate" and "communicate" in the paper points at AI or at pedagogy.** Of the paper's
instances: the definition's clause is "with AI"; a background sentence says misconceptions "limit
people's ability to effectively use, collaborate with, and act as critical consumers of AI"; the
remainder sit in the *design considerations*, where peer collaboration among learners appears as
Design Consideration 11 (*Social Interaction*) — "Consider designing AI learning experiences that
foster social interaction and collaboration." **Other humans appear in the pedagogy and never in the
competencies.** That distinction is the finding, and it is stronger than the sentence it replaces
because it can be checked in both directions.

The safe form for §3 and for `cards/long2020.md`: *no competency names another person as a party to
the interaction; the one competency that names humans at all names them as the system's designers.*

## The test

Yes, and the framework's own structure shows why. A person can satisfy all seventeen — she distinguishes
AI artifacts, argues about intelligence, names general versus narrow, knows what AI is good at, imagines
its futures, explains representations, decisions, ML steps, data, sensors, action, ethics and
programmability, and recognises that humans built the thing — and have no capacity whatever to make
herself legible to a human counterpart through a system that reads them both and commits a decision.
The framework scores her at ceiling. **All five of its organizing questions are questions about the
system.** Not one asks about a person reached through it.

## What we inherit

**The derivation contrast, and it is sharper with the selection rule in hand.** Their three questions —
does it reflect the definition, is it supported by numerous sources, is it useful to designers and
educators — admit a competency on the strength of the literature's agreement. Nothing in that rule
excludes an eighteenth, and nothing explains why nine belong under *How does AI work?* and one under
*How should AI be used?* Our facets are admitted by what the form withholds. The contrast lands more
cleanly here than against any other neighbour, and it should be made against their rule rather than
against their count.

**Their literacy-family argument**, which our locked introduction runs independently. They trace
literacy to written language and then to digital, computational, scientific and data literacies. Citing
that as the shelf we are both on costs a clause and pre-empts a reviewer who thinks the parallel is
ours alone.

**A design constraint on our own study.** Their setting is teaching, and AI literacy is what a teaching
context measures by default. If the Hult course teaches in this space and our instrument measures
algorithmacy, discriminant validity is a design problem for §5 rather than an abstract requirement.

## What adding items will not get

Ng, Leung, Chu and Qiao (2021) already compressed the seventeen into four cells — know and understand,
use and apply, evaluate and create, ethics — and later instruments inherit those cells. Every one is a
relation between a person and a technology. The framework's own themes are the ceiling: five questions
about a system admit only answers about a system, and the counterpart has nowhere to go.

## What is still open

Page anchors from the ACM version, for anything quoted in print. Competency numbers are the safer
citation form and the paper supports them. Nothing else on this construct is outstanding.
