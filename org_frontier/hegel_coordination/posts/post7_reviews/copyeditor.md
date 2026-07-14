# Copyedit & citation-integrity review — Paper 7, "The Necessary Middle"

**Verdict: NEAR-CLEAN, two genuine quotation-integrity defects to fix before posting.** Citations, References, dates, loci, and paraphrase discipline are almost entirely sound; the digest and the underlying repo essay both corroborate the wording. Two words sit inside quotation marks that are not in the source text, and both must be moved out.

**Single most important mechanical fix:** In the necessary/contingent definition quote (lines 30–35), the word **"because" is inside the opening quotation mark but is not in the source.** The essay reads "**It** can do integrating work…" (necessary_and_contingent_irreducibility.md, l. 8). Recast so "because" is the author's lead-in, outside the quote: `…sits in a coordination's core because "it can do integrating work the two other parties cannot reproduce…"`.

---

## A. Quotation-integrity defects (MUST FIX)

**A1. Line 30–35 — "because" fabricated inside a lab-receipt quote.**
Manuscript: `a third party sits in a coordination's core "because it can do integrating work the two other parties cannot reproduce by dealing with each other directly…"`
Source (essay l. 8, verified in repo): `It can do integrating work the two other parties cannot reproduce by dealing with each other directly…`
The verified string begins "It can do integrating work." "because" is neither in the source nor bracketed. Fix: move the opening quote mark to after "because" — `…core because "it can do integrating work…"` (lower-casing the source "It"→"it" for syntactic fit is permitted by APA without brackets). The internal ellipsis "or … a conduit" (eliding source "or it can be a conduit") is legitimate and correctly marked. Rest of the quote through "…stays in the core" matches the source verbatim.

**A2. Line 212–213 — "would" pulled inside a gated Nisbet quote (Addition to §255).**
Manuscript: `a corporation "would decline into a miserable guild system,"`
Digest (verified quotable string): `would "decline into a miserable guild system,"` — i.e., "would" sits OUTSIDE the quote.
Because Nisbet was inaccessible and this phrase is gated (`confirmed_in_primary:false`), the quotation must not run past what the digest verified. Fix: `a corporation would "decline into a miserable guild system,"`. The companion quote "a corporation is not a closed guild" (line 213) matches the digest exactly; keep. "guild" (not Knox "caste") — correct.

---

## B. Hegel primary quotations — all others PASS

| Locus | Manuscript wording | Digest check | Status |
|---|---|---|---|
| §252 (l. 65–66) | "like a second family" | matches | PASS |
| §253 (l. 68–70) | "without the honour of belonging to an estate" / "his isolation reduces him to the selfish aspect of his trade" | matches; NOT Knox "rank or dignity" | PASS |
| §207 (l. 72–73) | "recognition both in his own eyes and in the eyes of others" | matches; cited to §207 (not §§250–256); "esprit de corps" NOT quoted; rectitude framing paraphrased | PASS |
| §255 (l. 79–80) | "As the family was the first," … "so the Corporation is the second ethical root of the state" | matches | PASS |
| §255 "based in" (l. 80) | `the one based in civil society itself` — UNQUOTED | correctly left unquoted (gated single word, Nisbet not Knox "planted in") | PASS |
| §308 (l. 87–88) | "society is not dispersed into atomic units … it makes the appointment as a society, articulated into associations, communities, and Corporations" | matches; cited §308 for the deputize claim | PASS |
| §303R (l. 89–90) | "a crowd, i.e. a formless mass whose movement and activity can consequently only be elemental, irrational, barbarous, and terrifying" | matches; NOT Knox "aggregate/commotion/frightful" | PASS |
| Addition to §255 (l. 174–175) | "the abolition of Corporations in recent times" | matches; cited "Addition to §255" not §255R | PASS |

- **§288 trap:** confirmed NOT cited for representation in the body (appears only in the delete-before-posting sourcing note, l. 415, documenting its removal). PASS.
- **No Hegel page numbers anywhere.** Every PR cite is by § only. PASS.

---

## C. Lab-receipt quotes (cited inline as author's own report, NOT in References) — verified against repo files

- **Title company / escrow (l. 118–121):** matches essay ll. 82–84 verbatim. PASS.
- **Car dealer "whole Φ" (l. 124–125):** the two-word quote "whole Φ" IS verbatim in the essay (l. 42: "its whole Φ riding on the franchise law"). PASS.
- **Self-liquidating broker (l. 132–136):** the author paraphrases the run-up (unquoted) and quotes from "reads reducible: it has written itself out of the core…" through "…lacks the instrument to say so." — verbatim against essay ll. 64–67. PASS.
- **Three operations (l. 148–159):** all four fragments match post3_syllogism.md / digest verbatim; kept as three separate exact sentences, not spliced across an ellipsis. Lower-casing "The bypass counterfactual"→"the" (l. 151) is a permitted first-letter case change. PASS.
- **"The entity does not classify; the function does" (l. 275–276):** matches FINDINGS.md. PASS.
- **Margin line (l. 281–283):** "the integrating function carries margin 0 (the bypass takes nothing), the gate carries margin 2.0 (the bypass takes everything)" — matches FINDINGS.md. PASS.
- **In-silico line (l. 251–252):** matches essay l. 152. Quote closed early at "…fitted model of a market." (source continues "market, and…"); changing the terminal comma to a period is permitted by APA. PASS.
- **Category/instrument line (l. 254–255):** matches essay ll. 157–159. PASS.
- All lab receipts are cited inline (parenthetical repo paths), none appear in the References list. Correct.

---

## D. Abolition dates — ALL CORRECT

