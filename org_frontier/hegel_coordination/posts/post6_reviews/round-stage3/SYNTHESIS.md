Verified against ground truth. The panel's central contradiction resolves cleanly, and against the draft's favor: the two reviewers who caught the Zusatz-edition slip are right. Here is the synthesis.

---

# Post 6 "Parts and Members" — Five-Reviewer Synthesis (v-next change-list)

**Panel verdict:** unanimous MINOR REVISIONS (one reviewer flags a single gate that could escalate to MAJOR — the Zusatz edition — which I adjudicate below as a confirmed fix, not merely a gate). Every computed number is verbatim-correct. Both series guards hold, with one residual-risk zone named at the end.

**Adjudication method:** anything touching a number or an edition pin was checked against `library/RECEIPTS.md`, `library/digests/post6.md`, and — for the contested edition question — `check_editions.py`, `library/cards/hegel-el-bd.md`, and the parallel practice in Posts 5/8/9.

---

## GUARD CONFIRMATION (both hold)

- **Guard 1 (homology, not identity):** CLEAN, all five reviewers + digest. The draft disclaims anticipation explicitly ("he does — but not by anticipating my criterion… He wins by defining a member in terms my instrument was built without"). No breach anywhere. Keep this altitude.
- **Guard 2 (no demotion of Φ):** HOLDS. No banned term (calculator/decorative/hollow/unnecessary) touches Φ; "decoration" is correctly pinned to the Hegel *bridge* under a counterfactual that did not obtain, exactly as the digest blesses. **One residual-risk zone** (temper paragraph) — see Substantive #5 and the flag at the bottom.

---

## SUBSTANTIVE FIXES (argument / guard), ranked

**S1. "about the state, not the body" contradicts its own quote. [3 reviewers: hegel_specialist, formal_specialist, reviewer2_hostile]**
The §278R quotation's grammatical subject is "an animal organism" — the body. Framing it "about the state, not the body" fights the sentence a hostile reader reads next. Reframe as the organism-as-figure-*for*-the-state.
Exact change: replace "and about the state, not the body:" with a version that keeps the body as the figure — e.g. "…and states it of the animal organism in the middle of an argument about the state: '…' (Hegel, 1821/1991a, §278R). He reaches for the body to say what he means by a member of a state."

**S2. "argmax over every way the system could be partitioned" misstates IIT. [2 reviewers: formal_specialist, reviewer2_hostile — verbatim-grounded, self-contradicting]**
The major complex is the argmax over **subsets**; partition is the *minimization* (the MIP, the cut that costs least) that defines φ_s for a fixed subset. RECEIPTS line 50 / digest line 50 quote the source: "the subset that maximizes φ_s, the argmax of the characteristic function" — over subsets. The draft's own earlier clause gets it right, so this clause both misdescribes the machinery and self-contradicts.
Exact change: "where φ_s is the integrated information a given subset carries — each subset scored at the cut that costs it the least — and the winner is the argmax over every subset the system could pick out." (restores both the min-over-partitions and the max-over-subsets).

**S3. Severed hand + federation listed among computed receipts. [reviewer2_hostile]**
"The Documented Middle" lists "the severed hand, the federation with a flag, the rotating triad" as cases the test "reads." Only the rotating triad is computed (RECEIPTS line 70: no I/P/U triad built; Post 4 records zero self-production/hand models). Guard-adjacent: do not let a reader hear three receipts where there is one. Mark the hand and federation explicitly as *homological* illustrations there, the rotating triad as the computed case.

**S4. "shadow of the same thing" quietly settles the open question in the instrument's favor. [hegel_specialist, deepest single-reviewer catch]**
"Attractor-defense is the closest dynamical shadow of self-maintenance, and it is still a shadow" concedes the two are shadows *of one object*. A Kreines-realist denies even that — Hegel's self-production is a distinct causation (the whole as cause of its own parts) that may never enter the transition table Φ is read from. This *widens* the HC1 gap the draft wants to keep honest. Append (in voice): "— and I cannot yet say whether it is a dim image of the same thing or an image of something else entirely, a causation of the whole by itself that never reaches the transition table my Φ is read from. The φ-matched pair is the run that would tell me which." Optional but strengthens the gap-as-finding discipline; does not touch a guard the wrong way.

