# q163 — Computationalism under an agenda: the interested mediator as a third object

The computationalism battery separates two objects inside one triad. A channel relays the worker:
its system node S computes some function of W alone, and the whole-system Φ is 0. An actor commits the
joint determination of the two parties: S = W ∧ C, and Φ is 2.0. Refining a channel never makes an
actor, and reading both parties without committing is not the same as committing. The mediator in both
cases is faithful: it serves the parties.

Q126 introduced an interested mediator. It holds an agenda, a preferred output, and imposes it on the
k input states where the parties least warrant it, committing the faithful gate elsewhere. As k rises
the mediator stops serving the parties and starts serving itself. The question this study asks is
whether such a mediator is a third kind of object, an actor that reads its agenda but not the parties,
that the channel/actor pair cannot hold.

## Design

The actor form is the Q126 triad: W' = S, C' = S, S' = mediator(agenda, k). The channel form is the
matched relay: S forwards W and imposes the same agenda on the W-values least warranting it, never
reading C. Both are built in the shared module the interested-mediator line reuses. For each agenda
(approve a=1, deny a=0) and each k = 0..4 the study measures the actor Φ, the channel Φ, the actor
surplus Φ(actor) − Φ(channel), the parties S's rule reads on a connectivity flip-test, and the actor's
major complex. Two ladders are read: the ordered Q126 ladder, and the order-averaged ladder over all
C(4,k) choices of which states the agenda overrides. The control is k=0, the faithful actor from the
battery, which reads triadic with Φ = 2.0 against a channel at Φ = 0.

## Result

The channel sits at Φ = 0 for every k, so the actor surplus equals the actor Φ. Under the deny agenda
the surplus falls monotonically: 2.00, 1.50, 1.00, 0.50, 0.00 on the order-averaged ladder. Under the
approve agenda it is non-monotone: 2.00, 0.625, 0.417, 0.500, 0.00. The surplus dips at k=2 and rises
at k=3 before collapsing at k=4. A channel that merely degraded under interest would fall monotonically
to 0. The bump means the approve mediator is not a degrading channel. It is an actor whose
irreducibility recovers as more states bend to the agenda, then vanishes only when the agenda fully
displaces the parties. That places the interested actor outside the channel/actor dichotomy. H1 holds.

The second claim fails. H2 predicted that an interested mediator sheds a party before its whole-system
Φ reaches 0, so that reading-its-agenda substitutes for reading-the-parties. On the ordered ladder the
connectivity flip-test shows S still depending on both W and C through k=2 for the approve agenda, where
Φ has already fallen to 0 at k=2. The structural dependence on the parties outlives the irreducible
bind. Agenda-reading and party-reading do not dissociate on this test; the null holds. H2 is refuted.

## Reading

Interest does two things that come apart. It reshapes irreducibility in a way a channel cannot imitate,
which the non-monotone approve surplus records. It does not, on the coarse connectivity test, let the
mediator drop the parties from its rule while the bind still stands. The interested actor is a distinct
object by its Φ signature, and its rule still reads the parties it has stopped serving. The two facts
sit together: a mediator can compute on both parties and yield a form with no irreducible whole.

## Scope and validation gap

Exact Φ on a 3-node Boolean model. No worker is measured. "Agenda", "approve", "deny", and "interest"
name output values and rule structure, not intent. The empirical reading is on synthetic forms, and the
result is evidence about the instrument and the construct. The flip-test for party-reading is a binary
connectivity check; a graded read-dependence measure could move the H2 verdict, and that is the next
study in the line. Whether any real mediated coordination shows the approve bump is open.
