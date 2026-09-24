# Script — Do Triads Reduce to Dyads? The Ontology of Algorithmacy

<!-- Draft for the author's voice. One section per slide; each becomes that slide's speaker notes.
Target about 2,300 spoken words, about eighteen minutes at an even pace. Text in square brackets is a
stage direction and is not counted. -->

## Slide 1 — title
Thank you. My question today is an old one from logic, and I think the answer decides whether the word
on this conference's banner names anything at all.

## Slide 2 — the question
Here is the worry. Literacy is a competence for working with a medium — a text, a form, a ledger — that
answers to one party at a time. Algorithmacy, as I use the word, is a competence for coordinating through
a third that both parties determine. The platform that matches a driver and a rider is the obvious case.

If every relation among three can be rebuilt out of relations between two, then that third is just two
pairs stacked up, and algorithmacy is literacy applied twice. The word would name nothing new.

So the talk turns on whether triads reduce to dyads. Logicians have argued about exactly that for a
hundred and fifty years, and I want to walk through the argument before I say what our lab added to it.
One warning in advance: "reduce" is going to need a precise meaning, and by the end I'll have fixed one.

## Slide 3 — Peirce 1870
The argument starts with Charles Sanders Peirce, and it starts earlier than people usually say. Peirce
put both halves of his reduction thesis into a memoir he read in 1870. A relative term cannot be reduced
to absolute terms, he wrote, "nor can a conjugative term be reduced to any combination of simple
relatives". A conjugative term is a relation among three or more. And every relation among more than
two, he said, can be built from relations among three.

Notice what he did not do. He did not prove it. In the same memoir he admits, "I have, however, studied
this part of my notation but little." The proof came later, and it came as arithmetic.

## Slide 4 — the arithmetic
Think of a relation as a thing with blanks. Blank-gives-blank-to-blank has three. When you join two
relations you fill one blank of each with the same thing, so two blanks disappear. Join two dyads and
you get two plus two minus two: a dyad again. Join two triads and you get three plus three minus two:
four.

In 1897 Peirce put it this way: "artiads, or even-ads, can produce only artiads". Even plus even minus
two stays even, forever. Earlier he gave the picture: "no number of straight roads put end on end will
give more than two termini". Chains and rings are all that dyads can make. Triads can make anything.

That is the whole logical argument, and it has one premise hiding in it.

## Slide 5 — the junction
The hidden premise is about the junction. The arithmetic works only if a point where three lines meet
counts as a relation in its own right. Peirce said it does: "every node of bonds is equivalent to a
relative".

In 1886 Alfred Kempe attacked exactly there. Kempe redrew a triad as an extra unit with three plain links
coming off it, so no relation among three appears anywhere. Peirce took the objection seriously. He
granted in 1892 that Kempe "virtually shows that my algebra is perfectly adequate to expressing that A
gives B to C". What he denied was that expressing a triad this way builds it out of pairs. Kempe's extra
unit, he said, is itself the triad. So from its very first round the dispute has been about one thing —
the status of the junction.

## Slide 6 — giving
Peirce's favourite example shows what is at stake. Giving is not two handings. If A puts a book down
and C later picks it up, you have, in his words, "merely one dyadic relation followed by another".
Genuine giving is "A's making C the possessor according to Law". The three parties are held in one fact.

Keep that pair in mind: the real gift and its imitation. We will meet both again as models.

## Slide 7 — Simmel
That was the logic. Now the sociology. In 1902 Georg Simmel made the same step in the life of groups.
In a pair, he wrote, when one member refuses, "only the other remains, without any superindividual
energy". Add a third and something new appears: "each pair of elements are now joined by a broken line".
A and B are now connected directly and also through C.

Simmel is not arguing about definability. He is describing a change in the form of a group — the
mediator, the arbitrator, the third who profits from the quarrel of two. His point is that the step from
two to three changes what the group can do.

## Slide 8 — three is not enough
But Simmel also saw that three people are not automatically a triad. A third who stays distant from the
other two leaves, in his translator's phrase, "configurations of twos". The German is
Zweierkonfigurationen.

Our lab tested a version of this. Simmel's majority of three — each member does what the majority does —
comes out at Φ equal to zero, with no core. Three parties, and nothing binds them. So the count of three
is necessary. It is not sufficient. Hold on to that, because it is the clue to what a genuine triad is.

## Slide 9 — Löwenheim and Quine
Now the reply that made most philosophers stop believing Peirce. In 1915 Leopold Löwenheim showed that
you can code any relation as a relation between two things, provided you add new things — pairs — to
the universe. In 1936 László Kalmár proved a cousin of the result: for deciding questions of logic, one two-place relation letter is enough. In 1954 W. V. Quine published a two-page paper
showing that any theory can be rewritten with "only one predicate letter, and it a dyadic one".

Two facts about that paper matter. Quine assumes a fragment of set theory, so the pairs are there to
use. And on the pages we have checked, he does not mention Peirce at all. The reading of Quine as a
refutation of Peirce came from others. Robert Burch reports that the thesis was doubted by many after
Quine's proof. Quine himself never said so.