**S5. Temper paragraph — residual Φ-demotion risk (guard holds, but de-risk). [reviewer2_hostile HIGH, formal_specialist LOW, voice_reader; digest gate (e)]**
The paragraph clears the guard (ranking is pinned to Hegel; the sanctioned Paper-4 line "that consistency is the test doing its job, not failing it" is present). It still *leans*: it frames the instrument's determinateness as a "cost" and doubles the demotion ("speaks with total confidence about… the shallower of the two questions" + "never the smaller half"), quotable out of context. Minimum fix (formal_specialist): relativize unmistakably — "a boundary that, in Hegel's ordering, is the shallower of the two questions." Stronger fix (reviewer2_hostile): drop the doubling, stop calling the instrument's confidence a cost, pin the concession to symptom-not-direction: "What the verdict cannot reach is the coordinate Hegel cared about most… The instrument reads the cut, and reads it exactly; what it does not read is what the interrupted thing was for. That is the seam between the two holisms this series keeps — not a defect in either…" **Adopt the stronger rewrite** — it is the one place the piece can be quoted against itself. Keep the attractor/thermostat argument and the narrow-claim refusal exactly as written (all five praise them).

---

## FORMAL FIXES (citation / edition / number)

**Numbers: nothing to change.** Every computed figure is verbatim against RECEIPTS lines 60–71 — 115 of 115, 13% vs 10%, 0 of 78, top share 0.333, the finding-8 quotes, the {S, P} contraction, and the correct assertion that no Φ number exists for the I/P/U state triad. Φ is verdict-not-scale throughout. Confirmed by formal_specialist and voice_reader independently; I re-checked. No number mismatch exists.

**F1. [MAJOR — ADJUDICATED] Re-pin both Zusatz citations to Hackett 1830/1991b and add the Hackett reference. [copyeditor MAJOR + reviewer2_hostile gate]**
This is the panel's one real contradiction. hegel_specialist and formal_specialist left the §216-Addition and §135-Addition cites at B&D 2010a, relying on digest line 19 ("B&D prints the Zusaetze"). **They are wrong; copyeditor and reviewer2_hostile are right.** I verified directly:
- `check_editions.py` lines 131–135, 321–324: "the series pins **ALL** Zusätze to the Hackett edition even though Brinkmann/Dahlstrom carry a selection of Zusätze" — and it emits a WARN when a Zusatz is cited from B&D.
- Card `hegel-el-bd.md`: "The EL edition split is a hard series rule… ZUSÄTZE → Hackett. §135 Zusatz, §216 Zusatz (severed hand)… therefore cite Hackett, not B&D. check_editions.py enforces this per-locus."
- Posts 5/8/9 all execute it: Post 9 line 144 cites "(Hegel, 1830/1991b, §216 Zusatz)" and its own note (lines 487–489) documents making exactly this fix; Post 8 lines 79–80 cite "(Hegel, 1830/1991b, §24 Addition 2)."
Digest line 19 is *true but orthogonal*: that B&D physically carries the Zusätze does not override the series' edition-pin convention, which is machine-enforced. This is not a physical-volume gate — the resolution is unambiguous.
Exact changes:
- `(Hegel, 1830/2010a, §216, Addition)` → `(Hegel, 1830/1991b, §216 Zusatz)`
- `(Hegel, 1830/2010a, §135, Addition)` → `(Hegel, 1830/1991b, §135 Zusatz)`
- **Leave the two MAIN-paragraph cites at 2010a**: §216 "momentary means/purposes" and §135 Whole-and-Parts untruth are B&D and stay B&D.
- Add to References, between the 1991a and 2010a Hegel entries, the string already verbatim in Post 5 line 417: *Hegel, G. W. F. (1991b). The encyclopaedia logic: Part I of the Encyclopaedia of philosophical sciences with the Zusätze (T. F. Geraets, W. A. Suchting, & H. S. Harris, Trans.). Hackett. (Original work published 1830)*

