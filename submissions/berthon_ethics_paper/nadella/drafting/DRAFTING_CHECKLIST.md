# Drafting checklist for DRAFT_v2 (BEQ)

*Written by Claude (Opus 5.5), 19 Nov 2026, as a working tool for drafting, not paper prose. It merges four sources:
`AI_TICS_2026.md` (the evidence on AI-writing tics, with sources), `~/.claude/writing-style.md`, the repo
`CLAUDE.md`, and `../rebuild/MODEL_BRIEF.md` (C1–C20, Diamantis). Where they conflict, the author's rules win and the
conflict is recorded in §6. The author asked for prose that is clear, direct and accessible: a serious academic
essay, not marketing or a blog.*

## 1. The reader

Write for a business-ethics scholar who has not read Nadella's essay, Graff on literacy, Pettit on domination, or
the history in §3. That reader is intelligent and busy. Every sentence should be one they can follow on first
reading.

- **Define every term in plain words at first use, then keep it fixed.** Examples: *algorithmacy*; *deployer* ("the
  organisation that puts an agent to work"); *agent* (software that takes actions, not only answers); *envelope*
  ("the declared limits on what an agent may do"); *non-domination*; the *Requerimiento*. Do not vary a defined term
  for elegance (tics rule 21).
- **Introduce every person and text in a clause** at first mention: who they were and why they matter ("Bartolomé de
  las Casas, a Dominican friar who served in the Indies, ...").
- **Expand every acronym** at first use (the European Union's Artificial Intelligence Act; the General Data
  Protection Regulation, GDPR). Use an acronym only if it recurs.
- **One concrete case before any abstraction is used a second time.** The refund, the loan applicant, the voter at
  the registrar's desk.
- **Plain verbs.** *Show, keep, hold, refuse, read, pay.* Not *underscore, leverage, foster, navigate, showcase*.
- **At most one technical term introduced per sentence.**

## 2. Distribution gate (measured per section; edits by hand)

Measured with `~/.claude/skills/draft/engine/report.py --register beq`. The BEQ corpus figures are from
`registers/beq/targets.json`. The low-variance profile is the best-supported AI tell (tics rule 27); the mean is not.

| Measure | BEQ corpus | Our gate | Why |
|---|---|---|---|
| Words per sentence | 31.1 ± 4.7 | **25–30** | Lower edge, for accessibility |
| Sentence-length CV | 0.56 ± 0.16 | **≥ 0.55** | Variance is the main tell |
| Share of sentences > 40 words | 23% | **≤ 20%** | Accessibility |
| Share of sentences < 10 words | 6.4% | **5–10%** | Turns and verdicts only (C5) |
| Em-dashes per 1,000 words | 4.2 (0.5–12.6) | **2–6** | Glosses and turns only (C6–C7) |
| Words per paragraph | 246 ± 49 | **120–330, varied** | No run of same-length paragraphs |
| Same first word | — | **never 3 sentences in a row** | Repeated openers |

## 3. Avoid (no academic function; evidence ties them to LLM output)

- **Puff words:** delve, showcase, intricate, meticulous, tapestry, realm, landscape (figurative), testament, pivotal,
  vital, groundbreaking, vibrant, profound, renowned, garner, commendable, multifaceted, navigate (figurative),
  foster, underscore, boast.
- **Stock frames:** "it is important to note that", "plays a crucial role in", "serves as / stands as" for *is*,
  "in today's world", "a testament to".
- **Emphasis openers (repo ban):** Crucially, Importantly, Notably, Precisely, Note that, Stated plainly, To be
  clear, It is worth, We want to.
- **Didactic disclaimers and outlook endings:** "It is important to remember…", "Despite these challenges, X
  continues to…".
- **Vague attribution:** "scholars argue", "critics note", "research shows". Name the person, give the page.
- **Clichés and purple prose; redundant exposition** (saying what the reader can infer).
- **The abstract noun + agentless passive opener** ("It has been shown", "The form has been mapped"). This is the
  author's rule; see §6.
- **Self-commentary on rigour** (house rule 4): no sentence about the paper's care, candour or organising choices.

## 4. Inspect each hit (legitimate in the genre; a tell only in excess or when empty)

- **Present-participle tails** (", highlighting…", ", underscoring…", ", reflecting…"): replace with a finite clause
  and a named agent, unless the participle is plain subordination.
- **"Not X but Y" / "X rather than Y":** keep only when a named person holds X; otherwise state Y.
- **Triads:** keep only when every member is argued for.
- **Nominalisation runs** (*the implementation of the allocation of…*): give the verb back to its agent; in an ethics
  paper responsibility attaches to agents.
- **Em-dashes:** gloss or turn only; vary with commas, parentheses, colons.
- **Paragraph-final restatement:** end on the last new move or a hook to the next paragraph (cohesion 6).
- **High-density academic words** (*potential, insights, comprehensive, particularly, within, across, enhance*):
  keep where they do work; watch the density.
- **Metacommentary:** one roadmap, first-person method statements only ("I argue", "I define").
- **Hedges:** once, at the claim that needs it. Do not strip all hedging (LLMs under-hedge).

## 5. Keep (human markers the evidence and the venue support)

- First person for the paper's own moves (C1): *I argue, I call, I read*; never to carry a claim.
- Plain causal *because*; *be* as the main verb; finite clauses; analytic negation where it is the claim.
- Relation connectives as the logic needs (*However, But, Yet, Thus, For example, In addition*).
- The eight cohesion mechanisms (repo CLAUDE.md): tail-head linkage, end-focus, renaming the thread entity, glossing a
  term in the same breath, reformulation, forward and backward hooks, grouping parallel evidence.
- Short sentences as turns and verdicts (C5), not decoration.
- Opponents' own words in short quoted fragments, then turned (C14).

## 6. Conflicts recorded

1. **Agentless passives.** Reinhart et al. (2025, SI Tables S5–S6) find GPT-4o uses agentless passives at about half
   the human rate, so a passive is not an AI tell. The author's rule targets one construction, the abstract noun plus
   agentless passive as a sentence opener, on grounds of clarity and responsibility. **Kept as the author wrote it**;
   other passives are allowed where the agent is unknown or unimportant.
2. **Connectives.** The repo retired the ban on *Moreover / Furthermore*; the evidence does not support counting
   connectives as a tell (Bao et al. 2025; Reinhart et al. 2025). **Relation connectives allowed**; repeated
   openers are still checked (§2).
3. **Em-dashes.** Wikipedia's guide dates em-dash overuse as a model-specific tell; the repo says do not ration
   below about 3 per 1,000 words. **Gate set at 2–6 per 1,000**, glosses and turns only.
4. **Sentence length.** BEQ averages 31 words; the author asked for accessible prose. **Gate at 25–30**, with the
   variance kept high.

## 7. Truth rules

- Every quotation from a card or a review note with its locator; literacy-review quotations still unverified are
  checked against the PDF before the draft is finished.
- STRUCTURE v5 items marked [hypothesis] are written as open questions or left out, never asserted.
- The author's 04/05 wording is quoted verbatim and marked as his.
- Write "restriction", not "ban", for Ottoman printing; give contested claims both sides (Report §"Five claims").
- No motive is imputed to Nadella or Microsoft.

## 8. Process

Draft in order, section by section, against the model (sentence-by-sentence skill). After each section: run the
report, fix each hit by hand, check the section length against its band, commit and push. One self-check only; no
AI-review → AI-rewrite loop. The author's read-aloud is the last gate. BEQ requires the submission to declare any
AI-generated text.
