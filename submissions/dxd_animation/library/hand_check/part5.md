# S7 hand-check, batch 5 (Fable, 2026-11-06)

One card, `wu2026ainimation`, read against `~/iit-playground/dxd_animation_local/pdfs/wu2026ainimation/`: the held arXiv v1 PDF (sha256 recomputed, matches provenance.txt and sha256.txt), its reading-order text layer for every quotation (whitespace collapsed, pages counted by form feed), and datacite.json, openalex.json and arxiv_abs.xml for the frontmatter. The full text was read, so the claim uses c4–c9 and the word checks (Stark, Silvio, Maeda, Johnston, Lasseter, Disney, puppet, animator, "Illusion of Life", principles, decision: zero hits in both layers) rest on the whole paper. I also read `library/GAP_CHECK.md` to answer whether its c9 wording must change given this card; I did not edit it.

Verdicts: 0 index, 1 index after fix, 0 hold.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| wu2026ainimation | full_text | 15/15, each on the stated PDF page | index after fix | (1) "(the paper does not state their order)" → the paper's own "completed … in succession" (§5, PDF p. 6); (2) Caution: Experiment 2 confidence sentence is on PDF p. 8, not p. 7 | (a) whether "in succession" fixes the order 1→2→3 is a reading, not a statement in the paper. (b) The card keeps c4, c6, c7 bullets (all "not supported") for tags absent from its `claims` list; README asks one bullet per claim tag. (c) GAP_CHECK c9: see below. |

## GAP_CHECK.md, claim c9, given this card

The c9 verdict holds and the suggested §6 sentence can stay as written. The full text confirms what the abstract showed: Wu and Masson never use "decision", cite no animation theory, and never read the LLM as a character. Their "animation" is UI transition animation in the Heer & Robertson and Chevalier line (card, Caution, first bullet), so they take neither half (A) nor half (B) of c9. They do take something smaller, which GAP_CHECK already concedes: interface animation of AI responses as a tested design method.

Four wording updates, all small, for the author to make or decline:

1. Part 2, narrowing point 2, "Their abstract stops short of decisions and of the character reading … Card it before §6 is drafted": the card now exists and reads the full text, so "abstract" → "full text" and the instruction is done.
2. Hits table, first row: the paper and all three records spell the first author "Jiaqi Wu", not "Jia-Qi Wu"; "carded? **No**" → carded (`wu2026ainimation`, full_text, status candidate); the row's reading can rest on the full text rather than the abstract.
3. Verdict paragraph, "most of this check rests on abstracts": now true of every leg except Wu & Masson.
4. The §6 sentence "Interface research animates LLM output to help users review it (Wu & Masson, 2026)" is accurate, but the card's Caution asks §6 to say outright that "animation" there means UI transitions, not Stark's sense, so a reviewer does not read the sentence as the animation reading already taken. One clause would do it.

One addition beyond c9. Wu and Masson pose the pacing question directly — "Should AI answers be shown as fast as possible using technology-driven animations, or would slower but well-crafted animations be preferable?" (PDF p. 2, §2.1) — and answer it with the only lab datum the library holds for a crafted, slower display beating an instant one (n = 16, review tasks). That bears on c8 and OUTLINE §4.1/§5 more than on c9, as GAP_CHECK's "For the author" already notes.
