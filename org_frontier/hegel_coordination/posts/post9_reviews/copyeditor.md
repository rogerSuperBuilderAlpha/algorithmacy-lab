# Copyediting & citation review — Paper 9, "The Ledger" (series close)

## Verdict

**Accept with minor edits.** The manuscript is in strong mechanical shape. Every direct quotation
matches the verified digest, all q210/q211 numbers match the repo FINDINGS byte-for-byte, all six
cross-paper consistency fixes are correctly applied, the reference list is clean (12 entries, no
orphans in either direction), Hegel is cited by §/Preface with no page numbers, and Φ is defined at
first use. What remains is a small set of surgical fixes: one in-quote punctuation deviation, two
non-alphabetical multi-work citations, and a handful of minor consistency/typographic notes.

**Single most important fix:** In the Maybee "higher and richer" quotation (line 216), the source's
closed em dash "preceding—richer" has been rendered as a spaced em dash "preceding — richer." A
direct quotation must reproduce the source punctuation exactly (APA 8.30). Close the dash to match
the SEP entry.

---

## A. Quotation integrity (checked byte-for-byte against the digest)

All quotations match the digest with one exception (A1). Confirmations follow so the record is complete.

- **A1 — DEVIATION (line 216), Maybee "higher and richer."** Manuscript: "…higher and richer than the
  preceding **— **richer because it negates…" (spaced em dash, verified in the raw bytes: `g SP — SP r`).
  Source (digest): "…higher and richer than the preceding**—**richer because it negates…" (closed em dash).
  **Fix:** render `preceding—richer` with a closed em dash inside the quotation. Everything else in the
  quote is verbatim.

- **A2 — MINOR (lines 264–265), q211 super-additive quote.** Source (repo/digest) begins with a capital:
  "**The** merger is super-additive." The manuscript lowercases the first letter to fit the lead-in
  ("…the merger is super-additive: \"**the** merger is super-additive…\""). APA 8.31 permits changing the
  first letter case without brackets, so this is **permissible**. Note, however, the redundancy: the
  framing clause "the merger is super-additive:" immediately precedes a quoted sentence that repeats
  "the merger is super-additive." Consider trimming the lead-in to avoid the doubling (prose, not APA).
  The Φ=2.0 / Φ=3.0 unspaced forms inside this quote correctly reproduce the source and should be left as is.

- **A3 — CONFIRMED, owl of Minerva (lines 15–16).** "the owl of Minerva begins its flight only with the
  onset of dusk" — matches digest; Nisbet verb "begins its flight" (not Knox "spreads its wings"), "onset
  of dusk" (not Knox "falling of the dusk"). No Knox-as-Nisbet drift. Cited (Hegel, 1821/1991a, Preface).

- **A4 — CONFIRMED, grey in grey (lines 13–14).** "…it cannot be rejuvenated, but only **recognized**, by
  the grey in grey of philosophy" — Nisbet "recognized" (not Knox "understood"). Matches digest verbatim.

- **A5 — CONFIRMED, Maybee doubled meaning (line 212–213).** "both to cancel (or negate) and to preserve
  at the same time" (Maybee, 2020). Verbatim.

- **A6 — CONFIRMED, Maybee immanence (lines 223–224).** "driven by the nature, immanence or 'inwardness'
  of its own content" … "nothing extraneous is introduced" (Maybee, 2020). Verbatim.

- **A7 — CONFIRMED, Fuchs three senses (lines 294–297).** "eliminating/invalidating/dissolving/breaking up
  something (1), keeping or preserving something (2) and lifting something up (3)" (Fuchs, 2003). Verbatim.
  Used illustratively, no measure claimed — consistent with the gap the post draws.

- **A8 — CONFIRMED, severed hand short form (lines 139–140).** Quotes only "a hand in name only" (Hegel,
  1830/2010a, §216). The longer "hewn off from the body…" wording was correctly dropped.

