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
    **Answered — CORE_SHIFT_NO_FLIP.** Shared-coin (W′,C′) SBS is
    non-CI (residual≤0.25) but exact Φ only sees the CI projection
    (= indep dual-party flip): smooth decay, p*=0.5; one-point
    n_core dip at p=0.40; no interior verdict flip vs #61.
    See `studies/correlated_output_noise/`.
6. Is there a Φ phase transition as a probabilistic commit's noise rises, or only the smooth decay the
   reliability sweeps showed (#27, #38)?
    **Answered — SMOOTH_DECAY.** Conjunctive and parity n=3 hubs: Φ
    monotone glide; verdict flips only at p=0.5; no interior core/Φ
    decoupling. See `studies/commit_noise_phase/`.
7. Does intrinsic noise in the parties (not the mediator) collapse the triad at a different threshold
   than mediator noise?
    **Answered — SAME_THRESHOLD_DIFF_CURVE.** p*=0.5 both seats on
    conjunctive and parity hubs; Φ gaps 46%/64% of Φ(0); conjunctive
    party noise drops n_core 3→2 interiorly. See
    `studies/party_vs_mediator_noise/`.
8. Under noise, does the parity hub (which decays as 2^(2−n), #115) lose its verdict faster than the
   conjunctive hub at the same size?
    **Answered — SAME_P_STAR.** p*=0.5 both families at n=3,4;
    conjunctive sheds more Φ̂ (49/49 interior). See
    `studies/parity_vs_conjunctive_noise/`.

## C. Temporal and dynamical structure

9. Does separation of timescales — fast parties, slow mediator — factor the coordination the way
   sequential update did (#62)?
    **Answered — FACTORS_LIKE_62.** hold-for-k flips dyadic at k*=2
    (core→{S}); #62 sequential 6/6 dyadic; prob 1/k stays triadic.
    See `studies/timescale_separation/`.
10. Does a fixed delay between the commit and the parties' response move the verdict, or only its
    magnitude?
    **Answered — DELAY_CORE_SHIFT.** Buffer stays triadic; core and Φ
    move (2→1→2→2); lagged read flips at d=2. See
    `studies/commit_response_delay/`.
11. Do oscillatory forms (limit-cycle attractors) carry a different Φ scaling law than the fixed-point
    families in the zoo (#132)?
    **Answered — DIFFERENT_LAW.** rot_ring Φ=2 constant (period=n) vs
    and_ring cap / hub / parity landmarks. See
    `studies/oscillatory_scaling/`.
12. Computed in continuous time rather than by discrete update, is the verdict grain-and-schedule
    invariant after all (#112 found no discrete invariant)?
    **Answered — STILL_DEPENDENT.** CTMC→expm embedding softens #112
    (200/216 cells triadic vs discrete grain-2/seq 0/24) but extreme
    rate asymmetry still flips 8/24 forms; native CT Φ unavailable on
    PyPhi. See `studies/continuous_time_invariance/`.
13. Is there a coupling regime with genuine bistability — a triadic and a dyadic attractor coexisting —
    beyond the hysteresis a sticky mediator showed (#109)?
    **Answered — GENUINE_COEXISTENCE.** 6/9 n=3 couplings host
    triadic+dyadic attractors at fixed TPM; #109 sticky is MULTI_SAME
    (both dyadic) plus activity hysteresis (gap 0.066), not
    cross-verdict bistability. See `studies/genuine_bistability/`.
14. Does an adaptive mediator that learns toward higher Φ (not toward dropping a party, #79) converge to
    the conjunctive hub, the pool, or somewhere else?
    **Answered — PLATEAU_ELSE_POOL.** Fixed-party S′ ascent hits a
    46-form Φ=2 plateau (hub not selected); topology catalog ascent
    reaches pool (unique at n=4; pool/ring tie at n=3). Opposite of
    #79. See `studies/phi_ascent_mediator/`.

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
    **Answered — SPECTRAL_PARTIAL.** Transfer-operator spectral gap AUC=0.893
    vs inverted mean-MI 0.775 (lift +0.118 < 0.15 H1 bar).
    See `studies/spectral_invariant/`.
22. Does a structure-aware surrogate (a graph neural net on the connectivity-plus-function input)
    generalize across topology where coupling features fail (#129, #134)?
    **Answered — no material gain on a designed LOFO panel.** Structure-aware RF
    (cm+function) LOFO AUC 0.993 vs coupling 0.944 (lift +0.049 < 0.15).
    See `studies/structure_aware_surrogate/` NO_STRUCTURE_GAIN.
23. What trajectory length is needed to estimate the verdict at a fixed confidence — the sample
    complexity of the cheap screen (#122)?
    **Answered — FAST_WITHIN_FAMILY.** Strict-mediation n=3: mean-MI AUC≥0.97
    already at T=125; noise 0.16 same. Cross-topo MI stays ~0.2 at all T.
    See `studies/sample_complexity_screen/`.
24. How fast does estimability degrade under partial observation — a hidden node, or a party observed
    only intermittently?
25. Which forms are most informative to label first when training a surrogate (active learning over the
    corpus)?
    **Answered — AL_NO_GAIN.** Uncertainty Δ=+0.015 vs random on pooled
    (H1/H2 refuted; H3 supported). Topo-balance hurts under LOFO.
    See `studies/active_label_acquisition/`; lane note
    `ESTIMATION_ARC.md` (closable).

## F. The holistic residual

26. Does the irreducible-residual fraction (~5% at n=3, #131) shrink, hold, or grow at n=4 and n=5?
    **Answered through n=5 under unconstrained k=2.** n=3: 4.8%. n=4 unc: 7.5% (H2 grows; SM 2.4%
    was a base-rate artifact). **n=5 unc: 9.0% (45/500, H0 holds near n=4)** with both classes
    predicted. See `holistic_residual_n4_unconstrained/` and `holistic_residual_n5_unconstrained/`.
27. Are the residual forms exactly the affine (GF(2)-linear) determinations, or some other algebraic
    class connectivity cannot see (#130, #106)?
    **Answered — no.** Holistic residual (196/4096, 4.8%) shares **zero** forms with the 512 all-affine
    wirings; affine miss rate is 0%. See `template_coverage_census/FINDINGS.md` (H3). Related: among
    *triadic* strict-mediation forms the four catalog templates leave an 8/24 residual that *is* the
    affine joint (XOR/XNOR) band — a different residue, now the catalog's fifth template (parity).
28. Do the near-boundary holistic forms (#131) sit on a genuine phase boundary in function space — small
    perturbations flipping the verdict?
    **Answered — yes vs confident forms; not residual-specific (n=3 and n=4 unc).** n=3: mean flip
    0.482 vs far-hit 0.273. **n=4 unc residual misses: mean flip 0.371 vs far-hit 0.152 (+21.8 pp);
    near-hit 0.392 (H3 refuted).** See `residual_phase_boundary/` and `residual_phase_boundary_unc/`.
    n=5 replication deferred (exact-Φ cost).

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
    **Answered — PROTOCOL_IS_COMMIT.** Conveyors stay out; joint AND/OR/NAND/XOR with both
    agents reading P are protocol-triadic; no human required. See
    `studies/agent_protocol_triad/`.
38. Does a tool an agent calls join the core when the agent acts on its output, like the inference model
    (#4, #9)?
    **Answered — TOOL_LIKE_INFERENCE.** Unused out; pure act out of major complex; blend joins
    and displaces C (#4/#9 cut). Reciprocity neither necessary nor always sufficient.
    See `studies/agent_tool_core/`.
39. Human-in-the-loop AI: with human, AI, and counterpart, under what coupling is the human in the core
    versus a rubber stamp?
    **Answered — HUMAN_COMMIT_READ.** H in core iff in S’s determination and reads S;
    rubber stamps out; partial veto/read boundary. See `studies/hitl_rubber_stamp/`.
40. Does an AI that online-learns the counterpart's policy displace the counterpart over training, and
    does the displacement track model fidelity (#69)?
    **Answered — SHARP_FULL_DISPLACE.** Low fidelity keeps C; only full `M'=S` puts M in and
    C out; Φ flat (not smooth). See `studies/ai_fidelity_displace/`.
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
