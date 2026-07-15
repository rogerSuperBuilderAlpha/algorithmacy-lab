# Copyeditor / APA 7 / citation-integrity review — Paper 8, "At Home in the Other"

**VERDICT: Near-ready. Quotation integrity is clean — all nine Hegel quotes and all four lab-receipt
quotes match the digest/repo verbatim in the correct editions, with no Baillie/Knox drift and no page
numbers. Three mechanical defects block submission: two orphaned reference entries, one under-set block
quote, and one mis-attributed lab-doc file pointer.**

**Single most important mechanical fix:** Two References entries are never cited in the body —
**Honneth (1995)** and **Roy (2006)**. This is a two-way integrity failure a reviewer catches on first
pass. Either cite each in-text or delete the entry. (Roy is the intended scholarly hook for
*Beisichselbstsein im Anderen*; add "(Roy, 2006)" at first use of the German phrase. Honneth has no
natural in-text home and should be cut.)

---

## A. Quotation integrity — every Hegel quote checked against the digest (ALL PASS)

Each verified byte-for-byte against `post8_digest.md`, tagged to the correct edition, correct §/¶, no
page numbers.

1. Line 38 — "is raised to the status of an actual shape and passion" (Hegel, 1821/1991a, §5, Remark).
   Nisbet wording ✓ (not Knox "rises to a passion").
2. Line 44 — "the fanaticism of destruction of the whole existing social order" (§5, Remark).
   Correct Nisbet "**existing**" ✓ (not Knox "subsisting").
3. Line 38 — "the freedom of the void" ✓ (shared Knox/Nisbet, safe).
4. Lines 50–52 — "The sole work and deed of universal freedom is thus death, namely, a death which has
   no inner amplitude and no inner fulfillment…" (Hegel, 1807/2018, ¶590). Pinkard verbatim ✓.
5. Lines 52–54 — "It is therefore the coldest, emptiest death of all, having no more meaning than
   chopping off a head of cabbage or swallowing a mouthful of water" (Hegel, 1807/2018, ¶590). Pinkard
   verbatim ✓ — correctly SWITCHED from Baillie (no "cold-blooded/meaningless," "cleaving," or
   "draught").
6. Lines 76–77 — "freedom is precisely this: to be at home with oneself in one's other, to be dependent
   upon oneself, to be the determining factor for oneself" (Hegel, 1830/1991b, §24 Addition 2). GSH
   verbatim ✓ — "**precisely** this," "for oneself." The v1 trap ("just this" / "in oneself") is
   correctly avoided.
7. Line 78 — "Freedom exists only where there is no other for me that I am not myself" (§24 Addition 2).
   GSH verbatim ✓.
8. Lines 92–94 — "we already possess this freedom in the form of feeling … but willingly limit ourselves
   with reference to an other, even while knowing ourselves in this limitation as ourselves" (Hegel,
   1821/1991a, §7 Addition). Nisbet verbatim ✓ — correctly avoids Knox "limits himself with pleasure."
   (See B-3: length triggers block-quote rule.)
9. Lines 97–98 — love as "the consciousness of my unity with another," "I am not isolated for myself …
   but win my self-consciousness only through the giving-up of my independence" (§158 Addition). Nisbet
   verbatim ✓.
10. Line 122 — "The state is the actuality of concrete freedom" (§260). Shared Knox/Nisbet ✓; the
    continuation (lines 123–128) is correctly left as paraphrase, unquoted, per the gate.

No explicit "Terror"/"French Revolution" phrase is attributed to §5 Remark ✓. The word "terror"
(line 49) and "absolute freedom" (line 48) are the author's own gloss on the Phenomenology, not
claimed as §5R quotes.

**Edition disambiguation is correct throughout:** PR = 1991a (lines 39, 44, 70, 94, 100, 122); EL =
1991b (77, 78); PhG = 2018 (52, 54). All Hegel cited by §/¶ only, zero page numbers ✓.

## B. Lab-receipt quotes — checked against the repo files (3 of 4 file pointers correct)

All four quotes are verbatim-correct against the source files. One file **attribution** is wrong.

1. Lines 151–152 — definition "the autonomy proper to being irreducibly coordinated — standing and
   effective voice within a mediation one cannot leave, rather than independence from it or control over
   it" → matches `coordinative_sovereignty/README.md` lines 7–8 verbatim ✓. Cited inline, not in
   References ✓.
2. Lines 153–154 — "Digital sovereignty asks who owns the infrastructure; coordinative sovereignty asks
   what autonomy the actor coordinating through it can have" → README lines 11–12 verbatim ✓.
3. Lines 156–157 — "Its currency is voice, made effective — not the chance to speak, but terms that hold
   because the coordinated actors have the standing to make them hold" (coordinative_sovereignty.md) →
   `coordinative_sovereignty.md` lines 59–60 verbatim ✓, correct file ✓.
4. Lines 305–306 — "introduces no new computation." / "The bridge to organizations is unbuilt: the
   parties are nodes in a Boolean model, and standing is explored on those models, not measured on any
   firm" (instruments/formal_standing.md) → `formal_standing.md` lines 7 and 88–90 verbatim ✓.
   Critically, the phrase is the CORRECT "**The bridge to organizations is unbuilt**," NOT the misquote
   "the game is unbuilt" ✓.

