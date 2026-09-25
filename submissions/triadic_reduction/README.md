# Triadic reduction — the talk

**Status.** Claim locked 2026-09-24. **v3, 2026-09-25:** the deck is now the author's own 16-slide deck, with its design removed and its pictures, diagram and table kept (`talk/deck.pptx`, built from `talk/deck.md`). The script is the author's script of the same day, re-sectioned onto those slides (`talk/script.md`); it runs about 22.6 minutes at 130 words a minute against a 20-minute slot. Open questions on the new text are in [`AUTHOR_TASKS.md`](AUTHOR_TASKS.md); the author's timed read-aloud is next.
**Venue.** ALGOCON, the algorithmacy.org conference, Port of Spain, 28–31 October 2026. Slot: 20 minutes.
**Deliverables.** A black-and-white slide deck (`.pptx` built from Markdown: black text on white, the author's two portraits, the valency diagram and one plain table, nothing else) and a talk script.

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
