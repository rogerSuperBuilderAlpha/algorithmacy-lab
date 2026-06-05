# Methodology review (Stage 1, applied to the protocol itself)

The protocol asks each question to pass through six stages: review, deep research, five hypotheses,
methods, run, paper. This review places that pipeline against established research norms before the deep
research in `literature/deep_research_report.md` examines it in depth. The exercise is the protocol turned
on itself — a Stage 1 review of the methodology, to be followed by a Stage 2 deep-research run.

## What the pipeline is

A question-driven, in-silico, hypothesis-testing loop with a fixed instrument. The instrument is exact
IIT-4.0 Φ via PyPhi; the questions concern coordination structure; the output is a quantitative paper per
question. The defining commitments are three: hypotheses fixed before computation, claims checked by
running the numbers rather than arguing, and refutations reported as results.

## How it maps to established norms

**Strong inference (Platt 1964).** Platt's prescription is to design experiments that exclude hypotheses,
and to carry several hypotheses at once so that any outcome eliminates some of them. Stage 3's five
hypotheses with their nulls, each falsifiable by a Stage 4 test, is strong inference made routine. The
risk Platt warns of — one pet hypothesis defended past its evidence — is the failure mode the five-way
spread is meant to prevent.

**Multiple working hypotheses (Chamberlin 1890).** Chamberlin's older argument is that a single hypothesis
breeds attachment, and that holding several in parallel keeps the mind impartial. The protocol encodes
this as a count: five, not one. Whether five is the right number, or whether five rephrasings of one masquerade
as five, is a question the gate ("the five are distinct") tries to catch and the deep research should test
against current practice.

**Pre-registration.** Fixing H1–H5 before computation is the spirit of pre-registration without the
registry. The protocol deliberately avoids the word "pre-registered" in papers absent an actual record, to
keep the claim honest. The open question is whether an internal commit timestamp is a credible substitute
for an external registry, and the deep research should report what the open-science literature says.

**Simulation / in-silico science.** The questions are answered on computed models, not field data, which
places the work in the tradition of agent-based and simulation science. That tradition has its own
validity standards — verification (the code computes the intended model) and validation (the model bears on
the target system). The instrument-control gate is verification. Validation, the harder claim that a
Boolean coordination form says something about real organizations, is the protocol's weakest point and is
flagged as such in every paper's Limitations.

**AI-assisted and autonomous discovery.** Running the pipeline with an agent doing the reading, hypothesis
generation, coding, and writing places it among recent "AI scientist" systems. The known hazards there are
fabricated citations, plausible-but-wrong reasoning that survives because it reads well, and a drift toward
confirmation. The protocol's countermeasures are the citation-integrity gate, the compute-don't-assert
rule, and honest-null reporting. The deep research should report how current systems fail and whether these
countermeasures match what the literature recommends.

## Strengths

- **Decision rules fixed in advance** make nulls informative. A pipeline that decides what counts as
  confirmation only after seeing the numbers cannot produce a credible null; this one can, and roughly a
  third of the 134 prior probes are nulls or refinements.
- **A ground-truth instrument** removes the proxy problem for the questions it can reach. Most of social
  science argues over measures; exact Φ on a small system is not a measure to argue over.
- **Mechanized quality gates** (the de-slop greps, the control assertion, the citation check) convert
  judgment calls into checks that run the same way every time.

## Failure modes

- **The validation gap.** Verification is automatable; validation is not. A clean Φ result on a Boolean
  form is only as relevant as the mapping from that form to a real arrangement, and that mapping is a
  modeling choice the protocol cannot certify. Overreading the in-silico result as an empirical claim is
  the standing risk.
- **Five hypotheses can be theater.** The count is easy to satisfy and hard to satisfy well. Five genuinely
  independent predictions are rare; five framings of one are common. The gate is a weak guard.
- **Automated fluency hides error.** An agent writes prose that reads as authoritative whether or not the
  reasoning holds. The compute-don't-assert rule helps only where a claim is computable; the discursive
  parts of a paper are where wrong reasoning can still slip through.
- **The instrument bounds the questions.** Exact Φ is feasible only to about a dozen elements, and the
  verdict is relative to observation grain and update schedule (prior probes #32, #60, #62). Questions that
  need scale or continuous time fall outside what the instrument can answer cleanly.

## What the deep research should settle

Whether the five-hypothesis count has support or is arbitrary; whether an internal pre-commitment is
accepted as pre-registration-equivalent; how autonomous-discovery systems are evaluated and where they
fail; and what validity standards simulation science applies, so the validation gap is addressed by a known
standard rather than a disclaimer.
</content>
