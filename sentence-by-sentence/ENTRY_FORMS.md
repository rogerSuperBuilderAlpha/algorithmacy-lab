# Entry forms

Three entry shapes, one per artifact. Each is markdown, numbered continuously, written by hand. The
shapes exist so a gap is visible and a skipped judgment is visible.

**Ids never move.** A model entry keeps its number for the life of the workspace. If a transcription
error splits or merges a sentence, correct it in place and record the correction under the entry;
never renumber, because every outline and ledger entry points here.

---

## `MODEL.md` — one entry per model sentence

Stage 2 writes the header and the quotation; Stage 3 writes the judgments beneath it.

```markdown
### C1.007 · S1 ¶1 · 30w

> "These cases demonstrate how ineffective boards can enable misconduct, allow strategic and
> financial risks to escalate unchecked, and erode stakeholder trust, ultimately resulting in
> significant reputational, financial, and societal harm."

- **Move** — CONSEQUENCE. *These cases demonstrate how* + a verb triplet + a trailing participle
  carrying the harm. The paragraph's four named cases are cashed here.
- **Paragraph role** — seventh of nine. Closes the problem run so the definition can land at C1.008.
- **Research question** — indirect. Builds the pressure the question answers; states no part of it.
- **Thesis** — supports. Ineffectiveness has consequences, which the reframing later explains.
- **Register** — verbs *demonstrate, enable, allow, escalate, erode, resulting*. `Erode` is the one
  figurative verb in the paragraph and it is a dead metaphor, not a reach. No aphorism, no aside.
- **Our slot** — what follows when position goes ungraded: remedies land on the interface, not the
  position.
```

**Rules.**

- `w` is a word count taken by eye, to the nearest few. It is context for the sentence's shape, not a
  measurement, and nothing is computed from it.
- The quotation is verbatim. An elision is marked `…` and never removes the construction the entry is
  about.
- **Move** names the job and the frame that performs it. A move with no frame is a label.
- **Register** names what kind of words this sentence uses. It is where the model's diction is
  collected sentence by sentence, so that by the end of Stage 3 the brief's register field is
  evidenced rather than asserted. **A register line that could describe any sentence is not a register
  line.**
- **Research question** and **Thesis** may be `none` — many sentences serve neither, and saying so is
  a judgment.
- **Our slot** is what our answering sentence must do. Stage 4 may overrule it.

**A run of consecutive sentences doing one job still gets one entry each.** Two entries with identical
text mean the run was summarised, not read.

---

## `OUTLINE.md` — one entry per planned sentence

Written at Stage 4, complete before any prose exists.

```markdown
### S-042 → answers C1.030 · S1 ¶5 · target ~40w

- **Move** — CONTRIB-METHOD, closing the contribution run. C1.030's shape: *Finally,* + the method +
  its lineage + its transferability.
- **Paragraph role** — last of five. Ends the introduction on the method, which the conclusion answers.
- **Owes the question** — nothing directly.
- **Owes the thesis** — commitment 5, that the standard can be applied.
- **Draft support** — L240 carries both lineage claims, both verified against source.
- **Register** — C1.030 is plain and literal: *introduces, combining, applied*. No figure. Write the
  claim afresh; do not carry the draft's phrasing across.
- **Watch** — C1.030 credits two predecessors by name. Ours must credit its own or say why not.
```

**Rules.**

- **Every model entry is answered or warranted.** An unanswered entry carries one line under its id
  saying why our paper does not make that move. Silence is how a partition loses an argument.
- Several of ours may answer one of the model's; one of ours may answer none, with a warrant.
- **Draft support** names where in the draft the claim lives. It is a pointer to a *claim*, never to
  a phrasing. An entry with no draft support is a claim the paper cannot make; write the refusal now.
- **Register** names what the counterpart's diction requires of ours, so Stage 5 writes rather than
  paraphrases.
- `target ~Nw` is guidance for shape, not a budget.

---

## `LEDGER.md` — one entry per written sentence

Stage 5 and 6 together. The sentence and its verdicts are one entry.

```markdown
### S-042 · answers C1.030

> Finally, I introduce a grading procedure that reports the reading depth behind every count,
> extending two methods this review draws on (Novelli & Pignataro, 2026; Hertel et al., 2026).

- **Form** ✅ ~35w against C1.030's ~41. Same order: *Finally,* + the method + lineage.
- **Construction** ✅ No matched-pair dash, no bare pro-form. One trailing gloss, his only dash form.
- **Register** ✅ Verbs *introduce, reports, extending, draws on* — all literal, all in his range.
  **`prints` was rejected**: the draft says *prints the reading depth*, which is figurative, and no
  verb in his abstract reaches like that. `reports` says the same thing plainly.
- **Value** ✅ Discharges thesis commitment 5 and opens the loop the conclusion closes.
- **Counterpart** ✅ C1.030 credits two predecessors; this credits two of ours.
- **Truth** ✅ Draft L240, both claims read at source. Credit sits where the draft puts it.
```

**Rules.**

- **A ✅ with no reason is not a verdict**, and **a register verdict that does not name a word is not
  a register verdict.** "Reads plainly" is an unwritten entry. Name the word you kept or the word you
  rejected, and why.
- **Three marks.** **✅** passes. **⚠️** passes with a departure written down — the counterpart's move
  is still performed and the entry says how it differs. **❌** rewrites before moving on, and the entry
  keeps both attempts. A run that never uses ⚠️ is either flawless or hiding departures inside ✅.
- **Weight beyond ±40% of the counterpart is ⚠️ at best, and never silent.** The section total against
  the venue's range is a separate gate that per-sentence warrants do not satisfy.
- **Truth** cites the draft location and confirms the credit. Where the draft does not support the
  claim, the verdict is `REFUSED` with what the draft actually says.
- A departure from the counterpart is not a failure if it is written down. **An unrecorded departure
  is.**

### The register verdict, in practice

Take each notable word and figure and ask whether the model does that. Notable means a verb that is
not literal, a noun doing metaphorical work, or a phrase that reaches. Ordinary words need no check.

The failure this is written against, from the first run of this skill:

| written | why it failed | rewritten |
|---|---|---|
| "leaves the grantor's power to withdraw it **unpriced**" | pricing is a metaphor; his verbs are literal | "rarely examines who can take it away" |
| "without the older tradition's **apparatus**" | reaching for a word; he writes *overlooks* | "overlooks the older literature" |
| "two operations have **shared a word**" | a riddle; he states things flat | "whether they describe one operation or two" |
| "courts and regulators **actually** read" | *actually* nudges the reader | "for coordination research and for practice" |

All four came from the draft, carried across because the sentence was paraphrased rather than written.
**That is what Stage 5's rule prevents and this axis catches.**

---

## Correcting a finished entry

Work discovered later appends under a dated sub-heading. It never overwrites.

```markdown
#### correction 2026-08-22
Stage 3 read C1.030 as a transferability claim only. It is also a lineage claim: it credits two
methods by name, which is why S-042 owed a credit and did not carry one until this correction.
```

The record of what was wrong is the only evidence that the reading improved.
