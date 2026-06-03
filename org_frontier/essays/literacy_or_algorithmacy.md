# Literacy or Algorithmacy? Borrowing a Consciousness Measure to Read an Org Chart

*How researchers actually use PyPhi, and why the same tool can decide whether a way of
coordinating demands an old competence or a new one.*

---

Two drivers work the same delivery app in the same city. They start the week with the same rating,
the same car, the same neighborhood. One ends the month up; the other ends it deactivated. The app
is identical. The roads are the same. Something about how each driver coordinates with a system that
never explains itself made the difference. The interesting question is not who tried harder. It is
what competence the situation demanded, and whether either driver had it.

That question has an old answer and a new one. The old answer is literacy: learn to read the
interface, the ratings, the messages, the terms of service. The new answer is that reading the
interface is not enough, because the driver is not coordinating with the app. The driver is
coordinating with a customer, a restaurant, a dispatching algorithm, and a pricing model all at
once, through a system that interprets all of them and commits decisions none of them control. That
is a different shape of problem. It may demand a different competence. This essay argues that you
can tell which one a situation demands, and that the tool for telling is a piece of software written
to study consciousness.

The software is PyPhi. The competence question is literacy versus algorithmacy. The bridge between
them is a number called Φ. The rest of this essay explains all three, in that order, and then makes
the case that the bridge holds.

## Part one: what PyPhi is, and who actually uses it

PyPhi is the reference implementation of Integrated Information Theory, written by William Mayner
and colleagues in Giulio Tononi's lab at Wisconsin. Integrated Information Theory, IIT, is a theory
of consciousness. Its central claim is that a system is conscious to the degree that its parts form
an integrated whole whose causal power cannot be reduced to the causal power of the parts taken
separately. The quantity that measures this irreducibility is Φ, phi. A system with high Φ is one
whose behavior you cannot explain by cutting it into independent pieces and describing each piece on
its own. A system with Φ of zero falls apart cleanly: cut it the right way and nothing is lost,
because the pieces never really acted as one thing.

PyPhi computes Φ exactly. Give it a small system described as a set of elements that switch on and
off according to fixed rules, and it returns not just the number but the whole cause-effect
structure: which subsets of the system make a difference to which others, and by how much. The 2018
paper that introduced it calls it "an up-to-date reference implementation of the formalisms of
integrated information theory." That word, reference, matters. When other researchers want to know
the true value of Φ for a system, they run PyPhi. It is the ground truth against which everything
cheaper is measured.

We ran a survey of how the world actually uses this tool. Not how the theory papers say it could be
used, but what shows up in the published record. The picture is sharp, and it has three parts.

The first community is artificial life. Researchers evolve tiny artificial agents called animats,
small controllers built from logic gates, and let them adapt to mazes and other environments over
many generations. A standard animat has about eight binary elements: two sensors, four hidden units,
two motors. The foundational result of this line is that integrated information rises with fitness.
As the animats get better at their task, the Φ of their controllers goes up, and it goes up far more
tightly than cruder measures of how much the agent's past predicts its future. In one early study
the correlation between the main complex's Φ and fitness was about 0.94, against about 0.34 for
predictive information. The animat work is where IIT first showed that its number tracks something
real about how a system is organized.

The second community is complex systems and a bit of biology. Here the systems are abstract: logic
gate networks, random Boolean networks, the kind of toy dynamical systems that complexity science
has studied for decades. In 2021 the same Wisconsin group extended PyPhi past binary elements to
handle systems whose parts take more than two values, and demonstrated it on a small model of the
p53-Mdm2 regulatory network, a genuine piece of cell biology. This is the frontier where IIT reaches
toward living systems, still in proof-of-concept form.

The third community is neuroscience, and here the story turns. Neuroscientists want to use Φ to
index the level of consciousness in a real brain, across wakefulness, sedation, anesthesia, and
seizures. They cannot. A real brain has far too many parts. So they do not run PyPhi at all. They
substitute a tractable approximation, an autoregressive proxy called Φ_AR, and they estimate it from
small random subsets of EEG channels, and they report the result as a lower bound on the true value
they cannot compute. One study notes that a 128-channel recording would require something like
1.8×10^38 distinct ways of cutting the system in two. So it sampled eight channels at a time, six
hundred times over, and averaged. An SEEG study of epilepsy says plainly that its numbers "can only
be a lower bound on the true Φ values," because electrodes in a few spots cannot stand in for a whole
brain.

