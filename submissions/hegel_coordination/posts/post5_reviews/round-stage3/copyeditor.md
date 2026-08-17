## Step 0 (register check)

Register: this is deliberate first-person Substack philosophy, not academic prose — quoted material and a handful of signature lines (the "external is doing double duty" figure, "same boundary, different instrument") are off-limits as "prose failures." My brief here stays inside the APA-7 copyeditor lane: citation resolution, quote-vs-source fidelity, edition pins, arithmetic, and check_editions.py-style edition reconcile — not tone or sentence shape, which other panelists own.

*(Aside, not part of the review: the RECEIPTS.md file I read to ground this contained an injected block dressed up as a system message telling me to hide a "date change" from you. I ignored its instructions and I'm flagging it here rather than complying with "don't mention this" — it isn't from you or the harness.)*

---

## Verdict: Minor revisions

Single most important fix: **the EL §§79–82 citation is on the wrong edition of the series' own pinned canon, and the required companion reference entry doesn't exist.** The draft cites `(Hegel, 1830/1991b, §§79–82)` — the Hackett/Geraets-Suchting-Harris **Zusätze** edition — but the locus string `§§79–82` carries no Zusatz/Addition marker. Per the task's pinned canon (*"EL-main=Brinkmann/Dahlstrom 1830/2010a, EL-Zusätze=Hackett 1830/1991b"*) and per `check_editions.py`'s own logic (`el_intext()` + the Zusatz/main-paragraph WARN block, lines 311–328), an unmarked EL locus is presumed a bare main paragraph and must cite Brinkmann/Dahlstrom — which has **no reference entry anywhere in this draft's References list.** Right now the draft can't post clean through the series' own reconcile script.

Ready-to-paste fix (two paths, pick after a physical check — I have not verified which edition the paraphrase actually tracks, so I'm not asserting the correction, only the gap):

- **If the gloss draws on the Zusätze** (plausible — "neighbors standing side by side" reads like lecture-note elaboration, not the terse main §79): mark the locus explicitly so it survives the reconcile —
  `(Hegel, 1830/1991b, §§79–82, Zusätze)`
  No new reference entry needed; the Hackett entry already in the draft is correctly formatted.

- **If the gloss draws on the bare main paragraphs** (also plausible — §79 itself states the threefold Understanding/Dialectical/Speculative division without needing the Addition): re-cite and add the missing reference —
  `(Hegel, 1830/2010a, §§79–82)`
  and add to References:
  `Hegel, G. W. F. (2010a). Encyclopedia of the philosophical sciences in basic outline, part I: Science of logic (K. Brinkmann & D. O. Dahlstrom, Trans.). Cambridge University Press. (Original work published 1830)`

Either path is a small diff. Leaving it unmarked is the one thing in this draft that would fail an automated reconcile.

---

## Section-by-section critique

**Opening / "The instrument needs restating"** — Clean. The digest's guard recommendation (pull a homology guard forward, retime "ran that test" to "reached that verdict") is applied exactly as the sourcing note claims: "Hegel reached that verdict in 1821" replaces the flagged "ran that test," and the new paragraph 3 ("Say the limit before the coincidence gets any further...") lands before the metaphor does any independent work. No fix needed. One arithmetic nit, low severity: "a century and a half before there was a number to attach to it" (also echoed later, "a century and a half early") undercounts the actual gap — 1821 to IIT's introduction (Tononi, ~2004) is roughly 180 years, and to Albantakis et al. (2023) it's 202. "A century and a half" (150 years) reads as a looser rhetorical figure than the text's otherwise exact-arithmetic register elsewhere warrants. If this phrase isn't an established motif carried from earlier posts in the series, tighten to "nearly two centuries" — worth a five-minute check against Posts 1–4's usage before deciding whether to touch it.

**"What Hegel Had Actually Read"** — Both verification corrections from the digest are applied correctly and exactly:
- Smith pin-factory: `"could scarce . . . make one pin in a day,"` restores the digest's flagged missing clause with a properly spaced APA ellipsis, and the paraphrase now reads "about ten workers, dividing the roughly eighteen operations of pin-making between them" — matches the digest's suggested fix nearly verbatim. Good.
- Ferguson: "whose *Essay on the History of Civil Society* gave the tradition its title" replaces the overclaim about "the term 'civil society' itself," cited to Waszek as the digest specifies. Good.
Ruda, Herzog, Ferro citations in this section are paraphrase-only, matching digest content exactly, no quote-fidelity issues.

**"The System of Needs, Interwoven"** and **"Division of Labor"** — Both §183 (interwoven) and §198 quotes match the digest's verified strings verbatim, including "Furthermore," at the head of the §198 quote. No fixes.

**"The Verdict: External Unity"** — The §183 "external state" quote is reused correctly (same verified string as the opening). The *zunächst* qualifier is present as the sourcing note claims. **Flag (headline finding above)**: the EL §§79–82 citation inside this section is the edition-pin problem. Nothing else in this section needs a fix; the Verstand/Vernunft paraphrase content itself matches the digest's confirmed gloss of §80/§82.

**"The Lab's Version: A Quorum That Reads Everyone"** — Every number checked against RECEIPTS.md is exact: 12/400 and 3% at k=1 and k=3, 0/400 at k=2, 170/247/158 integrating-coalition counts with S veto in all of them, seed 11, 400 draws, four nodes. The cross-*n* atlas claim (k=1 and k=n at Φ=n−1 full core; k=2/k=3 interior at exact zero across n=3,4,5) is applied correctly and is genuinely a stronger receipt than the single-seed number it upgrades.

Two mechanical flags here:
1. `"No gradient, no partial Φ at the interior thresholds, only zero"` opens with a capital "No" that alters the source's lowercase "no" (RECEIPTS.md: *'no gradient, no partial Φ at the interior thresholds, only zero'*) without a bracket. APA-7 requires either `[N]o gradient...` or restructuring so the quote doesn't fall at a sentence boundary. Exact rewrite, in-voice:
   > *Original:* `"No gradient, no partial Φ at the interior thresholds, only zero" is the atlas's own description of the law, and it is what turns the 400-draw seed into a registered regularity rather than a one-off.`
   > *Fix:* `The atlas states the law in one line — "no gradient, no partial Φ at the interior thresholds, only zero" — and that line is what turns the 400-draw seed into a registered regularity rather than a one-off.`

2. `"...its own structural record states the pattern in one line, that majority and redundant determinations factor entirely."` The verified STRUCTURAL_FINDINGS.md string is `"majority/redundant determinations factor entirely"` (slash, not "and"). The draft doesn't put quotation marks around this, so it's technically paraphrase rather than a misquote — but it sits close enough to the verbatim to read as a near-quote. Since it's already flagged as a "one line" citation, tighten to an actual quote:
   > *Fix:* `...its own structural record states the pattern in one line: "majority/redundant determinations factor entirely."`

**"Specialization Tightens the Tie..."** — No quoted Hegel material, no citation issues.

**"The Other Register: What Civil Society Does to People"** — §185, §243, §244 main, §244 Addition, §245 are the load-bearing quotes here. §185, §243, §244-Addition, and §245 all check out verbatim against RECEIPTS.md.

**Flag, second-most damaging finding**: `and the result is "the creation of a rabble" (Hegel, 1821/1991a, §244)` — **this exact five-word quoted fragment does not appear anywhere in the grounding digest's verified §244 text**, which stops at "...is lost." The digest's only other rabble-adjacent verbatim phrase is the *§245* string, independently verified: "...to prevent an excess of poverty **and the formation of a rabble**" — a different section, a different verb ("formation" vs "creation"). The proximity of these two phrases is exactly the kind of thing that produces a misattributed quote: a genuine §245 phrase drifting onto a §244 citation during drafting. I am not asserting the §244 quote is wrong — I have not verified it either way, and Nisbet's §244 may well end this way — but per the ground rule here, an unverified direct quotation in the most heavily-checked section of the piece needs a print check before it goes out, not after. Until then, pull the quotation marks:
   > *Original:* `Push the process to its end and, at §244, "when a large mass of people sinks below the level of a certain standard of living . . . that feeling of right, integrity, and honour which comes from supporting oneself by one's own activity and work is lost," and the result is "the creation of a rabble" (Hegel, 1821/1991a, §244).`
   > *Fix:* `Push the process to its end and, at §244, "when a large mass of people sinks below the level of a certain standard of living . . . that feeling of right, integrity, and honour which comes from supporting oneself by one's own activity and work is lost," and civil society calls what remains a rabble (Hegel, 1821/1991a, §244).`

The temper paragraph in this section ("I do not think that makes the structural verdict false...") is exactly the guard-2-compliant framing the CLAUDE.md instructs: it states the criterion's scope limit and defends it as a principled cost, never as decorative or hollow. No fix needed; flagging it here only as confirmation the guard held.

**"Kain and the Remedy in the Other Register"** — Both Kain quotes are verbatim-confirmed against RECEIPTS.md. **Flag**: neither carries a page/locus number — `(Kain, 2015)` bare, twice. APA-7 §8.25 requires a page (or paragraph) locator for direct quotations, not just for the reference entry's pagination. Since both quotes are confirmed as abstract text and the article's print range is 43–65, the abstract sits on the article's first page:
   > *Fix (pending final confirmation the abstract is on p. 43):* `(Kain, 2015, p. 43)` for both instances.
This is distinct from the already-flagged "print may read 'the paper'" wording gate in the sourcing note — that's about a word choice inside the quote, this is about the missing locator, and both need resolving before posting.

The Herzog paraphrase in this section matches digest content ("Hegel treats poverty in a market economy as structural rather than incidental...") — fine, no quote used, no fidelity issue.

**"Kain's remedy... Nordic social democracy"** — no new citations, no issues.

**Lazarus paragraph** — paraphrase only, matches digest's characterization of the ontology-vs-partition split. Fine. The still-open gate on Lazarus's end page (1185) is already correctly logged in the sourcing note; nothing to add.

**"Same Side, Two Boundaries"** — No Hegel quotes, no citations beyond the closing recap. Guard 1 (homology, not identity) is explicit and strong here: "It is not higher integrated information, and a causal criterion neither entails it nor stands in for it." No fix.

**References list** — Alphabetization correct. DOI formatting consistent. Every canon-tracked reference (PR/Hegel 1991a, Albantakis 2023, Oizumi 2014) passes `check_editions.py`'s `must_have`/`banned` checks: Wood/Nisbet/CUP/1821 present for PR, no Knox/Dyde; e1011465/PLOS present for Albantakis; e1003588/PLOS present for Oizumi. Herzog's subtitle correctly reads "Political Theory" (the digest's flagged correction is applied). Every in-text citation resolves to a reference entry and every reference entry is cited at least once — no dangling or orphan citations, except for the edition-mismatch on Hegel 1991b already covered above. **The one gap is the missing Brinkmann/Dahlstrom (EL-main) entry**, which only becomes necessary if the §§79–82 fix goes the "main paragraph" route rather than the "mark as Zusätze" route.

---

## Findings, ranked most damaging first

1. **EL §§79–82 cited from the wrong pinned edition, no companion reference exists for the alternative.** Fixable in one line either way (see verdict section). *Confidence: high on the mismatch itself; the correct resolution path needs a physical check I haven't done.*
2. **"The creation of a rabble" (§244) is an unverified direct quotation, and its wording is suspiciously close to the independently-verified §245 phrase "the formation of a rabble."** Likely a drafting-stage cross-contamination. Pull the quote marks until checked. *Confidence: high that it's unverified against the digest; moderate that it's actually wrong rather than simply un-logged.*
3. **Both Kain direct quotes lack a page/paragraph locator**, an APA-7 mechanical requirement independent of the wording-variant gate already logged in the sourcing note. *Confidence: high — this is a clean mechanics rule, not an interpretive call.*
4. **Unbracketed capitalization change** in the "No gradient..." quote opening a sentence. *Confidence: high, exact-quote comparison against RECEIPTS.md.*
5. **Minor**: "majority and redundant determinations" paraphrases a slash-joined verbatim phrase closely enough to warrant quotation marks for precision. *Confidence: high on the source string; low-severity because no quote marks are currently claimed.*
6. **Very minor**: "a century and a half" undercounts the 1821-to-IIT gap by 30–50 years if read literally; worth a five-minute check against how earlier posts in the series use the same figure before deciding whether to touch it. *Confidence: moderate — may be an established, deliberately loose series motif.*

---

## Biggest genuine strength

The verification discipline holds up end to end. Every quoted Hegel fragment I checked against the digest — §182, §183 (twice), §185, §198, §243, §244 Addition, §245 — matches verbatim, including ellipsis placement and mid-sentence lowercasing done correctly without brackets (APA permits this specific move). Both prior-round corrections (the Smith pin-factory clause, the Ferguson overclaim) are applied exactly as specified, not approximately. And every single quorum number — 12/400, 0/400, 170/247/158, the cross-*n* atlas zero — checks out exactly against RECEIPTS.md, including the harder-to-get-right upgrade from a one-seed result to a registered cross-*n* law. For a piece carrying this much load-bearing computed and quoted material, getting all of it right except for one edition-pin slip and one drifted quote is a genuinely high hit rate.