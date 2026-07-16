# Copyeditor Review — Post 9, "The Ledger" (draft v4)

## STEP 0

Register: deliberate first-person Substack philosophy. Quoted material (Hegel, Maybee, Fuchs) and the series' signature lines ("the owl has flown," "at dusk that is the trade you take," the ledger conceit) are off-limits as "prose failures" — nothing below touches them; every flag is a citation, quote, edition, or arithmetic mechanic. Series guards both read clean on inspection: the anticipation guard holds ("never claims Hegel anticipated Φ… He reached a different criterion," homology language throughout — "a rhyme," "two lines that meet on the easy cases and part on the hard ones"), and the demotion guard is clean — the digest's two flagged phrases ("a thin one to hang two years on," "the sanctioned line about principled exploration") are both absent from this draft; the cheap-test objection is stated at full strength and answered structurally (OR-case, exact-regime boundary), never conceded as a demotion.

## Verdict: Minor revisions

This is very close to post-ready. Every substantive correction the Stage-3 digest and RECEIPTS.md called for has actually been applied — checked word-for-word, not assumed. What remains are mechanical APA slips: one in-text citation-order violation, four reference-string inconsistencies (verified against `check_editions.py`, run for real against the file on disk), and one typo.

**Single most important fix** — the in-text anchor citation in paragraph 2 is out of alphabetical order:

> "...the degree of that irreducibility is Φ, computed by finding the partition that does the least damage to a system's causal powers and reading what survives it (Oizumi et al., 2014; Albantakis et al., 2023)."

APA 7 (§8.12) orders multi-work parentheticals alphabetically by first surname, not by year — Albantakis before Oizumi. This is the exact fix the draft's own sourcing note claims v3 already made ("the two multi-work parentheticals alphabetized (Albantakis before Oizumi; Honneth into second position)"), so this is a regression from the v3→v4 rebuild, not an unnoticed gap. It sits in the series' second paragraph, the first citation a reader hits.

**Rewrite:** `(Albantakis et al., 2023; Oizumi et al., 2014)`

---

## Findings, most damaging first

**1. In-text citation order (paragraph 2).** As above. This is the load-bearing fix — everything else below is lower stakes.

**2. `Science of Logic` reference entry has the translator/editor roles reversed relative to the series' own canon.**

Draft (References): `Hegel, G. W. F. (2010b). *The science of logic* (G. di Giovanni, Trans. & Ed.). Cambridge University Press. (Original work published 1816)`

The card `hegel-sl-digiovanni.md` pins the author line as `"Hegel, G. W. F. (G. di Giovanni, Ed. & Trans.)"`, and Posts 3 and 4 (confirmed by running `check_editions.py`) both cite it as `(G. di Giovanni, Ed. & Trans.)`. Post 9 alone inverts the order. Also missing the DOI that posts 3/4 carry for the same work.

**Rewrite:** `Hegel, G. W. F. (2010b). *The science of logic* (G. di Giovanni, Ed. & Trans.). Cambridge University Press. https://doi.org/10.1017/9780511780240 (Original work published 1816)`

**3. `Encyclopaedia Logic` Zusätze (Hackett) reference has a capitalization slip against the series' own canonical string.**

Draft: `...*The encyclopaedia logic: Part I of the encyclopaedia of philosophical sciences with the Zusätze* (T. F. Geraets, W. A. Suchting, & H. S. Harris, Trans.). Hackett...`

Posts 5 and 8 both capitalize the second occurrence — "Part I of the **Encyclopaedia** of philosophical sciences" — treating it as the proper name of Hegel's larger three-part work (the reading `check_editions.py`'s cross-post reconcile flags as the majority/canonical form). Post 9 lowercases it.

**Rewrite:** `Hegel, G. W. F. (1991b). *The encyclopaedia logic: Part I of the Encyclopaedia of philosophical sciences with the Zusätze* (T. F. Geraets, W. A. Suchting, & H. S. Harris, Trans.). Hackett. (Original work published 1830)`

**4. Two reference entries are missing DOIs that the series has already established for the same works.**

- `Hegel, G. W. F. (2010a)` (EL main, B&D) — Posts 3 and 4 cite it with `https://doi.org/10.1017/9780511780226`; Post 9 omits it (matching only Post 6, itself unfixed).
- `Brandom, R. B. (2019)` — Post 2 cites it with `https://doi.org/10.4159/9780674239067` (confirmed against card `brandom2019spirit.md`, `doi: "10.4159/9780674239067"`); Post 9 (and 7) omit it.

**Rewrite (EL main entry):** `Hegel, G. W. F. (2010a). *Encyclopedia of the philosophical sciences in basic outline, Part I: Science of logic* (K. Brinkmann & D. O. Dahlstrom, Eds. & Trans.). Cambridge University Press. https://doi.org/10.1017/9780511780226 (Original work published 1830)`

**Rewrite (Brandom entry):** `Brandom, R. B. (2019). *A spirit of trust: A reading of Hegel's Phenomenology*. Belknap Press of Harvard University Press. https://doi.org/10.4159/9780674239067`

(Items 2–4 all surfaced by actually running `check_editions.py` against the file on disk — a genuine reconcile, not a mental approximation. Note these are distinct from the "EL split" reconcile the draft's own sourcing note defers as a series-wide, not-a-Post-9-blocker item — that split, main-vs-Zusatz per locus, is already correct in Post 9; the script's INFO lines confirm §§200–203 and §198 route to B&D and §216 Zusatz routes to Hackett, no errors. The DOI/capitalization/role-order slips are a separate, narrower defect the sourcing note never mentions.)

