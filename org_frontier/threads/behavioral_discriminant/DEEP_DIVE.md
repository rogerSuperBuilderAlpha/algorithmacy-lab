# Can behavior tell a committing mediator from a conveying one — twenty steps deep

Q10 from the [mediation-boundary thread](../mediation_boundary/QUESTIONS.md), taken twenty steps deep. The
first two dives used exact Φ, the structural instrument. This one asks whether the behavioral instrument,
cross-recurrence on a run of the form, can recover the commit-or-convey distinction without the model. The
answer is a moderate screen and a sharp limit, and the limit is the finding: a large class of conveying
mediators is behaviorally identical to committing ones. Each step's question is drawn from the previous
step's result; every number reproduces from [`chain.py`](chain.py).

## The chain

**1 — A clean signature, on clean cases.** Question: do committing and conveying mediators leave different
cross-recurrence traces? On clear cases they do. A committing mediator (S = W ∧ C) makes the worker and
counterpart recur synchronously, W-C lag 0, prominence 0.25, with a central mediator. A conveying relay
makes them recur at a directed lag, lag 2, prominence 0.16, with a less central mediator. → Does the
synchrony signature hold across a population?

**2 — Synchrony fails to generalize.** Question: across random strict-mediated forms, does W-C synchrony
predict a committing verdict? Barely, AUC 0.54. The clean-case signal washes out. What survives is the
directed-coupling prominence, AUC about 0.70, and the mediator's coupling centrality, about 0.70. The clean
signature was misleading; the population is messier. → Can the two surviving measures combine to beat 0.70?

**3 — Combining adds nothing.** Question: do prominence and centrality carry independent signal? They do
not; their sum scores the same 0.71. They measure the same coupling, and the ceiling holds near 0.70. → Is
the ceiling a limit of the data or of the instrument?

**4 — The ceiling is structural.** Question: do longer and cleaner trajectories lift it? They do not.
Fifteen hundred steps at a lower noise rate hold the prominence AUC at about 0.72 to 0.75. The ceiling is
not a sampling limit; it is built into what behavior can show. → Which committing forms does it catch, and
which does it miss?

**5 — Detectability tracks the margin.** Question: are some committing forms easier to detect than others?
Yes, and along the dive-2 margin. Among committing forms, W-C prominence correlates with Φ at +0.42, so
strong-commitment forms read clearly and forms near the dyad boundary blur. The behavioral signal is
sharpest exactly where the structural margin is widest. → Does the directed-lag carry the conveying signal
the synchrony missed?

**6 — The lag fails too.** Question: across the population, does a directed W-C lag mark a
conveying mediator? No, AUC 0.54. Neither synchrony nor lag separates the classes in a random population.
The lead-lag that read cleanly on the relay vanishes in the population. → What is the error profile of the
best detector?

**7 — Sensitive, not specific.** Question: what does the prominence detector get wrong? At a screening
threshold it catches almost every committing form, recall 0.97, but flags many conveying forms too. It is a
sensitive screen with poor specificity. → Does the mediator's behavioral centrality recover anything exactly?

**8 — Mediator centrality recovers core membership exactly.** Question: does S's coupling centrality track
its place in the structure? It does, perfectly. The behavioral centrality of the mediator separates the
forms where S sits in the major complex from those where it is absent at AUC 1.00. Behavior recovers the
mediator's structural membership cleanly, even where it cannot recover the whole verdict. → Why does the
whole verdict stay at 0.70?

**9 — Raw determinism misleads.** Question: does stronger coupling mark a committing form? The opposite. The
plain determinism of the W-C pair scores AUC 0.31, below chance: stronger coupling predicts a dyadic
verdict, the dynamic face of the corpus result that Φ and determinism anti-correlate. Only the directed,
prominence-corrected coupling carries any signal. → Does any whole-system measure help?

**10 — The whole-system reading is chance.** Question: does multidimensional recurrence of the full state
separate the classes? No, AUC 0.56. The signal lives only in the mediated pair and nowhere
else. → What do the false positives have in common?

**11 — The false positives are indistinguishable.** Question: how do the conveying forms that fool the
detector differ from real committing forms? They do not. The conveying false positives have mean W-C
determinism 0.73 and prominence 0.27; the true committing forms have 0.74 and 0.26. On every behavioral
measure the two classes are the same. → Can a threshold separate them anyway?

**12 — No threshold separates them.** Question: can specificity be bought by raising the prominence bar?
No. At threshold 0.15 precision is 0.54; raising it to 0.30 leaves precision at 0.48 while recall falls to
0.30. The classes overlap completely in behavior, so no operating point recovers them. → How does this
compare to the cheap proxies the lab already tested?

