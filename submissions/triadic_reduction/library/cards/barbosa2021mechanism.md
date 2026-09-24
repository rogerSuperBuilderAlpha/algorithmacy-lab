---
citekey: barbosa2021mechanism
title: "Mechanism Integrated Information"
authors: "Barbosa, Leonardo S.; Marshall, William; Albantakis, Larissa; Tononi, Giulio"
year: 2021
venue: "Entropy 23(3): 362 (published 18 Mar 2021)"
doi: "10.3390/e23030362"
section: "S5"
status: candidate
verified: verified
source_basis: "Full text read from the PubMed Central open-access JATS XML (PMC8003304, CC BY; the publisher's own deposit), converted to text; DOI, volume, issue, article number and authors confirmed in Crossref. MDPI's PDF route returned an HTML page to curl, so the typeset PDF was not read and the loci below are by section and equation, not by page."
access_url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC8003304/"
retrieved: 2026-09-24
sha256: "32bb37790562e06ad018f6d45d10c396036ab0d0d11d2a819bc8439690bdb5e9"
---

## What the talk may use it for
This paper takes the intrinsic difference (ID) of barbosa2020measure and builds mechanism-level integrated information φ from it. IIT 4.0 later adopts that machinery, so for S5 this is the source for how φ of a two-input mechanism is computed. Three pieces matter. First, φ of a mechanism M in state m over a purview Z is the ID between the intact repertoire and the repertoire under the minimum-information partition, evaluated at the single purview state that maximizes selectivity × informativeness. Second, the paper replaces bipartitions with "disintegrating partitions" (Eq 4), which must cut the mechanism into at least two parts or cut the whole mechanism away from the whole purview. Third, mechanism φ is min(φ_cause, φ_effect) (Eq 3).

The worked examples in §4.2 are second-order, which is to say two-input, mechanisms. M = {A, E} over Z = {A, E} scores 0.36 against the complete partition but 0 against the partition that pairs A with A and E with E, so it is reducible and "does not exist within the system over this purview". M = {A, B} over Z = {A, B} survives: its MIP cuts B away from the purview, and φ_e = 0.36. A third-order example shows that a partition with an empty mechanism part can reduce a mechanism whose inputs to one unit cancel each other. For the talk's XOR example, the lesson is that a two-input mechanism's φ depends on the partition set as well as the gate, and that a pair of inputs can be reducible.

## Loci
Loci are sections and equations of the PMC full text.
- Abstract — "Here we show that the new measure also satisfies the remaining postulates of IIT—integration and exclusion—and create the framework that identifies maximally irreducible mechanisms."
- §2 — "Mechanism integrated information (φ) is an analogous measure that quantifies the existence of a mechanism within a system. Only mechanisms that exist within a system (φ>0) contribute to its cause–effect structure."
- §3.1.3 — the difference between repertoires "is evaluated as the maximum of the absolute value of some function f that is assessed for particular states." Eq 8 carries the absolute-value bars in the XML markup.
- §3.1.4 — "If φe(m,Z)=0, there is a partition of the candidate mechanism that does not make a difference, which means that the candidate mechanism is reducible."
- §3.1.5, Eq 3 — φ(m) = min{φc(m), φe(m)}.
- §3.2, Eq 4 — the set Ψ(M, Z) of disintegrating partitions; "the mechanism set must be divided into at least two parts, except for the special case where one part contains the whole mechanism but no units in the purview (complete partition, ψ0)."
- §3.3, Theorem 1 — f(p, q) = k p log(p/q), and the integrated information of a mechanism over a purview is max over z of π(z|m) log[π(z|m)/π^ψ*(z|m)].
- §4.2 — "we find that the candidate mechanism is not integrated" (M = {A, E}, partition ψ1, ID = 0); "the candidate mechanism M={A,B} has integrated effect information" (φe = 0.36 under MIP ψ2, against 0.51 for the complete partition).
- §4.2 — "This occurs since B and D have opposite effects over the purview unit E, and by cutting both inputs to E we avoid changing the repertoire." — the third-order mechanism {A, B, D} is reducible.
- §5 — "Previous formulations of mechanism integrated information restricted the set of all possible partitions to bipartitions of a mechanism and its purview but allowed for partitions that do not qualify as “disintegrating” the mechanism (for example, cutting away a single purview unit) [3]."

## What the preliminary sources claim about it
- No register row cites this paper. Two rows describe machinery that originates here and that the albantakis2023information card already corrects against IIT 4.0:
  - iit4-mechanism-partitions (TR-S5-096): "IIT 4.0 MIP evaluation tests all bipartitions of the candidate mechanism" → the correction stands. Barbosa et al. introduced the disintegrating partitions (Eq 4) and say that the earlier formulation used bipartitions (§5).
  - iit-mechanism-phi-definition (TR-S5-019): "Mechanism-level phi = D(p || p^MIP)" → the correction stands. Here φ is the ID at the maximizing purview state, not a divergence between whole repertoires (§3.3).
- xor-mechanism-id-value (TR-S5-099): this paper's f is p log(p/q) with an absolute value around it and no |p − q| factor, which agrees with the refutation on the barbosa2020measure and albantakis2023information cards.

## Notes
- The φ values in §4 appear to be in nats. A fully constrained binary unit gives 0.69 (§4.1), which is ln 2, i.e. p = 1 against q = 1/2 under a natural log (my arithmetic). IIT 4.0 reports ibits (log base 2), so these numbers are not directly comparable with the lab's PyPhi outputs.
- The example units are logistic threshold units with bias h and indeterminism τ (Eq 9), not logic gates, and the connectivity of the Figure 4a system is shown only in the figure, which was not read. The card therefore reports the §4.2 values and not the wiring behind them.
- IIT 4.0 (albantakis2023information) cites this paper as [12], per the barbosa2020measure card.
- The paper says that system-level Φ "will be discussed elsewhere" (§3). It defines only mechanism φ.
