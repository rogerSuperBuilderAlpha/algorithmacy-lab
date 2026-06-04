# Fifty research questions

Open questions that extend the org_frontier experiments. Each is grounded in a specific result, a
surfaced limit, or a refuted hypothesis from the classifier, the corpus, the multiparty suite, the
principal study, the proxy bridge, or the 53-probe loop (see `probes/PROBES.md`,
`STRUCTURAL_FINDINGS.md`). Grouped by theme; each notes what it extends and, where clear, how it would
be tested.

## A. Hardening the two-condition account (coupling + pivotality)

1. **Does a higher-order influence measure close the full-family prediction gap?** Probe 13 refuted a
   context-sensitive single-node measure (AUC 0.649 vs 0.695). Test whether a joint/synergy-based
   influence (pairwise Boolean sensitivity, or a PID-derived term) pushes the 4,096-family AUC toward
   the controlled 0.89.
2. **Can triadicity be predicted from the cause-effect structure rather than per-node features?** The
   residual is holistic (Probe 13). Test whether the relation count or composition (Probe 36) predicts
   the verdict where per-node influence cannot.
3. **Is the 2(n−1) minimal-edge law tight at n=5 and n=6?** Probe 35 found 4 edges at n=3, 6 at n=4.
   Search (or sample) higher n for any triadic form below 2(n−1) edges.
4. **What is the exact triadic rate over the complete n=4 family**, not just the strict-mediation
   sample (2.3%)? Enumerate or larger-sample, and break down the edge-budget distribution.
5. **Does pivotality predict core membership for multi-valued elements?** PyPhi's multi-valued
   extension (Gomez 2021) is not on the IIT-4.0 branch used here; on a build that supports it, test
   whether ternary parties obey the same coupling + pivotality law.

## B. The verdict's robustness and scope

6. **Is the verdict invariant under every reasonable state-individuation choice?** Probe 14 tested
   relabeling and re-encoding. Test coarse-grainings of the state space for verdict flips.
7. **How does the grain-relativity threshold depend on the coordination's timescale?** Probe 32 showed
   the 2-step map washes the triad out. Find the sampling rate below which the triad is always
   detectable, as a function of the form's attractor period.
8. **Do IIT 3.0 and IIT 4.0 give the same verdict on the corpus?** The repo carries both configs;
   the survey flagged the version split. Quantify agreement.
9. **When does correlated (not independent) mediator noise change the verdict rather than the
   magnitude?** Probe 27/38 used independent noise and found graceful degradation. Test structured
   noise.
10. **Is the verdict stable under asynchronous or continuous-time update** rather than the synchronous
    discrete TPM? Build an asynchronous analogue and compare.

## C. Multi-party scaling and structure

11. **Does the triadic rate fall to a floor or to zero past n=5?** The decline is 9.4%→2.3%→0%
    (probes 30, 35, scaling). Sample n=6 (with proxies if needed) for the asymptote.
12. **Is the chain's Φ = 2.0-at-every-depth a theorem, and what sets the constant?** Probe (chains)
    found invariance through n=6. Characterize analytically.
13. **Do branching (tree) mediation topologies dilute like breadth or preserve like depth?** Neither
    pure chain nor pure pool; test intermediate trees.
14. **Can the major complex of a heterogeneous team be predicted from its coupling graph alone?**
    Probe 51 showed the core is a tight subset. Find a graph rule that names it without computing Φ.
15. **At what n does group-level integration beyond members become generic** rather than requiring the
    all-required pool? Probe 52 found it at n=4 for the pool only; map the boundary.

## D. Dynamics and time (the temporal-tracking dimension)

16. **Does a non-stationary mediator bind its regime when analyzed over a lifted state space?** Probe 3
    refuted static analysis of a switching rule. Lift the regime into the system and recompute.
17. **Does an adaptive/learning mediator produce a different verdict trajectory than a fixed one?**
    Update the determination by a learning rule across epochs and track the verdict.
18. **Do Φ and coordination success decouple over learning?** Probe 48 found them orthogonal at a
    snapshot. Train a form toward success and see whether Φ tracks, lags, or ignores it.
19. **Is there any coordination form where Φ peaks at intermediate coupling (criticality)?** Probes 27,
    38 found monotone degradation; Niizato (2024) found a Φ peak at criticality in fish schools. Search
    for an interior maximum.

## E. Estimation and the proxy problem (bridging to data)

20. **Does the Barrett–Seth Φ_AR proxy (the one neuroscience uses) recover the verdict** better than
    Φ_R / Φ_WMS? The proxy bridge tested the latter two (rank-AUC ≤ 0.63). Add Φ_AR.
21. **Can a learned surrogate recover the binary verdict** where single proxies fail? Apply the
    `learned_surrogate` random-forest approach to coordination forms.
22. **What trajectory length stabilizes ΦID estimates, and does more data ever recover the verdict?**
    Probe 47 used 8000 steps. Sweep length.
23. **Does the ΦID synergy separation improve under MMI vs CCS redundancy, or at higher noise?**
    Probe 47 used CCS at noise 0.1.