That gap between the exact tool and the real target defines the field's central problem, and it has
a name worth keeping: the proxy problem. Φ is defined exactly. Φ is computed exactly only on small
systems. On anything large or real, researchers compute a cheaper stand-in and hope it tracks the
real thing. A whole companion literature exists to build better stand-ins: heuristic search methods,
geometric approximations, and most recently graph neural networks trained on exact PyPhi outputs to
predict Φ for systems too large to compute directly. In every case PyPhi is the teacher. The
approximations are the students.

Behind all of this sits one hard fact. Exact Φ is expensive in a way that does not soften with
better hardware. The cost grows as roughly n^5 times 3^n, where n is the number of elements. The
practical ceiling is around ten to twelve elements. Seven elements already took hours on dozens of
processors. This ceiling is not a bug in PyPhi. It is intrinsic to what exact Φ asks: consider every
way of partitioning the system, score each one, and find the partition that the system resists
least. The number of partitions explodes. So every honest application of IIT lives under this
ceiling or pays the proxy tax to escape it.

One more fact about the tool, because it matters for anyone building on it. IIT has versions. The
current formulation is IIT 4.0, published in 2023, which rebuilt the theory's foundations and
introduced a cleaner measure of how much difference a mechanism makes. PyPhi tracks 4.0 on a
dedicated branch, while its stable documentation still describes the older 3.0. Anyone starting now
should build on 4.0, and should say which version they used, because the two do not always agree.

So that is the survey, in one paragraph. PyPhi is the exact reference implementation of a
consciousness measure. It is used on tiny evolved agents, on abstract networks, and, by proxy, on
brains. It is bounded by a hard size ceiling. And across every primary source we checked, it has
never once been pointed at an organization, a team, a market, or any human coordination structure.
The domain tags on the software itself stop at biology. That absence is the opening this essay is
about.

## Part two: literacy, and the competence that writing created

Step away from the software for a moment and consider a much older transition.

Before writing there was speech. A culture that has only speech can do a great deal. It can tell
stories, pass down law as memory, organize a hunt, run a household, settle disputes in front of
witnesses. What it cannot do is hold a contract still for a hundred years, compare two ledgers
written in different cities, or run a bureaucracy whose rules outlive the people who made them.
Writing made those things possible. It did so through three properties speech lacks. Writing
persists: it stays fixed while memory drifts. Writing is portable: it moves without its author.
Writing is comparable: two documents can be laid side by side and checked against each other.

From those three properties came codified law, double-entry bookkeeping, and the administrative
file. None of these is just speech written down. Each is a new form of coordination at a scale
speech cannot reach. And each demanded something new of the people inside it. The competence is
literacy, and literacy was not an add-on to oral skill. It
restructured what a person had to be able to do to take part in social life. A scribe is not a
better talker. A clerk is not a more careful rememberer. The transition from oracy to literacy was a
change in kind, not a change in degree.

Two qualifications keep this from being a fairy tale. First, the change was slow and contested.
Print took centuries to settle, and for a long time printed books were as full of error and dispute
as anything else. So an in-kind transition need not be sudden or clean. The unevenness of a
transition is not evidence that it is not happening. Second, literacy's effects are not magic. A
long tradition in literacy studies showed that reading and writing do not automatically rewire a
mind in some universal way. Their effects depend on the practices they are embedded in. This is true
and it does not undercut the argument, because the claim here is not about cognition in the abstract.
It is about coordination. Writing makes certain forms of coordination materially possible. Those
forms are historically locatable and unevenly distributed, exactly as the practice-based view says.
The competence follows the form.

Now bring this frame to the present. The dominant vocabulary for life with algorithms is built on
the word literacy. Algorithmic literacy, AI literacy, data literacy, and their cousins all describe
something a person knows or is aware of: how a recommender works, what a model can and cannot do, how
to read a feed critically. This vocabulary treats the algorithm as a medium to be read. It puts a
person on one side and a system on the other, and asks whether the person understands what the system
is doing to them.

That picture is dyadic. Two parties, a person and a medium. The medium conveys, scores, or
interprets, but it does not pursue its own goals across two different humans at once. For a great
deal of digital life the dyadic picture is right, and literacy is the right word. Reading a privacy
policy is a literacy task. Understanding why a video was recommended to you is a literacy task. If
that were all platforms did, there would be nothing new to name.

## Part three: algorithmacy, and why the surface lies

Platforms do more than that, and the delivery driver from the opening shows it.

