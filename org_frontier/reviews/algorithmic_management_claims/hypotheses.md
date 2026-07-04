# Hypotheses — what the algorithmic-management literature asserts versus tests

*Committed before any corpus is harvested or coded. The question: what does the algorithmic-management
literature assert versus test — the structure of its knowledge claims and its empirical grounding? Each
hypothesis names the knowledge claim it interrogates (in the knowledge-weaving typology of Simsek,
Heavey, Fox & Yu 2022), its operationalization, and the outcome that would support versus challenge it.*

This is a descriptive review of a literature's knowledge claims. It asks not whether algorithmic
management is good or bad but what kind of thing the field says, and on what evidentiary footing. The
claim-weaving lens treats a field's stylized facts, assumptions, critiques, and omissions as the objects
of study. The review measures three properties of the claim set: which outcomes it addresses, what
evidence it rests on, and whether its central proposition — that the algorithm controls workers — is
established or merely repeated.

## H1 — Outcomes skew to worker experience and control, not performance
- **Knowledge claim (stylized fact under test):** the field's attention concentrates on how workers
  experience algorithmic systems and on the control those systems exert, and largely bypasses whether
  algorithmic management improves productivity or firm performance.
- **Operationalization:** code each source's primary outcome — `control`, `worker_experience`,
  `performance`, `other` — and compare the shares.
- **Predicts:** `control` and `worker_experience` together are a large majority; `performance` is rare
  (a small single-digit-to-low-double-digit percentage).
- **Challenged if:** `performance` is a substantial share, or the control/experience pair is not a
  majority.

## H2 — Mostly qualitative or conceptual; quantitative causal evidence uncommon
- **Knowledge claim (key assumption under test):** the field advances largely through interviews, cases,
  and conceptual argument, with quantitative evidence — let alone causal quantitative evidence — a
  minority footing.
- **Operationalization:** code each source's evidence base — `conceptual`, `qualitative`,
  `quantitative`, `mixed` — and report the quantitative share (`quantitative` alone, and with `mixed`).
- **Predicts:** `conceptual` + `qualitative` is a majority; `quantitative` is a minority.
- **Challenged if:** `quantitative` (with or without `mixed`) is a plurality or more.

## H3 — "The algorithm controls workers" is a stylized fact: asserted widely, tested rarely
- **Knowledge claim (stylized fact under test):** the proposition that algorithmic management is a new
  form of control over workers functions as a stylized fact — a claim the field takes as established and
  repeats without fresh test. If so, the sources coded as `stylized_fact` should rest disproportionately
  on conceptual or qualitative evidence rather than quantitative.
- **Operationalization:** among sources coded `claim_type = stylized_fact` whose `outcome = control`,
  cross-tabulate `evidence`. Compare the quantitative share within that subset to the quantitative share
  of the whole corpus.
- **Predicts:** the control-stylized-fact subset is even more conceptual/qualitative than the corpus at
  large; its quantitative share is at or below the corpus rate.
- **Challenged if:** the control-stylized-fact sources are as quantitatively grounded as the rest, or
  the control claim is coded predominantly as tested (`quantitative`/`mixed`).

## Method fixed in advance
- Corpus boundary and search: `coding_protocol.md` and the corpus builder (semantic-search connectors,
  screened to algorithmic-management-of-workers sources).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`, coding title +
  abstract only.
- Reliability reported (Fleiss' κ per categorical variable). Any hypothesis the data contradict is
  reported as challenged.