- **A9 — CONFIRMED, state triad (lines 185–186).** "the state is a system of three syllogisms" (Hegel,
  1830/2010a, §198) — cited to the main paragraph, not the Zusatz and not §198R. Correct.

- **A10 — CONFIRMED, §189 Remark (lines 92–93).** Paraphrased, not quoted ("Smith, Say, and Ricardo… an
  endless mass of economic detail"), cited (Hegel, 1821/1991a, §189, Remark). No "interesting spectacle"
  Knox string. Matches the Paper 5 decision. (Minor note: the paraphrase "thought working on an endless
  mass" tracks Knox's phrasing closely; since it is not in quotation marks this is acceptable, but if a
  reviewer knows the Knox wording it may read as an echo — optional to loosen.)

---

## B. Lab-receipt numbers (checked against q211/q210 FINDINGS.md)

All five load-bearing numbers match the repo exactly. No corrections.

- **B1 — CONFIRMED.** Single conjunctive triad reads Φ = 2.0 (FINDINGS: "single triad triadic Φ=2.000000"). ✓
- **B2 — CONFIRMED.** NONE (no channel): whole factors, major complex one triad at Φ = 2.0 (lines 246). ✓
- **B3 — CONFIRMED.** AND core **{S1, W2, S2, C2} at Φ = 3.0**, spanning both triads, super-additive over
  2.0 (lines 249–250, 261–262). Member set and value match FINDINGS. ✓
- **B4 — CONFIRMED.** OR core **{S1, S2} at Φ = 2.0** across the triad boundary, whole still factors
  (lines 251–253). ✓
- **B5 — CONFIRMED, q210 contrast.** "every bridge's core read exactly Φ = 2.0; none produced a spanning
  core" (lines 255–256). Matches q210 FINDINGS (H2–H5 refuted, all cores Φ = 2.0, no spanning core). ✓
- **B6 — Inline sourcing correct.** Both FINDINGS are cited inline by file path as the author's own report
  (lines 246, 251, 254, 258, 266, 302) and are **not** entered in the References. Correct per the Papers
  7–8 convention.

---

## C. Cross-paper consistency (must match Papers 4–8)

All six flagged fixes are correctly landed.

- **C1 — CONFIRMED.** Pippin = *Hegel's practical philosophy: Rational agency as ethical life* (Cambridge
  University Press, 2008). Not *Hegel on Self-Consciousness* / Princeton 2011. (Reference line 402–403;
  in-text line 120.) ✓
- **C2 — CONFIRMED.** Honneth = Polity Press, 1995 (Original work published 1992). Not MIT. (Reference
  line 388–389.) ✓
- **C3 — CONFIRMED.** State-triad cited to EL §198 main paragraph (not Zusatz, not §198R). ✓
- **C4 — CONFIRMED.** §189 Remark paraphrased, not quoted. ✓
- **C5 — CONFIRMED.** Severed hand trimmed to "a hand in name only." ✓
- **C6 — CONFIRMED.** Günther dated 1976–1980, multivolume span (Reference line 378–379; in-text line 307). ✓
- **C7 — CONFIRMED.** Brandom given full "Belknap Press of Harvard University Press"; Ng given full APA
  entry. Both match Papers 4/6/7. ✓
- **C8 — CONFIRMED.** Chemism kept paraphrased throughout (lines 57–63); no unverified chemism quote
  reintroduced; loci cited (Hegel, 1830/2010a, §§200–203). ✓

---

## D. APA 7 in-text citations

- **D1 — ISSUE (line 23).** "(Oizumi et al., 2014; Albantakis et al., 2023)" is not alphabetical. APA 8.12
  orders multiple works in one parenthetical alphabetically by first author. **Fix:**
  "(Albantakis et al., 2023; Oizumi et al., 2014)." (This reorder would also need to be consistent wherever
  the pair recurs — it appears only here in the body.)