The driver is not on one side of a medium. The driver is trying to coordinate with a customer she
will never meet, through a system that reads her behavior and the customer's behavior at the same
time and commits decisions, about routing, pricing, ranking, and deactivation, that neither of them
controls. The customer is in the same position from the other side. The system sits in the middle
and pursues objectives of its own, set by a company neither party works for. This is not a person
reading a medium. It is two humans coordinating through a third party that interprets both of them.

That third structure has a shape, and the shape is triadic. The dissertation this lab grows out of
gives the new competence a name to match: algorithmacy. Algorithmacy is the integrated competence
through which a worker coordinates with another human through an algorithmic third party that
interprets both sides and commits determinations neither side controls.

It has three parts, and the driver shows each one. The first is inferential. She cannot see the
customer, the dispatcher, or the model that ranks her. She sees only outcomes: a ride offered or
withheld, a tip given or not, a rating that moved. From those outcomes she has to reconstruct what
the hidden parties want and how the system is reading her. This is real work, and the research on
how gig workers build folk theories of their platforms shows it is effortful and consequential. The
driver who infers well gets more of the rides she wants. The second part is translational. Her real
intent, take the good jobs, avoid the traps, build a reputation, has to be compressed into the few
signals the system accepts: accept or decline, this route or that one, available or offline.
Something is always lost in that compression, and the skilled driver knows what is lost and works
around it. The third part is temporal. The rules change while she uses them, because the system
learns and updates. A strategy that worked last month stops working, with no announcement. She has
to detect the shift and adapt against a moving target. These three compose into one capacity, and
the claim is that this capacity is to platform coordination what literacy was to written
coordination. A change in kind, demanded by a new form, unevenly held.

Here is the hard part, and the part that makes a measurement tool necessary rather than optional.
You cannot tell whether a situation is dyadic or triadic by looking at it. The surface lies.

Count the parties and you learn nothing reliable. A three-party arrangement can be secretly dyadic.
Picture a worker, a manager, and a scheduling tool where the tool only relays the manager's
decisions without interpreting anyone. Three names are involved, but the structure factors cleanly:
the tool is a wire, the manager is the real counterpart, and the worker is in an ordinary
two-party relationship dressed up as three. Literacy handles it. Now picture the opposite. A worker
alone with an app, no other human visibly in the loop, just her and a screen. It looks like the most
dyadic situation imaginable. But if that app is interpreting her behavior on behalf of customers,
advertisers, or a labor market she never sees, and committing outcomes that bind all of them, then
the structure is triadic even though only one human is visibly present. The interface shows two
parties. The structure has three.

So the number of parties does not settle it. The kind of interface does not settle it. A friendly
chat window can sit on top of a triadic structure, and a forbidding multi-party dashboard can sit on
top of a dyadic one. If you want to know which competence a coordination form demands, you need to
look past its surface to its structure, and structure is exactly the thing that is hard to read by
eye. This is where the consciousness measure earns its place.

## Part four: the bridge

Strip Φ of its philosophy and look at what it actually measures. It measures irreducibility. It asks
whether a system's behavior, taken as a whole, can be reconstructed from its parts acting
independently. If the answer is yes, the system factors, and Φ is zero. If the answer is no, if there
is some genuine joint determination that no partition can recover, then Φ is positive, and its size
reflects how much is lost when you try to cut the system apart.

That is precisely the dyadic-versus-triadic question, in formal dress. A dyadic coordination form is
one that factors: the third element is a wire, and once you account for it the situation reduces to
two parties acting through a passive channel. A triadic form is one that does not factor: the third
party is doing real interpretive work that binds the two humans together, and no cut recovers the
whole. Reducible means dyadic. Irreducible means triadic. And irreducibility is what Φ measures.

So the theory is this. Model a coordination form as a small discrete system, with the worker, the
system, and the counterpart as elements that influence one another by fixed rules. Run PyPhi. If Φ
over the partition the system resists least comes out at zero, the form is dyadic, and the competence
it demands is literacy. If Φ comes out positive, the form is triadic, and the competence it demands
is algorithmacy. PyPhi becomes an instrument that reads the structural fact the surface hides, and
returns a verdict on which kind of competence the situation requires.

