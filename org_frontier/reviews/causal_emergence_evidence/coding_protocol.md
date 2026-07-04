# Coding protocol (codebook) — causal emergence: evidence, formalism, claim direction

Code each source from its title + abstract. Code what the SOURCE does, not what this review predicts.
You are one of several independent coders; do not consult another coder's output. Use `na` where a
variable does not apply. When unsure between two values, pick the better fit — disagreement is expected
and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id (copy it verbatim from `literature/corpus.jsonl`).

- **evidence** — how the source supports its claim about emergence / downward causation (tests H1):
  - `conceptual` — philosophical or theoretical argument, analogy, review, or position; no emergence
    measure is computed. Most philosophy-of-mind and metaphysics sources are here.
  - `formal_model` — an emergence / causation measure (effective information, integrated information,
    a decomposition term, a dynamical-independence criterion, etc.) is computed or derived on a toy,
    simulated, abstract, or synthetic system (Boolean networks, Markov chains, cellular automata,
    Ising models, Game of Life, flocking simulations, worked mathematical examples).
  - `empirical` — an emergence / causation measure is computed on real measured data from an actual
    system (neural / fMRI / ECoG recordings, biological, financial, social, ecological data). The
    system must be real and measured, not simulated.
  - `na` — not applicable (e.g. a pure methods or tooling paper with no emergence claim).

- **formalism** — the formal apparatus the source uses or discusses (tests H3):
  - `information_theoretic` — effective information, integrated information / Φ, information
    decomposition (PID / ΦID), channel-capacity or entropy-based measures of emergence.
  - `dynamical` — dynamical-systems machinery: coarse-graining of state-space dynamics, dynamical
    independence, computational mechanics, renormalization / scale transforms, attractor / stability
    arguments, differential-equation or iteration-map models.
  - `statistical` — causal-inference or statistical measures: interventionist / Pearl-style causation,
    Granger-type prediction, regression, causal primitives (sufficiency / necessity), model selection.
  - `other` — a formal apparatus that fits none of the above (e.g. category-theoretic, logical,
    thermodynamic-only).
  - `na` — no formal apparatus is used or centrally discussed (most purely verbal philosophy).

- **claim_direction** — the direction of the source's central claim about whether macro-scale causal
  emergence / downward causation is real (tests H2):
  - `emergence_real` — argues or shows that macro-scale causal emergence (or downward causation) is
    genuine: macro can carry causal power the micro lacks, emergence is ontological, the measure
    detects a real effect.
  - `deflationary` — argues that the apparent emergence is not genuine in the strong sense: it is
    observer-relative, epistemic, a coarse-graining or measure artifact, or reducible; downward
    causation is incoherent or dispensable.
  - `neutral` — takes no side, or develops method / measurement without adjudicating the reality
    question (surveys that only summarize, tooling papers, measure-development papers that stay
    agnostic).

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"hoel2013","evidence":"formal_model","formalism":"information_theoretic","claim_direction":"emergence_real"}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list order
and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts `evidence=empirical` is rare. A source that genuinely computes an emergence measure on
  real measured data is a real disconfirming datum — record it as `empirical`.
- H2 predicts both `emergence_real` and `deflationary` are well represented. Code the direction the
  source actually takes; a source with no side is `neutral`, not a forced pick.
- H3 predicts formalisms fragment. Code the formalism the source actually uses, not the one the review
  is about.