- **D2 — ISSUE (line 120).** "(Brandom, 2019; Pinkard, 1994; Pippin, 2008; Honneth, 1995)" — Honneth is out
  of order. **Fix:** "(Brandom, 2019; Honneth, 1995; Pinkard, 1994; Pippin, 2008)." Note the running prose
  (line 117, "Brandom, Pinkard, Pippin, and Honneth") may keep its rhetorical order; only the parenthetical
  must be alphabetized.
- **D3 — CONFIRMED.** Hegel cited by §/Preface throughout, no page numbers: Preface (lines 14, 16), §§200–203
  (60), §189, Remark (93), §183 (95), §216 (140), §§250–256 (176), §198 (186). ✓
- **D4 — CONFIRMED.** Maybee (2020), Fuchs (2003), Günther (1976–1980), Brandom (2019), Pinkard (1994),
  Pippin (2008), Honneth (1995), Ng (2020), Albantakis et al. (2023), Oizumi et al. (2014) all present and
  well-formed in-text. ✓
- **D5 — CONFIRMED, block-quote threshold.** No quotation reaches 40 words (the longest, the q211
  super-additive passage, is ~36 words). Inline quotation is correct; no block quote required. ✓

---

## E. References list (12 entries)

Element order, italics, sentence case, DOIs, and translator/editor credits are all correct, and every entry
matches the digest. Two-way orphan check passes.

- **E1 — Orphan check, entries → in-text.** All 12 entries are cited in the body: Albantakis (23),
  Brandom (120), Fuchs (298), Günther (307), Hegel 1991a (14+), Hegel 2010a (60+), Honneth (120),
  Maybee (213+), Ng (52), Oizumi (23), Pinkard (120), Pippin (120). No uncited entries. ✓
- **E2 — Orphan check, in-text → entries.** Every in-text author-date has a matching entry. No IIT cite
  without an entry; no recognition-family name (Brandom/Pinkard/Pippin/Honneth) listed-but-uncited or
  cited-but-unlisted. ✓
- **E3 — CONFIRMED, SEP-article form.** Maybee, J. E. (2020). Hegel's dialectics. In E. N. Zalta (Ed.),
  *The Stanford encyclopedia of philosophy*. Metaphysics Research Lab, Stanford University.
  https://plato.stanford.edu/entries/hegel-dialectics/ — correct APA form for an SEP entry; live /entries/
  URL per house convention. ✓ (Optional: APA allows appending the edition, e.g. "(Summer 2020 ed.)"; the
  digest treats the live URL as standard, so no change needed.)
- **E4 — CONFIRMED, Günther multivolume.** *Beiträge zur Grundlegung einer operationsfähigen Dialektik*
  (Vols. 1–3). Felix Meiner. Year span 1976–1980; German noun capitalization correct (Beiträge, Grundlegung,
  Dialektik capitalized; operationsfähigen lowercase). ✓
- **E5 — CONFIRMED, translated primaries.** Hegel 1991a (Wood, Ed.; Nisbet, Trans.), Hegel 2010a (Brinkmann
  & Dahlstrom, Eds. & Trans.), Honneth (Anderson, Trans.) all carry "(Original work published …)". ✓
- **E6 — CONFIRMED, journal articles.** Albantakis et al. (2023) and Oizumi et al. (2014): journal in title
  case italic, volume italic, issue in parentheses, Article e-number, working DOI links. ✓
- **E7 — CONFIRMED, sentence case + retained proper nouns.** Book titles in sentence case with legitimate
  caps preserved (Phenomenology, Part I: Science of logic, Aristotle-free). British "-isation" in the Fuchs
  entry correctly reproduces the source. ✓

---

## F. Symbols, dashes, headings, deletable apparatus

