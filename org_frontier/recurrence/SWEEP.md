# The corpus-wide sweep: where structure and behavior agree, and where they part

[`sweep.py`](sweep.py) reads every curated form through both instruments. Φ comes from the form's
transition matrix: the structure verdict, the maximum integrated information, and the major-complex
membership. CRQA comes from a stochastic trajectory of the same form: the recurrence rate,
determinism, longest diagonal, and the diagonal-profile peak lag for each pair of parties. A random
ensemble adds the statistics the eight named forms cannot give alone. Numbers reproduce at the seeds
in the script.

## The named forms

Φ confirms the documented verdict on all eight forms: the four dyadic forms carry zero whole-system
integrated information, the four triadic forms carry positive Φ. The behavioral reading agrees with
the structure on most forms and parts from it on three, and the three departures are where the
experiments begin.

**The false dyad hides its tight coupling.** `gig_false_dyad` presents as a worker-system pair with
an unseen counterpart the dispatch reads. CRQA exposes the concealment. The presented W-S tie is
weak: recurrence rate 0.32, longest diagonal 12. The hidden S-C tie dominates: recurrence rate 0.74,
determinism 0.96, longest diagonal 72. The strongest coordination in the form runs along the edge
its surface presentation hides, and Φ places the major complex on the presented W-S pair while the
behavior couples S-C. Structure and behavior locate the tight pair on different edges.

**The relay couples strongly and integrates nothing.** `pure_relay` is a feedforward chain. Every
pair shows sustained cross-recurrence, determinism above 0.85, long diagonals. Φ is zero and the
major complex is a single node. A chain that passes a signal cleanly down its length is strongly
coupled in behavior and reducible in structure.

**The back-channel agrees.** `hierarchy_backchannel` has a direct worker-counterpart edge. CRQA makes
W-C the tightest pair, longest diagonal 50, and the major complex is the W-C pair. Here the
behavioral tight pair and the structural core coincide.

## The random ensemble

Three hundred random three-node forms give the rates the named set cannot.

- **Irreducibility is rare.** Φ calls 5% of random forms triadic, matching the triadic rates the
  earlier probes found.
- **The profile lag recovers wiring partially.** The diagonal-profile peak reads off the correct
  direction for 40% of directed read edges, with a 6% false-positive rate on absent edges. Direction
  is recoverable from behavior, and the ceiling below 100% is the subject of the CRQA experiments:
  cycles, common drivers, and fast coupling confound the lag.
- **Reciprocity reads as synchrony.** 80% of the Φ-irreducible forms also show a synchronous,
  prominent diagonal peak. A mutual coupling that integrates also tends to recur at lag zero, which
  ties the structural signature of irreducibility to the behavioral signature of synchrony.

## What the sweep seeds

The three departures define two batteries. The structural questions become the ten Φ experiments in
[IIT_EXPERIMENTS.md](IIT_EXPERIMENTS.md): how a false dyad differs from a true one, why a chain
integrates nothing, whether reciprocity is what drives irreducibility, where the third party sits in
the core. The behavioral questions become the ten CRQA experiments in
[CRQA_EXPERIMENTS.md](CRQA_EXPERIMENTS.md): what raises edge recovery, what produces the false
positives, how the profile lag tracks path length, and how the categorical method extends to graded
signals and to a coordination whose wiring changes mid-run.
