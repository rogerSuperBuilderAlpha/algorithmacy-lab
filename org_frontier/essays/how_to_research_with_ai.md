# A protocol for AI-assisted research

Most AI research assistants are used as fast writers. Someone asks for a literature review, a draft, an
analysis, and the model returns fluent text in seconds. The text reads well and is often wrong in ways
that read well too. The fluency is the problem. A model that produces a confident paragraph produces an
equally confident paragraph when the reasoning behind it is broken, and a reader cannot tell the two apart
from the prose. Speed without a method amplifies error instead of catching it.

There is a better way to use these tools, and it is old. It is the ordinary discipline of empirical
science, made routine by automation. Fix your hypotheses before you compute. Hold several at once so you
cannot fall in love with one. Specify exactly how each will be tested before running anything. Run the
test against something that can prove you wrong. Report the failures. What an AI assistant adds is that it
can run this loop end to end, fast, on question after question, provided the loop is built to stop it from
cutting corners. This essay describes such a loop, the evidence behind each step, and a worked example
from a research program that has now run it 134 times.

## The pipeline

One question goes through six stages, in order, and each stage produces an artifact the next stage reads.

1. **Review.** State the question precisely. Find what is already known, in your own prior work and in the
   record, so the new work extends rather than repeats. If the question is already answered, stop.
2. **Deep research.** Run a real literature search: fan out across angles, fetch primary sources, verify
   each claim against the document it came from, and write a report with citations and an explicit
   statement of the open gap. A scan of the three papers you already know does not count.
3. **Hypotheses.** Turn the question into several falsifiable predictions, each paired with the null it
   would have to beat, and the outcome each predicts named in advance. Write them down before computing
   anything.
4. **Methods.** For each hypothesis, specify the exact test: the system, the measure, the controls, and
   the rule that will decide the hypothesis. A reader should be able to reproduce the design from this
   alone.
5. **Run.** Execute the tests against a ground-truth instrument. Validate the instrument on a known control
   first. Record exact numbers. A test that goes against its hypothesis is logged as a refutation.
6. **Paper.** Write the finding as a complete quantitative paper, with abstract, introduction, related
   work, hypotheses, methods, results, discussion, limitations, and references, every number traceable to
   a result and every citation to a real source.

The order is the point. Stages 1 through 4 commit you to a position before any data exists. Stages 5 and 6
hold you to it.

## Why each step, and where the evidence backs it

The pipeline is an assembly of methods that predate AI by decades. Each stage answers to a known result.

**Holding several hypotheses is a defense against your own bias.** In 1890 the geologist T. C. Chamberlin
described what happens with a single explanation: the mind performs "an unconscious selection and
magnifying of the phenomena that fall into harmony with the theory and support it, and an unconscious
neglect of those that fail of coincidence" [Chamberlin 1890]. His remedy was to become "the parent of a
family of hypotheses" and stay "forbidden to fasten his affections unduly upon any one." Platt's 1964
"strong inference" sharpened the idea into a method: design each test to exclude hypotheses, and carry
enough of them that any outcome eliminates some [Platt 1964]. A pipeline that fixes a set of competing
hypotheses builds this defense in.

The count matters less than the discipline. A fixed quota of five is a useful habit against
single-hypothesis attachment, and it is informative only when the hypotheses can actually be told apart by
the instrument. A modern reconstruction of Chamberlin's method makes the condition explicit: candidate
hypotheses must be checked for identifiability before data collection, because distinct processes can
produce indistinguishable patterns [Yanco 2020]. Five predictions the instrument cannot separate are not
five tests.

**Fixing the claims before computing keeps a result honest.** When analytic choices are made after seeing
the data, the "garden of forking paths" opens: with enough defensible choices, a researcher can reach
almost any conclusion and never notice the search [Gelman & Loken 2013; Nosek 2018]. Pre-registration
closes the path by committing to the analysis before the outcomes are known. The evidence on whether it
works carries a sharp lesson. A study of 15,992 test statistics across leading economics journals found no
meaningful difference between pre-registered and non-pre-registered work, except where the registration
included a complete pre-analysis plan, where the studies were measurably less p-hacked [Brodeur 2024]. The
operative commitment is the detailed specification of how each hypothesis will be tested, more than the
bare act of declaring it. In the pipeline above, that puts the credibility in Stage 4. Listing hypotheses
buys little; naming the decision rule for each, in advance, buys the result.

