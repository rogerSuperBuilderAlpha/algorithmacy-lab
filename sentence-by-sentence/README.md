# sentence-by-sentence

A writing skill for [Claude Code](https://claude.com/claude-code). It rebuilds a manuscript one
sentence at a time against a published model paper, by reading rather than by measuring.

**It requires two things and refuses to start without both: a model paper, and a draft.** The model
supplies form and words. The draft supplies claims, and nothing else.

There is no code in it. Nothing counts, splits, diffs, scores or gates. The four files are the whole
skill.

## Why it works this way

The skill was built after a pass that failed, and the failure is the reason for every rule in it.

A manuscript was rewritten "sentence by sentence" against one exemplar. Seven scripts were built and
debugged, five defects were found *in the instruments*, and unhooked paragraph joins improved from
51.2% to 21.5%. The per-sentence judgment columns were empty in all 617 rows. The work was reading
614 sentences and writing 614 sentences, and it never happened, because there was always a number to
move instead.

The defect that exposed it reached the abstract, and a cohesion script had scored that very sentence
as **good** — it opened with a pro-form and shared a content word with its predecessor, which is what
the metric rewards. The measurement did not miss the defect. It endorsed it.

Three further rules came from things that went wrong afterwards:

- **Words come from the model, never the draft.** A first run of the skill produced an abstract whose
  every mannered phrase had been imported wholesale from the draft while only the punctuation was
  checked against the model. Eight sentences were marked *style ✅* and not one of those verdicts had
  looked at a word.
- **Read the venue before calling anything a rule.** Three rules taken from one author's habit, or
  from two sentences in one section, did more damage than the scripts. A trait the model alone has is
  his, and does not become a target.
- **Weight is a gate at the section, not the sentence.** Five independent runs of this skill overshot
  the venue's range by twenty percent, each of them passing every individual sentence with a written
  warrant.

## The files

| file | what it holds |
|---|---|
| [`SKILL.md`](SKILL.md) | the contract — three sources, the rules, seven stages, the refusals |
| [`STAGES.md`](STAGES.md) | what each stage produces, what done looks like, what it was built against |
| [`ENTRY_FORMS.md`](ENTRY_FORMS.md) | the three entry shapes: a model entry, an outline entry, a written entry |
| [`CHECKLIST.md`](CHECKLIST.md) | reading for register, then for constructions |

## Installing it

Copy the directory to where Claude Code looks for skills — `~/.claude/skills/` for every project, or
`<project>/.claude/skills/` for one:

```
cp -r sentence-by-sentence ~/.claude/skills/
```

That is the whole installation. There is no manifest to register and nothing to build.

## Running it

```
/sentence-by-sentence --model PATH --draft PATH --into DIR   # begin
/sentence-by-sentence DIR                                    # resume, or report where it stands
```

It produces a workspace of numbered markdown — a brief on the model, one entry per model sentence, an
outline written before any prose exists, the manuscript, and a ledger carrying six verdicts on every
sentence written.

**It is slow, and it does not parallelise.** A 14,000-word model runs to roughly 500 sentences and a
manuscript of similar weight to about 600, each of which is read, analysed, written and judged by
hand. Any version of it that finishes quickly has skipped the reading, which is the failure it exists
to prevent.

## What it cannot do

- **Choose the model.** Mirroring a badly-chosen exemplar faithfully still yields a bad paper.
- **Supply claims.** A thin draft yields a thin manuscript; the skill says so rather than invent, and
  the refusals go in the ledger.
- **Tell whether the argument is any good.** Whether the thesis is worth arguing is a judgment no
  procedure reaches, and the last gate is still a person reading the whole thing aloud.

## Provenance

Built in this lab against *Academy of Management Annals* 20(2), and every number quoted above is from
that work. The rules were then tested by running the skill five times, in five independent contexts,
on the same model and the same draft. Four of the five rebuilt the model's opening sentence frame
unprompted; all five overshot on length; all five collided with the same three unstated rules, which
are now stated.

That test also found that the skill's own worked examples had contaminated it — five runs
unanimously rejected the six phrases the checklist names, which measured compliance rather than
reading. Those examples are now marked as spent, and the file says a hit on them does not count.

MIT licensed, with the rest of the lab.