A concrete case makes this less abstract. Take three elements: a worker, a counterpart, and a
system, each either active or not at each step, each updating by a fixed rule from the others' states
the step before. Suppose the system's next state is some joint function of the worker and the
counterpart, the worker's next state depends on the system, and the counterpart's does too. Now ask
PyPhi the one question that matters: is there any way to cut this three-element system into pieces
that lose nothing? If the worker and the counterpart also talk to each other directly, there is. You
can often split the system off and describe the two humans as a pair coordinating on their own, with
the system as a passive add-on. That cut survives, Φ is zero, and the form is dyadic. Now suppress
the direct channel. Force the worker and the counterpart to influence each other only through the
system, never directly. The pair no longer factors, because everything that passes between them runs
through the interpreting third party, and cutting the system out destroys the coordination it was
carrying. No partition survives. Φ goes positive, and the form is triadic. The single structural
change that flips the verdict is whether the humans can reach each other without the system in the
middle. That is the endpoint result the dissertation found to be robust, and it is exactly the
condition that distinguishes a platform from a phone book.

This is the move the whole lab is built on. It is a modeling choice, not a discovered identity. The claim is not that a delivery platform is
literally conscious, or that organizations have minds. The claim is narrower and more defensible.
The structural property that IIT built Φ to detect, irreducibility of joint causal determination, is
the same structural property that separates triadic coordination from dyadic coordination. So the
tool built for the first job can do the second job, as long as you are honest that you are borrowing
the measure for its formal content and leaving the metaphysics at the door.

This matters because IIT as a theory of consciousness is contested. In 2023 a large group of
scientists and philosophers signed an open letter calling it pseudoscience, and critics have long
argued that its consciousness claims are hard or impossible to test. Borrowing Φ here does not take a
side in that fight, because the borrowing does not rest on IIT being a correct theory of
consciousness. It rests on Φ being a well-defined measure of causal irreducibility, which is a
mathematical fact about the measure regardless of what it means for minds. The consciousness debate
is about whether irreducible cause-effect structure is what experience is. The use here is about
whether irreducible cause-effect structure is what triadic coordination is. The second question can
be answered yes while the first stays open. Keeping the two apart is what makes the borrowing
defensible, and it is why the strongest objections to IIT as a theory of mind leave this application
untouched.

Why borrow Φ instead of using a cheaper test for whether a system factors? Because Φ is strictly
stronger. Across the complete family of small three-element coordination forms, the dissertation
found that the Φ verdict disagrees with a cheap factorization test on more than forty percent of
cases. The cheap test asks a coarse question and gets a coarse answer. Φ asks whether there is any
partition at all that the system survives, weighs every one, and reports the binding that no cut can
break. That extra strength is the reason to pay for the harder computation when the case is close.

## Part five: what the tool can and cannot do, said plainly

A theory is only as good as its limits, so here are the limits, drawn from the work that has already
tested this bridge rather than from hope.

The binary verdict is the solid part. Dyadic versus triadic, Φ equals zero versus Φ greater than
zero, holds up. It holds up at its endpoints in particular: when you suppress the direct channel
between the two human parties and force them to coordinate only through the interpreting system, the
form classifies as triadic, and when you open that channel back up, it can fall back to dyadic. That
is the central prediction, and it survives. An agent-based experiment backs it behaviorally:
coordinating through a strict joint determination with no direct channel is markedly harder than
coordinating through the same determination with a channel left open, and the difficulty gap is
large and stable even after thousands of rounds of practice. The structural verdict and the lived
difficulty point the same way.

The graded version is the part that fails. The
temptation is to read the size of Φ as a readability score, a dial from easy to hard. It does not
work. The magnitude of Φ turns out to be dominated by a technical feature of how you encode the
form's decision rule, to the point where one kind of rule inflates Φ by an order of magnitude beyond
anything a real organization would show. Different reasonable ways of encoding the same coordination
form give different magnitudes. So Φ is a classifier and, at most, a rough ordinal hint. It is not a
ruler. The earlier hope of a smooth difficulty scale was withdrawn after the numbers refused to
support it, and that withdrawal is a feature of the work, not an embarrassment to be hidden.

The modeling commitments are real and have to be declared every time. The verdict depends on
representing the coordination at the right layer, on a fixed rule for how you carve the system's
states, and on reading irreducibility over the partition the system resists least. Change those
commitments and you can change the verdict. This is not a flaw unique to this application. It is the
ordinary condition of any formal model. But it means the tool produces a verdict relative to a
stated model, and the honesty lives in stating the model.