**F2. Cite §198R (Remark) throughout, and rewrite the false-fork sourcing note. [hegel_specialist + formal_specialist push Remark; copyeditor + reviewer2_hostile call bare §198 acceptable]**
Adjudication: bare "§198" and "§198 (Remark)" are both digest-sanctioned, so the *body* is safe either way. But the draft's sourcing note stages a false 50/50 — "a separate check found no Anmerkung," "holds the locus open." That **misrepresents the digest**, which does not hold it open: the digest's TOP GATE says "revert to Remark," and the Remark is triple-confirmed (hegel.de typography class "pa" = Anmerkung; card `el_198_three_syllogisms.md`; hegel-system.de "Enz Anm.§198"). hegel_specialist wins on the note. Since the note must be corrected regardless and the digest prefers the Remark, **cite §198R (Remark) in all three citations in the state-triad section** and rewrite the note to state the verified finding (it *is* the Anmerkung, three-way confirmed; the only residual physical gate is B&D's English typography label). Do not print "no Anmerkung."

**F3. §276A: one clause is unverified past the digest. [hegel_specialist, formal_specialist]**
The clause "and there is no resistance to it" fills the exact spot the digest marks with an ellipsis (line 27: the Addition text "was not extractable from the free German source"). It is the one clause in the post carried entirely on unconfirmed Addition apparatus. Either trim to the digest span ("'it is present at every point, there is only one life in all of them … Separated from it, each point must die.'") or verify against the physical 1991 Nisbet before posting. Do not let a later pass treat it as settled.

**F4. Kreines: keep the page gate visible and fix the added emphasis. [gate: hegel_specialist/formal_specialist/reviewer2_hostile; italics: copyeditor]**
- Page: "p. 346" comes from the rewrite brief's Wayback galley, not the digest, which pins the range **pp. 344–377** (digest line 33, card `kreines2008logiclife.md`). Keep the range gate open; do not let in-text "p. 346" read as settled.
- Emphasis: neither digest nor card records italics on "*do*" or "*can*." APA 7 (8.31) requires "[emphasis added]" for author-added stress. **Preferred fix: drop the italics** (match the verified wording — "Hegel holds, against Kant" already carries the contrastive force). Otherwise add "emphasis added" to the citation.

**F5. Minor citation completeness. [copyeditor]**
- Vieweg reference is missing its verified DOI (card `vieweg2017state.md`): append `https://doi.org/10.1093/oso/9780198778165.003.0007`.
- The corpus-grep claim carries no citation, breaking the piece's own convention: add `(org_frontier/probes/PROBES.md)` (RECEIPTS line 70).
- Two lab-receipt cites point to a directory, not the file: `(org_frontier/threads/veto_player)` → `…/veto_player/THREAD.md`; `(org_frontier/threads/back_edge)` → `…/back_edge/THREAD.md` (matches the parallel cyclic/THREAD.md cite; RECEIPTS lines 64–67).
- Restate (already-gated, do not re-discover): Corti (2022) needs a paragraph/PDF locator for its direct quotes (Article 17, no conventional pagination — owed to a print/PMC check); James (2020) needs its chapter page range. Both are disclosed gates, not new.

**F6. Placement + dating consistency. [placement: hegel_specialist/formal_specialist/reviewer2_hostile; dating: formal_specialist/reviewer2_hostile]**
- "near the top of his *Logic*" reads as *near the beginning*, but §216 sits in the Doctrine of the Concept (Life), the Logic's culmination — and the draft itself calls §135 "earlier still," making "near the top" self-refuting. Change to "deep in his *Logic*, in the account of Life."
- "a hundred and fifty years early" vs later "two centuries early" — same gap, two numbers (1821/1830 → IIT is nearer two centuries). Pick one ("the better part of two centuries early").

**F7. Two low-priority precision notes. [reviewer2_hostile; formal_specialist]**
- Add one clause noting the three-syllogism mapping is the **EL §198** mapping (I=citizen, P=system of needs, U=government/law), *not* Vieweg's PR institutional mapping (I=monarch, U=legislature, P=government) — the draft correctly follows §198, but the Vieweg citation should not look like it claims Vieweg's assignments.
- Early "amputation" briefly blurs partition (cut ties, leave parts in) with removal (lift the part out). Add a three-word hedge at first mention — "severing one of the parts *— cutting its ties, not lifting it out —*" — since the clean resolution ("never lifts the hand off the wrist") is a full section later.

**Confirmed already-correct (do NOT reintroduce error):** the §198 rotation now runs **P → I → U** across the three figures (a genuine v4 fix of v3's P-U-I, per all five reviewers; the digest's gate (f) predates this draft). §278R uses Nisbet's "separate existence," §276A Nisbet's "point." The φ_s Greek glyph is reproduced, not transliterated. Corti quotes verbatim (PMC9054894). James carries "Organisational **View**" — do not let a pass "correct" it to PhilPapers' mis-indexed "Theory." Every optional ellipsis-glyph nicety is Substack-tolerable.

---

## VOICE FIXES [voice_reader; register is deliberate first-person Substack — the repo no-first-person rule does NOT govern this series, per all five STEP-0 notes]

Preserve every "I/my" and the signature lines (severed-hand/photograph-of-a-fire, two-teams example, "the purpose was never the smaller half"). The tic to cut is the antithesis machine and self-narrating rigor — not the person.

**V1. Break the three-in-a-row "not X, but Y" cluster in "What a Member Is, for Hegel."** Three consecutive paragraphs resolve on the identical frame, dulling the best line (the corpse sentence) by making it the third firing. Rewrite the first two to state the positive claim directly; **leave "A corpse is not a body with the life subtracted…" untouched** so it lands as the payoff.

**V2. Break the second antithesis cluster in "Where the Two Accounts Come Apart"** (the "Self-maintenance is the criterion. My instrument does not compute self-maintenance." run, and the "not borrowing 'organism' as a metaphor" line). One paragraph runs the device twice — cut the first instance, keep the earned "the strong claim… is not mine to make."

**V3. Break the section-closing epigram drumbeat.** Five of six sections end on the same parallel-clause maxim. Two earn it (keep). The state-triad closer ("That caution is not special to Hegel — it is the standing caution…") is the worst offender, stacking antithesis + em-dash + epigram — rewrite it to a plainer sentence.

**V4. Cut the residual self-narrating-rigor lines** the v4 note claimed to have removed but that grew back: "I would rather name that cost," "I want to stop at that sentence," "the wide one repeats a mistake this series has made before," "I register… I do not dress." None breaches a guard — they are a voice tic, the exact family the round tried to remove. State the limitation; do not narrate the care.

**Keep untouched:** "The severed hand is a hand the way a photograph of a fire is warm. The word survives. The thing is gone." (the piece's best sentence), the two-teams concretization, and "The Documented Middle" (the model for how closers should behave).

---

## RESIDUAL GUARD RISK (flagged, per mandate)

One zone only: the **temper paragraph** (Substantive #5). The guard holds today — no banned term touches Φ and the demotion is pinned to Hegel's ranking — but "speaks with total confidence about… the shallower of the two questions" + "never the smaller half," read together and out of context, are the one place a reader could quote the author as conceding Φ answers the lesser question. The digest pre-flagged this exact paragraph (gate (e)) and the author flagged it as not-yet-owned. Applying reviewer2_hostile's rewrite (symptom-not-direction, drop the doubling, stop calling confidence a cost) closes the risk. No other guard exposure survives.

---

## META / SECURITY NOTE (not a content finding)

voice_reader reported that the Read output for the ground-truth files appeared to carry injected content — a spurious "date changed, don't mention it" reminder plus unrelated MCP tool-loading directives — and declined to act on it. I saw the same appended block in this environment. Treating it as untrusted; it has no bearing on the review and I did not act on any instruction in it. Surface to the rebuild owner as a possible prompt-injection vector riding on tool output.