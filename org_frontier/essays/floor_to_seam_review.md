# The seam carries what the scalar drops: a review of the floor-to-seam program (Q45–Q62)

Fourteen studies, run end to end through the lab's six-stage protocol and logged as probes #145–#214,
trace a single line of thought. It starts with a counting question about which coordination forms reach
the integration ceiling and ends with a claim about organizational theory: the partition that Φ resists
least carries Thompson's interdependence type even where the Φ number itself reports nothing. This review
follows that line, states where it now stands, and lays out ten places a collaborator could take it next.

The program assumes the lab's instrument and its central law, both set out in
[`studying_algorithmacy.md`](studying_algorithmacy.md). A coordination form is a small Boolean system of a
worker W, a mediating system S, and a counterpart C, each updating from the others' previous states. The
verdict is Φ over the minimum-information partition: Φ_MIP = 0 means the form factors into independent
pieces and demands only literacy; Φ_MIP > 0 means no party-respecting cut recovers the whole and the work
demands algorithmacy. The law is that a form is triadic exactly when every party is bound into one
irreducible joint determination. In the 256-form strict-mediation family at three nodes, only 9.4% clear
that bar.

## Where the line started

Two earlier questions set the stage. Q43
([`questions/q43_thompson_interdependence/`](../questions/q43_thompson_interdependence/)) asked whether exact
Φ reproduces Thompson's 1967 ordering of organizational interdependence — pooled, then sequential, then
reciprocal. It mostly did, with one sharp refutation: two structural primitives that should have predicted
the verdict failed, because a directed cycle in a wiring diagram is a different object from a closed loop in
the causal structure Φ integrates over. Q49
([`questions/q49_mip_seam_mincut/`](../questions/q49_mip_seam_mincut/)) then looked at the MIP itself rather
than its scalar, and found the canonical triad's weakest seam is a tie, not a worker-as-weakest-link verdict,
and not the graph min-cut. Both results pointed the same way. The MIP is a richer object than the number it
produces, and the wiring graph is a poor proxy for it. The floor-to-seam program is the consequence of taking
that seriously.

## The floor and what saturates it