A second caution travels with this. Pre-registration's benefits are argued design intents, partly
contested, not settled fact; the strong claim that the practice has been shown to both reduce bias and
improve study quality does not hold up [Lakens 2024]. The honest version is narrower: a pre-analysis plan
reduces undisclosed flexibility, and that is worth having.

**A ground-truth instrument removes the argument about measurement.** Much of social science argues over
whether a measure captures what it claims to. When an exact computation is available on a small system,
there is nothing to argue: the number is the thing. The catch is what the number is about. The simulation
literature is blunt here. Comparing a model against a second model, a practice called "docking,"
establishes that they agree, at one of three levels: identical outputs, statistically indistinguishable
outputs, or the same qualitative orderings [Axtell 1996]. Agreement between models is internal validity.
External validity is a separate claim. Two models of an organization can match each other exactly and both
be wrong about real organizations. A passed computational test is evidence about the model, and at most
about a second model that reproduces it, not yet about the world the model stands for. The gap does not
close by computing harder. It closes only with an empirical anchor, and until there is one, the result
stays a result about the model.

**Reporting the failures makes the record trustworthy.** A literature that publishes only positive results
is a biased sample of the work done [Scheel 2021]. The same bias operates inside a single research program:
a loop that quietly drops its refutations reads as a string of successes and means nothing. The fix is to
log refutations and partial results as first-class findings. In the program described below, about a third
of the results are nulls or refinements, and that fraction is what makes the confirmations credible.

## The part AI changes, and the part it does not

Automation changes the cost of the loop. A capable model can do the reading, propose the hypotheses, write
the test code, run it, and draft the paper, which collapses weeks of work into hours and makes it feasible
to run the loop across dozens of questions. That is the genuine gain.

It also introduces the loop's main hazard, the fluency the opening warned about. An AI assistant writes
authoritative prose whether or not the reasoning holds, so the usual signal a reader uses to detect a weak
argument, that it reads as strained, is gone. Three failure modes follow, and each maps to a stage that
guards against it. Fabricated or subtly wrong citations are caught only when Stage 2 verifies every source
against the primary document, instead of against a generated summary. Plausible-but-wrong reasoning shaped
to fit a conclusion is the postdiction-dressed-as-prediction problem, and the defense is the Stage 3 and
Stage 4 pre-commitment, which fixes the analysis before the narrative exists. Confirmation bias is
Chamberlin's failure mode, and the multiple-hypothesis structure plus the honest reporting of Stage 6 are
the classical counters.

One limit is worth stating flatly. Verifying that an automated executor actually honors the
pre-commitment, instead of reconstructing a tidy story after seeing the results, is an open problem. The
guard is mechanical: the hypotheses are committed to version control with a timestamp before the test code
is written, so the order is auditable. That is weaker than a public registry and stronger than trusting the
model's account of its own process.

## A worked example

The first question run through the automated pipeline asked whether a 1967 classic of organization theory
survives a computational test. James Thompson sorted organizational interdependence into three types of
rising coordination demand: pooled, where units share a common resource with no direct contact; sequential,
where one unit's output is the next's input; and reciprocal, where each unit's output feeds back as
another's input. The textbook ordering is pooled below sequential below reciprocal. The question: does an
exact measure of structural irreducibility reproduce that ordering when each type is built as a small
dynamical system?

Stage 1 placed the question against the program's own record and found the ordering already in trouble. A
chain, the natural model of sequential interdependence, had measured as maximally irreducible in earlier
work, a top-of-scale reading for a middle type. The gap was that the three types had never been built as a
matched set, holding everything fixed but the topology, and read head to head.

