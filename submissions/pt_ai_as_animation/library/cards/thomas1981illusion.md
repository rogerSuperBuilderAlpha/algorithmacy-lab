---
key: thomas1981illusion
apa: "Thomas, F., & Johnston, O. (1981). *Disney animation: The illusion of life* (1st ed.). Abbeville Press."
authors: "Thomas, Frank; Johnston, Ollie"
year: 1981
title: "Disney Animation: The Illusion of Life"
venue: ""
volume: ""
issue: ""
pages: ""
doi: ""
url: "https://openlibrary.org/works/OL2924612W"
type: book
facets: [F4]
claims: [c6]
role: anchor
load: load-bearing
read_depth: metadata
object_read: "(1) Open Library search result (JSON), 3 hits for 'Disney Animation' by Frank Thomas and Ollie Johnston (OL34586365W Abbeville 1990, OL31195516W Abbeville 1987, OL7810929M BDD 1989), openlibrary_search.json at ~/iit-playground/pt_ai_animation_local/pdfs/thomas1981illusion/ (copied from dxd_animation_local per provenance.txt), sha256 1679e42e5f653f74a1bf1c839d61bbf17a6be728519ce22c26c18061e247b44b; (2) Open Library work record OL2924612W and its editions list, fetched by the writer from https://openlibrary.org/works/OL2924612W.json and .../editions.json on 2026-11-08 into the session scratchpad, sha256 66b2f4bd0a99ec988f8aa7254f33ea5778d7a42aa6a8a91e4db972f506563ec7 (work) and b03b091a18a27f160b8301307d92050b04e6611ca1f746073e20bfbf34cee5f4 (editions); [Corrected by Fable, S7: the key folder now holds these records, saved 2026-11-08 per its provenance.txt: openlibrary_work.json (sha256 66b2f4bd..., same as the writer's copy), openlibrary_editions.json (sha256 340c7c4643ef9253fcec1f2217ec69e0796f73fcead0955ae17802620610a5c4, the verifier's refetch, not the writer's b03b... copy) and openlibrary_edition_OL4266737M.json (sha256 6e7551dff8b56079a58f8b32e22aceb4caf19a7b3f3a5b55295da549dd327b16)]; no text of the book; inbox/thomas1981illusion.pdf absent; read 2026-11-08"
verified: corrected
verified_against: "openlibrary_search.json; Open Library OL2924612W work, editions list, edition OL4266737M and three author records, refetched by the verifier 2026-11-08; SKETCH.md working titles; no loci"
prior_cards: [dxda/thomas1981illusion, dxdanimator/thomas1981illusion]
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Thomas & Johnston (1981), Disney animation: The illusion of life

## What it argues

This is a metadata card. The Open Library work OL2924612W, "Disney animation", gives a first publish date of
1981. Its edition OL4266737M reads: *Disney animation: the illusion of life*, "1st ed.", Abbeville Press,
New York, 1981, 575 pages, "Includes index", with the statement of responsibility "Frank Thomas and Ollie
Johnston." and Johnston listed as contributor ("Johnston, Ollie, 1912-"). The catalogue subjects are Walt
Disney Productions and animated films in the United States, history and criticism. The work record links a
*New York Times* review of 29 November 1981 titled "Making drawings move". Nothing in any record says what
the book argues.

## What the paper uses it for

- **c6** (animation is the craft of composing a living character from inert parts): the sketch's anchor for
  §3, with Lasseter (1987), and the source of its second working title, *The Illusion of Life, Again*.
  FACETS wants two things from it: the Disney principles, and the division between key poses and in-betweens
  on which §3's mapping rests. The records confirm only that the book exists, who wrote it and that its
  subtitle is "the illusion of life". They do not show that the book states principles, how many, or how it
  divides the work. The c6 use therefore rests on an unread book. A second step stretches even a read
  source: the book describes one studio's character animation for film, and carrying its working methods
  over to building AI systems is the paper's move, not Thomas and Johnston's.

## Loci

None.

## Caution

- The book is on `BROWSER_LIST.md` (upgrade row, OL2924612W; the principles chapter first), and no copy is
  in `inbox/`. DECISIONS calls for full text of the principles chapter if Roger opens the book.