## Slide 10 — every reduction mints a third
Here is the pattern I want you to see. Kempe added a unit. Peirce, answering him, pointed to "this
action", an abstraction added to the universe. Löwenheim added pairs. Quine added sets of the form x, y.
Every one of these reductions works by minting a new object that stands for the whole tuple.

So what the reductions show is this: a relation among three is expressible with two-place relations over
a larger universe. What they do not show is that it can be composed from pairs among the same parties.
That second claim is the one coordination needs, and Sergiy Koshkin makes the same point about pairing:
it conceals the triad; it does not remove it. This slide is my argument, not a consensus.

## Slide 11 — both right?
The logicians after Quine made the disagreement precise. Hans Herzberger showed in 1981 that the thesis holds for one kind of construction and collapses under another. I am relying on Koshkin's account of that paper. Robert Burch built a whole algebra in which it
holds. Joachim Hereth Correia and Reinhard Pöschel gave the strongest proofs.

Where does that leave us? Burch, in the Stanford Encyclopedia, draws the peaceful conclusion: "both
Peirce and Quine were correct: the issue entirely depends on exactly what constructive resources are to
be allowed". Koshkin will not accept the truce: "It cannot simply be that Peirce and Quine are both
right." Both sides accept the same theorems. They disagree about which constructions are legitimate —
and the constructions split, again, on the three-way junction.

## Slide 12 — the lab's move
Here is our move. In logic a junction has no direction. A tuple doesn't say whether one thing fans out to
three, or three things fix one. Causation does say. So we asked the question causally, using integrated
information theory, IIT 4.0, as the instrument.

The criterion, fixed before our confirmatory runs: a genuine triad is a party jointly determined by two
others, inside a whole that does not factor. Here is the smallest case. M's next state is A and B
together. A and B each read M. IIT finds the whole irreducible, Φ equal to 2.0, with all three in the
core. And it finds M's own causes irreducibly spanning A and B. That is joint determination in a whole.

## Slide 13 — composing pairs
Now the test Peirce's thesis invites. We built every system in which each element simply copies one
other element — the causal version of a dyad — at three and four elements: 89 wirings. We had
pre-registered that none would contain a three-party fact. That prediction failed. Branches produced
three-party facts.

Then we looked at where they sat. Every one was on the effect side: one element fanning out to several.
Split the two directions and the cause side never goes above 2. No element is ever jointly determined by
two others. I want to be plain about this: that split came after the result, and it is close to true by construction, because a copying element has one cause. What it does is reproduce Peirce's arithmetic in causal
terms, with his branch in its place. It is a calibration, not a discovery.

## Slide 14 — Φ alone is not the test
The next slide is where the instrument earns its keep, because it separates things the logical debate ran
together. A mutual pair, a ring of copies and the imitation of giving are all wholes, at Φ equal to 2.0, and none contains a triad. The control, genuine giving and Peirce's sign with a working interpreter
contain joint determination inside a whole. And Simmel's majority has members jointly determined by the
other two while the system as a whole factors, at Φ equal to zero. We wrote that prediction down and published it before we ran it.

So wholeness and joint determination come apart in both directions. That is why our lab no longer calls
every irreducible system triadic. We used to. We now require joint determination as well.

## Slide 15 — two forms of coordination
Now back to the question on the banner. Literacy, in coordination terms, is a chain: a writer fixes a
text, and later a reader reads it. The text is inert while it is read. Even a long correspondence only
loops that chain into a ring, and a ring is a whole with no triad in it.

Someone here is about to say: Peirce made every sign triadic, so reading is triadic. Yes. But the sign triad sits inside one reader. It binds the text, what the text is about and one reader's
interpretation. It determines nothing on the other person's side. Every sign is triadic. The
coordination is a chain.

Algorithmacy's form is the control. The platform's next state is fixed by both parties at once, and both
read it. In that form, when one party acts, what the third does next turns on the other party she cannot
see. That is the demand a literate reader never faces.

I should concede something before you do. Simmel's arbitrator has exactly this form, and there is no
algorithm in it. The target is older than AI. What is new is that this form now runs through ordinary
work and ordinary life at scale.

## Slide 16 — what follows
So here is the argument, in the sense of "reduce" I promised to fix. Among fixed parties, one-input
mediation never composes joint determination. Joint determination inside a whole exists. So algorithmacy
has a target that literacy cannot build out of its own forms.

That is what I mean by an ontological argument for the necessity of algorithmacy. It is ontological
about the target: the kind of coordination exists, and it cannot be composed from literacy's kind. The
necessity is conditional: wherever coordination takes this form, the competence it demands is not
literacy twice.

Two limits. These are Boolean models, not people; no worker has been measured. And the strongest
objection is one Quine would enjoy: you have moved the argument from operations to units, because
whether M counts as one party is a choice. IIT has a test for that choice, and running it on this form
is our next step. Thank you.