- **F1 — CONFIRMED, Φ first definition.** Φ is introduced and defined at first use (lines 21–23: "the degree
  of that irreducibility is Φ, computed by finding the partition that does the least damage…"). All later
  uses ("Φ = 2.0", etc.) follow the definition. ✓
- **F2 — Φ spacing.** Author's own prose uses spaced "Φ = 2.0/3.0" consistently; the unspaced "Φ=2.0/3.0"
  appears only inside the verbatim q211 quote (lines 264–265), which is correct. No inconsistency to fix. ✓
- **F3 — CONFIRMED, en dashes in ranges.** All ranges use en dashes, no hyphens: §§200–203, §§250–256,
  1976–1980, pp. 195–244, Vols. 1–3, Papers 4–8. Grep for digit-hyphen-digit and §§n-n ranges returns
  nothing. ✓ (13 en dashes total.)
- **F4 — Em-dash count.** 56 em dashes in the body (lines 13–360); 57 in the file. This is heavy but within
  the series' house style (em dashes are allowed). No mechanical defect, but if tightening is wanted the
  densest clusters are lines 234–235, 283–286, and 314–319. One of the 56 (line 216) is the in-quote dash
  flagged in A1 and must be closed regardless.
- **F5 — Heading case.** All H2 headings are sentence case and consistent. Minor: *Aufhebung* in the H2
  "Aufhebung against the operators" (line 198) is not italicized, though it is italicized as a foreign term
  in the body (lines 211, 294). Optional consistency fix: italicize it in the heading, or leave per house
  practice.
- **F6 — Foreign-term italics (minor).** *Not- und Verstandesstaat* (93), *Glied* (143), *Aufheben* (211),
  *Aufhebung* (294), *operationsfähige Dialektik* (306) are italicized. **Korporation** (172, 179) and
  *avant la lettre* (109) are not. For internal consistency, either italicize Korporation and avant la lettre
  or accept both as naturalized. Low priority.
- **F7 — CONFIRMED, deletable apparatus is body-independent.** The "draft v2" byline block (lines 3–9) and
  the "Sourcing note" (lines 407–461) are both marked "delete before posting." The body cites every source
  inline and never points the reader to the byline or the sourcing note; the References list is separate and
  survives deletion. Removing both leaves the post intact. ✓
- **F8 — Sourcing note, minor factual slip (deletable, so low priority).** Line 447 says q210 "produced no
  spanning core in any of its **five conditions**." q210 has three bridge rules (none/AND/OR); "n = 5"
  refers to five hypotheses (H1–H5), not five conditions. If the note is kept for any reason, change to
  "three bridge conditions." Since the note is slated for deletion, this need not block posting.
- **F9 — Quote characters.** Straight quotes/apostrophes throughout (0 curly), consistent; Substack will
  curl them on publish. No double spaces in body text (the grep hits are markdown list indentation in the
  deletable sourcing note). ✓

---

## Pre-submission checklist

1. [ ] **A1 (required):** Close the em dash inside the Maybee quote — `preceding—richer` (line 216).
2. [ ] **D1 (required):** Alphabetize line 23 → "(Albantakis et al., 2023; Oizumi et al., 2014)."
3. [ ] **D2 (required):** Alphabetize line 120 → "(Brandom, 2019; Honneth, 1995; Pinkard, 1994; Pippin, 2008)."
4. [ ] **A2 (optional):** Trim the "the merger is super-additive:" lead-in so it does not double the quoted sentence.
5. [ ] **F5/F6 (optional):** Decide italics policy for *Aufhebung* in the heading, and for Korporation / avant la lettre.
6. [ ] **Delete before posting:** the "draft v2" byline block (lines 3–9) and the "Sourcing note" (lines 407–461).
7. [ ] **Gate to clear before posting (author task, per sourcing note):** confirm the Nisbet Preface wording
   (owl of Minerva; grey in grey) against the printed Wood/Nisbet edition — this is the one new primary
   passage; every other Hegel claim carries over from Papers 4–8.
8. [ ] Confirm no page numbers were reintroduced on any Hegel cite during edits. (Currently clean.)
9. [ ] Re-run the two-way orphan check after any citation edits.
