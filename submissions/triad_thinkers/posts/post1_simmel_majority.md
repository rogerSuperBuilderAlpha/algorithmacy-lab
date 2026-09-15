# The Majority Binds No One: Simmel's Triad, Computed

*Roger Hunt · draft v1 (lab-generated for the author to revise; delete this byline before posting). Every
number below reproduces from `org_frontier/thinkers/simmel/` in the public lab repo; the paper behind the
post is `paper.md` there. Quotations are from Simmel's 1902 essay in the* American Journal of Sociology,
*Albion Small's translation, which is public domain. Sourcing note at the end.*

---

Two people who depend on each other and on no one else have a peculiar problem. If one of them stops,
there is nothing left. Georg Simmel put it this way in 1902: in a pair, "when he refuses to do this, only
the other remains, without any superindividual energy such as, even in the case of a combination of only
three, is in some measure present." The pair has no life over and above its members. Add a third person
and, Simmel says, something new appears — a whole that outlasts any one of them, a group that can be
spoken of as a thing.

That claim is the founding sentence of the sociology of small groups. Coalition theory, network analysis,
the study of brokers and middlemen and go-betweens all descend from Simmel's essay on the number of members
of a group. It has been quoted for a hundred and twenty years. It has never been computed, because the
claim is about structure — about whether three people bound together are *one thing* or *three things
standing near each other* — and until recently there was no way to put a number on that.

There is now, and I ran Simmel through it. Two of his five claims about the triad hold up exactly. Two
fail. One turns out to be half right. And the one that fails hardest is the one he leaned on most: the
idea that what makes three into a group is that two of them can outvote the third.

## What the instrument does

The tool is integrated information, a quantity written Φ, from a theory built for a different purpose
entirely — Giulio Tononi's integrated information theory of consciousness. I want to be plain about the
borrowing. I am not claiming that groups are conscious. I am using the theory's formal machinery for one
thing it does very well: it tells you whether a system of interacting parts is *irreducible* — whether you
can cut it into pieces without losing what it does — and if you cannot, it tells you *which* parts belong
to the irreducible core.

Here is how it works, without the mathematics. You describe each party by a rule: what it does next, given
what everyone did last. Then the theory tries every way of cutting the system into two pieces and asks how
much of the system's causal structure each cut destroys. If some cut destroys nothing, the system was never
one thing; it factors, and Φ is zero. If every cut destroys something, the system is irreducible, Φ is
positive, and the set of parts that cannot be cut apart is the core. On systems of three to five parties
the computation is exact — no estimate, no sampling, no p-value.

For three years my lab has run this on small models of coordination: a worker, a platform, a customer;
a maker, a dealer, a buyer. It has produced a few hundred results and a short list of structural laws.
Simmel wrote the first draft of those laws in prose. I wanted to know how much of it survives.

## The five claims

I took the 1902 essay and pulled out every claim about the triad that concerns *who is bound to whom* —
structure, not feeling. There are five. For each I wrote down what Simmel predicts, what my lab's earlier
results predict, and how the test would decide, before running anything.

**One. The superindividual triad.** In the triad, Simmel says, "each pair of elements are now joined by a
broken line" — A and B are connected directly *and* through C. That second route is what the dyad lacks.

**Two. The decisive step.** The change from two to three is a change in kind; adding a fourth or fifth is
a change in degree. "A third and fourth member of the alliance would produce no further essential variation
after the principal change had once occurred."

**Three. The majority.** "In a combination of two there is no majority which can override the individual,
and that occasion for such a majority is given so soon as a single unit is added." This is Simmel's
mechanism: the triad has power over its members because two can outvote one.

**Four. Mediator or arbitrator.** The nonpartisan third comes in two forms. The mediator carries each
side's claims to the other, stripped of heat, and "seeks to eliminate himself" — success means the parties
"unite directly" and no longer need him. The arbitrator decides; the parties "have put this ultimate
decision out of their own hands." Between them, Simmel says, lie "very many intermediate grades."

**Five. The *tertius gaudens*.** The third who profits from the quarrel of the other two. His strength,
Simmel insists, is not his own: "when the quantities of force are practically equal, a minimum of addition
often suffices." Two evenly matched rivals make a weak third all-powerful. One dominant rival makes him
worthless.

## What held

Simmel's first claim is exactly right, and in a way I did not expect. I modeled the pair as two parties
each reading the other, and the triad as three parties each reading the other two. The pair is irreducible
at Φ = 2. The triad is irreducible at Φ = 6 — the whole exceeds the members by three times as much. Then I
did what Simmel's "broken line" invites: I cut the direct tie between A and B and left only their common
relation to C. They stay bound. Φ = 2, all three in the core. The third holds the pair together after the
pair's own tie is gone. And when I cut the tie in the dyad, what remained was a single party reading
itself — "only the other remains," to the letter.

The surprise is where the broken line landed. The form Simmel describes — A and B each reading C, C
reading both — is the exact form my lab uses as its control, the reference triad every experiment is
checked against. Simmel's second route between a pair *is* the mediated triad. He drew our instrument's
calibration case in 1902.

His fifth claim also holds, and it holds through a mechanism he gestured at and could not name. I built a
small contest: A pushes for an outcome, B pushes against, T lends his weight to whichever side he favors,
and the outcome follows the heavier side. Then I varied only the weights. With A and B evenly matched, T is
pivotal three times in four, and T is in the core. Give A twice B's weight and T is pivotal half the time,
and still in the core, weakly. Give A three times B's weight and A decides alone; T is pivotal one time in
four and drops out of the core entirely. The third's standing tracks the rivals' balance exactly, as Simmel
said.