- d'Allarde: adopted 2 March / enacted 17 March 1791 (l. 165–167). PASS.
- Le Chapelier: 14 June 1791 (l. 168). PASS.
- Prussian Gewerbesteueredikt: **2 November 1810** (l. 169) — correct; NOT the 27 October Finanzedikt (correctly distinguished in the sourcing note, l. 419–423). PASS.
- Gewerbefreiheit: 7 September 1811 (l. 170). PASS.
- No Wikipedia entries in References. PASS.

---

## E. Secondary-source discipline — PASS

- **Heiman (1971):** paraphrase-only (l. 96–98); no "not a nostalgic recovery of the guild" quote; "modern institution" NOT in quotes. PASS.
- **Klikauer (2015):** "moral corporation" (l. 100) is in quotation marks. It is the book's title phrasing, and the sourcing note (l. 433) flags it as title framing rather than an attributed quotation — defensible. MINOR: consider recasting as `Klikauer's (2015) Hegel's moral corporation` to avoid reading as an interior quotation; optional.
- **James (2017):** cited, no quotation (l. 100). PASS.
- **Recognition family — Brandom (2019), Pinkard (1994), Pippin (2008), Honneth (1995):** cited as a family locating a normative-attitudinal account (l. 198), no corporation-specific claim attributed to any. PASS.

---

## F. References — order, format, orphan check

**Element order, italics, sentence case, DOIs, editor/translator credits, "(Original work published …)"** all conform and match the digest byte-for-byte:

- Alphabetical order correct: Albantakis, Brandom, Hegel, Heiman, Honneth, James, Klikauer, Oizumi, Pinkard, Pippin.
- Hegel (1991a): editor (A. W. Wood, Ed.) + translator (H. B. Nisbet, Trans.) + "(Original work published 1821)". PASS.
- Honneth (1995): (J. Anderson, Trans.) + "(Original work published 1992)". PASS.
- Heiman (1971): chapter-in-edited-book form, "(pp. 111–135)" with en-dash. PASS.
- Albantakis (2023) & Oizumi (2014): journal + italic volume, non-italic issue, "Article e…", live DOIs. PASS.
- **Two-way orphan check (10 entries expected, 10 present):** every reference is cited in the body and every body citation resolves to an entry. No orphans in either direction. PASS.
- **No Hegel page numbers in the reference entry** (only §§ in text). PASS.

**F1. NOTE (not an error): "1991a" suffix unaccompanied.** Within Paper 7's own reference list, only one Hegel 1991 work appears, so the "a" disambiguator has no "1991b" partner — nonstandard in a standalone paper. It is a deliberate series-wide pin (the digest fixes it as "Hegel (1821/1991a), matching Papers 5–6"). Keep for cross-paper consistency; flagging only so it is not mistaken for a stray letter.

---

## G. Mechanics: Φ, §, dashes, headings, byline

- **Φ symbol & first definition:** first use at l. 49 defines it — "exact integrated information (Φ; Albantakis et al., 2023; Oizumi et al., 2014)". All five later uses (ll. 111, 113, 124, 251) are the bare Φ glyph, consistent. No Φ before the definition. PASS.
- **§ conventions:** consistent throughout (§252, §253, §207, §255, §308, §303R, "Addition to §255", "§§250–256" with double-§ for the range). Body uses "§303R"; the delete-before-posting sourcing note says "§303 Remark" (l. 414) — harmless internal variance in a section that will be deleted. PASS.
- **En-dashes in ranges:** exactly 3 en-dashes, all correct — "111–135" (page range, l. 369), "§§250–256" (section range, l. 408), "author–date" (l. 460). No range mistakenly set with a hyphen. PASS.
- **Em-dash count: 60** across the body. This is high (repo house style caps at ~1/paragraph; the user's global style permits em-dashes but not pile-ups). Not an APA error, but flagged for a density pass — several paragraphs carry 3+ (e.g., ll. 302–309, 342–350). OPTIONAL cleanup.
- **Heading case:** all nine section headings are consistent title case (Level 1). PASS.
- **"draft v2" byline (l. 3–10):** self-marked "delete this byline before posting"; body-independent. PASS.
- **Sourcing note (l. 390–463):** headed "delete before posting"; body-independent (nothing in the body relies on it). PASS. Both deletion-marked blocks confirmed removable without breaking the body.

---

## H. Minor / optional

- **H1 (l. 100, Klikauer):** see E — optional recast to remove the interior-quote appearance.
- **H2 (em-dash density):** see G — optional trim.
- **H3 (Visa specifics, l. 277–280):** "authorization"→necessary and "network acceptance"→contingent are narrative (unquoted) and rest on the author's direct-file verification per the sourcing note (l. 445–446); the digest confirms the Uber pair explicitly but not the Visa pair. Low risk since unquoted; confirm against FINDINGS.md if a final pass is wanted.

---

## Pre-submission checklist

- [ ] **A1 — move "because" outside the quotation** (l. 30); quote begins "it can do integrating work". (REQUIRED)
- [ ] **A2 — move "would" outside the Addition-to-§255 quote** (l. 212); quote begins "decline into a miserable guild system". (REQUIRED)
- [ ] Delete the "draft v2" byline (l. 3–10) before posting.
- [ ] Delete the "Sourcing note" (l. 390–463) before posting.
- [ ] (Optional) Recast Klikauer "moral corporation" to avoid interior-quote reading (l. 100).
- [ ] (Optional) Trim em-dash density (60 total; target ≤1 per paragraph).
- [ ] (Optional) Cross-check Visa authorization/network-acceptance labels against FINDINGS.md.
- [ ] Confirmed clean, no change needed: all other Hegel §§ quotes; all abolition dates; Heiman paraphrase-only; all 10 References (order/italics/DOIs/translator credits); two-way orphan check; no Hegel page numbers; Φ first-definition; en-dash ranges; §288 not cited for representation; §207 (not §§250–256) for the recognition phrase.
