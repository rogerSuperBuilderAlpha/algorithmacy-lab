---
key: crafton2012shadow
apa: "Crafton, D. (2012). *Shadow of a mouse: Performance, belief, and world-making in animation*. University of California Press. https://doi.org/10.1525/9780520352520"
authors: "Crafton, Donald"
year: 2012
title: "Shadow of a Mouse: Performance, Belief, and World-Making in Animation"
venue: "University of California Press"
volume: ""
issue: ""
pages: ""
doi: "10.1525/9780520352520"
url: ""
type: book
facets: [F4, F5]
claims: [c6, c8, c10]
role: anchor
load: load-bearing
read_depth: metadata
object_read: "Crossref work record for 10.1525/9780520352520 (no abstract), at ~/iit-playground/pt_ai_animation_local/pdfs/crafton2012shadow/crossref.json; fetched by S4 (FETCH_LOG.tsv: 'Crossref 200; records only'); read 2026-11-08; sha256 eaa14e27fcbf12d034fbd6a6d667767da1ab3c6bb1fe3c0600acaab2b716420f. No text of the book; inbox/ empty on 2026-11-08"
verified: verified
verified_against: "crossref.json (sha256 recomputed); FETCH_LOG, BROWSER_LIST, FACETS and DECISIONS rows; metadata depth, Loci None"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Crafton (2012), Shadow of a mouse

## What it argues

This is a metadata card. I read no text of the book, and the record carries no abstract. The Crossref record
shows only this: University of California Press published *Shadow of a Mouse: Performance, Belief, and
World-Making in Animation* by Donald Crafton. Crossref lists Crafton twice, as author and as editor, and types
the work "edited-book". It dates print publication 2012-12-31 and online publication 2023-09-19, gives the
electronic ISBN 9780520352520, and points to a De Gruyter Brill landing page. It records 34 citing works. The
subtitle names the three topics the paper wants (performance, belief, world-making), but what Crafton argues
about them is unread.

## What the paper uses it for

Each use below is what the triage file expects from the subtitle and an abstract I did not see. None is
supported until the book is read.

- **c6** (animation composes a living character from inert parts): the paper needs an animation scholar who
  treats the animated character as a performer. The subtitle's "performance" promises that; the book's
  position is unread.
- **c8** (co-optation; the viewer is co-opted): "belief" and "world-making" are the viewer's side of
  co-optation. Whether Crafton treats belief as willing, as default, or as produced by the film is unknown.
- **c10** (the analogy breaks at liveness): the paper needs to know whether Crafton treats animated
  performance as live or present. Unread. If he argues that it does feel live, he weakens §5's claim that
  animation is "rendered in advance", and the card would then need the role contrast for c10.

## Loci

None

## Caution

- **Year (DECISIONS correction applied).** FACETS dates the book 2013. Crossref gives print 2012-12-31, and
  DECISIONS rules 2012. A 31 December date may be how the deposit records a year alone; the title page or
  copyright page should confirm it. The online date (2023-09-19) belongs to the De Gruyter Brill digital
  edition, not to first publication.
- **Type.** Crossref's "edited-book" type and its listing of Crafton as editor sit oddly with a single-author
  monograph. The APA entry names him as author, as the record's author field does; the title page settles it.
- **Abstract not held.** Triage F1-F4.md quotes an OpenAlex abstract ("Are animated characters actors and
  stars, just like humans? ..."). No openalex.json sits in the key folder and I did not see that abstract this
  run, so the card does not use it (README rule 1).
- **On BROWSER_LIST.md** (book; closed route). Until a copy reaches `pt_ai_animation_local/inbox/`, the paper
  may say only that the book exists and what its title names. "Anchor" is the role the paper intends, not
  something the card has confirmed.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W2 group 2
- verdict: verified
- checked: frontmatter against crossref.json (Crafton, Donald, as author and again as editor; type edited-book; title "Shadow of a Mouse" with subtitle "Performance, Belief, and World-Making in Animation"; University of California Press; print and issued 2012-12-31, online 2023-09-19; electronic ISBN 9780520352520; DOI; 34 citing works; De Gruyter Brill landing page; no abstract); crossref.json sha256 recomputed, matches; the folder holds crossref.json only and inbox/ is empty; FETCH_LOG.tsv row reads "Crossref 200; records only"; BROWSER_LIST.md row present; FACETS.md gives 2013 and DECISIONS rules 2012, as Caution says; triage F1-F4.md carries the OpenAlex abstract the card rightly leaves out. What it argues states only record facts; Loci None; the c6, c8, c10 uses say they are unread.
- changed: nothing in the card's content. I removed the empty "## Hand-check" placeholder heading.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (metadata card, Loci None); frontmatter vs crossref.json (Crafton as author and editor, edited-book, UC Press, print 2012-12-31, ISBN 9780520352520, DOI); crossref.json sha256 recomputed, matches; inbox/ empty; the three claim uses say they are unread.
- Changed: nothing.
- For the author: status is `cited`, but SOURCE.md and SKETCH.md do not name Crafton (README: cited = SOURCE or SKETCH uses it); the role `anchor` is the paper's intention at metadata depth. Decide once the book is opened.
