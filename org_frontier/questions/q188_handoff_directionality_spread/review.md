# q188 — review

## What the probe shows

Two narrations of one shift-boundary handoff read as different Phi structures. The one-way account
is dyadic, the reciprocal account triadic, and the spread between them is graded in the strength of
the narrated back-channel. Both hypotheses, fixed before computing, came out as written.

## Strengths

- The instrument control passes on the faithful triad (triadic, max_phi 2.0), and a second collapse
  control confirms that zeroing the back-channel in both accounts drives the spread to zero. The
  parameter does what it claims.
- H2 is a clean monotone curve, not a single contrast. The Phi gap rises strictly from 0 to 2.0
  with a smallest step of 0.15, so the spread tracks the degree of disagreement and not just its
  presence.
- The study reuses the study-1 bridge and the existing classifier; it does not reimplement Phi.
- Deterministic: byte-identical across three runs under a fixed seed.

## Limits

- The two accounts are synthetic. They are coder-supplied rule sets chosen to instantiate one-way
  vs reciprocal coupling, not narrations elicited from clinicians. The empirical reading is on
  synthetic data.
- The back-channel dial is a stochastic-TPM construction on a single edge. It is a clean reciprocity
  knob, but its mapping to any measurable feature of a real narration is not established here.
- n = 3 and a single rule-set pair. The result is a demonstration on one coordination, not a survey
  across handoff types.

## Standing

The disagreement-as-Phi-spread instrument distinguishes a conveyed handoff from a bound one on
synthetic accounts, and the spread is graded in narrated reciprocity. The validation gap to real
handoff narrations is open.
