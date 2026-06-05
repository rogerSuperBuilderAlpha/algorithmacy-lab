# 50 new research questions (v2 agenda)

Drawn from a review of all 134 probes (the original 53 plus programs v1–v6). Each question is new — none
is answered by an existing probe — and most name the result it grows from. Questions only; no method or
runnable design yet. Themes group them; numbering is 1–50.

## A. Beyond binary state

1. Do ternary parties (idle / engaged / overcommitted) change which party is pivotal, or does the
   two-condition account survive multivalued state? (parked #5; the whole corpus is binary)
2. Does a graded commit — the mediator outputs a level, not a bit — keep a sharp dyadic/triadic verdict,
   or does the verdict itself become graded?
3. In a mixed-radix system (binary parties, ternary mediator), where does the extra mediator resolution
   go — into Φ magnitude or into core membership?
4. Is the parity blind spot (#113) binary-specific, or do higher-radix "balanced" commits (sum mod k)
   produce the same low-Φ pure-higher-order forms?

## B. Stochastic determinations and noise

5. Does true correlated output noise — a state-by-state TPM the state-by-node form cannot express —
   change the verdict, where a static shared input did not (#61)?
6. Is there a Φ phase transition as a probabilistic commit's noise rises, or only the smooth decay the
   reliability sweeps showed (#27, #38)?
7. Does intrinsic noise in the parties (not the mediator) collapse the triad at a different threshold
   than mediator noise?
8. Under noise, does the parity hub (which decays as 2^(2−n), #115) lose its verdict faster than the
   conjunctive hub at the same size?

## C. Temporal and dynamical structure

9. Does separation of timescales — fast parties, slow mediator — factor the coordination the way
   sequential update did (#62)?
10. Does a fixed delay between the commit and the parties' response move the verdict, or only its
    magnitude?
11. Do oscillatory forms (limit-cycle attractors) carry a different Φ scaling law than the fixed-point
    families in the zoo (#132)?
12. Computed in continuous time rather than by discrete update, is the verdict grain-and-schedule
    invariant after all (#112 found no discrete invariant)?
13. Is there a coupling regime with genuine bistability — a triadic and a dyadic attractor coexisting —
    beyond the hysteresis a sticky mediator showed (#109)?
14. Does an adaptive mediator that learns toward higher Φ (not toward dropping a party, #79) converge to
    the conjunctive hub, the pool, or somewhere else?

## D. Larger and structured topologies

15. In a hierarchy of mediators (an org chart), which level holds the major complex, and does Φ scale by
    depth or by breadth?
16. When do two separately-triadic groups sharing one member merge into a single core versus stay two
    (extends the multi-role result #73 to two full triads)?
17. Does small-world coupling combine the ring's size-independent cap (#132) with a hub's growth, or
    pick one?
18. Across random coupling topologies at fixed n, what is the distribution of Φ and the triadic rate,
    and does it match any standard network ensemble?
19. Is there a topology between the ring (Φ capped at 4) and the pool (Φ = n(n−1)) whose law is
    logarithmic or square-root in n?
20. Does a "spanning" mediator added atop the symmetric multi-hub raise Φ beyond the pool, or is the
    pool the ceiling (#119)?

## E. The estimation frontier

21. Is there any topology-invariant feature — spectral, not coupling-based — that ranks the verdict
    across families, given that pairwise coupling inverts across topology (#134)?
22. Does a structure-aware surrogate (a graph neural net on the connectivity-plus-function input)
    generalize across topology where coupling features fail (#129, #134)?
23. What trajectory length is needed to estimate the verdict at a fixed confidence — the sample
    complexity of the cheap screen (#122)?
24. How fast does estimability degrade under partial observation — a hidden node, or a party observed
    only intermittently?
25. Which forms are most informative to label first when training a surrogate (active learning over the
    corpus)?

## F. The holistic residual

26. Does the irreducible-residual fraction (~5% at n=3, #131) shrink, hold, or grow at n=4 and n=5?
27. Are the residual forms exactly the affine (GF(2)-linear) determinations, or some other algebraic
    class connectivity cannot see (#130, #106)?
28. Do the near-boundary holistic forms (#131) sit on a genuine phase boundary in function space — small
    perturbations flipping the verdict?

## G. Political economy and organization design

29. With two principals issuing conflicting commits, whose core wins, and is there a stable shared core
    (extends the single-principal study and #37)?
30. If parties choose whether to join a coalition, do they endogenously form the coalition that maximizes
    their own core membership (#66 imposed it)?
31. Does a worker union scale the same way a counterpart coalition does, and does it vanish past some
    size the way single-mediator triadicity did (#97)?
32. A worker on two competing platforms — do the two cores compete for the worker, and does one win
    (extends #73 to rivalrous platforms)?
33. A regulator that gates the platform but is itself gated by it: at what coupling does oversight become
    capture (#76, #111)?
34. Does opening the commit function to the parties (algorithmic transparency of the rule, not the
    channel #24) change the structural verdict?
35. In a gig market with many substitutable workers, at what substitution rate does the individual worker
    drop from the core (#8, #22)?
36. Does an extractive commit's ejection order (#110) predict which real platform stakeholders lose
    standing first?

## H. AI and multi-agent systems

37. Two LLM-style agents negotiating through a protocol node: does the protocol's design set dyadic vs
    triadic the way the commit did (#50, #88), and can a "negotiation" protocol be triadic without a
    human?
38. Does a tool an agent calls join the core when the agent acts on its output, like the inference model
    (#4, #9)?
39. Human-in-the-loop AI: with human, AI, and counterpart, under what coupling is the human in the core
    versus a rubber stamp?
40. Does an AI that online-learns the counterpart's policy displace the counterpart over training, and
    does the displacement track model fidelity (#69)?
41. In multi-agent RL, does the emergent coordination structure's verdict predict whether the agents can
    learn the task (a behavioral test the static ABM nulls #98, #107 leave open)?

## I. Construct validity and organization-theory bridges

42. Do the HMC / CMC / AI-MC discriminants (#15, #19, #20) hold at n > 3, or does scale blur them?
43. Does the verdict correspond to Thompson's interdependence types — pooled dyadic, sequential the
    chain, reciprocal triadic?
44. Does measured task interdependence (Wageman-style) predict the verdict on a modeled task?
45. Is the conjunctive Φ = n−1 law (#116) visible in any real coordination dataset rendered as a Boolean
    form?
46. Does the verdict align with the formal-vs-informal coordination distinction, or cut across it?

## J. Formal and theoretical

47. Prove the scaling laws closed-form: conjunctive Φ = n−1, pool Φ = n(n−1), parity Φ = 2^(2−n) (#116,
    #132, #115) — derive them from the MIP rather than reading them off.
48. Is the conjunctive hub the unique form achieving its Φ at the 2(n−1) edge floor, or are there others
    (#30, #116)?
49. Is there a min-cut theorem placing the MIP at the least-coupled node for a class of forms, extending
    the worker-as-weakest-seam result (#26, #33)?
50. Does the verdict, with Φ magnitude, induce a partial order on coordination forms — a lattice of
    coordination kinds — and what are its extremes?