**13 — A modest gain over the cheap proxy.** Question: does cross-recurrence beat the proxy bridge? By a
little. The proxy-bridge attempt reached AUC at most 0.63 separating dyadic from triadic; the directed
cross-recurrence prominence reaches about 0.70. Better, and still far from a verdict. → Why is the ceiling
where it is?

**14 — Behavior cannot see the factorization.** Question: what is the 0.70 ceiling made of? It is the
structure-behavior dissociation. Two forms can run with the same coupling, the same recurrence, the same
prominence, and differ only in whether the cause-effect structure factors across the partition. That
difference is what Φ computes and what behavior leaves hidden. The ceiling is no noise floor; it is the
genuine ambiguity of behavior about structure. → What does the clean-case signature mean, then?

**15 — Ideal cases mislead.** Question: why did step 1 look so clean? Because the clean cases are
well-separated points the population fills the space between. A hand-picked committing form and a
hand-picked relay differ behaviorally; a random committing form and a random conveying form often do not.
The signature is real at the extremes and absent in the middle. → What does behavior recover, if not the
verdict?

**16 — Behavior recovers membership and direction, not the verdict.** Question: where is cross-recurrence
reliable? On the mediator's core membership, perfectly, and on the direction of a clear relay. It reads who
is coupled to whom and which way a signal flows, and it does this without a model. It leaves unread whether
the coupling integrates into an irreducible whole. → What does this say about the instrument choice?

**17 — The case for exact Φ.** Question: does this vindicate the structural instrument? It does. The
commit-or-convey verdict is not recoverable from behavior because behavior under-determines it; a cheap
behavioral proxy cannot replace exact Φ for this question, which is the lab's standing position made
concrete on a third instrument. → Does this explain the real-data dives?

**18 — Why the real-data work needed the model.** Question: does the ceiling explain v8 and v9? It does.
v8's weekly-activity cross-recurrence could not read the coordination's structure, and v9 succeeded only by
eliciting the merge rule and computing Φ on it. Behavior alone, however well encoded, would have hit the
same ceiling; the elicited model is what carried the verdict. → What, then, is cross-recurrence for?

**19 — The bridge, not the verdict.** Question: what does cross-recurrence add that Φ does not? It runs on
recorded data with no model, recovers the mediator's membership and the direction of flow, and screens for
likely commitment. It is the bridge to real series and a sensitive first pass, valuable for what it reads
directly, never a stand-in for the structural verdict. → What is the whole picture?

**20 — The behavioral discriminant.** Cross-recurrence is a sensitive, low-specificity screen for committing
mediation, scoring about 0.70 with directed-coupling prominence and mediator centrality, sharpest where the
dive-2 margin is widest and blind near the boundary. It recovers the mediator's core membership exactly and
reads the direction of a relay, but it cannot confirm the commit-or-convey verdict, because a large class of
conveying mediators runs with behavior identical to a committing one. The structure-behavior dissociation is
the ceiling, and exact Φ is what clears it.

## What the dive establishes

Behavior is a moderate, honest screen for committing mediation and a poor judge of it. The directed-coupling
prominence and the mediator's centrality reach about 0.70 on the commit-or-convey verdict, a little above
the cheap proxies and far below a decision, while raw coupling strength misleads and whole-system recurrence
is chance. The screen is sensitive, catching nearly all committing forms, and unspecific, flagging as many
conveying ones, because the two classes can be behaviorally identical. What behavior does recover cleanly is
the mediator's structural membership, at AUC 1.00, and the direction of a clear relay, both without a model.
The verdict itself stays with exact Φ, which is the point: the cause-effect structure that decides commit
from convey is the part behavior cannot show.

## Connections

The dive answers Q10 and ties the three together. The behavioral detectability tracks the dive-2 margin
(strong commitment reads clearly, near-boundary commitment blurs), and the co-monotonicity law of dive 1
sets which forms are committing in the first place. The ceiling is the structure-behavior dissociation the
[recurrence sweep](../../recurrence/SWEEP.md) and [experiments](../../recurrence/IIT_EXPERIMENTS.md) found,
and the result explains why [v8](../../recurrence/real_series/) was null and
[v9](../../recurrence/event_series/) needed an elicited model. It supports the lab's reliance on exact Φ and
the [proxy-bridge](../../proxy_bridge/) finding that cheap signals cannot recover the verdict.