But look at who else is in the core. Under balance, the irreducible whole is T and the outcome — and *no
one else*. The two rivals who "paralyze each other" are outside it. Each is dispensable given the other;
neither is necessary to what the whole decides. Under the dictator, the core is A and the outcome. In every
case the core is whoever holds the decision, and only them. Simmel wrote that the weak third's position
"may attain to unlimited strength." Structurally, that strength is a monopoly: he is the only party the
whole cannot do without.

## What failed

The second claim fails on the quantity. I built mutual groups of two, three, four, and five, every member
reading every other, and computed Φ for each. The numbers are 2, 6, 12, 20 — the number of ties in the
group, n times n minus one. The increments grow: plus four, plus six, plus eight. On a graded measure of how
much a whole exceeds its parts, the step from two to three is not special. It is the largest *proportional*
jump — tripling, then doubling, then less — but Simmel's claim was that the form changes in kind at three
and stops changing, and the instrument sees only degree, growing without limit.

That would be a minor result if Simmel had not told us what the change in kind *was*. He did. It was the
majority. At three, and not before, two can override one. So the real test of the second claim is the third.

And the third claim fails completely. I built a triad in which each member does, next, whatever the majority
of the three did last — the plainest rendering of a group that can outvote its members. It has no
irreducible structure at all. Φ is zero. Not zero for the whole with a bound pair inside it; zero
everywhere, no core of any size. The majority triad is three things standing near each other.

For contrast I built the opposite: a triad in which each member does what *all three* did — unanimity,
where every member is necessary. Φ = 6, all three in the core.

The reason is a law my lab found years before it looked at Simmel: **substitutability collapses
irreducibility.** Under majority rule, any two members suffice. No member is pivotal in most situations;
each is replaceable by the other two. The whole's decision does not depend on any one of them — and a whole
that depends on no one binds no one. Simmel read the majority as the group's power over the individual.
The instrument reads it as the individual's irrelevance to the group. Those are not two descriptions of
one fact. They are opposites. To be outvotable is to be dispensable, and dispensable parts do not make a
whole.

## What was half right

The fourth claim, the scale from mediator to arbitrator, splits down the middle. The positions sort as
Simmel said. The arbitrator — whose decision both parties adopt — is in the core. The mediator — who filters
what passes between two parties that keep their own will and read only him — is in the core. The mediator
whose parties have "unite[d] directly" and no longer read him is out; the whole factors and only the pair
remains. He eliminated himself, as Simmel said he would.

What does not exist is the grade between them. Simmel's mediator, who "holds himself this side of actual
decision," binds the parties exactly as tightly as the arbitrator who takes it: Φ = 2 for both. Whether the
third decides or merely filters is a fact about his output. What the instrument reads is whether the
parties' next moves depend on him and his on them — and in both forms they do. The "very many intermediate
grades" Simmel saw are grades of something, but not of this.

## What Simmel found, and what he was looking for

Put the five together and one condition sits beneath all of them. A party belongs to the whole when the
whole's decision depends on it and its next move depends on the whole. Every member necessary: the mutual
triad, Φ = 6. One party holding the decision: the *tertius*, alone in the core with the outcome. The third
that both parties read: mediator and arbitrator alike. No member necessary: the majority, Φ = 0. And the
bare count of members, which the condition never mentions — which is why the second claim failed.

Simmel found the cases. He found them with nothing but a pen and a century of European history, and three
of the five are right or nearly right. What he did not have was the condition, and so he attached the
triad's power to the wrong mechanism. He thought three became a group because two could outvote one. Three
becomes a group when none of the three can be done without. The majority is the one arrangement in which
all of them can.

That matters beyond Simmel. Every institution that binds people by vote has been told, since 1902, that the
vote is what makes it a body. On this criterion the vote is what makes it a crowd. The body is wherever the
decision cannot be taken without you — which is a smaller place than the ballot suggests, and a more
exposed one.

## What this is not

These are results about Boolean models with three to five parts, not about any three people. A party in the
model is a bit with a rule; Simmel's parties have jealousy, intimacy, and a history, none of which a bit
carries. Each claim was rendered as one form, and a different rendering could move a borderline case — the
mediator especially. The hypotheses and the test rules were written down before any computation ran, and
the refutations are refutations of those renderings under those rules. The paper lists the alternatives
that were not run. I would rather report two clean failures than five rendered-to-fit successes, and the
paper says which is which.

Next in the series: Peirce, who claimed in 1897 that a genuine triadic relation cannot be built out of pairs
— which is not a claim about groups at all, but is, word for word, what the instrument tests.

---

*Sourcing.* Simmel, G. (1902). "The Number of Members as Determining the Sociological Form of the Group,"
Parts I and II, *American Journal of Sociology* 8(1): 1–46 and 8(2): 158–196; trans. A. W. Small. Public
domain. The dyad passages are Part I, pp. 45–46; the majority, nonpartisan, and *tertius gaudens* passages
are Part II. The instrument: Albantakis et al. (2023), *PLOS Computational Biology* 19(10), and Mayner et
al. (2018), *PLOS Computational Biology* 14(7), for PyPhi. Code, hypotheses, and results:
`org_frontier/thinkers/simmel/` in the algorithmacy-lab repository; every number is under continuous
integration and re-derives from a committed script.
