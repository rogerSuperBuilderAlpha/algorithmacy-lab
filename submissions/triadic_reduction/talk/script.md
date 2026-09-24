# Script — Do Triads Reduce to Dyads? The Ontology of Algorithmacy

<!-- Draft for the author's voice. One section per slide; each becomes that slide's speaker notes.
Revised 2026-09-24 after the Phase 6 correctness panel. Text in square brackets is a stage direction and
is not counted. -->

## Slide 1 — title
Thank you. My question today is an old one from logic, and I think the answer decides whether the word
on this conference's banner names anything at all.

## Slide 2 — the question
Here is the worry. Literacy is a competence for working with a medium that answers to one party at a
time: a letter, a notice, a manual. One person fixes it, another reads it. Algorithmacy, as I use the
word, is a competence for coordinating through a third that both parties determine, and that acts back
on both. A platform that matches a driver and a rider is the picture most of us have in mind.

If every relation among three can be rebuilt out of relations between two, then that third is just two
pairs stacked up, and algorithmacy is literacy applied twice. The word would name nothing new.

So the talk turns on whether triads reduce to dyads. Logicians have argued about exactly that for a
hundred and fifty years, and I want to walk through the argument before I say what our lab added. One
warning: "reduce" is going to need a precise meaning, and halfway through I'll fix one.

## Slide 3 — Peirce 1870
The argument starts with Charles Sanders Peirce, and earlier than people usually say. Peirce put both
halves of his reduction thesis into a memoir he read in 1870. A relative term cannot be reduced to
absolute terms, he wrote, "nor can a conjugative term be reduced to any combination of simple
relatives". A conjugative term is a relation among three or more. And every relation among four or
more, he said, can be built from relations among three.

Notice what he did not do. He gave no argument for it there. The argument came later, and it came as
arithmetic.

## Slide 4 — the arithmetic
Think of a relation as a thing with blanks. Blank-gives-blank-to-blank has three. When you join two
relations you fill one blank of each with the same thing, so two blanks disappear. Join two dyads and you
get two plus two minus two: a dyad again. Join two triads and you get three plus three minus two: four.

In 1897 Peirce put it this way: "artiads, or even-ads, can produce only artiads". Even plus even minus
two stays even, forever. Elsewhere he gave the picture: "no number of straight roads put end on end will
give more than two termini". Chains and rings are all that dyads can make. Triads can make anything.

That is the logical argument, and it rests on one premise.

## Slide 5 — the junction
The premise is about the junction. The arithmetic works only if a point where three lines meet counts as
a relation in its own right.

In 1886 Alfred Kempe challenged the negative clause. He redrew a triad as an extra unit with three plain
links coming off it, so that no relation among three appears anywhere. Peirce took the objection
seriously. In 1892 he answered that Kempe's picture still contains mediation, in "the attachment of lines
to spots", and that the extra unit comes from an abstraction the diagram never shows being made. In 1897
he stated the premise outright: "every node of bonds is equivalent to a relative". So from the first
round the dispute has been about the junction, and about the object that fills it.

## Slide 6 — giving
Peirce's favourite example shows what is at stake. If A throws something away and it happens to hit C,
you have, in his words, "merely one dyadic relation followed by another". Genuine giving is "A's making C
the possessor according to Law". The three parties are held in one fact.

Keep that pair in mind, the real gift and its imitation. We will meet a model of each.

## Slide 7 — Simmel
That was the logic. Now the sociology. In 1902 Georg Simmel made the same step in the life of groups. In
a pair, he wrote, when one member refuses, "only the other remains, without any superindividual energy".
Add a third and something new appears: "each pair of elements are now joined by a broken line". A and B
are still connected directly, and now also through C, and the same holds for every pair.

Simmel is not arguing about definability. He is describing a change in the form of a group: the
mediator, the arbitrator, the third who profits from the quarrel of two.

## Slide 8 — three is not enough
But Simmel also saw that three people are not automatically a triad. He set aside a third so distant
from the other two that it unites them only as a pair facing it. There he finds, in his translator's
phrase, "configurations of twos". The German is Zweierkonfigurationen.

So three is necessary. It is not sufficient. Hold on to that, because the question of what makes three
into one is where our lab comes in.

## Slide 9 — Löwenheim, Kalmár, Quine
First, though, the result that led many to doubt Peirce, although none of its authors aimed it at him.
In 1915 Leopold Löwenheim showed that two-place relations suffice to express any relation, provided you
add new objects, pairs, to the domain. In 1936 László Kalmár showed that, for deciding satisfiability,
a single two-place relation is enough. And in 1954 W. V. Quine published a short paper showing that any
first-order theory can be rewritten with "only one predicate letter, and it a dyadic one".

Quine assumes a fragment of set theory, so the pairs are there to use. On the pages we have checked he
does not mention Peirce, and Koshkin reports that he never connected the result to Peirce. Others did.

## Slide 10 — every reduction keeps the junction
Here is what these reductions do. Take "A gives B to C". Mint a new object, g, the giving. Now write three
pairs: g's giver is A, g's gift is B, g's recipient is C. Every relation is two-place. But g is a new
thing, and it holds the three together. Kempe's unit is that object. So is Peirce's "this action", and so
are Löwenheim's and Quine's pairs.

The logicians made this exact. Hereth Correia and Pöschel proved, and Koshkin has since sharpened, that
dyads build a triad only with a three-way junction: a minted object, or a variable shared three ways.
Without one, never. Koshkin puts it in logical terms: the pairing construction hides a three-way
junction.

