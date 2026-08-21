# Provenance, and what is deliberately not in this directory

## Two model texts are local-only

This round reviewed the chapter against two model papers. Neither full text is committed, because
`algorithmacy-lab` is a public repository and both are third-party copyrighted works. The repo's
existing policy is already explicit about this — `.gitignore` carries "Lima acquired PDFs — local only;
do not commit publisher copies" — and the same rule applies here.

| Not committed | What it is | How to re-acquire |
| --- | --- | --- |
| `hansen_1999.pdf` | Miriam Bratu Hansen, "The Mass Production of the Senses: Classical Cinema as Vernacular Modernism," *Modernism/Modernity* 6.2 (1999), 15pp. | `curl -sL https://web.njit.edu/~kimmelma/Miriam_B_Hansen__The_Mass_Production_of_the_Senses.pdf` |
| `models/model_mcloughlin.md` | James McLoughlin, "'What's Going On?': The Moral Philosophy of *A Serious Man*," New Critique, 23 Jan 2020 (first published Sonder Magazine, 23 Jun 2017). 78 paragraphs, 5,536 words. | `curl -sL -A "Mozilla/5.0 …" "https://web.archive.org/web/20240915193227/https://newcritique.co.uk/2020/01/23/essay-whats-going-on-the-moral-philosophy-of-a-serious-man-james-mcloughlin/"`, then extract `div.entry-content`. WebFetch returns HTTP 403 from newcritique.co.uk, from the sondermag mirror, and is blocked from web.archive.org; curl with a browser user-agent defeats all three. |

What **is** committed is derived work: `models/model_poulaki.md` (a seven-move structural map plus the
v16→v17 sentence audit, quoting Poulaki only in short excerpts) and `models/hansen_sentence_ledger.md`
(a prior pass's rewrite ledger, already in the archive). Seat 07's review quotes McLoughlin in short
excerpts for criticism. Those are ordinary scholarly quotation; the full texts are not.

## What produced the rest

`mechanical/` is verbatim tool output against `chapter.md` pinned at `db5468d`:
`check_bans.py`, `check_film.py`, `check_quotes.py` (run against a staged root, since it resolves the
transcript relative to an older layout), and `~/.claude/skills/draft/engine/report.py --register slacker`.
`apparatus_v17.txt` is a notes/bibliography reconciliation written for this round.
`v17_sentences.txt` comes from `split_sentences.py`, kept here so the numbering the reviews cite can be
regenerated: `python3 split_sentences.py ../../chapter.md > v17_sentences.txt`.

## Seat 08

Seat 08's Fable agent terminated twice on API spend limits without producing a file. That seat was re-run
directly by the orchestrator, is narrower than the other seven, and says so in its own header. Nothing
from the two terminated runs is reported in it.
