# irreducibility-pipeline

Organizations increasingly coordinate through a third thing that sits between the parties: a dispatch
system that matches a driver to a rider, an engine that screens a claim before an adjuster sees it, a CI
gate between an author and a maintainer, an AI agent that negotiates for one side. Whether such an
arrangement is **irreducibly three-party**, or factors into two-party relations that happen to share a
platform, decides who is bound to whom and what a redesign would change. Platform research usually settles
the question by description. This repository settles it by computation.

The pipeline takes a coordinative structure as it is encountered (a description, interview excerpts,
documents) and returns an exact irreducibility analysis:

1. **Encode (AI drafts, a researcher approves).** Rival Boolean models of the arrangement, one per
   defensible reading, with every rule tied to a verbatim quote from the evidence and a prediction fixed
   before anything is computed. A checker rejects any rule whose quote is not in the source.
2. **Compute (PyPhi).** For each encoding, the rules become a transition matrix. PyPhi's IIT-4.0
   implementation returns integrated information Φ over the minimum-information partition in every
   reachable state, and the major complex. **Triadic** means no cut along party lines leaves the structure
   intact (Φ > 0); **dyadic** means some cut does (Φ = 0).
3. **Read (structural position).** Who is bound (the major complex); the mediator's position (bottleneck,
   enricher, capture, bypassed); whether its place is intrinsic or held by a constraint on bypassing it;
   and, across rival encodings, which single rule the verdict turns on.

The repository is the prototype for a proposal to *Organization Science*, "AI-Enabled Frontiers in
Organizational Science." It analyzes structures; the strategic model that maps a structural position to
a decision is the next stage of the work and is not here yet.

## Install

```bash
python -m venv .venv && source .venv/bin/activate      # Python 3.10+; tested on 3.12
pip install -r requirements.txt
python -m irreducibility.validate                      # must end "Instrument validated."
```

`validate` runs two controls before anything else: a structure with a decoupled party must read dyadic
(Φ = 0), and a fully coupled three-node network must read triadic (Φ = 0.830). Five reference forms
follow. Every analysis script refuses to run if the controls fail.

## A walk-through: gig dispatch

**The structure** ([`examples/01_gig_dispatch/prose.md`](examples/01_gig_dispatch/prose.md), a stipulated
description, not field data). A driver, a dispatch platform, a rider; the recurring act is one match. The
platform's manual says "The system assigns a trip only when an eligible driver is available and a rider
has confirmed the request." A driver says "It's a suggestion, it follows what I do." The manual also says
"Any eligible driver in range may be assigned," and some riders "just text my regular driver."

**Encode.** [`encodings.json`](examples/01_gig_dispatch/encodings.json) holds three rival readings and
five design scenarios. Each party's rule is a Boolean expression; each rule cites its passage:

```json
"rules":    {"D": "P", "P": "D and R", "R": "P"},
"evidence": {"P": [{"source": "prose.md", "locator": "¶2",
                    "quote": "The system assigns a trip only when an eligible driver is available and a rider has confirmed the request"}]},
"alternative": {"P": {"rule": "D", "why": "Drivers describe dispatch as a suggestion that follows the driver (¶3)"}},
"predicted": {"structure": "triadic", "core": ["D", "P", "R"], "reason": "..."}
```

```bash
python -m irreducibility.encode_check examples/01_gig_dispatch/encodings.json
# ADMISSIBLE: 8 encoding(s); every rule has evidence found verbatim in its source; every encoding carries a prediction.
```

**Compute.**

```bash
python -m irreducibility.analyze examples/01_gig_dispatch/encodings.json
```

```
[A] platform's account: dispatch commits a binding match  (rival)
    D' = P
    P' = D and R
    R' = P
  PyPhi input: TPM 8x3 (state-by-node), connectivity [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
  Φ_MIP by reachable state: 000:0.000, 010:0.000, 101:0.000, 111:2.000
  verdict: TRIADIC  max Φ_MIP = 2.000  (1/4 states irreducible)
  MIP at state 111: 2 parts: {D,PR}
  major complex (who is bound): {D, P, R}
  mediator (P) position: BOTTLENECK
  bypass test on P: intrinsic (Φ lost when the bypass opens: 0.000; core {D,P,R} -> {D,P})
  predicted before computing: triadic, core {D,P,R}  -> HELD

[B] driver's account: dispatch relays a suggestion  (rival)
  verdict: DYADIC  max Φ_MIP = 0.000  ...  major complex: {D, P}

[C] pooled drivers: any eligible driver will do  (rival)
  verdict: DYADIC  ...  major complex: {P, R}            <- the driver drops out of the core
```

**Read.** The three readings disagree, and the report says on what:

```
A vs B: verdicts triadic/dyadic, Φ gap 2.000, core overlap 0.667
    single rule that flips it: P: 'D and R' -> 'D'
CONTESTED: the verdict depends on which encoding the evidence supports
```

The whole question is whether dispatch *commits* a match that needs both parties or *relays* the driver's
choice. That is the fact a field study must settle. Pooling drivers (reading C) removes the individual
driver from the irreducible core: the platform and the rider remain bound, the driver does not.

The five design scenarios hold the platform's rule fixed and vary the parties' outside options:

| Scenario | Driver | Rider | Position of the platform | Core |
|---|---|---|---|---|
| O1 both captive | `P` | `P` | BOTTLENECK | {D, P, R} |
| O2 complementary direct tie | `P and R` | `P and D` | ENRICHER | {D, P, R} |
| O3 captive driver, mobile rider | `P` | `P or D` | CAPTURE | {D, P} |
| O4 mobile driver, captive rider | `P or R` | `P` | CAPTURE | {P, R} |
| O5 both mobile | `P or R` | `P or D` | BYPASSED | {D, R} |

