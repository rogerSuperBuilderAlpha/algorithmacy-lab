# Committee panel review — "Committed determination: one axis across six exact-Φ studies"

A four-member committee reviewed the synthesis paper
(`committed_determination_synthesis.md`). Each member read the synthesis and the studies it leans on,
from a distinct lens, and returned an independent verdict. All four returned **major revisions**. This
document records the panel, the chair's synthesis, and the consolidated revision list. The revised
paper responds point by point in its own revision note.

## The verdicts

| Member | Lens | Verdict | The one objection that mattered most |
|--------|------|---------|--------------------------------------|
| 1 | IIT / formal methods | major revisions | the Shapley "bridge" and the "one line" convergence are stated more strongly than the studies and their own deep-research reports support |
| 2 | Economics | major revisions | the competitive-bottleneck mapping is wrong: the captured side is the *single-homing* side that lacks a competing platform-route, not "parties with no outside option to each other" |
| 3 | Organization theory / methods | major revisions | algorithmacy is verdict-identical to directive algorithmic management with no discriminating case; and the affirmative instrument-choice case is available but not made |
| 4 | Adversarial skeptic | major revisions | the convergence is coincidence of verdicts on hand-built models, neither derived nor predictive; and "committed determination" is defined as the condition that produces triadicity (circular) |

## Chair's synthesis

The panel was unusually unanimous, and its objections cluster into five, in order of severity.

**1. The convergence is asserted at an altitude the paper's own limitations retract.** Three members
independently flagged that "Read down any column and it is the same line" contradicts the paper's own
"shown by coincidence of verdicts, not derived." Only the IIT↔Shapley column has any computational
coincidence behind it, and that one is qualified. The table reads as five independent confirmations; it
is one qualified coincidence plus four verbal mappings.

**2. A substantive economics error.** The economist identified a real mistake: Armstrong's competitive
bottleneck captures the *single-homing* side (which lacks a competing platform-route to a given
counterparty), not the side with "no outside option to reach each other." The paper conflates two
distinct axes — *disintermediation* (can the two sides bypass the platform entirely?) and *capture*
(which side is exploited within platform competition) — and conflates two distinct results (bilateral
surplus-division, Binmore–Shaked–Sutton, with multi-sided pricing, Armstrong) into one row. This is not
pedantry; the bottleneck's content is precisely this distinction.

**3. The tautology, and built-in versus discovered convergence.** The skeptic and the methods member
pressed the same crack from two sides: "committed determination" is defined as the condition that
produces triadicity, so "the studies are six views of one variable" is, for the stipulated models,
analytic rather than discovered — and the synthesis does not pass through the constituent papers'
sharper admission (the membership paper calls one core result "close to tautological by construction").
The informative cases (a routing cycle reading triadic against the naive reading; rotations; the
extremes-only quorum law) are real and should be separated from the cases where the axis was encoded in.

**4. The two original results are overstated, and one statistic is internally inconsistent.** The IIT
member found the graded-pivotality "bridge" rests on a single-node influence measure that undercounts
the higher-order marginal contributions the Shapley value is defined over, is population-dependent, and
is "precise only at the null-player corner" by the source paper's own statement. He also flagged a
factual inconsistency: the membership study reports rank-AUC 0.629 (unconstrained family) while its own
deep-research report cites 0.89 (strict-mediation family) — two populations, presented as if one
headline number.

**5. The instrument-choice case is unmade, and the construct's distinctness is undefended.** Both the
methods member and the skeptic asked: if a cheap commit-versus-convey coding reaches the same verdict,
what does exact Φ add, and is algorithmacy more than directive algorithmic management re-labeled? The
methods member noted, importantly, that the affirmative answer is *available in the material* and merely
buried: one computation returns five disciplinary tests; the major complex names *which* parties bind,
which a binary coding cannot; and the graded membership law is a genuinely Φ-specific result. The paper
should make this case and explicitly not claim Φ is *necessary*.

Plus minor prose: the antithesis construction is overused (one line stacks four), the "a construct earns
its place" trope repeats across two papers, and the closing section restates the one before it.

## The consolidated required revisions

1. Bring the convergence table and "the same line" down to the limitations' altitude: state that four of
   five columns are structural/verbal correspondences and only IIT↔Shapley has computational coincidence.
2. Correct the competitive-bottleneck mapping (single-homing side; competing route), and separate
   disintermediation from capture, and surplus-division (BSS) from platform pricing (Armstrong).
3. Address the tautology: state committed determination independently of triadicity where possible, and
   partition the six studies into stipulated-axis (analytic) and computed-against-naive (informative).
4. Restore the bridge's caveats (undercounting proxy, population-dependence, null-player-corner only);
   downgrade "bridges" to "conjectured, verified at one corner"; reconcile the 0.629/0.89 AUC by naming
   both populations.
5. Make the affirmative instrument-choice case (unification, the major complex names who binds, the
   Φ-specific graded law), and state Φ is not claimed necessary. Defend algorithmacy as a generalization
   of directive algorithmic management to the worker–system–counterpart triad, not a wholly new construct.
6. Move the 40%-flip-under-re-encoding fact beside the convergence table; cut the antithesis tics;
   rescope headline claims to "Boolean models of coordination."

**Update.** The panel's fourth point — that the Shapley bridge was verified only at the null-player
corner on a single-node proxy — has since been taken up directly in
[`threads/shapley_membership`](../threads/shapley_membership/THREAD.md): the *exact* Shapley value over
the φ_s coalition game predicts major-complex membership at rank-AUC ≈ 0.87, against ≈ 0.63 for the
single-node influence the study used, and is the best predictor among pivotality notions. The moderate
AUC was the proxy's weakness, not the correspondence's; the bridge holds well past the corner as a
magnitude relation, though not as a clean equivalence. This strengthens the program's one genuinely new
result rather than retracting it.

The chair notes, with the panel, that none of this demotes the apparatus. The affirmative case — exact
Φ is a principled, unified, structure-naming lens on coordination irreducibility — is intact and, by the
methods member's reading, *stronger* once stated outright. The revisions match the paper's claims to the
evidence the studies produced, and answer the pushback rather than concede it.
