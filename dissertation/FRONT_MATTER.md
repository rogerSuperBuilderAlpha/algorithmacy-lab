<!-- Front matter of the dissertation. Precedes Chapter 1. Page numbers are inserted at
typesetting (PDF/Word assembly); markdown carries no pagination. Items in [brackets] are for
the author/program to complete. -->

# The Transition to Algorithmacy
## A Construct and a Formal Model of Triadic Algorithmic Coordination

<br>

A dissertation submitted in partial fulfillment
of the requirements for the degree of
**Doctor of Philosophy in Business** *[confirm exact degree/program]*

<br>

by

**Roger Hunt III**

<br>

Bentley University
Waltham, Massachusetts

[Month] 2026

<br>

---

**Dissertation Committee**

[Name], Chair
[Name]
[Name]

<br><br>

---
---

# Abstract

Equivalently positioned workers passing through identical algorithmic systems receive divergent coordination outcomes, and the constructs the field has for studying work with algorithms do not explain the variance. This dissertation argues that the puzzle is the surface of a structural change: coordination has become triadic. A worker now coordinates with a counterpart she may never meet, a rider, a hiring manager, a customer, through a system that interprets both, acts on both, and commits determinations neither party controls. The existing constructs are built around a dyad, a person and a system, and cannot reach this triad; the competency it demands, which the dissertation names algorithmacy, was unnamed and unmeasured.

The dissertation develops the construct and builds a formal model of the condition that demands it, then grades that model across organizations, in three papers ordered from the conceptual to the formal. Paper 1, an integrative review, establishes that the triadic coordination form is real, that the dyadic constructs cannot be extended to it, and specifies algorithmacy to the discipline of construct clarity. Paper 2 adopts integrated information theory's measure of irreducibility, Φ, as a formal model: a coordination form is modeled as triadic exactly when its application-layer structure does not factor into independent parties under any partition (Φ over the minimum-information partition is positive), and as dyadic when some partition factors it — a condition that is computable, that the paper checks on controls whose answers are known, that it shows is strictly stronger than a cheap factorization test, and that it presents as a modeling choice — with the measure's standing critiques acknowledged — rather than as a claimed identity. Paper 3 asks how far the model can be made graded, and is exact about where the answer is "not far." It computes Φ across the complete family of three-node forms, across a population of simulated organizations, and across named real cases, and tests the model's central prediction in a controlled agent-based experiment. Two results are robust: the binary dyad/triad classification (which, over the whole form family, is strictly stronger than a cheap factorization test, not a heavy reimplementation of one), and the construct's central prediction tested behaviorally — independent agents coordinate far less successfully through a strict joint determination with no direct channel than through the same determination with a channel open, a large effect that survives training to three thousand rounds. The finer ordering of regimes by Φ magnitude is *not* robustly supported in the population: with standard errors and a full-rank design only the determination function moves Φ significantly, so the ordering rests on the behavioral experiment, not the population. Φ as a fine-grained scale fails outright, its magnitude dominated by the determination function. Paper 3 therefore presents Φ as a structural classifier and, at most, an ordinal indicator validated behaviorally at one contrast. That the model scores a human-mediated court at the same level as an algorithmic platform of the same structure shows it is indifferent to the mediator's seat — an equivalence built into the shared coding rather than discovered, and read as a property of the model, not an empirical finding about courts and platforms. The dissertation tests the model's core prediction as a behavioral consistency check; it does not claim a validated measure, and that fuller validation is the empirical program it opens.

Together the three papers turn "coordination is becoming triadic" from an observation into a formal apparatus: a construct, a formal model of the condition that demands it, and a model-internal landscape that grades it. A word on what the dissertation does and does not deliver, because the two are easy to run together. Its object is two coupled things — the *demand* a coordination form makes (a property of the form) and the *capacity* a worker brings to it (a property of the person) — and the dissertation builds and tests the demand side while *naming and specifying, but not measuring,* the capacity side. Algorithmacy, the competency, is specified to the discipline of construct clarity in Paper 1; the instrument that would measure a given worker's algorithmacy is named as the program's next arc, not delivered here. What is delivered is a formal model of the triadic demand that competency answers to. The empirical validation of that model against observed coordination outcomes, and the matched, person-level instrument, are the program this work opens.

