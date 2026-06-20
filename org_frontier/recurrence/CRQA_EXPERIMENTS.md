# Ten CRQA experiments

[`crqa_experiments.py`](crqa_experiments.py) probes the behavioral instrument itself, seeded by the
sweep's 40% edge recovery, 6% false-positive rate, and false-dyad exposure. Each experiment prints
one result; the numbers reproduce at the seeds in the script. The findings divide into recovery
(what the diagonal-profile lag can and cannot read off behavior) and reach (how the categorical
method extends).

## What the profile lag recovers

**C1 — recovery rises with noise, then falls.** Edge recovery climbs from 20% at flip rate 0.02 to
43% at 0.20, then drops to 36% at 0.30. A nearly frozen trajectory gives the profile little structure
to lock onto; a moderate flip rate keeps the parties moving through shared states; too much noise
drowns the signal. The false-positive rate holds near 6% throughout.

**C3 — length trades against false positives, not recovery.** Recovery stays near 40% from 150 to
2400 steps. The false-positive rate falls from 14% at 150 steps to 6% by 600 and holds. A longer run
buys cleaner negatives, not more recovered edges. The recovery ceiling is structural, set by the next
two experiments.

**C2 — common drivers are the confound.** Two parties driven by a shared third, with no edge between
them, couple anyway: recurrence rate 0.50, determinism 0.85, a prominent peak at lag zero. The shared
driver makes them recur together. The peak sits at lag zero, so this confound inflates the
synchronous coupling count rather than the directed-edge recovery, and it is why a behavioral reading
needs the structural one to tell a common cause from a direct tie.

**C6 — lag tracks path length.** In a relay chain W to S to C, the profile peaks at lag +1 for W-S,
+1 for S-C, and +2 for W-C. The lag counts the hops between two parties, so the profile reads not
only direction but distance along the coupling path.

**C7 — synchrony marks reciprocity.** Reciprocal pairs, joined by edges both ways, peak near lag zero
in 86% of prominent cases. One-way pairs peak near zero in 79%. A mutual coupling pulls the two
series into step, which is the behavioral face of the structural reciprocity the Φ experiments tie to
irreducibility.

**C5 — prominence separates coupling from chance.** Two independent sticky series score determinism
0.98 with profile prominence 0.02. A one-way relay scores determinism 0.89 with prominence 0.31.
Determinism rewards any two smooth series; the profile prominence is what marks a real lead-lag.

## What the method exposes and reaches

**C4 — the false dyad's hidden tie always dominates.** Across 40 runs of `gig_false_dyad`, the hidden
S-C coupling outlasts the presented W-S coupling every time. The behavioral instrument exposes the
concealed edge with no model, which is the empirical form of the false-dyad finding.

**C8 — the method extends to graded signals.** A continuous diagonal profile with a two-dimensional
phase-space embedding recovers a known delay: a follower lagging a graded random walk by four steps
gives a peak at lag +4, prominence 0.73, against an independent series at prominence 0.05. The
categorical case the Boolean models need is the small end of a method that carries to vitals and
movement.

**C9 — windowed CRQA catches a regime change.** A coordination wired to couple for 300 steps and then
decouple shows window prominence 0.18 before the switch and 0.11 after. Sliding the window turns CRQA
into a detector of when a coordination's structure changes, which a single whole-run measure misses.

**C10 — the NICU triad, causal coupling without a communicative lead.** The committing-triad bedside
model, with an infant that emits a state the apparatus reads, gives the cross-reference its
measurement. The infant-apparatus pair shows the strongest sustained coupling, longest diagonal 81,
determinism 0.87, and no directional lead, because the apparatus integrates several inputs at once.
The infant-parent pair couples less, longest diagonal 39. Only the parent-apparatus pair carries a
clean directional read, peak lag +1, prominence 0.17. The infant's coupling is real and sustained and
runs to the apparatus, while the directional, communicative structure lives between the parent and
the apparatus. That is the causal-versus-communicative gap of the neonatal study, measured on a run.

## What this establishes

The diagonal-profile lag reads directed coupling off behavior at about 40% of edges with few false
positives, recovers both direction and path length, and marks reciprocity by synchrony. Its ceiling
comes from common drivers and from coupling too fast or too frozen to track. The method reaches from
binary states to graded signals and from whole-run to windowed readings. Paired with the structural
side in [IIT_EXPERIMENTS.md](IIT_EXPERIMENTS.md), it covers what Φ cannot see on its own: the
direction of a tie, the concealment of a false dyad, and the moment a coordination's wiring changes.
