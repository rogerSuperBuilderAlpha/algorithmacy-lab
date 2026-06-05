# Q49 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on what the minimum-information partition (MIP) of a triadic strict-mediation
form names — a worker-specific structural seam, or a degenerate tie broken by a fixed convention — and
whether a verdict-preserving asymmetry makes the seam unique and places it at a connectivity min-cut.
Written and committed before any test runs. The seam of a form is read at its max-Φ reachable state from
the set of partitions tied for the MIP (PyPhi's `sia.ties`), classified by which single party each tied
two-part partition severs as a singleton: `{X | rest}`. Prior probes (#26, #33, #55, #16, #56, #24, #30,
#54, #94, #106) supply the structural priors each null rests on.

## H1 — The canonical worker seam is a tie, not a unique fault line
- **Claim:** For the canonical strict-mediation triad (S = W∧C, W and C each read S back), the MIP is
  degenerate. The `{W,SC}` partition that #26 reports ties at equal integrated information with its mirror
  `{WS,C}`, so the worker is not the unique severed singleton. The seam set is `{W, C}`, and `{S,WC}` is
  not in it.
- **H0:** `{W,SC}` is the unique MIP for the canonical triad; `{WS,C}` carries strictly higher integrated
  information, so the worker is the structurally unique weakest seam.
- **Predicted outcome:** PyPhi's tie set at the max-Φ state contains both `{W,SC}` and `{WS,C}` at the
  system Φ (2.0), and not `{S,WC}`. H0 is refuted; the worker-as-seam is one of two symmetric
  representatives of a tie.

## H2 — No triadic strict-mediation form has a worker-unique seam
- **Claim:** Across all 24 triadic forms of the n=3 strict-mediation family (the 256-form family of
  `corpus/population.py`), the seam set is symmetric under worker↔counterpart: every form whose tie set
  severs W as a singleton also severs C as a singleton. No form makes the worker a weakest seam without
  the counterpart being one too.
- **H0:** At least one triadic strict-mediation form severs W alone (W in the seam set, C not), giving a
  genuine worker-specific seam.
- **Predicted outcome:** In all 24 triadic forms, `{W,SC} ∈ ties ⇔ {WS,C} ∈ ties`; zero forms break the
  W/C seam symmetry. This follows from the W↔C automorphism (#55) and balanced influence in triadic forms
  (#16). H0 is refuted.

## H3 — A one-sided back-channel breaks the seam tie
- **Claim:** Adding a single verdict-preserving asymmetry — the worker reading the counterpart directly
  (W' = S∧C, the back-channel of #24) — keeps the form triadic and lifts the W/C seam tie, leaving a
  unique severed singleton among the tied two-part partitions.
- **H0:** The back-channel leaves the seam tie intact, so the singleton-severing seam set stays `{W, C}`
  (or the form collapses to dyadic, in which case the premise fails and the test is void).
- **Predicted outcome:** The form stays triadic at Φ ≥ 2.0; the singleton-severing partitions in the tie
  set reduce to one party. H0 (a persistent `{W, C}` seam tie) is refuted.

## H4 — The broken seam follows the read direction, not the parties' interest
- **Claim:** The party that gains an incoming read is more tightly bound, so it is not the weak seam; the
  unique seam falls on the other party. The worker reading the counterpart (W' = S∧C) puts the seam on the
  counterpart, the counterpart reading the worker (C' = S∧W) puts it on the worker, and a symmetric
  two-sided channel restores the `{W, C}` tie.
- **H0:** The broken seam falls on the party that gained the read (the more-coupled party is the weak
  seam), or the side of the channel does not determine the seam.
- **Predicted outcome:** Worker-side channel → seam `{C}`; counterpart-side channel → seam `{W}`;
  symmetric channel → seam `{W, C}`. The seam is the party without the extra incoming read on every
  asymmetric panel form. H0 is refuted.

## H5 — The seam is not the connectivity min-cut
- **Claim:** A connectivity min-cut cannot account for the seam. A back-channel edge between W and C is
  incident on both parties, so it leaves their total connectivity degree equal: the graph min-cut keeps W
  and C tied on every back-channel form, while the Φ-seam breaks to one party (H3, H4). And the parity
  (XOR/XNOR) triadic forms are pure higher-order (#56): their MIP is the complete partition `{W,S,C}` with
  no two-part singleton seam, while a graph min-cut still returns a singleton. The seam is not a function
  of the wiring graph.
- **H0:** The Φ-MIP seam equals the connectivity min-cut singleton set on every triadic form — a clean
  graph min-cut law for the seam.
- **Predicted outcome:** On the asymmetric panel the graph min-cut returns `{W, C}` (equal degree) while
  the Φ-seam is a single party, a disagreement on every broken form. On the 8 parity forms the
  singleton-severing seam set is empty (complete-partition MIP) while the graph min-cut returns a
  singleton. H0 is refuted; the min-cut account fails in two distinct ways, mirroring connectivity's
  failure to define the verdict (#54, #94, #106).