24. **Can the verdict be estimated from real organizational interaction logs**, and how would it be
    validated? Identify a dataset (handoffs, message threads) and a validation protocol.

## F. The construct's dimensions and its neighbors

25. **Does a better-trained worker model displace the counterpart more strongly?** Probes 4 and 9
    showed a blended model substitutes for the counterpart. Vary model fidelity and measure
    displacement rate.
26. **Is the AI-MC indistinguishability resolvable by any structural refinement?** Probe 20 found the
    W→A→C loop triadic, the distinction a unit-of-analysis choice. Test whether timescale separation or
    a boundary criterion recovers the distinction.
27. **Does second-order theory of mind (the worker models the counterpart's model of the worker) add to
    the core or stay a sink?** Extend the inference probe to nested models.
28. **Can algorithm sensemaking be distinguished structurally from algorithmacy**, or is it dyadic like
    the literacies? Probe 31 placed it dyadic on one form; test a family.
29. **How does the verdict behave for multi-role agents** (a worker who is also a counterpart on
    another platform)? Build a two-platform agent and read the cores.

## G. Platform features and political economy

30. **Is there a coupling regime where the {S,P} platform-and-owner core is the generic outcome?**
    Probe 37 / the principal sweep found it at the extreme. Map how often it occurs.
31. **Can value capture be formalized alongside Φ** so that irreducibility predicts who captures
    surplus? The dissertation offers the political-economy proposition at the binary level only.
32. **Does a regulator node that can override the determination change the verdict**, and must effective
    oversight join the core? Model oversight as a coupled node.
33. **Does the coalition-dominates-principal result scale with coalition size?** Probe 37 used a pair.
    Test whether a larger counterpart coalition always wins.
34. **Does platform-side information asymmetry (the platform observes more than either party) have a
    structural signature** distinct from the determination structure?
35. **Does a "fair" determination (one not favoring the principal) carry a different Φ signature than an
    extractive one?** Probe 16 tied balance to influence-symmetry; extend to principal-weighted forms.

## H. Adjacent measures and consilience

36. **Do O-information, PID, ΦID, and causal-emergence verdicts agree with exact Φ across the 256-form
    family?** A consilience study (cf. Comolatti & Hoel 2025) mapping where the measures concur and
    diverge.
37. **Is there any cheap measure that cleanly separates the verdict**, or is exact Φ irreducibly
    required for this class? Probes 45, 46, 47 found dependence measures fail; widen the search.
38. **Does O-information separate the verdict better on the transition structure than the present-state
    joint?** Probe 46 was weak on the present-state joint.
39. **How does the EI-versus-Φ relationship generalize across the family?** Probe 49 found triadic
    forms have more causal emergence but lower EI on the corpus; test the full family.

## I. Validation and ground truth

40. **Can the binary verdict be validated against an agent-based coordination-difficulty measure across
    the whole corpus**, extending the dissertation's single-contrast behavioral check?
41. **Do human subjects coordinating through structurally-triadic vs dyadic interfaces show the
    predicted difficulty gap?** A lab experiment the model predicts.
42. **Can independent coders assign coordination structures to real organizations with agreement?** The
    dissertation names inter-rater coding as required work; test reliability.
43. **Does a Niizato-style size-4 discontinuity appear in any coordination family with richer (less
    collapsing) dynamics?** Probe 44 found the deterministic forms collapse; design non-collapsing
    dynamics.

## J. Theory and formal characterization

44. **Is "triadic" equivalent to a graph-theoretic property** (a non-separable determination hypergraph
    plus a feedback cycle), yielding a Φ-free test for this class? Probes 25, 39 supply the ingredients.
45. **Can the 4-edge minimum and cycle-necessity be unified into a necessary-and-sufficient structural
    theorem for n=3 triadicity?**
46. **Is role-symmetry an exact automorphism of the verdict under worker↔counterpart relabeling?**
    Probe 22 showed it behaviorally; prove or find a counterexample.
47. **Is there a form that is triadic at the system level but where no single party is pivotal** (pure
    higher-order binding)? Probe 13's holistic residual hints this may exist.

## K. New application domains

48. **Is a market clearinghouse (many buyers and sellers plus a matching/clearing mechanism)
    structurally triadic?** Extend the multiparty pool to a market form.
49. **Which voting/aggregation rules yield triadic governance forms?** Probe 10 found majority factors;
    map the aggregation-rule space (plurality, supermajority, veto, ranked) to verdicts.
50. **When is multi-agent AI coordination through a protocol irreducible?** Apply the classifier to AI
    agents coordinating via a shared protocol, asking whether the protocol is a conveyor (dyadic) or a
    committing third party (triadic).

---

Priority picks, by leverage: #36 (consilience map — directly advertisable and engages the dossier's
adjacent-measures literature), #20/#24 (the data bridge — the path to real organizational data),
#40/#41 (behavioral validation — the missing ground truth), #44/#45 (a Φ-free structural theorem —
would make the classifier cheap and exact at once), and #31 (value capture — the political-economy
payoff the dissertation defers).
