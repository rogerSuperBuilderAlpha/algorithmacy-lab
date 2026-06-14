# Field protocol — reading a real coordination arrangement with exact Φ

This is a procedure for taking one real coordination arrangement — a dispatch, a handoff, a review
gate — and producing the dyadic/triadic verdict on a model of it. It adapts the lab's research
protocol from invented forms to real ones. It is version 0: a discipline for honest modeling, not a
validated field instrument. Running it on real organizations is what will find its limits.

## What this produces, and what it does not

The verdict is about the model, not the organization. The model is a small Boolean dynamical system
whose nodes are the parties and whose rules encode what each party reads and commits. Exact Φ over
that model is exact. The claim that the model stands for the real arrangement is separate, and the
computation cannot supply it. A passed control establishes that the model has the structure claimed
(internal validity). That the model represents the real job is an empirical claim that needs field
evidence (external validity). The protocol's whole job is to keep these two apart and to make the
model falsifiable.

So the deliverable of a field study is not "this firm demands algorithmacy." It is: "under this
explicitly stated encoding, with this evidence behind each rule, the arrangement is triadic, and
here are the re-encodings that would flip it." The contribution is a disciplined, falsifiable model
and the verdict it carries.

## The steps

### 1. Bound one arrangement
Pick a single recurring act of coordination, not the whole organization. A driver and a rider
matched by a platform. An outgoing and an incoming nurse joined by a record. An author and a
maintainer gated by a review system. Write the boundary down: who is in, who is out, what one act
repeats.

### 2. Name the parties as nodes
Each party that holds a state and updates it. Keep the count small — exact Φ is feasible to about
ten to twelve elements, and a coordination unit is usually three to five: a worker, a system or
platform that mediates, a counterpart, and at most a few more. A party that only watches is a
candidate spectator (step 7); a party that is one of many interchangeable copies is a candidate for
substitution (step 8).

### 3. Define each node's bit
State what active versus inactive means for each node: complies/withholds, available/unavailable,
approves/blocks. This is an abstraction, and it discards detail. Record what each bit collapses and
what a finer encoding would carry. The verdict is relative to this choice.

### 4. Elicit the determination rules from evidence
For each node, write its next state as a fixed Boolean function of the others' current states. This
is the load-bearing step. Each rule is a claim about the real arrangement and needs evidence:
interviews, process documents, system logs, observation of the act. For each rule, record the
evidence behind it and at least one alternative that the evidence does not rule out. The system's
rule encodes what the platform reads and commits — whether it merely passes a message, or commits a
determination neither party sets alone. That distinction is usually where the verdict turns.

### 5. Pre-register the verdict and the reason
Before computing, write the expected verdict and why, from the structure of the rules. Commit it.
The discipline that makes the lab's record credible is that the prediction is fixed before the
number. Carry it into the field unchanged.

### 6. Validate the instrument
Run the two canonical controls (a decoupled form must read dyadic, a fully coupled form must read
triadic) before trusting any verdict. The protocol's runner does this first and refuses to proceed
if either fails.

### 7. Compute and read the verdict
Compute whole-system Φ over the MIP and the major complex. Dyadic (Φ_MIP = 0) means the arrangement
factors along party lines and demands literacy; triadic (Φ_MIP > 0) means it does not and demands
algorithmacy. Read membership on the major complex: a party in the irreducible core does real
coordinating work; a spectator (wired in but idle) drops out and must not be read off whole-system
Φ alone.

### 8. Sensitivity — re-encode the load-bearing rules
Take the one or two rules the verdict most depends on and re-encode them in a second defensible way
the evidence also permits. Recompute. If the verdict holds, it is robust to that modeling choice. If
it flips, the verdict is a property of the encoding, not the arrangement, and the study reports the
flip as its main finding. Three forces are known to flip a verdict and are worth testing directly:
**substitutability** (a party one of several interchangeable copies can supply becomes non-pivotal
and the form factors), **pass-through** (a system that only relays rather than commits is a pipe,
and the arrangement is dyadic), and **spectators** (an idle party sinks whole-system Φ while the
core stays intact — read the complex).

### 9. State the claim and what would falsify it
Report the verdict, the encoding in full, the evidence per rule, and the sensitivity result.
State plainly what re-encoding or what field observation would overturn it. The honesty of the
result is the clarity of the model behind it.

## What the verdict can and cannot say

It can say: under this model, the arrangement is or is not irreducible across party lines, and these
parties form the core. It is exact for the model and reproducible.

It cannot grade difficulty — the verdict is binary, and the magnitude of Φ is dominated by the
encoding, so it is read at most ordinally. It does not measure any worker. It is model-relative and
size-bounded. It is in-silico evidence about a model, and the validation gap to the real
organization is not closed by computing harder.

## The evidence a real study needs

The rules in step 4 are only as good as their evidence. A field study should ground each rule in at
least one of: a documented process or policy, a system log or audit trail, or convergent accounts
from the parties themselves. Where the parties disagree about what determines an action, that
disagreement is data — model both readings and report the verdict under each. Stipulated rules, with
no field evidence, produce a demonstration, not a finding. The mock studies in this directory are
exactly that: stipulated, for showing the mechanics.

## Limitations, and the path to a field-tested protocol

This protocol has not been run on a real organization. Several limits are visible already, and real
work will find more. Binary node states are coarse, and many coordination acts are graded. The rule
elicitation in step 4 has no standard method yet — no interview guide, no inter-rater reliability
for "what determines this action," no procedure for reconciling conflicting accounts. The boundary
in step 1 is a judgment call, and a different boundary can change the parties. The sensitivity step
samples re-encodings rather than searching them. Each of these is a place where a real study will
push back, and each push-back is how the field-tested version gets built. Treat the mocks as a
starting template, expect them to break in contact with a real case, and report what breaks.