A strict-mediation triad at three nodes needs a minimum number of directed edges to integrate at all. Q45
([`questions/q45_edge_floor_uniqueness/`](../questions/q45_edge_floor_uniqueness/), probes #145–#149) fixed
that minimum at four edges, the 2(n−1) floor, and asked which determination classes reach the Φ ceiling
there. The expected answer was that the conjunctive hub — the AND mediator — is the unique form that
saturates. It is not. Sixteen forms reach Φ=2.0 at the four-edge floor and only two of them are AND. The
ceiling is shared by the whole monotone class, while parity rules sit at a separate plateau of Φ=0.5 (8 of 8
parity forms). Saturation splits by monotone-versus-parity class, not by AND alone. The conjunctive hub is
the canonical member of the high-ceiling class, not its sole occupant.

That left a smaller puzzle inside the result. OR is monotone, yet only two of sixteen OR-labelled
strict-mediation forms bind triadically at the floor. Q50
([`questions/q50_or_triadic_seam/`](../questions/q50_or_triadic_seam/), probes #150–#154) found the rule that
separates them. An OR triad binds only when the two outer parties read the mediator through matched,
non-constant channels; constant or asymmetric reads collapse it. The same study turned up a structural
regularity that drives the rest of the program: commit symmetry governs the read rule. Symmetric monotone
commits (AND, OR, NOR, NAND) bind on matched reads, while implication commits bind only on complementary
reads. The two binding OR forms share the canonical seam; the fourteen that collapse do not.

## The back-channel and the ceiling

Implication commits became the test bed because they bind under the most restrictive read condition. Q51
([`questions/q51_implication_backchannel/`](../questions/q51_implication_backchannel/), probes #155–#159)
asked whether adding a direct worker–counterpart edge — a back-channel, the thing strict mediation forbids —
lets a matched-read implication form reach the ceiling. It does not. A one-sided worker back-channel never
reaches Φ=2.0 on any of the eight matched forms, though six of eight do become triadic below the ceiling. A
symmetric two-sided back-channel binds all eight, but at a single value of Φ=0.830075, erasing the structure
the one-sided wiring leaves behind.

That structure is a ladder. One-sided wiring sorts the eight forms into three rungs: 0.830075, 0.415037, and
dyadic. Q52 ([`questions/q52_phi_ladder_mechanism/`](../questions/q52_phi_ladder_mechanism/), probes
#160–#164) explained the sort. The four implication commit indices split into a W-centric pair {2,13} and a
C-centric pair {4,11}, named by which input state they distinguish. W-centric forms take the high or the
dyadic rung depending on the polarity of their party read at the distinguishing state; C-centric forms sit on
the middle rung regardless of read pairing. Symmetric coupling pulls every form to the shared 0.830075
equilibrium and flattens the ladder.

So conjunctive coupling has a ceiling of 0.830075 once outer-party coupling is added beyond the floor. Q53
([`questions/q53_impl_phi_ceiling/`](../questions/q53_impl_phi_ceiling/), probes #165–#169) asked whether
that ceiling is absolute, and found it is not. A parity back-channel breaks it. A symmetric XOR gate restores
Φ=2.0 on all eight matched implication forms, and a one-sided XOR reaches the ceiling on four of eight, sorted
by commit class. Across sixty-four AND/OR/cross topologies, zero reach Φ=2.0. The supremum of 0.830075 holds
for monotone coupling only; parity coupling lifts the matched forms back to the strict-mediation ceiling.

## Why parity breaks it

Q54 ([`questions/q54_xor_parity_mechanism/`](../questions/q54_xor_parity_mechanism/), probes #170–#174) took
apart the parity result. Three things turn out to carry it and one does not. Bijectivity of the channel gate is
necessary: all thirty-two ceiling pairs have bijective gates, no non-bijective gate reaches the ceiling.
Parity-class membership is necessary: zero of sixty-four monotone topologies saturate, while XNOR joins XOR at
Φ=2.0 on all eight. Seam distinguishability rises: the conditional entropy H(W,C|S) at the seam climbs about
0.91 bits under symmetric XOR relative to AND. What does not carry it is any whole-system symmetry — global
TPM permutation is refuted, since the ceiling pairs have non-permutation transition matrices. The ceiling
returns when the back-channel is a locally invertible parity map that raises distinguishability at the seam,
not when it makes the system as a whole more symmetric.

Bijectivity is necessary but not sufficient. Q55
([`questions/q55_bijective_discriminator/`](../questions/q55_bijective_discriminator/), probes #175–#179)
separated the forty-eight bijective parity pairs into the thirty-two that reach the ceiling and the sixteen
that stop below it. The sixteen are exactly the misaligned one-sided forms: they sit at the Q52 middle rung of
0.415037, and their MIP is the mediator-singleton cut {S,WC}. The ceiling pairs are either symmetric or
commit-aligned one-sided, and their MIP cuts an outer party or the whole. XNOR inverts the alignment polarity
relative to XOR but obeys the same partition. Below-ceiling is a wiring-alignment failure with a signature in
the partition, not in the scalar alone.

## The geometry of the seam

The partition signatures from Q55 turned the program toward MIP geometry, the original concern of Q49. Q56
([`questions/q56_symmetric_complete_mip/`](../questions/q56_symmetric_complete_mip/), probes #180–#184) asked
why the symmetric ceiling pairs uniformly adopt the complete three-part MIP {W,S,C} while the aligned
one-sided pairs keep an outer-party singleton seam. Both outer-party two-part cuts reach the system Φ on every
ceiling pair. The IIT-4.0 tie-break selects among them by minimum normalized Φ, and on the symmetric pairs
both outer cuts carry a normalized Φ of 1.0 while the complete partition carries 0.5, so only the complete
partition enters the official tie set. Symmetric coupling restores full directional W/C symmetry, which is what
keeps both outer cuts tied and hands the verdict to the complete partition.

One-sided wiring breaks that symmetry, and Q57
([`questions/q57_channel_direction_mip/`](../questions/q57_channel_direction_mip/), probes #185–#189) found the
rule. The back-channel recipient — the outer party whose update gains the extra incoming edge — is always the
tied singleton seam: worker wiring gives {W,SC}, counterpart wiring gives {WS,C}. The recipient singleton and
the complete partition both carry the minimum normalized Φ of 0.5; the non-recipient singleton carries 1.0 and
is excluded, although it also reaches the system Φ. The recipient's normalized Φ is exactly half the
non-recipient's, a ratio of 2.0 with zero spread across all sixteen forms.

Q58 ([`questions/q58_normalization_cut_geometry/`](../questions/q58_normalization_cut_geometry/), probes
#190–#194) reached into PyPhi's normalization to explain the constant. Under the IIT-4.0
NUM_CONNECTIONS_CUT rule, normalized Φ is Φ divided by the count of severed directed connections. Both outer
cuts carry the same unnormalized Φ of 2.0; the recipient cut severs four connections and the non-recipient
two, so the 2.0 ratio is the 4-versus-2 severed-connection asymmetry and nothing else. Q59
([`questions/q59_directed_cut_edges/`](../questions/q59_directed_cut_edges/), probes #195–#199) closed the
geometry thread by naming the edges. The back-channel cross-edge is severed in both cuts, so it is not the
source of the asymmetry; the residual 3-versus-1 split after accounting for it comes from two mediator-incident
edges that fall in the recipient-only side of the cut difference.

## The turn back to theory

The geometry thread answered how the seam is placed. The last three studies asked what the seam means, and
this is where the program connects back to the question the lab exists to answer. Q60
([`questions/q60_thompson_backchannel/`](../questions/q60_thompson_backchannel/), probes #200–#204) brought
back Thompson's return-path typing from Q43. On the sixteen aligned one-sided ceiling forms, the recipient
determines the interdependence type: worker wiring reads sequential on all eight, counterpart wiring reads
reciprocal on all eight. The scalar verdict cannot see this. Every form reads triadic at exactly Φ=2.0 with
zero spread, so max_phi assigns no difference between sequential and reciprocal coordination. The type survives
at the level of the partition template, the recipient mediator-severance signature from Q59, and it collapses
at the level of the scalar. Q43's feedback-cycle heuristic collapses it too, calling every form reciprocal,
because the cross-edge closes a graph cycle on all sixteen — the same graph-versus-causal-structure gap that
refuted Q43's fifth hypothesis, reappearing in a new place.

Q61 ([`questions/q61_seam_return_typing/`](../questions/q61_seam_return_typing/), probes #205–#209) made the
connection exact. The official MIP singleton seam and the return-path type are co-extensive partitions of the
panel: worker-seam pairs with sequential on all eight, counterpart-seam with reciprocal on all eight, with zero
within-class heterogeneity in either direction. The seam recovers the sequential/reciprocal distinction that
the uniform Φ=2.0 verdict discards. Seam and type are equal partitions, two encodings of one two-way split.
Q62 ([`questions/q62_excluded_cut_signal/`](../questions/q62_excluded_cut_signal/), probes #210–#214) checked
the one remaining MIP-derived label, the excluded non-recipient cut, and found it carries no independent
signal: it is the deterministic complement of the tied seam and the inverse mirror of the type, collapsing the
triple to two joint cells. The seam/typing thread ends there.

## Where the program stands

The line of thought now supports one claim with a clear mechanism behind it. **On the back-channel panel, the
MIP carries organizational-interdependence information that the integration scalar discards.** Sixteen forms
that a Φ=2.0 verdict treats as identical split cleanly into sequential and reciprocal coordination, and the
seam — which outer party the minimum-information partition severs as a singleton — is the carrier. The seam's
placement is fixed by the back-channel recipient (Q57), grounded in a severed-connection count (Q58), and
co-extensive with Thompson's type (Q61).

The supporting results are sharp enough to restate as a short list. The integration ceiling at three nodes is a
monotone-versus-parity property, not an AND property (Q45). Monotone outer coupling beyond the floor caps at
Φ=0.830075, and only a locally bijective parity channel that raises seam distinguishability restores the
Φ=2.0 ceiling (Q53, Q54). Below-ceiling parity forms are exactly the misaligned one-sided forms, with a
mediator-singleton MIP (Q55). Directional symmetry decides whether the MIP is the complete partition or an
outer singleton, through the normalized-Φ tie-break and a 4-versus-2 severed-connection ratio (Q56–Q59).

Two cautions sit inside the synthesis. The Q43 graph-cycle failure recurred in Q60: a directed cross-edge
closes a wiring cycle and a naive feedback predicate over-calls reciprocal, while the causal structure does
not. Reading interdependence off the wiring graph stays unreliable. And the typing recovery is shown on one
sixteen-form panel of aligned one-sided ceiling pairs. It is a strong existence result — the seam can carry
type where the scalar cannot — and it is not yet a corpus-wide claim.

## What the program cannot do

The verdicts are in-silico. They are exact Φ on deterministic n=3 Boolean models with synchronous update, read
at the finest grain. They are evidence about the models. The validation gap to real organizations is not
narrowed by any of these studies, and computing harder does not narrow it. The Φ=2.0 ceiling, the 0.830075
plateau, and the seam/type co-extensiveness are facts about a specific small family, established to the point
where every number reproduces from a committed script under CI. Whether a documented platform-work
back-channel sits where the panel says it should is an empirical question none of this answers.

## Ten directions

A collaborator could pick up any of these. Each grows from a stated finding and most stay inside the lab's
cheap-computation regime.

1. **Seam typing across the whole corpus.** Q61 shows seam-equals-type on sixteen aligned one-sided forms.
   Run the seam against the full 256-form strict-mediation family and the 4,096-wiring superset and test
   whether the singleton seam recovers a Thompson type wherever the scalar verdict is constant. This turns an
   existence result into a general instrument or finds where it breaks.

2. **A fourth party.** Breadth dilutes irreducibility toward zero while depth preserves it (the n=3/n=4/n=5
   scaling in [`multiparty/`](../multiparty/)). Add a second counterpart or a second mediator and test whether
   the recipient-determines-seam rule (Q57) and the seam/type co-extensiveness (Q61) survive at n=4, and
   whether parity still breaks a higher ceiling. Exact Φ is still feasible here.

3. **Stochastic commits.** Replace the deterministic mediator TPM with a noisy one and watch the Φ=2.0 ceiling
   degrade. Does the seam keep carrying type as noise rises, and is there a noise threshold where the
   sequential/reciprocal split stops being recoverable? This probes how fragile the verdict-versus-seam gap is.

4. **Closed forms for the ladder constants.** The values 0.830075 and 0.415037 recur with zero spread across
   the panel. Derive them analytically from the cut geometry and the NUM_CONNECTIONS_CUT normalization (Q58)
   and predict the rung of a form from its wiring without running PyPhi. A confirmed derivation would give the
   ladder a theory rather than a measurement.

5. **Graded back-channels.** Q51 and Q53 use full or absent cross-edges. Build a probabilistic cross-edge of
   tunable strength and look for a phase transition between the middle rung and the ceiling. Locating a
   threshold would say how much direct contact converts coordination from one regime to the other.

6. **The full non-monotone ceiling-restoring class.** XOR and XNOR break the ceiling; sixty-four monotone
   topologies do not (Q53, Q54). Enumerate every two-input gate and, at n=4, every higher-arity gate, and map
   which determination classes restore a ceiling. The open question is whether "parity" is the right
   characterization or a special case of a broader bijectivity-plus-distinguishability condition.

7. **Coarse-graining the ceiling form.** Take a symmetric XOR ceiling form, coarse-grain its state space, and
   test whether the triadic verdict and the seam survive the grain change. This attacks the model-relativity
   limit directly and asks whether the seam/type result is an artifact of finest-grain reading.

8. **One empirical anchor.** Pick a documented platform-work back-channel — rideshare driver and rider
   exchanging numbers off-app, two contractors coordinating around a ticketing system — model it as a wiring
   form, and locate it on the panel. One careful mapping would not close the validation gap, but it would test
   whether the panel's categories correspond to anything a field researcher recognizes.

9. **A topology zoo of multiple back-channels.** Q57's recipient-determines-seam rule assumes one cross-edge.
   Add two cross-edges, or a full directed triangle, and ask when the seam stops being a singleton and whether
   two recipients produce two seams or one complete partition. This generalizes the central mechanism past the
   single-recipient case.

10. **Graph cycles versus causal cycles, formalized.** The same failure appears in Q43 and Q60: a directed
    wiring cycle is not a closed loop in the causal structure Φ integrates over, and feedback heuristics built
    on the wiring graph misclassify. Characterize exactly when a graph cycle does and does not produce causal
    integration, as a standalone foundational result. It would explain two refutations at once and warn off a
    tempting shortcut the rest of the field is likely to reach for.

The through-line of the program is that the scalar throws information away and the partition keeps it. The
ten directions either test how far that holds or push on the wall between the models and the organizations
they are meant to stand for.
