# A recurrence handoff packet: read one coordination with both instruments

The recurrence pipeline packaged for handoff, so a researcher can take one recorded coordination from a
pair of behavioral series to a paired reading: cross-recurrence on the behavior and exact Φ on a model of
the same arrangement. The instruments exist and have run four times on real public data (v8–v11); what this
packet adds is the front door, the pre-registration discipline, and a runnable end-to-end scaffold for a
new study, so the fifth run starts from a template instead of from the four worked examples. It is the
behavioral-arm companion to the [field-study packet](../../../field/packets/gig_dispatch/) and the
[survey packet](../../../survey/cohort_algorithmacy/): those read structure and measure competence, this
one reads coordination off behavior.

## What a recurrence study produces

Two answers about one arrangement, from two instruments that catch what the other misses.
Cross-recurrence quantification analysis reads the behavior: whether two recorded series occupy matching
states over time, how much of that tracking is sustained rather than coincidental, and the lag that reads
leader from follower. It needs no model. Exact Φ reads the structure: whether a Boolean model of who
determines whom is causally irreducible, and which parties sit in the major complex. The pairing is the
contribution, and [the arm's charter](../../README.md) and [CONCEPTS.md](../../CONCEPTS.md) state what each
measure indexes and how they differ.

## The pipeline, and where each piece already lives

A recurrence study runs in stages. The reusable instruments are in the arm; the worked instances are the
templates to copy.

1. **Bound the coordination and pick the series.** Name the parties and the recorded behavior that stands
   in for each one's state over time (commits per week, merges per PR, a monitor's readings). The four
   instances show the range: [`real_series/`](../../real_series/) (commit activity),
   [`event_series/`](../../event_series/) (PR and review events), [`review_heavy/`](../../review_heavy/)
   (a review-gated project), [`bot_merged/`](../../bot_merged/) (a machine merge actor).
2. **Encode the bit.** Turn each series into an active/inactive state per time step, recording the rule and
   the alternative the evidence does not rule out. This is the field protocol's bit calibration on recorded
   data; [`real_series/encode.py`](../../real_series/encode.py) is the worked example.
3. **Commit the pre-registration.** Fill in [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) and commit it
   before running the analysis, so the git history shows the predictions and decision rules were fixed
   first. Each instance's `HYPOTHESES.md` is a filled example.
4. **Fetch and freeze the provenance.** Pull the raw data once and commit it as a frozen CSV, the way each
   instance keeps its `fetch_*.py` and the raw file beside it.
5. **Run both instruments.** [`run_study.py`](run_study.py) runs the paired reading: cross-recurrence
   (recurrence rate, determinism, line length, peak lag) through the arm's [`crqa.py`](../../crqa.py), and
   exact Φ through the lab's probe. It runs now on a bundled example and accepts your series and model.
6. **State the verdict against the pre-registration.** Report which predictions held and which were
   refuted, the way each instance's `FINDINGS.md` does.

## How to instantiate

Copy this directory to `org_frontier/recurrence/<your_study>/`, replace the bundled example series in
[`run_study.py`](run_study.py) with your encoded series and your elicited Boolean model, fill and commit
[`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) before you run anything, then run the analysis and write the
findings. Run the scaffold from the repo root:

```bash
PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/recurrence/packets/template/run_study.py
```

The cross-recurrence half runs on numpy alone. The Φ half needs the PyPhi venv from
[`../../../../GETTING_STARTED.md`](../../../../GETTING_STARTED.md); when it is absent the scaffold runs the
behavioral half and says where the structural half goes.

## What it closes, and what it does not

A completed study closes one coordination's behavioral reading and pairs it with the structural one on the
same arrangement. Cross-recurrence runs on any recorded series, including a party the structural model
handles awkwardly, a signal-emitter that takes up nothing. The two open steps the arm names stay open: a
coordination whose determination rule must be recovered from interviews rather than read off a documented
process is the [field protocol's](../../../field/PROTOCOL.md) harder elicitation, and a bedside
model-bound study is the [neonatal prior's](../../../qualitative/neonatal_third/PRIOR_ANALYSIS.md). This
packet hands off the method; the encoding still has to fit the arrangement, which is where v8 located the
gap and v9 began to close it.
