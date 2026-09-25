# Triadic reduction — the talk

**Status.** Claim locked 2026-09-24. **v4, 2026-09-25:** the deck is now 23 slides (`talk/deck.pptx`, built from `talk/deck.md`). Slides 1–15 are the author's own deck, design removed, pictures, diagram and table kept; slides 16–22 are new — three findings from the lab, two invitations to fork the repository, and a live session with its fallback; slide 23 is Image Sources, moved from 16. The script (`talk/script.md`) is 3,314 spoken words, 25.5 minutes at 130 words a minute, against a 30-minute slot (`talk/check_talk.py`); the 30-minute slot is requested, not confirmed — the venue's confirmed slot is 20 minutes. Open questions on the new text are in [`AUTHOR_TASKS.md`](AUTHOR_TASKS.md); the author's timed read-aloud, with the live demo clocked separately, is next.
**Venue.** ALGOCON, the algorithmacy.org conference, Port of Spain, 28–31 October 2026. Slot: 20 minutes confirmed, 30 minutes requested.
**Deliverables.** A black-and-white slide deck (`.pptx` built from Markdown: black text on white, the author's two portraits, the valency diagram and one plain table, nothing else), a talk script, and a live-session runbook (`talk/LIVE_SESSION.md`) for building and running an audience member's coordination scenario during the talk.

The talk makes one argument. Literacy is a dyadic competence and algorithmacy a triadic one. If every
triad reduces to dyads, algorithmacy is literacy applied twice and names nothing new. If some triads do
not reduce, algorithmacy has a target of its own. The talk argues the second case from the ground up:
Peirce's logical argument that genuine triads cannot be built from pairs, Simmel's sociology of the third,
Quine's 1954 reduction of every predicate to one dyadic predicate, the logicians who answered him, and
the lab's own move, which uses integrated information (IIT 4.0) to separate a relation that binds three
parties from a system that merely does not factor.

**Triad criterion (fixed 2026-09-24).** An irreducible triad here is a party jointly determined by two
others inside a system that does not factor. Φ > 0 alone is not the test: the lab's own results give
Φ = 2.0 for a mutual dyad and for a ring of one-input copies.

## Ground rules

1. Everything under `sources/` is preliminary. The Gemini chats, the Gem's source documents and the
   pasted Gemini script are process, not citable sources. A claim from them enters the talk only through
   the claims register and a verified card in `library/cards/`.
2. Quote Peirce, Simmel, Quine and the logicians from the primary text, with the edition named.
3. Every number on a slide or in the script appears verbatim in a lab `results/` file and in
   `ci/reproduce.json`, as in [`../triad_thinkers/`](../triad_thinkers/). The talk borrows lab results;
   it does not re-run Φ.
4. State the scope once: the lab's results are about small Boolean models, not about people.
5. Nothing here is sent, posted or submitted by an agent.

## Files

| Path | Use |
| --- | --- |
| [`SOURCE.md`](SOURCE.md) | Provenance of every input, what each covers, and what is still missing |
| [`sources/`](sources/) | Verbatim captures: Gemini share pages (G1–G7), Drive documents (D-series), the pasted Gemini script (P1) |
| [`sources/MANIFEST.md`](sources/MANIFEST.md) | How each capture was made and checked, with hashes |
| [`sources/capture_gemini_share.py`](sources/capture_gemini_share.py) | Re-captures a Gemini share page as Markdown |
| [`CLAIM.md`](CLAIM.md) | The claim lock: title, question, the one thesis, what it licenses, what not to claim, open decisions — **draft, awaiting the author** |
| [`ARGUMENT.md`](ARGUMENT.md) | The premise-by-premise argument, S1–S6, each premise with its card, CI or register support |
| [`OUTLINE.md`](OUTLINE.md) | Slide-by-slide plan: which passage of the author's script each slide carries, and its sources |
| [`AUTHOR_TASKS.md`](AUTHOR_TASKS.md) | Decisions and items only the author can close |
| [`claims/`](claims/) | The claims register: every claim the preliminary sources make, with a verbatim anchor and what became of it (`check_register.py` gates it) |
| [`library/`](library/) | One card per work, marked verified, corrected, metadata-only or unverifiable against what was actually read |
| [`talk/`](talk/) | Deck and script sources, the deck's pictures (`talk/media/`), the deck builder, the checker, the previewer, prepared Q&A |
| [`talk/LIVE_SESSION.md`](talk/LIVE_SESSION.md) | Runbook for the live session on slide 21: environment, translation rules, size and time limits, rehearsed prompts |
| [`talk/live/`](talk/live/) | The live session's command-line helper (`show.py`) and its rehearsal record |
| [`reviews/`](reviews/) | The correctness panel: findings, the verification gate, and what was applied |

## Re-capturing a Gemini share page

```
/usr/bin/python3 sources/capture_gemini_share.py <share-id> out.md --raw-dir <local dir> --budget-ms 40000
```

The script needs Google Chrome, pandoc, and a Python with bs4 and lxml. Keep raw dumps out of the repo.

## Building and checking the talk

```
/usr/bin/python3 talk/build_deck.py          # deck.md + script.md -> deck.pptx (script in the speaker notes)
/usr/bin/python3 talk/check_talk.py          # black on white, glyphs, notes = script, quotations, numbers, timing
/usr/bin/python3 talk/preview_deck.py DIR    # PNG previews outside the repo
```

For the live session on slide 21, `talk/live/show.py` takes a name, a label string and one rule per party
(see `talk/LIVE_SESSION.md` for the recipe and `--bypass`); for example, `python talk/live/show.py
dispatcher AMB "x[1]" "x[0] & x[2]" "x[1]"` prints the whole/factors verdict, the core and who is set by
two others.
