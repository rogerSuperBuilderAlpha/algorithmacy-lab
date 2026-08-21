---
name: sentence-by-sentence
description: Rebuild a manuscript sentence by sentence against a published model paper, by reading rather than measuring. Reads the model whole for its form and its diction, partitions it by transcription, analyses every model sentence for its move and what it owes the research question and thesis, builds an outline to the same depth, then writes and evaluates one sentence at a time. Requires a model paper and a draft. Use when a manuscript must be rebuilt to a model's form and register without losing what the draft established.
---

# sentence-by-sentence

Six stages after intake, run in order, on one model paper and one draft. Output is a new manuscript
composed against an outline, every sentence evaluated as it is written.

**Three sources, and confusing them is the failure mode.**

| source | supplies | never supplies |
|---|---|---|
| **the model** | form **and words** — its moves, its constructions, its diction | the claims |
| **the draft** | the claims, and nothing else | a single word of the prose |
| **the venue** | whether a trait is the model's own or the genre's | either of the above |

**There is no code in this skill and none may be added.** Nothing here counts, splits, diffs, scores
or gates. The stages produce numbered markdown, read and written by hand.

The skill exists because the pass it is named after did not happen. A manuscript was rewritten
"sentence by sentence" against *Academy of Management Annals* 20(2); seven scripts were built and
debugged, and the per-sentence judgment columns were empty in all 617 rows.

## The rule the whole thing rests on

**Every sentence is read by a reader and written by a writer. Nothing here is measured, because
measuring it is how it went undone.**

The defect that exposed that pass reached the abstract: *"It is not yet a form in the sense the other
three are…"* — an antecedent thirty-five words back, the referent not named until the sentence's last
four words, and a second sentence taking back what the first granted. The cohesion script scored it as
**linked**, because it opens with a pro-form and shares a content word with its predecessor. The
metric the pass was optimising endorsed the defect.

## The second rule, and it is the one that gets broken

**The draft supplies claims. It never supplies words. Words come from the model.**

The first run of this skill produced an abstract whose every mannered phrase had been imported
wholesale from the draft — *leaves the grantor's power to withdraw it **unpriced***, *without the
older tradition's **apparatus***, *two operations have **shared a word***, *the instruments courts and
regulators **actually** read*. Punctuation was checked against the model. Vocabulary was checked
against nothing. Eight sentences were marked **Style ✅** and not one of those verdicts had looked at a
word.

That model's abstract has no metaphor in it, and its verbs — *are reshaping, provide, focuses, lags,
overlooks, merge, develop, integrates, concludes* — are plain, every one. It repeats *board
effectiveness* seven times rather than reach for a variation. The full before-and-after is in
[`CHECKLIST.md`](CHECKLIST.md).

**A technical term is not register.** The paper's own constructs — its coinages, the things it names —
stay. What may not travel from the draft is the *manner*: metaphor, aphorism, elegant variation,
rhetorical nudges, a word reaching to sound clever.

**And there is a line inside "words come from the model."** Take its **frames, connectives and single
verbs** — `Conversely,`, `Few efforts have been made to`, `focuses narrowly on`, `overlooks`,
`In doing so, it (1)…`. Do not take its **distinctive predicates or its adjective pairs**: *incomplete
and siloed* is his verdict in his words, and lifting it whole imports his judgment instead of writing
yours. Five independent runs of this skill split on exactly this line, and four drew it here.

## The precedence rule

**Where the project's house style and the model's register conflict, the house style wins and the
departure is recorded.** The house style is the author's standing decision across all their work; the
model is one paper.

**Unless the venue is unanimous with the model.** Then it is a genre rule rather than one author's
habit, and the conflict goes to the author rather than being decided in the ledger.

All five runs hit this collision — the model's *"Few efforts have been made to merge…"* is an agentless
passive the house style bans outright — and none could find a rule for it.

## The third rule

**Read the model whole, and read the venue before calling anything a rule.** Rules taken from a
handful of sentences, or from one author's habit, do the most damage:

| what was claimed | what the essays do |
|---|---|
| "both his colons deliver a full clause" | sixteen of his twenty-two deliver an **enumerated list** |
| "the model never uses a matched-pair em-dash" | true of him; the venue runs **1–26 per paper** |
| "he opens 0 of 499 sentences on a bare pro-form" | true of him; the venue runs **2–9 per paper** |

**A trait the model alone has is his, not the genre's, and does not become a target.** The classified
table and the worked cases are in [`CHECKLIST.md`](CHECKLIST.md), including what to do when a genre
rule would discharge a credit and how to tell a corpus number from a result.

## Invocation

```
/sentence-by-sentence --model PATH --draft PATH --into DIR   # begin
/sentence-by-sentence DIR                                    # resume, or report where it stands
```

**Refuse to begin without both a model paper and a draft.** Name both in `MODEL_BRIEF.md`'s header.

Each stage below names its artifact and its completion test. What "done" looks like, and the failure
each stage is built against, are in [`STAGES.md`](STAGES.md).

## Stage 0 — intake

Confirm both files exist and are readable prose. Create the workspace:

```
MODEL_BRIEF.md    stage 1   question · thesis · contributions · skeleton · moves · REGISTER
MODEL.md          stage 2-3 one numbered entry per model sentence
OUR_BRIEF.md      stage 4   our question · thesis · contributions, same specification
OUTLINE.md        stage 4   one numbered entry per planned sentence
MANUSCRIPT.md     stage 5   the prose
LEDGER.md         stage 5-6 one entry per written sentence, with its verdicts
```

