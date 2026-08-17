# Formal standing: coordinative sovereignty as pivotality and core membership

The chapter defines coordinative sovereignty as an actor's standing within a coordination it cannot leave.
Standing is a word, and the lab already holds a formal object that can carry it. This note operationalizes
standing as a party's place in the cooperative game that integrated information defines on a coordination, and
ties that formal reading to the necessary/contingent diagnostic and to what the realizing institutions do. It
introduces no new computation. Every result it leans on is a committed thread of `phi_as_a_cooperative_game.md`.

## The construction the lab already has

Model a coordination as a small Boolean system whose nodes are the parties — a worker, a mediating system, a
counterpart. For a subset S of parties, the system integrated information φ_s(S) measures how irreducible that
subset's cause-effect structure is. Read φ_s as the worth of a coalition, v(S) = φ_s(S): a coalition is worth
how irreducibly it coordinates. The parties are players; the coordination is the game.

Two objects from that game name a party's place in it.

- **Shapley value.** A party's Shapley value over v is its average marginal contribution to the coordination's
  integration across all orders of coalition formation. It is the party's share of the credit for the whole's
  irreducibility, and the threads read it as pivotality: the party the coordination most depends on carries the
  largest share. A party outside the irreducible core carries a negative Shapley value, because it dilutes the
  coalitions it joins (`credit_concentration` thread).
- **Core membership.** The core is the set of ways to divide the whole's worth that no subcoalition can block. A
  party whose claim sits in the core holds a share that the others cannot rearrange the coordination to strip
  from it. On the structured mediated triads the dissertation models, the core is non-empty and the credit
  splits stably (`structured_forms` thread).

## Standing, formally

Coordinative sovereignty asks how much of a coordination a given actor holds and whether that hold can be taken
away. The two game objects answer exactly those two questions.

**Standing is a coordinated actor's pivotality, and its security is that actor's core membership.** An actor
has standing to the degree the coordination's integration depends on it — its Shapley share — and that standing
is secure to the degree its share sits in the core, unblockable by any rearrangement the other parties could
prefer. Low standing is a small Shapley share held outside the core; high standing is a large share the game
cannot evict.

The threads make the reading concrete and, for the coordinated actor, sobering. When a coordination runs
through a single mediator, that mediator is the pivotal party, the veto player, and the Shapley-argmax, in every
form the lab found (`veto_player`, 115 of 115). On the read-recipient triad the mediator's share is two-thirds;
on the structured mediated triads it is a little over half (`shapley_membership`, `structured_forms`). The
worker and the counterpart hold the remainder. So the default formal reading of a platform-mediated coordination
is that the mediator holds the standing and the coordinated actors hold little — which is the chapter's
co-optation stated as an allocation, not a metaphor.

## The bridge to exit and voice

The necessary/contingent test decides whether the mediator's large share is reachable.

- For a **contingent** mediator, opening the bypass collapses its share: its position rested on the absence of
  the direct tie, and restoring the tie returns the parties to a game they play without it, in which their own
  shares rise. Exit is the move, and it is a move on the game itself — it changes v by adding the forbidden
  edge.
- For a **necessary** mediator, opening the bypass takes nothing: its share rests on integrating work the direct
  tie cannot reproduce, and the actors' shares do not rise when the tie is restored. Exit cannot raise standing,
  and only voice remains.

Standing-as-Shapley thus gives exit and voice a common currency. Both are attempts to raise the coordinated
actor's share of the coordination it is in; exit raises it by removing a mediator whose hold was contingent,
voice by rebuilding the game so the actor's hold rises even though the mediator stays.

## What the institutions do, formally

The realizing institutions of the chapter's §7 are, in this reading, moves that rewrite the game so a
coordinated actor's Shapley share rises or its claim enters the core.

- **Platform cooperativism** makes the coordinated actors owners, which changes who the players are and folds
  the mediator's role into a coalition the actors control; the credit that concentrated on an external mediator
  is redistributed by construction.
- **Data trusts and collective bargaining** change v without changing the players: they make the coordinated
  actors, acting as a bloc, a party the mediator cannot integrate around, raising the bloc's marginal
  contribution and moving its claim toward the core.
- **Contestability** operates at the level of a single determination rather than the whole game, so it raises
  standing least; it gives the actor a claim on one outcome without changing its Shapley share over the
  coordination in general, which is why the chapter rates it a case-level voice.

The diagnostic sorts these the way it sorts exit and voice: interoperability and portability are exit moves,
effective against contingent shares; cooperatives, trusts, and bargaining are voice moves, the only ones that
raise standing against a necessary mediator.

## What this is and is not

This is a candidate formalization, offered for its suggestiveness, and it inherits every limit the cooperative-
game essay names. The forms are random Boolean truth tables, sampled for coverage; no mediator, platform, or
outside option is wired into the population, and a node earns the mediator's name after the fact. The credit-
concentration and pivotality readings hold on the structured mediated triads the dissertation models, and the
empty-core contestability reading is the random sample's, not the structured forms'. The bridge to organizations
is unbuilt: the parties are nodes in a Boolean model, and standing is explored on those models, not measured on
any firm. Integrated information is the object; the cooperative game is a language that makes standing legible
and ties it to how coordination is theorized elsewhere.

The value of the formal reading is that it gives the survey construct (`coordinative_sovereignty_instrument.md`)
a second, structural anchor. The instrument measures a coordinated actor's *perceived and reported* standing;
the game measures the standing a modeled coordination *affords*. A validated survey and a computed Shapley
share are two operationalizations of one construct, and the program can ask whether they agree — whether actors
who report high coordinative sovereignty are the ones a model of their coordination would place near the core.
That is the AGENDA's first item, stated as a testable correspondence rather than a definition.

## Next steps

- Specify the mediated-triad models whose Shapley shares stand in for the worked cases of the chapter (App Store
  developer, marketplace seller, platform worker), reusing the existing templates rather than deriving new Φ.
- State the correspondence hypothesis precisely: rank actors by reported coordinative sovereignty and by modeled
  Shapley share, and predict a positive rank correlation on cases where both can be assigned.
- Keep the computation in the existing cooperative-game threads; this program contributes the organizational
  interpretation and the tie to the survey instrument, not new Φ.
