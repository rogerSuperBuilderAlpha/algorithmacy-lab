# Coding protocol (codebook) — measures of integrated information: families and validation

Code each source from its title + abstract (and note, where present). Code what the SOURCE does, not
what this review predicts. You are one of several independent coders; do not consult another coder's
output. Use `na` where a variable does not apply. When unsure between two values, pick the better fit —
disagreement is expected and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id.

- **measure_family** — the family of integration / complexity / synergy measure the source proposes,
  develops, or centrally studies (tests H1 and H3). Closed set:
  - `exact_iit_phi` — the exact IIT measure Φ in one of its canonical formulations (IIT 2.0/3.0/4.0,
    Tononi/Oizumi/Albantakis PyPhi-style Φ), computed or defined as the theory prescribes.
  - `practical_proxy` — a practical / empirical approximation of Φ meant to be tractable on data or
    larger systems: Φ*, Φ_AR / autoregressive Φ, stochastic-interaction / mismatched-decoding Φ,
    Φ_G geometric integrated information, whole-minus-parts / whole-minus-sum surrogates.
  - `causal_emergence` — Hoel-style causal emergence, effective information, causal primitives, macro
    vs micro causation measures.
  - `iid_synergy` — integrated information decomposition (ΦID), partial information decomposition
    (PID), synergy / redundancy measures, Φ_R.
  - `total_correlation` — total correlation, multi-information, integration as I(whole) − Σ parts,
    interaction complexity, mutual-information-based integration indices not framed as Φ or as
    decomposition.
  - `geometric_complexity` — neural complexity (Tononi–Sporns–Edelman), TSE complexity, and other
    complexity / integration–segregation balance measures (excluding those better placed above).
  - `other` — a distinct measure that fits none of the above (name it in a `note` if you like).
  - `na` — not a proposal or study of an integration/complexity/synergy measure.

- **validation** — how the source establishes that its measure captures integration (tests H2):
  - `ground_truth` — validates the measure against a ground truth: exact IIT Φ, another reference
    measure treated as criterion, a known generative structure, or an external empirical criterion the
    measure is scored against.
  - `internal` — self-consistency only: axiomatic derivation, satisfaction of desiderata, toy-example
    sanity checks, or demonstration on simulated systems without scoring against an external criterion.
  - `none/conceptual` — proposes, asserts, reviews, or argues for the measure with no validation.
  - `na` — not applicable.

- **substrate** — the system the measure is applied to or demonstrated on:
  - `neural` — brain, neural, EEG/MEG/fMRI, neural-network activity.
  - `simulated` — toy models, Boolean networks, logic gates, simulated dynamical systems.
  - `abstract` — purely formal / mathematical, no specific substrate.
  - `other` — anything else (social, artificial, physical) or mixed.
  - `na` — not applicable.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"balduzzi2008","measure_family":"exact_iit_phi","validation":"internal","substrate":"simulated"}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list order
and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts many families each carry sources. Code the family the source actually proposes, even if
  it is a rare one.
- H2 predicts `validation=ground_truth` is rare. A source that genuinely scores its measure against
  exact Φ or an external criterion is a real disconfirming datum — record it as `ground_truth`.