- **Records outside the key folder.** The key folder holds only the search JSON copied from the dxd run,
  whose three hits are later editions (1987, 1989, 1990) and none of which gives 1981 or the subtitle. I
  fetched OL2924612W and its editions from Open Library on 2026-11-08 to check the year, subtitle and
  publisher, and kept them in the session scratchpad, which is not durable. S6 should refetch them, or S4
  should save them to the key folder, before the 1981 details count as recorded.
- **Correction to the dxda card.** That card marks the year 1981, the subtitle and the 1981 publisher
  unchecked, because no record it read showed them. Edition OL4266737M shows all three (1981, "the illusion
  of life", Abbeville Press, New York). A second 1981 edition, OL8255081M (June 1981, ISBN 0896592332, 575
  pp.), agrees. An Abbeville 1984 edition, OL2838660M (382 pp.), also sits under the work. The dxda file is
  left alone.
- **Author field.** The work record lists three author keys, which resolve to "Thomas, Frank", "Thomas
  Johnson" and "Ollie Johnson", the garbled field DECISIONS describes. The card takes the names from the
  edition's statement of responsibility, "Frank Thomas and Ollie Johnston."
- **The dxd_animator card** (read depth "partial") claims the book sets out "the studio's twelve principles
  of animation", lists five of them, and says believability comes from emotional reading rather than
  realism. No record read this run shows any of that; the dxda card already flagged these claims, and they
  remain unchecked. That file is left alone.
- **SKETCH title order.** SKETCH.md (working titles) gives the book as *The Illusion of Life: Disney
  Animation*. Every 1981 record read here gives *Disney animation: the illusion of life*; the sketch's order
  matches none of them. The card follows the records; SKETCH is left alone. [added by S6 verifier]
- **"1st ed."** comes from the edition record's `edition_name`. APA would normally omit a first-edition
  statement; S8 can drop it.
- **What the paper may not claim from it:** any principle, number of principles, or account of key poses and
  in-betweens, until the chapter is read.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W2 group 1
- verdict: corrected
- checked: sha256 of openlibrary_search.json matches; its three hits are as the card lists them; as Caution asked, I refetched from openlibrary.org on 2026-11-08: work OL2924612W (sha256 66b2f4bd... identical to the writer's copy; first publish date 1981; NYT review link "making-drawings-move", 1981-11-29), the editions list (content matches the writer's copy; only the "self" link differs) and edition OL4266737M (title "Disney animation", subtitle "the illusion of life", edition_name "1st ed.", Abbeville Press, New York, 1981, 575 p., "Includes index.", by-statement "Frank Thomas and Ollie Johnston.", contribution "Johnston, Ollie, 1912-", ISBNs 0896592324 and 0896592332); OL8255081M (June 1981, 575 pp.) and OL2838660M (1984, 382 pp.) are as stated; the three work author keys resolve to "Thomas, Frank", "Thomas Johnson" and "Ollie Johnson". The refetched copies sit in the verifier's session scratchpad, not the key folder (this step may touch only cards), so S4 or S8 should still save them there. Prior-card notes match the dxda and dxd_animator cards. Status cited is right (SKETCH §3 and working titles name the book).
- changed: added a Caution bullet recording that SKETCH.md inverts the title relative to every 1981 record (README rule 3).

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index after fix**.
- Checked: Loci = None (metadata card); the key folder now holds four Open Library records; sha256 recomputed: openlibrary_search.json 1679e42e... (matches), openlibrary_work.json 66b2f4bd... (matches the writer's copy), openlibrary_edition_OL4266737M.json 6e7551df... and openlibrary_editions.json 340c7c46... (the verifier's refetch; the writer's b03b... copy is not the saved one); edition OL4266737M gives 1981, 'the illusion of life', Abbeville Press, New York, 575 p., 1st ed., by-statement 'Frank Thomas and Ollie Johnston.', as the card says; status cited is right (SKETCH names the book).
- Changed: object_read: the sentence saying the work and editions records sat only in the session scratchpad is out of date; added the saved files and their sha256 values, marked [Corrected by Fable, S7]. The Caution bullet 'Records outside the key folder' is left as a record of the writer's situation.
- For the author: SKETCH.md gives the title as *The Illusion of Life: Disney Animation*; every 1981 record reads *Disney animation: the illusion of life*. The book is unopened and the principles chapter is still the ask