Giving only the driver an outside option does not free the platform; it moves the lock-in to the rider
(O3 → O4). Only symmetric options remove the platform from the core (O5). These are readings of a model;
what a platform, a drivers' collective or a regulator should *do* given them is the strategic model still
to be built.

## Where AI enters, and what it did

[`encode/`](encode/) holds the AI step: a JSON schema, a **drafter** prompt (rival encodings with verbatim
evidence and a prediction) and an **adversary** prompt (the most different readings the evidence still
permits: commit vs convey, substitutability, outside options). Both are model-agnostic. The checker
[`irreducibility/encode_check.py`](irreducibility/encode_check.py) rejects a rule with no evidence, a quote
not found verbatim in the source, a mediator rule with no alternative, or an encoding with no prediction.

Logged runs (Claude Sonnet 5.5, 26 Oct 2026, prompts as committed, case prose only, no tools):

- **Gig dispatch, drafter** ([`ai_draft.json`](examples/01_gig_dispatch/ai_draft.json)): two rival
  encodings, identical to the human encodings A and B; all quotes verbatim; both predictions held. It did
  not encode the driver pool.
- **Gig dispatch, adversary** ([`ai_draft_plus_adversary.json`](examples/01_gig_dispatch/ai_draft_plus_adversary.json)):
  found the driver pool and the substitute direct tie, and declined a complement tie as unsupported by ¶6.
  **Both of its predictions failed** when computed: it expected the pooled structure to stay triadic (it
  is dyadic, core {P, R}) and the direct-tie structure to be dyadic (it is triadic with the platform
  bypassed, core {D, R}). The model found the readings; PyPhi decided them.
- **Insurance claim, drafter** ([`ai_draft.json`](examples/02_insurance_claim/ai_draft.json)): for four of
  five designs it declined to write rules the prose does not specify and said what evidence was missing.
  The checker rejects the file (9 problems), which is the gate doing its job.

Nothing yet reads interview transcripts or documents at scale; that, and agreement between the AI drafter
and two human coders, is the next stage.

## Run it on your own structure

1. Write the case material to a file and number its paragraphs or give each excerpt a locator.
2. Copy an `encodings.json`, set the `parties` and the `mediator`, and write each party's rule as a
   Boolean expression over party labels (`and`, `or`, `not`, `xor`, `0`, `1`). Cite a verbatim quote for
   every rule and fix the prediction. Or paste the case into [`encode/PROMPT_drafter.md`](encode/PROMPT_drafter.md),
   then [`PROMPT_adversary.md`](encode/PROMPT_adversary.md), with any model.
3. `python -m irreducibility.encode_check your.json`
4. `python -m irreducibility.analyze your.json --json report.json`

The field protocol for real arrangements (bounding the act, coding the bits, eliciting rules from
evidence, inter-rater reliability, ethics) is in [`protocol/`](protocol/).

## Reproduce every number

```bash
python reproduce.py          # 17 checks, about 2 minutes on a laptop
pytest -q                    # 19 tests
```

| Check | What it reproduces |
|---|---|
| `instrument-controls` | the controls and five reference forms |
| `example-*` | the four worked examples (gig dispatch, insurance claim, code-review gate, dealer vs clearinghouse) |
| `ai-draft-gig`, `ai-draft-insurance-rejected` | the logged AI runs, checked and computed |
| `census` | 24 of 256 strict-mediation structures are triadic; 24/160 where the mediator reads both parties, 0/96 otherwise |
| `field-mocks` | ten mock organizations: 9/10 match the reading fixed before computing; 4 flip under a second defensible encoding |
| `mediator-in-core`, `enricher-regime` | regime frequencies over 500 random forms; the outside-option law (60/60) |
| `contingent-irreducibility` | the bypass test separates intrinsic from contingent intermediation |
| `design-operations` | three design levers (binding, liveness, requirement), each with a build and an inverse break |
| `thompson-ordering` | Thompson's pooled < sequential < reciprocal ordering collapses at the top step |
| `adversarial-coding` | an evidence-limited adversary flips the point verdict on 101/101 contested accounts |
| `proxies` | two time-series proxies separate dyadic from triadic at rank-AUC 0.563 and 0.629 (0.5 is chance) |

## Scope

- Verdicts are exact **for the stated encoding**. The same arrangement can be encoded more than one
  defensible way, which is why the pipeline reports every encoding and the rule the verdict turns on.
- A verdict on a model is evidence about the model. It is not, by itself, evidence that real workers
  experience an arrangement as irreducible; that needs fieldwork.
- Exact Φ is practical up to about ten binary nodes. Coordination units of three to five parties compute in
  seconds.
- The examples are stipulated descriptions written to demonstrate the method, and the lab's results for
  them were known when they were written; their predictions record the naive reading, not a blind test.

## Layout

```
irreducibility/   core.py (PyPhi wrapper) · validate.py · regime.py · contingency.py · spread.py
                  rule_to_phi.py · rules.py · encoding.py · encode_check.py · analyze.py
encode/           SCHEMA.json · PROMPT_drafter.md · PROMPT_adversary.md
examples/         01_gig_dispatch · 02_insurance_claim · 03_code_review_gate · 04_dealer_vs_clearinghouse
studies/          the scripts behind the reference results (census, mocks, regimes, design operations, ...)
protocol/         field protocol, coding scheme, interview guide, ethics, predictions fixed in advance
tests/            pytest suite
reproduce.py      one command for every number
```

MIT licensed. PyPhi is developed by the Tononi lab (Mayner et al., 2018, *PLOS Computational Biology*); IIT
4.0 is specified in Albantakis et al. (2023, *PLOS Computational Biology*).
