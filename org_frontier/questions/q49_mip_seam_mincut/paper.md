# The weakest seam is a tie

<code + data: org_frontier/questions/q49_mip_seam_mincut/ ; probes #140–#144 in probes/PROBES.md>

## Abstract

The minimum-information partition (MIP) of a coordination form names its informational weakest link, and
two earlier probes in this program read that link as the worker: every triadic corpus form was reported to
cut at `{W,SC}`, the worker severed as a singleton. This study reads the full MIP tie set rather than the
single representative PyPhi prints. The canonical triad has four tied MIPs, and the `{W,SC}` cut ties
exactly with its mirror `{WS,C}`, so the worker is not the unique seam (H1, confirmed). Across all 24
triadic forms of the n=3 strict-mediation family the seam set is symmetric in worker and counterpart, with
zero forms severing the worker alone (H2, confirmed). The symmetry is robust: a one-sided back-channel that
makes the wiring asymmetric leaves the seam tied at a lower Φ (H3, refuted), and the side carrying the
channel does not move the seam (H4, refuted). A connectivity min-cut matches the seam on the conjunctive
forms but fails on all 8 parity forms, whose MIP is the complete partition with no singleton seam (H5,
confirmed). The worker-as-weakest-seam result is a labeling convention over a degenerate tie, and agenda
question #49's min-cut theorem for the seam does not hold.

## Introduction

A coordination form modelled as a small Boolean dynamical system has a minimum-information partition: the
cut along which the system most nearly factors. Balduzzi and Tononi introduced it as the informational
"weakest link," the decomposition into the parts that are most independent of one another
(`balduzzi2008integrated`). Reading the MIP of the worker–system–counterpart triad, two earlier probes in
this program found the worker on one side of that cut. Probe #26 reported every triadic corpus form cutting
at `{W,SC}` and read it as a structural claim: the worker is the most separable party, the system and
counterpart cohere more tightly than the worker attaches. Probe #33 made it a population statement, 67% of
triadic forms cutting at `{W,SC}` and 33% at the complete partition.

