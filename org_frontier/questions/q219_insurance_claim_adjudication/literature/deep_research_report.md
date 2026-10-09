# Q219 — Stage 2 deep research: automated claims handling and the human in the loop

**Status: partial.** This first pass collects 13 sources, each with a DOI checked against Crossref on
2026-10-09. The protocol targets 15–30, so the scan is to be extended before the paper stage, especially on
claims-handling practice and on regulation of automated individual decisions. The gap stated below does
not depend on the missing sources: no source in this scan, or known to this review, computes whether a
claims arrangement is structurally irreducible.

## Automation in insurance claims

Eling, Nuessle, and Staubli (2022) map artificial intelligence along the insurance value chain and place
claims management among the steps most exposed to automation, through straight-through processing of
simple claims and machine fraud detection [eling2022impact]. Their account supplies the three designs this
study models: a pass-through pipe, threshold auto-approval with human review of flagged claims, and a
fraud-flag loop. It describes these designs by cost and risk and says nothing about the structure of the
coordination they create.

## Levels of automation and human oversight

Parasuraman, Sheridan, and Wickens (2000) grade automation by how far it reaches into acquisition,
analysis, decision, and action [parasuraman2000types]. A claims engine that auto-approves small claims
automates the decision stage for those claims and only the analysis stage for flagged ones, which is
the split variant b encodes. Parasuraman and Riley (1997) name the failure modes of that division: use,
misuse, disuse, and abuse of automation [parasuraman1997humans]. Bainbridge (1983) shows the irony that
automating the routine cases leaves the human with the hardest cases and the least practice
[bainbridge1983ironies].

## The human as rubber stamp

Skitka, Mosier, and Burdick (1999) found that people supported by an automated aid commit omission and
commission errors that unaided people avoid, so an adjuster shown an engine's flag may follow it
[skitka1999automation]. Green (2022) reviews policies that require human oversight of government
algorithms and finds that people cannot perform the oversight such policies assign them, which gives a
mandated reviewer a legitimating role more than a corrective one [green2022flaws]. Wagner (2019) asks
whether a human placed in an automated decision is in control or only liable [wagner2019liable]. Elish
(2019) names the result a moral crumple zone: the human absorbs responsibility for a system it does not
steer [elish2019moral]. Dietvorst, Simmons, and Massey (2015) add the opposite drift, in which people
abandon an algorithm after seeing it err [dietvorst2015algorithm]. Together these accounts predict that
the adjuster's formal authority and structural place can come apart, which is the distinction the lab's
#39 study drew with exact Φ.

## Algorithmic control and coordination

Kellogg, Valentine, and Christin (2020) treat algorithms at work as a contested terrain of control in
which direction, evaluation, and discipline move into the system [kellogg2020algorithms]. Malone and
Crowston (1994) define coordination as managing dependencies among activities and place the mechanism
inside the coordination structure [malone1994interdisciplinary]. Neither computes whether a given
arrangement is irreducible.

## Instrument

Exact integrated information follows IIT 4.0 [albantakis2023iit4] as implemented in PyPhi
[mayner2018pyphi]. A form is dyadic when Φ over the minimum-information partition is zero and triadic
when it is positive.

## The gap

The literature describes who holds authority over a claim and how human reviewers behave beside an
automated aid. It does not ask whether the claimant, engine, and adjuster form one irreducible
determination or factor into a pair and a bystander, and it has no instrument that would answer that
question for a specific routing design. The gap is open.
