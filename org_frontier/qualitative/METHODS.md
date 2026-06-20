# Qualitative methods for reading coordination

The field protocol names its own open gaps: the rule elicitation in step 4 has no standard interview guide,
no inter-rater reliability for "what determines this action," and no procedure for reconciling conflicting
accounts. This document is a first pass at the methods that fill them. Each method states what it produces,
which step of the [field protocol](../field/PROTOCOL.md) it serves, and the standard it is held to. The
through-line is one question: does the mediating system commit a determination neither party sets alone, or
does it convey a signal between parties who decide on their own? That distinction is where the verdict turns,
and it is a question about practice that qualitative work is built to answer.

## 1. Determination-rule elicitation interviews

Serves field step 4. The aim is to recover each party's update rule: under what conditions does this party
act, and on whose state does that depend. The interview works backward from concrete recent instances —
"walk me through the last time you declined" — to the conditions that governed the action, then asks the
party to confirm or correct a stated rule. A driver's rule is a function of what the app showed; the app's
rule is a function of what the driver and the rider did. The product is a Boolean function per party with the
evidence behind it recorded, and, as the protocol requires, at least one alternative the evidence does not
rule out. The standard: a rule a second researcher could derive from the same transcript and reach the same
function.

## 2. Observation of the bounded coordination act

Serves field steps 1 through 3. Watching the act fixes the boundary, names the parties who actually hold and
update a state, and calibrates the bit. Observation catches what interviews miss — the party who is wired in
but idle (a spectator), the step that looks like a decision but only relays, the back-channel the parties use
around the system. The product is the boundary, the party list, and a defended encoding of active versus
inactive for each node, with a note on what the bit collapses. The standard: another observer of the same
act would draw the same boundary and name the same parties.

## 3. Document and log analysis

Serves field step 4. Policies, terms of service, dispatch logs, and audit trails are evidence for the rules,
often the only evidence for the system's rule, which the parties cannot see. A scheduling policy states the
threshold at which shifts are assigned; a moderation guideline states what the system enforces and what it
escalates; a log shows which inputs preceded which commitment. The product is rule evidence drawn from the
record, cross-checked against the parties' accounts. The standard: each documented rule cites the artifact
and the passage, and conflicts between the document and the accounts are reported, not resolved silently.

## 4. Disagreement as data

Serves field steps 4, 8, and 9. When the parties describe the same arrangement differently — the worker says
the system decides, the platform says it only suggests — the disagreement is itself a finding about whose
account of the coordination governs. The method models both readings, computes or reasons through the verdict
under each, and reports the spread. A verdict that holds across the readings is robust to the disagreement; a
verdict that flips is a property of whose model you adopt, and that is the result. The product is two rule
sets and the verdict under each. The standard: both readings are defensible from the evidence, and the study
states what observation would settle which one holds.

## 5. Bit calibration and inter-rater reliability

Serves field step 3. A binary node discards detail, and the verdict is relative to where the line is drawn,
so the line needs defending. The method adapts the calibration discipline of qualitative comparative analysis
(Rihoux & Ragin 2009): state the threshold for active versus inactive, apply it to coded instances, and have
a second rater code independently. Agreement is reported as Krippendorff's α, with α ≥ 0.80 the working bar.
Member checking — showing the parties the encoding and recording whether they accept it — is the second
check. The product is a calibrated bit per node with a reliability figure. The standard: the threshold is
fixed before coding and the raters do not confer until both have coded.

## 6. Thick description of a coordination setting

Serves the stand-alone mode. A study can document a coordination kind richly without computing a verdict: how
the parties experience the arrangement, what they take the system to be doing, where authority over the
outcome is felt to sit. This is a record for the catalog, a candidate for later modeling, and evidence in its
own right about a coordination form. The product is a written account grounded in observation and interview.
The standard: the description is concrete enough that a later study could attempt the field protocol on it,
and it marks the points where the parties' accounts diverge.

## 7. Fieldwork falsification

Serves field steps 8 and 9 from the field side. A pre-registered verdict makes a claim that observation can
overturn: that the worker is pivotal rather than substitutable, that the system commits rather than relays,
that a party is in the core rather than watching. The method states, before the fieldwork, what would
falsify each, then looks for it — a second worker who is in fact interchangeable, a documented case where the
system passed the determination through unchanged, a party who turns out idle. The product is the falsifier
sought and what was found. The standard: the falsification conditions are written before the field visit and
reported whether or not they were met.

## 8. Worker folk-theory elicitation

Serves the stand-alone mode and feeds step 4. Algorithmacy is a lived competence with three parts: a worker
reconstructs a hidden counterpart's wants from outcomes, compresses real intent into the few signals the
system accepts, and tracks rule changes the system makes without announcement. How workers themselves model
the algorithmic third party is data about that competence, and it is often the best evidence for the system's
rule, since the worker has theorized it from the outside. The method elicits the worker's account of what the
system is doing and why, treating it as a hypothesis about the system's rule to be checked against documents
and logs. The product is the worker's model, recorded and compared to the documented one. The standard: the
worker's theory is reported as theirs, with its divergences from the record marked.

## Pre-registration

Every method is held to the lab's pre-commitment discipline. The interview guide, the coding scheme, the
calibration thresholds, and the falsification conditions are committed to git before the fieldwork, so the
history shows the questions were fixed before the answers. This is the qualitative form of committing
hypotheses before computing, and it is what lets a reader trust that the study found what it set out to test
rather than what it hoped to see.