*Keywords:* algorithmacy; triadic coordination; algorithmic management; platform work; integrated information; construct development; formal modeling.

<br><br>

---
---

# Acknowledgments

*[To be written by the author.]*

<br><br>

---
---

# Table of Contents

| | Chapter / Section | |
|---|---|---|
| | **Abstract** | |
| | **Acknowledgments** | |
| | **List of Tables** | |
| | | |
| **1** | **The Transition to Algorithmacy** (Introduction) | |
| 1.1 | A puzzle on the platforms | |
| 1.2 | The structural change beneath the puzzle | |
| 1.3 | The measurement problem and a found tool | |
| 1.4 | Three papers, one argument | |
| 1.5 | The combined contribution | |
| 1.6 | Plan of the dissertation | |
| | | |
| **2** | **Algorithmacy: A Communication Competency for Triadic Algorithmic Coordination** (Paper 1) | |
| 2.1 | Introduction | |
| 2.2 | Method of the review | |
| 2.3 | The triadic form and its three conditions | |
| 2.4 | The existing construct landscape | |
| 2.5 | The historical and theoretical adjacents | |
| 2.6 | Algorithmacy as a construct | |
| 2.7 | Future research agenda | |
| 2.8 | Conclusion | |
| | | |
| **3** | **Is It a Triad? Integrated Information as a Formal Model of Non-Dyadic Algorithmic Coordination** (Paper 2) | |
| 3.1 | Introduction: the form question | |
| 3.2 | The borrowing | |
| 3.3 | The application layer | |
| 3.4 | The state alphabet | |
| 3.5 | The model and its controls | |
| 3.6 | The model at work | |
| 3.7 | What the instrument establishes, and what it does not | |
| | | |
| **4** | **Toward a Readability Score for Coordination: Modeling Triadic Demand Across a Population of Organizations, and Testing the Structural Axis** (Paper 3) | |
| 4.1 | Introduction | |
| 4.2 | The coordination form as unit | |
| 4.3 | Model and methods | |
| 4.4 | Results | |
| 4.5 | Discussion | |
| 4.6 | Limitations | |
| 4.7 | Conclusion | |
| 4.8 | Data and code availability | |
| | | |
| **5** | **The Combined Contribution and the Program It Opens** (Conclusion) | |
| 5.1 | What the three papers, together, establish | |
| 5.2 | The puzzle revisited | |
| 5.3 | Significance | |
| 5.4 | The program the dissertation opens | |
| 5.5 | The bounds of the work | |
| 5.6 | The transition | |
| | | |
| | **References** *(per chapter; see Back Matter)* | |
| | **Appendices** *(computational artifacts; see Back Matter)* | |

*(Page numbers are added at typesetting. Section numbers within Chapters 2–5 are renumbered here to the
chapter (e.g., Paper 1's "§1 Introduction" becomes §2.1) so the dissertation reads as one document; each
paper's internal numbering is preserved in its own chapter file.)*

<br><br>

---
---

# List of Tables

| Table | Title | Chapter |
|---|---|---|
| 2.1 | Synthesis of the foreclosed constructs (structural commitment × where each stops short) | 2 (Paper 1) |
| 3.1 | Model controls and worked Φ values (factoring, irreducible, the worked cases) | 3 (Paper 2) |
| 4.1 | The Φ landscape of the W–S–C model family | 4 (Paper 3) |
| 4.2 | The typology on the triadic-demand bands | 4 (Paper 3) |
| 4.3 | Coordination success by condition (the structure-axis test) | 4 (Paper 3) |

*Tables are numbered by chapter. Tables 4.1–4.2 are formally numbered in Paper 3; the Chapter 2 synthesis
table and the Chapter 3 controls/worked-values table appear in those chapters and should be given the
numbers above when the chapters are assembled into the single document.*

**List of Figures**

| Figure | Title | Chapter |
|---|---|---|
| 4.1 | The Φ landscape of the W–S–C model family (Φ over all 4,096 three-node wirings) | 4 (Paper 3) |
| 4.2 | Coordination success by determination structure (the structure-axis test) | 4 (Paper 3) |

*The dissertation reports most results in tables; the two figures are the Paper 3 model-family landscape and the structure-axis test.*
