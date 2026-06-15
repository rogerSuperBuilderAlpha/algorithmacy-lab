# Platform-position theory — Stage 1 review

## The question

When is a mediating system part of the irreducible coordination it sits in, and what governs whether
it is an indispensable bottleneck, a dispensable enricher, a captor of one side, or bypassed?

## What is already here

Two exploratory threads, both CI-gated and reproducible:
- `THREAD.md` / `mediator_in_core.py` — the trichotomy (bottleneck / enricher / bypassed) and the
  disintermediation result: a platform is bypassed when the parties' direct tie is a *substitute* for
  it, not a *complement*.
- `THREAD_enricher.md` / `enricher_regime.py` — genuine enrichment is rare (6%) and fragile; capture
  dominates the in-core regime (28%); the outside-option law: a platform's irreducible core is itself
  plus exactly the parties with no outside option; asymmetric options give capture (lock-in of the
  dependent side), symmetric options give bypass.

## The honest status, and the gap

These threads were *exploratory*, not pre-registered. They formed and revised predictions iteratively
(documented self-corrections at thread Q3, Q18, E2/E3). To make this a paper, two things are needed
that the threads lack:

1. **A literature pass.** The outside-option law, disintermediation, and lock-in are squarely in the
   territory of platform economics (two-sided markets, multi-homing, competitive bottlenecks),
   switching-cost lock-in, and bargaining theory (outside options / BATNA, hold-up). The threads cite
   none of it. The result is the most likely of the whole pipeline to be a rediscovery, and the
   deep-research report (`literature/`) must establish exactly which parts match known economics and
   whether anything is new.
2. **Pre-registration.** The exploratory findings must be restated as hypotheses fixed before a fresh
   confirmatory run. The two thread scripts are deterministic and serve as that run; `hypotheses.md`
   pre-registers the claims (drawn from the threads, framed by the literature) and the existing
   CI-gated outputs confirm them.

The contribution, if any survives the literature check, is not the economics — it is the *structural
restatement*: that a value-theoretic result about outside options appears as an exact cause-effect
membership law (the major complex equals the platform plus the parties with no outside option),
computed from IIT-4.0 Φ on a Boolean model. The paper will be explicit that the economic content is
established and the contribution is the bridge, or it will retract the claim to novelty entirely.
