# Coding protocol (codebook) — systematicity in consciousness-science reviews

Code each review from its title + abstract (and journal, where it disambiguates). Code what the SOURCE
reports, not what this review predicts. You are one of several independent coders; do not consult
another coder's output. Be conservative: a practice counts `yes` only when the abstract shows positive
evidence that the review performed or reported it. Absence of evidence is `no`. Disagreement is expected
and measured by Fleiss' κ.

The seven practices are Simsek, Fox & Heavey's (2023). Each is the reportable trace of one stage of a
systematic review. Below is the operational rule for judging each from an abstract.

## The seven practices (each coded "yes" / "no")

- **envisioning** — the review states an explicit orienting question, objective, or aim, or names its
  review type (systematic, scoping, narrative, integrative). Evidence: "the aim of this review is…",
  "we ask whether…", "this scoping review…", a stated research question. `no` if the abstract only
  announces a topic ("here we discuss consciousness theories") with no stated question or aim.
- **explicating** — the review states its boundary conditions: scope, inclusion window, which theories
  or literatures are in or out, level of analysis. Evidence: "articles published between 2007–2017",
  "we restrict attention to neuroscientific theories", "four prominent approaches". `no` if scope is
  left implicit.
- **executing** — the review describes how it searched or assembled its sources: a database search,
  search terms, screening counts, citation tracking, a corpus size. Evidence: "1130 articles were
  assessed, 85 included", "a systematic search of PubMed", "N = 412 experiments". `no` if no search or
  assembly procedure is described (most narrative reviews).
- **evaluating** — the review describes appraising, weighing, or quality-checking the evidence or
  theories it covers, or a criterion for doing so. Evidence: "we assess the strengths and limitations",
  "we evaluate which theory better predicts", "critically evaluated", a comparison rubric or scoring.
  `no` if sources are summarized without appraisal.
- **encoding** — the review describes extracting or coding its sources into a structured scheme: a
  framework, grid, taxonomy, dimensions, categories, or classification applied across sources.
  Evidence: "a thematic grid", "we classify along three dimensions", "an inter-theory classification
  interface", "explanatory profiles". `no` if no structured extraction scheme is described.
- **elaborating** — the review builds something beyond summary: a synthesis, integration, new
  framework, model, agenda, or propositions developed from the coded material. Evidence: "we propose a
  unifying framework", "toward a standard model", "we develop a taxonomy", "a research agenda". `no` if
  the review only reports what others have said.
- **expositing** — the review reports on its own procedure transparently enough to be reproduced or
  audited: it describes its method, steps, or protocol as part of the reporting (PRISMA-style flow,
  stated stages, a replication or data-sharing statement, an open database). Evidence: "following
  PRISMA", "we preregistered", "the database is openly available", an explicit methods description of
  the review itself. `no` if the review's own process is not described.

Note the distinction the codebook enforces: **executing** is doing a search; **expositing** is
reporting the review's method transparently; **encoding** is having a coding scheme; **elaborating** is
building new synthesis on top. A narrative overview typically shows envisioning and elaborating but not
executing, encoding, or expositing. A scoping review typically shows all or most.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source, every field present:

`{"slug":"theoriesofconsciousne2021","envisioning":"yes","explicating":"yes","executing":"no","evaluating":"yes","encoding":"no","elaborating":"yes","expositing":"no","year":2021,"cites":420}`

Copy `year` and `cites` from `literature/corpus.jsonl` unchanged. Code every source in the corpus. If
capacity runs low, code in file order and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts most reviews report fewer than half the practices. A review that genuinely reports all
  seven (a rigorous systematic review) is a real datum — code every `yes` the abstract earns.
- H2 predicts newer reviews report more practices. Do not inflate a recent review's practices or deflate
  an old one's; code the abstract in front of you.
