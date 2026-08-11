# Slop pass v6 — instrumented locator repair

Date: 2026-08-11. Target: `chapter/chapter_v6.md`.
Method: edit by locator from `run_gate` / `check_bans` / draft `report.py --register slacker`;
do not regenerate sections. Model: `v4/prose_pass/SLOP_PASS_2.md`.

## Baseline (pre-edit)

```
python3 v4/tools/run_gate.py chapter/chapter_v6.md --allow-disc
python3 v4/tools/check_bans.py chapter/chapter_v6.md
python3 ~/.claude/skills/draft/engine/report.py --paper chapter/chapter_v6.md --register slacker
```

| instrument | result |
|---|---|
| apparatus | PASS (33 notes, 16 bib) |
| carryover | PASS |
| bans verbatim | none |
| landing lines | 10/41 = 24% (threshold 25%) ok |
| rather than | **1.31/1k OVER budget 1.20** (6 hits) |
| antithesis / agentless / enumerator | ok |
| punctuation | emdash 0.2, colon 8.8 (z=+2.0), semicolon 2.0 — all under corpus max |
| film | PASS (13 scenes, max gap 190) |
| ceiling | 4564 ≤ 5000 |
| disc | 7 markers deferred (`--allow-disc`) |
| **G4** | **PASS** (bans quiet-mode still reports rate over) |
| draft Tier 3 | **BREACH** parallel staccato 1.08 vs floor 0.34 (5 hits; several FP dialogue) |
| draft cohesion | drumbeat "man" (~sent 43); drumbeat "film" (~sent 192 / §8); 75% para joins no shared entity |

### `rather than` locators (check_bans)

| para@ | snippet | load-bearing? |
|---|---|---|
| 17 | community rather than a crowd | yes (Royce) |
| 35 | Slack rather than cheapness | yes (argument) |
| 59 | body rather than in a reply to a referee | **decorative meta** — cut |
| 71 | *mine* rather than merely true of me | yes (loyalty) |
| 77 | against the third rather than through it | yes (contrast) |
| 85 | independent sources rather than in the Constitution | yes (doctrine) |

Cutting one decorative hit: 6 → 5 → ~1.10/1k under budget.

### Parallel staccato (draft; keep dialogue FPs)

1. `That makes perfect sense. | The street supplied the opening twice. | It arranged nothing.` — merge last two.
2–4. Film dialogue stacks — leave (documented FP: terse dialogue).

### Drumbeats

- §2 Gary join: "man" ×3 in consecutive short sentences → rename two.
- §8: "film" unvaried across consecutive sentences → rename to *Slacker* / "it" / "this material" where the referent is clear.

### Sense (minimal, already flagged)

- §4: "addressed with no addressee" → clearer without installing antithesis machine.

## Edit ledger

### §2 — man drumbeat + staccato landings
- "The asker asked one man. Another man answered." → "The asker asked one stranger. Someone else answered."
- "The street supplied the opening twice. It arranged nothing." → "The street supplied the opening twice and arranged nothing." (kills non-dialogue staccato triplet with the Schegloff courtesy quote)

### §4 — sense
- "Segments 33 and 34 are addressed with no addressee:" → "Segments 33 and 34 speak with no one there to hear:"

### §5 — rather than (decorative)
- "belongs in the body rather than in a reply to a referee" → "belongs in the body. Leaving it for a reply to a referee would leave the concession half-made."

### §8 — film drumbeat
- Opened on "*Slacker* does not…"; "reading the film" → "reading the picture"; "Call the film pre-qualitative material" → "Call that material pre-qualitative"; "the film is the control case" → "*Slacker* is the control case"; "inside the film" → "inside the picture"; "what this film is good for" → "what this material is good for"; "the film's last talkers" → "its last talkers."
- Left "Aware… the film names" once (needed noun for the rename chain).

## Post-edit instruments

| instrument | result |
|---|---|
| rather than | **1.10/1k** (budget 1.20) ok |
| all other rate tells | ok |
| verbatim bans | none |
| landing lines | 24% ok |
| G4 | **PASS** |
| draft parallel staccato | 0.87/1k still BREACH — **remaining 4 hits are film dialogue / door speech** (documented FP) |
| drumbeats man/film | cleared from findings |
| slop_trends structural scan | 0 hits (not just/not only; not X but Y; serves as; trailing participles; canned closers; vague attribution) |

Stop condition met: bans rates inside panel budgets; apparatus, carryover, film, ceiling pass. No further regenerate.

## Clarity pass (author direction 2026-08-11)

Author: cut cute scaffolding; write claims straight. Not a section regenerate — same argument and apparatus; delete throat-clears and fake counts.

Cuts / straightenings include:
- "Sociology has four answers…" deleted; open on Simmel
- "film changes its mind" → "who does the joining changes"
- "worth stating because they do not explain this" → named as questions that do not explain the migration
- referee-concession meta deleted; keep the selection/pricing claim
- "Two things follow, and the second is the useful one" → "Two limits follow"
- "One gate refused them" deleted
- "Aware, then… Unaware in that…" restated as plain aware/unaware sentences
- carryover: restored "Slack rather than cheapness is what it had" (v3 shingle)

G4 PASS after carryover fix. DOCX refreshed.

## Sentence-defense pass (author direction 2026-08-11)

Rule: keep only if the sentence is evidence, a definition, a necessary hinge, or a claim the surrounding paragraph actually uses. Else cut or rewrite.

Failed defense → cut/rewrite (representative):
| was | why failed | action |
|---|---|---|
| audiences follow it without much trouble | unsupported soft claim | folded into "usual account" hinge |
| Every published account… says the same thing | overclaim | → "The usual account…" |
| A sidewalk knows nobody | cute personification | → "A sidewalk has no parties" |
| both cost the argument something | empty meta | cut |
| this film's talkers know it | mind-reading | cut |
| What the count actually shows is simpler | throat-clear | cut |
| material conditions were ordinary | "ordinary" does no work | cut |
| What the six share is concrete | throat-clear | cut |
| Two questions… do not explain… Neither… is what changed | circular | → constant-while-migrating rewrite |
| Nobody… is devoted to anything | overclaim | → "do not show devotion to a calling" + evidence |
| sixty years before the cases below | dangling referent | cut the temporal flourish |
| Reich carries… that far, and no further | cute | → "Reich stops there" |
| film is aware / unaware | personifies the heading | → names / has no concept |
| an instrument that arrives blind and works anyway | unclear referent | → stamp demonstrated on a wrist |
| their not needing it is the finding | restates next claim | cut |
| unusual purity | booster | cut |

Kept on defense: Simmel figures + deferral; taxi/accident join; Royce memory/triad + limits; Gary overheard join; Schegloff summons cost; work/exchange census; housing slack vs rent; Erickson/Long; joining census thirds; four capacities at the door; Amazon/drivers; Stark & Pais; Reich grant vs stamp; FX venues for rules-not-structure; algorithmacy boundary; closing eviction.

G4 PASS after this pass; DOCX refreshed.
