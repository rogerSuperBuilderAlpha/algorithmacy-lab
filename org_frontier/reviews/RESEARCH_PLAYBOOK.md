# Research playbook: a systematic archival review that tests claims about a literature

A reusable process for running an experiment on a body of literature. The output is not a synthesis
essay; it is a set of falsifiable claims about a field, tested against a coded corpus and its citation
graph, with an intercoder-reliability figure. The method draws two frameworks together (both in
[`METHODS_FOUNDATIONS.md`](METHODS_FOUNDATIONS.md)): the seven *practices* of systematicity (Simsek,
Fox & Heavey 2023) give the pipeline its stages, and the *knowledge-weaving* stages (Simsek, Heavey,
Fox & Yu 2022) give the review its questions — a literature's stylized facts, key assumptions,
enduring critiques, and substantive omissions are exactly the claims a review can test.

Two rules carry most of the weight, and they match the lab's own discipline:

1. **Fix the hypotheses before computing.** Commit `hypotheses.md` in its own commit, before any
   corpus is harvested or coded. The git history is the pre-registration.
2. **Measure, do not assert.** "The homes are isolated," "the rivals ignore each other," "no one has
   assembled these" are claims a citation graph can check. Run the numbers; report what they show,
   including when they challenge the hypothesis. A challenged hypothesis is a finding.

---

## Phase 1 — Envision (the question and its knowledge claims)

- State one orienting question about the literature. Systematicity distinguishes five kinds
  (exploratory, descriptive, evaluative, integrative, explanatory); name which yours is, because it
  fixes what counts as an answer.
- Extract the target field's **knowledge claims** and sort them by type: *stylized facts* (what the
  field takes as established), *key assumptions* (what it takes for granted), *enduring critiques*
  (its unresolved disputes), *substantive omissions* (what it has not addressed). Each claim you mean
  to test becomes a hypothesis.
- Write each hypothesis so a number can falsify it. "Sub-literature A and B developed in isolation"
  becomes "cross-cluster citation ≪ within-cluster citation." "No one has assembled these" becomes
  "no external paper cites sources from ≥ k of the clusters." "X is asserted, not tested" becomes a
  coding variable (conceptual vs empirical) with a predicted proportion.

## Phase 2 — Explicate (the corpus boundary)

- Define the corpus boundary explicitly — substantive (theories, constructs, level of analysis) and
  procedural (period, fields, journals, databases). State it so the inclusion of any single source is
  decidable.
- Decide the gray-literature question on purpose (preprints, reports, dissertations in or out) rather
  than by accident of which database you searched.
- These boundaries are the review's gates. Record them; they are what makes the corpus auditable.

## Phase 3 — Execute (search and citation harvest)

- Derive search terms from the question, balancing recall and precision. Seed from a known-relevant
  set, then snowball: `lib/harvest.py` pulls each seed's backward references and forward citers from
  Semantic Scholar.
- Use an explicit stopping rule and log it — e.g. Booth's heuristic of terminating when a search
  yields fewer than five relevant articles per hundred references scanned. Never truncate silently; a
  review that drops coverage without saying so reads as complete when it is not.
- References are elided by some publishers, so the outbound-citation channel is partial; the inbound
  citer channel is more complete. Keep both.

## Phase 4 — Encode (the codebook and independent coders)

- Write a fixed codebook (`coding_protocol.md`): one row per variable, each with a closed set of
  values and a one-line rule. Include the variables your hypotheses need (cluster/home, claim type,
  conceptual-vs-empirical, which dimensions a source develops) and the source id.
- Have **at least three independent coders** apply the codebook blind to one another, coding the
  source's own argument from its note or abstract. Coders are naturally LLM agents run in parallel
  (one per coder, same codebook, no shared output); the harness is the Agent-spawn pattern documented
  in [`lib/README.md`](lib/README.md).
- Compute reliability with `lib/reliability.py`: Fleiss' κ per categorical variable, Jaccard for
  set-valued ones, and a majority-vote adjudicated dataset. Report κ; it is the answer to the
  single-coder objection. Landis & Koch read κ > 0.80 as almost perfect, 0.61–0.80 as substantial.

## Phase 5 — Evaluate (test the claims)

- Run the content-coding tests on the adjudicated dataset: cross-tabulate the coded variables against
  the hypotheses (e.g. the proportion of a home's sources framed one way, the per-cell coverage across
  sub-literatures).
- Run the bibliometric tests with `lib/bibliometrics.py`: the cluster-to-cluster citation matrix (a
  block-diagonal shape is isolation), the assembly-spanning count (how many clusters any prior paper
  reaches), and mutual-citation density among a named rival set.
- Report every hypothesis with its statistic and a verdict — supported, qualified, or challenged.
  State the limitations that bound each: elided references, small clusters, a corpus inherited from a
  prior review rather than an independent search, coders who are agents rather than trained humans.

## Phase 6 — Exposit (the findings)

- Write `FINDINGS.md`: the per-hypothesis verdicts with their numbers and the reliability figure, then
  the honest limitations. Lead with what the data show, not with the framing.
- Match the lab's prose discipline (see the root `CLAUDE.md` and `foundations/RESEARCH_PLAYBOOK.md`
  Phase 7): plain declarative sentences, short noun-phrase section titles, no meta-narration, effect
  size alongside significance. A challenged hypothesis stated plainly is worth more than a supported
  one dressed up.
- Register any headline numbers in `ci/reproduce.json` and list the exact reproduce commands.

---

## Reusable file layout

```
<review_slug>/
  README.md            the question and where it stands
  hypotheses.md        the falsifiable claims, committed BEFORE results
  coding_protocol.md   the codebook (variables, values, rules)
  methods.md           corpus boundary, search, coder design, statistics
  seeds.json           [{slug, doi|title}] for the harvest
  clusters.json        {slug: cluster_label} for the bibliometrics
  coding/              one JSONL per independent coder (coderA.jsonl ...)
  edges/              per-seed citation-graph files (from lib/harvest.py)
  results/             frozen (adjudicated) dataset, matrices, tables
  literature/
    references.bib     the corpus (open-access PDFs only; paywalled = note + DOI)
  FINDINGS.md          per-hypothesis verdicts + reliability figure + limitations
```

## The short version

Extract a field's knowledge claims and turn the ones you can test into falsifiable hypotheses. Fix
them before computing. Bound the corpus explicitly, harvest its citation graph, and code it with three
independent coders — then report Fleiss' κ, which is what a single-coder review cannot. Test the
claims with the coded data and the citation matrix. Report every hypothesis with its number and an
honest verdict, challenges included. Make it reproducible end to end.
