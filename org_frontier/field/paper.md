# Reading a real coordination arrangement with exact Φ: a field protocol and ten worked models

<code + data: org_frontier/field/ ; reproduce the demonstration with `python -m org_frontier.field.run`>

## Abstract

This is a methods paper. It proposes a protocol for taking one real organizational coordination
arrangement to an explicit, falsifiable Boolean dynamical model and an exact IIT-4.0 Φ verdict —
dyadic, the arrangement factors along party lines, or triadic, it does not — and demonstrates it on ten
mock organizations. The protocol belongs to the computational-organization-theory tradition of formal
modeling (NK-landscape and agent-based studies of interdependence), adopts that tradition's
theory-building validation language (internal validity established by the model; external validity a
separate empirical claim; equifinality, so one working model does not validate the theory), and
specifies its rule-elicitation step with established methods — causal cognitive mapping, QCA-style bit
calibration, and a reported inter-rater reliability coefficient — that the protocol previously left
open. Φ is used strictly as a measure of structural irreducibility, with no consciousness claim. The
ten mocks demonstrate the four modeling judgments the protocol forces and the validation gap it keeps
visible.

## Introduction

Organization theory has a long tradition of representing coordination formally — Thompson's
interdependence typology, coordination theory's "managing dependencies between activities," and the
computational lineage of NK-landscape and agent-based models (Rivkin & Siggelkow 2002, 2003). This
paper adds a procedure to that tradition: a way to model one real coordination arrangement as a small
Boolean dynamical system and compute, exactly, whether its cause-effect structure is irreducible across
the parties. The verdict is exact for the model; the contribution is the protocol that produces a
falsifiable model and states precisely what the verdict does and does not claim.

## The protocol

`PROTOCOL.md` gives the nine steps: bound one arrangement; model the parties as nodes; define each
node's bit; elicit the determination rules from evidence; pre-register the verdict; validate the
instrument; compute the verdict and major complex; run a mandatory sensitivity step; state the claim and
what would falsify it. Three commitments distinguish it.

**It belongs to the computational-organization-theory tradition, and inherits its norms.** Importing a
formal apparatus from another field — here Boolean dynamics and Φ from neuroscience — is established
practice, with the standing requirement that the tool be adapted with care to the organizational context
rather than applied naively (Rivkin & Siggelkow 2002). The instrument is validated on controls before
any verdict, and the verdict is read on the major complex, not whole-system Φ, for forms with spectators.

**Its validation-gap language is the field's.** Simulation is a theory-building method whose strength is
internal validity (Davis, Eisenhardt & Bingham 2007). Operationalizing a verbal account forces
"specificity gaps" filled with defensible assumptions, and equifinality means many models fit the same
account, so one model "working" does not validate it. The protocol's mandatory sensitivity step is the
direct response: it re-encodes the load-bearing rules to show whether the verdict is a property of the
arrangement or of the encoding. The validation gap — internal validity established, external validity a
separate empirical claim — is stated in the field's own terms.

**It specifies the rule-elicitation step.** The protocol's named weakness was that Stage-4 rule
elicitation had no standard method. The paper closes it: elicit the determination rules by causal
cognitive mapping (Axelrod tradition; Hodgkinson, Maule & Bown 2004), calibrate each node's bit with
QCA-style anchors (Rihoux & Ragin 2009), and report an inter-rater reliability coefficient (Krippendorff's
α ≥ 0.80; Krippendorff 2004) for the coded rules. Coordination theory's "managing dependencies between
activities" (Malone & Crowston 1994) and Thompson's typology are the target constructs the model
represents.

## Φ is a structural measure, not a consciousness claim

IIT as a theory of consciousness is contested — a September 2023 open letter (Fleming et al.) argued it
should be labelled pseudoscience, and objections note that high-Φ arrays of XOR gates have no plausible
consciousness and that Φ is not determinable from input–output behaviour. None of this bears on the use
here. The protocol uses Φ as an exact, well-defined measure of the structural irreducibility of a small
discrete dynamical system — a computable property of its cause-effect structure — and makes no claim
about consciousness. The dyadic/triadic verdict is a statement about whether a coordination model factors
along party lines, nothing more.

## Demonstration: ten mock organizations

The ten mocks (`mocks.py`, `FINDINGS.md`) are stipulated, not elicited, and measure no real
organization; they demonstrate the protocol's mechanics and the four judgments it forces. Six read
triadic, four dyadic; nine matched the pre-registered reading. The demonstration shows that a system in
the middle is not enough (a relay, a transparent pipe, and a substitutable marketplace read dyadic);
that the verdict turns on the encoding (four arrangements flip under a defensible re-encoding); that one
must compute rather than assert (a routing cycle reads triadic against the naive reading); and that a
triadic verdict still needs the major complex to name who binds.

## Limitations

The protocol has not been run on a real organization, and the mocks are stipulated. Rule elicitation,
even with the methods specified here, is a coding task whose reproducibility must be demonstrated, not
assumed. Binary node states are coarse. Equifinality means a passed verdict establishes internal
validity only. Exact Φ is feasible to roughly ten to twelve elements, which bounds the arrangements that
can be read. The next step is a real case, where the protocol will be revised by what it cannot capture.

## References

Davis J. P., Eisenhardt K. M. & Bingham C. B. (2007). Developing theory through simulation methods.
*Acad. Manag. Rev.* 32(2): 480–499.
Rivkin J. W. & Siggelkow N. (2003). Balancing search and stability. *Manag. Sci.* 49(3): 290–311.
Rivkin J. W. & Siggelkow N. (2002). Organizational sticking points on NK landscapes. *Complexity* 7(5):
31–43.
Malone T. W. & Crowston K. (1994). The interdisciplinary study of coordination. *ACM Comput. Surv.*
26(1): 87–119.
Thompson J. D. (1967). *Organizations in Action*. McGraw-Hill.
Rihoux B. & Ragin C. C. (2009). *Configurational Comparative Methods*. SAGE.
Hodgkinson G. P., Maule A. J. & Bown N. J. (2004). Causal cognitive mapping. *Organ. Res. Methods* 7(1):
3–26.
Krippendorff K. (2004). *Content Analysis*. SAGE.
Fleming S. M. et al. (2023). The IIT of consciousness as pseudoscience. PsyArXiv.
