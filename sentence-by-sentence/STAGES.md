# Stages — what each produces, and what done looks like

Seven stages counting intake. Each names its artifact, its completion test, and the failure it is
built against. **A stage is not begun until the one before it is done**, and done means the page shows
it, not that the session says so.

Completion is checked by reading. There is no command.

---

## Stage 0 — intake

**Produces:** the workspace, and `MODEL_BRIEF.md`'s header.

Record both inputs by path, and the draft's git SHA if it has one. State the model's length and the
sentence count it implies, so the scale is known before the first entry.

**Done when:** both files are named and both open. **Refuse otherwise.** A model with no draft has no
claims and Stage 5 cannot run; a draft with no model has neither form nor register and Stages 1–3
cannot run.

---

## Stage 1 — the model brief

**Produces:** `MODEL_BRIEF.md`, complete.

| field | what it holds |
|---|---|
| research question | every statement of it, quoted, each located |
| thesis | the claim, and the *shape* of the claim |
| contribution moves | in the order the paper makes them |
| section skeleton | every section: paragraph count, and the shape of those paragraphs |
| move vocabulary | the recurring jobs its sentences do, named, read off this model |
| **register** | its verbs, its metaphors, what it does with its key term, its abstraction level, what it never does |
| constructions | per construction: the model's practice, the venue's range, the alternative |

**Done when:** no field is empty; every research-question statement carries a location; the register
field lists actual verbs from the model rather than adjectives about them; and every construction and
register row carries a venue range beside the model's practice — not the model's alone.

**Built against two failures.**

*Rules taken from one author and called venue law.* Three of four were, and the venue-range column is
the fix.

*A brief with no register field at all.* The first run of this skill had none, so Stage 5 took its
words from the draft and Stage 6 checked punctuation. Every mannered phrase in the output —
*unpriced*, *apparatus*, *shared a word*, *actually read* — came across untouched. **The register
field is what gives Stage 6 something to check against.**

**Do not skip the section skeleton.** Paragraph counts and shapes are what Stage 4 budgets against.

---

## Stage 2 — the model partition

**Produces:** `MODEL.md`, header and quotation for every sentence.

Transcribe in order, numbered continuously, each entry carrying section and paragraph.

**Done when:** ids run unbroken from first sentence to last, and per-section counts agree with Stage
1's skeleton. A section holding twelve entries where the skeleton says thirty is the test failing, and
it is visible on the page.

**Built against:** a generated index nobody reads. The failed pass produced one, joined it, reconciled
four errors in it, and never read it end to end — leaving 71% of the model unread at sentence level.

---

## Stage 3 — the model analysis

**Produces:** six judgments under every entry — move, paragraph role, research question, thesis,
**register**, our slot.

**Done when:** every entry carries all six, **and no two entries carry the same text.** Identical
judgments across consecutive entries mean a run was summarised rather than read.

**Built against:** analysis at run level passed off as analysis at sentence level.

The register line is where the model's diction is collected sentence by sentence, so that Stage 1's
register field ends the stage **evidenced rather than asserted**. By the last entry you should be able
to say what the model's verbs are like without opening it again.

`none` is legitimate for research question and thesis, and common. Writing `none` is a judgment;
leaving the field blank is not.

---

## Stage 4 — our brief, then our outline

**Produces:** `OUR_BRIEF.md` to Stage 1's specification, then `OUTLINE.md`.

Write the brief first. This is where the paper's own argument is settled — the question, the thesis,
the contributions — before any prose exists.

Then one outline entry per planned sentence: the model entry it answers, its move, its paragraph role,
what it owes the question or thesis, **where the draft supports it**, and **what its counterpart's
register requires**.

**Done when:** every model entry is either answered or carries a written reason for having none, and
every outline entry names its draft support or records a refusal.

**Built against:** an outline written during composition, which is a rationalisation of prose that
already exists. And against silent omission — a model entry with no answer and no reason is how a
partition loses an argument, which is how a paper's central intellectual debt was deleted.