Stage 2 ran a literature search that confirmed Thompson's typology as the standard and found no prior
computational test of it against integrated information. Stage 3 then fixed five hypotheses before any
computation. The first predicted the naive ordering would break. The next three predicted that "pooled" and
"sequential" are each ambiguous, buildable to either verdict depending on a single edge, and that
"reciprocal" reads as irreducible only when its coupling closes a real feedback loop. The fifth proposed a
replacement: drop the labels and read the verdict off two structural primitives, joint determination and a
feedback cycle.

Stage 4 specified each test as a matched comparison at fixed size and rule family, with a known control
that had to reproduce its established value first. Stage 5 ran them. The control passed every time. Four of
the five hypotheses confirmed. The ordering broke exactly where predicted: pooled came out reducible while
sequential and reciprocal tied at the top, so the typology's final step vanished. Pooled and sequential
each took both verdicts, flipped by one edge, whether a downstream node is jointly determined by all
contributors, whether a chain has a return path. Reciprocal read as irreducible only when its loop genuinely
closed; arrows drawn in both directions without a closed loop read as reducible.

The fifth hypothesis was refuted, and that is the part worth keeping. The proposed two-primitive replacement
failed: four forms carried both primitives, three of them with identical wiring diagrams, and still split
across the two verdicts. A directed cycle in the wiring diagram turned out to be a different object from a
closed loop in the causal structure the measure integrates over. The clean replacement for Thompson's labels
does not exist at that level of description. A pipeline tuned to produce a tidy story would have buried this
and reported a four-for-five success. The protocol logged it as a refutation, and the refutation is the most
informative result of the five: it says the verdict lives in the cause-effect structure, finer than any
label and finer than the obvious structural summary.

The whole run completed without human intervention: review, literature search, five hypotheses, methods,
five executed tests against the exact instrument, a complete paper, and a de-slop pass. Every number in the
paper reproduces from a committed script. The headline is a negative result about a classic typology,
reported as such.

## What this is good for, and what it is not

The protocol fits questions that can be settled by computation against a ground-truth instrument. It does
not turn a model result into a claim about the world; that step needs data the computation cannot supply,
and the protocol's job is to keep the two apart. Within that boundary, it converts an AI assistant from a
fast writer into a slow, auditable researcher, one that commits before it computes, tests against something
that can prove it wrong, and reports what it finds, including the third of the time it is wrong.

The discipline is old. The automation is new. The combination is what makes it worth doing at scale.

## References

Chamberlin TC (1890). The method of multiple working hypotheses. Reprinted in *Science* 148(3671):754–759
(1965). doi:10.1126/science.148.3671.754.

Platt JR (1964). Strong inference. *Science* 146(3642):347–353. doi:10.1126/science.146.3642.347.

Yanco SW, McDevitt A, Trueman CN, Hartley L, Wunder MB (2020). A modern method of multiple working
hypotheses to improve inference in ecology. *Royal Society Open Science* 7(6):200231.
doi:10.1098/rsos.200231.

Gelman A, Loken E (2013). The garden of forking paths. Working paper, Columbia University.

Nosek BA, Ebersole CR, DeHaven AC, Mellor DT (2018). The preregistration revolution. *PNAS*
115(11):2600–2606. doi:10.1073/pnas.1708274114.

Brodeur A, Cook N, Hartley J, Heyes A (2024). Do pre-registration and pre-analysis plans reduce p-hacking
and publication bias? *Journal of Political Economy: Microeconomics* 2(3). doi:10.1086/730455.

Lakens D, Mesquida C, Rasti S, Ditroilo M (2024). The benefits of preregistration and Registered Reports.
*Evidence-Based Toxicology* 2(1). doi:10.1080/2833373X.2024.2376046.

Axtell R, Axelrod R, Epstein JM, Cohen MD (1996). Aligning simulation models: A case study and results.
*Computational and Mathematical Organization Theory* 1(2):123–141. doi:10.1007/BF01299065.

Scheel AM, Schijen MRMJ, Lakens D (2021). An excess of positive results. *Advances in Methods and
Practices in Psychological Science* 4(2). doi:10.1177/25152459211007467.
