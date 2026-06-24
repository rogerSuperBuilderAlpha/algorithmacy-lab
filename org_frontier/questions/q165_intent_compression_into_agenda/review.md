# q165 — review of prior work

The question extends the lab's embodiment battery (battery_embodiment in
[`cognition/theory_batteries.py`](../../cognition/theory_batteries.py)). That battery established two
results q165 builds on: a co-monotone meaning degrades gracefully as read-fidelity q drops (the noisy()
sweep), and a nuance bit the system does not read is left outside the bound whole (the reads_n / blind_n
forms). Both were stated for a faithful mediator. q165 is the first to run them against an interested one.

It joins that line to Q126's interested mediator
([`q126_interested_mediator`](../q126_interested_mediator/)). Q126 showed that imposing an agenda over the
parties' joint determination drives whole-system Φ to zero and sheds the parties from the core at full
fidelity. q165 asks the embodiment-side question Q126 left open: how the agenda interacts with
read-fidelity compression, and whether it evicts the worker's nuance specifically. The shared forms live
in [`cognition/interested_mediator_forms.py`](../../cognition/interested_mediator_forms.py), the bridge
this empirical line extends.

What is new is the comparison of compression curves. Q126 read Φ at full fidelity; the embodiment battery
read the fidelity curve only for a faithful gate. q165 puts the two together and finds the interested
curve strictly below the faithful one at every q < 1, and a nuance bit evicted by the agenda alone. No
prior statement in the lab compares how a faithful and an interested mediator shed the worker's meaning
under the same compression.