Why should coordination care about the difference? Because a coordination between two people presupposes
that each can act on their own. Fuse them into one unit, or route them through a new object, and you have
changed who is coordinating.

## Slide 11 — both right?
Robert Burch built an algebra, PAL, and proved the thesis in it, but only with a restriction on when
products may be formed. Hereth Correia and Pöschel removed the restriction and gave the strongest proofs.
Hans Herzberger, in 1981, had shown that the thesis holds for one kind of construction and collapses
under another. I am relying on Koshkin's account of that paper.

Where does that leave us? Burch, in the Stanford Encyclopedia, draws the peaceful conclusion: "both
Peirce and Quine were correct: the issue entirely depends on exactly what constructive resources are to
be allowed". Koshkin will not accept the truce: "It cannot simply be that Peirce and Quine are both
right." His view is that if you allow any construction and count each three-way junction as a triad,
the thesis comes out true. The split, again, is over the junction.

## Slide 12 — the lab's move
Here is our move. In logic a junction has no direction. A tuple doesn't say whether one thing fans out to
three, or three things fix one. Causation does say. So we asked the question causally, with integrated
information theory, IIT 4.0, as the instrument. IIT asks one question of a system: cut it into
independent parts, and what do you lose? Φ measures what is lost under the least damaging cut. If Φ is
zero, the system splits into parts. If Φ is above zero, every cut loses something.

Now the sense of "reduce" I promised. From here on, to reduce a form is to rebuild it among the same
parties, out of links in which each element answers to just one other. In Quine's sense, triads reduce.
In this sense, the question is open.

And the criterion: a genuine triad is a party jointly determined by two others, inside a whole that does
not factor. I chose that criterion after our first probes. We then pre-registered a test of it and ran
it on new cases. Here is the smallest example; we call it the control. M turns on only when A and B are
both on, like a deal that closes only if both sign, and A and B each follow M. Φ is 2.0, with all three in
the core. The two arrows into M are not two pairs: M's rule takes A and B together.

## Slide 13 — composing pairs
Now the test Peirce's thesis invites. We built every system in which each element simply copies one
other element, at three and four elements: 89 wirings. In these models every element, the parties
included, answers to one other. We had pre-registered that none would contain a three-party fact. That
prediction failed. Branches made three-party facts.

Then we looked at where they sat. Every one was a fan-out: one element read by several. And the systems
that had them all split into parts, at Φ equal to zero. On the cause side, a fact never spans more than
the element and its one source. No element is ever jointly determined by two others. That split came
after the result, and it is close to true by construction, because a copying element has one cause. What
it does is reproduce Peirce's arithmetic in causal terms, with his branch in its place.

## Slide 14 — Φ alone is not the test
This is where the instrument earns its keep, because it separates things the logical debate ran together.
A mutual pair, a ring of copies and our model of the imitation of giving are all wholes, at Φ equal to
2.0. The imitation model closes the loop, because what the receiver holds feeds back to the giver. That
return makes it one whole, but no party in it is fixed by two others.

The control, genuine giving, and a model of a sign whose interpretation acts back on its object all have
joint determination inside a whole. And in a fresh sample we pre-registered, eleven of thirty forms have
a party jointly determined by two others while the system splits into parts. So wholeness and joint
determination come apart in both directions. That is why our lab no longer calls every irreducible system
triadic. We used to. We now require joint determination as well.

## Slide 15 — two forms of coordination
Now back to the question on the banner. Literacy, in coordination terms, is a chain: a writer fixes a
text, and later a reader reads it. The text is inert while it is read. Even a long correspondence only
loops the chain into a ring, and a ring is a whole with no triad in it.

Someone here is about to say: Peirce made every sign triadic, so reading is triadic. Yes. But the sign
triad closes in one reader. It binds the text, what the text is about and one reader's interpretation,
and it determines nothing on the other person's side. Every sign is triadic. The coordination is a chain.

Algorithmacy's form is the control: a third set by both parties at once, which both then read. A
matching platform plausibly has this form. Whether a given platform does depends on its rule, and no one
has modelled that yet. In this form, one party's own act settles what the third does only some of the
time. Otherwise it turns on the other party's act, so she has to infer the side she cannot see.

I should concede something before you do. Simmel's arbitrator meets this criterion, and there is no
algorithm in it. So does a tally that both sides write and both read. The criterion is about form, not
about machines. My historical premise, not a lab result, is that this form now runs through ordinary work
and ordinary life at scale, mostly through algorithms. That is why I use the name.

## Slide 16 — what follows
So here is the argument, in the sense of "reduce" I fixed. Among fixed parties, one-input determination
never composes joint determination. Joint determination inside a whole exists. So coordination through a
jointly determined third has a target of its own.

One premise carries us from form to competence: to coordinate through such a third, you have to
anticipate what it will do, and here that means inferring the party you cannot see. Grant that, and the
competence is not literacy twice. That is what I mean by an ontological argument for the necessity of
algorithmacy. It is ontological about the target: the kind exists, and literacy's forms cannot compose
it. The necessity is conditional: wherever coordination takes this form, the competence it demands is
algorithmacy.

Two limits. These are Boolean models, not people: no worker has been measured and no platform's rule
modelled. And the strongest objection is one Quine would enjoy: whether A and B count as separate units
is a choice. IIT has its own test for that choice, and running it on this form is our next step. Thank
you.
