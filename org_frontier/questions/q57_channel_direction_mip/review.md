# Q57 — channel direction MIP seam · Stage 1 review

**Question.** Why does the one-sided channel direction fix which outer party — W under worker wiring, C
under counterpart wiring — achieves minimum normalized_phi and co-enters the official MIP tie set with the
complete partition, when both outer-party two-part cuts reach system Phi on every aligned ceiling pair?

**Agenda id.** Grows from Q56 probes #181 and #184. No dedicated agenda slot; the open thread is the
directional mechanism behind the one-sided min-norm tie-break that Q56 documented.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #181 (Q56 H2) | Sixteen one-sided ceiling pairs tie exactly one outer-party cut plus complete. | Documents worker→{W,SC}, counterpart→{WS,C}; mechanism untested. |
| #184 (Q56 H5) | Minimum normalized_phi predicts official tie set on 32/32 ceiling pairs. | Names the tie-break rule; does not explain why direction picks the favored singleton. |
| #182 (Q56 H3) | One-sided ceiling pairs break directional W/C symmetry; symmetric pairs restore it. | Directional asymmetry correlates with the split; causal link unverified. |
| #183 (Q56 H4) | Symmetric pairs have both outer cuts at system Phi but higher normalized_phi than complete. | Shows norm split excludes outer cuts on symmetric pairs; one-sided favored cut shares complete minimum. |
| #173 (Q54 H4) | One-sided Phi=2.0 requires commit-topology alignment. | Defines the sixteen aligned one-sided ceiling pairs in the test ensemble. |
| #178 (Q55 H4) | Below-ceiling pairs at MIP {S,WC}; ceiling uses outer-party or complete cuts. | Supplies the ceiling panel and partition vocabulary. |

## The gap

Q56 (#181, #184) established that aligned one-sided bijective parity ceiling pairs tie one outer-party
singleton seam with the complete partition, and that the official tie set follows minimum normalized_phi.
Worker wiring consistently favors {W,SC}; counterpart wiring favors {WS,C}. Both outer-party cuts reach
system Phi on every pair. No probe has tested whether the back-channel recipient party (the outer party
whose update rule gains the extra incoming cross-edge) determines the favored singleton, whether the
excluded cut carries exactly twice the normalized_phi of the tied cut, or whether XOR and XNOR gate
polarity preserve the same direction rule. The aligned one-sided ceiling enumeration and partition scan
from Q56 are available; the directional mechanism is not.
