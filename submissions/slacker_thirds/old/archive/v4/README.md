# v4 — the rebuild

Opened 2026-08-10 on the author's instruction: a full redo rather than another revision,
and a fresh starting point to prune and perfect from.

Nothing under `chapter/` or `research/` is modified by this work. v3 stays where it is as
the reference record, and `chapter/archive/` keeps v1 and v2. What changes is the process.

## Why a rebuild rather than a fifth revision

The chapter is not short of effort. It has four review rounds, seven per-section research
dossiers, a full dialogue transcript, a scene inventory, and a catalogue of about fifty
caught factual errors. It is short of a *process that converges*, and the repo's own review
record says why: verification, argument review, and prose review were the same activity,
performed by the same eleven-lens panel, on the same artifact, over and over.

Four things followed from that, all documented in `reviews/`:

- **Tics regrew.** "The chapter revises compulsively and the drumbeat came back — and it
  came back hardest in exactly the paragraphs the panel never saw… Every new addition
  auditioned."
- **Fixes installed new faults.** One proposed repair was declined because "the proposed
  fix adds an agentless passive — the disease as cure." A banned throat-clear was replaced
  by a different throat-clear.
- **Later panels overturned earlier panels' clearances.** Sentences one round protected as
  register, the next round removed as metaphor doing argumentative work.
- **An upstream gloss propagated unread.** A research verdict recorded in `outline_v3.md`
  ("an ally, not a rival") survived every downstream pass and produced a fatal error,
  because each pass read the outline rather than the source.

Three architectural objections were re-raised across three rounds and answered by hedging.
The rebuild treats them as entry criteria instead.

## The design

Five bets, each one a mechanism rather than an intention.

1. **No compression phase.** v3 drafted 6,152 words and compressed to 5,408; that is where
   the film got deleted. v4 drafts each section at its budget.
2. **Facts are verified claim-against-source, never claim-against-project-file.** Verifiers
   see the sentence and the citation and nothing else.
3. **The argument is adjudicated on the outline; the prose is judged once, at the end.**
4. **Every anti-regrowth control is a script.** See `tools/` below. Panels forget; regexes
   do not.
5. **The author's read-aloud is terminal.** After it, the only permitted machine edits are
   deletions and sourced factual corrections. A deletion cannot install a construction.

## Layout

```
v4/
  ASSUMPTIONS.md        every unconfirmed premise, and what breaks if it is wrong
  factbase/
    CLAIMS.md           one row per verified fact, with a provenance class A-D
    GLOSSES.md          prior interpretations, quarantined -- consult, never cite
    BANNED_FACTS.md     the fifty caught errors, so none is walked back into
    scene_ledger.md     the film's 35 dialogue segments, and what each can carry
    film_lexicon.txt    the terms check_film.py counts as the film being present
  extract/              per-dossier extraction, merged into factbase/
  rederivation/
    OBJECTIONS.md       the standing objections, verbatim, as entry criteria
    CANDIDATE_A/B/C.md  three frames -- two written blind to v3, one defending it
    DIVERGENCE.md       what each candidate keeps and drops, and what it answers
  outline_v4.md         sections, budgets summing to 5,000, assigned scenes
  disc_worksheet.md     what one afternoon with the Criterion disc would settle
  verification/         phase 5 results and the diff ledger
  tools/                the mechanical gate
```

## The gate

```
python3 v4/tools/run_gate.py chapter/chapter_v4.md
```

Runs five checks and reports each. It is meant to run after every applied fix, not once at
the end.

| check | what it proves | script |
|---|---|---|
| apparatus | notes and bibliography reconcile both ways, no placeholders | `check_apparatus.py` (existing) |
| carryover | no 8-word sequence shared with v1, v2, v3, or v3_long, outside quotations and the apparatus | `v4/tools/check_carryover.py` |
| bans | no construction a previous panel already cut; rate tells against the panels' own measured budgets | `v4/tools/check_bans.py` |
| film | ≥12 scenes engaged, every section reaching the film within 120 words, no filmless run over 250 | `v4/tools/check_film.py` |
| ceiling + disc | body within the limit; no unresolved `[DISC:…]` markers | `run_gate.py` |

**Baseline, measured against v3 on 2026-08-10.** The instruments reproduce the panels'
own findings independently, which is the reason to trust them on v4:

- bans: 35 percent of paragraphs end on a sentence of 13 words or fewer, against a 25
  percent threshold — the metronome the August editor counted by hand. Pseudo-clefts at
  1.58 per thousand. Two constructions flagged in the August bans round are still present.
- film: 7 of 35 scenes engaged; §5 does not reach the film until word 141; the longest
  filmless run is 218 words. This is the complaint every editor lens raised in every round,
  in numbers.

The scripts report locators and rates. They do not issue verdicts — that judgment is the
author's, and it arrives at the read-aloud.

## Register

The calibrated `slacker` register in `~/.claude/skills/draft/registers/slacker/` (42
single-author critical essays from four open-access film collections, 250,772 words),
under `~/.claude/writing-style.md`. **The outer repo's no-first-person rule does not apply
to this chapter.** First person, contractions, em-dashes used as beats, and pointed
concessions are protected: eleven reviewers across two panels raised zero register
complaints, and five named the concessions the chapter's best feature.