State the scale before starting. A 14,000-word model runs to roughly 500 sentences, a manuscript of
similar weight to about 600. **This is many sessions and none of it is parallel.**

## Stage 1 — read the model whole, and write the brief

Read the model end to end before writing anything. Then fill every field:

- **The research question**, quoted at *every* place it is stated, each located.
- **The thesis, and its shape** — not only the claim but the form of the claim.
- **The contribution moves**, in the order the paper makes them.
- **The section skeleton**: every section, its paragraph count, and their shapes.
- **The move vocabulary** — the recurring jobs its sentences do, named, read off this model.
- **The register** — see below. This field is not optional and the pass fails without it.

**Then read at least three of the venue's other papers** for every construction *and every register
trait* the brief is about to call a rule. Record the model's practice and the range across siblings. A
trait the model alone has is written down as the model's, and does not become a target.

Reading for both: [`CHECKLIST.md`](CHECKLIST.md).

### The register field

Six things, written from reading and evidenced by quotation, not by adjective: **its verbs** — list
thirty; **its metaphors**, if it has any; **what it does with its key term**, repeat or vary;
**its abstraction level**; **whether it names plainly or coins**; and **what it never does** —
aphorism, epigram, the knowing aside, `actually`. The method for each is in
[`CHECKLIST.md`](CHECKLIST.md).

## Stage 2 — partition the model, by transcription

Transcribe every sentence into `MODEL.md`, numbered continuously, with its section and paragraph.
Read in order. **Do not skip, do not group, do not summarise a run.**

Transcription is slower than splitting and that is the point: it is the only thing that guarantees the
model was read at sentence level, which is this stage's deliverable.

Entry shape: [`ENTRY_FORMS.md`](ENTRY_FORMS.md).

## Stage 3 — analyse every model sentence

For each entry: its **move**; its **role in its paragraph**; what it gives the **research question**;
what it gives the **thesis**; and the **slot** it sets for us.

**An entry that could have been written without reading the sentence is not an entry.**

## Stage 4 — our brief, then our outline

Write `OUR_BRIEF.md` to Stage 1's specification: our research question, our thesis and its shape, our
contribution moves. The paper's own argument is settled here, before any prose exists.

Then `OUTLINE.md`: one entry per planned sentence, naming the model entry it answers, its move, its
paragraph role, what it owes the question or thesis, and **where the draft supports it**.

**Every model entry is either answered or carries a written reason for having none.**

## Stage 5 — write, first sentence to last

Compose each sentence to its outline entry, in order.

**Take the claim from the draft and the words from the model.** Do not paraphrase the draft's
sentence; write the claim afresh in the model's register. A draft phrase that survives into the
manuscript survives because it is *also* how the model would say it, never because it was already
written.

A claim the draft does not support is refused, and the refusal is written into the ledger.

## Stage 6 — evaluate, before moving on

After each sentence, write its ledger entry: the sentence, then the verdicts.

| axis | the question |
|---|---|
| **form** | does it perform its counterpart's move, within ±40% of its weight? |
| **construction** | does it use a sentence shape the model and the venue avoid — **and does every pronoun in it have exactly one antecedent, named before it is used?** |
| **register** | **could its vocabulary appear in the model?** Take each notable word and figure and ask whether the model does that |
| **value** | does it deliver what the outline entry said it owed the question or the thesis? |
| **counterpart** | does it answer the model entry's job, or is a warrant written? |

Three marks, and they mean different things. **✅** passes. **⚠️** passes with a departure written
down. **❌** rewrites before moving on, and the entry keeps both attempts.

### Weight is guidance per sentence and a gate per section

A single sentence's counterpart is one data point, so ±40% is guidance and a warrant settles it. **The
section total against the venue's range is a gate**, because that range is seven papers rather than
one. A section that lands outside the venue's band is a defect, not a departure, and the warrants
written on its sentences do not add up to a warrant for the whole.

Five independent runs of this skill overshot the venue band by twenty percent, every one of them
passing every sentence with a written warrant. Weight was the only axis with no gate and it was the
only axis that failed unanimously.

Then the truth check, in three parts: **is this claim in the draft · does it credit whom the draft
credits · and where it is a number, does the draft print the same number everywhere?**

A compression can leave every claim intact and still move a credit — two authors merged into one
subject, a later paper's move given to an earlier one. Asking only whether the claim is present does
not catch it.

**A draft that contradicts itself about a number is a refusal, not a choice of which instance to
copy.** Two of five runs found the draft printing 697 appearances in one place and running the same
pass over 698 in another, and footnoting 26 demonstrations against a printed nineteen. One refused the
number and wrote why; the other copied the headline. The rule exists so that is not luck.

**Sentence N+1 is not begun until sentence N's entry is complete.** The format is the gate; there is
nothing to run. A verdict of ✅ with no reason is not a verdict, and **a register verdict that does not
name a word is not a register verdict.**

## Reporting where it stands

Completeness is read off the page, never asserted. Entry ids run unbroken; a gap is visible.

**Never report a stage complete without showing the entry range and the count.** The failure this
skill exists to prevent was a completion claim made over 617 empty cells.

## What this skill cannot do

- **It cannot choose the model.** Mirroring a badly-chosen exemplar faithfully still yields a bad
  paper, and the choice is the author's.
- **It cannot supply claims.** A thin draft yields a thin manuscript. The skill says so rather than
  invent, and the refusals are in the ledger.
- **It cannot be run quickly or in parallel.** Both are the failure mode, not the goal.
- **It cannot tell whether the argument is any good.** Whether the thesis is worth arguing is a
  judgment no procedure reaches, and the last gate is still the author reading the whole thing aloud.
