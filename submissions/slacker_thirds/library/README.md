# The Slacker chapter's source library

What this folder is for: keeping the chapter's novelty claim checkable. The chapter says four things
nobody has said together — that a city holds strangers in reach and introduces nobody, that a camera
does the selecting, that access at a door is a grant pronounced by someone who can be argued with, and
that platforms kept all three and withdrew the person. Each of those sits inside a literature that has
been circling it for decades. The library exists so that "nobody has said this" is a finding rather
than a hope.

## How it is built

```
domains/            per-domain audits — the deep research sweeps, one file per knowledge domain
cards/              one card per source, keyed by citekey
CARDS_INDEX.md      generated from cards/ by build_index.py — do not hand-edit
REFERENCES.md       Part A, the chapter's Chicago bibliography; Part B, everything held or proposed
build_index.py      python build_index.py  (rewrite)   |   --check  (fail if stale or malformed)
```

A **domain sweep** answers one question put to one literature: *is what this chapter claims already
said here, under another name?* It audits every claim the chapter makes in that domain, ranks the works
it is missing by consequence, and lists the objections the domain would raise. The sweeps are the
reasoning; the cards are the index into it.

A **card** is one source. Its frontmatter carries `citekey`, `title`, `authors`, `year`, `domain`,
`used_by`, `status`, `verified`, `source_basis`, and a `sweep` pointer back to the audit that found it.
Its body says what the source does for the argument, where the loci are, and — this is the field that
earns the folder — what it does to the novelty claim.

**`status`** — `cited` (in the live chapter), `held` (already in the folder, not yet used), `candidate`
(surfaced by a sweep as worth citing).

**`verified`** — `verified` (a fetched authoritative text was read), `corrected` (checked, and the
chapter is wrong about it), `metadata-only` (record and abstract confirmed, full text not read),
`unswept` (cited in the chapter, but no domain sweep has audited it yet). Nothing is marked verified on
the strength of a search result; the sweeps hold to that rule and so should anything added here.

## What the deck currently says

137 cards: 55 cited, 13 held, 69 candidates. 41 verified against a fetched text, 5 corrected,
79 metadata-only, 12 unswept. Five domains swept over two rounds.

### Round 2 — the film scholarship, 19 August 2026

The question: has a film scholar already named the camera as the thing that chooses? **Yes, once, in an
article the chapter already cites for something else.** Jeong 2021, at 144, writes that "the camera
autonomously shifts from one person to another … which renders palpable the camera's own agency," calls
it "the real agent of networking on the ground," and describes "the camera's hesitation about whom to
follow between different characters whose paths cross" — attached to Berg's daisy-chain plot, one page
after naming *Slacker* as a network narrative film. Note 10 cites Jeong for Berg's page range and
nothing else. See [`jeong2021network`](cards/jeong2021network.md).

That is the panel's mandatory M3 — prior art on a page already cited — repeating in the chapter's own
field. The thesis survives the collision: Jeong's camera-agent *connects*, the chapter's camera *chooses
one and never returns*, and he has no reach, no door, no grant, and no person who could be asked. The
repair is roughly twenty-five words and it strengthens the chapter, because a distinction drawn against
a named rival is load-bearing in a way a gap is not.

Round 2 also verified two things and closed one debt. Soldani, cited only for drift, documents the guest
list and the admission stamp as a pair at 78–79 — peer-reviewed corroboration of the door reading at
zero body words — and her Debord quotation confirms that the chapter's grammatical-person objection to
the drift readings is correctly aimed. And Jeong 144 reads "(Berg 2006, 24–26)" verbatim, which closes
the corroborating half of note 10. See [`soldani2017performance`](cards/soldani2017performance.md) and
[`berg2006taxonomy`](cards/berg2006taxonomy.md).

The durable lesson is the pattern, not the finding: the same error — prior art on a page already cited —
surfaced independently in platform studies and in film studies. **The chapter cites for pins and does
not read for arguments.**

### Round 1 — the borrowed domains, 18 August 2026

Round 1 ran over four domains — the urban stranger, platform studies,
new property and platform regulation, and Royce and the pragmatist theory of community. All four
returned the same shape of verdict: the chapter's primary-source work is unusually accurate, and its
sense of what is already in print is not. Five findings are load-bearing.

- **Simmel wrote the reach section.** "The Metropolis and Mental Life" describes a city holding people
  in unceasing contact while withholding acquaintance. The chapter's claim that the postponed third
  "has remained where Simmel left it" is false of Simmel's own corpus, whatever is true of the triad
  literature. See [`simmel1903metropolis`](cards/simmel1903metropolis.md).
- **The two jobs restate Goffman.** Unfocused and focused interaction is holding and selecting, in
  print since 1963. The chapter's novelty is that the selector is a camera, not a person — defensible,
  and currently unsaid. See [`goffman1963behavior`](cards/goffman1963behavior.md).
- **The vacancy already has four names.** Bovens and Zouridis's vanished street-level bureaucrat
  (2002), Nissenbaum's four barriers (1996), Alkhatib and Bernstein's discretion gap (2019), Stark and
  Vanden Broeck's "distributed, deflected, and denied" (2024). None of the four has the door, the
  grant, or the film — so the novelty survives, and has to be defended rather than asserted. See
  [`bovens2002streetlevel`](cards/bovens2002streetlevel.md).
- **Royce wrote his own theory of the third,** and the chapter cites him only for a membership test.
  The Community of Interpretation at 2:209–13 answers the chapter's question directly: somebody wills
  to interpret you to a stranger. See [`royce1913interpretation`](cards/royce1913interpretation.md).
- **The law already legislated the answerer.** GDPR art. 22(3) since 2018, California's appeals process
  since 2020, Australia's deactivation code requiring a representative produced on request since 2025.
  The chapter's "the law has begun trying" understates by three decades, and its own California
  evidence is evidence of a failed remedy rather than an unregulated one. See
  [`aus2024deactivationcode`](cards/aus2024deactivationcode.md) and [`ca2020prop22`](cards/ca2020prop22.md).

Every one of these is repairable by addition, and none of them touches the thesis. That is the round-1
result and it is a good one.

## What is still open

Round 2 answered the novelty question and could not read four things while doing it: the Internet
Archive was offline for the whole sweep, which took Stone's chapter 3 with it; criterion.com sits behind
a Cloudflare challenge; the *ReFocus* volume text was not obtained. Those are re-runs, not gaps. The
remaining unswept domain is the German sociology of the third, where note 21 rests a negative claim on
two edited volumes read from tables of contents. See [`GAPS.md`](GAPS.md).
