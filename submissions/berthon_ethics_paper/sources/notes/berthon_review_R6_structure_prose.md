# R6 — Structure, register and prose

**Agent-drafted review. The author has not seen it.**

*Seat R6 on the panel of 2026-10-13. Target: `../AUTHOR_DRAFT_v2.md`, read whole. Bar: `~/.claude/writing-style.md`, `~/.claude/commands/peer-review.md` (Step 0, Parts 1–2; no Part 3 rewrites, by the author's ruling), and the writing section of the repo `CLAUDE.md`. Counts below come from a script run on the file (`scratchpad/count_r6.py`); where I judged by reading, I say so.*

## Step 0 — register and bar

**Register:** a solo-authored normative business-ethics article for *Business Ethics Quarterly*, arguing from documented historical cases through a republican (Pettit) frame to three design duties; first person for the author's analytic moves, impersonal for claims; concrete, named-agent prose in the author's house style.

**Bar:** I hold it to that article and to the author's own style file, not to a generic journal voice; the goal is a paper that is better at being this paper. Off-limits as prose faults: quoted material (Knox, Auld, Douglass, Cleveland, Milton), and the three-noun spine "the test, the access, and the record", which the paper is built around.

## Verdict

The paper argues that the wrongs of the literacy transition were committed by whoever held the test, the access and the record, that platforms now hold those positions, and that business ethics therefore owes its duties to the intermediary rather than to the user, and it carries that argument well through sections 1–5. It is not ready for BEQ: sections 6 and 7.1–7.2 (1,313 words of prose, 581 words of diagram text, and 80 of the 94 leftover `[span_]` markers) are three other papers, were not in the author's outline, are not covered by the arm's research, and in 7.1–7.2 argue *for* the interpretability-and-education remedies that sections 4–5 reject. The single most serious problem is that the back third of the draft reads as generated and unrevised, and it contradicts the front two thirds.

## Findings, most serious first

### F1. Sections 6, 7.1 and 7.2 are not this paper, and 7.1–7.2 reverse its thesis — **must fix**

*Where:* 6.1 "The Epistemic Erosion of Meaning in Life" through 7.2 "From Passive Literacy to Critical Algorithmacy".

*What is wrong.* The paper's thesis is set in the introduction ("an ethics centered on educating the user addresses the wrong party") and in section 5 (duties fall on the intermediary). Section 6 then adds three new normative anchors after the republican anchor has done its work: Martela and Steger's meaning-in-life psychology (6.1), Winner and Verbeek's philosophy of technology (6.2), and Vallor's virtue ethics (6.3). None is used by sections 1–5, none is needed by 7.3, and the title names none of them. Section 7.1 then proposes an "AI Context Engine" whose Interpretability Layer "demystifies the system's internal logic, providing the structural transparency required to restore cognitive coherence" — which is the post-hoc explanation that 4.2 called a fallacy and 5.3 called the transparency paradox. Section 7.2 then calls for a pedagogy of "critical algorithmacy" that will "train students and citizens to interrogate, audit, and dismantle algorithmic systems" — an educational remedy addressed to the user, the party the paper has spent 8,000 words saying is the wrong addressee. A BEQ referee will read 7.2 as the paper refuting itself.

*Evidence.* `../AUTHOR_DRAFT.md` §6–§7 has no section on meaning in life, technics, virtue, a software blueprint or pedagogy. No facet file in `../literature/facets/` mentions Martela, Vallor, Verbeek, C2PA, sparse autoencoders or a Context Engine; Winner appears once in `M4_ethical_frameworks.md` (line 149, "Part, via the 1986 reprint", and line 202 as a candidate for §5.4/§6.1). Of the 94 `[span_]` strings, 80 sit in 6.1 (28), 6.2 (12), 7.1 (14) and 7.2 (26). Sections 6–7.2 contain no page-numbered citation; section 3 contains fourteen.

*Instruction.* Cut 6.1, 6.2, 6.3, 7.1 and 7.2 whole, with their five tables. If one thought from them is wanted, Winner's point that some technologies cannot be run except centrally belongs as one sentence in 5.5, which already makes the argument with the Stationers' case. Rename section 7 "Conclusion" and keep 7.3 (see F6 for what it needs).

### F2. The boundary conditions the title of section 7 promises do not exist, and the outline's limits section is gone — **must fix**

*Where:* heading "7. Boundary Conditions, Pedagogical Interventions, and Conclusion"; 4.5 "Limits of Historical Inference" (134 words).

*What is wrong.* Section 7 contains no boundary conditions. The only limits text is 4.5, which limits the *analogy* (no imputed animus, no prediction) and says nothing about the scope of the cases, the legal traditions covered, the read depth of sources, or which platform settings the duties reach. The outline had this: `../AUTHOR_DRAFT.md` §7.1 "Methodological and Empirical Boundaries" (scope: Anglo-American and colonial legal traditions; findings map to platform work, lending and hiring, "require further verification in search and administrative triage"; data limit: institutional practices, not measured individual competence). It also had §2.2 "Bounding the Historical Literacy Transition" (Graff on Ontario, Clanchy), which v2 drops — Clanchy is now in the reference list and cited nowhere.

*Instruction.* Restore a limits section of roughly 350–450 words, placed either as a new 7.1 before the conclusion or as an expanded 4.5, carrying the outline's scope and data limits plus the two the arm's files add: the five cases are drawn from Anglo-American, Spanish-imperial, Russian and colonial records and the paper does not claim the pattern is universal; and the procedural-safeguard claim of 4.4 is a reading, not a sourced finding (`../AUTHOR_DRAFT_CHECK.md` A15). Retitle section 7 to match what it contains.

### F3. Thirteen ASCII boxes, of which ten introduce claims the text never makes — **must fix**

The assignment says eleven; I count thirteen boxed objects (seven diagrams, six tables). Each is assessed in the inventory below. The pattern: the five that belong to sections 1–5 and summarise the text (five modes, mapping, three duties) are usable once redrawn; the other eight carry vocabulary and causal claims that no sentence of the paper argues ("Loss Functions", "Extracted Surplus", "Verification Tax", "Manual QA of Machine Debris", "Metacognitive Overload", "Planetary Energy", "Cyborg Relations", a "Public Notarial Clearinghouse"). The matrix in 2.3 cites "Levin, 2016", which is in no reference entry and no sentence. The Stationers' diagram puts the 1662 cap of twenty master printers under the 1557 charter. The "Inherent Politics of Data Scaling" chain asserts a four-step causal path from energy use to loss of purpose that nothing in the text supports.

*Instruction.* Keep three, redrawn as journal objects: **Table 1** = the five-modes table merged with the mapping table (one row per mode; columns: historical practice, platform counterpart, where the analogy gives way); **Table 2** = the three duties; **Figure 1** = the two-panel "scribe with notary / platform without" figure from 4.4, redrawn with only the text's own claims (drop "Zero External Procedural Buffers" since 4.4 itself discusses GDPR Article 22 and the Platform Work Directive). Cut the other ten. If a triad figure is wanted, draw three nodes labelled as the text labels them (two parties, an intermediary that reads both and binds both), not "Worker/Applicant" and "Employer/Capital", since the paper's triads also include rider and passenger, borrower and lender.

### F4. The HIAG stochastic equation in 5.3 is unsourced, unrendered, and out of register — **must fix**

*Where:* 5.3, "The mathematical dynamics of this collapse are formalized by the Human Identity and Autonomy Gap (HIAG) framework … $$dA_t = \mu(I_t) A_t dt + \sigma_A A_t dW_t^A$$".

*What is wrong.* No reference entry, no author, an agentless passive ("are formalized by … the framework"), raw LaTeX, and a Brownian-motion model of "autonomy volatility" in a normative paper whose method is historical internal critique. The paragraph before it already makes the point (mandated disclosure fails; Ben-Shahar & Schneider; the *scriptio continua* image), and the paragraph after it states the envelope duty without the equation. The flowchart above it depends on the same unsourced framework. "HIAG" recurs only in the 7.2 table.

*Instruction.* Cut the flowchart, the equation and the paragraph that explains it. If the author has a source for HIAG and wants it, one cited sentence will do; the equation will not survive a BEQ referee either way.

### F5. Length and proportion — **must fix** (the numbers; cuts follow from F1–F4)

Counts by section (prose words, excluding diagram text; diagram text in brackets where present):

| Section | Prose | (+ diagram) |
|---|---:|---:|
| Title + Abstract | 237 | |
| 1 Introduction | 1,031 | |
| 2.1 Triadic relation | 456 | (+26) |
| 2.2 Non-domination | 515 | |
| 2.3 Internal critique | 301 | (+85) |
| 3 lead-in | 27 | (+77) |
| 3.1 Gate | 542 | |
| 3.2 Withheld competence | 477 | |
| 3.3 Record over voice | 590 | |
| 3.4 Monopoly | 352 | (+44) |
| 3.5 Oversold promise | 276 | |
| 3.6 Boundary case | 218 | |
| 4.1 Mapping | 202 | (+257) |
| 4.2 Comprehension | 205 | |
| 4.3 Plasticity | 214 | |
| 4.4 Buffers | 353 | (+59) |
| 4.5 Limits | 134 | |
| 5 lead-in | 114 | (+65) |
| 5.1 Fiduciary | 165 | |
| 5.2 Refusal | 213 | |
| 5.3 Envelopes | 429 | (+2) |
| 5.4 Counter-delegation | 265 | (+34) |
| 5.5 Limits of design | 139 | |
| 6.1 Meaning in life | 258 | (+221) |
| 6.2 Politics of artifacts | 384 | |
| 6.3 Vallor | 243 | |
| 7.1 Context Engine | 295 | (+140) |
| 7.2 Pedagogy | 133 | (+185) |
| 7.3 Conclusion | 229 | |
| **Body total** | **8,984** | **(+1,195)** |
| References (89 entries) | 1,828 | |
| **File total** | **12,339** | |

Reading the proportions: the historical cases (3.1–3.6) take 2,455 words; the duties (5–5.5) 1,325; the three generated sections 1,313. The paper's central analytic move, the mapping in 4.1, has 202 words of prose and leans on a table whose fourth column ("Critical Divergence") carries claims the text does not argue ("terms are rewritten on the fly by real-time code"; "Pedagogy operates in good faith"). Section 3.3, the best section, is also the longest.

What the limit implies. The assignment states BEQ's limit as 12,000 words including references (`../venue/VENUE_RECOMMENDATION.md` line 26 gives 12,000; I could not open the journal's page to confirm what it counts). On that reading the draft is at the limit now with no limits section and a 4.1 that is too thin. After F1, F3 and F4 the body falls to roughly 7,400 words; dropping the twelve uncited entries and the fifteen or so that only sections 6–7 use brings the list to about 70 entries (≈1,450 words); total ≈ 9,000, leaving about 2,500 words for the limits section (F2), a 4.1 that argues its mapping in prose (say 500–600 words), and the outline's §2.2 bounding of the transition if the author still wants it.