**Draft support points at a claim, never at a phrasing.** An outline entry that quotes the draft's
sentence has already decided Stage 5's words, and that is the whole defect.

---

## Stage 5 — writing

**Produces:** `MANUSCRIPT.md`, and the sentence half of each `LEDGER.md` entry.

Compose to the outline, first sentence to last, in order.

**Take the claim from the draft and the words from the model.** Write the claim afresh in the model's
register; do not paraphrase the draft's sentence. A draft phrase surviving into the manuscript
survives because it is *also* how the model would say it — never because it was already written.

A claim the draft does not support is refused. Write the refusal into the ledger and amend the outline
entry; do not compose around it.

**Done when:** every outline entry has a written sentence, and `MANUSCRIPT.md` reads in the outline's
order.

**Built against two failures.** *Composing against a form-only partition*, which invents claims —
three opening sentences in the failed project conformed to the model's shape and asserted things the
paper does not hold. And *paraphrasing the draft*, which imports its register wholesale: the first run
of this skill changed punctuation, moved a number, restated one finding, and left the vocabulary
entirely the draft's.

---

## Stage 6 — evaluation

**Produces:** six judgments under every written sentence.

| axis | reads | fails when |
|---|---|---|
| form | the counterpart entry and the move vocabulary | it does not perform the move, or sits beyond ±40% of its weight without a warrant |
| construction | the brief's construction rows | it uses a shape the model **and** the venue avoid, or a pronoun in it has no antecedent or more than one |
| **register** | the brief's register field | a word or figure in it could not appear in the model |
| value | `OUR_BRIEF.md` and the outline entry | it does not deliver what the entry said it owed |
| counterpart | the model entry's job | the job is unanswered and no warrant is written |
| truth | the draft | the claim is not in the draft, the credit has moved, or the draft prints the number differently elsewhere |

**Done when:** every written sentence carries six judgments, each with its own reason; **every register
verdict names a word** — one kept, or one rejected, and why; and **the section's total weight sits
inside the venue's range**.

That last is a gate and the per-sentence warrants do not satisfy it. Five runs passed every sentence
with a warrant and every one of them finished twenty percent above the whole venue.

**Sentence N+1 is not begun until sentence N's entry is complete.** The format is the gate.

**Built against:** 617 empty judgment cells behind a completion claim, and then eight **Style ✅**
verdicts that were true about punctuation and silent about every word on the page.

---

## Running on part of a paper

A scoped run — one section, one abstract — is legitimate and the skill's ordering does not survive it
intact. Three rules make it honest rather than a pretence.

**Register is read from the whole model regardless of scope.** It cannot be read off eight sentences,
and a register field asserted from a fragment is the "rules from a handful of sentences" failure the
third rule names. Read the model's abstract, its introduction, its methodology and enough body to
have seen fifty of its verbs, whatever the scope of what you transcribe. Say in the brief what you
read and what you did not.

**Stage 2's count test uses the scoped unit's own sentence count**, since a section skeleton does not
apply below a section.

**Stage 4's safeguard stops working and you must say so.** At 8-to-8 the "every model entry is
answered or warranted" test is satisfied trivially and catches nothing — the artifact built to stop
an argument going missing does no work at that scale. Write that in the brief rather than reporting a
green stage.

## Reporting

State the entry range and the count. `MODEL.md` S3: entries C4.001–C4.087, 87 of 87. Never a
percentage, never a summary adjective, never "complete" without the numbers beside it.

When a stage is partly done, say which entries are done and which are not. Numbered entries make this
cost nothing to say truthfully.

---

## Working across sessions

The artifacts hold everything; nothing is carried in a session. Resuming means opening `MODEL.md` or
`LEDGER.md`, finding the last id, and continuing at the next.

Work in runs that end on a section boundary where possible, so Stage 2's count test applies to what
was just done. A run ending mid-section needs no marker — the last id is the marker.