And the ceiling from part one never goes away. Exact Φ is feasible only for small systems. This
turns out to be less of a problem here than in neuroscience, because the units of coordination that
matter are small. A worker, a system, and a counterpart is three elements. A handful of roles around
a decision is a handful of elements. The structures where the literacy-or-algorithmacy question
actually bites tend to live comfortably under the ten-element ceiling. Where they do not, the same
proxy and approximation tools the neuroscientists built, the autoregressive estimates and the neural
network predictors, are available to borrow in turn.

## Part six: why this is worth doing, and the invitation

The survey found a clean white space. PyPhi has been pointed at evolved agents, at abstract
networks, at brains by proxy, and at the edge of cell biology. It has not been pointed at human
coordination. No published work we found applies exact IIT Φ to organizations, teams, markets, or
institutions. We hold that claim carefully, because proving an absence is hard and a dedicated sweep
of the management literature could still turn something up. But the tool's own documentation, and
the whole arc of its use, stops short of the social world.

That is a strange gap, because the question the tool answers is exactly the question organizational
theory keeps asking in other words. When does adding a system in the middle change the kind of
coordination, rather than just speeding up the old kind? When is a platform a new organizational form
and not a faster version of an old one? When does a worker face something her training never prepared
her for, not because the task is harder but because its structure is different? These are
irreducibility questions wearing organizational clothes, and there has been an exact instrument for
irreducibility sitting in a neuroscience repository the whole time.

Organizational theory has a habit of borrowing formal models from other fields, and it has done well
by the habit. Population biology gave it organizational ecology, the study of how organizational
forms are born and die in populations. Microeconomics gave it transaction-cost theory, the account
of why some exchanges happen inside firms and others in markets. Each borrowing took a formal tool
built for one purpose and found that it answered a structural question the borrowing field had only
been able to gesture at. Integrated information is a candidate for the next such borrowing, and the
structural question it answers is the one the platform literature has been circling. Scholars have
argued that the platform is a distinct organizational form, a third coordination mechanism alongside
the market and the hierarchy, with its own triangular geometry. That argument is about structure,
and it has lacked a structural instrument. Φ is one.

The stakes are not only theoretical. The reason the two delivery drivers ended the month so
differently is that the form they worked inside demanded a competence the labor market does not yet
name, let alone teach. Training programs, worker protections, and platform regulations are all being
written right now on the assumption that the relevant skill is literacy: teach people to read the
app and understand the terms. If the form is actually triadic, that assumption trains workers for
the wrong problem. Knowing which forms are which is not an academic nicety. It decides whether a
training curriculum, a labor standard, or a platform audit is aimed at the situation workers are
actually in. A reliable classifier is the difference between regulating the interface and regulating
the structure underneath it.

The plan for this lab is to close that gap in public and give the result away. Three pieces follow
directly from the survey. First, a usable classifier: drop in a model of a coordination form, get
back a literacy-or-algorithmacy verdict, with the modeling commitments made explicit so the verdict
can be argued with. Second, a bridge to real data, testing whether the cheap proxies that work on
brain time series also track exact Φ on the small coordination structures underneath organizational
interaction logs. Third, the piece the survey says is missing most: a library of honest models, a set
of transition rules for canonical coordination forms, the dyad, the mediated triad, the broadcast,
the market, the hierarchy, so that anyone studying organizations has a defensible way to turn a
coordination form into something PyPhi can read.

The neuroscience community made exact PyPhi the ground truth and built a whole apparatus of
approximations around it. The contribution on offer here is the same pattern in a new domain: the
ground-truth verdicts, the proxy bridges, and the labeled examples that let other people work, but
for coordination instead of cognition. The dissertation this lab accompanies is making the careful,
case-by-case version of the argument under the constraints of a degree. This lab is the faster,
more exposed version, meant to be argued with, forked, and corrected.

The delivery driver from the opening cannot run PyPhi on her week. She does not need to. The point
of the instrument is not to score individual people. It is to tell the difference between a situation
that asks for an old competence and one that asks for a new one, so that the people who train
workers, design platforms, and write the rules can tell which world they are building. For a long
time that difference has been argued about with anecdotes and intuitions. It turns out there is a
number for it. The number was written to study consciousness. It reads an org chart just as well.

---

*This essay is the public writeup of the first study in this lab's `landscape` survey. The usage
findings, the full source list with DOIs, and the open questions are in the companion report; the
literacy-and-algorithmacy construct and its formal tests come from the accompanying dissertation. The
classifier, the proxy bridge, and the coordination-form model library are the next things to build.*