**5. Typo, §189 Remark paraphrase.**

> "...the system Smith, Say, and Ricardo had already described, **thought** working on an endless mass of economic detail (Hegel, 1821/1991a, §189, Remark)..."

**Rewrite:** "...the system Smith, Say, and Ricardo had already described, **though** working on an endless mass of economic detail (Hegel, 1821/1991a, §189, Remark)..."

**6. Minor — italics scope on a technical term.**

> "his preserved moment survives *as ideell*, negated into a subordinate function"

Only the German term should carry emphasis, not the English "as."

**Rewrite:** "his preserved moment survives as *ideell*, negated into a subordinate function"

**7. Very minor — inline lab-receipt citation format drifts within the piece.** The q210/q211 exhibits are cited by full path (`org_frontier/questions/q211_direct_mediator_channel/FINDINGS.md`) in "The one computed thing," but by bare question ID (`q81, q82`) in "What the ledger owes," and `STRUCTURAL_FINDINGS.md, Finding 7` in between. This is a house convention (not APA), so not wrong, but tightening to one form throughout would read cleaner. Optional, not required.

---

## What did NOT need fixing (checked and cleared)

- **Every load-bearing correction the sourcing note claims to have made is genuinely present**, verified against `library/digests/post9.md` and the source cards: the two Science of Logic sentences ("higher and richer," "nothing extraneous is introduced") are correctly re-attributed to Hegel (1816/2010b, p. 33, quoted in Maybee, 2020), not Maybee's prose; the Fuchs quotation is the verified pp. 209–210 chapter text, not the misattributed fuchsc.net enumeration; the severed-hand quote is correctly re-keyed to (Hegel, 1830/1991b, §216 Zusatz); the demotion language is fully excised; the proxy sentence is narrowed to "time-series proxies" with the q81/q82 cross-size receipt attached; Lawvere is named as a third ancestor with the categorical/non-quantitative framing intact; the HC1–HC6 tally is internally consistent (two closed / one open / one undecided / one probe / one exhibit, stated identically in both places it appears).
- **q210/q211 arithmetic is exact against the FINDINGS files** — Φ=2.000000 single triad; AND core {S1,W2,S2,C2} at Φ=3.0; OR core {S1,S2} at Φ=2.0 with the whole factoring; q210's three bridges all at Φ=2.0 with no spanning core; the mirror-core tie-break claim in the third-disanalogy paragraph matches the FINDINGS' own caveat verbatim.
- **Proxy numbers are exact**: Φ_R 0.621, Φ_WMS 0.547, edge count 0.966, surrogate in-distribution 1.000, cross-size 0.250 — all confirmed against `STRUCTURAL_FINDINGS.md` Finding 7 and the q81/q82 FINDINGS files.
- **No dangling or orphaned citations** — every in-text key resolves to a References entry and vice versa (`check_editions.py` reports zero errors of this kind for post9_ledger.md specifically).
- **All five pinned editions are used correctly and consistently**: PR only as Wood/Nisbet 1991a (no Knox leakage — the §189R and §183 material is deliberately paraphrased, not quoted, exactly as the digest recommends); EL main paragraphs only as Brinkmann/Dahlstrom 2010a; EL Zusätze only as Hackett 1991b; SL only as di Giovanni 2010b; the recognition family is exactly Brandom 2019 / Pinkard 1994 / Pippin 2008 / Honneth 1995 Polity, with no cross-contamination from the other Pinkard, Pippin, or Honneth editions that exist elsewhere in the library.
- **Reference list alphabetization and letter-suffix assignment (1991a/b, 2010a/b) are both correct** by APA 7 rules (ordered by translation year shown, suffixes assigned by title alphabetization ignoring "The").
- The residual physical-copy gates the draft's own sourcing note discloses (Nisbet Preface p. 23, di Giovanni p. 33, B&D §198/§216 English wording, Lawvere pp. 70–73 pin) are honestly flagged as still open — nothing in the digest or cards lets me close them from here, and the draft doesn't overclaim past what's verified.

## Biggest genuine strength

The rewrite is disciplined in exactly the place series work usually slips: it treats its own prior corrections as binding rather than décor. Every one of the six "load-bearing fixes this pass" claimed in the byline checks out against the primary sources when re-verified independently — the SL re-attribution, the Fuchs swap, the Hackett re-key, the demotion excision, the proxy narrowing, the Lawvere addition — and the HC6 exhibit's arithmetic (2.0 → 3.0, the asymmetric core, the containment guard) is exact to the FINDINGS files down to which four nodes are and are not in the major complex. That is the hard part of this kind of piece, and it is done. What's left is reference-list housekeeping: a citation-order slip, two missing DOIs, a reversed role order, and a capitalization drift — none of which touch a quote, a number, or a claim about Hegel or about Φ.

**Files consulted:** `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/hegel_coordination/library/digests/post9.md`, `.../library/RECEIPTS.md`, `.../library/cards/{maybee2020dialectics,fuchs2003dialectical,hegel-pr-nisbet,hegel-el-bd,hegel-el-hackett,hegel-sl-digiovanni,gunther1976dialektik,lawvere1989taco,lawvere1991category,brandom2019spirit}.md`, `.../hegel_coordination/check_editions.py` (executed against `.../posts/post9_ledger.md`), `org_frontier/questions/{q210_shared_counterpart,q211_direct_mediator_channel}/FINDINGS.md`, `org_frontier/STRUCTURAL_FINDINGS.md`, `org_frontier/questions/{q81_learned_surrogate,q82_surrogate_vs_proxy}/FINDINGS.md`, and the live draft at `.../posts/post9_ledger.md`.