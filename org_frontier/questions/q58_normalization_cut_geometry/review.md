# Q58 — normalization cut geometry · Stage 1 review

**Question.** Why does isolating the back-channel recipient as the outer singleton yield normalized_phi
exactly half that of the non-recipient singleton on aligned one-sided ceiling pairs, and which IIT-4.0
partition repertoire or cut-size asymmetry produces the fixed 2.0 ratio with zero spread across all
sixteen forms?

**Agenda id.** Grows from Q57 probe #187 (H3) and the mechanistic thread left open after Q57 documented
the two-to-one normalized_phi ratio without inspecting PyPhi's normalization denominator.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #187 (Q57 H3) | Excluded/tied normalized_phi ratio exactly 2.0 on 16/16 pairs; spread 0. | Documents the ratio; does not identify the cut-size or normalization-factor mechanism. |
| #186 (Q57 H2) | Tied norm 0.5, excluded norm 1.0 on dual at-system-Phi outer cuts. | Supplies the absolute normalized_phi values to decompose into phi and normalization factor. |
| #188 (Q57 H4) | Complete min norm equals tied outer cut (0.5) on 16/16. | Suggests complete shares recipient cut geometry; cut-matrix comparison untested. |
| #185 (Q57 H1) | Back-channel recipient determines tied singleton seam. | Names which cut is tied vs excluded; mechanistic link to severed-edge count unverified. |
| #184 (Q56 H5) | Minimum normalized_phi predicts official tie set. | Tie-break rule depends on normalized_phi; denominator structure unexplained. |
| #173 (Q54 H4) | One-sided Phi=2.0 requires commit-topology alignment. | Defines the sixteen aligned one-sided ceiling pairs. |

## The gap

Q57 (#187) established that the non-recipient outer singleton carries normalized_phi exactly twice the
recipient singleton on every aligned one-sided ceiling pair, with zero spread. Both cuts reach system Phi.
No probe has inspected PyPhi's IIT-4.0 normalization term (`normalized_phi = phi × normalization_factor`,
with `normalization_factor = 1 / num_connections_cut` for `GeneralKCut`), compared the implied
denominator on min-norm at-system-Phi partitions, or tested whether the 2.0 ratio equals a
severed-connection-count ratio rather than unnormalized phi asymmetry. The aligned one-sided ceiling
enumeration and partition scan from Q56–Q57 are available; the normalization geometry is not.