**B-ATTRIBUTION ERROR (line 176):** the q213 hinge "exit where a gate is contingent, voice where a
mediator is necessary" is cited as `(coordinative_sovereignty.md)`, but that verbatim phrase does not
appear in `coordinative_sovereignty.md`. It appears in `coordinative_sovereignty/README.md` line 15.
(The digest also mis-pointed this to coordinative_sovereignty.md; the repo is the ground truth.)
**Fix:** change the inline pointer at line 176 to `(coordinative_sovereignty/README.md)`. The quotation
itself is verbatim-correct.

## C. Reference orphans — two-way check

Eleven entries; nine cited, two orphaned.

- **ORPHAN 1 — Honneth (1995), lines 375–376.** Appears only in References. Body says "Recognition
  theorists" generically (line 199), never "Honneth." Not in the digest's APA list either. **Cut it**,
  or add "(e.g., Honneth, 1995)" at line 199.
- **ORPHAN 2 — Roy (2006), lines 387–388.** Appears in References and in the deletable sourcing note
  (line 453) only — never in the body proper. The German phrase *Beisichselbstsein im Anderen*
  (lines 25, 149) is Roy's hook and is uncited. **Add "(Roy, 2006)"** at line 24–25 or 149, or cut the
  entry.
- Cited-and-listed (all confirmed present both places): Albantakis et al. (2023), Berlin (1958/1969),
  Hegel (1821/1991a), Hegel (1830/1991b), Hegel (1807/2018), Hirschman (1970), Neuhouser (2000), Oizumi
  et al. (2014), Patten (1999) ✓. No in-text cite lacks an entry ✓.

## D. APA 7 mechanics

- **D-1 (block quote, lines 92–94):** the §7 Addition quotation runs **41 words** and is set run-in with
  quotation marks. APA 7 requires quotations of **40+ words** to be set as a block quote (indented, no
  surrounding quotation marks, parenthetical citation after the closing period). **Reformat as a block
  quote.** This is the only quote in the piece that crosses the threshold — all others are ≤26 words or
  are separate interwoven fragments.
- **D-2 (locator format inconsistency):** Remark citations use a comma — "§5, Remark" (lines 39, 44) —
  while Addition citations do not — "§7 Addition" (94), "§158 Addition" (100), "§24 Addition 2" (77–78).
  Standardize to **"§5 Remark"** (no comma) to match the Addition style.
- **D-3 (inline lab-doc pointer style):** the README is cited with the folder — "coordinative_sovereignty/
  README.md" (lines 152, 154) — but the framing doc as a bare "coordinative_sovereignty.md" (157, 176).
  Pick one convention; recommend the folder-prefixed form for both.
- **References list — all nine cited entries PASS:** element order, italics (journal + volume; book
  titles), sentence case, translator/editor credits, and "(Original work published …)" are all correct.
  DOIs are full https URLs ✓. Alphabetical order correct; Hegel 1991a/1991b suffixing is correct
  (title-alphabetized: *Elements* before *encyclopaedia*), matching in-text PR = 1991a / EL = 1991b ✓.
  Page ranges use en-dashes (Berlin 118–172, Roy 225–255) ✓. Roy's title-internal quotation marks are
  part of the actual title and match the digest — keep as-is.

## E. Symbols, dashes, headings, byline

- **Φ:** defined at first substantive use — "exact integrated information (Φ; Albantakis et al., 2023;
  Oizumi et al., 2014)" (line 181) — and used consistently thereafter (309) ✓. Multiple-work
  parenthetical is alphabetical ✓.
- **En-dashes:** correct in all ranges (page ranges above; "Papers 5–7," line 439) ✓. No range uses a
  hyphen where an en-dash is required.
- **Em-dashes:** 55 in the file. Heavy (~11 per 1,000 words of body). The series register and the global
  house style permit em-dashes, so this is not an APA error, but recommend one pass to break up any
  pile-ups. (Style note, not a blocker.)
- **Headings:** all H2 section heads and the H1 title are consistent title case ("Freedom Lives in
  Institutions, or It Does Not Live," "Coordinative Sovereignty Is This Claim in the Lab's Grammar,"
  etc.) ✓.
- **Byline (lines 3–11) and Sourcing note (lines 392–457):** both explicitly marked "delete before
  posting," and the body does not depend on either ✓. No action beyond the marked deletion. (Note: the
  "byline" is really a mini sourcing note; that is fine since it is flagged for removal.)

## F. Low-priority note

- Line 48 — "absolute freedom" in quotation marks reads as a term-of-art reference to the Phenomenology
  section title, not a claimed verbatim translation, so it needs no locator. If intended as a Pinkard
  quotation, add ¶. As written, acceptable.

---

## Pre-submission checklist

- [ ] Cut Honneth (1995) from References (or add an in-text cite at line 199).
- [ ] Add "(Roy, 2006)" at the first *Beisichselbstsein im Anderen* (line 24–25 or 149), or cut Roy.
- [ ] Reformat the 41-word §7 Addition quote (lines 92–94) as an APA block quote.
- [ ] Fix the file pointer at line 176: coordinative_sovereignty.md → coordinative_sovereignty/README.md.
- [ ] Standardize section locators: "§5, Remark" → "§5 Remark."
- [ ] Unify inline lab-doc citation style (folder prefix on both README and framing doc).
- [ ] Delete the draft-v2 byline (lines 3–11) and the Sourcing note (lines 392–457) before posting.
- [ ] Optional: one pass to thin em-dash pile-ups.
- [ ] Confirmed clean, no action: all Hegel quotes verbatim in correct editions; "bridge to
      organizations is unbuilt" correct; Φ defined at first use; no page numbers on any Hegel cite;
      three-edition disambiguation and 1991a/1991b suffixing correct.
