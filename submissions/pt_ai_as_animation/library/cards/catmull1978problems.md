---
key: catmull1978problems
apa: "Catmull, E. (1978). The problems of computer-assisted animation. In *Proceedings of the 5th Annual Conference on Computer Graphics and Interactive Techniques* (SIGGRAPH '78) (pp. 348–353). ACM. https://doi.org/10.1145/800248.807414"
authors: "Catmull, Edwin"
year: 1978
title: "The problems of computer-assisted animation"
venue: "SIGGRAPH '78 (Proceedings of the 5th annual conference on Computer graphics and interactive techniques)"
volume: ""
issue: ""
pages: "348–353"
doi: "10.1145/800248.807414"
url: ""
type: proceedings
facets: [F4]
claims: [c6, c7, c10]
role: contrast
load: load-bearing
read_depth: metadata
object_read: "Crossref work record (JSON) for 10.1145/800248.807414, crossref.json at ~/iit-playground/pt_ai_animation_local/pdfs/catmull1978problems/; no abstract in the record; no text of the paper; inbox/catmull1978problems.pdf absent; read 2026-11-08; sha256 8caa195f447b11cb344b0e4735a008ce1c7946c934f45f4e26fd0337023a3393 (crossref.json, computed with shasum -a 256; no sha256.txt in the folder)"
verified: verified
verified_against: "crossref.json (fields, 12 references, is-identical-to relation); BROWSER_LIST row; triage/F1-F4.md abstract lines; no loci"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# Catmull (1978), The problems of computer-assisted animation

## What it argues

This is a metadata card. The Crossref record carries no abstract, so it says nothing about the paper's
argument. It shows this much. Edwin Catmull, of the Computer Graphics Lab at the New York Institute of
Technology, published the paper in the proceedings of SIGGRAPH '78 (ACM, New York), pp. 348–353, dated
23 August 1978. The record lists twelve references. They include Baecker's "Picture-driven animation"
(1969), Burtnyk and Wein's "Computer Animation" (1977), Stern's dissertation "GAS - A system for computer
aided keyframe animation" (1978), Kitching's "Computer animation - some new ANTICS" (1973) and Tuori's
thesis "Tools and Techniques for computer-aided animation" (1977). Crossref marks the paper as identical to
10.1145/965139.807414.

## What the paper uses it for

Every use below rests on the triage file's reading of an abstract that no record in the key folder holds.
None of it is checked.

- **c6** (animation is the craft of composing a living character from inert parts): Catmull would supply
  the production division the paper's §3 mapping needs, with animators drawing key or "extreme" drawings and
  a computer asked to supply the rest. The record's reference titles (keyframe animation, picture-driven
  animation) fit that topic; they do not show what Catmull says about it.
- **c7** (necessary opacity: no frame holds the motion): this is the contrast. If Catmull treats missing
  in-between drawings as an engineering problem that computers can attack, he objects to the sketch's
  claim that "there will always be missing frames". On that reading the missing frames are a gap in labour,
  not a gap in principle. c7 survives only if §4.2 restates it as FACETS proposes: what no frame holds is
  the motion, which the viewer's perception supplies. The triage file also reads the abstract the other
  way: if Catmull says information is lost because the drawings project a character the animator holds in
  mind, then he supports c7. Which reading holds cannot be settled without the text.
- **c10** (the analogy breaks; the LLM makes its own in-betweens): Catmull would be the historical source
  for machine in-betweening, the row of §3's mapping that pairs in-betweening with decoding and sampling.
  The paper would object to its own analogy here: if computers have produced in-betweens since the 1970s
  without anyone calling the computer the animator, then "the LLM makes its own in-betweens" does not by
  itself make the LLM more than a tool. This stretches Catmull, who wrote about drawing systems, not about
  agents.

## Loci

None.

## Caution

- The paper is on `BROWSER_LIST.md` (row for `catmull1978problems`): dl.acm.org returned 403 to S4, and
  no copy is in `inbox/`. When Roger saves the PDF there, the same writer takes the card to full text.
- **Unchecked abstract.** `triage/F1-F4.md` (F4 notes) quotes an abstract: the systems aimed "to let the
  computer produce missing drawings based on extreme drawings produced by animators", and drawings are "two
  dimensional projections of three dimensional characters as visualized in the animators head, hence
  information is lost". Neither line appears in `crossref.json`, and there is no `openalex.json` in the
  folder. They stay out of Loci and out of "What it argues" until the text or a record shows them.
- **Two DOIs.** Crossref gives 10.1145/800248.807414 (the proceedings) and, under "is-identical-to",
  10.1145/965139.807414. DECISIONS adds that the second is *ACM SIGGRAPH Computer Graphics* 12(3), but the
  record here does not show that volume and issue. The card cites the proceedings DOI, the one in the key
  folder.
- The Crossref affiliation reads "Old Westhury, New York", as deposited.
- **What the paper may not claim from it:** anything about what Catmull argues, until the text is read.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W2 group 1
- verdict: verified
- checked: sha256 of crossref.json matches; author, affiliation ("Old Westhury"), title, container title, event SIGGRAPH '78, pages 348-353, date 1978-08-23, publisher ACM (New York), type proceedings-article and DOI all match the record; no abstract in the record, so metadata depth is honest; the five reference titles named are in the record's 12 references; is-identical-to 10.1145/965139.807414 is in the record; the triage abstract lines are correctly kept out of Loci; BROWSER_LIST row says dl.acm.org 403; no inbox copy; status candidate is right (SKETCH and SOURCE do not name Catmull); every use is marked as resting on the unread text.
- changed: nothing

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 0/0 (metadata card, Loci None); frontmatter vs crossref.json (Edwin Catmull, SIGGRAPH '78 proceedings, pp. 348–353, 1978-08-23, ACM New York, no abstract); sha256 recomputed, matches; the triage abstract lines rightly kept out; inbox empty.
- Changed: nothing
- For the author: nothing beyond the status inconsistency with burtnyk1976interactive (status note in part1.md).