Two other results in the program make that reading suspect. Worker↔counterpart relabeling is an exact
automorphism of the verdict, 0 flips and 0 Φ difference over 256 forms (#55), and every triadic form
carries balanced determination influence, with any influence asymmetry collapsing the form to dyadic (#16).
For a form symmetric in the two parties, the `{W,SC}` and `{WS,C}` partitions must carry identical
integrated information, so neither can be the unique seam. The earlier probes never checked this, because
each read a single MIP per form and the IIT 4.0 tie-break returns one representative of a tie set by a fixed
convention (`albantakis2023iit4`). This study reads the tie set itself, asks whether a verdict-preserving
asymmetry can make the seam unique, and tests whether a unique seam falls at a connectivity min-cut — agenda
question #49.

## Related work

The MIP carries an explicit tie rule from its first formulation. Balduzzi and Tononi search all partitions
for the minimum normalized integrated information and, when several partitions attain it, select the ones
with the lowest unnormalized value as the minimum information partition(s) — the plural is in the original
(`balduzzi2008integrated`). IIT 3.0 carried the MIP forward (`oizumi2014phenomenology`), descending from the
integration proposal of `tononi2004information`, and IIT 4.0 fixes the normalization so the partition reads
a system's fault lines, with ties broken by the largest unnormalized φs under the principle of maximal
existence (`albantakis2023iit4`). PyPhi computes this and exposes the tie set
(`mayner2018pyphi`), which is what lets this study read the seam as the program's earlier probes did not.

A partition of a system invites a graph reading. The min-cut of an edge-weighted graph is the two-set split
minimizing crossing-edge weight (`stoer1997simple`), and IIT 4.0's normalization counts the connections a
cut severs, favoring cuts across few connections (`albantakis2023iit4`). Whether the cause-effect MIP
reduces to a graph min-cut is an empirical question, and the program's prior work cautions against it:
connectivity predicts the triadic verdict only to about 93% at n=3, with a holistic residual no graph
feature recovers (#54, #94, #106). Organization theory has its own weakest link. Hirshleifer models public
goods whose provision is the minimum contribution, arising when each member holds a veto, as when each is
responsible for one link of a chain (`hirshleifer1983weakest`); coordination theory frames coordination as
managing dependencies whose structure sets the mechanism (`malone1994interdisciplinary`,
`thompson1967organizations`). A coordination form's structural weakest link, read off the MIP, is the formal
analogue, and identifying it with the worker is a substantive claim worth checking against the tie set.

## Hypotheses

Fixed before computation (Stage 3), each with its structurally-expected null. The seam set of a form is the
set of parties severed as a singleton by some tied two-part MIP at the max-Φ reachable state.

- **H1 — the canonical worker seam is a tie.** The canonical triad's MIP is degenerate: `{W,SC}` ties with
  `{WS,C}`, so the seam set is `{W,C}` and the worker is not unique. H0: `{W,SC}` is the unique MIP.
- **H2 — no triadic strict-mediation form has a worker-unique seam.** Across all 24 triadic forms,
  (W in seam) iff (C in seam). H0: at least one form severs the worker alone.
- **H3 — a one-sided back-channel breaks the seam tie.** Adding W'=S∧C keeps the form triadic and leaves a
  single severed party. H0: the seam tie survives, seam set stays `{W,C}`.
- **H4 — the broken seam follows the read direction.** A worker-side channel puts the seam on the
  counterpart, a counterpart-side channel on the worker, a symmetric channel restores the tie. H0: the side
  of the channel does not determine the seam.
- **H5 — the seam is not the connectivity min-cut.** The Φ-seam equals the graph min-cut for conjunctive
  forms but not for the parity forms, whose MIP is the complete partition. H0: the Φ-seam equals the graph
  min-cut on every triadic form.

## Methods

All forms are n=3 deterministic Boolean systems with little-endian indexing W, S, C, classified with the
program's exact-Φ instrument (`classifier.classify_rules`, wrapping `proxy_audit.exact_phi`). The seam is
read at the form's max-Φ reachable state by taking `new_big_phi.sia`, collecting the tied partitions
(`sia.ties`), and recording which party each tied two-part partition severs as a singleton. The graph
min-cut singleton set is the parties minimizing total crossing-edge degree in the connectivity matrix,
`cut(X) = Σ_{j≠X} cm[X,j] + cm[j,X]`. The helper is `seam.py`; each hypothesis has one probe
(`probe_seam_tie.py`, `probe_seam_family.py`, `probe_seam_break.py`, `probe_seam_direction.py`,
`probe_seam_mincut.py`).

The instrument control is the canonical triad W'=S, S'=W∧C, C'=S, the established triadic form (#57, #26).
Every probe asserts it reads triadic at Φ=2.0 with MIP `2 parts: {W,SC}` before running its comparison;
all five passed. The decision rules above were committed to git before the probe code existed
(`balduzzi2008integrated`-style ties were anticipated, but the family sweep, the back-channel behavior, and
the min-cut comparison were not computed until after commitment, following `chamberlin1890multiple` and
`brodeur2024preregistration`). Results are evidence about these Boolean models, separated from claims about
real organizations by the validation gap the docking standard fixes (`axtell1996aligning`).

## Results

**H1 — confirmed.** The canonical triad has system Φ=2.0 with four tied MIPs at that value: `{W,SC}`,
`{WS,C}`, and the complete partition `{W,S,C}` twice. The seam set is `{W,C}`, and `{S,WC}` is absent. The
`{W,SC}` cut that #26 reported is one of two symmetric representatives; the worker and the counterpart are
severed on identical terms. PyPhi prints `{W,SC}` because the IIT 4.0 tie-break selects one representative
(`albantakis2023iit4`), not because the worker is the unique fault line.

**H2 — confirmed.** The strict-mediation family has 24 triadic forms, matching #33. Every one has
(W in seam) iff (C in seam): zero forms sever the worker alone. The breakdown recovers #33 exactly. The 16
conjunctive forms (Φ=2.0) all have seam set `{W,C}` — each is a `{W,SC}`/`{WS,C}` tie — and the 8 parity
forms (Φ=0.5) all have an empty seam set, their MIP the complete partition. So #33's 67% cutting `{W,SC}`
are 16 forms each tying the worker cut with the counterpart cut, and its 33% cutting the complete partition
are the 8 parity forms. No triadic strict-mediation form makes the worker a weakest seam the counterpart is
not.

**H3 — refuted.** The worker-side back-channel W'=S∧C, which adds a direct C→W read, stays triadic but
drops to Φ=1.0, and its seam set is still `{W,C}`. The one-sided wiring asymmetry lowers integration without
breaking the seam tie. The premise that a verdict-preserving asymmetry would make the seam unique fails: the
seam stays symmetric in the two parties even when the connectivity graph does not.

**H4 — refuted.** Across the panel the read direction does not move the seam. The worker-side channel leaves
seam `{W,C}`, the counterpart-side channel leaves seam `{W,C}`, and the symmetric two-sided channel raises Φ
to 6.0 with an empty seam set, its MIP the complete partition. None of the three matches the predicted
`{C}`, `{W}`, `{W,C}`. A one-sided read changes the magnitude of Φ but not which parties the MIP severs,
and a two-sided read converts the form to one with no singleton seam at all.

**H5 — confirmed.** The Φ-seam and the connectivity min-cut disagree on 8 of 11 forms. The canonical triad
and both one-sided back-channel forms agree, all three with Φ-seam `{W,C}` and min-cut `{W,C}`. All 8 parity
forms disagree: their Φ-seam is empty (complete-partition MIP) while the graph min-cut still returns
`{W,C}`. The min-cut matches the seam on the conjunctive forms by accident of their symmetry and fails on
every parity form, so there is no graph min-cut theorem for the seam. This is connectivity's failure to
fix the verdict (#54, #94, #106), now shown for the location of the partition as well as its value.

## Discussion

The five results converge on one statement: the worker is never the unique weakest seam of a triadic
coordination form. For every form in the family the MIP severs the worker and the counterpart on equal
terms, because the seam tracks the determination's symmetry in the two parties, and every triadic form has
balanced determination influence (#16). The worker-as-weakest-seam reading of #26 and #33 is a labeling
convention over a degenerate tie that the IIT 4.0 tie-break resolves to one representative
(`albantakis2023iit4`). The correction is exact and traceable: the 67% and 33% of #33 are the 16 conjunctive
and 8 parity forms, and reading the tie set shows the conjunctive forms tie the worker cut with the
counterpart cut while the parity forms have no singleton seam.

The seam symmetry is sturdier than the wiring. A one-sided back-channel makes the connectivity graph
asymmetric and lowers Φ, yet the seam stays tied (H3), and the side carrying an extra read does not move it
(H4). The seam is a property of the cause-effect structure, which stays symmetric in the two parties as long
as the determination does, not a property of the edge graph. That is why a graph min-cut, which depends only
on edges, matches the seam on the symmetric conjunctive forms and fails on the parity forms (H5). Agenda
question #49 asked for a min-cut theorem placing the MIP at the least-coupled node; for this family there is
none. The answer extends the program's standing result that connectivity is necessary for the verdict but
never sufficient (#54, #94, #106): the graph underdetermines not only whether a form is triadic but also
where its partition falls.

The organizational reading is narrow and worth stating carefully. A coordination form's structural weakest
link is the analogue of the weakest-link party in Hirshleifer's chain (`hirshleifer1983weakest`), but the
model says the worker and the counterpart sit at that link symmetrically. Any account that treats the worker
as the structurally most expendable party in an algorithmic triad has to locate the asymmetry in something
outside these forms — the parties' interests, their outside options, or the determination's content — because
the irreducible structure of a balanced triad does not single the worker out.

## Limitations

The forms are n=3, the strict-mediation family plus three n=3 back-channel variants, read at the max-Φ
reachable state under synchronous update; the verdict's grain- and schedule-relativity carries to the seam
(#32, #62, #112). The back-channel W'=S∧C is one verdict-preserving asymmetry, and it lowers Φ rather than
holding it at 2.0, so it does not match the gentler observation channel of #24; other asymmetries
(asymmetric mediator reliability #38, self-loops #43) were not tested and could in principle break the seam
where a W–C channel does not. The min-cut tested is the unweighted total-degree cut; a weighted or directed
min-cut might track the seam more closely on the conjunctive forms, though it cannot help on the parity
forms, where there is no singleton seam to find. The results are evidence about these Boolean models, not
about firms (`axtell1996aligning`).

## References

Cited keys resolve to `literature/references.bib`: `albantakis2023iit4`, `axtell1996aligning`,
`balduzzi2008integrated`, `brodeur2024preregistration`, `chamberlin1890multiple`, `hirshleifer1983weakest`,
`malone1994interdisciplinary`, `mayner2018pyphi`, `oizumi2014phenomenology`, `stoer1997simple`,
`thompson1967organizations`, `tononi2004information`.
