# Source library — hospitality phygital

A card per source, organized around the paper's argument rather than the alphabet. Built 8 August
2026, after the manuscript was complete, because the research behind it was scattered across
bibliography notes, one prose file that stopped three rounds early, and a set of deep-research audits
that existed only in a conversation.

## What it is for

The reviewer-response round asks one question repeatedly: *why this source and not that one?* The
answer usually exists at the moment the decision is made and is unrecoverable a month later. A card
records it. That is the whole justification.

So the library holds more than the bibliography does. Alongside the sources the paper cites, it keeps
the ones weighed and declined — with the displacement argument that kept each one out — and the ones
held but uncited, with the reason. If a referee proposes an alternative, the card shows whether it was
already considered and what it lost to.

## Layout

| path | what it is |
|---|---|
| `cards/<citekey>.md` | one card per source, flat, filename equal to the citekey |
| [`CARDS_INDEX.md`](CARDS_INDEX.md) | generated. Master table, a by-section rollup, a by-cluster rollup, and the open-debts table |
| [`CLAIMS.md`](CLAIMS.md) | the controlled vocabulary of claims a card may say it supports |
| [`VENUE_RULINGS.md`](VENUE_RULINGS.md) | standing decisions about outlets, so the same rejections are not re-litigated |
| `build_index.py` | regenerates the index and validates every card |

Cards are flat and both axes — the five literature clusters and the nine manuscript sections — live in
frontmatter. Nothing is filed in a directory, because a card in the wrong directory is silently wrong
whereas a generated index cannot be stale without CI saying so. That failure already happened once
here: `literature/field_map.md` was a hand-maintained taxonomy and it went stale the moment two
research rounds skipped their update step.

## The fields that matter

`status` is `cited`, `held`, `rejected` or `superseded`. A held card must say why it is held; a
rejected card must say what displaced it; a superseded card must name its replacement. `role` records
what the source does — evidence, a framing the paper argues past, both, a published null, a nearest
rival, or a governor that keeps another claim from overreaching.

`read_depth` is `full-text`, `abstract` or `metadata`, and it is declared honestly. Twenty-eight
cards sit at `full-text` after the 8 August retrieval pass; most of the rest sit at `abstract`, which
is the true state and worth seeing. One card, `lynch2021critical`, claims full-text depth from a
reading whose copy was not retained, and carries a `no-retained-copy` flag saying so rather than
quietly asserting a depth nobody can re-check. Every bullet in a card's
key-facts section carries its own depth tag, and the check refuses a card whose frontmatter claims
one depth while its facts claim another.

`verified` mirrors the bibliography's vocabulary rather than inventing a second one, so
`render_refs.py` keeps working unchanged. The check fails any card claiming a stronger tier than its
bibliography note supports.

## Running it

```
python3 build_index.py                            # rewrite CARDS_INDEX.md
python3 build_index.py --check                    # CI gate
python3 build_index.py --check --require-complete # also demand a card per bibliography entry
```

The check is wired into `ci/reproduce.json` as `hospitality-library-current`. It fails on a stale
index, a malformed card, an unknown claim slug, a citation with no card, a card marked cited that the
manuscript does not use, a verification tier stronger than the bibliography supports, or a depth-honesty
violation.

Quotations on full-text cards were checked back against the retrieved files on 8 August: all 65
appear in their source, and the two carrying `[…]` mark a real elision of an inline citation. That
check is not wired into CI, because it needs the full texts and those are not in the repository.
What *is* wired in is `manuscript/check_citations.py`, which compares every in-text year against the
rendered reference list — the gate that would have caught four references pairing an online-first
year with a version-of-record issue.

That last set is not defensive decoration. On the day the library was built the check found two real
defects in a manuscript already merged to `main`: Morrison (2014) cited in section 5 with no entry in
the reference list, and two Lynch 2021 works rendering identically as "(2021)" while the text cited
2021a and 2021b. Both had survived every prior read.

## Keeping it true

Every research run adds or updates cards with a fresh `generated_run`, flips displaced sources to
`superseded` rather than deleting them, appends a part to
[`../literature/FOUNDATION.md`](../literature/FOUNDATION.md) citing citekeys, and reruns
`build_index.py`. Three of those four are enforced by CI; the FOUNDATION part is narrative and is not,
which is acceptable now that it is no longer the only record of anything.

Open debts appear at the top of the index rather than in a paragraph someone has to remember to read.