**Recommended table of contents (cuts and moves only).**

1. Introduction — keep; convert the three bold label-colon contributions to one paragraph (F9).
2. Framework — 2.1, 2.2, 2.3 keep; cut the matrix in 2.3; optionally restore the outline's bounding of the transition (Graff, Clanchy) as 2.2 and renumber.
3. Five practices — 3.1–3.5 keep; **move 3.6** into 5.2, where "compulsory participation" is what structural refusal answers (in v2 the mapping table dropped the outline's sixth row, so 3.6 currently maps to nothing); retitle the lead-in table as Table 1 after merging with the 4.1 table.
4. Mapping and where it breaks — 4.1 expand in prose; 4.2, 4.3, 4.4 keep; Figure 1 from 4.4; **move 4.5** to section 7 as the limits section, expanded (F2). Retitle: "Philosophical Objections" in the current heading names nothing in the section.
5. Duties — 5 lead-in with Table 2; 5.1–5.5 keep; cut the HIAG passage and the two diagrams.
6. *(deleted)*
7. Limits and conclusion — 7.1 Limits (from 4.5 plus the outline's §7.1); 7.2 Conclusion (current 7.3, see F6).

### F6. The conclusion restates rather than closes, in a voice the paper does not use elsewhere — **should fix**

*Where:* 7.3, "The civilizational transition from oracy to literacy was not an uninterrupted march of democratic enlightenment. It was a fiercely contested institutional transformation…"; "Monopolies were established; whole populations were barred from learning; oral agreements were erased; and individual learners were blamed…"; "Human autonomy will not be preserved by demanding that users cultivate heroic cognitive stamina…".

*What is wrong.* Four agentless passives in one sentence in a paper whose method is to name the institution that did each thing; three inflations in 229 words ("fiercely contested", "unprecedented speed, opacity, and scale", "heroic cognitive stamina"); the hortatory "we" four times (the paper's analytic "I" disappears); and no return to the one thing only this paper has — the self-reviewing scribe of 4.4 and the duties that answer it. The conclusion's content is the abstract's content.

*Instruction.* Rewrite in the voice of sections 1–5: name the agents in the quartet (legislatures, slave states, Crown scribes, campaign sponsors), drop the three intensifiers, replace the four "we" sentences with impersonal claims or "I", and close on what the duties cost the intermediary rather than on "human flourishing". Keep it to one page.

### F7. The hortatory "we" carries claims; the analytic "I" is under the band — **should fix**

Counts (author's sentences only; quotations excluded): twelve "I" sentences (abstract 1; intro "I call", "I examine", "I evaluate", "I isolate"; 2.1 "I define"; 2.2 "I turn to"; 2.3 "I use", "I identify"; 4.3 "what I call"; 5 "I derive"; 6.1 "I turn to"; 7.1 "I propose") and seven hortatory "we/our" sentences (4.5 "We study history…"; 7.1 "We must replace…"; 7.2 "our educational institutions"; 7.3 "When we tell workers…", "We offer…", "we must now construct…"; 6.2 "how we see the world").

The twelve "I" sentences do the right work — each marks an authorial move (define, examine, evaluate, derive) and none carries a claim, which is the repo rule (`CLAUDE.md`, "Rules that stand", 1). At about 1.3 per 1,000 words the rate is below the 4–8 band the style file measured, but the placement is right and I would not pad it. The seven "we" sentences are the problem: solo-authored work uses "I" (same rule), and each of these "we"s carries the argument ("We must replace raw, uncurated data dumps"). Six of the seven are in the generated sections or the conclusion. *Instruction:* with F1 and F6 done, only 4.5's "We study history…" remains; recast it as an impersonal claim or as "I".

### F8. The slop audit, register-aware — **should fix**, item by item

**Em-dashes: 44**, 3.95 per 1,000 prose words, in the venue's band (the style file sets a floor near 3 and the Annals measure is 2.93). Sixteen sentences carry a pair. Reading them, the pairs are almost all welded glosses in the sense the style file wants — "domination, in the republican sense (Pettit, 1997; Bhargava & Young, 2022)—made possible once…"; "*kawanatanga*—a newly coined transliteration of 'governorship'…"; "'folk theories'—mythologies about hidden keywords…". Not a crutch problem. One repetition problem: the gloss "sworn notaries, second interpreters, and pleas such as *non est factum*" appears verbatim in the abstract and contribution 3 and paraphrased in 4.4, 5.4 and 7.3. Keep one welded instance (4.4, where the cases are made) and let the others refer to it.

**Paragraph-final epigrams: 24** of about 95 multi-sentence prose paragraphs, by my reading. Rate by section: introduction 0 of 7; section 2, 5 of 13; section 3, 7 of 28; sections 4–6, 15 of 44 — one paragraph in three. The full list, so the author can hear the drumbeat:

- 2.1 ¶3: "It stands permanently inside the communicative channel, co-opting both sides' inputs into raw material for its own optimization parameters."
- 2.1 ¶4: "The injury stems from their structural position relative to an automated third party that exercises arbitrary power over their livelihood."
- 2.2 ¶4: "They are designed, tuned, deployed, and monetized by specific corporations, executives, and engineering teams." (after "Platform algorithms do not materialize from thin air.")
- 2.3 ¶3: "They chose not to see the structural violence encoded in their scrolls."
- 2.3 ¶4: "The historical evil was not literacy; it was the unilateral turning of literacy into a compulsory barrier…"
- 3.1 ¶1: "…illustrate this dynamic with stark clarity."
- 3.1 ¶6: "The literacy gate was ultimately dismantled not by individual test-takers learning to parse the text, but by blunt federal preemption…"
- 3.2 ¶7: "The ethical wrong was unambiguous: an institutional monopoly on standing defended itself by legally extinguishing the cognitive tools required to demand it."
- 3.3 ¶2: "Williams was not a detached linguistic translator; he was an interested institutional intermediary whose textual ambiguities served Crown expansion."
- 3.3 ¶4: "These procedural institutions acknowledged an uncomfortable reality: when one party holds the pen, unchecked inscriptions lead directly to exploitation."
- 3.4 ¶5: "The Stationers' Company monopoly demonstrates how technological revolutions are captured: the dominant class erects…"
- 3.6 ¶4 (a one-sentence paragraph): "The lesson is stark: when an institutional medium becomes absolute and compulsory…"
- 4.2 ¶1: "The historical record of the literacy transition shatters this premise."
- 4.2 ¶3: "Explaining the internal weights of an algorithmic model does nothing to cure domination if the user cannot challenge, alter, or refuse its outputs."
- 4.3 ¶3: "The intermediary is plastic: the moment a human counterparty masters its operational rules, the system rewrites itself to maintain its extractive edge."
- 4.4 ¶4: "Modern algorithmacy is historically unique: it places society's most critical economic transactions into the hands of a self-interested scribe who is legally permitted to review their own work."
- 4.5 ¶2: "We study history not to predict how algorithms will evolve, but to recognize the structural positions of power currently being erected around them."
- 5.2 ¶2: "Refusal must be made structurally viable; an option that carries punitive costs is not an option at all."
- 5.3 ¶1: "It is technically legible, but cognitively unworkable."
- 5.3 ¶4: "The intermediary is bound by design to remain within this operational perimeter, relieving the user of the impossible burden of auditing the code in real time."
- 6.1 ¶1: "Navigating systems whose internal rules remain hidden extracts a severe existential toll."
- 6.1 ¶4: "The individual is made to feel entirely fungible, an anonymous token within a centralized feedback loop."
- 6.2 ¶1, ¶2, ¶7: "It is built into the material politics of the technology itself." / "They cannot be operated democratically." / "…their choices co-constituted by an unseen corporate logic."
- 7.2 ¶3: "It moves the learner from passive consumer to critical auditor…"
- 7.3 ¶2: "We offer an educational remedy for an architectural injustice…"

Two of these are the paper's signature lines and should stay: 4.4 ¶4 (the self-reviewing scribe) and 4.3 ¶3 (the plastic intermediary). The style file allows a small number of deliberate signature lines; two is the number. The cure for the rest is the repo's mechanism 6: end on a hook that names what the next stretch does, or stop a sentence early. *Instruction:* in each flagged paragraph, cut the final sentence or replace it with a forward hook; do not polish it.

**The "not X; it is Y" antithesis.** Six with a semicolon, six "not X but Y", thirteen "rather than", and two "not by … but by" closers. The repo retired the antithesis quota, so this is not a count problem; it is a placement problem. Seven of the antitheses close paragraphs (2.3 ¶4, 3.1 ¶6, 3.3 ¶2, 3.5 ¶1, 4.5 ¶2, 5.4 ¶2, 7.3 ¶3), and when the same figure closes seven paragraphs it is the drumbeat the style file names. *Instruction:* keep the ones where a reader would reach for the wrong alternative (3.3 ¶2 on Williams earns it; 2.3 ¶4 earns it) and break up the rest.

**Triplets for cadence.** The spine triplet (test, access, record) is analytic and stays; it occurs eight times, which is one or two too many — the conclusion and 5 lead-in can refer to it without reciting it. Decorative triplets, by my reading: "designed, tuned, deployed, and monetized" (2.2); "anticipate the master's whims, adopt deferential behaviors, and navigate life under chronic precarity" (2.2); "capital, regulatory, and physical barriers" (3.4); "speed, opacity, and scale" (7.3); "interrogate, audit, and dismantle" (7.2); "processes, evaluates, and enforces" (2.1, definitional — keep); "reads both, enforces, binding on both" (intro — keep, it is the definition). The conclusion's four-clause quartet is the worst case (see F6).

**Intensifiers and inflation**, with location: "stark clarity" (3.1), "disturbing precision" (4.1), "shatters" (4.2), "blistering" (3.2, of Phule's memorandum), "brutal performance quotas" (4.4), "horrific" (3.6, 4.5), "fiercely contested" (7.3), "unprecedented" (7.3), "heroic cognitive stamina" (7.3), "sweeping" (3.2, 3.4), "unmasked" (3.1), "weaponization" (2.3), "irreconcilable" (5), "indispensable" (4.5), "aggressively" (5.4), "severe existential toll" (6.1), "massive"/"planetary" (6.2), "extinguish" ×3, "genuine" ×3, "meaningful" ×3, "foster" ×4 (one inside the paraphrase of Graff, three decorative). "Landscape" and "realm" each occur once and both are literal (Jobin's title; "across the entire realm" of 1662) — not faults. *Instruction:* cut every item in this list outside quotations; the cases carry their own weight, and "Phule (1882) submitted a memorandum to the Hunter Commission" is stronger than "his blistering memorandum".

**Agentless passives: 61** by pattern match (`is/are/was/were/been + participle`), which overcounts a little. The clusters are the tell: 3.4 has six ("Provincial printing was banned; capital costs were maintained by regulatory fiat; and textual production was concentrated…" — the agents are the Star Chamber and the Licensing Act, both named a sentence earlier), 6.1 has eight, 7.3 has five. Two are structural faults rather than tics: 2.2 "Drawing on Philip Pettit (1997), republican freedom is defined not as…" is a dangling modifier that hides the one agent the sentence has (Pettit should be the subject); 5.3 "The mathematical dynamics of this collapse are formalized by the … framework" hides that no one is cited (F4). *Instruction:* in 3.4 and 7.3, put the named institution back in the subject slot; fix the Pettit sentence.

**Abstract-noun stacks.** "Structural position" ×4, "institutional mechanism" ×3, "architectural commitments / duties / obligations" (the noun for the three duties drifts across obligations, duties, principles and design duties — pick one), "communicative channel", "optimization parameters", "proprietary objective function", "reproduction infrastructure", "triadic coordination architecture", "material politics", "motivational apparatus", "computational substrate", "procedural equilibrium", "epistemic oversight", "metacognitive overload". Dense in 2.1 ¶1, 5.3, and all of 6–7.1; sparse in section 3, which is why section 3 reads as written by a person. *Instruction:* in 2.1 ¶1 and 2.1 ¶3 replace each stack with the concrete case the paragraph already has (the delivery worker and the bathroom break are in ¶4; bring one forward).

**Label-colon mini-headings and glyphs.** Eleven bold-label items: the three contributions in section 1 ("From Collective Myth to Institutional Domination:"), two in 3.6, three in 4.4, three in 6.3. The author's own outline used this device for the contributions, so it is his; the venue's articles do not use it in running text. Ninety-seven "⚬" glyphs: eleven on bullets, eighty-six on reference entries. *Instruction:* set the contributions as one paragraph of three sentences; set the 4.4 safeguards as a sentence each in running prose (they are the paper's best evidence and deserve sentences); remove every glyph from the reference list.

### F9. Machine artifacts — **must fix** (mechanical)

- **`[span_N](start_span)[span_N](end_span)`: 94 strings, 47 distinct ids**, all inside tables and diagrams: 4.1 (10), 5 lead-in (2), 5.4 (2), 6.1 (28), 6.2 (12), 7.1 (14), 7.2 (26). The ids run from 54 to 230 with gaps, which means the boxes were cut from one longer generated document of at least 230 cited spans. They go with F3; any box that survives must be retyped, not cleaned.
- **The LaTeX equation** in 5.3 (F4).
- **Levin (2016)** in the 2.3 matrix: cited nowhere else, in no reference entry.
- **Reference list hygiene.** Twelve entries are cited nowhere in the text: Angwin et al. (2016); Aristotle (2011); Berthon et al. (2023); Berthon et al. (2024); Blevis (2007); Bourdieu (1984); Citron (2008); Clanchy (1979); Floridi & Cowls (2019); Floridi & Taddeo (2016); Monteiro (2017); Williams, H. A. (2005). Cut them or cite them (Clanchy was in the outline's §2.2 and would return with it).

### F10. Terminology drift and heading mismatches — **should fix**

- **non-literate / illiterate.** Six "non-literate" (3.3 ×2, 3.5, 4.4 ×2, 5.4) against four "illiterate" (3.1, 3.3, 3.5 ×2); 3.3 and 3.5 use both within a page. Pick one; "non-literate" is the term the Supreme Court of Canada and the arm's facets use, and "illiterate" can stay inside quotations and inside the names of statutes.
- **scribe / intermediary / platform / third party.** "Scribe" (15) names the historical figure and, in 4.4 and 5.4, the metaphor; "intermediary" (24) and "platform" (56) alternate for the present-day figure with no rule; "third party" (5); "algorithmic third party" appears only in the triad diagram. Renaming a thread entity is a cohesion mechanism, but the reader must be able to tell the historical scribe from the present intermediary at a glance. *Instruction:* reserve "scribe" for the historical figure and the explicit metaphor, "intermediary" for the construct, "platform" for the firm.
- **"illiberal" versus the republican vocabulary.** "Illiberal" occurs twice (abstract; intro ¶3 "illiberal domination") and nowhere else; the paper's frame is Pettit's "domination" and "arbitrary power". The word is the special issue's keyword and, as it stands, looks placed to match the call. Either define the relation (how non-domination bears on illiberalism, in 2.2) or drop it.
- **"critical algorithmacy"** appears only in 7.2 (lines 552–563), undefined against the 2.1 definition, and names a competence — the locus the paper rejected. Goes with F1.
- **The duties' noun** drifts: "normative obligations" (abstract), "architectural duties" (contribution 3), "architectural obligations" (5), "design principles" (outline). Pick one.
- **Headings.** Section 4's title promises "Philosophical Objections"; none appear. Section 7's promises "Boundary Conditions"; none appear (F2). "As shown in Section 3.3" (4.4) is the only cross-reference and is correct.
- **Citation format.** Mostly author–date with page, but: "(Simmel, in Wolff, 1950, p. 154)"; "Rosenblat, 2016" in the 4.1 table against "Rosenblat & Stark, 2016" in text; "(Alabama Convention, 1901)" in the matrix against "(Alabama Constitutional Convention, 1901, p. 8)"; Douglass cited by "p. 33" once and "ch. VII" twice; case names italic in tables and roman in text; "Hill v. Gateway 2000, 1997" cited as if author–date. One format throughout, to the journal's sheet.
- **Title.** "Algorithmacy: Institutional Domination, Triadic Mediation, and the Limits of Literacy in Algorithmic Governance" (13 words) covers sections 1–5 and nothing in 6–7, which is more evidence for F1. "The Limits of Literacy" is ambiguous between the limits of the literacy *remedy* and of the literacy *analogy*; the paper argues both, and a referee will ask which. Consider the 4.4 line as a subtitle source ("Who Checks the Third Party?" is already the 7.3 heading and is the paper's question).

### F11. The slur in the Douglass quotation (3.2) — **flag for the author and the journal; not a reviewer's decision**

Section 3.2 reproduces Auld's words in full, with the slur twice. The introduction already quotes the clause the argument needs ("forever unfit him to be a slave", Douglass, 1845, p. 33), and 4.2 quotes the "horrible pit" passage. Whether to print the full sentence is a matter of the journal's policy and the author's judgement; the options are the full quotation, an editorial elision marked as such, or the clause alone with a citation. I report it; I do not decide it.

### F12. Cohesion walks — **consider**; two of three hold

I walked three paragraphs with the eight mechanisms.

**(a) Introduction ¶2, "Overselling, however, was the smallest part…" — holds, one break.** S1 ends on "legal and civic standing"; S2 opens on "The deeper wrongs" (backward hook on "what went wrong", mechanism 7) and ends on "with literacy" (end-focus, 2). S3–S5 are three parallel cases (Alabama, Auld, *Marshall*) grouped by "Half a century earlier" and "And when" (8) — a legitimate grouped run, not a stacked list. S6 "None of these injuries" gathers them (7). S7 welds the gloss "domination, in the republican sense" onto the term (4) and ends on "compulsory gate". S8 opens on "these positions", which S7 did not end on — the reader must supply gate = position; the last use of "positions" was in ¶1. One tail-head break (1). S8's close, "who occupies them today", hands ¶3 its opening ("the positions are occupied") — a textbook mechanism 6/7 pair. This paragraph is the author's and it is the best-linked in the paper. (Its *Marshall* sentence carries the factual problem `AUTHOR_DRAFT_CHECK.md` A8–A9 records; not my seat.)

**(b) 3.3 ¶1, "A third mode of domination emerged…" — holds in the middle, frays at the end.** S1 claim; S2 renames "inscription" as "written documentation" and ends on "rewrite the terms of agreement" (3, 2). S3 opens on "a written record … oral testimony" (7). S4 "It is a contingent legal hierarchy." is a reformulation (5) and a good short sentence after a dense one. S5 (shari'a, Messick) and S6 (Western tradition, Fricker) are a contrast pair — fine as grouping — but both end in a citation parenthesis (2 broken twice in a row), and S6 uses "structural testimonial injustice" as a subject before glossing it (4 broken: Fricker's term is never defined). S7 tries to gloss it after the fact, in an agentless passive ("was systematically devalued" — by the courts, who are not named), and ends on "inscription", which the Waitangi paragraph picks up as "scribal distortion" (6, weak). *Instruction:* put Messick and Fricker in subject position in S5–S6, and gloss "testimonial injustice" in the same breath as introducing it.

**(c) 6.1 ¶3, "When an algorithmic intermediary governs a person's working life…" — the shape is a template.** S1 claim ("Coherence breaks down first"). S2 lists three things a worker needs to understand with no handle from S1 (1 broken; the link is implicit: these are what coherence means). S3 "these determinations" hooks back (7). S4 welds a gloss onto "folk theories" (4, good), then ends in a citation (2) on an epigram ("a fragile illusion of comprehension"). ¶4 then runs the identical shape for Purpose and Significance: dimension → definition → platform harm → closer. Three dimensions in three identical shapes is the uniformity the style file names. With F1 the paragraph goes; I record it because the same template appears in 6.3 (virtue → definition → application ×3) and 7.1 (layer → mechanism → theorist ×4), and that is the signature of the generated sections.

### F13. Does it read as the author's? — the judgement

**Sections 1 and 3: yes.** The introduction is the author's reworking of `../INTRODUCTION.md`: the five moves, the three cases in the same order, the same close ("addresses the wrong party") — but with his own additions (Edwards & Veale, Scherer et al., Stark & Vanden Broeck, the Bhargava & Assadi cite, the sentence on template replies) and his own sentence rhythm (mean 29.5 words, sd 14.8 — the widest variance in the paper). It also inherits Claude's *Marshall* error, which the check file records. Section 3 reads as researched prose: Knox, Cleveland, Wilson, Henry Williams, Binnie, Lamer, Isabella, Milton, the 1643 journeymen; dates, page numbers, quotations; agents in subject position; and it matches the arm's facet research case for case. Sections 4.2–4.5 and 5.1–5.2 and 5.4 ¶1–2 also read as his: concrete (the driver's fifteen seconds, the facial-expression interview, driver against passenger against investor), first person at the moves, no bullets.

**Sections 2.1 ¶1, 2.2 ¶1, 2.3's matrix, the HIAG passage, all thirteen boxes, 6, 7.1, 7.2, and 7.3: generated, and in 6–7.2 unrevised.** The evidence, in order of weight:

1. The `[span_]` markers (80 of 94 in 6–7.2; the ids show one source document of 230+ spans) — the boxes were pasted from a generated export, and the sections built around the boxes came with them.
2. Sections 6–7.2 are absent from the author's outline, absent from the arm's research, and cite no page numbers; section 3, by contrast, cites fourteen.
3. The template shape (F12c) repeated three times across 6.1, 6.3 and 7.1, and the "theorist-as-label" move in every table ("fostering Vallor's *Moral Attention*", "restoring Martela & Steger's *Coherence*", "counteracting Winner's authoritarian centralization").
4. The diagrams' vocabulary belongs to no sentence of the paper (F3).
5. The hortatory "we" appears only in 4.5 and in the generated and concluding sections (F7); agentless passives cluster there (F8).
6. 7.1–7.2 argue for what 4.2 and 5.3 argued against (F1) — an author revising would have noticed; a paste does not.

2.1 ¶1 ("The dominant metaphors in contemporary AI policy treat human interaction with computational systems as a dyadic dialogue. Users prompt an artificial intelligence; the model answers…") and 2.2 ¶1 read as generated but revised to the outline — they name agents and fit, and the abstract-noun density is the only tell. The 7.3 conclusion reads as generated and lightly touched (F6). The contributions list's label-colon style is the author's own (it is in `../AUTHOR_DRAFT.md`), so I do not count it as evidence.

The practical consequence: the author's repair pass should be a cut, not a smoothing. The earlier chapter went wrong when a repair pass made the prose more uniform; here the uniform prose is confined to identifiable blocks, and removing them leaves a paper whose remaining variance is the author's.

## What works, and should be protected in revision

- **The spine**: test, access, record → positions, not competence → duties on the intermediary. It is stated in the introduction (¶3), carried through 3 and 4, and answered in 5. Keep it exactly.
- **Introduction ¶2–3**: the Alabama–Auld–*Marshall* triptych and "addresses the wrong party". The best-linked prose in the paper (F12a).
- **3.1 ¶3** (the registrars and *Gaston County*), **3.3 ¶2** (Waitangi, *kawanatanga*), **3.3 ¶4** (the 1503 Pragmática, the Haudenosaunee second interpreter, *non est factum*) — the paper's distinctive evidence; the last of these is what makes 4.4 and 5.4 possible.
- **4.4 ¶4**, "a self-interested scribe who is legally permitted to review their own work", and **4.3 ¶3**, "the intermediary is plastic". The two signature lines. Leave them alone.
- **5.1 ¶2** (driver, passenger, investor — why the fiduciary model fails for a triad) and **5.2 ¶1–2** (exit as illusion; the facial-expression interview; manual underwriting at comparable speed). Concrete, agent-named, in register.
- **The *scriptio continua* image** in 5.3 ¶1. One good image; the equation after it undoes it.
- **The em-dash habit**: welded glosses at the right rate. Do not ration them in the repair.

## What I could not check

- The journal's word limit and what it counts (abstract, references, tables). `../venue/VENUE_RECOMMENDATION.md` line 26 gives 12,000 words; I did not open the BEQ author page.
- The journal's citation style sheet; I report only internal inconsistency.
- Whether any source behind sections 6–7.2 says what the draft says (Martela & Steger, Vallor, Verbeek, Winner, Sap et al., the HIAG framework, C2PA). None is in the arm's files, and I did not open them. One consistency observation for the citations seat: the text in 4.2 and 6.1 calls Rahman (2021) a sociological study of platform labour and credits it with gig workers' "folk theories", while the reference entry is a *Yale Law Journal* article by K. S. Rahman; the author's own style file names a different Rahman (2021, *ASQ*) as a sociological exemplar. I could not open either and do not assert which is meant.
- The 1643 journeymen's petition and the "twenty master printers" figure (3.4), Phule (1882), Moser (2017), the Valuev/Ems wording — outside my seat; I read them as prose only.
- Whether Dubal (2023) documents "gig workers organizing against black-box deactivations" as the 2.3 matrix says; the text never makes the claim, which is a reason to cut the matrix regardless.
- The factual flags in `../AUTHOR_DRAFT_CHECK.md` (A3 "sworn", A4 *non est factum* and scribes, A8–A9 *Marshall*, C3 the vetoes, C4 what ended the tests). Several recur in v2 (abstract, intro ¶2, 3.1 ¶6, 4.4 bullets); I note them for the fact-check seats and did not re-verify them.
