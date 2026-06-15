# Overview — what this lab is doing, where it stands, and how to join

A five-minute orientation for anyone deciding whether to contribute. For navigation, use the directory
in [`README.md`](README.md); this page is for judging whether the program is worth your time.

## In two minutes

This lab asks one question about coordination: when a worker, a mediating system, and a counterpart work
together, is the arrangement *irreducible* — does it genuinely bind all three — or does it factor into
independent two-party pieces? It answers by modeling the arrangement as a small Boolean dynamical system
and computing exact integrated information (Φ, from IIT 4.0, via [PyPhi](https://github.com/wmayner/pyphi)).
A form is **triadic** (irreducible; the lab's name for it is *algorithmacy*) or **dyadic** (it factors;
*literacy*). On systems small enough, that verdict is exact, not a proxy.

The work runs as a fixed protocol: every question gets a literature pass, five hypotheses fixed before any
computation, an instrument-validated run, and a paper. There are 74 such questions, a measure-validation
arc that established Φ as the instrument first, six synthesis papers that tie threads together, and a
field arc that begins the bridge to real organizations.

## The honest standing

The distinguishing feature of this lab is that it tells you where it is weak, and you should know that
before contributing.

- **The instrument is real and the results are exact and reproducible.** Every number re-derives from a
  committed script under CI. That part is solid.
- **Most individual "laws" are rediscoveries.** When the program ran the literature on its own results, it
  found that bidirectional coupling is IIT's own requirement, that pivotality and substitutability are
  cooperative game theory's (the Shapley value), that the platform-position theory is platform economics'
  competitive bottleneck and the outside-option principle, and that the commit-versus-convey distinction is
  the communication literature's own. The synthesis paper states this plainly.
- **A little is genuinely new.** A graded membership relation (complex membership rising with causal
  pivotality, where IIT membership is per-form binary) and an extremes-only quorum law. Both are bounded;
  see the synthesis and its committee review for how much weight they bear.
- **The real contribution is the bridge, not any single law.** One exact, computable criterion — Φ
  irreducibility on a coordination model — turns out to be the common image of five separate disciplines'
  tests, and it names *which* parties are bound (the major complex), which a one-line heuristic cannot.
- **The validation gap is open.** Everything is in-silico: evidence about Boolean models of coordination,
  not measurements of organizations. No real worker, platform, or message has been measured. Closing this
  is the program's largest open need.

If you want a program that overclaims, this is not it. If you want one that subjects its own results to
deep research and an adversarial committee and reports what survives, read the
[synthesis](org_frontier/essays/committed_determination_synthesis.md) and its
[committee review](org_frontier/essays/committed_determination_committee_review.md) and decide.

## What is already here

- **The instrument and its validation** — [`foundations/`](foundations/): a complete manuscript showing
  no cheap proxy recovers exact Φ, so the exact computation is needed. The classifier, controls, and the
  major-complex reading live in [`org_frontier/classifier/`](org_frontier/classifier/).
- **The logbook** — 74 questions in [`org_frontier/questions/`](org_frontier/questions/), each a full
  paper, plus a per-probe log in [`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md).
- **Synthesis & reviews** — the six pipeline papers (core-membership law, coordination-logic atlas,
  discriminant boundaries, platform position, the field protocol) and the cross-program
  [synthesis](org_frontier/essays/committed_determination_synthesis.md).
- **The field arc** — [`org_frontier/field/`](org_frontier/field/): a protocol for modeling one real
  coordination arrangement and the verdict it yields, demonstrated on ten mock organizations, with the
  validation gap kept explicit.

## Where you could contribute

Concrete open threads, roughly easiest to hardest. Each is a real gap, not busywork.

- **Pick an open question.** Fifty are pre-written and waiting in
  [`org_frontier/RESEARCH_AGENDA_50_V2.md`](org_frontier/RESEARCH_AGENDA_50_V2.md). Scaffold one with
  `python -m org_frontier.protocol.new_question` and run it through the protocol.
- **Stress a standing result.** The extremes-only quorum law (study D) uses clean threshold counts; does it
  survive *weighted or noisy* quorums? The membership law (study A) uses a single-node influence proxy;
  does a higher-order pivotality measure sharpen the Shapley correspondence past the null-player corner?
  (A first pass exists in [`org_frontier/threads/shapley_membership`](org_frontier/threads/shapley_membership/THREAD.md)
  — the exact Shapley value reaches AUC ≈ 0.87 vs ≈ 0.63 for single-node influence; extending it to
  larger forms and a coalition-formation account is open.)
- **Settle a construct question the committee flagged.** Find one coordination arrangement that is
  *algorithmacy but not directive algorithmic management* (or show none exists). That case is what would
  establish the construct's marginal value.
- **Run the first real field case.** The field protocol ([`org_frontier/field/PROTOCOL.md`](org_frontier/field/PROTOCOL.md))
  is ready and its weakest step — eliciting determination rules from evidence with reported inter-rater
  reliability — is specified but undemonstrated. A single honest real-world case, run and reported, is the
  highest-value contribution available, because it begins to close the validation gap.
- **Push past the size ceiling.** Exact Φ is feasible to ~10–12 elements. The proxy-bridge attempt
  (foundations) does not yet recover the verdict from cheap signals; making it work would unlock larger
  arrangements.
- **Review, don't just submit.** The program runs a reproducibility-first public review; maintainers and
  reviewers are needed (see [`MAINTAINERS.md`](MAINTAINERS.md)).

## How to start

1. Read [`GETTING_STARTED.md`](GETTING_STARTED.md) — environment, the instrument-validation gate, the model
   in one paragraph, and the contributor path end to end.
2. Read one worked question (e.g. [`org_frontier/questions/q43_thompson_interdependence/`](org_frontier/questions/q43_thompson_interdependence/))
   and the [research protocol](org_frontier/protocol/RESEARCH_PROTOCOL.md).
3. Scaffold your own with `python -m org_frontier.protocol.new_question`, commit your hypotheses *before*
   computing, register your numbers for CI, and open a pull request into `contrib` per
   [`PUBLISHING.md`](PUBLISHING.md).

## The pitch, in one paragraph

A coordination arrangement is irreducible when a mediating system commits a determination that binds all
parties, and reducible when it merely conveys while the parties stay separable. This lab makes that line
exact and computable, names which parties a real arrangement would bind, and submits every claim to deep
research and adversarial review before keeping it. Most of what it has found, other fields already knew in
their own terms; the lab's contribution is to compute the same line once, across all of them, on explicit
models — and the largest thing left to do is to point the instrument at a real organization and report
honestly what breaks.
