# q167 — review of prior work

The question extends the lab's extended-mind battery (battery_extended_mind in
[`cognition/theory_batteries.py`](../../cognition/theory_batteries.py)). That battery established the
result q167 builds on: a four-node core in which a platform input supplants the worker's input as a
capture share g rises, with the worker leaving the major complex at a low threshold (the X1 sweep loses W
by g = 0.1, faithful platform branch P ∧ C). The battery stated this for a faithful platform. q167 is the
first to run it against an interested one.

It joins that line to Q126's interested mediator
([`q126_interested_mediator`](../q126_interested_mediator/)). Q126 showed that imposing an agenda over the
parties' joint determination erodes whole-system Φ and sheds the parties from the core. q167 puts the
agenda inside the platform branch of the capture model and asks the extended-mind question Q126 left open:
whether an interested platform takes the worker's seat at a lower capture share than a faithful one, and
whether the displaced worker is replaced by the agenda specifically. The shared forms live in
[`cognition/interested_mediator_forms.py`](../../cognition/interested_mediator_forms.py), the bridge this
empirical line extends; q167 adds the four-node core4_tpm / core4_complex forms there.

What is new is the capture-threshold-by-interest sweep. The battery read the threshold for a faithful
platform; Q126 read agenda effects in a three-node triad at full determination. q167 crosses the two and
finds the threshold non-monotone in interest: the agenda lowers it only where the platform branch stays
informative about (P, C), raises it where the agenda goes constant, and replaces the worker with the
counterpart rather than the agenda node. No prior statement in the lab relates the extended-mind capture
threshold to the platform's interest.
