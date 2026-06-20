# Recurrence — reading coordination off behavior, paired with Φ

A coordination arrangement can be read two ways. Its structure says whether the parties form a
causally irreducible whole: that reading is integrated information, the exact Φ the lab already
computes from a model's transition rules. Its behavior says whether the parties' states actually
track each other over time, how strongly, and which one leads: that reading is cross-recurrence
quantification analysis, a time-series method from dynamical systems. This arm pairs them. Φ reads
the model; CRQA reads a run of it; the two answers come from one arrangement, and each catches what
the other cannot.

The pairing is the contribution. Φ is intrinsic and structural. It asks whether the mechanism, taken
as it is, can be split without loss. CRQA is extrinsic and observed. It asks whether two recorded
series occupy matching states in a shared space, in sustained diagonal patterns, with a lag that
reads leader from follower. A search of the literature finds the two used side by side as separate
complexity metrics on single systems and never combined, and never in the between-system
cross-recurrence form (Sarasso et al. 2021 is the closest, and it keeps them apart). The CRQA-to-Φ
bridge is open ground.

## Why the lab needs both

The threads and the corpus compute Φ on Boolean models. The field and qualitative arms reach toward
real coordination, where the evidence arrives as time series: a dispatcher's actions over a shift,
a monitor's readings, an infant's vitals. CRQA is the instrument that turns those series into
coordination measures, and it does so without a model. That makes it the empirical partner the
structural work has been missing. Three uses follow.

- **Recover the wiring.** The diagonal cross-recurrence profile peaks at the lag by which one series
  leads another. That lead-lag is the observable trace of a directed read edge, so CRQA can check the
  who-reads-whom that a Φ model takes as input. The field protocol's bit calibration gains a
  behavioral backstop.
- **Separate sustained coupling from chance.** Determinism and diagonal line length distinguish a
  coordination the parties hold from a momentary coincidence, which is the commit-versus-convey
  question asked of data rather than of a rule.
- **Measure coupling where a model cannot apply.** A party that emits a signal but takes up nothing,
  the infant of the neonatal study, is a case the structural model handles awkwardly. CRQA measures
  the coupling directly from the two series, which is why it is the right instrument for the
  causal-versus-communicative gap that study names.

## The bridge, demonstrated

[`bridge_demo.py`](bridge_demo.py) runs one Boolean model through both instruments. Φ comes from the
model's transition matrix; CRQA comes from a stochastic trajectory of the same model. Two findings,
reproduced in [FINDINGS.md](FINDINGS.md):

- Φ and CRQA partition the coupling regimes between them. Φ alone marks a mutual wiring as
  irreducible and reads a one-way relay as no different from two independent parties. CRQA alone
  reads the relay's direction off the profile lag and reads the independent pair as flat. Each
  instrument resolves a distinction the other misses.
- In the committing triad, each party tracks the apparatus in long sustained episodes while the two
  parties track each other only in short ones, through the hub. The disintermediation result, read
  off behavior, lines up with the apparatus sitting in the major complex as a veto player.

## Files

- [`crqa.py`](crqa.py) — categorical cross-recurrence: the recurrence matrix, the measures (RR, DET,
  line length, entropy), the diagonal profile and its peak lag, and a trajectory generator that runs
  a Boolean form as a stochastic dynamical system.
- [`CONCEPTS.md`](CONCEPTS.md) — what each measure indexes, the parameters, how Φ and CRQA differ,
  and the method citations.
- [`bridge_demo.py`](bridge_demo.py) — the two-instrument demonstration on one model.
- [`FINDINGS.md`](FINDINGS.md) — the demonstration's numbers and what they show.
- [`sweep.py`](sweep.py), [`SWEEP.md`](SWEEP.md) — the corpus-wide sweep: Φ against CRQA on every
  named form, plus the random-ensemble statistics.
- [`iit_experiments.py`](iit_experiments.py), [`IIT_EXPERIMENTS.md`](IIT_EXPERIMENTS.md) — ten Φ
  experiments seeded by the sweep.
- [`crqa_experiments.py`](crqa_experiments.py), [`CRQA_EXPERIMENTS.md`](CRQA_EXPERIMENTS.md) — ten
  CRQA experiments seeded by the sweep.

## The agenda

The sweep and the two experiment batteries close the first wave. The corpus-wide comparison ran
(SWEEP.md): structure and behavior agree on most named forms and part on the false dyad, the relay,
and the back-channel. Edge recovery from the profile lag was characterized at scale (CRQA_EXPERIMENTS
C1–C7): about 40%, held back by common drivers and by coupling too fast or too frozen to track. The
neonatal cross-reference was measured on the committing-triad model (CRQA_EXPERIMENTS C10) and is
designed for bedside series in [`../qualitative/neonatal_third/PRIOR_ANALYSIS.md`](../qualitative/neonatal_third/PRIOR_ANALYSIS.md).
Continuous CRQA with phase-space embedding was demonstrated on graded signals (C8). What remains:

- Take the bridge to four-party and larger forms, where the multiparty and hierarchy threads already
  compute Φ, and the diagonal profile must read more than one lag at once.
- Move from synthetic trajectories to a real recorded series through the field protocol, the first
  time the behavioral instrument runs on data the lab did not generate.
- A model-bound neonatal study: elicit the determination rules, then read the bedside series with
  both instruments against the pre-registered verdict.

## Method note

Φ and CRQA are different instruments for different questions, and the framework keeps them so. Φ is
the principled structural measure the dissertation builds on, and CRQA does not replace it. CRQA is
the behavioral bridge to data the structural measure cannot reach on its own. The neighbor methods
that read directional coupling from time series, Granger causality and transfer entropy and
convergent cross mapping, measure prediction and information transfer. Φ measures something they do
not, intrinsic causal irreducibility, and CONCEPTS.md states the difference so a reader does not
collapse one into the other.
